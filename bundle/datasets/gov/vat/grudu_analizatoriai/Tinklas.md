---
type: Table
title: "Tinklas — Pateikiama informacija (eksploatavimo vietos adresas, ūkio subjekto pavadinimas / vardas pavardė) apie ūkio subjektų turimus grūdų analizatorius, įjungtus į tinklą Lietuvoje"
description: "Spinta table datasets/gov/vat/grudu_analizatoriai/Tinklas (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/grudu_analizatoriai/Tinklas"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/grudu_analizatoriai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/grudu_analizatoriai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Tinklas — Pateikiama informacija (eksploatavimo vietos adresas, ūkio subjekto pavadinimas / vardas pavardė) apie ūkio subjektų turimus grūdų analizatorius, įjungtus į tinklą Lietuvoje

- **Model:** `datasets/gov/vat/grudu_analizatoriai/Tinklas`[^manifest]
- **Dataset:** [datasets/gov/vat/grudu_analizatoriai](../grudu_analizatoriai.md) (`datasets/gov/vat/grudu_analizatoriai`)
- **Manifest CSV:** [datasets/gov/vat/grudu_analizatoriai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/grudu_analizatoriai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/grudu_analizatoriai/Tinklas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/grudu_analizatoriai.csv
