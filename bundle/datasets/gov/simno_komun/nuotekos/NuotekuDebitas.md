---
type: Table
title: "NuotekuDebitas — Nuotekų debitas"
description: "Alytaus rajono savivaldybės įmonės „Simno komunalininkas“ vedamoje nuotekų debitų apskaitoje fiksuojamas kiekviename valymo įrenginyje išvalytų buitinių nuotekų kiekis, skaičiuojamas kubiniais metrais per dieną."
resource: "https://get.data.gov.lt/datasets/gov/simno_komun/nuotekos/NuotekuDebitas"
tags: [gov, simno_komun, nuotekudebitas, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/nuotekos.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/simno_komun/nuotekos.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2783/"
    title: "data.gov.lt DCAT-AP — datasets/gov/simno_komun/nuotekos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# NuotekuDebitas — Nuotekų debitas

Alytaus rajono savivaldybės įmonės „Simno komunalininkas“ vedamoje nuotekų debitų apskaitoje fiksuojamas kiekviename valymo įrenginyje išvalytų buitinių nuotekų kiekis, skaičiuojamas kubiniais metrais per dieną. Duomenys nuo 2018 iki 2023 metų.[^manifest]

- **Model:** `datasets/gov/simno_komun/nuotekos/NuotekuDebitas`[^manifest]
- **Dataset:** [Nuotekų debitas](../nuotekos.md) (`datasets/gov/simno_komun/nuotekos`)[^manifest]
- **Manifest CSV:** [datasets/gov/simno_komun/nuotekos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/nuotekos.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/simno_komun/nuotekos/NuotekuDebitas` (`deployed`)[^manifest]
- **Provider:** `simno_komun` — Alytaus rajono savivaldybės įmonė „Simno komunalininkas“ *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `irenginys` | `string` | — | `4` | `open` | — | Įrenginys | — |
| `data` | `date` | `D` | `4` | `open` | — | Laikotarpis | — |
| `debitas_m3` | `number` | `m^3/d` | `4` | `open` | — | Atitekėjusių (ištekėjusių) nuotekų kiekis per dieną | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/simno_komun/nuotekos.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/nuotekos.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/simno_komun/nuotekos (https://data.gov.lt/datasets/2783/)
