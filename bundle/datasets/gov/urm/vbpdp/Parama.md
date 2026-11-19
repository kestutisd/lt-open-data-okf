---
type: Table
title: "Parama"
description: "Spinta table datasets/gov/urm/vbpdp/Parama (9 columns)."
tags: [gov, urm, parama, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/urm/vbpdp.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/urm/vbpdp.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Parama

- **Model:** `datasets/gov/urm/vbpdp/Parama`[^manifest]
- **Dataset:** [Vystomojo bendradarbiavimo ir paramos demokratijai programos įgyvendinimas](../vbpdp.md) (`datasets/gov/urm/vbpdp`)[^manifest]
- **Manifest CSV:** [datasets/gov/urm/vbpdp.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/urm/vbpdp.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `urm` — Lietuvos Respublikos užsienio reikalų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `metai`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `savanoriskos_imokos` | `number` | — | `2` | `open` | — | Savanoriškoms įmokoms į daugiašalius fondus | — |
| `projektai` | `number` | — | `2` | `open` | — | Projektams | — |
| `humanitarine_pagalba` | `number` | — | `2` | `open` | — | Humanitarinei pagalbai | — |
| `dalyvavimas_tarpt_org` | `number` | — | `2` | `open` | — | Dalyvavimui ES, JT ir kitų tarptautinių organizacijų veikloje ir programos stebėsenai | — |
| `kitos_bendrad_veiklos` | `number` | — | `2` | `open` | — | Kitoms vystomojo bendradarbiavimo veikloms | — |
| `inasas_i_epf` | `number` | — | `2` | `open` | — | Įnašas į Europos plėtros fondą (EPF) | — |
| `mokesciai` | `number` | — | `2` | `open` | — | Mokesčiams tarptautinėms organizacijoms sumokėti | — |
| `is_viso` | `number` | — | `2` | `open` | — | Iš viso | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `savanoriskos_imokos` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `projektai` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `humanitarine_pagalba` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `dalyvavimas_tarpt_org` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `kitos_bendrad_veiklos` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `inasas_i_epf` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `mokesciai` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `is_viso` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/urm/vbpdp.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/urm/vbpdp.csv#L5)
