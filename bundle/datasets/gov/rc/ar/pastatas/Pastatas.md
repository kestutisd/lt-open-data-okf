---
type: Table
title: "Pastatas — Adresų registro žemės sklypams ir pastatams suteiktų adresų tekstiniai duomenys"
description: "Žemės sklypams ir pastatams suteiktų adresų tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (žemės sklypams ar pastatams suteiktus adresus apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/pastatas/Pastatas"
tags: [gov, rc, pastatas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/pastatas.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/pastatas.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1342/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ar/pastatas"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Pastatas — Adresų registro žemės sklypams ir pastatams suteiktų adresų tekstiniai duomenys

Žemės sklypams ir pastatams suteiktų adresų tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (žemės sklypams ar pastatams suteiktus adresus apibūdinantys duomenys). Duomenų geografinė imtis — visa šalies teritorija.[^manifest]

- **Model:** `datasets/gov/rc/ar/pastatas/Pastatas`[^manifest]
- **Dataset:** [Adresų registras](../pastatas.md) (`datasets/gov/rc/ar/pastatas`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/pastatas.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/pastatas.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/pastatas/Pastatas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `aob_kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `ref` | [Savivaldybe](../savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybės, kurios teritorijoje yra statinys arba žemės sklypas, identifikavimo kodas | — |
| `aob_kodas` | `ref` | [Adresas](../adresai/Adresas.md) (`level=4 UUID`: `aob_kodas._id`) | `4` | `open` | — | Statinio arba žemės sklypo identifikavimo kodas | — |
| `gyvenamoji_vietove` | `ref` | [GyvenamojiVietove](../gyvenamojivietove/GyvenamojiVietove.md) (`level=4 UUID`: `gyvenamoji_vietove._id`) | `4` | `open` | — | Gyvenamosios vietovės, kuriai priklauso adresas, identifikavimo kodas | — |
| `gatve` | `ref` | [Gatve](../gatve/Gatve.md) (`level=4 UUID`: `gatve._id`) | `4` | `open` | — | Gatvės, kuriai priklauso adresas, identifikavimo kodas | — |
| `nr` | `string` | — | `4` | `open` | — | Žemės sklypo ir (ar) pastato numeris gatvėje arba gyvenamojoje vietovėje | — |
| `korpuso_nr` | `string` | — | `4` | `open` | — | Korpuso numeris | — |
| `pasto_kodas` | `string` | — | `4` | `open` | — | Pašto kodas | — |
| `aob_nuo` | `date` | `D` | `4` | `open` | — | Objekto įregistravimo data | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/pastatas.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/pastatas.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ar/pastatas (https://data.gov.lt/datasets/1342/)
