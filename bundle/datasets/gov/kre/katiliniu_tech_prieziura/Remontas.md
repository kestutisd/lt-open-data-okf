---
type: Table
title: "Remontas — Klaipėdos rajono energijos katilinių techninės priežiūros sąrašas"
description: "Katilinių techninės priežiūros ir remonto registras yra skirtas kaupti duomenis apie Klaipėdos rajone esančių ir UAB 'Klaipėdos rajono energija' prižiūrimų katilinių techninę priežiūrą ir remontą."
resource: "https://get.data.gov.lt/datasets/gov/kre/katiliniu_tech_prieziura/Remontas"
tags: [gov, kre, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kre/katiliniu_tech_prieziura.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kre/katiliniu_tech_prieziura.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Remontas — Klaipėdos rajono energijos katilinių techninės priežiūros sąrašas

Katilinių techninės priežiūros ir remonto registras yra skirtas kaupti duomenis apie Klaipėdos rajone esančių ir UAB 'Klaipėdos rajono energija' prižiūrimų katilinių techninę priežiūrą ir remontą.

- **Model:** `datasets/gov/kre/katiliniu_tech_prieziura/Remontas`[^manifest]
- **Dataset:** [Klaipėdos rajono energijos katilinių techninės priežiūros sąrašas](../katiliniu_tech_prieziura.md) (`datasets/gov/kre/katiliniu_tech_prieziura`)
- **Manifest CSV:** [datasets/gov/kre/katiliniu_tech_prieziura.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kre/katiliniu_tech_prieziura.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kre/katiliniu_tech_prieziura/Remontas`
- **Primary Key (`ref`):** `eiles_nr`
- **Level:** `4`

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

[^manifest]: atviriduomenys/manifest — datasets/gov/kre/katiliniu_tech_prieziura.csv
