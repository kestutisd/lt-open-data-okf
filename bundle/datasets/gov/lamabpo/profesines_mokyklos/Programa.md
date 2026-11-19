---
type: Table
title: "Programa — Profesinio mokymo programų duomenys"
description: "Pateikiami profesinio mokymo programų duomenys Lietuvos profesinio mokymo įstaigose."
resource: "https://get.data.gov.lt/datasets/gov/lamabpo/profesines_mokyklos/Programa"
tags: [gov, lamabpo, programa, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/profesiniu_prasymai.csv#L11"
    title: "atviriduomenys/manifest — datasets/gov/lamabpo/profesiniu_prasymai.csv#L11"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2913/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lamabpo/profesines_mokyklos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Programa — Profesinio mokymo programų duomenys

Pateikiami profesinio mokymo programų duomenys Lietuvos profesinio mokymo įstaigose. Lentelės objektas – profesinio mokymo įstaigos vykdomos mokymo programos modulis vieno priėmimo etapo metu per vienerių metų laikotarpį. Nurodomi priėmimo etapo duomenys (metai ir etapas) ir duomenys apie mokymo programą (mokymo įstaiga, filialas, programos pavadinimas, modulis, mokymo programos vykdymo apskritis,savivaldybė ir suteikiama kvalifikacija, baigus mokymo programą).[^manifest]

- **Model:** `datasets/gov/lamabpo/profesines_mokyklos/Programa`[^manifest]
- **Dataset:** [Priėmimo į profesinio mokymo įstaigas prašymų duomenys](../profesines_mokyklos.md) (`datasets/gov/lamabpo/profesines_mokyklos`)[^manifest]
- **Manifest CSV:** [datasets/gov/lamabpo/profesiniu_prasymai.csv#L11](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/profesiniu_prasymai.csv#L11)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lamabpo/profesines_mokyklos/Programa` (`deployed`)[^manifest]
- **Provider:** `lamabpo` — Lietuvos aukštųjų mokyklų asociacija bendrajam priėmimui organizuoti (LAMA BPO) *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `programos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `programos_id` | `string` | — | `4` | `open` | — | Programos identifikacinis numeris | — |
| `programos_metai` | `date` | `Y` | `4` | `open` | — | Laikotarpis, kuriam aktualūs duomenys apie mokymo programą | — |
| `etapas` | `string` | — | `4` | `open` | — | Prašymo teikimo etapas | — |
| `programos_valst_kodas` | `string` | — | `4` | `open` | — | Mokymo programos kodas | — |
| `programos_pavadinimas` | `string` | — | `4` | `open` | — | Mokymo programos pavadinimas | — |
| `modulio_kodas` | `string` | — | `4` | `open` | — | Modulio kodas | — |
| `modulio_pavadinimas` | `string` | — | `4` | `open` | — | Modulio pavadinimas | — |
| `svietimo_sritis` | `string` | — | `4` | `open` | — | Mokymo programos švietimo sritis | — |
| `suteikiama` | `string` | — | `4` | `open` | — | Suteikiamas kvalifikacinis laipsnis | — |
| `kvalifikacijos_lygis` | `string` | — | `4` | `open` | — | Suteikiamas kvalifikacijos lygis | — |
| `kvalifikacijos_pavadinimas` | `string` | — | `4` | `open` | — | Kvalifikacijos pavadinimas | — |
| `istaigos_jar` | `string` | — | `4` | `open` | — | Mokymo įstaigos JAR kodas | — |
| `jar_validacija` | `string` | — | `4` | `open` | — | Juridinio asmens kodo validacija | — |
| `mokymo_istaiga` | `string` | — | `4` | `open` | — | Prašymą gavusios mokymo įstaigos pavadinimas | — |
| `filialo_kodas` | `string` | — | `4` | `open` | — | Prašymą gavusios mokymo įstaigos filialo kodas | — |
| `filialo_pavadinimas` | `string` | — | `4` | `open` | — | Prašymą gavusios mokymo įstaigos filialo pavadinimas | — |
| `apskrities_kodas` | `string` | — | `4` | `open` | — | Apskrities, į kurios profesinę mokyklą asmuo pateikė priėmimo prašymą, kodas | — |
| `apskritis` | `string` | — | `4` | `open` | — | Klasifikuojamai vertei atitinkančios 1 hierarchijos lygmens vertės tekstinė reikšmė (lietuvių kalba) | — |
| `savivaldybes_kodas` | `string` | — | `4` | `open` | — | Savivaldybės, į kurios profesinę mokyklą asmuo pateikė priėmimo prašymą, kodas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Klasifikuojamai vertei atitinkančios 2 hierarchijos lygmens vertės tekstinė reikšmė (lietuvių kalba) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `suteikiama` | `"kvalifikacija"` | — | — | — | — |
| `suteikiama` | `"vidurinis išsilavinimas ir kvalifikacija"` | — | — | — | — |
| `suteikiama` | `"kompetencija"` | — | — | — | — |
| `suteikiama` | `"kvalifikacija ir mokymasis socialinių įgūdžių ugdymo programoje"` | — | — | — | — |
| `kvalifikacijos_lygis` | `"II"` | — | — | — | — |
| `kvalifikacijos_lygis` | `"III"` | — | — | — | — |
| `kvalifikacijos_lygis` | `"IV"` | — | — | — | — |
| `kvalifikacijos_lygis` | `"V"` | — | — | — | — |
| `jar_validacija` | `"Tinkamas"` | — | — | — | — |
| `jar_validacija` | `"Tuščia reikšmė"` | — | — | — | — |
| `jar_validacija` | `"Netinkamas ilgis"` | — | — | — | — |
| `jar_validacija` | `"Yra ne skaitmenų"` | — | — | — | — |
| `jar_validacija` | `"Netinkamas kontrolinis skaitmuo"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lamabpo/profesiniu_prasymai.csv#L11 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/profesiniu_prasymai.csv#L11)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lamabpo/profesines_mokyklos (https://data.gov.lt/datasets/2913/)
