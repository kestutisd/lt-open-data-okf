---
type: Table
title: "LisRusis — Licencijų rūšių klasifikatorius"
description: "Spinta table datasets/gov/rc/lis/lis_rusys_tipai/LisRusis (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/lis/lis_rusys_tipai/LisRusis"
tags: [gov, rc, lisrusis, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_rusys_tipai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/lis/lis_rusys_tipai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1808/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/lis/lis_rusys_tipai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# LisRusis — Licencijų rūšių klasifikatorius

- **Model:** `datasets/gov/rc/lis/lis_rusys_tipai/LisRusis`[^manifest]
- **Dataset:** [Licencijų informacinė sistemos tipų ir rūšių klasifikatoriai](../lis_rusys_tipai.md) (`datasets/gov/rc/lis/lis_rusys_tipai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/lis/lis_rusys_tipai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_rusys_tipai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/lis/lis_rusys_tipai/LisRusis` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `integer` | — | `4` | `open` | — | Licencijos rūšies kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Licencijos rūšies pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/lis/lis_rusys_tipai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_rusys_tipai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/lis/lis_rusys_tipai (https://data.gov.lt/datasets/1808/)
