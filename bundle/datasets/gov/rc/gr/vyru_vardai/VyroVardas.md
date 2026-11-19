---
type: Table
title: "VyroVardas — Populiariausi vyrų vardai Lietuvoje nuo 1900 metų, TOP 50"
description: "Spinta table datasets/gov/rc/gr/vyru_vardai/VyroVardas (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/gr/vyru_vardai/VyroVardas"
tags: [gov, rc, vyrovardas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/vyru_vardai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/gr/vyru_vardai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1754/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/gr/vyru_vardai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# VyroVardas — Populiariausi vyrų vardai Lietuvoje nuo 1900 metų, TOP 50

- **Model:** `datasets/gov/rc/gr/vyru_vardai/VyroVardas`[^manifest]
- **Dataset:** [Populiariausi vyrų vardai Lietuvoje nuo 1900 metų, TOP 50](../vyru_vardai.md) (`datasets/gov/rc/gr/vyru_vardai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/gr/vyru_vardai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/vyru_vardai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/gr/vyru_vardai/VyroVardas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `vardas` | `string` | — | `3` | `open` | — | Vyro vardas | — |
| `viso_vardas` | `integer` | `U` | `4` | `open` | — | Vyrų, gimusių nuo 1900 m. ir kuriems suteiktas toks vardas, skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/gr/vyru_vardai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/vyru_vardai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/gr/vyru_vardai (https://data.gov.lt/datasets/1754/)
