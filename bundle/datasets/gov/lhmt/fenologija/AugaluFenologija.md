---
type: Table
title: "AugaluFenologija — LHMT duomenys apie Lietuvoje žydinčių augalų fenologinius tarpsnius"
description: "\"Duomenų rinkinyje pateikiami Lietuvos hidrometeorologijos tarnybos (LHMT) duomenys apie Lietuvoje žydinčių augalų fenologinių tarpsnių stebėjimą."
resource: "https://get.data.gov.lt/datasets/gov/lhmt/fenologija/AugaluFenologija"
tags: [gov, lhmt, augalufenologija, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/augalu_fenologija.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lhmt/augalu_fenologija.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2851/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lhmt/fenologija"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# AugaluFenologija — LHMT duomenys apie Lietuvoje žydinčių augalų fenologinius tarpsnius

**Dataset Context:** "Duomenų rinkinyje pateikiami Lietuvos hidrometeorologijos tarnybos (LHMT) duomenys apie Lietuvoje žydinčių augalų fenologinių tarpsnių stebėjimą. Viena rinkinio eilutė atitinka tam tikro augalo vieną fenologinio tarpsnio fazę konkrečią dieną. Vienoje eilutėje esančius duomenis sudaro: augalo pavadinimas, fenologinio tarpsnio fazė, stebėjimo data, stebėjimo stoties pavadinimas ir koordinatės, duomenų gavimo į LHMT informacinę sistemą data. Fazės kodo ir fazės stadijos kodo stulpelių pora nurodo konkretų fazės pavadinimą, kuris gaunamas iš fazių klasifikatoriaus. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt."[^manifest]

- **Model:** `datasets/gov/lhmt/fenologija/AugaluFenologija`[^manifest]
- **Dataset:** [Lietuvos hidrometeorologijos tarnybos registruoti žydinčių augalų fenologiniai tarpsniai Lietuvoje](../fenologija.md) (`datasets/gov/lhmt/fenologija`)[^manifest]
- **Manifest CSV:** [datasets/gov/lhmt/augalu_fenologija.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/augalu_fenologija.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lhmt/fenologija/AugaluFenologija` (`deployed`)[^manifest]
- **Provider:** `lhmt` — Lietuvos hidrometeorologijos tarnyba (LHMT) *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_pk`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_pk` | `string` | — | `4` | `open` | — | VDA PK | Valstybės duomenų agentūros unikalus identifikacinis įrašo numeris (pirminis raktas). |
| `augalas_id` | `string` | — | `4` | `open` | — | Augalo ID | Augalo identifikacinis numeris LHMT informacinėje sistemoje. |
| `augalas` | `string` | — | `4` | `open` | — | Augalo pavadinimas | — |
| `faze_id` | `string` | — | `4` | `open` | — | Fazės ID | Kartu su fazės stadijos identifikaciniu kodu naudojami konkrečiai fazei įvardinti. |
| `fazes_stad_id` | `string` | — | `4` | `open` | — | Fazės stadijos ID | Kartu su fazės identifikaciniu kodu naudojami konkrečiai fazei įvardinti. |
| `faze` | `string` | — | `4` | `open` | — | Fenologinio tarpsnio fazė | Augalo fenologinio tarpsnio fazė. |
| `stebeta` | `date` | `1D` | `4` | `open` | — | Stebėjimo data | "Data, kada buvo augalo fenologinė tarpsnio fazė pastebėta" |
| `stotis` | `string` | — | `4` | `open` | — | Stebėjimo stotis | "Stoties, kurioje atliekamas stebėjimas, pavadinimas. AMS - automatinė meteorologijos stotis, MS - meteorologijos stotis." |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | WGS-84 koordinatės taškas | "Stoties, kurioje atliekamas stebėjimas, WGS-84 taško koordinatė." |
| `duomenys_ikelti` | `date` | `1D` | `4` | `open` | — | Duomenys įkelti | Kada duomenys buvo užregistruoti LHMT informacinėje sistemoje. |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lhmt/augalu_fenologija.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/augalu_fenologija.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lhmt/fenologija (https://data.gov.lt/datasets/2851/)
