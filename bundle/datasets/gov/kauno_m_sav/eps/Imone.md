---
type: Table
title: "Imone — Kauno m. sav. Elektronine paslaugų sistema besinaudojančios įmonės"
description: "Kauno miesto savivaldybės valdoma Elektroninių paslaugų sistema (EPS) saugo Kauno m."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/eps/Imone"
tags: [gov, kauno_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/eps.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/eps.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Imone — Kauno m. sav. Elektronine paslaugų sistema besinaudojančios įmonės

Kauno miesto savivaldybės valdoma Elektroninių paslaugų sistema (EPS) saugo Kauno m. sav. administracijos teikiamų elektroninių paslaugų duomenis. Duomenys renkami nuo 2017 m., ir yra atnaujinami kasdien. Duomenų rinkyje saugomi EPS besinaudojančių įmonių duomenys: JAR kodas, pavadinimas, buveinės adresas ir teisinė forma.

- **Model:** `datasets/gov/kauno_m_sav/eps/Imone`[^manifest]
- **Dataset:** [Kauno m. sav. Elektronine paslaugų sistema besinaudojančios įmonės](../eps.md) (`datasets/gov/kauno_m_sav/eps`)
- **Manifest CSV:** [datasets/gov/kauno_m_sav/eps.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/eps.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/eps/Imone`
- **Primary Key (`ref`):** `jar_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `jar_kodas` | `string` | — | `4` | `open` | — | Įmonės juridinių asmenų registro kodas | — |
| `ja_pavadinimas` | `string` | — | `4` | `open` | — | Įmonės pavadinimas | — |
| `ja_adresas` | `string` | — | `4` | `open` | — | Įmonės buveinės adresas | — |
| `ja_teisine_forma` | `string` | — | `4` | `open` | — | Įmonės teisinė forma | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/eps.csv
