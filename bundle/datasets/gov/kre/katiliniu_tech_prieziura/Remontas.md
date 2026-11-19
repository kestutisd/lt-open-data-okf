---
type: Table
title: "Remontas — Klaipėdos rajono energijos katilinių techninės priežiūros sąrašas"
description: "Katilinių techninės priežiūros ir remonto registras yra skirtas kaupti duomenis apie Klaipėdos rajone esančių ir UAB 'Klaipėdos rajono energija' prižiūrimų katilinių techninę priežiūrą ir remontą."
resource: "https://get.data.gov.lt/datasets/gov/kre/katiliniu_tech_prieziura/Remontas"
tags: [gov, kre, remontas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kre/katiliniu_tech_prieziura.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/kre/katiliniu_tech_prieziura.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2747/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kre/katiliniu_tech_prieziura"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Remontas — Klaipėdos rajono energijos katilinių techninės priežiūros sąrašas

Katilinių techninės priežiūros ir remonto registras yra skirtas kaupti duomenis apie Klaipėdos rajone esančių ir UAB 'Klaipėdos rajono energija' prižiūrimų katilinių techninę priežiūrą ir remontą.[^manifest]

- **Model:** `datasets/gov/kre/katiliniu_tech_prieziura/Remontas`[^manifest]
- **Dataset:** [Klaipėdos rajono energijos katilinių techninės priežiūros sąrašas](../katiliniu_tech_prieziura.md) (`datasets/gov/kre/katiliniu_tech_prieziura`)[^manifest]
- **Manifest CSV:** [datasets/gov/kre/katiliniu_tech_prieziura.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kre/katiliniu_tech_prieziura.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kre/katiliniu_tech_prieziura/Remontas` (`deployed`)[^manifest]
- **Provider:** `kre` — Klaipėdos rajono energija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `eiles_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eiles_nr` | `string` | — | `4` | `open` | — | Eilės numeris | — |
| `remonto_data` | `date` | `D` | `4` | `open` | — | Techninės priežiūros ir/ar remonto data | — |
| `istaigos_pavadinimas` | `string` | — | `4` | `open` | — | Savivaldybei priklausančios įstaigos, kurios teritorijoje yra katilinė, pavadinimas | — |
| `katilines_adresas` | `string` | — | `4` | `open` | — | Tikslus objekto, kuriame yra katilinė, adresas | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | X koordinatė | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Y koordinatė | — |
| `atlikti_darbai` | `string` | — | `4` | `open` | — | Atlikti techninės priežiūros ir/ar remonto darbai | — |
| `pastabos` | `string` | — | `4` | `open` | — | Pastabos | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kre/katiliniu_tech_prieziura.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kre/katiliniu_tech_prieziura.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kre/katiliniu_tech_prieziura (https://data.gov.lt/datasets/2747/)
