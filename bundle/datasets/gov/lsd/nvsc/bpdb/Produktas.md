---
type: Table
title: "Produktas — Produktai"
description: "Lentelė „Produktai“. Lentelę sudaro: negrįžtamai šifruotas produkto identifikatorius, pavadinimas, gamintojas, autorizacijos liudijimo sąlygos ir pastabos."
resource: "https://get.data.gov.lt/datasets/gov/lsd/nvsc/bpdb/Produktas"
tags: [gov, lsd, produktas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nvsc/bpdb.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lsd/nvsc/bpdb.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2917/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/nvsc/bpdb"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Produktas — Produktai

Lentelė „Produktai“. Lentelę sudaro: negrįžtamai šifruotas produkto identifikatorius, pavadinimas, gamintojas, autorizacijos liudijimo sąlygos ir pastabos. Produktų pastabos aktualios tik produktams su galiojančiais autorizacijos liudijimais. Vienas įrašas atitinka vieną produktą.[^manifest]

- **Model:** `datasets/gov/lsd/nvsc/bpdb/Produktas`[^manifest]
- **Dataset:** [Biocidinių produktų duomenys](../bpdb.md) (`datasets/gov/lsd/nvsc/bpdb`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/nvsc/bpdb.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nvsc/bpdb.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/nvsc/bpdb/Produktas` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `produkto_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `produkto_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `produkto_pav` | `string` | — | `2` | `open` | — | Pavadinimas | — |
| `produkto_gamintojas` | `string` | — | `2` | `open` | — | Gamintojas | — |
| `autorizacijos_liudijimo_salygos` | `string` | — | `2` | `open` | — | Sąlygos, pagal kurias suteiktas autorizacijos liudijimas produktui | — |
| `pastaba` | `string` | — | `2` | `open` | — | Pastabos, aktualios tik produktams su galiojančiais autorizacijos liudijimais | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/nvsc/bpdb.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nvsc/bpdb.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/nvsc/bpdb (https://data.gov.lt/datasets/2917/)
