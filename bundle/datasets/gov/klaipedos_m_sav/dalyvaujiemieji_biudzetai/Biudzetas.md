---
type: Table
title: "Biudzetas — Gyventojų investicinių projektų atrankos informacinės sistemos „Dalyvauk“ dalyvaujamųjų biudžetų pasiūlymų duomenys."
description: "Klaipėdos miesto savivaldybės informacinės sistemos „Dalyvauk“ duomenys, kurioje gyventojai teikia idėjas ir iniciatyvas dėl viešosios infrastruktūros gerinimo Klaipėdos mieste, taip pat dalyvauja balsavime renkant patraukliausias iniciatyvas."
resource: "https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/dalyvaujiemieji_biudzetai/Biudzetas"
tags: [gov, klaipedos_m_sav, biudzetas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/dalyvaujiemieji_biudzetai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/dalyvaujiemieji_biudzetai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2690/"
    title: "data.gov.lt DCAT-AP — datasets/gov/klaipedos_m_sav/dalyvaujiemieji_biudzetai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Biudzetas — Gyventojų investicinių projektų atrankos informacinės sistemos „Dalyvauk“ dalyvaujamųjų biudžetų pasiūlymų duomenys.

Klaipėdos miesto savivaldybės informacinės sistemos „Dalyvauk“ duomenys, kurioje gyventojai teikia idėjas ir iniciatyvas dėl viešosios infrastruktūros gerinimo Klaipėdos mieste, taip pat dalyvauja balsavime renkant patraukliausias iniciatyvas. Lentelė sudaryta VDA ir yra atnaujinama kasmet. Šioje lentelėje pateikiami, tokie duomenys kaip pasiūlymo data ir laikas, dalyvaujamasis biudžetas, kurio metu idėja buvo pasiūlyta, siūlančioji organizacija (jei pasiūlyta ne fizinio asmens), pateikiamos idėjos, jų aprašymai, numatomi rezultatai, balsavimo rezultatai, įvykdomumo vertinimo rezultatai, duomenys apie tai, ar idėja buvo atrinkta balsavimui ir ar laimėjo balsavimą. Susipažinti su gyventojų pateiktomis iniciatyvomis galima interneto svetainėje https://dalyvauk.klaipeda.lt/.[^manifest]

- **Model:** `datasets/gov/klaipedos_m_sav/dalyvaujiemieji_biudzetai/Biudzetas`[^manifest]
- **Dataset:** [Gyventojų investicinių projektų atrankos informacinės sistemos „Dalyvauk“ dalyvaujamųjų biudžetų...](../dalyvaujiemieji_biudzetai.md) (`datasets/gov/klaipedos_m_sav/dalyvaujiemieji_biudzetai`)[^manifest]
- **Manifest CSV:** [datasets/gov/klaipedos_m_sav/dalyvaujiemieji_biudzetai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/dalyvaujiemieji_biudzetai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/dalyvaujiemieji_biudzetai/Biudzetas` (`deployed`)[^manifest]
- **Provider:** `klaipedos_m_sav` — Klaipėdos miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `projekto_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `projekto_id` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `projekto_ikelimo_data` | `datetime` | `S` | `4` | `open` | — | Sukūrimo data | — |
| `biudzetas` | `string` | — | `4` | `open` | — | Dalyvaujamasis biudžetas | — |
| `organizacija` | `string` | — | `4` | `open` | — | Pasiūlymą pateikusi organizacija | — |
| `autoriaus_vardas_pavarde` | `string` | — | `4` | `open` | — | Autoriaus vardas ir pavardė | — |
| `autoriaus_gimimo_metai` | `datetime` | `Y` | `4` | `open` | — | Autoriaus gimimo metai | — |
| `projekto_pavadinimas` | `string` | — | `4` | `open` | — | Projekto pavadinimas | — |
| `projekto_aprasymas` | `string` | — | `4` | `open` | — | Projekto aprašymas | — |
| `projekto_rezultatai` | `string` | — | `4` | `open` | — | Tikėtini projekto įgyvendinimo rezultatai | — |
| `projekto_samata` | `number` | — | `4` | `open` | — | Numatoma projekto įgyvendinimo kaina | — |
| `samatos_paaiskinimas` | `string` | — | `4` | `open` | — | Sąmatos pagrindimas | — |
| `vieta` | `string` | — | `4` | `open` | — | Vietovė kur numatomas įgyvendinimas | — |
| `ar_atrinkta` | `boolean` | — | `4` | `open` | — | Ar projektas atrinktas balsavimui | — |
| `ivykdomumas` | `string` | — | `4` | `open` | — | Įvykdomumo vertinimas | — |
| `neivykdomumo_priezastis` | `string` | — | `4` | `open` | — | Priežastys kodėl projektas neįgyvendinamas | — |
| `komentaru_skaicius` | `number` | — | `4` | `open` | — | Bendras gautų komentarų skaičius | — |
| `fiziniai_balsai` | `number` | — | `4` | `open` | — | Gyvai atiduotų balsų skaičius | — |
| `balsai` | `number` | — | `4` | `open` | — | Bendras balsų skaičius | — |
| `vertinimas_baigtas` | `boolean` | — | `4` | `open` | — | Ar pasiūlymo vertinimas užbaigtas | — |
| `ar_laimejo` | `boolean` | — | `4` | `open` | — | Ar projektas laimėjo balsavimą | — |
| `paskutinio_atnaujinimo_data` | `datetime` | `S` | `4` | `open` | — | Datos ir laiko žyma kada įrašas paskutinį kartą atnaujintas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/dalyvaujiemieji_biudzetai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/dalyvaujiemieji_biudzetai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/klaipedos_m_sav/dalyvaujiemieji_biudzetai (https://data.gov.lt/datasets/2690/)
