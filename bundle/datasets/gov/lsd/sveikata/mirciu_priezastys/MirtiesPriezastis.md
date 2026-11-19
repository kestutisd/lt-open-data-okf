---
type: Table
title: "MirtiesPriezastis — Mirtys ir jų priežastys Lietuvoje"
description: "Spinta table datasets/gov/lsd/sveikata/mirciu_priezastys/MirtiesPriezastis (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/mirciu_priezastys/MirtiesPriezastis"
tags: [gov, lsd, mirtiespriezastis, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/mirciu_priezastys.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/mirciu_priezastys.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2026/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/mirciu_priezastys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# MirtiesPriezastis — Mirtys ir jų priežastys Lietuvoje

- **Model:** `datasets/gov/lsd/sveikata/mirciu_priezastys/MirtiesPriezastis`[^manifest]
- **Dataset:** [Mirties priežastys pagal skaitmeninius medicininius mirties liudijimus](../mirciu_priezastys.md) (`datasets/gov/lsd/sveikata/mirciu_priezastys`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/mirciu_priezastys.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/mirciu_priezastys.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/mirciu_priezastys/MirtiesPriezastis` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus įdentifikatorius | — |
| `mirties_metai` | `integer` | — | `2` | `open` | — | Faktinės asmens mirties datos metai | — |
| `mirties_menuo` | `string` | — | `3` | `open` | — | Faktinės asmens mirties datos mėnuo (du skaitmenys) | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Asmens amžiaus mirties dieną grupė, dešimties metų rėžiais | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `priezastis` | `ref` | [Tlk10am](../../../vlk/tlk10am/Tlk10am.md) (`level=4 UUID`: `priezastis._id`) | `4` | `open` | — | Triženklė TLK-10 diagnozė, klasifikatorius | Nerevizuota pagrindinė asmens mirties priezastis (triženklė TLK-10 diagnozė, klasifikatorius), kokią ją nurodė sveikatos priežiūros specialistas. Palčiau apie sąvokas 'pagrindinė mirties priežastis', 'tarpinė mirties priežastis' ir 'tiesioginė mirties priežastis' skaitykite čia: https://hi.lt/uploads/pdf/padaliniai/MPR/MML_rekomendacijos.pdf |
| `asmenu_sk` | `integer` | — | `4` | `open` | — | Mirusių asmenų skaičius | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"mot"` | — | — | Moteris | — |
| `lytis` | `"vyr"` | — | — | Vyras | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `mirties_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/mirciu_priezastys.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/mirciu_priezastys.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/mirciu_priezastys (https://data.gov.lt/datasets/2026/)
