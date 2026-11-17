---
type: Table
title: "SumaMediatoriui — Teiktų mediacijos paslaugų trukmė ir vertė"
description: "Spinta table datasets/gov/vgtpt/teisis/ismoketa_mediatoriams/SumaMediatoriui (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vgtpt/teisis/ismoketa_mediatoriams/SumaMediatoriui"
tags: [gov, vgtpt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vgtpt/teisis/ismoketa_mediatoriams.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/ismoketa_mediatoriams.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# SumaMediatoriui — Teiktų mediacijos paslaugų trukmė ir vertė

- **Model:** `datasets/gov/vgtpt/teisis/ismoketa_mediatoriams/SumaMediatoriui`[^manifest]
- **Dataset:** [Teiktų mediacijos paslaugų trukmė ir vertė](../ismoketa_mediatoriams.md) (`datasets/gov/vgtpt/teisis/ismoketa_mediatoriams`)
- **Manifest CSV:** [datasets/gov/vgtpt/teisis/ismoketa_mediatoriams.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/ismoketa_mediatoriams.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vgtpt/teisis/ismoketa_mediatoriams/SumaMediatoriui`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `sprendimo_metai` | `integer` | — | `2` | `open` | — | Sprendimo išmokėti užmokestį metai | — |
| `sprendimo_ketvirtis` | `integer` | — | `2` | `open` | — | Sprendimo išmokėti užmokestį ketvirtis | — |
| `teritorijos_kodas` | `ref` | [/datasets/gov/vgtpt/teisis/klasifikatoriai/Teritorija](../klasifikatoriai/Teritorija.md) | `4` | `open` | — | Antrinę teisinę pagalbą gaunančio asmens gyvenamosios vietos teritorijos kodas | Iš TEISIS teritorijos klasifikatoriaus |
| `mediacijos_rusis` | `integer` | — | `4` | `open` | — | Požymis, nurodantis mediacijos rūšį | — |
| `priskaiciuota_suma` | `number` | — | `2` | `open` | — | Sprendime nurodytas mediatoriui išmokėti skirtas užmokestis | — |
| `trukme` | `integer` | `min` | `4` | `open` | — | Mediatoriaus sugaišto laiko trukmė | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `mediacijos_rusis` | `0` | — | — | Taikoma teisminė mediacija | — |
| `mediacijos_rusis` | `1` | — | — | Taikoma valstybės užtikrinama neteisminė mediacija | — |
| `mediacijos_rusis` | `2` | — | — | Taikoma privalomoji mediacija | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sprendimo_metai` | `update(type: "date", ref: "Q")` | `type` | `4` | — | — | — | — |
| `priskaiciuota_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vgtpt/teisis/ismoketa_mediatoriams.csv
