---
type: Table
title: "ChlorofilasA — Kuršių marių ir Baltijos jūros chlorofilo a tyrimų duomenys"
description: "Spinta table datasets/gov/aaa/juros_mariu_monitoringas/ChlorofilasA (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/juros_mariu_monitoringas/ChlorofilasA"
tags: [gov, aaa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/juros_mariu_monitoringas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_monitoringas.csv#L44"
    last_modified: "2026-11-11T14:39:20Z"
---

# ChlorofilasA — Kuršių marių ir Baltijos jūros chlorofilo a tyrimų duomenys

- **Model:** `datasets/gov/aaa/juros_mariu_monitoringas/ChlorofilasA`[^manifest]
- **Dataset:** [datasets/gov/aaa/juros_mariu_monitoringas](../juros_mariu_monitoringas.md) (`datasets/gov/aaa/juros_mariu_monitoringas`)
- **Manifest CSV:** [datasets/gov/aaa/juros_mariu_monitoringas.csv#L44](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_monitoringas.csv#L44)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/juros_mariu_monitoringas/ChlorofilasA`
- **Primary Key (`ref`):** `reg_nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `reg_nr` | `string` | — | `4` | `open` | — | Tyrimo registracijos numeris | Registracijos nr. unikalus |
| `data` | `datetime` | `D` | `4` | `open` | — | Mėginio paėmimo data | — |
| `telkinio_pav` | `string` | — | `3` | `open` | — | Vandens telkinio pavadinimas | — |
| `m_vietos_kodas` | `string` | — | `3` | `open` | — | Monitoringo vietos kodas | — |
| `m_vietos_pav` | `string` | — | `3` | `open` | — | Monitoringo vietos pavadinimas | — |
| `m_koordinate` | `geometry(point, 3346)` | — | `3` | `open` | — | Monitoringo vietos koordinatės (LKS-94) | — |
| `tyrim_objektas` | `string` | — | `3` | `open` | — | Tyrimų objektas | — |
| `horizontas` | `string` | — | `3` | `open` | — | Vandens sluoksnis, iš kurio paimtas mėginys | — |
| `gylis_nuo` | `string` | — | `2` | `open` | — | Gylis, iš/nuo kurio paimtas mėginys, metrais | Vandens gylio nuo, m ir vandens gylio iki, m eilutės nurodo, kad mėginys buvo imtas integruotu būdu. Šiuo atveju vandens horizontas įgauna reikšmę "Integruotas". Vandens gylio nuo, m reikšmė visada = 0. |
| `gylis_iki` | `number` | `m` | `4` | `open` | — | Gylis, iki kurio paimtas mėginys, metrais | Vandens gylio nuo, m ir vandens gylio iki, m eilutės nurodo, kad mėginys buvo imtas integruotu būdu. Šiuo atveju vandens horizontas įgauna reikšmę "Integruotas". Vandens gylio iki, m reikšmė = -10. |
| `parametro_pav` | `string` | — | `3` | `open` | — | Tiriamo parametro pavadinimas | — |
| `rezultatas` | `number` | — | `4` | `open` | — | Parametro tyrimo rezultatas | — |
| `matavimo_vnt` | `string` | — | `4` | `open` | — | Matavimo vienetai | — |
| `tyr_metodas` | `string` | — | `3` | `open` | — | Tyrimų metodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/juros_mariu_monitoringas.csv
