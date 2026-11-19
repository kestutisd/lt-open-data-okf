---
type: Table
title: "Imone — Kauno m. sav. Elektronine paslaugų sistema besinaudojančios įmonės"
description: "Kauno miesto savivaldybės valdoma Elektroninių paslaugų sistema (EPS) saugo Kauno m. sav."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/eps/Imone"
tags: [gov, kauno_m_sav, imone, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/eps.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/eps.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2741/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/eps"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Imone — Kauno m. sav. Elektronine paslaugų sistema besinaudojančios įmonės

Kauno miesto savivaldybės valdoma Elektroninių paslaugų sistema (EPS) saugo Kauno m. sav. administracijos teikiamų elektroninių paslaugų duomenis. Duomenys renkami nuo 2017 m., ir yra atnaujinami kasdien. Duomenų rinkyje saugomi EPS besinaudojančių įmonių duomenys: JAR kodas, pavadinimas, buveinės adresas ir teisinė forma.[^manifest]

- **Model:** `datasets/gov/kauno_m_sav/eps/Imone`[^manifest]
- **Dataset:** [Kauno m. sav. Elektronine paslaugų sistema besinaudojančios įmonės](../eps.md) (`datasets/gov/kauno_m_sav/eps`)[^manifest]
- **Manifest CSV:** [datasets/gov/kauno_m_sav/eps.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/eps.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/eps/Imone` (`deployed`)[^manifest]
- **Provider:** `kauno_m_sav` — Kauno miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `jar_kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `jar_kodas` | `string` | — | `4` | `open` | — | Įmonės juridinių asmenų registro kodas | — |
| `ja_pavadinimas` | `string` | — | `4` | `open` | — | Įmonės pavadinimas | — |
| `ja_adresas` | `string` | — | `4` | `open` | — | Įmonės buveinės adresas | — |
| `ja_teisine_forma` | `string` | — | `4` | `open` | — | Įmonės teisinė forma | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/eps.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/eps.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/eps (https://data.gov.lt/datasets/2741/)
