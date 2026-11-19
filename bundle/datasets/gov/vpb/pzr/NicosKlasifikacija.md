---
type: Table
title: "NicosKlasifikacija — Prekių ženklų Nicos klasifikacijos"
description: "Lentelė „Prekių ženklų Nicos klasifikacijos“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/pzr/NicosKlasifikacija"
tags: [gov, vpb, nicosklasifikacija, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/pzr.csv#L48"
    title: "atviriduomenys/manifest — datasets/gov/vpb/pzr.csv#L48"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3809/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpb/pzr"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# NicosKlasifikacija — Prekių ženklų Nicos klasifikacijos

Lentelė „Prekių ženklų Nicos klasifikacijos“. Lentelę sudaro: prekės ženklo registracijos ir paraiškos numeriai, Nicos klasifikacinis kodas ir jam priskirti terminai. Vienas įrašas atitinka vieną unikalią prekės ženklo registracijos, paraiškos numerių ir Nicos klasifikacinio kodo kombinaciją.[^manifest]

- **Model:** `datasets/gov/vpb/pzr/NicosKlasifikacija`[^manifest]
- **Dataset:** [Lietuvos Respublikos prekių ženklai](../pzr.md) (`datasets/gov/vpb/pzr`)[^manifest]
- **Manifest CSV:** [datasets/gov/vpb/pzr.csv#L48](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/pzr.csv#L48)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/pzr/NicosKlasifikacija` (`deployed`)[^manifest]
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
| `klases_kodas` | `string` | — | `4` | `open` | — | Nicos klasifikacijos klasės kodas | — |
| `klases_terminai` | `string` | — | `4` | `open` | — | Nicos klasifikacijos klasės terminai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/pzr.csv#L48 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/pzr.csv#L48)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpb/pzr (https://data.gov.lt/datasets/3809/)
