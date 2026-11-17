---
type: Table
title: "Apsilankymas — Gyventojų investicinių projektų atrankos platformos „Dalyvauk“ puslapio apsilankymai."
description: "Klaipėdos miesto savivaldybės platformos „Dalyvauk“ duomenys, kurioje gyventojai teikia idėjas ir iniciatyvas dėl viešosios infrastruktūros gerinimo Klaipėdos mieste."
resource: "https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/dalyvauk_apsilankymai/Apsilankymas"
tags: [gov, klaipedos_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/dalyvauk_apsilankymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/dalyvauk_apsilankymai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Apsilankymas — Gyventojų investicinių projektų atrankos platformos „Dalyvauk“ puslapio apsilankymai.

Klaipėdos miesto savivaldybės platformos „Dalyvauk“ duomenys, kurioje gyventojai teikia idėjas ir iniciatyvas dėl viešosios infrastruktūros gerinimo Klaipėdos mieste. Taip pat dalyvauja balsavime, renkant patraukliausias iniciatyvas.

Lentelė sudaryta VDA ir yra atnaujinama kas ketvirtį. Šioje lentelėje pateikiami, tokie duomenys kaip puslapio lankytojų naršyklė, operacinė sistema, įrenginio tipas, apsilankymo laikas ir pagal IP adresą nustatyti vietovės duomenys.

Susipažinti su gyventojų pateiktomis iniciatyvomis galima interneto svetainėje https://dalyvauk.klaipeda.lt/.

- **Model:** `datasets/gov/klaipedos_m_sav/dalyvauk_apsilankymai/Apsilankymas`[^manifest]
- **Dataset:** [Gyventojų investicinių projektų atrankos platformos „Dalyvauk“ puslapio apsilankymai.](../dalyvauk_apsilankymai.md) (`datasets/gov/klaipedos_m_sav/dalyvauk_apsilankymai`)
- **Manifest CSV:** [datasets/gov/klaipedos_m_sav/dalyvauk_apsilankymai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/dalyvauk_apsilankymai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/dalyvauk_apsilankymai/Apsilankymas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikacinis kodas | — |
| `lankytojo_id` | `string` | — | `4` | `open` | — | Lankytojo identifikacijos kodas | — |
| `ip_adresas` | `string` | — | `4` | `open` | — | Lankytojo IP adresas | — |
| `nukreiptas_is` | `string` | — | `4` | `open` | — | Nukreiptas iš | — |
| `narsykle` | `string` | — | `4` | `open` | — | Naršyklė | — |
| `operacine_sistema` | `string` | — | `4` | `open` | — | Operacinė sistema | — |
| `irenginio_tipas` | `string` | — | `4` | `open` | — | Įrenginio tipas | — |
| `pradeta` | `datetime` | `S` | `4` | `open` | — | Sesija pradėta | — |
| `salies_kodas` | `string` | — | `4` | `open` | — | Šalies kodas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė | — |
| `miestas` | `string` | — | `4` | `open` | — | Miestas | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Lankytojo miesto platuma pagal WGS84 koordinačių sistemą | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Lankytojo miesto ilguma pagal WGS84 koordinačių sistemą | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/dalyvauk_apsilankymai.csv
