---
type: Table
title: "Bustas — Klaipėdos miesto savivaldybės nuomojamų būstų registras"
description: "Rinkinys apie savivaldybės ir socialinio būsto nuomą Klaipėdos miesto savivaldybėje, kuriame pateikiama informacija apie būstų charakteristikas, nuomos sąlygas ir nuomininkus."
resource: "https://get.data.gov.lt/datasets/gov/kbu/Bustas"
tags: [gov, kbu, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kbu/bustai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kbu/bustai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Bustas — Klaipėdos miesto savivaldybės nuomojamų būstų registras

Rinkinys apie savivaldybės ir socialinio būsto nuomą Klaipėdos miesto savivaldybėje, kuriame pateikiama informacija apie būstų charakteristikas, nuomos sąlygas ir nuomininkus. Kiekvienos lentelės viena eilutė atitinką vieną sudarytą nuomos sutartį Klaipėdos miesto savivaldybėje. Duomenų teikėjas: VšĮ Klaipėdos butai.

- **Model:** `datasets/gov/kbu/Bustas`[^manifest]
- **Dataset:** [VšĮ Klaipėdos būstai](../kbu.md) (`datasets/gov/kbu`)
- **Manifest CSV:** [datasets/gov/kbu/bustai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kbu/bustai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kbu/Bustas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `ntr_kodas` | `string` | — | `4` | `open` | — | NT registro kodas | — |
| `busto_tipas` | `string` | — | `4` | `open` | — | Būsto tipas | — |
| `busto_busena` | `string` | — | `4` | `open` | — | Būsto užimtumas | — |
| `busto_plotas` | `number` | — | `4` | `open` | — | Būsto plotas | — |
| `kambariu_skaicius` | `integer` | — | `4` | `open` | — | Kambarių skaičius | — |
| `men_nuomos_suma` | `number` | — | `4` | `open` | — | Mėnesio įmokos suma | — |
| `sutarties_data` | `date` | `D` | `4` | `open` | — | Nuomos sutarties sudarymo data | — |
| `nuoma_nuo` | `date` | `D` | `4` | `open` | — | Nuomos sutarties pradžios data | — |
| `nuoma_iki` | `date` | `D` | `4` | `open` | — | Nuomos sutarties pabaigos data | — |
| `vardas_pavarde` | `string` | — | `4` | `open` | — | Vardas ir pavardė | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Asmens kodas | — |
| `ak_validacija` | `string` | — | `4` | `open` | — | Asmens kodo validacija | — |
| `gimimo_desimtmetis` | `integer` | — | `4` | `open` | — | Asmens gimimo metai, suapvalinti į dešimtmetį | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `busto_adresas` | `string` | — | `4` | `open` | — | Būsto adresas | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Platumos koordinatė WGS84 koordinačių sistemoje | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Ilgumos koordinatė WGS84 koordinačių sistemoje | — |
| `geometrija` | `string` | — | `4` | `open` | — | Geometrija | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kbu/bustai.csv
