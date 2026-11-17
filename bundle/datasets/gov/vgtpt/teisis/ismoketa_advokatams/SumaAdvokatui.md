---
type: Table
title: "SumaAdvokatui — Teiktos valstybės garantuojamos antrinės teisinės pagalbos trukmė ir vertė"
description: "Spinta table datasets/gov/vgtpt/teisis/ismoketa_advokatams/SumaAdvokatui (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vgtpt/teisis/ismoketa_advokatams/SumaAdvokatui"
tags: [gov, vgtpt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vgtpt/teisis/ismoketa_advokatams.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/ismoketa_advokatams.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# SumaAdvokatui — Teiktos valstybės garantuojamos antrinės teisinės pagalbos trukmė ir vertė

- **Model:** `datasets/gov/vgtpt/teisis/ismoketa_advokatams/SumaAdvokatui`[^manifest]
- **Dataset:** [Teiktos valstybės garantuojamos antrinės teisinės pagalbos trukmė ir vertė](../ismoketa_advokatams.md) (`datasets/gov/vgtpt/teisis/ismoketa_advokatams`)
- **Manifest CSV:** [datasets/gov/vgtpt/teisis/ismoketa_advokatams.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/ismoketa_advokatams.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vgtpt/teisis/ismoketa_advokatams/SumaAdvokatui`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `sprendimo_metai` | `integer` | — | `2` | `open` | — | Sprendimo išmokėti užmokestį metai | — |
| `sprendimo_ketvirtis` | `integer` | — | `2` | `open` | — | Sprendimo išmokėti užmokestį ketvirtis | — |
| `teritorijos_kodas` | `ref` | [/datasets/gov/vgtpt/teisis/klasifikatoriai/Teritorija](../klasifikatoriai/Teritorija.md) | `4` | `open` | — | Antrinę teisinę pagalbą gaunančio asmens gyvenamosios vietos teritorijos kodas | Iš TEISIS teritorijos klasifikatoriaus |
| `bylos_rusies_kodas` | `ref` | [/datasets/gov/vgtpt/teisis/klasifikatoriai/BylosRusis](../klasifikatoriai/BylosRusis.md) | `4` | `open` | — | Bylos, kurioje reikalinga antrinė teisinė pagalba, rūšies kodas | Iš TEISIS bylų rūšių klasifikatoriaus |
| `moketina_suma` | `number` | — | `2` | `open` | — | Sprendime nurodytas antrinės teisinės pagalbos teikėjui mokėtinas užmokestis | — |
| `trukme` | `integer` | `min` | `4` | `open` | — | Antrinės teisinės pagalbos teikėjo sugaišto laiko trukmė | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sprendimo_metai` | `update(type: "date", ref: "Q")` | `type` | `4` | — | — | — | — |
| `moketina_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vgtpt/teisis/ismoketa_advokatams.csv
