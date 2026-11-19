---
type: Table
title: "Sutartis — VšĮ Centrinės projektų valdymo agentūros Vidaus saugumo fondo ir Integruoto sienų valdymo fondo informacinių sistemų sutarčių duomenys."
description: "Duomenų rinkį sudaro VšĮ Centrinės projektų valdymo agentūros administruojamų projektų sutarčių duomenys, susiję su Vidaus saugumo fondu ir Integruoto sienų valdymo fondu."
resource: "https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys_sf/Sutartis"
tags: [gov, cpva, sutartis, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys_vorai.csv#L14"
    title: "atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys_vorai.csv#L14"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4062/"
    title: "data.gov.lt DCAT-AP — datasets/gov/cpva/paramu_duomenys_sf"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Sutartis — VšĮ Centrinės projektų valdymo agentūros Vidaus saugumo fondo ir Integruoto sienų valdymo fondo informacinių sistemų sutarčių...

Duomenų rinkį sudaro VšĮ Centrinės projektų valdymo agentūros administruojamų projektų sutarčių duomenys, susiję su Vidaus saugumo fondu ir Integruoto sienų valdymo fondu. Rinkinyje pateikiama informacija apie projektą įgyvendinančią instituciją, nurodomas jos identifikatorius (JAR), sutarties numeris ir pavadinimas. Lentelėje fiksuojamos svarbiausios projekto datos – paraiškos pateikimo, veiklų pradžios ir pabaigos, sutarties įsigaliojimo bei projekto pabaigos datos. Taip pat pateikiami finansiniai rodikliai: finansavimo procentas, prašoma suma, finansuojama suma ir faktiškai išmokėta suma bei paskutinio mokėjimo data. Duomenys leidžia įvertinti projektų finansavimo apimtį ir mokėjimų eigą. Lentelėje nurodomas partnerių skaičius, leidžiantis analizuoti projektų bendradarbiavimo mastą. Be to, pateikiamas nustatytų pažeidimų skaičius, kuris svarbus priežiūros ir rizikų vertinimui. Papildomi laukai – regionas ir priemonės pavadinimas – sudaro galimybę analizuoti projektų pasiskirstymą teritoriniu ir programiniu pjūviu. Duomenų teikėjas – VšĮ Centrinė projektų valdymo agentūra. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^manifest]

- **Model:** `datasets/gov/cpva/paramu_duomenys_sf/Sutartis`[^manifest]
- **Dataset:** [VšĮ Centrinės projektų valdymo agentūros Vidaus saugumo fondo ir Integruoto sienų valdymo fondo...](../paramu_duomenys_sf.md) (`datasets/gov/cpva/paramu_duomenys_sf`)[^manifest]
- **Manifest CSV:** [datasets/gov/cpva/paramu_duomenys_vorai.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys_vorai.csv#L14)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys_sf/Sutartis` (`deployed`)[^manifest]
- **Provider:** `cpva` — VšĮ Centrinė projektų valdymo agentūra *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `sutarties_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys_vorai.csv#L14 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys_vorai.csv#L14)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/cpva/paramu_duomenys_sf (https://data.gov.lt/datasets/4062/)
