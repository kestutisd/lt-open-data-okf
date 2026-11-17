---
type: Table
title: "ValstybesDalyvis — Valstybės ir (ar) savivaldybių juridinių asmenų dalyvių duomenys"
description: "Spinta table datasets/gov/rc/jadis/valstybes_dalyviai/ValstybesDalyvis (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jadis/valstybes_dalyviai/ValstybesDalyvis"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jadis/valstybes_dalyviai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/valstybes_dalyviai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# ValstybesDalyvis — Valstybės ir (ar) savivaldybių juridinių asmenų dalyvių duomenys

- **Model:** `datasets/gov/rc/jadis/valstybes_dalyviai/ValstybesDalyvis`[^manifest]
- **Dataset:** [Valstybės ir (ar) savivaldybių juridinių asmenų dalyvių duomenys](../valstybes_dalyviai.md) (`datasets/gov/rc/jadis/valstybes_dalyviai`)
- **Manifest CSV:** [datasets/gov/rc/jadis/valstybes_dalyviai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/valstybes_dalyviai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jadis/valstybes_dalyviai/ValstybesDalyvis`
- **Primary Key (`ref`):** `juridinis_asmuo`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../../jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Juridinio asmuo iš Juridinių asmenų registro | — |
| `forma` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Forma](../../jar/formos_statusai/Forma.md) | `4` | `open` | — | Juridinio asmens teisinė forma iš Juridinių asmenų registro | — |
| `statusas` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Statusas](../../jar/formos_statusai/Statusas.md) | `4` | `open` | — | Juridinio asmens teisinis statusas iš Juridinių asmenų registro | — |
| `ja_reg_data` | `date` | `D` | `4` | `open` | — | Juridinio asmens įregistravimo į Juridinių asmenų registrą data | — |
| `ne_juridinis_asmuo` | `ref` | [/datasets/gov/rc/jar/ne_juridiniai_asmenys/NeJuridinisAsmuo](../../jar/ne_juridiniai_asmenys/NeJuridinisAsmuo.md) | `4` | `open` | — | Juridinio asmens dalyvis ne juridinis asmuo iš Juridinių asmenų registro | — |
| `dal_dalys` | `number` | — | `3` | `open` | — | Juridiniame asmenyje dalyvaujančių dalyvių dalys juridiniame asmenyje procentais | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jadis/valstybes_dalyviai.csv
