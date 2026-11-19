---
type: Table
title: "DarbovieciuImunizacija — Asmenų imunizacija pagal darbovietes"
description: "Kasdien atnaujinami darbuotojų imunizacijos nuo SARS-CoV-2 duomenys dvidešimtyje tūkstančių Lietuvos įmonių, įstaigų, organizacijų (ekonominės veiklos rūšių klasifikatorių (redakcija 2)"
resource: "https://get.data.gov.lt/datasets/gov/lsd/covid19/DarbovieciuImunizacija"
tags: [gov, lsd, darbovieciuimunizacija, deployed, level-3, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L34"
    title: "atviriduomenys/manifest — datasets/gov/lsd/covid19.csv#L34"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1670/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/covid19"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# DarbovieciuImunizacija — Asmenų imunizacija pagal darbovietes

Kasdien atnaujinami darbuotojų imunizacijos nuo SARS-CoV-2 duomenys dvidešimtyje tūkstančių Lietuvos įmonių, įstaigų, organizacijų (ekonominės veiklos rūšių klasifikatorių (redakcija 2)[^manifest]

- **Model:** `datasets/gov/lsd/covid19/DarbovieciuImunizacija`[^manifest]
- **Dataset:** [COVID-19 pandemijos duomenys](../covid19.md) (`datasets/gov/lsd/covid19`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/covid19.csv#L34](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L34)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/covid19/DarbovieciuImunizacija` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `workplace_code` | `string` | — | `2` | `open` | — | Darbovietės juridinio asmens registracijos kodas (iš Registrų centro) | — |
| `workplace_name` | `string` | — | `2` | `open` | — | Darbovietės pavadinimas | — |
| `activity_evrk2` | `ref` | [EkonominesVeiklosRusis](../cl/evrk/EkonominesVeiklosRusis.md) (`level=4 UUID`: `activity_evrk2._id`) | `4` | `open` | — | Darbovietės veikla pagal ekonominės veiklos rūšių klasifikatorių (redakcija 2) | — |
| `municipality` | `string` | — | `2` | `open` | — | Savivaldybė, kurioje registruota darbovietė (neatsižvelgiama į filialus, padalinius) | — |
| `county` | `string` | — | `2` | `open` | — | Apskritis, kuriai priklauso ta savivaldybė | — |
| `employees` | `integer` | `U` | `4` | `open` | — | Suapvalintas darbuotojų skaičius (tik turintys LT asmens kodus) | — |
| `immunised_percent` | `string` | — | `3` | `open` | — | Imunizuotų (skiepais arba natūraliai) darbuotojų procentas (tik turintys LT asmens kodus) | — |
| `percentile_1` | `integer` | — | `3` | `open` | — | Procentilis, į kurį patenka darbovietė pagal imunizuotų darbuotojų procentą (parodo, koks procentas visų darboviečių yra „žemiau“ už šią darbovietę) | — |
| `percentile_2` | `integer` | — | `3` | `open` | — | Tas pats procentilis, tačiau prieš skaičiavimą pašalinus visas su žmonių sveikatos priežiūros veikla susijusias darbovietes | — |
| `as_of_date` | `string` | — | `2` | `open` | — | Paskutinė para, kurios duomenys yra įtraukti | — |

# Related References

- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/covid19.csv#L34 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L34)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/covid19 (https://data.gov.lt/datasets/1670/)
