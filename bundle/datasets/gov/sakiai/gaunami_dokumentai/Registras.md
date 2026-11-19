---
type: Table
title: "Registras"
description: "Visi nuo 2018 m. tik Šakių rajono savivaldybės administracijos raštinės registruoti gauti dokumentai - asmenų skundai, prašymai paslaugoms gauti, raštai iš LR ministerijų/departamentų ir kita."
resource: "https://get.data.gov.lt/datasets/gov/sakiai/gaunami_dokumentai/Registras"
tags: [gov, sakiai, registras, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sakiai/gaunami_dokumentai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/sakiai/gaunami_dokumentai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2390/"
    title: "data.gov.lt DCAT-AP — datasets/gov/sakiai/gaunami_dokumentai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Registras

**Dataset Context:** Visi nuo 2018 m. tik Šakių rajono savivaldybės administracijos raštinės registruoti gauti dokumentai - asmenų skundai, prašymai paslaugoms gauti, raštai iš LR ministerijų/departamentų ir kita.[^manifest]

- **Model:** `datasets/gov/sakiai/gaunami_dokumentai/Registras`[^manifest]
- **Dataset:** [Šakių rajono savivaldybės gaunami dokumentai](../gaunami_dokumentai.md) (`datasets/gov/sakiai/gaunami_dokumentai`)[^manifest]
- **Manifest CSV:** [datasets/gov/sakiai/gaunami_dokumentai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sakiai/gaunami_dokumentai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sakiai/gaunami_dokumentai/Registras` (`deployed`)[^manifest]
- **Provider:** `sakiai` — Šakių rajono savivaldybė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `rz_id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `open` (inherited)[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `rz_id` | `integer` | — | `4` | `open` (inherited) | — | — | — |
| `rz_skodas` | `string` | — | `2` | `open` (inherited) | — | Registro numeris | — |
| `rz_pav` | `string` | — | `2` | `open` (inherited) | — | Registro pavadinimas | — |
| `rz_pav2` | `string` | — | `2` | `open` (inherited) | — | Registro pavadinimas trumpas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sakiai/gaunami_dokumentai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sakiai/gaunami_dokumentai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/sakiai/gaunami_dokumentai (https://data.gov.lt/datasets/2390/)
