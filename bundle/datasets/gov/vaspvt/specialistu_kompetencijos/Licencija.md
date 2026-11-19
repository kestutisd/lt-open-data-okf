---
type: Table
title: "Licencija — Sveikatos priežiūros specialistų licencijos"
description: "\"Sveikatos priežiūros specialistų licencijų duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos sveikatos priežiūros specialistų kompetencijų platformos."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/specialistu_kompetencijos/Licencija"
tags: [gov, vaspvt, licencija, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/specialistu_kompetencijos.csv#L24"
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/specialistu_kompetencijos.csv#L24"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3887/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vaspvt/specialistu_kompetencijos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Licencija — Sveikatos priežiūros specialistų licencijos

"Sveikatos priežiūros specialistų licencijų duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos sveikatos priežiūros specialistų kompetencijų platformos. Viena lentelės eilutė atitinka vieną sveikatos priežiūros specialisto licenciją, galiojančią tam tikru laikotarpiu. Eilutėje nurodomas specialisto identifikacinis numeris, licencijos pavadinimas ir šifruotas numeris, išdavimo metai, licencijos būsena, licencijos sustabdymo ir panaikinimo metai, taip pat keli techniniai stulpeliai, nurodantys, kada įrašas duomenų bezėje buvo sukurtas ir atnaujintas."[^manifest]

- **Model:** `datasets/gov/vaspvt/specialistu_kompetencijos/Licencija`[^manifest]
- **Dataset:** [Sveikatos priežiūros specialistų kompetencijų duomenys](../specialistu_kompetencijos.md) (`datasets/gov/vaspvt/specialistu_kompetencijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vaspvt/specialistu_kompetencijos.csv#L24](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/specialistu_kompetencijos.csv#L24)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/specialistu_kompetencijos/Licencija` (`deployed`)[^manifest]
- **Provider:** `vaspvt` — Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA unikalus raktas | "Unikalios eilutės identifikatorius sudarytas iš stulpelių - specialisto_id, numeris, busena ir irasas_sukurtas" |
| `specialisto_id` | `string` | — | `4` | `open` | — | Specialisto ID | "Specialisto, kuriam priklauso licencija, identifikacinis numeris" |
| `licencija` | `string` | — | `4` | `open` | — | Licencijos pavadinimas | — |
| `numeris` | `string` | — | `4` | `open` | — | Licencijos numeris | — |
| `isdavimo_metai` | `date` | `Y` | `4` | `open` | — | Licencijos išdavimo metai | — |
| `busena` | `string` | — | `4` | `open` | — | Licencijos galiojimo būsena | — |
| `sustabdymo_metai` | `date` | `Y` | `4` | `open` | — | Licencijos sustabdymo metai | — |
| `panaikinimo_metai` | `date` | `Y` | `4` | `open` | — | Licencijos panaikinimo metai | — |
| `irasas_sukurtas` | `datetime` | `S` | `4` | `open` | — | Įrašas sukurtas | "Įrašo, duomenų bazėje, sukūrimo data ir laikas" |
| `irasas_atnaujintas` | `datetime` | `S` | `4` | `open` | — | Įrašas atnaujintas | "Įrašo, duomenų bazėje, atnaujinimo data ir laikas" |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `busena` | `"VALID"` | — | — | Galiojanti licencija | — |
| `busena` | `"CANCELED"` | — | — | Panaikinta licencija | — |
| `busena` | `"SUSPENDED"` | — | — | Sustabdyta licencija | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/specialistu_kompetencijos.csv#L24 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/specialistu_kompetencijos.csv#L24)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vaspvt/specialistu_kompetencijos (https://data.gov.lt/datasets/3887/)
