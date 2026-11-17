---
type: Table
title: "BilietuPardavimas — VšĮ Žaliojo regiono elektroninių bilietų pardavimų duomenys"
description: "Lentelėje pateikti elektroninio bilieto sistemos duomenys apie elektroninių bilietų pardavimus nuo 2023 metų, teikiami VšĮ Žaliojo regiono apie Jurbarko, Šilalės, Tauragės rajonus ir Pagėgius."
resource: "https://get.data.gov.lt/datasets/gov/zr/elektroninio_bilieto_sistema/BilietuPardavimas"
tags: [gov, zr, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zr/elektroninio_bilieto_sistema.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zr/elektroninio_bilieto_sistema.csv#L27"
    last_modified: "2026-11-11T14:39:20Z"
---

# BilietuPardavimas — VšĮ Žaliojo regiono elektroninių bilietų pardavimų duomenys

Lentelėje pateikti elektroninio bilieto sistemos duomenys apie elektroninių bilietų pardavimus nuo 2023 metų, teikiami VšĮ Žaliojo regiono apie Jurbarko, Šilalės, Tauragės rajonus ir Pagėgius. Informacija atnaujinama kas mėnesį.

- **Model:** `datasets/gov/zr/elektroninio_bilieto_sistema/BilietuPardavimas`[^manifest]
- **Dataset:** [VšĮ Žaliojo Regiono elektroninių bilietų pardavimai](../elektroninio_bilieto_sistema.md) (`datasets/gov/zr/elektroninio_bilieto_sistema`)
- **Manifest CSV:** [datasets/gov/zr/elektroninio_bilieto_sistema.csv#L27](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zr/elektroninio_bilieto_sistema.csv#L27)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/zr/elektroninio_bilieto_sistema/BilietuPardavimas`
- **Primary Key (`ref`):** `bilieto_id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `bilieto_id` | `string` | — | `4` | `open` | — | Kortelės bilieto pirminis raktas | — |
| `bilietas` | `string` | — | `4` | `open` | — | Bilieto tipas | — |
| `panaudotas` | `string` | — | `4` | `open` | — | Žyma, nurodanti, ar bilietas yra išnaudotas | — |
| `kaina` | `number` | — | `4` | `open` | — | Bilieto kaina | — |
| `pilna_kaina` | `number` | — | `4` | `open` | — | Bilieto pilna kaina | — |
| `bilietu_kiekis` | `number` | — | `4` | `open` | — | Bilietų kiekis | — |
| `korteles_id` | `string` | — | `4` | `open` | — | Kortelės išorinis raktas | — |
| `bilieto_pirkimo_data` | `datetime` | `L` | `4` | `open` | — | Bilieto pirkimo data | — |
| `bilieto_galiojimo_pradzia` | `datetime` | `L` | `4` | `open` | — | Bilieto galiojimo pradžia | — |
| `bilieto_pardavimo_vietove` | `string` | — | `4` | `open` | — | Bilieto pardavimo vietovė | — |
| `bilieto_pardavimo_adresas` | `string` | — | `4` | `open` | — | Bilieto pardavimo vietovės adresas | — |
| `bilieto_galiojimo_pabaiga` | `datetime` | `L` | `4` | `open` | — | Bilieto galiojimo pabaiga | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zr/elektroninio_bilieto_sistema.csv
