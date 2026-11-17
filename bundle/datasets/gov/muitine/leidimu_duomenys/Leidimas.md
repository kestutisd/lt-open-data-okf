---
type: Table
title: "Leidimas — Leidimai"
description: "Duomenys apie suteiktą teisę atlikti tam tikrą veiklą ar naudotis lengvata."
resource: "https://get.data.gov.lt/datasets/gov/muitine/leidimu_duomenys/Leidimas"
tags: [gov, muitine, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/leidimu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/leidimu_duomenys.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Leidimas — Leidimai

Duomenys apie suteiktą teisę atlikti tam tikrą veiklą ar naudotis lengvata. Čia matoma, kam išduota, koks tipas, kokia būsena ir nuo kada iki kada galioja.

- **Model:** `datasets/gov/muitine/leidimu_duomenys/Leidimas`[^manifest]
- **Dataset:** [Muitinės leidimų sistemos leidimų ir prašymų duomenys](../leidimu_duomenys.md) (`datasets/gov/muitine/leidimu_duomenys`)
- **Manifest CSV:** [datasets/gov/muitine/leidimu_duomenys.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/leidimu_duomenys.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/leidimu_duomenys/Leidimas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `leid_aun` | `string` | — | `4` | `open` | — | Leidimo registracijos numeris (AUN) | — |
| `leid_asm_ident_nr` | `string` | — | `4` | `open` | — | Leidimo turėtojo kodas | — |
| `leid_asm_tipas` | `string` | — | `4` | `open` | — | Leidimo turėtojo kodo rūšis | — |
| `leid_isdav_ist_kod` | `string` | — | `4` | `open` | — | Leidimą išdavusios muitinės įstaigos kodas | — |
| `leid_tipo_kod` | `string` | — | `4` | `open` | — | Leidimo rūšies kodas | — |
| `leid_pavadinimas` | `string` | — | `4` | `open` | — | Leidimo rūšies pavadinimas | — |
| `leid_versijos_nr` | `integer` | — | `4` | `open` | — | Leidimo versijos numeris | — |
| `leid_busenos_kod` | `string` | — | `4` | `open` | — | Leidimo būsenos kodas | — |
| `leid_busena` | `string` | — | `4` | `open` | — | Leidimo būsena | — |
| `leid_isdavimo_data` | `date` | `D` | `4` | `open` | — | Leidimo išdavimo data | — |
| `leid_galiojimo_data_nuo` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo data nuo | — |
| `leid_galiojimo_data_iki` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo data iki | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/leidimu_duomenys.csv
