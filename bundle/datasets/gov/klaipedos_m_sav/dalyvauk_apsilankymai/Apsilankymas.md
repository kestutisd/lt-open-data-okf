---
type: Table
title: "Apsilankymas — Gyventojų investicinių projektų atrankos platformos „Dalyvauk“ puslapio apsilankymai."
description: "Klaipėdos miesto savivaldybės platformos „Dalyvauk“ duomenys, kurioje gyventojai teikia idėjas ir iniciatyvas dėl viešosios infrastruktūros gerinimo Klaipėdos mieste."
resource: "https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/dalyvauk_apsilankymai/Apsilankymas"
tags: [gov, klaipedos_m_sav, apsilankymas, deployed, level-4, cadence-annual_3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/dalyvauk_apsilankymai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/dalyvauk_apsilankymai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2691/"
    title: "data.gov.lt DCAT-AP — datasets/gov/klaipedos_m_sav/dalyvauk_apsilankymai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Apsilankymas — Gyventojų investicinių projektų atrankos platformos „Dalyvauk“ puslapio apsilankymai.

Klaipėdos miesto savivaldybės platformos „Dalyvauk“ duomenys, kurioje gyventojai teikia idėjas ir iniciatyvas dėl viešosios infrastruktūros gerinimo Klaipėdos mieste. Taip pat dalyvauja balsavime, renkant patraukliausias iniciatyvas. Lentelė sudaryta VDA ir yra atnaujinama kas ketvirtį. Šioje lentelėje pateikiami, tokie duomenys kaip puslapio lankytojų naršyklė, operacinė sistema, įrenginio tipas, apsilankymo laikas ir pagal IP adresą nustatyti vietovės duomenys. Susipažinti su gyventojų pateiktomis iniciatyvomis galima interneto svetainėje https://dalyvauk.klaipeda.lt/.[^manifest]

- **Model:** `datasets/gov/klaipedos_m_sav/dalyvauk_apsilankymai/Apsilankymas`[^manifest]
- **Dataset:** [Gyventojų investicinių projektų atrankos platformos „Dalyvauk“ puslapio apsilankymai.](../dalyvauk_apsilankymai.md) (`datasets/gov/klaipedos_m_sav/dalyvauk_apsilankymai`)[^manifest]
- **Manifest CSV:** [datasets/gov/klaipedos_m_sav/dalyvauk_apsilankymai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/dalyvauk_apsilankymai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/dalyvauk_apsilankymai/Apsilankymas` (`deployed`)[^manifest]
- **Provider:** `klaipedos_m_sav` — Klaipėdos miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_3`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/dalyvauk_apsilankymai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/dalyvauk_apsilankymai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/klaipedos_m_sav/dalyvauk_apsilankymai (https://data.gov.lt/datasets/2691/)
