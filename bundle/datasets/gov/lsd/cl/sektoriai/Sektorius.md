---
type: Table
title: "Sektorius — Sektorius arba subsektorius"
description: "Spinta table datasets/gov/lsd/cl/sektoriai/Sektorius (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/cl/sektoriai/Sektorius"
tags: [gov, lsd, sektorius, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/cl/sektoriai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/lsd/cl/sektoriai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1928/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/cl/sektoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Sektorius — Sektorius arba subsektorius

- **Model:** `datasets/gov/lsd/cl/sektoriai/Sektorius`[^manifest]
- **Dataset:** [Sektorių ir subsektorių klasifikatoriai](../sektoriai.md) (`datasets/gov/lsd/cl/sektoriai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/cl/sektoriai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/cl/sektoriai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/cl/sektoriai/Sektorius` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `string` | — | `4` | `open` | — | Kodas | — |
| `pavadinimas_lt` | `string` | — | `2` | `open` | — | Pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/cl/sektoriai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/cl/sektoriai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/cl/sektoriai (https://data.gov.lt/datasets/1928/)
