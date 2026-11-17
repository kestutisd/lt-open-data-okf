---
type: Table
title: "LeidimoImoka — Įmokos už Panevėžio miesto savivaldybės išduodamus leidimus ir licencijas"
description: "Informacija apie imokas už Panevėžio miesto savivaldybės išduodamus leidimus ir licencijas"
resource: "https://get.data.gov.lt/datasets/gov/panevezio_m_sav/leidimu_administravimas/LeidimoImoka"
tags: [gov, panevezio_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/panevezio_m_sav/leidimu_administravimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/leidimu_administravimas.csv#L29"
    last_modified: "2026-11-11T14:39:20Z"
---

# LeidimoImoka — Įmokos už Panevėžio miesto savivaldybės išduodamus leidimus ir licencijas

Informacija apie imokas už Panevėžio miesto savivaldybės išduodamus leidimus ir licencijas

- **Model:** `datasets/gov/panevezio_m_sav/leidimu_administravimas/LeidimoImoka`[^manifest]
- **Dataset:** [Panevėžio miesto savivaldybės išduotos licencijos ir jų apmokėjimai](../leidimu_administravimas.md) (`datasets/gov/panevezio_m_sav/leidimu_administravimas`)
- **Manifest CSV:** [datasets/gov/panevezio_m_sav/leidimu_administravimas.csv#L29](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/leidimu_administravimas.csv#L29)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/panevezio_m_sav/leidimu_administravimas/LeidimoImoka`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Įrašo identifikatorius | — |
| `mokestiniai_metai` | `integer` | — | `4` | `open` | — | Mokestiniai metai | — |
| `juridinio_asmens_kodas` | `string` | — | `4` | `open` | — | Juridinio asmens kodas | — |
| `juridinio_asmens_pavadinimas` | `string` | — | `4` | `open` | — | Juridinio asmens pavadinimas | — |
| `fizinio_asmens_kodas` | `string` | — | `4` | `open` | — | Fizinio asmens kodas | — |
| `fizinio_asmens_vardas_pavarde` | `string` | — | `4` | `open` | — | Fizinio asmens vardas ir pavardė | — |
| `imoku_gavejas` | `string` | — | `4` | `open` | — | Įmokų gavėjas | — |
| `imoku_gavejo_kodas` | `string` | — | `4` | `open` | — | Įmokų gavėjo kodas | — |
| `leidimo_licencijos_tipas` | `string` | — | `4` | `open` | — | Licencijos ar leidimo tipas | — |
| `sumoketu_imoku_suma` | `number` | — | `4` | `open` | — | Sumokėtų įmokų suma už mokestinius metus eurais | — |
| `sumoketu_imoku_skaicius` | `integer` | — | `4` | `open` | — | Mokamų įmokų skaičius mokestiniais metais | — |
| `sumoketu_imoku_irasai` | `integer` | — | `4` | `open` | — | Įrašų skaičius mokestiniais metais | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `imoku_gavejas` | `"Valstybinė mokesčių inspekcija"` | — | — | Valstybinė mokesčių inspekcija | — |
| `imoku_gavejas` | `"Panevėžio_miesto_savivaldybė"` | — | — | Panevėžio miesto savivaldybė | — |
| `imoku_gavejo_kodas` | `"188659752"` | — | — | Valstybinės mokesčių inspekcijos kodas | — |
| `imoku_gavejo_kodas` | `"288724610"` | — | — | Panevėžio miesto savivaldybės kodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/panevezio_m_sav/leidimu_administravimas.csv
