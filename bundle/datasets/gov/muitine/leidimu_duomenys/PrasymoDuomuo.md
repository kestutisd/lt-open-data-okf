---
type: Table
title: "PrasymoDuomuo — Prašymų duomenys"
description: "Papildomos prašymo detalės eilutėmis."
resource: "https://get.data.gov.lt/datasets/gov/muitine/leidimu_duomenys/PrasymoDuomuo"
tags: [gov, muitine, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/leidimu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/leidimu_duomenys.csv#L46"
    last_modified: "2026-11-11T14:39:20Z"
---

# PrasymoDuomuo — Prašymų duomenys

Papildomos prašymo detalės eilutėmis. Čia fiksuojami konkretūs prašymo priedai, pastabos ar kiti duomenys, kurie padeda įvertinti prašymą ir gali skirtis pagal situaciją.

- **Model:** `datasets/gov/muitine/leidimu_duomenys/PrasymoDuomuo`[^manifest]
- **Dataset:** [Muitinės leidimų sistemos leidimų ir prašymų duomenys](../leidimu_duomenys.md) (`datasets/gov/muitine/leidimu_duomenys`)
- **Manifest CSV:** [datasets/gov/muitine/leidimu_duomenys.csv#L46](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/leidimu_duomenys.csv#L46)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/leidimu_duomenys/PrasymoDuomuo`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `spec_arn` | `string` | — | `4` | `open` | — | Prašymo registracijos numeris (ARN) | — |
| `spec_lrn` | `string` | — | `4` | `open` | — | Pareiškėjo prašymui suteiktas unikalus numeris (LRN) | — |
| `spec_tipo_kod` | `string` | — | `4` | `open` | — | Prašymo rūšies kodas | — |
| `pras_pavadinimas` | `string` | — | `4` | `open` | — | Prašymo rūšies pavadinimas | — |
| `spec_sukurimo_data` | `date` | `D` | `4` | `open` | — | Prašymo sukūrimo data | — |
| `pras_busenos_kod` | `string` | — | `4` | `open` | — | Prašymo būsenos kodas | — |
| `pras_busena` | `string` | — | `4` | `open` | — | Prašymo būsena | — |
| `spec_elem_pav` | `string` | — | `4` | `open` | — | Specifinio duomenų elemento pavadinimas | — |
| `spec_elem_reiks` | `string` | — | `4` | `open` | — | Specifinio duomenų elemento reikšmė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/leidimu_duomenys.csv
