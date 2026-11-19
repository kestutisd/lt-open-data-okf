---
type: Table
title: "Lankymas — Neformaliojo vaikų švietimo programų lankymas"
description: "Viena eilutė atitinka vieną neformaliojo vaikų švietimo programą lankiusių mokinių skaičių atitinkamais mokslo metais"
resource: "https://get.data.gov.lt/datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos/Lankymas"
tags: [gov, nsa, lankymas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos.csv#L46"
    title: "atviriduomenys/manifest — datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos.csv#L46"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3997/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Lankymas — Neformaliojo vaikų švietimo programų lankymas

Viena eilutė atitinka vieną neformaliojo vaikų švietimo programą lankiusių mokinių skaičių atitinkamais mokslo metais[^manifest]

- **Model:** `datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos/Lankymas`[^manifest]
- **Dataset:** [Neformaliojo vaikų švietimo programos](../neformaliojo_vaiku_svietimo_programos.md) (`datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos`)[^manifest]
- **Manifest CSV:** [datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos.csv#L46](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos.csv#L46)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos/Lankymas` (`deployed`)[^manifest]
- **Provider:** `nsa` — Nacionalinė švietimo agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus lentelės raktas | — |
| `programos_id` | `string` | — | `4` | `open` | — | Programos identifikatorius | — |
| `mokslo_metai` | `string` | — | `4` | `open` | — | Mokslo metai | — |
| `mok_sk` | `integer` | — | `4` | `open` | — | Mokinių, lankiusių neformaliojo švietimo programą atitinkamais metais skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos.csv#L46 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos.csv#L46)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos (https://data.gov.lt/datasets/3997/)
