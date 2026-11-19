---
type: Table
title: "Atvaizdas — Dizainų atvaizdai"
description: "Lentelė „Dizainų atvaizdai“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/dr/Atvaizdas"
tags: [gov, vpb, atvaizdas, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/dr.csv#L39"
    title: "atviriduomenys/manifest — datasets/gov/vpb/dr.csv#L39"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3807/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpb/dr"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Atvaizdas — Dizainų atvaizdai

Lentelė „Dizainų atvaizdai“. Lentelę sudaro: dizaino ir paraiškos numeriai ir dizaino atvaizdo pavyzdžio internetinė nuoroda. Kiekvienas dizainas gali turėti po keletą atvaizdų, o kiekvienas atvaizdas – po keletą pavyzdžių (paveikslėlių). Vienas įrašas atitinka vieną internetinę nuorodą.[^manifest]

- **Model:** `datasets/gov/vpb/dr/Atvaizdas`[^manifest]
- **Dataset:** [Lietuvos Respublikos dizainų duomenys](../dr.md) (`datasets/gov/vpb/dr`)[^manifest]
- **Manifest CSV:** [datasets/gov/vpb/dr.csv#L39](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/dr.csv#L39)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/dr/Atvaizdas` (`deployed`)[^manifest]
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
| `atvaizdo_nuoroda` | `string` | — | `4` | `open` | — | Dizaino pavyzdžių vaizdų internetinė nuoroda | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/dr.csv#L39 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/dr.csv#L39)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpb/dr (https://data.gov.lt/datasets/3807/)
