---
type: Table
title: "NeveiksnusAmziusLytis — NIRVAR statistika apie teismo tvarka neveiksniais pripažintus asmenis pagal amžiaus grupes ir lytį"
description: "Spinta table datasets/gov/rc/nirvar/neveiksnus_pagal_amziu_lyti/NeveiksnusAmziusLytis (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/nirvar/neveiksnus_pagal_amziu_lyti/NeveiksnusAmziusLytis"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/nirvar/neveiksnus_pagal_amziu_lyti.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/nirvar/neveiksnus_pagal_amziu_lyti.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# NeveiksnusAmziusLytis — NIRVAR statistika apie teismo tvarka neveiksniais pripažintus asmenis pagal amžiaus grupes ir lytį

- **Model:** `datasets/gov/rc/nirvar/neveiksnus_pagal_amziu_lyti/NeveiksnusAmziusLytis`[^manifest]
- **Dataset:** [NIRVAR statistika apie teismo tvarka neveiksniais pripažintus asmenis pagal amžiaus grupes ir lytį](../neveiksnus_pagal_amziu_lyti.md) (`datasets/gov/rc/nirvar/neveiksnus_pagal_amziu_lyti`)
- **Manifest CSV:** [datasets/gov/rc/nirvar/neveiksnus_pagal_amziu_lyti.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/nirvar/neveiksnus_pagal_amziu_lyti.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/nirvar/neveiksnus_pagal_amziu_lyti/NeveiksnusAmziusLytis`
- **Primary Key (`ref`):** `amziaus_grupe, asm_lytis`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `amziaus_grupe` | `string` | — | `4` | `open` | — | Ribotai veiksnių asmenų amžiaus grupė (18-24; 25-34; 35-44; 45-54; 55-64; 65-84; 85+) | — |
| `asm_lytis` | `string` | — | `4` | `open` | — | Ribotai veiksnių asmenų lytis (V – vyras / M- moteris) | — |
| `neveiksniu_asm_skaicius` | `string` | — | `3` | `open` | — | Neveiksnių asmenų skaičius | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `amziaus_grupe` | `"18-24"` | — | — | Nuo 18 iki 24 | — |
| `amziaus_grupe` | `"25-34"` | — | — | Nuo 25 iki 34 | — |
| `amziaus_grupe` | `"35-44"` | — | — | Nuo 35 iki 44 | — |
| `amziaus_grupe` | `"45-54"` | — | — | Nuo 45 iki 54 | — |
| `amziaus_grupe` | `"55-64"` | — | — | Nuo 55 iki 64 | — |
| `amziaus_grupe` | `"65-84"` | — | — | Nuo 65 iki 84 | — |
| `amziaus_grupe` | `"85+"` | — | — | Nuo 85 | — |
| `asm_lytis` | `"V"` | — | — | Vyras | — |
| `asm_lytis` | `"M"` | — | — | Moteris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/nirvar/neveiksnus_pagal_amziu_lyti.csv
