---
type: Table
title: "CBARusis — Gyventojų registro civilinės būklės aktų įrašų rūšių klasifikatorius"
description: "Spinta table datasets/gov/rc/gr/cba_rusys/CBARusis (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/gr/cba_rusys/CBARusis"
tags: [gov, rc, cbarusis, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/cba_rusys.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/gr/cba_rusys.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1755/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/gr/cba_rusys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# CBARusis — Gyventojų registro civilinės būklės aktų įrašų rūšių klasifikatorius

- **Model:** `datasets/gov/rc/gr/cba_rusys/CBARusis`[^manifest]
- **Dataset:** [Gyventojų registro civilinės būklės aktų įrašų rūšių klasifikatorius](../cba_rusys.md) (`datasets/gov/rc/gr/cba_rusys`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/gr/cba_rusys.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/cba_rusys.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/gr/cba_rusys/CBARusis` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas, kodo_kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `string` | — | `4` | `open` | — | Gyventojų registro civilinės būklės akto įrašo rūšies kodas | — |
| `aprasymas` | `string` | — | `3` | `open` | — | Gyventojų registro civilinės būklės akto įrašo rūšies aprašymas | — |
| `kodo_kodas` | `string` | — | `4` | `open` | — | Gyventojų registro civilinės būklės akto įrašo rūšies kodo kodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/gr/cba_rusys.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/cba_rusys.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/gr/cba_rusys (https://data.gov.lt/datasets/1755/)
