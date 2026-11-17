---
type: Table
title: "JuruLaivas — Jūrų laivai"
description: "Spinta table datasets/gov/ltsa/juru_laivai/JuruLaivas (27 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/juru_laivai/JuruLaivas"
tags: [gov, ltsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ltsa/juru_laivai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/juru_laivai.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# JuruLaivas — Jūrų laivai

- **Model:** `datasets/gov/ltsa/juru_laivai/JuruLaivas`[^manifest]
- **Dataset:** [datasets/gov/ltsa/juru_laivai](../juru_laivai.md) (`datasets/gov/ltsa/juru_laivai`)
- **Manifest CSV:** [datasets/gov/ltsa/juru_laivai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/juru_laivai.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/juru_laivai/JuruLaivas`
- **Primary Key (`ref`):** `reg_perm_id,reg_temp_id,own_le,own_np_sys_id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `record_id` | `string` | — | `4` | `open` | — | Įrašo ID | — |
| `own_le` | `string` | — | `2` | `open` | — | Savininkas JA | Savininko juridinio asmens kodas |
| `adm_le` | `string` | — | `2` | `open` | — | Valdytojas JA | Valdytojo juridinio asmens kodas |
| `own_np_sys_id` | `integer` | — | `2` | `open` | — | Savininkas FA | Savininko fizinio asmens ID |
| `reg_perm_expired` | `datetime` | `T` | `4` | `open` | — | Registracija panaikinta | — |
| `reg_perm_from` | `datetime` | `T` | `4` | `open` | — | Registracija galioja nuo | — |
| `reg_perm_id` | `integer` | — | `4` | `open` | — | Registracijos ID | — |
| `reg_perm_no` | `string` | — | `4` | `open` | — | Registracijos numeris | — |
| `reg_perm_to` | `datetime` | `T` | `4` | `open` | — | Registracija galioja iki | — |
| `reg_perm_unreg` | `datetime` | `T` | `4` | `open` | — | Išregistravimas | — |
| `ship_constructed` | `datetime` | `T` | `4` | `open` | — | Laivo pastatymo metai | — |
| `ship_call_sign` | `string` | — | `4` | `open` | — | Laivo šaukiniai | — |
| `ship_dw` | `number` | `t` | `4` | `open` | — | Laivo dedveito tonažas | — |
| `ship_gross_tg` | `number` | `m^3` | `4` | `open` | — | Laivo bendroji talpa | — |
| `ship_id` | `integer` | — | `4` | `open` | — | Laivo ID | — |
| `ship_imo` | `integer` | — | `4` | `open` | — | Laivo IMO kodas | International Marytime Organization identifikacinis kodas |
| `ship_length` | `number` | `m` | `4` | `open` | — | Laivo gabaritinis ilgis | — |
| `ship_max_drght` | `number` | `m` | `4` | `open` | — | Laivo grimzlė | — |
| `ship_name` | `string` | — | `4` | `open` | — | Laivo pavadinimas | — |
| `ship_net_tg` | `number` | `m^3` | `4` | `open` | — | Laivo grynoji talpa | — |
| `ship_recon` | `datetime` | `T` | `4` | `open` | — | Laivo rekonstrukcija | — |
| `ship_side_hght` | `number` | `m` | `4` | `open` | — | Laivo borto aukštis | — |
| `ship_width` | `number` | `m` | `4` | `open` | — | Laivo gabaritinis plotis | — |
| `ship_type` | `string` | — | `3` | `open` | — | Laivo tipas | — |
| `reg_temp_from` | `datetime` | `T` | `4` | `open` | — | Laikina registracija galioja nuo | — |
| `reg_temp_to` | `datetime` | `T` | `4` | `open` | — | Laikina registracija galioja iki | — |
| `reg_temp_id` | `integer` | — | `4` | `open` | — | Laikinos registracijos ID | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/juru_laivai.csv
