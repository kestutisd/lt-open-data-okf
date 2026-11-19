---
type: Table
title: "LokarnoKlasifikacija — Dizainų Lokarno klasifikacijos"
description: "Lentelė „Dizainų Lokarno klasifikacijos“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/dr/LokarnoKlasifikacija"
tags: [gov, vpb, lokarnoklasifikacija, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/dr.csv#L32"
    title: "atviriduomenys/manifest — datasets/gov/vpb/dr.csv#L32"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3807/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpb/dr"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# LokarnoKlasifikacija — Dizainų Lokarno klasifikacijos

Lentelė „Dizainų Lokarno klasifikacijos“. Lentelę sudaro: dizaino ir paraiškos numeriai, Lokarno klasifikacijos kodas ir jo semantinis apibūdinimas. Vienas įrašas atitinka vieną unikalią dizaino numerio ir Lokarno klasifikacijos kodo kombinaciją.[^manifest]

- **Model:** `datasets/gov/vpb/dr/LokarnoKlasifikacija`[^manifest]
- **Dataset:** [Lietuvos Respublikos dizainų duomenys](../dr.md) (`datasets/gov/vpb/dr`)[^manifest]
- **Manifest CSV:** [datasets/gov/vpb/dr.csv#L32](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/dr.csv#L32)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/dr/LokarnoKlasifikacija` (`deployed`)[^manifest]
- **Provider:** `vpb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus indentifikatorius | — |
| `registracijos_nr` | `string` | — | `4` | `open` | — | Dizaino bylos registracijos numeris | — |
| `paraiskos_nr` | `string` | — | `4` | `open` | — | Dizaino bylos paraiškos numeris | — |
| `lokarno_klasifikacija` | `string` | — | `4` | `open` | — | Lokarno klasifikacijos kodas | — |
| `klasifikacijos_apibudinimas` | `string` | — | `4` | `open` | — | Lokarno klasifikacijos kodo apibūdinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/dr.csv#L32 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/dr.csv#L32)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpb/dr (https://data.gov.lt/datasets/3807/)
