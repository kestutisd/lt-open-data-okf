---
type: Table
title: "Sarasas — Klaipėdos rajono energijos katilinių sąrašas"
description: "Katilinių sąrašo registras skirtas kaupti duomenis apie Klaipėdos rajone esančias ir UAB 'Klaipėdos rajono energija' prižiūrimas katilines."
resource: "https://get.data.gov.lt/datasets/gov/kre/katiliniu_sarasas/Sarasas"
tags: [gov, kre, sarasas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kre/katiliniu_sarasas.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/kre/katiliniu_sarasas.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2746/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kre/katiliniu_sarasas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Sarasas — Klaipėdos rajono energijos katilinių sąrašas

Katilinių sąrašo registras skirtas kaupti duomenis apie Klaipėdos rajone esančias ir UAB 'Klaipėdos rajono energija' prižiūrimas katilines.[^manifest]

- **Model:** `datasets/gov/kre/katiliniu_sarasas/Sarasas`[^manifest]
- **Dataset:** [Klaipėdos rajono energijos katilinių sąrašas](../katiliniu_sarasas.md) (`datasets/gov/kre/katiliniu_sarasas`)[^manifest]
- **Manifest CSV:** [datasets/gov/kre/katiliniu_sarasas.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kre/katiliniu_sarasas.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kre/katiliniu_sarasas/Sarasas` (`deployed`)[^manifest]
- **Provider:** `kre` — Klaipėdos rajono energija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `eiles_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eiles_nr` | `string` | — | `4` | `open` | — | Eilės numeris | — |
| `istaigos_pavadinimas` | `string` | — | `3` | `open` | — | Savivaldybei priklausančios įstaigos, kurios teritorijoje yra katilinė, pavadinimas | — |
| `katilines_adresas` | `string` | — | `3` | `open` | — | Tikslus objekto, kuriame yra katilinė, adresas | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | X koordinatė | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Y koordinatė | — |
| `aptarnaujama_nuo` | `date` | `Y` | `4` | `open` | — | Įstaiga aptarnaujama nuo | — |
| `aptarnaujama_iki` | `date` | `Y` | `4` | `open` | — | Įstaiga aptarnaujama iki | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kre/katiliniu_sarasas.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kre/katiliniu_sarasas.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kre/katiliniu_sarasas (https://data.gov.lt/datasets/2746/)
