---
type: Reference
title: "AR Address Register Hierarchy & LKS-94 Coordinate Reference"
description: "Canonical join reference for VĮ Registrų centras Address Register (rc/ar): Apskritis -> Savivaldybe -> Seniunija -> GyvenamojiVietove -> Gatve -> Adresas -> Pastatas -> Patalpa and EPSG:3346 vs EPSG:4326."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/savivaldybe/Savivaldybe"
tags: [join, ar, rc, address, lks94, geometry]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: ar-manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/savivaldybe.csv"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/* Address Register Schemas"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: spinta-dsa
    resource: "https://atviriduomenys.readthedocs.io/latest/dsa/index.html"
    title: "Spinta DSA Geometry & Foreign-Key Specification"
    author: "team:vssa"
---

# AR Address Register Hierarchy & LKS-94 Coordinate Reference

The **Address Register** (*Adresų registras* — **AR**, maintained by *VĮ Registrų centras* under `datasets/gov/rc/ar/*`) defines Lithuania's administrative territorial hierarchy, address objects, and `LKS-94` spatial coordinates.[^ar-manifest]

## 1. Administrative & Address Object Hierarchy (`level = 4`)

All core AR models operate at `level = 4`, meaning `ref` foreign keys on `get.data.gov.lt` serialize as Spinta UUID objects (`{"_id": "<UUID>"}`) while exposing stable integer natural keys (`model.ref`):[^ar-manifest][^spinta-dsa]

| Hierarchy Level | Model (`datasets/gov/rc/ar/...`) | Natural PK (`model.ref`) | Outgoing `level=4` Parent `ref` Columns |
| --- | --- | --- | --- |
| 1. County (*Apskritis*) | [Apskritis](../../datasets/gov/rc/ar/apskritis/Apskritis.md) | `adm_kodas` (`integer`) | — (top level, 10 counties) |
| 2. Municipality (*Savivaldybė*) | [Savivaldybe](../../datasets/gov/rc/ar/savivaldybe/Savivaldybe.md) | `sav_kodas` (`integer`) | `apskritis` -> `Apskritis._id` |
| 3. Eldership (*Seniūnija*) | [Seniunija](../../datasets/gov/rc/ar/seniunija/Seniunija.md) | `sen_kodas` (`integer`) | `savivaldybe` -> `Savivaldybe._id` |
| 4. Settlement (*Gyvenamoji vietovė*) | [GyvenamojiVietove](../../datasets/gov/rc/ar/gyvenamojivietove/GyvenamojiVietove.md) | `gyv_kodas` (`integer`) | `seniunija` -> `Seniunija._id`, `savivaldybe` -> `Savivaldybe._id` |
| 5. Street (*Gatvė*) | [Gatve](../../datasets/gov/rc/ar/gatve/Gatve.md) | `gat_kodas` (`integer`) | `gyvenamoji_vietove` -> `GyvenamojiVietove._id` |
| 6. Address Object (*Adresas* / *Pastatas*) | [Adresas](../../datasets/gov/rc/ar/adresai/Adresas.md) / [Pastatas](../../datasets/gov/rc/ar/pastatas/Pastatas.md) | `aob_kodas` (`integer`) | `aob_kodas` -> `Adresas._id`, `savivaldybe`, `gyvenamoji_vietove`, `gatve` |
| 7. Premise (*Patalpa*) | [Patalpa](../../datasets/gov/rc/ar/patalpa/Patalpa.md) | `aob_kodas` (`integer`) | `aob_kodas` -> `Adresas._id`, `pastatas` -> `Pastatas._id` |

- **Boundary & Point Geometries:** Point coordinates for `aob_kodas` are published in {ar_taskas} (`lks: geometry(point, 3346)`, `x_koord`, `y_koord`, `n_koord`, `e_koord` in meters), while polygon/line geometries live in the `gra*` datasets (`graapskritis`, `grasavivaldybe`, `graseniunija`, `gragyvenamojivietove`, `gragatve`).[^ar-manifest]

## 2. Coordinate Reference Systems: `LKS-94` (`EPSG:3346`) vs `WGS-84` (`EPSG:4326`)

- **Default Spinta CRS (`EPSG:3346`):** Unless a `geometry(...)` type explicitly specifies `4326` (e.g., `geometry(point, 4326)`), Lithuanian Spinta `geometry` columns and `x`/`y` coordinate pairs use the national metric grid **`LKS-94 / Lithuania TM` (`EPSG:3346`, planar meters)**.[^spinta-dsa]
- **Axis Order & Reprojection Warning:** In Lithuanian cadastral/AR tables (`EPSG:3346`), `x_koord` (`n_koord`, ~`5 970 000`–`6 260 000` m) is Northing and `y_koord` (`e_koord`, ~`300 000`–`680 000` m) is Easting, whereas WKT `POINT(E N)` in GIS tools orders Easting first. Always verify axis order and reproject `EPSG:3346` -> `EPSG:4326` before rendering on web slippy maps.[^ar-manifest][^spinta-dsa]

- See also: [Spinta DSA & API Reference](../spinta-dsa-guide.md) and [JAR Legal Entities Join Reference](jar-legal-entities.md).

[^ar-manifest]: atviriduomenys/manifest — `datasets/gov/rc/ar/savivaldybe.csv` (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/savivaldybe.csv)
[^spinta-dsa]: Spinta DSA Geometry & Foreign-Key Specification (https://atviriduomenys.readthedocs.io/latest/dsa/index.html)
