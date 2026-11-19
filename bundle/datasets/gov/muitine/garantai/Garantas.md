---
type: Table
title: "Garantas — Informacija apie muitinės garantus"
description: "Informacija apie muitinės garanto statusą turinčias banko įstaigas ar draudimo bendroves"
resource: "https://get.data.gov.lt/datasets/gov/muitine/garantai/Garantas"
tags: [gov, muitine, garantas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/garantai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/muitine/garantai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2837/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/garantai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Garantas — Informacija apie muitinės garantus

Informacija apie muitinės garanto statusą turinčias banko įstaigas ar draudimo bendroves[^manifest]

- **Model:** `datasets/gov/muitine/garantai/Garantas`[^manifest]
- **Dataset:** [Informacija apie muitinės garantus](../garantai.md) (`datasets/gov/muitine/garantai`)[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/garantai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/garantai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/garantai/Garantas` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/garantai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/garantai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/garantai (https://data.gov.lt/datasets/2837/)
