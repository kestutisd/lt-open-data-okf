---
type: Table
title: "ValstybinioAuditoRezultatai — Valstybinio audito rezultatai"
description: "Valstybės kontrolės finansinių, atitikties ir veiklos auditų ataskaitų, išvadų duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vk/varezultatai/ValstybinioAuditoRezultatai"
tags: [gov, vk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vk/varezultatai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/varezultatai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# ValstybinioAuditoRezultatai — Valstybinio audito rezultatai

Valstybės kontrolės finansinių, atitikties ir veiklos auditų ataskaitų, išvadų duomenys

- **Model:** `datasets/gov/vk/varezultatai/ValstybinioAuditoRezultatai`[^manifest]
- **Dataset:** [datasets/gov/vk/varezultatai](../varezultatai.md) (`datasets/gov/vk/varezultatai`)
- **Manifest CSV:** [datasets/gov/vk/varezultatai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/varezultatai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vk/varezultatai/ValstybinioAuditoRezultatai`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `audit_cardid` | `integer` | — | `3` | `open` | — | Produkto ID | Audito identifikacijos numeris |
| `audito_pavadinimas` | `string` | — | `3` | `open` | — | Produkto pavadinimas | Audito pavadinimas |
| `audito_tipas` | `string` | — | `4` | `open` | — | Audito tipas | Audito tipas: finansinis, veiklos, atitikties auditas |
| `srities_pavadinimas` | `string` | — | `3` | `open` | — | Srities pavadinimas | Srities, kurioje suplanuotas auditas, pavadinimas |
| `registravimo_data` | `date` | `D` | `4` | `open` | — | Registracijos data | Dokumento registracijos dokumentų valdymo posistemyje data |
| `failo_url` | `url` | — | `4` | `open` | — | Nuoroda į produkto dokumentą | Audito ataskaitos dokumentas |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `audito_tipas` | `"Veiklos auditai"` | — | — | Veiklos auditai | Veiklos auditai – kai vertinama audituojamo subjekto veikla ekonomiškumo, efektyvumo ir rezultatyvumo požiūriu. |
| `audito_tipas` | `"Finasiniai auditai"` | — | — | Finasiniai auditai | Finansiniai auditai – kai vertinami audituojamo subjekto metinių (konsoliduotųjų) finansinių ir biudžeto vykdymo ataskaitų rinkinių duomenis ir pareiškiama nepriklausoma auditoriaus nuomonė. |
| `audito_tipas` | `"Atitikties auditai"` | — | — | Atitikties auditai | Atitikties auditai – kai vertinama audituojamo subjekto veiklos atitiktis teisės aktų ir (ar) kitiems reikalavimams ir gali būti pareiškiama nepriklausoma auditoriaus nuomonė. |

[^manifest]: atviriduomenys/manifest — datasets/gov/vk/varezultatai.csv
