---
type: Table
title: "EcallSkambutis — Transporto priemonių pagalbos iškvietimo skambučių „eCall“ duomenys"
description: "Lentelėje pateikti Bendrosios pagalbos centro (BPC) registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, duomenys, kai transporto priemonėje įrengta sistema suaktyvinama automatiškai (transporto priemonėje įrengtais..."
resource: "https://get.data.gov.lt/datasets/gov/bpc/pagalbos_ecall_iskvietimai/EcallSkambutis"
tags: [gov, bpc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/bpc/pagalbos_ecall_iskvietimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_ecall_iskvietimai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# EcallSkambutis — Transporto priemonių pagalbos iškvietimo skambučių „eCall“ duomenys

Lentelėje pateikti Bendrosios pagalbos centro (BPC) registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, duomenys, kai transporto priemonėje įrengta sistema suaktyvinama automatiškai (transporto priemonėje įrengtais jutikliais) arba rankiniu būdu ir per mobiliojo ryšio tinklą užmezgamas ryšys tarp į eismo ar kitokį įvykį patekusios transporto priemonės ir Bendrojo pagalbos centro. Duomenys kaupiami nuo 2003 m. ir yra atnaujinami kas mėnesį.

- **Model:** `datasets/gov/bpc/pagalbos_ecall_iskvietimai/EcallSkambutis`[^manifest]
- **Dataset:** [datasets/gov/bpc/pagalbos_ecall_iskvietimai](../pagalbos_ecall_iskvietimai.md) (`datasets/gov/bpc/pagalbos_ecall_iskvietimai`)
- **Manifest CSV:** [datasets/gov/bpc/pagalbos_ecall_iskvietimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_ecall_iskvietimai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/bpc/pagalbos_ecall_iskvietimai/EcallSkambutis`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `ivykio_id` | `string` | — | `4` | `open` | — | Įvykio identifikatorius | — |
| `ivykio_tipas` | `string` | — | `4` | `open` | — | Įvykio tipas | — |
| `aktyvavosi_automatiskai` | `boolean` | — | `4` | `open` | — | Požymis, ar eCall funkcija aktyvavosi automatiškai | — |
| `vin` | `string` | — | `4` | `open` | — | Transporto priemonės identifikavimo numeris | — |
| `valst_numeriai` | `string` | — | `4` | `open` | — | Transporto priemonės valstybiniai numeriai | — |
| `marke` | `string` | — | `4` | `open` | — | Transporto priemonės markė | — |
| `modelis` | `string` | — | `4` | `open` | — | Transporto priemonės modelis | — |
| `spalva` | `string` | — | `4` | `open` | — | Transporto priemonės spalva | — |
| `kuras` | `string` | — | `4` | `open` | — | Transporto priemonės naudojamas kuras | — |
| `tp_tipas` | `string` | — | `4` | `open` | — | Transporto priemonės tipas | — |
| `iv_miestas` | `string` | — | `4` | `open` | — | Įvykio miestas | — |
| `iv_vieta` | `string` | — | `4` | `open` | — | Įvykio vieta | — |
| `iv_savivaldybe` | `string` | — | `4` | `open` | — | Įvykio savivaldybė | — |
| `iv_gatve` | `string` | — | `4` | `open` | — | Įvykio gatvė | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | Įvykio x koordinatė pagal LKS-94 koordinačių sistemą | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Įvykio y koordinatė pagal LKS-94 koordinačių sistemą | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/bpc/pagalbos_ecall_iskvietimai.csv
