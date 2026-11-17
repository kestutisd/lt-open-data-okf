---
type: Table
title: "IregistruotasParamosGavejas — Juridinių asmenų registre įregistruoti paramos gavėjai"
description: "Spinta table datasets/gov/rc/jar/iregistruoti_paramos_gavejai/IregistruotasParamosGavejas (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/iregistruoti_paramos_gavejai/IregistruotasParamosGavejas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/iregistruoti_paramos_gavejai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/iregistruoti_paramos_gavejai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# IregistruotasParamosGavejas — Juridinių asmenų registre įregistruoti paramos gavėjai

- **Model:** `datasets/gov/rc/jar/iregistruoti_paramos_gavejai/IregistruotasParamosGavejas`[^manifest]
- **Dataset:** [Juridinių asmenų registre įregistruoti paramos gavėjai (pagal įregistruotą statusą „PARAMOS GAVĖJAI“)](../iregistruoti_paramos_gavejai.md) (`datasets/gov/rc/jar/iregistruoti_paramos_gavejai`)
- **Manifest CSV:** [datasets/gov/rc/jar/iregistruoti_paramos_gavejai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/iregistruoti_paramos_gavejai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/iregistruoti_paramos_gavejai/IregistruotasParamosGavejas`
- **Primary Key (`ref`):** `juridinis_asmuo`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Juridinio asmens pavadinimas Juridinių asmenų registre | — |
| `paramos_gav_nuo` | `date` | `D` | `4` | `open` | — | Paramos gavėjo statuso įregistravimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/iregistruoti_paramos_gavejai.csv
