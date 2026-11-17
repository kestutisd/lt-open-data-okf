---
type: Table
title: "PrograminisSertifikatas — Sveikatos priežiūros specialistų sertifikatai pagal programą"
description: "Sveikatos priežiūros specialistų įgyti sertifikatai pagal programą duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos, sveikatos priežiūros specialistų kompetencijų platformos."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/specialistu_kompetencijos/PrograminisSertifikatas"
tags: [gov, vaspvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/specialistu_kompetencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/specialistu_kompetencijos.csv#L54"
    last_modified: "2026-11-11T14:39:20Z"
---

# PrograminisSertifikatas — Sveikatos priežiūros specialistų sertifikatai pagal programą

Sveikatos priežiūros specialistų įgyti sertifikatai pagal programą duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos, sveikatos priežiūros specialistų kompetencijų platformos. Tai yra pažymėjimai/sertifikatai, išduoti pagal programas, kurios buvo užregistruotos ir patvirtintos Kompetencijų platformoje. Tuomet pagal patvirtintas programas organizatoriai kuria renginius, kuriems pasibaigus organizatorius užregistruoja renginio dalyvius, ir po šio fakto, dalyviai gauna elektroninius pažymėjimus, kurie yra paremti programos duomenimis. Viena lentelės eilutė atitinka vieną įgytą sveikatos priežiūros specialisto sertifikatą. Eilutėje nurodomas sveikatos priežiūros specialisto identifikacinis numeris, sertifikato įgijimo data, sertifikato/renginio pavadinimas, aprašymas ir tikslas, sertifikato forma ir žinių vertinimo tipas, mokymų tipas, mokymų organizatoriaus pavadinimas, JAR kodas, JAR kodo validavimo įvertis, adresas ir geolokacija, mokymų pradžios ir pabaigos datos, trukmė akademinėmis valandomis, sertifikato aktyvumo statusas. Paskutiniai du stulpeliai nurodo, kada įrašas buvo sukurtas ir atnaujintas duomenų bazėje.

- **Model:** `datasets/gov/vaspvt/specialistu_kompetencijos/PrograminisSertifikatas`[^manifest]
- **Dataset:** [Sveikatos priežiūros specialistų kompetencijų duomenys](../specialistu_kompetencijos.md) (`datasets/gov/vaspvt/specialistu_kompetencijos`)
- **Manifest CSV:** [datasets/gov/vaspvt/specialistu_kompetencijos.csv#L54](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/specialistu_kompetencijos.csv#L54)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/specialistu_kompetencijos/PrograminisSertifikatas`
- **Primary Key (`ref`):** `sertifikato_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sertifikato_id` | `string` | — | `4` | `open` | — | Sertifikato ID | Unikalios eilutės identifikatorius, nurodantis unikalų sveikatos priežiūros specialisto įgytą sertifikatą |
| `specialisto_id` | `string` | — | `4` | `open` | — | Specialisto ID | Specialisto, kuriam priklauso sertifikatas, identifikacinis numeris |
| `sertifikavimo_data` | `date` | `D` | `4` | `open` | — | Sertifikato įgijimo data | Data, kada specialistas sertifikatą įgijo |
| `pavadinimas` | `string` | — | `4` | `open` | — | Sertifikato/Renginio pavadinimas | — |
| `aprasymas` | `string` | — | `4` | `open` | — | Sertifikato/Renginio aprašymas | — |
| `tikslas` | `string` | — | `4` | `open` | — | Sertifikato/Renginio tikslas | — |
| `forma` | `string` | — | `4` | `open` | — | Sertifikato programos forma | — |
| `vertinimas` | `string` | — | `4` | `open` | — | Sertifikato įgijimo vertinimo tipas | — |
| `mokymu_tipas` | `string` | — | `4` | `open` | — | Mokymų tipas | — |
| `organizatorius` | `string` | — | `4` | `open` | — | Organizatorius | Organizacijos, rengiančios mokymus, pavadinimas |
| `org_ident_kodas` | `string` | — | `4` | `open` | — | Organizatoriaus kodas | Organizacijos, rengiančios mokymus, JAR kodas |
| `jar_validacija` | `string` | — | `4` | `open` | — | JAR kodo validacija | Valstybės duomenų agentūros sugeneruotas stulpelis validuojantis institucijos JAR kodus |
| `adresas` | `string` | — | `4` | `open` | — | Organizacijos adresas | Organizacijos, rengiančios mokymus, adresas |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | Organizacijos geolokacija | Organizacijos, rengiančios mokymus, geolokacija. WGS-84 koordinatės taškas |
| `pradzios_data` | `date` | `D` | `4` | `open` | — | Mokymų pradžios data | — |
| `pabaigos_data` | `date` | `D` | `4` | `open` | — | Mokymų pabaigos data | — |
| `trukme` | `number` | — | `4` | `open` | — | Mokymų trukmė akademinėmis valandomis | — |
| `sert_statusas` | `string` | — | `4` | `open` | — | Sertifikato statusas | — |
| `irasas_sukurtas` | `datetime` | `S` | `4` | `open` | — | Įrašas sukurtas | Įrašo, duomenų bazėje, sukūrimo data ir laikas |
| `irasas_atnaujintas` | `datetime` | `S` | `4` | `open` | — | Įrašas atnaujintas | Įrašo, duomenų bazėje, atnaujinimo data ir laikas |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `sert_statusas` | `"ACTIVE"` | — | — | Patvirtintas sertifikatas | — |
| `sert_statusas` | `"CANCELED"` | — | — | Atšauktas sertifikatas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/specialistu_kompetencijos.csv
