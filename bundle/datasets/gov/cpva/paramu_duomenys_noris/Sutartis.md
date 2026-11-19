---
type: Table
title: "Sutartis — Pateiktos paraiškos bei pasirašytos finansuoti sutartys"
description: "Ši lentelė aprašo projektus, įgyvendinamus pagal 2014–2021 m. Europos ekonominės erdvės ir Norvegijos finansinius mechanizmus, kuriuos administruoja Centrinė projektų valdymo agentūra."
resource: "https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys_noris/Sutartis"
tags: [gov, cpva, sutartis, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys_noris.csv#L26"
    title: "atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys_noris.csv#L26"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3904/"
    title: "data.gov.lt DCAT-AP — datasets/gov/cpva/paramu_duomenys_noris"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Sutartis — Pateiktos paraiškos bei pasirašytos finansuoti sutartys

Ši lentelė aprašo projektus, įgyvendinamus pagal 2014–2021 m. Europos ekonominės erdvės ir Norvegijos finansinius mechanizmus, kuriuos administruoja Centrinė projektų valdymo agentūra. Joje pateikiama informacija apie kiekvieną projektą – pareiškėją, projekto kodą, pavadinimą, prašomą ir patvirtintą finansavimą, sutarties datas, projekto veiklų laikotarpį, būseną bei atsakingas institucijas. Duomenys leidžia analizuoti projektų finansavimą, įgyvendinimo eigą ir geografinį pasiskirstymą savivaldybių bei institucijų lygmeniu.[^manifest]

- **Model:** `datasets/gov/cpva/paramu_duomenys_noris/Sutartis`[^manifest]
- **Dataset:** [VšĮ Centrinės projektų valdymo agentūros 2014–2021 m. Europos ekonominės erdvės ir Norvegijos...](../paramu_duomenys_noris.md) (`datasets/gov/cpva/paramu_duomenys_noris`)[^manifest]
- **Manifest CSV:** [datasets/gov/cpva/paramu_duomenys_noris.csv#L26](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys_noris.csv#L26)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys_noris/Sutartis` (`deployed`)[^manifest]
- **Provider:** `cpva` — VšĮ Centrinė projektų valdymo agentūra *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `project_id` | `string` | — | `4` | `open` | — | Sutarties identifikatorius | — |
| `pareiskejo_ja_kodas` | `string` | — | `4` | `open` | — | Pareiškėjo JAR kodas | — |
| `istaigos_reg_savivaldybe` | `string` | — | `4` | `open` | — | Pareikškėjo registracijos savivaldybė | — |
| `pateikimo_data` | `datetime` | `L` | `4` | `open` | — | Pateikimo data | — |
| `projekto_pavadinimas_lt` | `string` | — | `2` | `open` | — | Projekto pavadinimas | — |
| `projekto_kodas` | `string` | — | `4` | `open` | — | Projekto kodas | — |
| `paraiskos_prasoma_suma` | `number` | — | `4` | `open` | — | Paraiškos prašomo finansavimo suma | — |
| `sutarties_prasoma_suma` | `number` | — | `4` | `open` | — | Sutarties prašomo finansavimo suma EEE (Europos ekonominė erdvė) | — |
| `vertinime_tvirtinamas_biudzetas` | `number` | — | `4` | `open` | — | Vertinime tvirtinamas biudžetas | — |
| `sutarties_isigaliojimo_data` | `date` | `D` | `4` | `open` | — | Sutarties įsigaliojimo data | — |
| `projekto_veiklu_pradzia` | `date` | `D` | `4` | `open` | — | Projekto veiklų įgyvendinimo pradžia | — |
| `projekto_veiklu_pabaiga` | `date` | `D` | `4` | `open` | — | Projekto veiklų įgyvendinimo pabaiga | — |
| `turi_partneriu` | `boolean` | — | `4` | `open` | — | Projekto įgyvendinimas su partneriu (0-ne, 1-taip) | — |
| `sutarties_busena` | `string` | — | `4` | `open` | — | Projekto būsena | — |
| `busenos_data` | `date` | `D` | `4` | `open` | — | Būsenos data | — |
| `priemones_kvietimo_kodas` | `string` | — | `4` | `open` | — | Priemonės kvietimo kodas | — |
| `priemones_kvietimo_pavadinimas` | `string` | — | `4` | `open` | — | Priemonės kvietimo pavadinmas | — |
| `atsakinga_institucija` | `string` | — | `4` | `open` | — | Atsakingos institucijos pavadinimas | — |
| `atsakingos_institucijos_santrumpa` | `string` | — | `4` | `open` | — | Atsakingos institucijos santrumpa | — |
| `atsakingos_institucijos_jar` | `string` | — | `4` | `open` | — | Atsakingos institucijos JAR kodas | — |
| `apskritis` | `string` | — | `4` | `open` | — | Atsakingos institucijos apskritis | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė kuriai tenka didžioji dalis paramos | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `projekto_pavadinimas_lt` | `update(property: "projekto_pavadinimas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys_noris.csv#L26 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys_noris.csv#L26)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/cpva/paramu_duomenys_noris (https://data.gov.lt/datasets/3904/)
