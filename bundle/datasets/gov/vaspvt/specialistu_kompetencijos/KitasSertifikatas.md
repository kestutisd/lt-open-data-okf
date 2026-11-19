---
type: Table
title: "KitasSertifikatas — Sveikatos priežiūros specialistų papildomai įgyti sertifikatai"
description: "\"Sveikatos priežiūros specialistų papildomai įgytų sertifikatų duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos sveikatos priežiūros specialistų kompetencijų platformos."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/specialistu_kompetencijos/KitasSertifikatas"
tags: [gov, vaspvt, kitassertifikatas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/specialistu_kompetencijos.csv#L78"
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/specialistu_kompetencijos.csv#L78"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3887/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vaspvt/specialistu_kompetencijos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# KitasSertifikatas — Sveikatos priežiūros specialistų papildomai įgyti sertifikatai

"Sveikatos priežiūros specialistų papildomai įgytų sertifikatų duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos sveikatos priežiūros specialistų kompetencijų platformos. Tai yra tobulinimosi pažymėjimai, kuriuos į Kompetencijų platformą rankiniu būdu įkelia patys specialistai. Šie pažymėjimai reikalauja patvirtinimo proceso, kad būtų galima užtikrinti, jog pateikti duomenys yra teisingi ir pažymėjimas gali būti naudojamas tobulinimosi valandų gavimui. Viena lentelės eilutė atitinka vieną įgytą sveikatos priežiūros specialisto sertifikatą. Eilutėje nurodomas sveikatos priežiūros specialisto identifikacinis numeris, sertifikato įgyjimo data, sertifikato/renginio pavadinimas, forma, tipas, mokymų organizatoriaus pavadinimas, šalis, mokymų pradžios ir pabaigos data, trukmė akademinėmis valandomis ir esamas sertifikato statusas. Paskutiniai du stulpeliai nurodo įrašo sukūrimo ir atnaujinimo datą duomenų bazėje. "[^manifest]

- **Model:** `datasets/gov/vaspvt/specialistu_kompetencijos/KitasSertifikatas`[^manifest]
- **Dataset:** [Sveikatos priežiūros specialistų kompetencijų duomenys](../specialistu_kompetencijos.md) (`datasets/gov/vaspvt/specialistu_kompetencijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vaspvt/specialistu_kompetencijos.csv#L78](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/specialistu_kompetencijos.csv#L78)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/specialistu_kompetencijos/KitasSertifikatas` (`deployed`)[^manifest]
- **Provider:** `vaspvt` — Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `sertifikato_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sertifikato_id` | `string` | — | `4` | `open` | — | Sertifikato ID | "Unikalios eilutės identifikatorius, nurodantis unikalų sveikatos priežiūros specialisto įgytą sertifikatą" |
| `specialisto_id` | `string` | — | `4` | `open` | — | Specialisto ID | "Specialisto, kuriam priklauso sertifikatas, identifikacinis numeris" |
| `sertifikavimo_data` | `date` | `D` | `4` | `open` | — | Sertifikato gavimo data | "Data, kada specialistas sertifikatą įgijo" |
| `pavadinimas` | `string` | — | `4` | `open` | — | Sertifikato pavadinimas (renginio tema) | — |
| `forma` | `string` | — | `4` | `open` | — | Sertifikato/Renginio programos forma | — |
| `tipas` | `string` | — | `4` | `open` | — | Sertifikato tipas | — |
| `organizatorius` | `string` | — | `4` | `open` | — | Organizatorius | "Organizacijos, rengiančios mokymus, pavadinimas" |
| `salis` | `string` | — | `4` | `open` | — | Šalis/Valstybė | "Šalis/Valstybė, kurioje vyko mokymai" |
| `pradzios_data` | `date` | `D` | `4` | `open` | — | Mokymų pradžios data | — |
| `pabaigos_data` | `date` | `D` | `4` | `open` | — | Mokymų pabaigos data | — |
| `trukme` | `number` | — | `4` | `open` | — | Mokymų trukmė akademinėmis valandomis | — |
| `sert_statusas` | `string` | — | `4` | `open` | — | Sertifikato statusas | — |
| `irasas_sukurtas` | `datetime` | `S` | `4` | `open` | — | Įrašas sukurtas | "Įrašo, duomenų bazėje, sukūrimo data ir laikas" |
| `irasas_atnaujintas` | `datetime` | `S` | `4` | `open` | — | Įrašas atnaujintas | "Įrašo, duomenų bazėje, atnaujinimo data ir laikas" |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `sert_statusas` | `"NOT_EVALUATED"` | — | — | Neįvertintas sertifikatas | — |
| `sert_statusas` | `"ACTIVE"` | — | — | Patvirtintas sertifikatas | — |
| `sert_statusas` | `"REJECTED"` | — | — | Atmestas sertifikatas | — |
| `sert_statusas` | `"NOT_RELEVANT_FOR_LICENSING"` | — | — | Neaktualus sertifikatas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/specialistu_kompetencijos.csv#L78 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/specialistu_kompetencijos.csv#L78)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vaspvt/specialistu_kompetencijos (https://data.gov.lt/datasets/3887/)
