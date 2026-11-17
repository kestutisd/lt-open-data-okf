---
type: Table
title: "Sutartis — VšĮ Centrinės projektų valdymo agentūros Vidaus saugumo fondo ir Integruoto sienų valdymo fondo informacinių sistemų sutarčių duomenys."
description: "Duomenų rinkį sudaro VšĮ Centrinės projektų valdymo agentūros administruojamų projektų sutarčių duomenys, susiję su Vidaus saugumo fondu ir Integruoto sienų valdymo fondu."
resource: "https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys_sf/Sutartis"
tags: [gov, cpva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys_vorai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys_vorai.csv#L14"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sutartis — VšĮ Centrinės projektų valdymo agentūros Vidaus saugumo fondo ir Integruoto sienų valdymo fondo informacinių sistemų sutarčių duomenys.

Duomenų rinkį sudaro VšĮ Centrinės projektų valdymo agentūros administruojamų projektų sutarčių duomenys, susiję su Vidaus saugumo fondu ir Integruoto sienų valdymo fondu. Rinkinyje pateikiama informacija apie projektą įgyvendinančią instituciją, nurodomas jos identifikatorius (JAR), sutarties numeris ir pavadinimas. Lentelėje fiksuojamos svarbiausios projekto datos – paraiškos pateikimo, veiklų pradžios ir pabaigos, sutarties įsigaliojimo bei projekto pabaigos datos.

Taip pat pateikiami finansiniai rodikliai: finansavimo procentas, prašoma suma, finansuojama suma ir faktiškai išmokėta suma bei paskutinio mokėjimo data. Duomenys leidžia įvertinti projektų finansavimo apimtį ir mokėjimų eigą. Lentelėje nurodomas partnerių skaičius, leidžiantis analizuoti projektų bendradarbiavimo mastą. Be to, pateikiamas nustatytų pažeidimų skaičius, kuris svarbus priežiūros ir rizikų vertinimui. Papildomi laukai – regionas ir priemonės pavadinimas – sudaro galimybę analizuoti projektų pasiskirstymą teritoriniu ir programiniu pjūviu.

Duomenų teikėjas – VšĮ Centrinė projektų valdymo agentūra.

- **Model:** `datasets/gov/cpva/paramu_duomenys_sf/Sutartis`[^manifest]
- **Dataset:** [VšĮ Centrinės projektų valdymo agentūros Vidaus saugumo fondo ir Integruoto sienų valdymo fondo informacinių sistemų sutarčių duomenys.](../paramu_duomenys_sf.md) (`datasets/gov/cpva/paramu_duomenys_sf`)
- **Manifest CSV:** [datasets/gov/cpva/paramu_duomenys_vorai.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys_vorai.csv#L14)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys_sf/Sutartis`
- **Primary Key (`ref`):** `sutarties_nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `institucijos_jar` | `string` | — | `4` | `open` | — | Institucijos JAR kodas | — |
| `institucija` | `string` | — | `4` | `open` | — | Institucijos pavadinimas | — |
| `sutarties_nr` | `string` | — | `4` | `open` | — | Sutarties/projekto numeris | — |
| `sutarties_pavadinimas_lt` | `string` | — | `2` | `open` | — | Sutarties/projekto pavadinimas | — |
| `paraiskos_pateikimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos pateikimo data | — |
| `veiklu_pradzia` | `date` | `D` | `4` | `open` | — | Veiklų pradžios data | — |
| `veiklu_pabaiga` | `date` | `D` | `4` | `open` | — | Veiklų pabaigos data | — |
| `sutarties_isigaliojimo_data` | `date` | `D` | `4` | `open` | — | Sutarties/projekto įsigaliojimo data | — |
| `projekto_pabaiga` | `date` | `D` | `4` | `open` | — | Projekto/sutaries pabaigos data | — |
| `finansavimo_procentas` | `number` | — | `4` | `open` | — | Finansavimo procentas | — |
| `prasoma_suma` | `number` | — | `4` | `open` | — | Prašoma suma | — |
| `finansuojama_suma` | `number` | — | `4` | `open` | — | Finansuojama suma | — |
| `ismoketa_suma` | `number` | — | `4` | `open` | — | Išmokėta suma | — |
| `paskutinio_mok_data` | `date` | `D` | `4` | `open` | — | Paskutinio mokėjimo data | — |
| `partneriu_kiekis` | `integer` | — | `4` | `open` | — | Partnerių kiekis | — |
| `pazeidimu_kiekis` | `integer` | — | `4` | `open` | — | Pažeidimų kiekis | — |
| `regionas` | `string` | — | `4` | `open` | — | Regionas kuriame vykdomas projektas | — |
| `priemones_pavadinimas` | `string` | — | `4` | `open` | — | Finansavimo priemonės pavadinimas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sutarties_pavadinimas_lt` | `update(property: "sutarties_pavadinimas_lt@lt", type: "text")` | `type` | `3` | `open` | — | Sutarties/projekto pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys_vorai.csv
