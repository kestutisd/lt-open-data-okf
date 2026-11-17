---
type: Table
title: "Biudzetas — Gyventojų investicinių projektų atrankos informacinės sistemos „Dalyvauk“ dalyvaujamųjų biudžetų pasiūlymų duomenys."
description: "Klaipėdos miesto savivaldybės informacinės sistemos „Dalyvauk“ duomenys, kurioje gyventojai teikia idėjas ir iniciatyvas dėl viešosios infrastruktūros gerinimo Klaipėdos mieste, taip pat dalyvauja balsavime renkant patraukliausias..."
resource: "https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/dalyvaujiemieji_biudzetai/Biudzetas"
tags: [gov, klaipedos_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/dalyvaujiemieji_biudzetai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/dalyvaujiemieji_biudzetai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Biudzetas — Gyventojų investicinių projektų atrankos informacinės sistemos „Dalyvauk“ dalyvaujamųjų biudžetų pasiūlymų duomenys.

Klaipėdos miesto savivaldybės informacinės sistemos „Dalyvauk“ duomenys, kurioje gyventojai teikia idėjas ir iniciatyvas dėl viešosios infrastruktūros gerinimo Klaipėdos mieste, taip pat dalyvauja balsavime renkant patraukliausias iniciatyvas.

Lentelė sudaryta VDA ir yra atnaujinama kasmet. Šioje lentelėje pateikiami, tokie duomenys kaip pasiūlymo data ir laikas, dalyvaujamasis biudžetas, kurio metu idėja buvo pasiūlyta, siūlančioji organizacija (jei pasiūlyta ne fizinio asmens), pateikiamos idėjos, jų aprašymai, numatomi rezultatai, balsavimo rezultatai, įvykdomumo vertinimo rezultatai, duomenys apie tai, ar idėja buvo atrinkta balsavimui ir ar laimėjo balsavimą.

Susipažinti su gyventojų pateiktomis iniciatyvomis galima interneto svetainėje https://dalyvauk.klaipeda.lt/.

- **Model:** `datasets/gov/klaipedos_m_sav/dalyvaujiemieji_biudzetai/Biudzetas`[^manifest]
- **Dataset:** [Gyventojų investicinių projektų atrankos informacinės sistemos „Dalyvauk“ dalyvaujamųjų biudžetų pasiūlymų duomenys.](../dalyvaujiemieji_biudzetai.md) (`datasets/gov/klaipedos_m_sav/dalyvaujiemieji_biudzetai`)
- **Manifest CSV:** [datasets/gov/klaipedos_m_sav/dalyvaujiemieji_biudzetai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/dalyvaujiemieji_biudzetai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/dalyvaujiemieji_biudzetai/Biudzetas`
- **Primary Key (`ref`):** `projekto_id`
- **Level:** `4`
- **Access:** `open`

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

[^manifest]: atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/dalyvaujiemieji_biudzetai.csv
