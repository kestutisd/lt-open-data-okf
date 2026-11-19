---
type: Table
title: "Aprupinimas — Gyventojų aprūpinimas stabiliojo jodo preparatais pagal savivaldybes"
description: "Spinta table datasets/gov/essc/aprupinimas_jodo_preparatais/Aprupinimas (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/essc/aprupinimas_jodo_preparatais/Aprupinimas"
tags: [gov, essc, aprupinimas, deployed, level-4, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/essc/aprupinimas_jodo_preparatais.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/essc/aprupinimas_jodo_preparatais.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2371/"
    title: "data.gov.lt DCAT-AP — datasets/gov/essc/aprupinimas_jodo_preparatais"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Aprupinimas — Gyventojų aprūpinimas stabiliojo jodo preparatais pagal savivaldybes

- **Model:** `datasets/gov/essc/aprupinimas_jodo_preparatais/Aprupinimas`[^manifest]
- **Dataset:** [Gyventojų aprūpinimas stabiliojo jodo preparatais pagal savivaldybes](../aprupinimas_jodo_preparatais.md) (`datasets/gov/essc/aprupinimas_jodo_preparatais`)[^manifest]
- **Manifest CSV:** [datasets/gov/essc/aprupinimas_jodo_preparatais.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/essc/aprupinimas_jodo_preparatais.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/essc/aprupinimas_jodo_preparatais/Aprupinimas` (`deployed`)[^manifest]
- **Provider:** `essc` — Ekstremalių sveikatai situacijų centras *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_2`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė | — |
| `metai` | `date` | `Y` | `4` | `open` | — | Metai | — |
| `suaugusiuju_sk_bal` | `integer` | — | `4` | `open` | — | Suaugusiųjų gyventojų skaičius savivaldybėje balandį | — |
| `vaiku_sk_bal` | `integer` | — | `4` | `open` | — | Vaikų iki 12 m. skaičius savivaldybėje balandį | — |
| `isduota_tableciu_2020` | `integer` | — | `4` | `open` | — | 2020 metais išduotų kalio jodido tablečių skaičius Lietuvos savivaldybėms | — |
| `isduota_rezervo_2022` | `integer` | — | `4` | `open` | — | 2022 m. Lietuvos savivaldybėms išduoti 5 proc. kalio jodido tablečių rezervo | — |
| `gave_gyv_bal` | `integer` | — | `4` | `open` | — | Gyventojų skaičius, gavusių kalio jodido preparatus iki balandžio 1 d. | — |
| `gave_gyv_proc_bal` | `number` | `%` | `4` | `open` | — | Gyventojų skaičius, gavusių kalio jodido preparatus balandį, procentais | — |
| `likutis_bal` | `integer` | — | `4` | `open` | — | Kalio jodido preparatų likutis balandį skaičius | — |
| `pastabos_bal` | `string` | — | `4` | `open` | — | Pastabos | — |
| `suaugusiuju_sk_sp` | `integer` | — | `4` | `open` | — | Suaugusiųjų gyventojų skaičius savivaldybėje spalį | — |
| `vaiku_sk_sp` | `integer` | — | `4` | `open` | — | Vaikų iki 12 m. skaičius savivaldybėje spalį | — |
| `gave_gyv_sp` | `integer` | — | `4` | `open` | — | Gyventojų skaičius, gavusių kalio jodido preparatus iki spalio 1 d. | — |
| `gave_gyv_proc_sp` | `number` | `%` | `4` | `open` | — | Gyventojų skaičius, gavusių kalio jodido preparatus spalį, procentais | — |
| `likutis_sp` | `integer` | — | `4` | `open` | — | Kalio jodido preparatų likučio spalį skaičius | — |
| `pastabos_sp` | `string` | — | `4` | `open` | — | Spalio mėnesio pastabos | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/essc/aprupinimas_jodo_preparatais.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/essc/aprupinimas_jodo_preparatais.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/essc/aprupinimas_jodo_preparatais (https://data.gov.lt/datasets/2371/)
