---
type: Table
title: "SumaMediatoriui — Teiktų mediacijos paslaugų trukmė ir vertė"
description: "Valstybės garantuojamos teisinės pagalbos tarnybos duomenų, kaupiamų Teisinės pagalbos paslaugų informacinėje sistemoje (TEISIS),duomenys apie teiktų mediacijos paslaugų trukmę ir vertę."
resource: "https://get.data.gov.lt/datasets/gov/vgtpt/teisis/ismoketa_mediatoriams/SumaMediatoriui"
tags: [gov, vgtpt, sumamediatoriui, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/ismoketa_mediatoriams.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/vgtpt/teisis/ismoketa_mediatoriams.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1761/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vgtpt/teisis/ismoketa_mediatoriams"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# SumaMediatoriui — Teiktų mediacijos paslaugų trukmė ir vertė

**Dataset Context:** Valstybės garantuojamos teisinės pagalbos tarnybos duomenų, kaupiamų Teisinės pagalbos paslaugų informacinėje sistemoje (TEISIS),duomenys apie teiktų mediacijos paslaugų trukmę ir vertę. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 1 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0. Atvėrimo data —2023-04-03.[^manifest]

- **Model:** `datasets/gov/vgtpt/teisis/ismoketa_mediatoriams/SumaMediatoriui`[^manifest]
- **Dataset:** [Teiktų mediacijos paslaugų trukmė ir vertė](../ismoketa_mediatoriams.md) (`datasets/gov/vgtpt/teisis/ismoketa_mediatoriams`)[^manifest]
- **Manifest CSV:** [datasets/gov/vgtpt/teisis/ismoketa_mediatoriams.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/ismoketa_mediatoriams.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vgtpt/teisis/ismoketa_mediatoriams/SumaMediatoriui` (`deployed`)[^manifest]
- **Provider:** `vgtpt` — Valstybės garantuojamos teisinės pagalbos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `sprendimo_metai` | `integer` | — | `2` | `open` | — | Sprendimo išmokėti užmokestį metai | — |
| `sprendimo_ketvirtis` | `integer` | — | `2` | `open` | — | Sprendimo išmokėti užmokestį ketvirtis | — |
| `teritorijos_kodas` | `ref` | [Teritorija](../klasifikatoriai/Teritorija.md) (`level=4 UUID`: `teritorijos_kodas._id`) | `4` | `open` | — | Antrinę teisinę pagalbą gaunančio asmens gyvenamosios vietos teritorijos kodas | Iš TEISIS teritorijos klasifikatoriaus |
| `mediacijos_rusis` | `integer` | — | `4` | `open` | — | Požymis, nurodantis mediacijos rūšį | — |
| `priskaiciuota_suma` | `number` | — | `2` | `open` | — | Sprendime nurodytas mediatoriui išmokėti skirtas užmokestis | — |
| `trukme` | `integer` | `min` | `4` | `open` | — | Mediatoriaus sugaišto laiko trukmė | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `mediacijos_rusis` | `0` | — | — | Taikoma teisminė mediacija | — |
| `mediacijos_rusis` | `1` | — | — | Taikoma valstybės užtikrinama neteisminė mediacija | — |
| `mediacijos_rusis` | `2` | — | — | Taikoma privalomoji mediacija | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sprendimo_metai` | `update(type: "date", ref: "Q")` | `type` | `4` | — | — | — | — |
| `priskaiciuota_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vgtpt/teisis/ismoketa_mediatoriams.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/ismoketa_mediatoriams.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vgtpt/teisis/ismoketa_mediatoriams (https://data.gov.lt/datasets/1761/)
