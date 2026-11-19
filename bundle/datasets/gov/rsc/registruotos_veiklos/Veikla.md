---
type: Table
title: "Veikla — Registruota veikla su jonizuojančios spinduliuotės šaltiniais"
description: "Spinta table datasets/gov/rsc/registruotos_veiklos/Veikla (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rsc/registruotos_veiklos/Veikla"
tags: [gov, rsc, veikla, deployed, level-2, cadence-unknown]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsc/registruotos_veiklos.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rsc/registruotos_veiklos.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2186/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rsc/registruotos_veiklos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Veikla — Registruota veikla su jonizuojančios spinduliuotės šaltiniais

- **Model:** `datasets/gov/rsc/registruotos_veiklos/Veikla`[^manifest]
- **Dataset:** [Radiacinės saugos centro registruotos veiklos su jonizuojančiosios spinduliuotės šaltiniais](../registruotos_veiklos.md) (`datasets/gov/rsc/registruotos_veiklos`)[^manifest]
- **Manifest CSV:** [datasets/gov/rsc/registruotos_veiklos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsc/registruotos_veiklos.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rsc/registruotos_veiklos/Veikla` (`deployed`)[^manifest]
- **Provider:** `rsc` — Radiacinės saugos centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `UNKNOWN`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `leid_nr` | `string` | — | `4` | `open` | — | Registruotos veiklos numeris | — |
| `isduota` | `date` | `D` | `4` | `open` | — | Registruotos veiklos išdavimo data | — |
| `busena` | `string` | — | `4` | `open` | — | Registruotos veiklos būsena | — |
| `ja_kodas` | `string` | — | `2` | `open` | — | Juridinio asmens kodas | — |
| `org_pav` | `string` | — | `1` | `open` | — | Juridinio asmens pavadinimas | — |
| `adresas` | `string` | — | `2` | `open` | — | Pilnas adresas | — |
| `miesto_pozymis` | `boolean` | — | `4` | `open` | — | Miesto požymis | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybės pavadinimas | — |
| `salis` | `string` | — | `4` | `open` | — | Valstybės pavadinimas | — |
| `koord` | `geometry(point, 3346)` | — | `3` | `open` | — | Juridinio asmens koordinatės | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `busena` | `"Neregistruota"` | — | — | Neregistruota | — |
| `busena` | `"Registruota"` | — | — | Registruota | — |
| `busena` | `"Panaikintas registravimas"` | — | — | Panaikintas registravimas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ja_kodas` | `create(property: "ja_kodas", type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | — | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rsc/registruotos_veiklos.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsc/registruotos_veiklos.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rsc/registruotos_veiklos (https://data.gov.lt/datasets/2186/)
