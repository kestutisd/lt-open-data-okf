---
type: Table
title: "Muitine — Prekių saugojimo ir muitinio tikrinimo vietos, pripažintos tinkamomis augalams, augaliniams produktams ir kitiems susijusiems objektams laikyti"
description: "Spinta table datasets/gov/vat/tikrinimo_vietos/Muitine (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/tikrinimo_vietos/Muitine"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/tikrinimo_vietos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/tikrinimo_vietos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Muitine — Prekių saugojimo ir muitinio tikrinimo vietos, pripažintos tinkamomis augalams, augaliniams produktams ir kitiems susijusiems objektams laikyti

- **Model:** `datasets/gov/vat/tikrinimo_vietos/Muitine`[^manifest]
- **Dataset:** [datasets/gov/vat/tikrinimo_vietos](../tikrinimo_vietos.md) (`datasets/gov/vat/tikrinimo_vietos`)
- **Manifest CSV:** [datasets/gov/vat/tikrinimo_vietos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/tikrinimo_vietos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/tikrinimo_vietos/Muitine`
- **Primary Key (`ref`):** `eil_nr`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eil. Nr. | — |
| `pazymejimo_isdavimas` | `date` | `D` | `4` | `open` | — | Pažymėjimo išdavimo data | — |
| `pazymejimo_nr` | `string` | — | `4` | `open` | — | Pažymėjimo numeris | — |
| `terminalas` | `ref` | [/datasets/gov/rc/ar/adresotaskas/AdresoTaskas](../../rc/ar/adresotaskas/AdresoTaskas.md) | `3` | `open` | — | Sandėlio / terminalo adresas | — |
| `tipo_nr` | `string` | — | `1` | `open` | — | Sandėlio / terminalo tipas ir numeris | — |
| `ukio_subjektas` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_pavadinimas]](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `2` | `open` | — | Ūkio subjektas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/tikrinimo_vietos.csv
