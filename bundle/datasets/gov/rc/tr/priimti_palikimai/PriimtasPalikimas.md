---
type: Table
title: "PriimtasPalikimas"
description: "Spinta table datasets/gov/rc/tr/priimti_palikimai/PriimtasPalikimas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/tr/priimti_palikimai/PriimtasPalikimas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/tr/priimti_testamentai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/priimti_testamentai.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# PriimtasPalikimas

- **Model:** `datasets/gov/rc/tr/priimti_palikimai/PriimtasPalikimas`[^manifest]
- **Dataset:** [Testamentų registro (TR) duomenys apie priimtą palikimą](../priimti_palikimai.md) (`datasets/gov/rc/tr/priimti_palikimai`)
- **Manifest CSV:** [datasets/gov/rc/tr/priimti_testamentai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/priimti_testamentai.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/tr/priimti_palikimai/PriimtasPalikimas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Objekto identifikavimo kodas šiame duomenų rinkinyje | — |
| `reg_data` | `string` | — | `3` | `open` | — | Įregistravimo laikotarpis (metai - ketvirtis) | — |
| `teikejas` | `string` | — | `3` | `open` | — | Duomenų teikėjas | — |
| `palikejo_lytis` | `string` | — | `4` | `open` | — | Palikėjo lytis | — |
| `uzsienietis` | `integer` | — | `4` | `open` | — | Požymis ar užsienietis | — |
| `palikejo_amzius` | `string` | — | `3` | `open` | — | Palikėjo amžiaus grupė | — |
| `ipedinio_lytis` | `string` | — | `4` | `open` | — | Įpėdinio lytis | — |
| `ipedinio_amzius` | `string` | — | `3` | `open` | — | Įpėdinio amžiaus grupė, kai įpėdinis fizinis asmuo | — |
| `poz_ar_iped_ja` | `integer` | — | `4` | `open` | — | Požymis ar įpėdinis Juridinis asmuo | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `palikejo_lytis` | `"V"` | — | — | Vyras | — |
| `palikejo_lytis` | `"M"` | — | — | Moteris | — |
| `palikejo_lytis` | `"ND"` | — | — | Nėra duomenų | — |
| `uzsienietis` | `1` | — | — | Užsienietis | — |
| `uzsienietis` | `0` | — | — | Lietuvos Respublikos pilietis | — |
| `ipedinio_lytis` | `"V"` | — | — | Vyras | — |
| `ipedinio_lytis` | `"M"` | — | — | Moteris | — |
| `ipedinio_lytis` | `"ND"` | — | — | Nėra duomenų | — |
| `poz_ar_iped_ja` | `1` | — | — | Juridinis asmuo | — |
| `poz_ar_iped_ja` | `0` | — | — | Fizinis asmuo | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/tr/priimti_testamentai.csv
