---
type: Table
title: "LaivoPaieska — Policijos ieškomų laivų ir orlaivių duomenys"
description: "Lentelėje pateikiami Policijos departamento prie LR vidaus reikalų ministerijos ieškomų laivų ir orlaivių duomenys iš Ieškomų transporto priemonių registro (ITPR)."
resource: "https://get.data.gov.lt/datasets/gov/pd/policijos_ieskomi_laivai_ir_orlaiviai/LaivoPaieska"
tags: [gov, pd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pd/policijos_ieskomi_laivai_ir_orlaiviai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/policijos_ieskomi_laivai_ir_orlaiviai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# LaivoPaieska — Policijos ieškomų laivų ir orlaivių duomenys

Lentelėje pateikiami Policijos departamento prie LR vidaus reikalų ministerijos ieškomų laivų ir orlaivių duomenys iš Ieškomų transporto priemonių registro (ITPR). Informacija lentelėje atnaujinama kas mėnesį.

- **Model:** `datasets/gov/pd/policijos_ieskomi_laivai_ir_orlaiviai/LaivoPaieska`[^manifest]
- **Dataset:** [Policijos ieškomų laivų ir orlaivių duomenys](../policijos_ieskomi_laivai_ir_orlaiviai.md) (`datasets/gov/pd/policijos_ieskomi_laivai_ir_orlaiviai`)
- **Manifest CSV:** [datasets/gov/pd/policijos_ieskomi_laivai_ir_orlaiviai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/policijos_ieskomi_laivai_ir_orlaiviai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pd/policijos_ieskomi_laivai_ir_orlaiviai/LaivoPaieska`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `iraso_sukurimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo (duomenų eilutės) sukūrimo data | — |
| `iraso_atnaujinimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo (duomenų eilutės) atnaujinimo data | — |
| `paieskos_statusas` | `string` | — | `4` | `open` | — | Paieškos statusas | — |
| `nacionalinis_id` | `string` | — | `4` | `open` | — | Nacionalinis identifikatorius | — |
| `obekto_tipas` | `string` | — | `4` | `open` | — | Ieškomo objekto (transporto priemonės) tipas | — |
| `laivo_kategorija` | `string` | — | `4` | `open` | — | Laivo kategorija | — |
| `laivo_korpuso_nr` | `string` | — | `4` | `open` | — | Laivo korpuso numeris | — |
| `orlaivio_kategorija` | `string` | — | `4` | `open` | — | Orlaivio kategorija | — |
| `orlaivio_id_kodas` | `string` | — | `4` | `open` | — | Orlaivio identifikacinis numeris | — |
| `paieskos_priezastis` | `string` | — | `4` | `open` | — | Paieškos priežastis | — |
| `paieska_paskelbusi_valstybe` | `string` | — | `4` | `open` | — | Paiešką paskelbusi valstybė | — |
| `praradimo_data` | `datetime` | `S` | `4` | `open` | — | Laivo arba orlaivio praradimo data | — |
| `paieskos_pradzia` | `datetime` | `S` | `4` | `open` | — | Laivo arba orlaivio paieškos pradžia | — |
| `paieskos_pabaiga` | `date` | `D` | `4` | `open` | — | Laivo arba orlaivio paieškos pabaiga | — |
| `suradimo_laikas` | `datetime` | `S` | `4` | `open` | — | Laivo arba orlaivio suradimo laikas | — |
| `nutraukimo_data` | `datetime` | `S` | `4` | `open` | — | Paieškos nutraukimo data | — |
| `nutraukimo_pagrindas_lt` | `string` | — | `4` | `open` | — | Paieškos nutraukimo pagrindas | — |
| `nutraukimo_pagrindas_kt_lt` | `string` | — | `4` | `open` | — | Kitas paieškos nutraukimo pagrindas | — |
| `archyvavimo_data` | `date` | `D` | `4` | `open` | — | Įrašo archyvavimo data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nutraukimo_pagrindas_lt` | `update(property: "nutraukimo_pagrindas_lt@lt", type: "text")` | `type` | — | — | — | — | — |
| `nutraukimo_pagrindas_kt_lt` | `update(property: "nutraukimo_pagrindas_kt_lt@lt", type: "text")` | `type` | — | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pd/policijos_ieskomi_laivai_ir_orlaiviai.csv
