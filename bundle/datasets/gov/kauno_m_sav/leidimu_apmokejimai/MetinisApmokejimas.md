---
type: Table
title: "MetinisApmokejimas — Apmokėjimai už Kauno miesto savivaldybės išduodamus leidimus"
description: "Apmokėjimai už Kauno miesto savivaldybės išduodamus leidimus reklamai, alkoholio ir tabako prekybai"
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/leidimu_apmokejimai/MetinisApmokejimas"
tags: [gov, kauno_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/leidimu_apmokejimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/leidimu_apmokejimai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# MetinisApmokejimas — Apmokėjimai už Kauno miesto savivaldybės išduodamus leidimus

Apmokėjimai už Kauno miesto savivaldybės išduodamus leidimus reklamai, alkoholio ir tabako prekybai

- **Model:** `datasets/gov/kauno_m_sav/leidimu_apmokejimai/MetinisApmokejimas`[^manifest]
- **Dataset:** [Apmokėjimai už Kauno miesto savivaldybės išduodamus leidimus](../leidimu_apmokejimai.md) (`datasets/gov/kauno_m_sav/leidimu_apmokejimai`)
- **Manifest CSV:** [datasets/gov/kauno_m_sav/leidimu_apmokejimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/leidimu_apmokejimai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/leidimu_apmokejimai/MetinisApmokejimas`
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
| `licencijos_tipas` | `string` | — | `4` | `open` | — | Licencijos tipas | — |
| `sumoketa_imoku_suma` | `number` | — | `4` | `open` | — | Sumokėtų įmokų suma už mokestinius metus eurais | — |
| `sumoketas_imoku_skaicius` | `integer` | — | `4` | `open` | — | Mokamų įmokų skaičius mokestiniais metais | — |
| `irasu_skaicius_mokestiniais_metais` | `integer` | — | `4` | `open` | — | Įrašų skaičius mokestiniais metais | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `imoku_gavejas` | `"Kauno miesto savivaldybė"` | — | — | — | — |
| `imoku_gavejo_kodas` | `"188764867"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/leidimu_apmokejimai.csv
