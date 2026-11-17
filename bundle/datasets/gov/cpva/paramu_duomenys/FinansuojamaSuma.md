---
type: Table
title: "FinansuojamaSuma — Projekto įgyvendinimui prašomos finansuoti, finansuotos bei grąžintos sumos"
description: "Duomenys pateikiami iš Informacinės projektų administravimo sistemos (IPAS) skirtos kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis, susijusius su VšĮ Centrinės projektų valdymo agentūros administruojamų Europos..."
resource: "https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys/FinansuojamaSuma"
tags: [gov, cpva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys.csv#L13"
    last_modified: "2026-11-11T14:39:20Z"
---

# FinansuojamaSuma — Projekto įgyvendinimui prašomos finansuoti, finansuotos bei grąžintos sumos

Duomenys pateikiami iš Informacinės projektų administravimo sistemos (IPAS) skirtos kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis, susijusius su VšĮ Centrinės projektų valdymo agentūros administruojamų Europos Sąjungos 2014–2020 m. struktūrinių fondų programos projektų įgyvendinimu. Lentelėje galima rasti tokią informaciją:

pateiktos paraiškos bei pasirašytos finansuoti sutartys (viena eilutė atitinka atitinkamą paraišką, pasirašytos sutarties statusų pasikeitimų eigą).

Projektai, kurie buvo vykdomi naudojantis šia sistema jau pasibaigę, bet sistemos duomenys retais atvejais vis dar atnaujinami. Tokiu atveju, duomenų atnaujinimas numatomas kas 6 mėn.

- **Model:** `datasets/gov/cpva/paramu_duomenys/FinansuojamaSuma`[^manifest]
- **Dataset:** [VšĮ Centrinės projektų valdymo agentūros teikiamų paramų sutartys ir finansavimas](../paramu_duomenys.md) (`datasets/gov/cpva/paramu_duomenys`)
- **Manifest CSV:** [datasets/gov/cpva/paramu_duomenys.csv#L13](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys.csv#L13)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys/FinansuojamaSuma`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Identifikacinis numeris | — |
| `paraiskos_id` | `string` | — | `4` | `open` | — | Paraiškos identifikacinis numeris | — |
| `sutarties_id` | `string` | — | `4` | `open` | — | Sutarties identifikacinis numeris | — |
| `sutarties_nr` | `string` | — | `4` | `open` | — | Sutarties numeris | — |
| `prasoma_suma` | `number` | — | `4` | `open` | — | Prašoma finansuoti suma | — |
| `finansuojama_suma` | `number` | — | `4` | `open` | — | Finansuojama suma | — |
| `sumoketa_suma` | `number` | — | `4` | `open` | — | Sumokėta finansuojama suma | — |
| `grazinama_suma` | `number` | — | `4` | `open` | — | Grąžinama suma | — |
| `grazinimo_priezastis` | `string` | — | `4` | `open` | — | Grąžinimo priežasties tipas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `grazinimo_priezastis` | `"Nesusijusios su pažeidimu"` | — | — | Nesusijusios su pažeidimu | — |
| `grazinimo_priezastis` | `"Susijusios su pažeidimu"` | — | — | Susijusios su pažeidimu | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys.csv
