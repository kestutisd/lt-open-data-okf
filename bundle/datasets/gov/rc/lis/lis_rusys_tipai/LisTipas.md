---
type: Table
title: "LisTipas — Licencijų tipų klasifikatorius"
description: "Spinta table datasets/gov/rc/lis/lis_rusys_tipai/LisTipas (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/lis/lis_rusys_tipai/LisTipas"
tags: [gov, rc, listipas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_rusys_tipai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/rc/lis/lis_rusys_tipai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1808/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/lis/lis_rusys_tipai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# LisTipas — Licencijų tipų klasifikatorius

- **Model:** `datasets/gov/rc/lis/lis_rusys_tipai/LisTipas`[^manifest]
- **Dataset:** [Licencijų informacinė sistemos tipų ir rūšių klasifikatoriai](../lis_rusys_tipai.md) (`datasets/gov/rc/lis/lis_rusys_tipai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/lis/lis_rusys_tipai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_rusys_tipai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/lis/lis_rusys_tipai/LisTipas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `integer` | — | `4` | `open` | — | Licencijos tipo kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Licencijos tipo pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/lis/lis_rusys_tipai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_rusys_tipai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/lis/lis_rusys_tipai (https://data.gov.lt/datasets/1808/)
