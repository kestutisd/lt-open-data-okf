---
type: Table
title: "SenGeoDuom2010 — Seniūnijų taškiniai geoerdviniai duomenys\",\" remiantis visuotiniu žemės ūkių sura"
description: "Spinta table datasets/gov/lsd/zemes_ukis/SenGeoDuom2010 (13 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/zemes_ukis/SenGeoDuom2010"
tags: [gov, lsd, sengeoduom2010, deployed, level-4, cadence-decennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/zemes_ukio_surasymai.csv#L47"
    title: "atviriduomenys/manifest — datasets/gov/lsd/zemes_ukio_surasymai.csv#L47"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1909/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/zemes_ukis"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# SenGeoDuom2010 — Seniūnijų taškiniai geoerdviniai duomenys"," remiantis visuotiniu žemės ūkių sura

- **Model:** `datasets/gov/lsd/zemes_ukis/SenGeoDuom2010`[^manifest]
- **Dataset:** [Lietuvos Respublikos visuotinio žemės ūkio surašymo rezultatų duomenys](../zemes_ukis.md) (`datasets/gov/lsd/zemes_ukis`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/zemes_ukio_surasymai.csv#L47](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/zemes_ukio_surasymai.csv#L47)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/zemes_ukis/SenGeoDuom2010` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `objectid`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DECENNIAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `geo_koord` | `geometry(point, 4326)` | `m` | `4` | `open` | — | Ūkio koordinatė (WGS84) | — |
| `objectid` | `integer` | — | `4` | `open` | — | Objekto įdentifikatorius | — |
| `sav_pav` | `string` | — | `2` | `open` | — | Savivaldybės pavadinimas | — |
| `sen_pav` | `string` | — | `2` | `open` | — | Seniūnijos pavadinimas | — |
| `galviju_sk` | `string` | — | `4` | `open` | — | Galvijų skaičius | — |
| `pauksc_sk` | `string` | — | `4` | `open` | — | Paukščių skaičius | — |
| `ariama_z` | `number` | — | `3` | `open` | — | Ariama žemė | — |
| `ukiu_sk` | `integer` | — | `4` | `open` | — | Ūkių skaičius | — |
| `znaudmenos` | `number` | — | `4` | `open` | — | Žemės naudmenos | — |
| `apskr_pav` | `string` | — | `2` | `open` | — | Apskrities pavadinimas | — |
| `kiauliu_sk` | `string` | — | `4` | `open` | — | Kiaulių skaičius | — |
| `darbuot_sk` | `string` | — | `4` | `open` | — | Darbuotojų skaičius | — |
| `karviu_sk` | `string` | — | `4` | `open` | — | Karvių skaičius | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/zemes_ukio_surasymai.csv#L47 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/zemes_ukio_surasymai.csv#L47)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/zemes_ukis (https://data.gov.lt/datasets/1909/)
