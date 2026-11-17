---
type: Table
title: "GydymoIstaiga — Gydymo įstaigų duomenys"
description: "Duomenys iš Higienos instituto apie gydymo įstaigas."
resource: "https://get.data.gov.lt/datasets/gov/hi/traumos_apsinuodijimai/GydymoIstaiga"
tags: [gov, hi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/hi/traumos_apsinuodijimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/traumos_apsinuodijimai.csv#L56"
    last_modified: "2026-11-11T14:39:20Z"
---

# GydymoIstaiga — Gydymo įstaigų duomenys

Duomenys iš Higienos instituto apie gydymo įstaigas. Vieną eilutę sudaro viena gydymo įstaiga. Eilutėje nurodomas gydymo įstaigos identifikacinis numeris, pavadinimas, juridinio asmens kodas ir jį validuojantis stulpelis, savivaldybė, adresas ir lokacijos koordinatės.

- **Model:** `datasets/gov/hi/traumos_apsinuodijimai/GydymoIstaiga`[^manifest]
- **Dataset:** [Stacionaro ir ambulatoriniai ligoniai, gydyti nuo traumų ir apsinuodijimų](../traumos_apsinuodijimai.md) (`datasets/gov/hi/traumos_apsinuodijimai`)
- **Manifest CSV:** [datasets/gov/hi/traumos_apsinuodijimai.csv#L56](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/traumos_apsinuodijimai.csv#L56)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/traumos_apsinuodijimai/GydymoIstaiga`
- **Primary Key (`ref`):** `gist_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gist_id` | `string` | — | `4` | `open` | — | Gydymo įstaigos identifikacinis numeris | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Gydymo įstaigos pavadinimas | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Gydymo įstaigos juridinio asmens kodas | — |
| `jar_validacija` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros sugeneruotas juridinio asmens validavimo stulpelis | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė, kurioje yra gydymo įstaiga | — |
| `adresas` | `string` | — | `4` | `open` | — | Gydymo įstaigos adresas | — |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | Gydymo įstaigos koordinatės | Gydymo įstaigos WKT tipo WGS-84 koordinatės taškas |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/traumos_apsinuodijimai.csv
