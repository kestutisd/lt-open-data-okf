---
type: Table
title: "Seniunija — Adresų registro seniūnijų tekstinių duomenų rinkinys"
description: "Seniūnijų tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - seniūnijas apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/seniunija/Seniunija"
tags: [gov, rc, seniunija, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/seniunija.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/seniunija.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1288/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ar/seniunija"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Seniunija — Adresų registro seniūnijų tekstinių duomenų rinkinys

Seniūnijų tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - seniūnijas apibūdinantys duomenys). Duomenų geografinė imtis — visa šalies teritorija.[^manifest]

- **Model:** `datasets/gov/rc/ar/seniunija/Seniunija`[^manifest]
- **Dataset:** [Adresų registras](../seniunija.md) (`datasets/gov/rc/ar/seniunija`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/seniunija.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/seniunija.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/seniunija/Seniunija` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `sen_kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sen_kodas` | `integer` | — | `4` | `open` | — | Seniūnijos identifikavimo kodas | — |
| `tipas` | `string` | — | `3` | `open` | — | Administracinio vieneto tipas | — |
| `tipo_santrumpa` | `string` | — | `3` | `open` | — | Administracinio vieneto tipo trumpinys | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Seniūnijos pavadinimas | — |
| `savivaldybe` | `ref` | [Savivaldybe](../savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybės, kurioje yra seniūnija, identifikavimo kodas | — |
| `sen_nuo` | `date` | `D` | `4` | `open` | — | Objekto įregistravimo data | — |
| `sen_iki` | `date` | `D` | `4` | `open` | — | Objekto išregistravimo data | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/seniunija.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/seniunija.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ar/seniunija (https://data.gov.lt/datasets/1288/)
