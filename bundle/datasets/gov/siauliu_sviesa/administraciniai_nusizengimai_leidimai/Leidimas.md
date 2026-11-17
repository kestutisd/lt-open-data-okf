---
type: Table
title: "Leidimas — Išduoti automobilių parkavimo leidimai Šiaulių mieste"
description: "Informacija apie išduotus automobilių parkavimo leidimus Šiaulių mieste"
resource: "https://get.data.gov.lt/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai/Leidimas"
tags: [gov, siauliu_sviesa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L20"
    last_modified: "2026-11-11T14:39:20Z"
---

# Leidimas — Išduoti automobilių parkavimo leidimai Šiaulių mieste

Informacija apie išduotus automobilių parkavimo leidimus Šiaulių mieste

- **Model:** `datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai/Leidimas`[^manifest]
- **Dataset:** [Išduoti automobilių stovėjimo leidimai ir užfiksuoti pažeidimai Šiaulių mieste](../administraciniai_nusizengimai_leidimai.md) (`datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai`)
- **Manifest CSV:** [datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L20](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L20)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai/Leidimas`
- **Primary Key (`ref`):** `leidimo_automobiliui_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `leidimo_automobiliui_id` | `string` | — | `4` | `open` | — | Leidimo automobiliui identifikatorius | — |
| `uzklausos_data` | `date` | `D` | `4` | `open` | — | Užklauso leidimui data | — |
| `galioja_nuo` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo pradžia | — |
| `galioja_iki` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo pabaiga | — |
| `asmens_vardas_pavarde_pavadinimas` | `string` | — | `4` | `open` | — | Šifruotas juridinio asmens vardas ir pavardė ar juridinio asmens pavadinimas | — |
| `vda_apmokejimo_budas` | `string` | — | `4` | `open` | — | VDA nustatytas apmokėjimo būdas | — |
| `asmens_tipas` | `string` | — | `4` | `open` | — | Asmens tipas | — |
| `leidimo_numeris` | `string` | — | `4` | `open` | — | Parkavimo leidimo numeris | — |
| `vda_nurodyto_automobilio_marke` | `string` | — | `4` | `open` | — | VDA nustatyta nurodyta automobilio markė leidime | — |
| `nurodytas_valstybinis_numeris` | `string` | — | `4` | `open` | — | Šifruotas leidime nurodyto automobilio valstybinis numeris | — |
| `vda_valstybinio_numerio_struktura` | `string` | — | `4` | `open` | — | VDA nustatyta valstybinio numerio struktūra | — |
| `vda_leidimo_vietos_koordinates` | `geometry(point, 4326)` | — | `4` | `open` | — | VDA nustatytos leidimo vietos koordinatės | — |
| `vda_koordinates_balai` | `number` | — | `4` | `open` | — | VDA nustatytų koordinačių tikslumas balais | — |
| `parkavimo_zona` | `string` | — | `4` | `open` | — | Nurodyta parkavimo zona | — |
| `leidimo_tipas` | `string` | — | `4` | `open` | — | Leidimo tipas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `asmens_tipas` | `"Fizinis asmuo"` | — | — | — | — |
| `asmens_tipas` | `"Juridinis asmuo"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv
