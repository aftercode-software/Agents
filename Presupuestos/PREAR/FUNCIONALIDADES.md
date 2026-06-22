# Funcionalidades

## Cliente

PREAR

## Tipo de proyecto

Sistema complejo

## Objetivo general

Desarrollar una aplicación web interna para digitalizar y centralizar la operación del taller de PREAR, permitiendo gestionar obras, órdenes de trabajo, compras, materiales, stock, costos y KPIs operativos desde una única plataforma.

## Problema o necesidad

Actualmente el taller necesita ordenar y profesionalizar su operación interna, registrar con trazabilidad el trabajo realizado para distintas obras y plantas, y poder calcular con mayor precisión el costo real de cada orden de trabajo. También necesitan dejar de depender de registros manuales o planillas aisladas para materiales, stock, horas hombre y seguimiento operativo.

La necesidad de fondo no es solo administrativa: PREAR quiere que el taller funcione como una unidad con costos propios, que permita comparar producción interna contra proveedores externos, analizar rentabilidad y tomar decisiones con información consolidada.

## Alcance incluido

- Aplicación web multiusuario de uso interno para PREAR.
- Login de usuarios internos con control de acceso por roles.
- Gestión de usuarios con al menos roles de administrador, operario de taller y compras.
- Gestión de obras con su despiece de piezas, tratadas como una misma entidad operativa.
- Gestión de órdenes de trabajo asociadas a una obra y opcionalmente a una pieza específica.
- Registro operativo por orden de trabajo: tipo de trabajo, descripción, fechas, estado, operarios, horas estimadas, horas reales, observaciones y métricas productivas.
- Base de datos propia de insumos y materiales dentro del sistema.
- Importación o carga inicial de catálogo de insumos a partir del archivo actual de inventario.
- Uso de insumos en órdenes de trabajo con descuento automático de stock al imputarlos a una obra u OT.
- Gestión básica de stock disponible para materiales e insumos utilizados por el taller.
- Módulo de pedidos de compra vinculado a faltantes o necesidades del taller.
- Módulo de costos para visualizar materiales, mano de obra y costo total por orden de trabajo.
- Dashboard de KPIs operativos y productivos.
- Persistencia de datos en base de datos propia del sistema.
- Panel administrador web para consulta y gestión interna.

## Exclusiones

- Aplicación mobile nativa para Android o iOS.
- Integración con ERP, sistema contable, facturación o proveedores externos no relevados.
- Automatización avanzada de compras con circuitos de aprobación multinivel.
- Integración en tiempo real con sistemas corporativos de otras áreas de PREAR.
- Control de stock completo de toda la empresa fuera del alcance del taller.
- Gestión financiera integral, contable o impositiva.
- Migración histórica exhaustiva de datos no estructurados.
- Reportería BI avanzada fuera de los KPIs operativos definidos para esta primera etapa.
- Infraestructura corporativa compleja, alta disponibilidad o arquitectura enterprise específica no relevada.

## Módulos o secciones

- Autenticación y acceso.
- Gestión de usuarios y roles.
- Gestión de obras con despiece.
- Gestión de órdenes de trabajo.
- Catálogo de insumos y materiales.
- Stock y movimientos básicos.
- Pedidos de compra.
- Costos y presupuestación interna.
- KPIs y dashboard.

## Funcionalidades detalladas

### Autenticación y acceso

- Inicio de sesión para usuarios internos.
- Gestión de credenciales y acceso seguro.
- Restricción de vistas y acciones según rol.

### Gestión de usuarios y roles

- Alta, edición y baja lógica de usuarios internos.
- Definición de roles con permisos generales.
- Rol administrador con acceso total a datos, costos y KPIs.
- Rol operario o trabajador con acceso operativo a obras y órdenes de trabajo.
- Rol compras con acceso acotado a pedidos de compra y actualización de ingresos de stock, según definición final.

### Gestión de obras con despiece

- Creación de obras con nombre, código, cliente o comitente y estado.
- Registro del despiece de piezas dentro de cada obra.
- Asociación de piezas a futuras órdenes de trabajo.
- Consulta de avance general por obra.

### Gestión de órdenes de trabajo

- Alta de órdenes de trabajo con numeración interna.
- Asociación de cada OT a una obra y opcionalmente a una pieza.
- Registro de tipo de trabajo, descripción, solicitante o sector, fechas, estado y observaciones.
- Registro de dimensiones, cantidades, operarios asignados, horas estimadas y horas reales.
- Seguimiento del estado de la OT durante su ciclo de vida.
- Posibilidad de imprimir o descargar la OT en PDF como salida integrada del flujo de la orden de trabajo.
- Posibilidad de generar una versión presupuestable o imprimible de la OT para circulación interna.

### Catálogo de insumos y materiales

- Base propia de materiales dentro del sistema.
- Carga manual de insumos.
- Importación inicial desde el archivo actual de inventario.
- Clasificación por tipo, unidad y costo unitario.
- Edición y mantenimiento del catálogo por usuarios autorizados.

### Stock y movimientos básicos

- Descuento automático de stock al imputar materiales a una OT.
- Visualización de stock disponible por insumo.
- Registro básico de ingresos de stock.
- Trazabilidad mínima de movimientos relacionados con uso e ingreso.
- Soporte para una operatoria mixta donde el sistema centraliza el stock operativo del taller.

### Pedidos de compra

- Generación de pedidos de compra desde necesidades detectadas en taller o por faltantes.
- Estado del pedido de compra dentro del sistema.
- Registro de recepción o ingreso posterior de materiales.
- Descarga o impresión del pedido de compra en PDF para envío a otra área, como salida integrada del flujo de compras.

### Costos y presupuestación interna

- Cálculo de costo de materiales por OT.
- Cálculo de costo de mano de obra por OT.
- Cálculo de costo total real por orden.
- Visualización comparativa entre horas estimadas y reales.
- Soporte para obtener un presupuesto o costo interno del molde o trabajo realizado.

### KPIs y dashboard

- KPIs de producción por período.
- KPIs de volumen productivo, costos y órdenes generadas.
- Indicadores de eficiencia basados en horas estimadas vs. reales.
- Indicadores de consumo o uso de materiales.
- Lectura ejecutiva para analizar rentabilidad y operación del taller.

## Roles y permisos

- Administrador: acceso total a obras, órdenes de trabajo, usuarios, materiales, stock, pedidos de compra, costos y KPIs.
- Operario / trabajador del taller: acceso operativo a consulta y carga de información vinculada a obras y órdenes de trabajo según permisos finales.
- Compras: acceso acotado a pedidos de compra y potencialmente a ingreso o actualización de stock, según definición final del circuito.

## Integraciones

- Importación inicial del catálogo de materiales desde el archivo actual provisto por PREAR.
- Posible lectura de una planilla operativa existente como apoyo al alta inicial de insumos.
- Generación de archivos PDF desde el sistema para circulación interna.

## Supuestos y dependencias

- PREAR definirá un responsable funcional para validar alcance, reglas operativas y permisos.
- El archivo actual de inventario será utilizable como base inicial para la carga del catálogo.
- Las reglas de costo por hora, cálculo de mano de obra y estructura de costos directos serán provistas o validadas por PREAR.
- El sistema se desarrollará para uso interno y no contemplará portales externos para clientes o proveedores en esta etapa.
- El circuito exacto de compras, recepción y actualización de stock puede requerir ajustes finos durante el relevamiento funcional detallado.
- El alcance contempla un stock operativo del taller, no una solución corporativa integral de inventario para toda la empresa.

## Pendientes abiertos

- Confirmar si el rol compras podrá únicamente cargar ingresos de stock o también gestionar estados completos del pedido.
- Confirmar si el circuito de aprobación de compras requiere uno o varios niveles de autorización.
- Definir con mayor precisión qué KPIs serán imprescindibles en la primera versión y cuáles quedarán para una segunda etapa.
- Definir si el sistema deberá contemplar materiales reutilizados o recuperados con una lógica de valorización diferenciada.
- Confirmar formato exacto y contenido de los PDF de órdenes de trabajo y pedidos de compra.
- Confirmar si la carga de stock inicial será única o si se requerirá una sincronización periódica con una planilla externa.

## Extras y plan de crecimiento sugerido

- Bitácora completa de movimientos de stock con trazabilidad ampliada.
- Circuito de compras más robusto con aprobación, recepción y conciliación interna.
- Reingreso formal de materiales al stock con historial detallado.
- Reportes avanzados de rentabilidad por obra, tipo de trabajo o período.
- Integraciones futuras con sistemas corporativos o planillas de otras áreas.
- Mayor granularidad de permisos por acción o por módulo.
