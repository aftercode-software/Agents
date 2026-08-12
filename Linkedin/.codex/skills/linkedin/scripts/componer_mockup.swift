#!/usr/bin/env swift

import Foundation
import CoreGraphics
import CoreImage
import ImageIO
import UniformTypeIdentifiers

struct Canvas: Decodable { let width: Int; let height: Int }
struct Template: Decodable {
    let id: String
    let file: String
    let category: String
    let label: String
    let tone: [String]
    let quad: [[Double]]
    let exclusions: [[[Double]]]?
}
struct Manifest: Decodable { let canvas: Canvas; let templates: [Template] }

enum ComposeError: Error, CustomStringConvertible {
    case usage(String), missingTemplate(String), invalidImage(String), invalidManifest(String), render(String)
    var description: String {
        switch self {
        case .usage(let s), .missingTemplate(let s), .invalidImage(let s), .invalidManifest(let s), .render(let s): return s
        }
    }
}

func value(after flag: String, in args: [String]) -> String? {
    guard let i = args.firstIndex(of: flag), i + 1 < args.count else { return nil }
    return args[i + 1]
}

func point(_ pair: [Double], canvasHeight: Int) throws -> CGPoint {
    guard pair.count == 2 else { throw ComposeError.invalidManifest("Punto inválido en manifest.json") }
    return CGPoint(x: pair[0], y: Double(canvasHeight) - pair[1])
}

func distance(_ a: CGPoint, _ b: CGPoint) -> CGFloat {
    hypot(a.x - b.x, a.y - b.y)
}

func polygonMask(width: Int, height: Int, quad: [CGPoint], exclusions: [[CGPoint]]) throws -> CGImage {
    let colorSpace = CGColorSpaceCreateDeviceGray()
    guard let context = CGContext(data: nil, width: width, height: height, bitsPerComponent: 8,
                                  bytesPerRow: width, space: colorSpace,
                                  bitmapInfo: CGImageAlphaInfo.none.rawValue) else {
        throw ComposeError.render("No se pudo crear la máscara")
    }
    context.setFillColor(gray: 0, alpha: 1)
    context.fill(CGRect(x: 0, y: 0, width: width, height: height))
    context.setFillColor(gray: 1, alpha: 1)
    context.beginPath()
    context.move(to: quad[0])
    quad.dropFirst().forEach { context.addLine(to: $0) }
    context.closePath()
    context.fillPath()
    context.setFillColor(gray: 0, alpha: 1)
    for exclusion in exclusions where exclusion.count >= 3 {
        context.beginPath()
        context.move(to: exclusion[0])
        exclusion.dropFirst().forEach { context.addLine(to: $0) }
        context.closePath()
        context.fillPath()
    }
    guard let image = context.makeImage() else { throw ComposeError.render("No se pudo finalizar la máscara") }
    return image
}

func preparedSource(_ source: CIImage, targetWidth: CGFloat, targetHeight: CGFloat, focus: String) -> CIImage {
    let sourceRect = source.extent
    let targetAspect = targetWidth / targetHeight
    let sourceAspect = sourceRect.width / sourceRect.height
    var crop = sourceRect

    if sourceAspect > targetAspect {
        crop.size.width = sourceRect.height * targetAspect
        switch focus {
        case "left": crop.origin.x = sourceRect.minX
        case "right": crop.origin.x = sourceRect.maxX - crop.width
        default: crop.origin.x = sourceRect.midX - crop.width / 2
        }
    } else {
        crop.size.height = sourceRect.width / targetAspect
        switch focus {
        case "top": crop.origin.y = sourceRect.maxY - crop.height
        case "bottom": crop.origin.y = sourceRect.minY
        default: crop.origin.y = sourceRect.midY - crop.height / 2
        }
    }

    let cropped = source.cropped(to: crop)
    let translated = cropped.transformed(by: CGAffineTransform(translationX: -crop.minX, y: -crop.minY))
    return translated.transformed(by: CGAffineTransform(scaleX: targetWidth / crop.width, y: targetHeight / crop.height))
}

func writePNG(_ image: CIImage, to url: URL, width: Int, height: Int) throws {
    let context = CIContext(options: [.useSoftwareRenderer: true])
    let bounds = CGRect(x: 0, y: 0, width: width, height: height)
    guard let cgImage = context.createCGImage(image.cropped(to: bounds), from: bounds) else {
        throw ComposeError.render("No se pudo renderizar la composición. Extensión: \(image.extent)")
    }
    guard let destination = CGImageDestinationCreateWithURL(url as CFURL, UTType.png.identifier as CFString, 1, nil) else {
        throw ComposeError.render("No se pudo crear el PNG de salida")
    }
    CGImageDestinationAddImage(destination, cgImage, nil)
    guard CGImageDestinationFinalize(destination) else { throw ComposeError.render("No se pudo guardar el PNG") }
}

do {
    let args = Array(CommandLine.arguments.dropFirst())
    guard let inputPath = value(after: "--input", in: args),
          let outputPath = value(after: "--output", in: args),
          let templateID = value(after: "--template", in: args) else {
        throw ComposeError.usage("Uso: swift componer_mockup.swift --template ID --input imagen --output salida.png [--focus center|top|bottom|left|right]")
    }
    let focus = value(after: "--focus", in: args) ?? "center"
    guard ["center", "top", "bottom", "left", "right"].contains(focus) else {
        throw ComposeError.usage("--focus debe ser center, top, bottom, left o right")
    }

    let scriptURL = URL(fileURLWithPath: #filePath).standardizedFileURL
    let skillURL = scriptURL.deletingLastPathComponent().deletingLastPathComponent()
    let assetURL = skillURL.appendingPathComponent("assets/mockups")
    let manifestData = try Data(contentsOf: assetURL.appendingPathComponent("manifest.json"))
    let manifest = try JSONDecoder().decode(Manifest.self, from: manifestData)
    guard manifest.canvas.width == 1080, manifest.canvas.height == 1350 else {
        throw ComposeError.invalidManifest("La galería debe usar un lienzo de 1080 × 1350")
    }
    guard let selected = manifest.templates.first(where: { $0.id == templateID }) else {
        throw ComposeError.missingTemplate("No existe la plantilla: \(templateID)")
    }
    guard selected.quad.count == 4 else { throw ComposeError.invalidManifest("La plantilla debe tener cuatro puntos") }

    let templateURL = assetURL.appendingPathComponent(selected.file)
    let inputURL = URL(fileURLWithPath: inputPath)
    guard let templateImage = CIImage(contentsOf: templateURL, options: [.applyOrientationProperty: true]) else {
        throw ComposeError.invalidImage("No se pudo abrir la plantilla \(selected.file)")
    }
    guard let sourceImage = CIImage(contentsOf: inputURL, options: [.applyOrientationProperty: true]) else {
        throw ComposeError.invalidImage("No se pudo abrir la imagen aprobada")
    }

    let quad = try selected.quad.map { try point($0, canvasHeight: manifest.canvas.height) }
    let exclusions = try (selected.exclusions ?? []).map { polygon in
        try polygon.map { try point($0, canvasHeight: manifest.canvas.height) }
    }
    let targetWidth = (distance(quad[0], quad[1]) + distance(quad[3], quad[2])) / 2
    let targetHeight = (distance(quad[0], quad[3]) + distance(quad[1], quad[2])) / 2
    let fitted = preparedSource(sourceImage, targetWidth: targetWidth, targetHeight: targetHeight, focus: focus)

    guard let perspective = CIFilter(name: "CIPerspectiveTransformWithExtent") else {
        throw ComposeError.render("El sistema no ofrece transformación de perspectiva")
    }
    perspective.setValue(fitted, forKey: kCIInputImageKey)
    perspective.setValue(CIVector(cgRect: CGRect(x: 0, y: 0, width: targetWidth, height: targetHeight)), forKey: "inputExtent")
    perspective.setValue(CIVector(cgPoint: quad[0]), forKey: "inputTopLeft")
    perspective.setValue(CIVector(cgPoint: quad[1]), forKey: "inputTopRight")
    perspective.setValue(CIVector(cgPoint: quad[3]), forKey: "inputBottomLeft")
    perspective.setValue(CIVector(cgPoint: quad[2]), forKey: "inputBottomRight")
    guard let placed = perspective.outputImage else { throw ComposeError.render("Falló la transformación de la imagen") }

    let maskCG = try polygonMask(width: manifest.canvas.width, height: manifest.canvas.height, quad: quad, exclusions: exclusions)
    let mask = CIImage(cgImage: maskCG)
    guard let blend = CIFilter(name: "CIBlendWithMask") else { throw ComposeError.render("No se pudo crear el compositor") }
    blend.setValue(placed, forKey: kCIInputImageKey)
    blend.setValue(templateImage, forKey: kCIInputBackgroundImageKey)
    blend.setValue(mask, forKey: kCIInputMaskImageKey)
    guard let output = blend.outputImage else { throw ComposeError.render("No se pudo componer la imagen") }

    let outputURL = URL(fileURLWithPath: outputPath)
    try FileManager.default.createDirectory(at: outputURL.deletingLastPathComponent(), withIntermediateDirectories: true)
    try writePNG(output, to: outputURL, width: manifest.canvas.width, height: manifest.canvas.height)
    print("Creado: \(outputURL.path) (1080 × 1350) con \(selected.id)")
} catch {
    fputs("Error: \(error)\n", stderr)
    exit(1)
}
