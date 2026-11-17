---
type: Table
title: "FitosanitarineVieta — Patikrinimo vietos, pripažintos tinkamomis atlikti fitosanitarinį tikrinimą įvežamiems į Lietuvos Respubliką ir Europos Sąjungą augalams, augaliniams produktams ir kitiems objektams laikyti"
description: "Spinta table datasets/gov/vat/tikrinimo_vietos/FitosanitarineVieta (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/tikrinimo_vietos/FitosanitarineVieta"
tags: [gov, vat, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/tikrinimo_vietos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/tikrinimo_vietos.csv#L14"
    last_modified: "2026-11-11T14:39:20Z"
---

# FitosanitarineVieta — Patikrinimo vietos, pripažintos tinkamomis atlikti fitosanitarinį tikrinimą įvežamiems į Lietuvos Respubliką ir Europos Sąjungą augalams, augaliniams produktams ir kitiems objektams laikyti

- **Model:** `datasets/gov/vat/tikrinimo_vietos/FitosanitarineVieta`[^manifest]
- **Dataset:** [datasets/gov/vat/tikrinimo_vietos](../tikrinimo_vietos.md) (`datasets/gov/vat/tikrinimo_vietos`)
- **Manifest CSV:** [datasets/gov/vat/tikrinimo_vietos.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/tikrinimo_vietos.csv#L14)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/tikrinimo_vietos/FitosanitarineVieta`
- **Primary Key (`ref`):** `eil_nr`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eil. Nr. | — |
| `isdavimas` | `date` | `D` | `4` | `open` | — | Pažymėjimo išdavimo data | — |
| `pazymejimo_nr` | `string` | — | `2` | `open` | — | Pažymėjimo numeris | — |
| `adresas` | `ref` | [/datasets/gov/rc/ar/adresotaskas/AdresoTaskas](../../rc/ar/adresotaskas/AdresoTaskas.md) | `3` | `open` | — | Sandėlio / terminalo adresas | — |
| `ukio_subjektas` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_pavadinimas]](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `2` | `open` | — | Ūkio subjektas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/tikrinimo_vietos.csv
