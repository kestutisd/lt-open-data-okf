---
type: Table
title: "Bustas — Klaipėdos miesto savivaldybės nuomojamų būstų registras"
description: "Rinkinys apie savivaldybės ir socialinio būsto nuomą Klaipėdos miesto savivaldybėje, kuriame pateikiama informacija apie būstų charakteristikas, nuomos sąlygas ir nuomininkus."
resource: "https://get.data.gov.lt/datasets/gov/kbu/Bustas"
tags: [gov, kbu, bustas, deployed, level-4, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kbu/bustai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/kbu/bustai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3831/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kbu"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Bustas — Klaipėdos miesto savivaldybės nuomojamų būstų registras

Rinkinys apie savivaldybės ir socialinio būsto nuomą Klaipėdos miesto savivaldybėje, kuriame pateikiama informacija apie būstų charakteristikas, nuomos sąlygas ir nuomininkus. Kiekvienos lentelės viena eilutė atitinką vieną sudarytą nuomos sutartį Klaipėdos miesto savivaldybėje. Duomenų teikėjas: VšĮ Klaipėdos butai. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/kbu/Bustas`[^manifest]
- **Dataset:** [VšĮ Klaipėdos būstai](../kbu.md) (`datasets/gov/kbu`)[^manifest]
- **Manifest CSV:** [datasets/gov/kbu/bustai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kbu/bustai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kbu/Bustas` (`deployed`)[^manifest]
- **Provider:** `kbu` — VšĮ Klaipėdos būstai *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_2`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/kbu/bustai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kbu/bustai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kbu (https://data.gov.lt/datasets/3831/)
