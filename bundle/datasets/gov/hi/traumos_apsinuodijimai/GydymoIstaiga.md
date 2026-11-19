---
type: Table
title: "GydymoIstaiga — Gydymo įstaigų duomenys"
description: "\"Duomenys iš Higienos instituto apie gydymo įstaigas."
resource: "https://get.data.gov.lt/datasets/gov/hi/traumos_apsinuodijimai/GydymoIstaiga"
tags: [gov, hi, gydymoistaiga, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/traumos_apsinuodijimai.csv#L56"
    title: "atviriduomenys/manifest — datasets/gov/hi/traumos_apsinuodijimai.csv#L56"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2829/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/traumos_apsinuodijimai"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# GydymoIstaiga — Gydymo įstaigų duomenys

"Duomenys iš Higienos instituto apie gydymo įstaigas. Vieną eilutę sudaro viena gydymo įstaiga. Eilutėje nurodomas gydymo įstaigos identifikacinis numeris, pavadinimas, juridinio asmens kodas ir jį validuojantis stulpelis, savivaldybė, adresas ir lokacijos koordinatės."[^manifest]

- **Model:** `datasets/gov/hi/traumos_apsinuodijimai/GydymoIstaiga`[^manifest]
- **Dataset:** ["Stacionaro ir ambulatoriniai ligoniai, gydyti nuo traumų ir apsinuodijimų"](../traumos_apsinuodijimai.md) (`datasets/gov/hi/traumos_apsinuodijimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/hi/traumos_apsinuodijimai.csv#L56](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/traumos_apsinuodijimai.csv#L56)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/traumos_apsinuodijimai/GydymoIstaiga` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `gist_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-10-20`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gist_id` | `string` | — | `4` | `open` | — | Gydymo įstaigos identifikacinis numeris | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Gydymo įstaigos pavadinimas | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Gydymo įstaigos juridinio asmens kodas | — |
| `jar_validacija` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros sugeneruotas juridinio asmens validavimo stulpelis | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | "Savivaldybė, kurioje yra gydymo įstaiga" | — |
| `adresas` | `string` | — | `4` | `open` | — | Gydymo įstaigos adresas | — |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | Gydymo įstaigos koordinatės | Gydymo įstaigos WKT tipo WGS-84 koordinatės taškas |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/traumos_apsinuodijimai.csv#L56 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/traumos_apsinuodijimai.csv#L56)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/traumos_apsinuodijimai (https://data.gov.lt/datasets/2829/)
