---
type: Table
title: "FinansuojamaSuma — Projekto įgyvendinimui prašomos finansuoti, finansuotos bei grąžintos sumos"
description: "Duomenys pateikiami iš Informacinės projektų administravimo sistemos (IPAS) skirtos kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis, susijusius su VšĮ Centrinės projektų valdymo agentūros administruojamų Europos Sąjungos 2014–2020 m. struktūrinių fondų..."
resource: "https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys/FinansuojamaSuma"
tags: [gov, cpva, finansuojamasuma, deployed, level-4, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys.csv#L13"
    title: "atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys.csv#L13"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2904/"
    title: "data.gov.lt DCAT-AP — datasets/gov/cpva/paramu_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# FinansuojamaSuma — Projekto įgyvendinimui prašomos finansuoti, finansuotos bei grąžintos sumos

Duomenys pateikiami iš Informacinės projektų administravimo sistemos (IPAS) skirtos kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis, susijusius su VšĮ Centrinės projektų valdymo agentūros administruojamų Europos Sąjungos 2014–2020 m. struktūrinių fondų programos projektų įgyvendinimu. Lentelėje galima rasti tokią informaciją: pateiktos paraiškos bei pasirašytos finansuoti sutartys (viena eilutė atitinka atitinkamą paraišką, pasirašytos sutarties statusų pasikeitimų eigą). Projektai, kurie buvo vykdomi naudojantis šia sistema jau pasibaigę, bet sistemos duomenys retais atvejais vis dar atnaujinami. Tokiu atveju, duomenų atnaujinimas numatomas kas 6 mėn. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/cpva/paramu_duomenys/FinansuojamaSuma`[^manifest]
- **Dataset:** [VšĮ Centrinės projektų valdymo agentūros teikiamų paramų sutartys ir finansavimas](../paramu_duomenys.md) (`datasets/gov/cpva/paramu_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/cpva/paramu_duomenys.csv#L13](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys.csv#L13)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys/FinansuojamaSuma` (`deployed`)[^manifest]
- **Provider:** `cpva` — VšĮ Centrinė projektų valdymo agentūra *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_2`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `grazinimo_priezastis` | `"Nesusijusios su pažeidimu"` | — | — | Nesusijusios su pažeidimu | — |
| `grazinimo_priezastis` | `"Susijusios su pažeidimu"` | — | — | Susijusios su pažeidimu | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys.csv#L13 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys.csv#L13)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/cpva/paramu_duomenys (https://data.gov.lt/datasets/2904/)
