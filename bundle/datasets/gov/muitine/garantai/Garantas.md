---
type: Table
title: "Garantas — Informacija apie muitinės garantus"
description: "Informacija apie muitinės garanto statusą turinčias banko įstaigas ar draudimo bendroves"
resource: "https://get.data.gov.lt/datasets/gov/muitine/garantai/Garantas"
tags: [gov, muitine, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/garantai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/garantai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Garantas — Informacija apie muitinės garantus

Informacija apie muitinės garanto statusą turinčias banko įstaigas ar draudimo bendroves

- **Model:** `datasets/gov/muitine/garantai/Garantas`[^manifest]
- **Dataset:** [Informacija apie muitinės garantus](../garantai.md) (`datasets/gov/muitine/garantai`)
- **Manifest CSV:** [datasets/gov/muitine/garantai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/garantai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/garantai/Garantas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Garanto identifikatorius | — |
| `garanto_pavadinimas` | `string` | — | `4` | `open` | — | Garanto pavadinimas | — |
| `garanto_identifikacinis_numeris` | `string` | — | `4` | `open` | — | Garanto identifikacinis numeris (GIN) | — |
| `garanto_identifikatorius_mpr` | `string` | — | `4` | `open` | — | Garanto identifikatorius muitinės prievolininkų registre (MPR) | — |
| `garanto_statusas` | `string` | — | `4` | `open` | — | Garanto statusas | — |
| `garanto_statuso_suteikimo_data` | `date` | `D` | `4` | `open` | — | Garanto statuso suteikimo data | — |
| `garanto_adresas` | `string` | — | `4` | `open` | — | Garanto adresas | — |
| `garanto_miestas` | `string` | — | `4` | `open` | — | Garanto miestas | — |
| `garanto_pasto_kodas` | `string` | — | `4` | `open` | — | Garanto pašto kodas | — |
| `garanto_el_pasto_adresas` | `string` | — | `4` | `open` | — | Garanto ar jo kontaktinio asmens elektroninio pašto adresas | — |
| `lakstu_formos_garantija` | `boolean` | — | `4` | `open` | — | Požymis, ar garantas išduoda lakštų formos garantiją | — |
| `perimancio_garanto_gin` | `string` | — | `4` | `open` | — | Garanto, kuris perima įsipareigojimus, identifikacinis numeris (GIN) | — |
| `perimancio_garanto_pavadinimas` | `string` | — | `4` | `open` | — | Garanto, kuris perima įsipareigojimus, pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/garantai.csv
