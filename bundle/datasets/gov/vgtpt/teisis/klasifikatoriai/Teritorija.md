---
type: Table
title: "Teritorija — Teisinės pagalbos paslaugų informacinės sistemos teritorijos klasifikatorius"
description: "Teisinės pagalbos paslaugų informacinės sistemos (TEISIS) klasifikatoriai, 3 vnt., Teisinės pagalbos paslaugų informacinės sistemos teritorijos klasifikatorius"
resource: "https://get.data.gov.lt/datasets/gov/vgtpt/teisis/klasifikatoriai/Teritorija"
tags: [gov, vgtpt, teritorija, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/klasifikatoriai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/vgtpt/teisis/klasifikatoriai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2288/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vgtpt/teisis/klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Teritorija — Teisinės pagalbos paslaugų informacinės sistemos teritorijos klasifikatorius

**Dataset Context:** Teisinės pagalbos paslaugų informacinės sistemos (TEISIS) klasifikatoriai, 3 vnt., Teisinės pagalbos paslaugų informacinės sistemos teritorijos klasifikatorius[^manifest]

- **Model:** `datasets/gov/vgtpt/teisis/klasifikatoriai/Teritorija`[^manifest]
- **Dataset:** [Teisinės pagalbos paslaugų informacinės sistemos (TEISIS) klasifikatoriai](../klasifikatoriai.md) (`datasets/gov/vgtpt/teisis/klasifikatoriai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vgtpt/teisis/klasifikatoriai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/klasifikatoriai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vgtpt/teisis/klasifikatoriai/Teritorija` (`deployed`)[^manifest]
- **Provider:** `vgtpt` — Valstybės garantuojamos teisinės pagalbos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `teritorijos_kodas` | `string` | — | `4` | `open` | — | Pagalbą gaunančio asmens gyvenamosios vietos teritorijos kodas | — |
| `teritorijos_pavadinimas` | `string` | — | `3` | `open` | — | Pagalbą gaunančio asmens gyvenamosios vietos teritorijos pavadinimas | Iš Adresų registro |
| `sav_kodas` | `ref` | [Savivaldybe](../../../rc/ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `sav_kodas._id`) | `4` | `open` | — | Savivaldybės kodas | Iš Adresų registro |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vgtpt/teisis/klasifikatoriai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/klasifikatoriai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vgtpt/teisis/klasifikatoriai (https://data.gov.lt/datasets/2288/)
