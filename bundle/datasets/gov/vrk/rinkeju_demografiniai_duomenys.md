---
type: Dataset
title: "Rinkėjų demografiniai duomenys"
description: "Vyriausiosios rinkimų komisijos Rinkėjų sąrašų tvarkymo posistemėje kaupiami rinkėjų balsavimo žymėjimai."
resource: "https://get.data.gov.lt/datasets/gov/vrk/rinkeju_demografiniai_duomenys"
tags: [gov, vrk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Rinkėjų demografiniai duomenys

Vyriausiosios rinkimų komisijos Rinkėjų sąrašų tvarkymo posistemėje kaupiami rinkėjų balsavimo žymėjimai. Duomenys kaupiami nuo 2011-12-29 ir yra atnaujinami iki šiol. Duomenų rinkinys sudarytas iš 4 atskirų lentelių apie rinkėjus, rinkėjų žymėjimus, rinkimų apygardas ir vykdomus rinkimus. Lentelėse yra įtraukti išorinių raktų stulpeliai, leidžiantys apjungti jose esančius duomenis.

- **Namespace:** `datasets/gov/vrk/rinkeju_demografiniai_duomenys`[^manifest]
- **Manifest CSV:** [datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vrk/rinkeju_demografiniai_duomenys`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Rinkejas](rinkeju_demografiniai_duomenys/Rinkejas.md) | Rinkėjai | `4` | `rinkejo_asm_k` | — | 3 | Balso teisę turinčių rinkėjų lentelė. |
| [Zymejimas](rinkeju_demografiniai_duomenys/Zymejimas.md) | Rinkėjų žymėjimai | `4` | `vda_prime_key` | — | 4 | Rinkėjų balsų žymėjimų lentelė. |
| [Apygarda](rinkeju_demografiniai_duomenys/Apygarda.md) | Rinkimų apygardos | `4` | `apygardos_id` | — | 2 | Rinkimų apygardų lentelė. |
| [RinkimuTuras](rinkeju_demografiniai_duomenys/RinkimuTuras.md) | Rinkimų turai | `4` | `vda_prime_key` | — | 7 | Vykdomų rinkimų lentelė. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv
