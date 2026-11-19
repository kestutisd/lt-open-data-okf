---
type: Table
title: "VienosKlasifikacija — Prekių ženklų Vienos klasifikacijos"
description: "Lentelė „Prekių ženklų Vienos klasifikacijos“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/pzr/VienosKlasifikacija"
tags: [gov, vpb, vienosklasifikacija, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/pzr.csv#L41"
    title: "atviriduomenys/manifest — datasets/gov/vpb/pzr.csv#L41"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3809/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpb/pzr"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# VienosKlasifikacija — Prekių ženklų Vienos klasifikacijos

Lentelė „Prekių ženklų Vienos klasifikacijos“. Lentelę sudaro: prekės ženklo registracijos ir paraiškos numeriai, Vienos klasifikacijos sekcija ir jos semantinis apibūdinimas. Vienas įrašas atitinka vieną unikalią prekės ženklo registracijos, paraiškos numerių ir Vienos klasifikacijos sekcijos kombinaciją.[^manifest]

- **Model:** `datasets/gov/vpb/pzr/VienosKlasifikacija`[^manifest]
- **Dataset:** [Lietuvos Respublikos prekių ženklai](../pzr.md) (`datasets/gov/vpb/pzr`)[^manifest]
- **Manifest CSV:** [datasets/gov/vpb/pzr.csv#L41](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/pzr.csv#L41)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/pzr/VienosKlasifikacija` (`deployed`)[^manifest]
- **Provider:** `vpb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `registracijos_nr` | `string` | — | `4` | `open` | — | Prekės ženklo bylos registracijos numeris | — |
| `paraiskos_nr` | `string` | — | `4` | `open` | — | Prekės ženklo bylos paraiškos numeris | — |
| `sekcija` | `string` | — | `4` | `open` | — | Vienos klasifikacijos sekcija | — |
| `aprasymas` | `string` | — | `4` | `open` | — | Vienos klasifikacijos sekcijos aprašymas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/pzr.csv#L41 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/pzr.csv#L41)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpb/pzr (https://data.gov.lt/datasets/3809/)
