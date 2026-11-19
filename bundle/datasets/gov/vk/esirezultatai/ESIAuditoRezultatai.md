---
type: Table
title: "ESIAuditoRezultatai — Europos Sąjungos investicijų audito rezultatai"
description: "Valstybės kontrolės Europos Sąjungos investicijų auditų ataskaitų duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vk/esirezultatai/ESIAuditoRezultatai"
tags: [gov, vk, esiauditorezultatai, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/esirezultatai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/vk/esirezultatai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1691/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vk/esirezultatai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# ESIAuditoRezultatai — Europos Sąjungos investicijų audito rezultatai

Valstybės kontrolės Europos Sąjungos investicijų auditų ataskaitų duomenys[^manifest]

- **Model:** `datasets/gov/vk/esirezultatai/ESIAuditoRezultatai`[^manifest]
- **Dataset:** [Europos Sąjungos investicijų audito rezultatai](../esirezultatai.md) (`datasets/gov/vk/esirezultatai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vk/esirezultatai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/esirezultatai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vk/esirezultatai/ESIAuditoRezultatai` (`deployed`)[^manifest]
- **Provider:** `vk` — Valstybės kontrolė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `audit_cardid` | `integer` | — | `3` | `open` | — | Produkto ID | Europos Sąjungos investicijų audito identifikacijos numeris |
| `audito_pavadinimas` | `string` | — | `3` | `open` | — | Produkto pavadinimas | Europos Sąjungos investicijų audito pavadinimas |
| `registravimo_data` | `date` | `D` | `4` | `open` | — | Registracijos data | Dokumento registracijos dokumentų valdymo posistemyje data |
| `failo_url` | `url` | — | `4` | `open` | — | Nuoroda į produkto dokumentą | Vertinimo, išvados, ataskaitos, projekcijos dokumentas |

[^manifest]: atviriduomenys/manifest — datasets/gov/vk/esirezultatai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/esirezultatai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vk/esirezultatai (https://data.gov.lt/datasets/1691/)
