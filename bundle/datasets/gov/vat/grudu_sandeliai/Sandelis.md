---
type: Table
title: "Sandelis — Pateikiama informacija (adresas, pavadinimas, licencijos išdavimo data, leistinos sandėliuoti grūdų rūšys bei kiekiai) apie ūkio subjektų licencijuotus grūdų sandėlius"
description: "Spinta table datasets/gov/vat/grudu_sandeliai/Sandelis (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/grudu_sandeliai/Sandelis"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/grudu_sandeliai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/grudu_sandeliai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sandelis — Pateikiama informacija (adresas, pavadinimas, licencijos išdavimo data, leistinos sandėliuoti grūdų rūšys bei kiekiai) apie ūkio subjektų licencijuotus grūdų sandėlius

- **Model:** `datasets/gov/vat/grudu_sandeliai/Sandelis`[^manifest]
- **Dataset:** [datasets/gov/vat/grudu_sandeliai](../grudu_sandeliai.md) (`datasets/gov/vat/grudu_sandeliai`)
- **Manifest CSV:** [datasets/gov/vat/grudu_sandeliai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/grudu_sandeliai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/grudu_sandeliai/Sandelis`
- **Primary Key (`ref`):** `licencijos_nr`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `licencijos_nr` | `string` | — | `2` | `open` | — | Eilės numeris | — |
| `isdavimas` | `date` | `D` | `4` | `open` | — | Licencijos išdavimo data | — |
| `grudu_rusis_ir_kiekis` | `string` | — | `1` | `open` | — | Grūdų rūšis ir kiekis | — |
| `ukio_subjekto_pav` | `string` | — | `2` | `open` | — | Ūkio subjekto pavadinimas | — |
| `adresas` | `string` | — | `1` | `open` | — | Ūkio subjekto adresas | — |
| `koord` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Grūdų sandėlio koordinatės (LKS) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ukio_subjekto_pav` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo", type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |
| `adresas` | `update(base: "/datasets/gov/rc/ar/adresotaskas/AdresoTaskas", type: "ref", ref: "/datasets/gov/rc/ar/adresotaskas/AdresoTaskas")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/grudu_sandeliai.csv
