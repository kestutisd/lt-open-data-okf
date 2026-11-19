---
type: Table
title: "Juridinis — Juridiniai asmenys"
description: "Kuriuose dirba visuomenės sveikatos specialistai"
resource: "https://get.data.gov.lt/datasets/gov/hi/specialistai/Juridinis"
tags: [gov, hi, juridinis, deployed, level-3, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/specialistai.csv#L21"
    title: "atviriduomenys/manifest — datasets/gov/hi/specialistai.csv#L21"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1106/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/specialistai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Juridinis — Juridiniai asmenys

Kuriuose dirba visuomenės sveikatos specialistai[^manifest]

- **Model:** `datasets/gov/hi/specialistai/Juridinis`[^manifest]
- **Dataset:** [Visuomenės sveikatos priežiūros specialistų duomenys](../specialistai.md) (`datasets/gov/hi/specialistai`)[^manifest]
- **Manifest CSV:** [datasets/gov/hi/specialistai.csv#L21](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/specialistai.csv#L21)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/specialistai/Juridinis` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `jar` | `ref` | [JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) (`level=4 UUID` via `JuridinisAsmuo[ja_kodas]`: `jar._id`) | `4` | `open` | — | Įstaigos juridinio asmens kodas | — |
| `istaiga` | `ref` | [JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) (`level=4 UUID` via `JuridinisAsmuo[ja_pavadinimas]`: `istaiga._id`) | `4` | `open` | — | Įstaigos pavadinimas | — |
| `ikurimas` | `date` | `D` | `4` | `open` | — | Įstaigos įkūrimo data | — |
| `istaigos_tipas` | `string` | — | `4` | `open` | — | Įstaigos tipas | Savivaldybių visuomenės sveikatos biurai, Nacionalinis visuomenės sveikatos centras, Specializuotos visuomenės sveikatos priežiūros įstaigos |
| `apskritis` | `string` | — | `2` | `open` | — | Apskritis, kur registruotas įstaiga | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybė, kur registruotas įstaiga | — |
| `padalinys` | `string` | — | `4` | `open` | — | Įstaigos padalinys | — |
| `specialistai` | `integer` | `U` | `4` | `open` | — | Visuomenės sveikatos specialistų skaičius | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/specialistai.csv#L21 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/specialistai.csv#L21)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/specialistai (https://data.gov.lt/datasets/1106/)
