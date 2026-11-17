---
type: Table
title: "SeiminePadetis — Gyventojų registro duomenys apie gyventojų šeiminę padėtį, vaikų skaičių savivaldybėse"
description: "Spinta table datasets/gov/rc/gr/seimines_padetys/SeiminePadetis (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/gr/seimines_padetys/SeiminePadetis"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/gr/seimines_padetys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/seimines_padetys.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# SeiminePadetis — Gyventojų registro duomenys apie gyventojų šeiminę padėtį, vaikų skaičių savivaldybėse

- **Model:** `datasets/gov/rc/gr/seimines_padetys/SeiminePadetis`[^manifest]
- **Dataset:** [Gyventojų registro duomenys apie gyventojų šeiminę padėtį, vaikų skaičių savivaldybėse](../seimines_padetys.md) (`datasets/gov/rc/gr/seimines_padetys`)
- **Manifest CSV:** [datasets/gov/rc/gr/seimines_padetys.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/seimines_padetys.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/gr/seimines_padetys/SeiminePadetis`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Gyventojo eilės numeris šiame duomenų rinkinyje | — |
| `lytis` | `string` | — | `4` | `open` | — | Gyventojo lytis (V - Vyras; M - Moteris) | — |
| `amzius` | `string` | — | `3` | `open` | — | Gyventojo amžius / amžiaus grupė | — |
| `seim_statusas` | `string` | — | `3` | `open` | — | Gyventojo šeiminė padėtis (nevedęs / netekėjusi, vedęs / ištekėjusi, našlys / našlė, išsiskyręs / išsiskyrusi) | — |
| `vaiku_sk` | `string` | — | `3` | `open` | — | Gyventojo turimų vaikų skaičius | — |
| `vaiku_sk_nuo_0_iki_6` | `integer` | `U` | `4` | `open` | — | Gyventojo turimų vaikų skaičius (nuo 0 iki 6 metų imtinai); | — |
| `vaiku_sk_nuo_7_iki_17` | `integer` | `U` | `4` | `open` | — | Gyventojo turimų vaikų skaičius (nuo 7 iki 17 metų imtinai); | — |
| `dek_metai` | `integer` | — | `2` | `open` | — | Gyventojo gyvenamosios vietos deklaravimo metai | — |
| `dek_ketvirtis` | `string` | — | `2` | `open` | — | Gyventojo gyvenamosios vietos deklaravimo metų ketvirtis | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybė, kurioje deklaruota gyventojo gyvenamoji vieta, iš Adresų registro | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/gr/seimines_padetys.csv
