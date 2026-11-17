---
type: Table
title: "Zeldynas — Anykščių miesto želdynai"
description: "Informacija apie Anykščių miesto želdynus"
resource: "https://get.data.gov.lt/datasets/gov/anyksciu_r_sav/zeldiniai/Zeldynas"
tags: [gov, anyksciu_r_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/anyksciu_r_sav/zeldiniai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anyksciu_r_sav/zeldiniai.csv#L23"
    last_modified: "2026-11-11T14:39:20Z"
---

# Zeldynas — Anykščių miesto želdynai

Informacija apie Anykščių miesto želdynus

- **Model:** `datasets/gov/anyksciu_r_sav/zeldiniai/Zeldynas`[^manifest]
- **Dataset:** [Anykščių miesto želdiniai ir želdynai](../zeldiniai.md) (`datasets/gov/anyksciu_r_sav/zeldiniai`)
- **Manifest CSV:** [datasets/gov/anyksciu_r_sav/zeldiniai.csv#L23](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anyksciu_r_sav/zeldiniai.csv#L23)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/anyksciu_r_sav/zeldiniai/Zeldynas`
- **Primary Key (`ref`):** `objekto_id`
- **Level:** `4`

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

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `zona` | `"miesto"` | — | — | Miesto zona | — |
| `zona` | `"gatves"` | — | — | Gatvės zona | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/anyksciu_r_sav/zeldiniai.csv
