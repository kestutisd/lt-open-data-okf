---
type: Table
title: "Laboratorija — Pateikiama informacija (adresas, pavadinimas, atestavimo data) apie grūdus superkančių ūkio subjektų atestuotas grūdų kokybės tyrimo laboratorijas"
description: "Spinta table datasets/gov/vat/grudu_kokybe/Laboratorija (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/grudu_kokybe/Laboratorija"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/r13_kokybes_laboratorijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r13_kokybes_laboratorijos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Laboratorija — Pateikiama informacija (adresas, pavadinimas, atestavimo data) apie grūdus superkančių ūkio subjektų atestuotas grūdų kokybės tyrimo laboratorijas

- **Model:** `datasets/gov/vat/grudu_kokybe/Laboratorija`[^manifest]
- **Dataset:** [datasets/gov/vat/grudu_kokybe](../grudu_kokybe.md) (`datasets/gov/vat/grudu_kokybe`)
- **Manifest CSV:** [datasets/gov/vat/r13_kokybes_laboratorijos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r13_kokybes_laboratorijos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/grudu_kokybe/Laboratorija`
- **Primary Key (`ref`):** `eil_nr`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eilės numeris | — |
| `pazymejimo_data` | `date` | `D` | `4` | `open` | — | Atestavimo pažymėjimo data | — |
| `pazymejimo_nr` | `string` | — | `2` | `open` | — | Atestavimo pažymėjimo Nr. | — |
| `ankstesnis_pazymejimas` | `string` | — | `1` | `open` | — | Ankstesnio (-ių) atestavimo pažymėjimo (-ų) data (-os) | — |
| `laboratorija` | `string` | — | `2` | `open` | — | Atestuotos laboratorijos pavadinimas | — |
| `adresas` | `string` | — | `1` | `open` | — | Atestuotos laboratorijos adresas | — |
| `pastabos` | `string` | — | `2` | `open` | — | Pastabos | — |
| `koord` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Laboratorijos vietos koordinatės (LKS) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `laboratorija` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo"` | `type` | — | — | — | — | — |
| `adresas` | `update(base: "/datasets/gov/rc/ar/adresotaskas/AdresoTaskas"` | `type` | — | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r13_kokybes_laboratorijos.csv
