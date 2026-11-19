---
type: Table
title: "Leidimas — Išduoti automobilių parkavimo leidimai Šiaulių mieste"
description: "Informacija apie išduotus automobilių parkavimo leidimus Šiaulių mieste"
resource: "https://get.data.gov.lt/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai/Leidimas"
tags: [gov, siauliu_sviesa, leidimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L20"
    title: "atviriduomenys/manifest — datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L20"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4037/"
    title: "data.gov.lt DCAT-AP — datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Leidimas — Išduoti automobilių parkavimo leidimai Šiaulių mieste

Informacija apie išduotus automobilių parkavimo leidimus Šiaulių mieste[^manifest]

- **Model:** `datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai/Leidimas`[^manifest]
- **Dataset:** [Išduoti automobilių stovėjimo leidimai ir užfiksuoti pažeidimai Šiaulių mieste](../administraciniai_nusizengimai_leidimai.md) (`datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L20](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L20)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai/Leidimas` (`deployed`)[^manifest]
- **Provider:** `siauliu_sviesa` — UAB Šiaulių šviesa *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `leidimo_automobiliui_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `asmens_tipas` | `"Fizinis asmuo"` | — | — | — | — |
| `asmens_tipas` | `"Juridinis asmuo"` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L20 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L20)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai (https://data.gov.lt/datasets/4037/)
