---
type: Table
title: "ESIAuditoRezultatai — Europos Sąjungos investicijų audito rezultatai"
description: "Valstybės kontrolės Europos Sąjungos investicijų auditų ataskaitų duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vk/esirezultatai/ESIAuditoRezultatai"
tags: [gov, vk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vk/esirezultatai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/esirezultatai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# ESIAuditoRezultatai — Europos Sąjungos investicijų audito rezultatai

Valstybės kontrolės Europos Sąjungos investicijų auditų ataskaitų duomenys

- **Model:** `datasets/gov/vk/esirezultatai/ESIAuditoRezultatai`[^manifest]
- **Dataset:** [datasets/gov/vk/esirezultatai](../esirezultatai.md) (`datasets/gov/vk/esirezultatai`)
- **Manifest CSV:** [datasets/gov/vk/esirezultatai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/esirezultatai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vk/esirezultatai/ESIAuditoRezultatai`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `audit_cardid` | `integer` | — | `3` | `open` | — | Produkto ID | Europos Sąjungos investicijų audito identifikacijos numeris |
| `audito_pavadinimas` | `string` | — | `3` | `open` | — | Produkto pavadinimas | Europos Sąjungos investicijų audito pavadinimas |
| `registravimo_data` | `date` | `D` | `4` | `open` | — | Registracijos data | Dokumento registracijos dokumentų valdymo posistemyje data |
| `failo_url` | `url` | — | `4` | `open` | — | Nuoroda į produkto dokumentą | Vertinimo, išvados, ataskaitos, projekcijos dokumentas |

[^manifest]: atviriduomenys/manifest — datasets/gov/vk/esirezultatai.csv
