---
type: Table
title: "PAHSpecReceptas — PAH specifiniam gydymui skiriamų vaistų receptai"
description: "\"PAH specifiniam gydymui skiriamų vaistų (ambrisentanas, bozentanas, iloprostas, sildenafilis, treprostinilis, macitentanas, seleksipagas) pirmo ir paskutinio galiojančio recepto išrašymo datos (su triukšmu iki 5 dienų), vaisto ATC kodas, bendrinis pavadinimas.\""
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/pah_diagnozes/PAHSpecReceptas"
tags: [gov, lsd, pahspecreceptas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/pah_diagnozes.csv#L31"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/pah_diagnozes.csv#L31"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3888/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/pah_diagnozes"
    author: "team:vda"
    last_modified: "2026-05-06T00:00:00Z"
---

# PAHSpecReceptas — PAH specifiniam gydymui skiriamų vaistų receptai

"PAH specifiniam gydymui skiriamų vaistų (ambrisentanas, bozentanas, iloprostas, sildenafilis, treprostinilis, macitentanas, seleksipagas) pirmo ir paskutinio galiojančio recepto išrašymo datos (su triukšmu iki 5 dienų), vaisto ATC kodas, bendrinis pavadinimas."[^manifest]

- **Model:** `datasets/gov/lsd/sveikata/pah_diagnozes/PAHSpecReceptas`[^manifest]
- **Dataset:** ["Pacientų, sergančių plaučių arterine hipertenzija, gydymo duomenys"](../pah_diagnozes.md) (`datasets/gov/lsd/sveikata/pah_diagnozes`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/pah_diagnozes.csv#L31](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/pah_diagnozes.csv#L31)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/pah_diagnozes/PAHSpecReceptas` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-05-06`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalios eilutės identifikatorius | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Asmens kodas | — |
| `vaisto_atc_kodas` | `string` | — | `4` | `open` | — | Vaisto ATC kodas | — |
| `vaisto_atc_pav` | `string` | — | `4` | `open` | — | Vaisto ATC pavadinimas | — |
| `first_prescription` | `date` | `D` | `4` | `open` | — | Pirmo recepto išrašymo data | "Pirmo recepto išrašymo data, su triukšmu iki 5 d." |
| `last_prescription` | `date` | `D` | `4` | `open` | — | Paskutinio recepto išrašymo data | "Paskutinio recepto išrašymo data, su triukšmu iki 5 d." |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/pah_diagnozes.csv#L31 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/pah_diagnozes.csv#L31)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/pah_diagnozes (https://data.gov.lt/datasets/3888/)
