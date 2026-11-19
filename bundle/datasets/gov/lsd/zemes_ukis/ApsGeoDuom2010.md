---
type: Table
title: "ApsGeoDuom2010 — Apskričių taškiniai geoerdviniai duomenys\",\" remiantis visuotiniu žemės ūkių surašymu 2010 m."
description: "Spinta table datasets/gov/lsd/zemes_ukis/ApsGeoDuom2010 (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/zemes_ukis/ApsGeoDuom2010"
tags: [gov, lsd, apsgeoduom2010, deployed, level-4, cadence-decennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/zemes_ukio_surasymai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/lsd/zemes_ukio_surasymai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1909/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/zemes_ukis"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# ApsGeoDuom2010 — Apskričių taškiniai geoerdviniai duomenys"," remiantis visuotiniu žemės ūkių surašymu 2010 m.

- **Model:** `datasets/gov/lsd/zemes_ukis/ApsGeoDuom2010`[^manifest]
- **Dataset:** [Lietuvos Respublikos visuotinio žemės ūkio surašymo rezultatų duomenys](../zemes_ukis.md) (`datasets/gov/lsd/zemes_ukis`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/zemes_ukio_surasymai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/zemes_ukio_surasymai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/zemes_ukis/ApsGeoDuom2010` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `objectid`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DECENNIAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `geo_koord` | `geometry(point, 4326)` | `m` | `4` | `open` | — | Ūkio koordinatė (WGS84) | — |
| `galviju_sk` | `integer` | — | `4` | `open` | — | Galvijų skaičius | — |
| `pauksc_sk` | `integer` | — | `4` | `open` | — | Paukščių skaičius | — |
| `ariama_z` | `number` | — | `3` | `open` | — | Ariama žemė | — |
| `ukiu_sk` | `integer` | — | `4` | `open` | — | Ūkių skaičius | — |
| `znaudmenos` | `integer` | — | `4` | `open` | — | Žemės naudmenos | — |
| `apskr_pav` | `string` | — | `2` | `open` | — | Apskrities pavadinimas | — |
| `kiauliu_sk` | `integer` | — | `4` | `open` | — | Kiaulių skaičius apskrityje | — |
| `darbuot_sk` | `integer` | — | `4` | `open` | — | Darbuotojų skaičius apskrityje | — |
| `karviu_sk` | `integer` | — | `4` | `open` | — | Karvių skaičius apskrityje | — |
| `objectid` | `integer` | — | `4` | `open` | — | Objekto įdentifikatorius | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/zemes_ukio_surasymai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/zemes_ukio_surasymai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/zemes_ukis (https://data.gov.lt/datasets/1909/)
