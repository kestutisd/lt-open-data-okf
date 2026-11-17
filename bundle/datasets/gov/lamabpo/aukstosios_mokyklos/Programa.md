---
type: Table
title: "Programa — Aukštojo mokslo programų duomenys"
description: "Pateikiami aukštojo mokslo programų duomenys Lietuvos aukštojo mokslo įstaigose."
resource: "https://get.data.gov.lt/datasets/gov/lamabpo/aukstosios_mokyklos/Programa"
tags: [gov, lamabpo, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lamabpo/aukstuju_prasymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/aukstuju_prasymai.csv#L10"
    last_modified: "2026-11-11T14:39:20Z"
---

# Programa — Aukštojo mokslo programų duomenys

Pateikiami aukštojo mokslo programų duomenys Lietuvos aukštojo mokslo įstaigose. Lentelės objektas – aukštojo mokslo įstaigos vykdoma mokymo programa pagal priėmimo metus. Nurodoma informacija apie mokymo programą: mokymo įstaiga, programos valstybinis kodas ir pavadinimas, mokymo programos vykdymo apskritis ir savivaldybė.

- **Model:** `datasets/gov/lamabpo/aukstosios_mokyklos/Programa`[^manifest]
- **Dataset:** [Priėmimo į aukštojo mokslo įstaigas prašymų duomenys](../aukstosios_mokyklos.md) (`datasets/gov/lamabpo/aukstosios_mokyklos`)
- **Manifest CSV:** [datasets/gov/lamabpo/aukstuju_prasymai.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/aukstuju_prasymai.csv#L10)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lamabpo/aukstosios_mokyklos/Programa`
- **Primary Key (`ref`):** `programos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `programos_id` | `string` | — | `4` | `open` | — | Programos identifikacinis numeris | — |
| `programos_metai` | `date` | `Y` | `4` | `open` | — | Laikotarpis, kuriam aktualūs duomenys apie mokymo programą | — |
| `programos_valst_kodas` | `string` | — | `4` | `open` | — | Mokymo programos kodas | — |
| `programos_pavadinimas` | `string` | — | `4` | `open` | — | Mokymo programos pavadinimas | — |
| `istaigos_jar` | `string` | — | `4` | `open` | — | Mokymo įstaigos JAR kodas | — |
| `jar_validacija` | `string` | — | `4` | `open` | — | Juridinio asmens kodo validacija | — |
| `mokymo_istaiga` | `string` | — | `4` | `open` | — | Mokymo įstaigos pavadinimas | — |
| `apskrities_kodas` | `string` | — | `4` | `open` | — | Studijų ar mokymo programos vykdymo apskrities kodas | — |
| `apskritis` | `string` | — | `4` | `open` | — | Klasifikuojamai vertei atitinkančios 1 hierarchijos lygmens vertės tekstinė reikšmė (lietuvių kalba) | — |
| `savivaldybes_kodas` | `string` | — | `4` | `open` | — | Studijų ar mokymo programos vykdymo savivaldybės kodas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Klasifikuojamai vertei atitinkančios 2 hierarchijos lygmens vertės tekstinė reikšmė (lietuvių kalba) | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `jar_validacija` | `"Tinkamas"` | — | — | — | — |
| `jar_validacija` | `"Tuščia reikšmė"` | — | — | — | — |
| `jar_validacija` | `"Netinkamas ilgis"` | — | — | — | — |
| `jar_validacija` | `"Yra ne skaitmenų"` | — | — | — | — |
| `jar_validacija` | `"Netinkamas kontrolinis skaitmuo"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lamabpo/aukstuju_prasymai.csv
