---
type: Table
title: "NotaruSarasas — Notarų sąrašas"
description: "Rinkinyje pateikiamas Lietuvos Respublikos notarų sąrašas, užtikrinantis notariato veiklos skaidrumą, teisinį reguliavimą ir priežiūrą."
resource: "https://get.data.gov.lt/datasets/gov/lrtm/notaru_sarasas/NotaruSarasas"
tags: [gov, lrtm, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lrtm/notaru_sarasas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrtm/notaru_sarasas.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# NotaruSarasas — Notarų sąrašas

Rinkinyje pateikiamas Lietuvos Respublikos notarų sąrašas, užtikrinantis notariato veiklos skaidrumą, teisinį reguliavimą ir priežiūrą. Rinkinį sudaro istoriniai ir aktualūs duomenys apie notarus, jų paskyrimus, atleidimus, veiklą ir įgaliojimų sustabdymus. Vienoje duomenų rinkinio eilutėje pateikiama informacija apie notarą konkrečiame notarų biure. Duomenų teikėjas – Lietuvos Respublikos teisingumo ministerija.

- **Model:** `datasets/gov/lrtm/notaru_sarasas/NotaruSarasas`[^manifest]
- **Dataset:** [Notarų sąrašo duomenų rinkinys](../notaru_sarasas.md) (`datasets/gov/lrtm/notaru_sarasas`)
- **Manifest CSV:** [datasets/gov/lrtm/notaru_sarasas.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrtm/notaru_sarasas.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrtm/notaru_sarasas/NotaruSarasas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Notaro unikalus identifikatorius | — |
| `vda_notaro_vardas_pavarde` | `string` | — | `4` | `open` | — | Notaro vardas ir pavardė | — |
| `notaro_vardas` | `string` | — | `4` | `open` | — | Notaro vardas | — |
| `notaro_pavarde` | `string` | — | `4` | `open` | — | Notaro pavardė | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Šifruotas asmens kodas | — |
| `asm_k_validacija` | `string` | — | `4` | `open` | — | VDA atliktas asmens kodo tikrinimas | — |
| `lytis` | `string` | — | `4` | `open` | — | Notaro lytis (V - Vyras, M - Moteris) | — |
| `vda_gimimo_desimtmetis` | `date` | `D` | `4` | `open` | — | VDA sudarytas gimimo dešimtmetis iš asmens kodo | — |
| `paskyrimo_data` | `date` | `D` | `4` | `open` | — | Notaro paskyrimo data į einamas pareigas | — |
| `atleidimo_metai` | `date` | `D` | `4` | `open` | — | Notaro atleidimo metai | — |
| `atleidimo_priezastis` | `string` | — | `4` | `open` | — | Notaro atleidimo priežastis | — |
| `notaro_biuras` | `string` | — | `4` | `open` | — | Notaro biuro pavadinimas | — |
| `notaro_savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė, kurioje veikia notaras | — |
| `notaro_apskritis` | `string` | — | `4` | `open` | — | Apskritis, kurioje veikia notaras | — |
| `igaliojimu_sustabdymo_pradzia` | `date` | `D` | `4` | `open` | — | Data, nuo kurios sustabdyti notaro įgaliojimai | — |
| `igaliojimu_sustabdymo_pabaiga` | `date` | `D` | `4` | `open` | — | Data, iki kurios buvo sustabdyti notaro įgaliojimai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrtm/notaru_sarasas.csv
