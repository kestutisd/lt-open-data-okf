---
type: Table
title: "Rekomendacija — Valstybinio audito rekomendacijų įgyvendinimas"
description: "Valstybės kontrolės atliktų valstybinių auditų rekomendacijų įgyvendinimo rezultatai"
resource: "https://get.data.gov.lt/datasets/gov/vk/rekomendacijos/Rekomendacija"
tags: [gov, vk, rekomendacija, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/rekomendacijos.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/vk/rekomendacijos.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1696/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vk/rekomendacijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Rekomendacija — Valstybinio audito rekomendacijų įgyvendinimas

Valstybės kontrolės atliktų valstybinių auditų rekomendacijų įgyvendinimo rezultatai[^manifest]

- **Model:** `datasets/gov/vk/rekomendacijos/Rekomendacija`[^manifest]
- **Dataset:** [Valstybinio audito rekomendacijų įgyvendinimas](../rekomendacijos.md) (`datasets/gov/vk/rekomendacijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vk/rekomendacijos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/rekomendacijos.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vk/rekomendacijos/Rekomendacija` (`deployed`)[^manifest]
- **Provider:** `vk` — Valstybės kontrolė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `rekomendacijosid` | `integer` | — | `3` | `open` | — | Rekomendacijos ID | Rekomendacijos kodas |
| `audit_cardid` | `integer` | — | `3` | `open` | — | Audito ID | Audito kodas |
| `turinys` | `string` | — | `3` | `open` | — | Turinys | Rekomendacijos turinys |
| `sritis` | `string` | — | `3` | `open` | — | Sritis | Srities, kurioje atliktas auditas, pavadinimas |
| `subjekto_kodas` | `string` | — | `4` | `open` | — | Subjekto kodas | Subjekto, kuris įgyvendina rekomendaciją, kodas |
| `subjekto_pavadinimas` | `string` | — | `4` | `open` | — | Subjekto pavadinimas | Subjekto, kuris įgyvendina rekomendaciją, pavadinimas |
| `igyvendinimo_data` | `date` | `D` | `4` | `open` | — | įgyvendinimo data | Rekomendacijos įgyvendinimo data |
| `bukle` | `string` | — | `3` | `open` | — | įgyvendinimo būklė | Rekomendacijos įgyvendinimo būklė |
| `laiko_bukle` | `string` | — | `3` | `open` | — | Laiko būklė | Rekomendacijos įgyvendinimo laiko būklė |
| `rezultatu_aprasymas` | `string` | — | `3` | `open` | — | Rezultatų aprašymas | Rekomendacijos įgyvendinimo rezultatų aprašymas |
| `stebesena_baigta` | `boolean` | — | `3` | `open` | — | Stebėsena baigta | Rekomendacijos stebėsenos pabaigos požymis |
| `pateikimo_forma` | `string` | — | `3` | `open` | — | Pateikimo forma | Rekomendacijos pateikimo forma |

[^manifest]: atviriduomenys/manifest — datasets/gov/vk/rekomendacijos.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/rekomendacijos.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vk/rekomendacijos (https://data.gov.lt/datasets/1696/)
