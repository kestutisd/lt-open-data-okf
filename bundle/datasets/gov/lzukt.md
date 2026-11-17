---
type: Dataset
title: "Lietuvos žemės ūkio konsultavimo tarnyba"
description: "Lietuvos žemės ūkio konsultavimo tarnybos integruotos augalų apsaugos informavimo, konsultavimo ir mokymų informacinė sistemos duomenų rinkiniai, skirti augalų kenkėjų, ligų ir žalingumo įverčių stebėsenai bei analizei."
resource: "https://get.data.gov.lt/datasets/gov/lzukt"
tags: [gov, lzukt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lzukt/ikmis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lzukt/ikmis.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Lietuvos žemės ūkio konsultavimo tarnyba

Lietuvos žemės ūkio konsultavimo tarnybos integruotos augalų apsaugos informavimo, konsultavimo ir mokymų informacinė sistemos duomenų rinkiniai, skirti augalų kenkėjų, ligų ir žalingumo įverčių stebėsenai bei analizei.

- **Namespace:** `datasets/gov/lzukt`[^manifest]
- **Manifest CSV:** [datasets/gov/lzukt/ikmis.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lzukt/ikmis.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lzukt`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Kenkejas](lzukt/Kenkejas.md) | Augalų kenkėjų katalogas | `4` | `vda_id` | `open` | 11 | Integruotos augalų apsaugos informavimo, konsultavimo ir mokymų informacinė sistemos kenkėjų katalogas |
| [Liga](lzukt/Liga.md) | Augalų ligų katalogas | `4` | `vda_id` | `open` | 10 | Integruotos augalų apsaugos informavimo, konsultavimo ir mokymų informacinė sistemos ligų katalogas |
| [Ivertis](lzukt/Ivertis.md) | Augalų kenksmingų organizmų plitimo žalingumo įverčiai | `4` | `vda_id` | `open` | 8 | Integruotos augalų apsaugos informavimo, konsultavimo ir mokymų informacinė sistemos augalų kenksmingų organizmų plitimo žalingumo įverčiai |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lzukt/ikmis.csv
