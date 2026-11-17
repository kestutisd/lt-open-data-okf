---
type: Table
title: "MirtiesPriezastis — Mirtys ir jų priežastys Lietuvoje"
description: "Spinta table datasets/gov/lsd/sveikata/mirciu_priezastys/MirtiesPriezastis (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/mirciu_priezastys/MirtiesPriezastis"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/mirciu_priezastys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/mirciu_priezastys.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# MirtiesPriezastis — Mirtys ir jų priežastys Lietuvoje

- **Model:** `datasets/gov/lsd/sveikata/mirciu_priezastys/MirtiesPriezastis`[^manifest]
- **Dataset:** [datasets/gov/lsd/sveikata/mirciu_priezastys](../mirciu_priezastys.md) (`datasets/gov/lsd/sveikata/mirciu_priezastys`)
- **Manifest CSV:** [datasets/gov/lsd/sveikata/mirciu_priezastys.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/mirciu_priezastys.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/mirciu_priezastys/MirtiesPriezastis`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus įdentifikatorius | — |
| `mirties_metai` | `integer` | — | `2` | `open` | — | Faktinės asmens mirties datos metai | — |
| `mirties_menuo` | `string` | — | `3` | `open` | — | Faktinės asmens mirties datos mėnuo (du skaitmenys) | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Asmens amžiaus mirties dieną grupė, dešimties metų rėžiais | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `priezastis` | `ref` | [/datasets/gov/vlk/tlk10am/Tlk10am](../../../vlk/tlk10am/Tlk10am.md) | `4` | `open` | — | Triženklė TLK-10 diagnozė, klasifikatorius | Nerevizuota pagrindinė asmens mirties priezastis (triženklė TLK-10 diagnozė, klasifikatorius), kokią ją nurodė sveikatos priežiūros specialistas. Palčiau apie sąvokas 'pagrindinė mirties priežastis', 'tarpinė mirties priežastis' ir 'tiesioginė mirties priežastis' skaitykite čia: https://hi.lt/uploads/pdf/padaliniai/MPR/MML_rekomendacijos.pdf |
| `asmenu_sk` | `integer` | — | `4` | `open` | — | Mirusių asmenų skaičius | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"mot"` | — | — | Moteris | — |
| `lytis` | `"vyr"` | — | — | Vyras | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `mirties_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/mirciu_priezastys.csv
