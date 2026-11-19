---
type: Table
title: "EkonominesVeiklosRusis — Ekonominės veikos rūšis (EVRK2.1)"
description: "Ekonominės veiklos klasifikatorius versija 2.1"
resource: "https://get.data.gov.lt/datasets/gov/lsd/cl/evrk2_1/EkonominesVeiklosRusis"
tags: [gov, lsd, ekonominesveiklosrusis, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/cl/evrk2_1.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lsd/cl/evrk2_1.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2919/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/cl/evrk2_1"
    author: "team:vda"
    last_modified: "2026-02-02T00:00:00Z"
---

# EkonominesVeiklosRusis — Ekonominės veikos rūšis (EVRK2.1)

**Dataset Context:** Ekonominės veiklos klasifikatorius versija 2.1[^manifest]

- **Model:** `datasets/gov/lsd/cl/evrk2_1/EkonominesVeiklosRusis`[^manifest]
- **Dataset:** [Ekonominės veiklos klasifikatorius versija 2.1](../evrk2_1.md) (`datasets/gov/lsd/cl/evrk2_1`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/cl/evrk2_1.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/cl/evrk2_1.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/cl/evrk2_1/EkonominesVeiklosRusis` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-02-02`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `string` | — | `4` | `open` | — | EVRK kodas | — |
| `pavadinimas_lt` | `string` | — | `4` | `open` | — | Pavadinimas lietuviškai | — |
| `pavadinimas_en` | `string` | — | `4` | `open` | — | Pavadinimas angliškai | — |
| `pastabos_lt` | `string` | — | `4` | `open` | — | Aiškinamosios pastabos lietuviškai | — |
| `pastabos_en` | `string` | — | `4` | `open` | — | Aiškinamosios pastabos angliškai | — |
| `lygmens_pavadinimas` | `string` | — | `4` | `open` | — | Aiškinamasis lygmens aprašas | — |
| `lygmuo` | `integer` | — | `4` | `open` | — | Lygmens kodas | — |

# Related References

- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/cl/evrk2_1.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/cl/evrk2_1.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/cl/evrk2_1 (https://data.gov.lt/datasets/2919/)
