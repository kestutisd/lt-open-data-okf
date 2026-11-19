---
type: Table
title: "Rodiklis — Dumblo susidarymas valymo įrenginiuose"
description: "SĮ \"Simno komunalininkas\" fiksuojamas dumblo susidarymas valymo įrenginiuose"
resource: "https://get.data.gov.lt/datasets/gov/simno_komun/dumblo_registras/Rodiklis"
tags: [gov, simno_komun, rodiklis, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/dumblo_registras.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/simno_komun/dumblo_registras.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2789/"
    title: "data.gov.lt DCAT-AP — datasets/gov/simno_komun/dumblo_registras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Rodiklis — Dumblo susidarymas valymo įrenginiuose

SĮ "Simno komunalininkas" fiksuojamas dumblo susidarymas valymo įrenginiuose[^manifest]

- **Model:** `datasets/gov/simno_komun/dumblo_registras/Rodiklis`[^manifest]
- **Dataset:** [Dumblo susidarymas valymo įrenginiuose](../dumblo_registras.md) (`datasets/gov/simno_komun/dumblo_registras`)[^manifest]
- **Manifest CSV:** [datasets/gov/simno_komun/dumblo_registras.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/dumblo_registras.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/simno_komun/dumblo_registras/Rodiklis` (`deployed`)[^manifest]
- **Provider:** `simno_komun` — Alytaus rajono savivaldybės įmonė „Simno komunalininkas“ *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA sukurtas šifruotas eilutės unikalus numeris | — |
| `atskaitos_menuo` | `date` | `M` | `4` | `open` | — | Atskaitos mėnuo | — |
| `vietove` | `string` | — | `4` | `open` | — | Valymo įrenginių vietovė | — |
| `rodikliai` | `string` | — | `4` | `open` | — | Rodiklių pavadinimai | — |
| `reiksmes` | `number` | — | `4` | `open` | — | Rodiklių reikšmės | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vietove` | — | `"Daugai"` | — | — | — |
| `vietove` | — | `"Simnas"` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/simno_komun/dumblo_registras.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/dumblo_registras.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/simno_komun/dumblo_registras (https://data.gov.lt/datasets/2789/)
