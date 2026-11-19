---
type: Table
title: "InkstoTransplantacija — Inkstų transplantacijų duomenys"
description: "Pacientams atliktų inkstų transplantacijų (intervencijos ACHI kodas 36503-00) datos (mėnesio tikslumu)"
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/inkstu_biopsijos/InkstoTransplantacija"
tags: [gov, lsd, inkstotransplantacija, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L58"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L58"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4573/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/inkstu_biopsijos"
    author: "team:vda"
    last_modified: "2026-03-17T00:00:00Z"
---

# InkstoTransplantacija — Inkstų transplantacijų duomenys

Pacientams atliktų inkstų transplantacijų (intervencijos ACHI kodas 36503-00) datos (mėnesio tikslumu)[^manifest]

- **Model:** `datasets/gov/lsd/sveikata/inkstu_biopsijos/InkstoTransplantacija`[^manifest]
- **Dataset:** ["Pacientų, kuriems atlikta inkstų biopsija, duomenys"](../inkstu_biopsijos.md) (`datasets/gov/lsd/sveikata/inkstu_biopsijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L58](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L58)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/inkstu_biopsijos/InkstoTransplantacija` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-03-17`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalios eilutės identifikatorius | "Valstybės duomenų agentūros sugeneruotas unikalios eilutės identifikatorius, kuri sudaro stulpeliai - asmens_kodas, transpl_data" |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Asmens kodas | — |
| `transpl_eiles_nr` | `integer` | — | `4` | `open` | — | Transplantacijos eilės numeris | "Rodiklis, nurodantis, kelintą kartą atlikta transplantacija" |
| `transpl_data` | `date` | `M` | `4` | `open` | — | Transplantacijos atlikimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L58 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L58)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/inkstu_biopsijos (https://data.gov.lt/datasets/4573/)
