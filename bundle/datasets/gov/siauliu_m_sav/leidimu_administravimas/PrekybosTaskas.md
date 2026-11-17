---
type: Table
title: "PrekybosTaskas — Šiaulių miesto savivaldybės išduoti leidimai kioskams ir pavilionams"
description: "Informacija apie Šiaulių miesto savivaldybės išduotus leidimus kioskams ir pavilionams"
resource: "https://get.data.gov.lt/datasets/gov/siauliu_m_sav/leidimu_administravimas/PrekybosTaskas"
tags: [gov, siauliu_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/siauliu_m_sav/leidimu_administravimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/leidimu_administravimas.csv#L64"
    last_modified: "2026-11-11T14:39:20Z"
---

# PrekybosTaskas — Šiaulių miesto savivaldybės išduoti leidimai kioskams ir pavilionams

Informacija apie Šiaulių miesto savivaldybės išduotus leidimus kioskams ir pavilionams

- **Model:** `datasets/gov/siauliu_m_sav/leidimu_administravimas/PrekybosTaskas`[^manifest]
- **Dataset:** [Šiaulių miesto savivaldybės išduoti leidimai ir jų apmokėjimai](../leidimu_administravimas.md) (`datasets/gov/siauliu_m_sav/leidimu_administravimas`)
- **Manifest CSV:** [datasets/gov/siauliu_m_sav/leidimu_administravimas.csv#L64](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/leidimu_administravimas.csv#L64)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/siauliu_m_sav/leidimu_administravimas/PrekybosTaskas`
- **Primary Key (`ref`):** `leidimo_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `leidimo_id` | `string` | — | `4` | `open` | — | Leidimo identifikatorius | — |
| `veiklos_tipas` | `string` | — | `4` | `open` | — | Veiklos tipas | — |
| `prekes_ar_paslaugos` | `string` | — | `4` | `open` | — | Prekės ar paslaugos | — |
| `leidimas_galioja_nuo` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo pradžia | — |
| `leidimas_galioja_iki` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo pabaiga | — |
| `leidimo_tipas` | `string` | — | `4` | `open` | — | Leidimo tipas | — |
| `leidimo_numeris` | `string` | — | `4` | `open` | — | Leidimo numeris | — |
| `juridinio_asmens_kodas` | `string` | — | `4` | `open` | — | Juridinio asmens, kuriam išduota leidimas, kodas | — |
| `juridinio_asmens_pavadinimas` | `string` | — | `4` | `open` | — | Juridinio asmens, kuriam išduota leidimas, pavadinimas | — |
| `fizinio_asmens_kodas` | `string` | — | `4` | `open` | — | Fizinio asmens, kuriam išduota leidimas, kodas | — |
| `fizinio_asmens_vardas_pavarde` | `string` | — | `4` | `open` | — | Fizinio asmens, kuriam išduota leidimas, vardas ir pavardė | — |
| `asmens_tipas` | `string` | — | `4` | `open` | — | Asmens tipas | — |
| `vda_asmens_tipas` | `string` | — | `4` | `open` | — | VDA nustatytas asmens tipas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `veiklos_tipas` | `"PrekybaNeMaistoProduktais"` | — | — | Prekyba ne maisto produktais | — |
| `veiklos_tipas` | `"PrekybaMaistoProduktais"` | — | — | Prekyba maisto produktais | — |
| `leidimo_tipas` | `"KioskaiPavilijonai.Pavilijonai"` | — | — | Pavilijonai | — |
| `leidimo_tipas` | `"KioskaiPavilijonai.Kioskai"` | — | — | Kioskai | — |
| `leidimo_tipas` | `"KioskaiPavilijonai.LaukoKavinė"` | — | — | Lauko kavinė | — |
| `asmens_tipas` | `"LietuvosJuridinis"` | — | — | Juridinis asmuo įsisteigęs Lietuvoje | — |
| `asmens_tipas` | `"LietuvosFizinis"` | — | — | Fizinis asmuo įsisteigęs Lietuvoje | — |
| `asmens_tipas` | `"UzsienioJuridinis"` | — | — | Juridinis asmuo įsisteigęs užsienyje | — |
| `vda_asmens_tipas` | `"Juridinis asmuo"` | — | — | Juridinis asmuo įsisteigęs Lietuvoje | — |
| `vda_asmens_tipas` | `"Fizinis asmuo"` | — | — | Fizinis asmuo Lietuvos pilietis | — |
| `vda_asmens_tipas` | `"Kita"` | — | — | Nenustatytas asmuo | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/siauliu_m_sav/leidimu_administravimas.csv
