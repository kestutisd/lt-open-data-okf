---
type: Table
title: "DarbovieciuImunizacija — Asmenų imunizacija pagal darbovietes"
description: "Kasdien atnaujinami darbuotojų imunizacijos nuo SARS-CoV-2 duomenys dvidešimtyje tūkstančių Lietuvos įmonių, įstaigų, organizacijų (ekonominės veiklos rūšių klasifikatorių (redakcija 2)"
resource: "https://get.data.gov.lt/datasets/gov/lsd/covid19/DarbovieciuImunizacija"
tags: [gov, lsd, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/covid19.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L34"
    last_modified: "2026-11-11T14:39:20Z"
---

# DarbovieciuImunizacija — Asmenų imunizacija pagal darbovietes

Kasdien atnaujinami darbuotojų imunizacijos nuo SARS-CoV-2 duomenys dvidešimtyje tūkstančių Lietuvos įmonių, įstaigų, organizacijų (ekonominės veiklos rūšių klasifikatorių (redakcija 2)

- **Model:** `datasets/gov/lsd/covid19/DarbovieciuImunizacija`[^manifest]
- **Dataset:** [datasets/gov/lsd/covid19](../covid19.md) (`datasets/gov/lsd/covid19`)
- **Manifest CSV:** [datasets/gov/lsd/covid19.csv#L34](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L34)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/covid19/DarbovieciuImunizacija`
- **Level:** `3`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `workplace_code` | `string` | — | `2` | `open` | — | Darbovietės juridinio asmens registracijos kodas (iš Registrų centro) | — |
| `workplace_name` | `string` | — | `2` | `open` | — | Darbovietės pavadinimas | — |
| `activity_evrk2` | `ref` | [/datasets/gov/lsd/cl/evrk/EkonominesVeiklosRusis](../cl/evrk/EkonominesVeiklosRusis.md) | `4` | `open` | — | Darbovietės veikla pagal ekonominės veiklos rūšių klasifikatorių (redakcija 2) | — |
| `municipality` | `string` | — | `2` | `open` | — | Savivaldybė, kurioje registruota darbovietė (neatsižvelgiama į filialus, padalinius) | — |
| `county` | `string` | — | `2` | `open` | — | Apskritis, kuriai priklauso ta savivaldybė | — |
| `employees` | `integer` | `U` | `4` | `open` | — | Suapvalintas darbuotojų skaičius (tik turintys LT asmens kodus) | — |
| `immunised_percent` | `string` | — | `3` | `open` | — | Imunizuotų (skiepais arba natūraliai) darbuotojų procentas (tik turintys LT asmens kodus) | — |
| `percentile_1` | `integer` | — | `3` | `open` | — | Procentilis, į kurį patenka darbovietė pagal imunizuotų darbuotojų procentą (parodo, koks procentas visų darboviečių yra „žemiau“ už šią darbovietę) | — |
| `percentile_2` | `integer` | — | `3` | `open` | — | Tas pats procentilis, tačiau prieš skaičiavimą pašalinus visas su žmonių sveikatos priežiūros veikla susijusias darbovietes | — |
| `as_of_date` | `string` | — | `2` | `open` | — | Paskutinė para, kurios duomenys yra įtraukti | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/covid19.csv
