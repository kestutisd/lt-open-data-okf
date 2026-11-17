---
type: Table
title: "Dokumentas — Lietuvos muitinei pateikiamų dokumentų sąrašo duomenys"
description: "Spinta table datasets/gov/muitine/dokumentu_sarasas/Dokumentas (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/muitine/dokumentu_sarasas/Dokumentas"
tags: [gov, muitine, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/dokumentu_sarasas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/dokumentu_sarasas.csv#L13"
    last_modified: "2026-11-11T14:39:20Z"
---

# Dokumentas — Lietuvos muitinei pateikiamų dokumentų sąrašo duomenys

- **Model:** `datasets/gov/muitine/dokumentu_sarasas/Dokumentas`[^manifest]
- **Dataset:** [Lietuvos muitinei pateikiamų dokumentų sąrašo duomenys](../dokumentu_sarasas.md) (`datasets/gov/muitine/dokumentu_sarasas`)
- **Manifest CSV:** [datasets/gov/muitine/dokumentu_sarasas.csv#L13](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/dokumentu_sarasas.csv#L13)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/dokumentu_sarasas/Dokumentas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA identifikatorius | Unikalus Valstybės duomenų agentūros eilutės identifikatorius. Eilutės unikalumą sudaro stulpeliai - rusies_kodas, dok_pav, pav_galioja_nuo |
| `dok_rusis` | `string` | — | `4` | `open` | — | Dokumento rūšis | — |
| `rusis_galioja_nuo` | `date` | `D` | `4` | `open` | — | Dokumento rūšies galiojimo pradžios data | — |
| `rusis_galioja_iki` | `date` | `D` | `4` | `open` | — | Dokumento rūšies galiojimo pabaigos data | — |
| `rusies_pav` | `string` | — | `4` | `open` | — | Dokumento rūšies pavadinimas | — |
| `rusies_kodas` | `string` | — | `4` | `open` | — | Dokumento rūšies kodas | — |
| `kod_galioja_nuo` | `date` | `D` | `4` | `open` | — | Dokumento rūšies kodas galiojimo pradžia | — |
| `kod_galioja_iki` | `date` | `D` | `4` | `open` | — | Dokumento rūšies kodo galiojimo pabaiga | — |
| `dok_kod_pav` | `string` | — | `3` | `open` | — | Dokumento rūšies kodo pavadinimas | — |
| `kod_pav_galioja_nuo` | `date` | `D` | `4` | `open` | — | Dokumento rūšies kodo pavadinimo galiojimo pradžios data | — |
| `dok_saltinis` | `string` | — | `4` | `open` | — | Dokumento šaltinis | Dokumento šaltinis. Požymis TARIC reiškia, kad dokumento įrašas gautas iš Europos Sąjungos integruoto tarifo (TARIC) duomenų bazės. Požymis National reiškia, kad dokumento įrašas yra iš dokumentų nacionalinių kodų sąrašo |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `dok_saltinis` | `"Taric"` | — | — | Taric | Dokumento įrašas gautas iš Europos Sąjungos integruoto tarifo (TARIC) duomenų bazės |
| `dok_saltinis` | `"National"` | — | — | National | Dokumento įrašas yra iš dokumentų nacionalinių kodų sąrašo |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/dokumentu_sarasas.csv
