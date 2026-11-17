---
type: Table
title: "Sarasas — Bibliotekų ir padalinių sąrašas"
description: "Spinta table datasets/gov/lnb/bibliotekos/Sarasas (22 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lnb/bibliotekos/Sarasas"
tags: [gov, lnb, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lnb/bibliotekos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/bibliotekos.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sarasas — Bibliotekų ir padalinių sąrašas

- **Model:** `datasets/gov/lnb/bibliotekos/Sarasas`[^manifest]
- **Dataset:** [Bibliotekų ir padalinių sąrašas](../bibliotekos.md) (`datasets/gov/lnb/bibliotekos`)
- **Manifest CSV:** [datasets/gov/lnb/bibliotekos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/bibliotekos.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lnb/bibliotekos/Sarasas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `bibliotekos_id` | `string` | — | `4` | `open` | — | Bibliotekos identifikatorius | — |
| `padalinio_id` | `string` | — | `4` | `open` | — | Bibliotekos padalinio (fondo / filialo ar skyriaus) identifikatorius | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Bibliotekos pavadinimas | — |
| `biblioteka_aktyvi` | `string` | — | `4` | `open` | — | Bibliotekos aktyvumo statusas | — |
| `padalin_pavadinimas` | `string` | — | `4` | `open` | — | Bibliotekos padalinio pavadinimas | — |
| `padalin_aktyvus` | `boolean` | — | `4` | `open` | — | Bibliotekos padalinio aktyvumo statusas | — |
| `soc_tinklai` | `string` | — | `4` | `open` | — | Bibliotekos socialinių tinklų nuoroda | — |
| `url` | `string` | — | `4` | `open` | — | Bibliotekos internetinė svetainė | — |
| `ar_edukacine` | `boolean` | — | `4` | `open` | — | Edukacinės institucijos požymis | — |
| `ar_biblioteka` | `boolean` | — | `4` | `open` | — | Bibliotekos požymis | — |
| `ar_leidejas` | `boolean` | — | `4` | `open` | — | Leidėjo požymis | — |
| `ar_skaitytojas` | `boolean` | — | `4` | `open` | — | Skaitytojo statuso požymis | — |
| `ar_duom_teikejas` | `boolean` | — | `4` | `open` | — | Duomenų teikėjo požymis | — |
| `ar_tba` | `boolean` | — | `4` | `open` | — | Tarpbibliotekinio abonemento požymis | — |
| `uzsak_atsiemimo_d` | `integer` | — | `4` | `open` | — | Dienų skaičius, per kurias galima atsiimti užsakymą | — |
| `padalin_priima_tba` | `boolean` | — | `4` | `open` | — | Požymis, ar padalinys priima užsakymus tarpbibliotekiniu abonementu | — |
| `padalin_siuncia_tba` | `boolean` | — | `4` | `open` | — | Požymis, ar padalinys siunčia užsakymus tarpbibliotekiniu abonementu | — |
| `sukurta` | `date` | `D` | `4` | `open` | — | Informacijos apie įstaigą pateikimo data | — |
| `atnaujinta` | `date` | `D` | `4` | `open` | — | Informacijos apie įstaigą atnaujinimo data | — |
| `adresas` | `string` | — | `4` | `open` | — | Padalinio adresas | — |
| `koord` | `geometry(3346)` | `m` | `4` | `open` | — | Padalinio koordinatės | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `biblioteka_aktyvi` | `"ACTIVE"` | — | — | Aktyvi | — |
| `biblioteka_aktyvi` | `"CLOSED"` | — | — | Neaktyvi | — |
| `biblioteka_aktyvi` | `"SUSPENDED"` | — | — | Suspenduota | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lnb/bibliotekos.csv
