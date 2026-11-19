---
type: Table
title: "Tinklas — Pateikiama informacija (eksploatavimo vietos adresas, ūkio subjekto pavadinimas / vardas pavardė) apie ūkio subjektų turimus grūdų analizatorius, įjungtus į tinklą Lietuvoje"
description: "Spinta table datasets/gov/vat/grudu_analizatoriai/Tinklas (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/grudu_analizatoriai/Tinklas"
tags: [gov, vat, tinklas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/grudu_analizatoriai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/grudu_analizatoriai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1873/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/grudu_analizatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Tinklas — Pateikiama informacija (eksploatavimo vietos adresas, ūkio subjekto pavadinimas / vardas pavardė) apie ūkio subjektų turimus...

- **Model:** `datasets/gov/vat/grudu_analizatoriai/Tinklas`[^manifest]
- **Dataset:** [Grūdų analizatorių tinklas](../grudu_analizatoriai.md) (`datasets/gov/vat/grudu_analizatoriai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/grudu_analizatoriai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/grudu_analizatoriai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/grudu_analizatoriai/Tinklas` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Eilės numeris | — |
| `ukio_subjektas` | `string` | — | `2` | `open` | — | Ūkio subjekto pavadinimas | — |
| `eksploatavimo_vieta` | `string` | — | `1` | `open` | — | Prietaiso eksploatavimo vieta | — |
| `modelis` | `string` | — | `3` | `open` | — | Prietaiso modelis | — |
| `prietaiso_nr` | `string` | — | `4` | `open` | — | Prietaiso numeris | — |
| `skyrius` | `string` | — | `4` | `open` | — | Regioninis skyrius | — |
| `koord` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Eksploatavimo vietos koordinatės (LKS) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ukio_subjektas` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo", type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |
| `eksploatavimo_vieta` | `update(base: "/datasets/gov/rc/ar/adresotaskas/AdresoTaskas", type: "ref", ref: "/datasets/gov/rc/ar/adresotaskas/AdresoTaskas")` | `type` | `4` | `open` | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/grudu_analizatoriai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/grudu_analizatoriai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/grudu_analizatoriai (https://data.gov.lt/datasets/1873/)
