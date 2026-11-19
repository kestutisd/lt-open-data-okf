---
type: Table
title: "Sutartis — Komunalinių atliekų tvarkymo sutartys"
description: "Informacija apie komunalinių atliekų tvarkymo sutartys"
resource: "https://get.data.gov.lt/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras/Sutartis"
tags: [gov, aaa, sutartis, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L104"
    title: "atviriduomenys/manifest — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L104"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3840/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Sutartis — Komunalinių atliekų tvarkymo sutartys

Informacija apie komunalinių atliekų tvarkymo sutartys[^manifest]

- **Model:** `datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras/Sutartis`[^manifest]
- **Dataset:** [Atliekų tvarkytojų valstybės registro duomenys](../atlieku_tvarkytoju_valstybes_registras.md) (`datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L104](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L104)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras/Sutartis` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `sutarties_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sutarties_id` | `string` | — | `4` | `open` | — | Sutarties identifikatorius | — |
| `sutarties_numeris` | `string` | — | `4` | `open` | — | Sutarties numeris | — |
| `sutartis_galioja_nuo` | `date` | `D` | `4` | `open` | — | Sutarties galiojimo pradžia | — |
| `sutartis_galioja_iki` | `date` | `D` | `4` | `open` | — | Sutarties galiojimo pabaiga | — |
| `sutarties_tipo_pavadinimas` | `string` | — | `4` | `open` | — | Sutarties tipo pavadinimas | — |
| `sutarties_objektas` | `string` | — | `4` | `open` | — | Sutarties objektas | — |
| `atlieku_tvarkymo_veiklos` | `string` | — | `4` | `open` | — | Komunalinėje sutartyje nurodytos atliekų tvarkymo veiklos (-ų) pavadinimas | — |
| `atlieku_pavadinimas` | `string` | — | `4` | `open` | — | Komunalinėje sutartyje nurodytų atliekų pavadinimas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Komunalinės sutarties savivaldybės | — |
| `atlieku_tvarkytojo_tipas` | `string` | — | `4` | `open` | — | Atliekų tvarkytojo tipas | — |
| `atlieku_tvarkytojo_pavadinimas` | `string` | — | `4` | `open` | — | Atliekų tvarkytojo pavadinimas | — |
| `tvarkytojo_juridinio_asmens_kodas` | `string` | — | `4` | `open` | — | Atliekų tvarkytojo juridinio asmens kodas | — |
| `atlieku_tvarkytojo_adresas` | `string` | — | `4` | `open` | — | Atliekų tvarkytojo adresas | — |
| `subjekto_tipas` | `string` | — | `4` | `open` | — | Komunalinės sutarties šalies (Komunalinių atliekų tvarkymo sistemos administratoriaus) subjekto tipas | — |
| `subjekto_juridinio_asmens_kodas` | `string` | — | `4` | `open` | — | Komunalinės sutarties šalies (Komunalinių atliekų tvarkymo sistemos administratoriaus) subjekto juridinio asmens kodas | — |
| `subjekto_pavadinimas` | `string` | — | `4` | `open` | — | Komunalinės sutarties šalies (Komunalinių atliekų tvarkymo sistemos administratoriaus) subjekto pavadinimas | — |
| `subjekto_adresas` | `string` | — | `4` | `open` | — | Komunalinės sutarties šalies(Komunalinių atliekų tvarkymo sistemos administratoriaus) subjekto adresas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `sutarties_tipo_pavadinimas` | `"Komunalinė sutartis"` | — | — | — | — |
| `atlieku_tvarkytojo_tipas` | `"JA"` | — | — | Juridinis asmuo | — |
| `atlieku_tvarkytojo_tipas` | `"FA"` | — | — | Fizinis asmuo | — |
| `atlieku_tvarkytojo_tipas` | `"UZ"` | — | — | Užsienio šalies pilietis | — |
| `subjekto_tipas` | `"JA"` | — | — | Juridinis asmuo | — |
| `subjekto_tipas` | `"FA"` | — | — | Fizinis asmuo | — |
| `subjekto_tipas` | `"UZ"` | — | — | Užsienio šalies pilietis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L104 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L104)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras (https://data.gov.lt/datasets/3840/)
