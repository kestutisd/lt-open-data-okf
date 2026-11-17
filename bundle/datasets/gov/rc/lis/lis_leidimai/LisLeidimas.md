---
type: Table
title: "LisLeidimas — Licencijų informacinės sistemos duomenys apie valstybės institucijų ūkio subjektams išduotus leidimus"
description: "Spinta table datasets/gov/rc/lis/lis_leidimai/LisLeidimas (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/lis/lis_leidimai/LisLeidimas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/lis/lis_leidimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_leidimai.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# LisLeidimas — Licencijų informacinės sistemos duomenys apie valstybės institucijų ūkio subjektams išduotus leidimus

- **Model:** `datasets/gov/rc/lis/lis_leidimai/LisLeidimas`[^manifest]
- **Dataset:** [Valstybės institucijų ūkio subjektams išduoti LEIDIMAI](../lis_leidimai.md) (`datasets/gov/rc/lis/lis_leidimai`)
- **Manifest CSV:** [datasets/gov/rc/lis/lis_leidimai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_leidimai.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/lis/lis_leidimai/LisLeidimas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `numeris` | `string` | — | `4` | `open` | — | Registracijos numeris | — |
| `isdavimo_data` | `date` | `D` | `4` | `open` | — | Išdavimo data | — |
| `galioja_nuo` | `date` | `D` | `4` | `open` | — | Galiojimo data nuo | — |
| `galioja_iki` | `date` | `D` | `4` | `open` | — | Galiojimo data iki | — |
| `juridinis_asmuo` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../../jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Licenciją išduodanti institucija | — |
| `gavejo_pavadinimas` | `string` | — | `3` | `open` | — | Gavėjo pavadinimas (fizinio asmens atveju tik įrašas „fizinis asmuo“) | — |
| `gavejo_kodas` | `string` | — | `3` | `open` | — | Gavėjo kodas (fizinio asmens atveju tik įrašas „fizinis asmuo“) | — |
| `lic_tipas` | `ref` | [/datasets/gov/rc/lis/lis_rusys_tipai/LisTipas](../lis_rusys_tipai/LisTipas.md) | `4` | `open` | — | Tipo kodas | — |
| `lic_rusis` | `ref` | [/datasets/gov/rc/lis/lis_rusys_tipai/LisRusis](../lis_rusys_tipai/LisRusis.md) | `4` | `open` | — | Rūšies kodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/lis/lis_leidimai.csv
