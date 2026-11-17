---
type: Table
title: "Eksportas — Eksporto sertifikatų ir prekių duomenų rinkinys"
description: "Duomenų rinkinyje registruojami prašymai išduoti veterinarinius sertifikatus maisto, gyvūnų ir pašarų eksportui bei pateikiama informacija apie sertifikatus, eksportuojamus produktus, jų kiekius, gavėjus, paskirties šalis ir veiklos..."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/eksportas/Eksportas"
tags: [gov, vmvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmvt/eksportas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/eksportas.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Eksportas — Eksporto sertifikatų ir prekių duomenų rinkinys

Duomenų rinkinyje registruojami prašymai išduoti veterinarinius sertifikatus maisto, gyvūnų ir pašarų eksportui bei pateikiama informacija apie sertifikatus, eksportuojamus produktus, jų kiekius, gavėjus, paskirties šalis ir veiklos vykdytojus.

- **Model:** `datasets/gov/vmvt/eksportas/Eksportas`[^manifest]
- **Dataset:** [Eksporto sertifikatų ir prekių duomenų rinkinys](../eksportas.md) (`datasets/gov/vmvt/eksportas`)
- **Manifest CSV:** [datasets/gov/vmvt/eksportas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/eksportas.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/eksportas/Eksportas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | — | Unikalus identifikatorius |
| `sertifikato_numeris` | `string` | — | `4` | `open` | — | — | Serifikato numeris |
| `sertifikato_isdavimo_data` | `date` | `D` | `4` | `open` | — | — | Sertifikato išdavimo data |
| `isdavusi_institucija` | `string` | — | `4` | `open` | — | — | Sertifikatą išdavusi institucija |
| `sert_veiklos_vygdytojas` | `string` | — | `4` | `open` | — | — | Veiklos vygdytojas |
| `sert_veiklos_vygdytojo_tipas` | `string` | — | `4` | `open` | — | — | Vygdytojo tipas |
| `sert_veiklos_vygdytojo_jar` | `string` | — | `4` | `open` | — | — | Vygdytojo JAR kodas |
| `sert_veiklos_vygdytojo_adresas` | `string` | — | `4` | `open` | — | — | Veiklos vygdytojo adresas |
| `gavejas` | `string` | — | `4` | `open` | — | — | Gavėjas |
| `gavejo_salis` | `string` | — | `4` | `open` | — | — | Produkto gavėjo (importuotojo) šalies pavadinimas arba ISO kodas |
| `kn_skyriaus_kodas` | `string` | — | `4` | `open` | — | — | KN skyriaus kodas |
| `kn_skyriaus_pavadinimas` | `string` | — | `4` | `open` | — | — | KN skyriaus pavadinimas |
| `kn_pozicijos_kodas` | `string` | — | `4` | `open` | — | — | KN pozicijos kodas |
| `kn_pozicijos_pavadinimas` | `string` | — | `4` | `open` | — | — | KN pozicijos pavadinimas |
| `kn_subpozicijos_kodas` | `string` | — | `4` | `open` | — | — | KN subpozicijos kodas |
| `kn_subpozicijos_pavadinimas` | `string` | — | `4` | `open` | — | — | KN subpozicijos pavadinimas |
| `kn_kodas` | `string` | — | `4` | `open` | — | — | KN kodas |
| `kn_prekes_aprasymas` | `string` | — | `4` | `open` | — | — | Produkto aprašymas pagal KN |
| `prod_vnt` | `string` | — | `4` | `open` | — | — | Produkto matavimo vienetai |
| `prod_kiekis` | `number` | — | `4` | `open` | — | — | Produkto kiekis |
| `prod_pakuotes` | `string` | — | `4` | `open` | — | — | Produkto pakuočių skaičius |
| `sert_sukurimo_data` | `datetime` | `L` | `4` | `open` | — | — | Įrašo sukūrimo data |
| `sert_modifikavimo_data` | `datetime` | `L` | `4` | `open` | — | — | Įrašo modifikavimo data |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/eksportas.csv
