#!/usr/bin/env swift

import AppKit
import Foundation

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

let scriptURL = URL(fileURLWithPath: #filePath).standardizedFileURL
let skillURL = scriptURL.deletingLastPathComponent().deletingLastPathComponent()
let assetsURL = skillURL.appendingPathComponent("assets/mockups")
let manifest = try JSONDecoder().decode(Manifest.self, from: Data(contentsOf: assetsURL.appendingPathComponent("manifest.json")))

let columns = 4
let cellWidth = 270
let previewHeight = 338
let labelHeight = 54
let rows = Int(ceil(Double(manifest.templates.count) / Double(columns)))
let size = NSSize(width: columns * cellWidth, height: rows * (previewHeight + labelHeight))
let output = NSImage(size: size)

output.lockFocus()
NSColor(calibratedWhite: 0.07, alpha: 1).setFill()
NSBezierPath(rect: NSRect(origin: .zero, size: size)).fill()

for (index, template) in manifest.templates.enumerated() {
    guard let image = NSImage(contentsOf: assetsURL.appendingPathComponent(template.file)) else { continue }
    let col = index % columns
    let row = index / columns
    let x = col * cellWidth
    let top = Int(size.height) - row * (previewHeight + labelHeight)
    let previewRect = NSRect(x: x, y: top - previewHeight, width: cellWidth, height: previewHeight)
    image.draw(in: previewRect, from: NSRect(origin: .zero, size: image.size), operation: .copy, fraction: 1)

    NSColor(calibratedWhite: 0.07, alpha: 0.96).setFill()
    NSBezierPath(rect: NSRect(x: x, y: top - previewHeight - labelHeight, width: cellWidth, height: labelHeight)).fill()
    let text = "\(template.id)\n\(template.label)"
    let paragraph = NSMutableParagraphStyle()
    paragraph.alignment = .center
    let attributes: [NSAttributedString.Key: Any] = [
        .font: NSFont.systemFont(ofSize: 11, weight: .medium),
        .foregroundColor: NSColor.white,
        .paragraphStyle: paragraph
    ]
    text.draw(in: NSRect(x: x + 8, y: top - previewHeight - labelHeight + 8, width: cellWidth - 16, height: labelHeight - 12), withAttributes: attributes)
}
output.unlockFocus()

guard let tiff = output.tiffRepresentation,
      let bitmap = NSBitmapImageRep(data: tiff),
      let png = bitmap.representation(using: .png, properties: [:]) else {
    fatalError("No se pudo generar catalogo.png")
}
try png.write(to: assetsURL.appendingPathComponent("catalogo.png"))
print("Catálogo creado con \(manifest.templates.count) plantillas")
