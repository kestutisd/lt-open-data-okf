---
type: Table
title: "NtrKainosTipas — NTR leistini sandorių kainų tipai"
description: "Spinta table datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai/NtrKainosTipas (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai/NtrKainosTipas"
tags: [gov, rc, ntrkainostipas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai.csv#L35"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai.csv#L35"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1900/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NtrKainosTipas — NTR leistini sandorių kainų tipai

- **Model:** `datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai/NtrKainosTipas`[^manifest]
- **Dataset:** [Kiti NTR klasifikatoriai](../ntr_kiti_klasifikatoriai.md) (`datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai.csv#L35](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai.csv#L35)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai/NtrKainosTipas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `sant_tipas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sant_tipas` | `integer` | — | `4` | `open` | — | Sandorio tipas | — |
| `sakt_tipas` | `integer` | — | `3` | `open` | — | Sandorio kainos tipas | — |
| `lsank_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai.csv#L35 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai.csv#L35)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai (https://data.gov.lt/datasets/1900/)
