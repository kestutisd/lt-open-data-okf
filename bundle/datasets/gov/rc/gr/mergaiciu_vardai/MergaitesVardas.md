---
type: Table
title: "MergaitesVardas — Populiariausi mergaičių vardai Lietuvoje, TOP 20 (mergaitės vardas, gimimo metai, bendravardžių kiekis)"
description: "Spinta table datasets/gov/rc/gr/mergaiciu_vardai/MergaitesVardas (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/gr/mergaiciu_vardai/MergaitesVardas"
tags: [gov, rc, mergaitesvardas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/mergaiciu_vardai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/gr/mergaiciu_vardai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1751/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/gr/mergaiciu_vardai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# MergaitesVardas — Populiariausi mergaičių vardai Lietuvoje, TOP 20 (mergaitės vardas, gimimo metai, bendravardžių kiekis)

- **Model:** `datasets/gov/rc/gr/mergaiciu_vardai/MergaitesVardas`[^manifest]
- **Dataset:** [Populiariausi mergaičių vardai Lietuvoje, TOP 20 (mergaitės vardas, gimimo metai, bendravardžių...](../mergaiciu_vardai.md) (`datasets/gov/rc/gr/mergaiciu_vardai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/gr/mergaiciu_vardai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/mergaiciu_vardai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/gr/mergaiciu_vardai/MergaitesVardas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `gimimo_metai, gimimo_ketvirtis, nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Vardo eilės numeris šiame rinkinyje (pagal populiarumą, 1 - populiariausias); | — |
| `vardas` | `string` | — | `3` | `open` | — | Mergaitės vardas | — |
| `viso_vardas` | `integer` | `U` | `4` | `open` | — | Skaičius vardo (iš viso nurodytu laikotarpiu) įrašyto į Gyventojų registrą (bendravardžių kiekis) | — |
| `gimimo_metai` | `integer` | — | `2` | `open` | — | Gyventojo gimimo datos metai | — |
| `gimimo_ketvirtis` | `string` | — | `2` | `open` | — | Gyventojo gimimo datos ketvirtis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/gr/mergaiciu_vardai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/mergaiciu_vardai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/gr/mergaiciu_vardai (https://data.gov.lt/datasets/1751/)
