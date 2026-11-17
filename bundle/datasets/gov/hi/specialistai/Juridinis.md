---
type: Table
title: "Juridinis — Juridiniai asmenys"
description: "Kuriuose dirba visuomenės sveikatos specialistai"
resource: "https://get.data.gov.lt/datasets/gov/hi/specialistai/Juridinis"
tags: [gov, hi, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/hi/specialistai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/specialistai.csv#L21"
    last_modified: "2026-11-11T14:39:20Z"
---

# Juridinis — Juridiniai asmenys

Kuriuose dirba visuomenės sveikatos specialistai

- **Model:** `datasets/gov/hi/specialistai/Juridinis`[^manifest]
- **Dataset:** [Visuomenės sveikatos priežiūros specialistų duomenys](../specialistai.md) (`datasets/gov/hi/specialistai`)
- **Manifest CSV:** [datasets/gov/hi/specialistai.csv#L21](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/specialistai.csv#L21)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/specialistai/Juridinis`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `jar` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_kodas]](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Įstaigos juridinio asmens kodas | — |
| `istaiga` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_pavadinimas]](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Įstaigos pavadinimas | — |
| `ikurimas` | `date` | `D` | `4` | `open` | — | Įstaigos įkūrimo data | — |
| `istaigos_tipas` | `string` | — | `4` | `open` | — | Įstaigos tipas | Savivaldybių visuomenės sveikatos biurai, Nacionalinis visuomenės sveikatos centras, Specializuotos visuomenės sveikatos priežiūros įstaigos |
| `apskritis` | `string` | — | `2` | `open` | — | Apskritis, kur registruotas įstaiga | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybė, kur registruotas įstaiga | — |
| `padalinys` | `string` | — | `4` | `open` | — | Įstaigos padalinys | — |
| `specialistai` | `integer` | `U` | `4` | `open` | — | Visuomenės sveikatos specialistų skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/specialistai.csv
