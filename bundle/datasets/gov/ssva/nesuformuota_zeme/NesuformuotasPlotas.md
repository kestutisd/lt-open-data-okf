---
type: Table
title: "NesuformuotasPlotas — Nesuformuoti žemės plotai"
description: "Duomenų rinkinys apima informaciją apie valstybės valdomus, bet dar nesuformuotus žemės plotus."
resource: "https://get.data.gov.lt/datasets/gov/ssva/nesuformuota_zeme/NesuformuotasPlotas"
tags: [gov, ssva, nesuformuotasplotas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/nesuformuota_zeme.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/ssva/nesuformuota_zeme.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3879/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ssva/nesuformuota_zeme"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# NesuformuotasPlotas — Nesuformuoti žemės plotai

Duomenų rinkinys apima informaciją apie valstybės valdomus, bet dar nesuformuotus žemės plotus. Kiekvienam sklypui pateikiamas unikalus identifikatorius, jį administruojanti institucija (dažniausiai Nacionalinė žemės tarnyba), buvimo vietos koordinatės (taškinė ir poligoninė geometrija), nesuformuotos žemės perimetras bei plotas. Duomenys taip pat apima savivaldybės ir gyvenvietės kodus, o geografinė informacija pateikta keliuose koordinacinių sistemų formatuose (LKS94, WGS84, GeoJSON, WKT).[^manifest]

- **Model:** `datasets/gov/ssva/nesuformuota_zeme/NesuformuotasPlotas`[^manifest]
- **Dataset:** [Nesuformuoti žemės plotai](../nesuformuota_zeme.md) (`datasets/gov/ssva/nesuformuota_zeme`)[^manifest]
- **Manifest CSV:** [datasets/gov/ssva/nesuformuota_zeme.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/nesuformuota_zeme.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/nesuformuota_zeme/NesuformuotasPlotas` (`deployed`)[^manifest]
- **Provider:** `ssva` — Statybos sektoriaus vystymo agentūra (SSVA) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus nesuformuotos žemės identifikatorius | — |
| `patiketinis` | `string` | — | `4` | `open` | — | Patikėtinio tipas: N - NŽT, S - savivaldybė | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Patikėtinio pavadinimas | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Patiketinio JAR kodas | — |
| `gyv_kodas` | `string` | — | `4` | `open` | — | Gyvenvietės kodas | — |
| `sav_kodas` | `string` | — | `4` | `open` | — | Savivaldybės kodas | — |
| `perimetras_m` | `number` | — | `4` | `open` | — | Nesuformuoto ploto perimetras metrais | — |
| `plotas_m2` | `number` | — | `4` | `open` | — | Nesuformuotas plotas kvadratiniais metrais | — |
| `geometrija_adp` | `geometry(point, 3346)` | — | `4` | `open` | — | Nesuformuoto ploto taškinė geometrija WKT (Well-Known Text) formatu | — |
| `geom_wkt` | `string` | — | `4` | `open` | — | Nesuformuoto ploto geometrija WKT (Well-Known Text) formatu (LKS94) | — |
| `geojson_wgs` | `string` | — | `4` | `open` | — | Nesuformuoto ploto geometrija GeoJSON formatu (koordinatės WGS84 sistemoje) | — |
| `geojson_lks` | `string` | — | `4` | `open` | — | Nesuformuoto ploto geometrija GeoJSON formatu (koordinatės LKS94 sistemoje) | — |
| `paskutinio_atnaujinimo_data` | `datetime` | `D` | `4` | `open` | — | Duomenų atnaujinimo data | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/nesuformuota_zeme.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/nesuformuota_zeme.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ssva/nesuformuota_zeme (https://data.gov.lt/datasets/3879/)
