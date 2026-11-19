---
type: Table
title: "Zeldynas — Anykščių miesto želdynai"
description: "Informacija apie Anykščių miesto želdynus"
resource: "https://get.data.gov.lt/datasets/gov/anyksciu_r_sav/zeldiniai/Zeldynas"
tags: [gov, anyksciu_r_sav, zeldynas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anyksciu_r_sav/zeldiniai.csv#L23"
    title: "atviriduomenys/manifest — datasets/gov/anyksciu_r_sav/zeldiniai.csv#L23"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2900/"
    title: "data.gov.lt DCAT-AP — datasets/gov/anyksciu_r_sav/zeldiniai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Zeldynas — Anykščių miesto želdynai

Informacija apie Anykščių miesto želdynus[^manifest]

- **Model:** `datasets/gov/anyksciu_r_sav/zeldiniai/Zeldynas`[^manifest]
- **Dataset:** [Anykščių miesto želdiniai ir želdynai](../zeldiniai.md) (`datasets/gov/anyksciu_r_sav/zeldiniai`)[^manifest]
- **Manifest CSV:** [datasets/gov/anyksciu_r_sav/zeldiniai.csv#L23](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anyksciu_r_sav/zeldiniai.csv#L23)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/anyksciu_r_sav/zeldiniai/Zeldynas` (`deployed`)[^manifest]
- **Provider:** `anyksciu_r_sav` — Anykščių rajono savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `objekto_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `objekto_id` | `string` | — | `4` | `open` | — | Želdyno identifikatorius | — |
| `zona` | `string` | — | `4` | `open` | — | Zona nurodanti ar želdynas yra gatvės ar miesto teritorijoje | — |
| `kvartalas_gatve` | `string` | — | `4` | `open` | — | Kvartalo numeris arba gatvės pavadinimas, kurioje auga želdynas | — |
| `sklypo_numeris` | `string` | — | `4` | `open` | — | Sklypo numeris, kuriame auga želdynas | — |
| `kvartalas_gatve_sklypas` | `string` | — | `4` | `open` | — | Kvartalo ir sklypo numeriai arba gatvės pavadinimas ir sklypo numeris | — |
| `zeldyno_plotas` | `number` | — | `4` | `open` | — | Želdyno plotas kvadratiniais metrais | — |
| `ar_kirsti` | `string` | — | `4` | `open` | — | Dokumento numeris leidžiantis kirtimą | — |
| `ar_zeldinti` | `string` | — | `4` | `open` | — | Identifikatorius nurodantis ar reikalingas papildomas želdinimas | — |
| `zeldyno_koordinates` | `geometry(polygon,3346)` | `m` | `3` | `open` | — | Želdyno ribos nurodytos koordinatėmis LKS koordinačių sistemoje | — |
| `geometrija_adp` | `geometry(point, 3346)` | — | `3` | `open` | — | Želdyno ribos nurodytos koordinatėmis LKS koordinačių sistemoje, kai Želdynas padalintas į kelias dalis | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `zona` | `"miesto"` | — | — | Miesto zona | — |
| `zona` | `"gatves"` | — | — | Gatvės zona | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/anyksciu_r_sav/zeldiniai.csv#L23 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anyksciu_r_sav/zeldiniai.csv#L23)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/anyksciu_r_sav/zeldiniai (https://data.gov.lt/datasets/2900/)
