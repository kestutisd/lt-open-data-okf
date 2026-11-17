---
type: Table
title: "Sertifikatas — Pateikiama informacija apie išduotus fitosanitarijos sertifikatus per tam tikrą laikotarpį (išdavimo data; sertifikato numeris; būsena; fitosanitarinio sertifikato tipas; šalis gavėja..."
description: "Spinta table datasets/gov/vat/fitosanitarijos_ataskaitos/Sertifikatas (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/fitosanitarijos_ataskaitos/Sertifikatas"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/r4_fitosanitarijos_ataskaitos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r4_fitosanitarijos_ataskaitos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sertifikatas — Pateikiama informacija apie išduotus fitosanitarijos sertifikatus per tam tikrą laikotarpį (išdavimo data; sertifikato numeris; būsena; fitosanitarinio sertifikato tipas; šalis gavėja...

- **Model:** `datasets/gov/vat/fitosanitarijos_ataskaitos/Sertifikatas`[^manifest]
- **Dataset:** [datasets/gov/vat/fitosanitarijos_ataskaitos](../fitosanitarijos_ataskaitos.md) (`datasets/gov/vat/fitosanitarijos_ataskaitos`)
- **Manifest CSV:** [datasets/gov/vat/r4_fitosanitarijos_ataskaitos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r4_fitosanitarijos_ataskaitos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/fitosanitarijos_ataskaitos/Sertifikatas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Įrašo identifikatorius | — |
| `padalinys` | `string` | — | `4` | `open` | — | Patikrinimą atlikęs teritorinis padalinys | — |
| `transporto_priemone` | `string` | — | `4` | `open` | — | Transporto priemonė | — |
| `busena` | `string` | — | `4` | `open` | — | Būsena | — |
| `tipas` | `string` | — | `4` | `open` | — | Fitosanitarinio sertifikato tipas | — |
| `salis_gaveja` | `string` | — | `4` | `open` | — | Šalis gavėja | — |
| `kpn_kodas` | `string` | — | `4` | `open` | — | Produkcijos KPN kodas | — |
| `prod_kiekis` | `number` | — | `4` | `open` | — | Produkcijos kiekis (Neto) | — |
| `matavimo_vienetas` | `string` | — | `4` | `open` | — | Produkcijos kiekio matavimo vienetas | — |
| `prod_kilmes_salis` | `string` | — | `4` | `open` | — | Produkcijos kilmės šalis | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `padalinys` | `"Klaipėdos regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Vilniaus regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Klaipėdos jūrų uosto pasienio kontrolės punkto fitosanitarijos postas (skyrius)"` | — | — | — | — |
| `padalinys` | `"Panevėžio regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Kauno regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Šiaulių regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Kauno oro uosto pasienio kontrolės punkto fitosanitarijos postas (skyrius)"` | — | — | — | — |
| `padalinys` | `"Marijampolės regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Alytaus regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Tauragės regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Utenos regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Telšių regioninis skyrius"` | — | — | — | — |
| `transporto_priemone` | `"Kelių transporto priemonė"` | — | — | — | — |
| `transporto_priemone` | `"Jūrinis konteineris"` | — | — | — | — |
| `transporto_priemone` | `"Geležinkelių transportas"` | — | — | — | — |
| `transporto_priemone` | `"Laivas"` | — | — | — | — |
| `transporto_priemone` | `"Orlaivis"` | — | — | — | — |
| `transporto_priemone` | `"Siuntinys"` | — | — | — | — |
| `busena` | `"PATVIRTINTAS"` | — | — | — | — |
| `busena` | `"PANAIKINTAS"` | — | — | — | — |
| `busena` | `"PASIRASYTAS"` | — | — | — | — |
| `tipas` | `"FITOSANITARINIS_EKSPORTO_SERTIFIKATAS"` | — | — | — | — |
| `tipas` | `"FITOSANITARINIS_REEKSPORTO_SERTIFIKATAS"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r4_fitosanitarijos_ataskaitos.csv
