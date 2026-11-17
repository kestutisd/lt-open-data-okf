---
type: Table
title: "Seniunija — Adresų registro seniūnijų tekstinių duomenų rinkinys"
description: "Seniūnijų tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - seniūnijas apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/seniunija/Seniunija"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/seniunija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/seniunija.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Seniunija — Adresų registro seniūnijų tekstinių duomenų rinkinys

Seniūnijų tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - seniūnijas apibūdinantys duomenys). Duomenų geografinė imtis — visa šalies teritorija.

- **Model:** `datasets/gov/rc/ar/seniunija/Seniunija`[^manifest]
- **Dataset:** [Adresų registras](../seniunija.md) (`datasets/gov/rc/ar/seniunija`)
- **Manifest CSV:** [datasets/gov/rc/ar/seniunija.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/seniunija.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/seniunija/Seniunija`
- **Primary Key (`ref`):** `sen_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sen_kodas` | `integer` | — | `4` | `open` | — | Seniūnijos identifikavimo kodas | — |
| `tipas` | `string` | — | `3` | `open` | — | Administracinio vieneto tipas | — |
| `tipo_santrumpa` | `string` | — | `3` | `open` | — | Administracinio vieneto tipo trumpinys | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Seniūnijos pavadinimas | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybės, kurioje yra seniūnija, identifikavimo kodas | — |
| `sen_nuo` | `date` | `D` | `4` | `open` | — | Objekto įregistravimo data | — |
| `sen_iki` | `date` | `D` | `4` | `open` | — | Objekto išregistravimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/seniunija.csv
