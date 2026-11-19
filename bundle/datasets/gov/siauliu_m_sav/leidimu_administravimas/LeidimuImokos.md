---
type: Table
title: "LeidimuImokos — Įmokos už Šiaulių miesto savivaldybės išduodamus reklamos leidimus"
description: "Informacija apie imokas už Šiaulių miesto savivaldybės išduodamus reklamos leidimus"
resource: "https://get.data.gov.lt/datasets/gov/siauliu_m_sav/leidimu_administravimas/LeidimuImokos"
tags: [gov, siauliu_m_sav, leidimuimokos, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/leidimu_administravimas.csv#L115"
    title: "atviriduomenys/manifest — datasets/gov/siauliu_m_sav/leidimu_administravimas.csv#L115"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2912/"
    title: "data.gov.lt DCAT-AP — datasets/gov/siauliu_m_sav/leidimu_administravimas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# LeidimuImokos — Įmokos už Šiaulių miesto savivaldybės išduodamus reklamos leidimus

Informacija apie imokas už Šiaulių miesto savivaldybės išduodamus reklamos leidimus[^manifest]

- **Model:** `datasets/gov/siauliu_m_sav/leidimu_administravimas/LeidimuImokos`[^manifest]
- **Dataset:** [Šiaulių miesto savivaldybės išduoti leidimai ir jų apmokėjimai](../leidimu_administravimas.md) (`datasets/gov/siauliu_m_sav/leidimu_administravimas`)[^manifest]
- **Manifest CSV:** [datasets/gov/siauliu_m_sav/leidimu_administravimas.csv#L115](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/leidimu_administravimas.csv#L115)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/siauliu_m_sav/leidimu_administravimas/LeidimuImokos` (`deployed`)[^manifest]
- **Provider:** `siauliu_m_sav` — Šiaulių miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Įrašo identifikatorius | — |
| `mokestiniai_metai` | `string` | — | `4` | `open` | — | Mokestiniai metai | — |
| `juridinio_asmens_kodas` | `string` | — | `4` | `open` | — | Juridinio asmens kodas | — |
| `juridinio_asmens_pavadinimas` | `string` | — | `4` | `open` | — | Juridinio asmens pavadinimas | — |
| `fizinio_asmens_kodas` | `string` | — | `4` | `open` | — | Fizinio asmens kodas | — |
| `fizinio_asmens_vardas_pavarde` | `string` | — | `4` | `open` | — | Fizinio asmens vardas ir pavardė | — |
| `imoku_gavejas` | `string` | — | `4` | `open` | — | Įmokų gavėjas | — |
| `imoku_gavejo_kodas` | `string` | — | `4` | `open` | — | Įmokų gavėjo kodas | — |
| `leidimo_tipas` | `string` | — | `4` | `open` | — | Leidimo tipas | — |
| `sumoketu_imoku_suma` | `number` | — | `4` | `open` | — | Sumokėtų įmokų suma už mokestinius metus eurais | — |
| `sumoketu_imoku_skaicius` | `integer` | — | `4` | `open` | — | Mokamų įmokų skaičius mokestiniais metais | — |
| `sumoketu_imoku_irasai` | `integer` | — | `4` | `open` | — | Įrašų skaičius mokestiniais metais | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `imoku_gavejas` | `"Šiaulių miesto savivaldybė"` | — | — | Šiaulių miesto savivaldybė | — |
| `imoku_gavejo_kodas` | `"188771665"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/siauliu_m_sav/leidimu_administravimas.csv#L115 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/leidimu_administravimas.csv#L115)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/siauliu_m_sav/leidimu_administravimas (https://data.gov.lt/datasets/2912/)
