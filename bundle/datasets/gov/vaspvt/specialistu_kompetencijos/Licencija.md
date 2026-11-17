---
type: Table
title: "Licencija — Sveikatos priežiūros specialistų licencijos"
description: "Sveikatos priežiūros specialistų licencijų duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos sveikatos priežiūros specialistų kompetencijų platformos."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/specialistu_kompetencijos/Licencija"
tags: [gov, vaspvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/specialistu_kompetencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/specialistu_kompetencijos.csv#L24"
    last_modified: "2026-11-11T14:39:20Z"
---

# Licencija — Sveikatos priežiūros specialistų licencijos

Sveikatos priežiūros specialistų licencijų duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos sveikatos priežiūros specialistų kompetencijų platformos. Viena lentelės eilutė atitinka vieną sveikatos priežiūros specialisto licenciją, galiojančią tam tikru laikotarpiu. Eilutėje nurodomas specialisto identifikacinis numeris, licencijos pavadinimas ir šifruotas numeris, išdavimo metai, licencijos būsena, licencijos sustabdymo ir panaikinimo metai, taip pat keli techniniai stulpeliai, nurodantys, kada įrašas duomenų bezėje buvo sukurtas ir atnaujintas.

- **Model:** `datasets/gov/vaspvt/specialistu_kompetencijos/Licencija`[^manifest]
- **Dataset:** [Sveikatos priežiūros specialistų kompetencijų duomenys](../specialistu_kompetencijos.md) (`datasets/gov/vaspvt/specialistu_kompetencijos`)
- **Manifest CSV:** [datasets/gov/vaspvt/specialistu_kompetencijos.csv#L24](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/specialistu_kompetencijos.csv#L24)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/specialistu_kompetencijos/Licencija`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA unikalus raktas | Unikalios eilutės identifikatorius sudarytas iš stulpelių - specialisto_id, numeris, busena ir irasas_sukurtas |
| `specialisto_id` | `string` | — | `4` | `open` | — | Specialisto ID | Specialisto, kuriam priklauso licencija, identifikacinis numeris |
| `licencija` | `string` | — | `4` | `open` | — | Licencijos pavadinimas | — |
| `numeris` | `string` | — | `4` | `open` | — | Licencijos numeris | — |
| `isdavimo_metai` | `date` | `Y` | `4` | `open` | — | Licencijos išdavimo metai | — |
| `busena` | `string` | — | `4` | `open` | — | Licencijos galiojimo būsena | — |
| `sustabdymo_metai` | `date` | `Y` | `4` | `open` | — | Licencijos sustabdymo metai | — |
| `panaikinimo_metai` | `date` | `Y` | `4` | `open` | — | Licencijos panaikinimo metai | — |
| `irasas_sukurtas` | `datetime` | `S` | `4` | `open` | — | Įrašas sukurtas | Įrašo, duomenų bazėje, sukūrimo data ir laikas |
| `irasas_atnaujintas` | `datetime` | `S` | `4` | `open` | — | Įrašas atnaujintas | Įrašo, duomenų bazėje, atnaujinimo data ir laikas |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `busena` | `"VALID"` | — | — | Galiojanti licencija | — |
| `busena` | `"CANCELED"` | — | — | Panaikinta licencija | — |
| `busena` | `"SUSPENDED"` | — | — | Sustabdyta licencija | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/specialistu_kompetencijos.csv
