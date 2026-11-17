---
type: Table
title: "Sutartis — Pateiktos paraiškos bei pasirašytos finansuoti sutartys"
description: "Duomenys pateikiami iš Informacinės projektų administravimo sistemos (IPAS) skirtos kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis, susijusius su VšĮ Centrinės projektų valdymo agentūros administruojamų Europos..."
resource: "https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys/Sutartis"
tags: [gov, cpva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys.csv#L51"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sutartis — Pateiktos paraiškos bei pasirašytos finansuoti sutartys

Duomenys pateikiami iš Informacinės projektų administravimo sistemos (IPAS) skirtos kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis, susijusius su VšĮ Centrinės projektų valdymo agentūros administruojamų Europos Sąjungos 2014–2020 m. struktūrinių fondų programos projektų įgyvendinimu. Lentelėje galima rasti tokią informaciją:

pateiktos paraiškos bei pasirašytos finansuoti sutartys (viena eilutė atitinka atitinkamą paraišką, pasirašytos sutarties statusų pasikeitimų eigą).

Projektai, kurie buvo vykdomi naudojantis šia sistema jau pasibaigę, bet sistemos duomenys retais atvejais vis dar atnaujinami. Tokiu atveju, duomenų atnaujinimas numatomas kas 6 mėn.

- **Model:** `datasets/gov/cpva/paramu_duomenys/Sutartis`[^manifest]
- **Dataset:** [VšĮ Centrinės projektų valdymo agentūros teikiamų paramų sutartys ir finansavimas](../paramu_duomenys.md) (`datasets/gov/cpva/paramu_duomenys`)
- **Manifest CSV:** [datasets/gov/cpva/paramu_duomenys.csv#L51](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys.csv#L51)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys/Sutartis`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | identifikacinis numeris | — |
| `istaigos_jar_kodas` | `string` | — | `4` | `open` | — | Įstaigos JAR kodas | — |
| `istaigos_reg_savivaldybe` | `string` | — | `4` | `open` | — | Įstaigos registracijos savivaldybė | — |
| `application_id` | `string` | — | `4` | `open` | — | Paraiškos identifikacinis numeris | — |
| `paraiskos_pateikimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos pateikimo data | — |
| `sutarties_id` | `string` | — | `4` | `open` | — | Sutarties identifikacinis numeris | — |
| `sutarties_pavadinimas` | `string` | — | `2` | `open` | — | Sutarties pavadinimas | — |
| `sutarties_nr` | `string` | — | `4` | `open` | — | Sutarties numeris | — |
| `sutarties_isigaliojimo_data` | `date` | `D` | `4` | `open` | — | Sutarties įsigaliojimo data | — |
| `sutarties_pabaigos_data` | `date` | `D` | `4` | `open` | — | Sutarties pabaigos data | — |
| `projekto_veiklu_pradzia` | `date` | `D` | `4` | `open` | — | Projekto veiklų pradžios data | — |
| `projekto_veiklu_pabaiga` | `date` | `D` | `4` | `open` | — | Projekto veiklų pabaigos data | — |
| `turi_partneriu` | `boolean` | — | `4` | `open` | — | Ar turi partnerių? | — |
| `sutarties_busena` | `string` | — | `4` | `open` | — | Sutarties būsena | — |
| `sutarties_busenos_data` | `date` | `D` | `4` | `open` | — | Sutarties būsenos data | — |
| `priemones_id` | `string` | — | `4` | `open` | — | Finansavimo priemonės identifikacinis numeris | — |
| `priemones_kodas` | `string` | — | `4` | `open` | — | Finansavimo priemonės kodas | — |
| `priemones_pavadinimas` | `string` | — | `4` | `open` | — | Finansavimo priemonės pavadinimas | — |
| `atsakinga_institucija` | `string` | — | `4` | `open` | — | Atsakinga instituciją už finansavimo priemonę | — |
| `regionas` | `string` | — | `4` | `open` | — | Regionas kam skirta finansavimo priemonės parama | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `sutarties_busena` | `"Įgyvendinama sutartis"` | — | — | Įgyvendinama sutartis | — |
| `sutarties_busena` | `"Baigtas"` | — | — | Baigtas | — |
| `sutarties_busena` | `"Įgyvendinama"` | — | — | Įgyvendinama | — |
| `sutarties_busena` | `"Nutraukta sutartis"` | — | — | Nutraukta sutartis | — |
| `sutarties_busena` | `"Atsisakė pasirašyti"` | — | — | Atsisakė pasirašyti | — |
| `sutarties_busena` | `"Baigta"` | — | — | Baigta | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys.csv
