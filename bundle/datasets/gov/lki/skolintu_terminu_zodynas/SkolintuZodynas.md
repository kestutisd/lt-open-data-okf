---
type: Table
title: "SkolintuZodynas — Skolintų terminų ir jų atitikmenų žodynas"
description: "Lentelėje pateikiamas Lietuvių kalbos instituto (LKI) sudarytas aiškinamasis skolintų terminų ir jų atitikmenų žodynas (http://sta.lki.lt/)."
resource: "https://get.data.gov.lt/datasets/gov/lki/skolintu_terminu_zodynas/SkolintuZodynas"
tags: [gov, lki, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lki/skolintu_terminu_zodynas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/skolintu_terminu_zodynas.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# SkolintuZodynas — Skolintų terminų ir jų atitikmenų žodynas

Lentelėje pateikiamas Lietuvių kalbos instituto (LKI) sudarytas aiškinamasis skolintų terminų ir jų atitikmenų žodynas (http://sta.lki.lt/). Žodynas parengtas remiantis 1956–2010 m. išleistais įvairių sričių aiškinamaisiais bei verčiamaisiais terminų žodynais. Lentelę sudaro skolinti terminai, jų apibrėžtys, kirčiuoti terminai, sinonimai ir kitų kalbų atitikmenys..

- **Model:** `datasets/gov/lki/skolintu_terminu_zodynas/SkolintuZodynas`[^manifest]
- **Dataset:** [Skolintų terminų ir jų atitikmenų žodynas](../skolintu_terminu_zodynas.md) (`datasets/gov/lki/skolintu_terminu_zodynas`)
- **Manifest CSV:** [datasets/gov/lki/skolintu_terminu_zodynas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/skolintu_terminu_zodynas.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lki/skolintu_terminu_zodynas/SkolintuZodynas`
- **Primary Key (`ref`):** `termino_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `termino_kodas` | `string` | — | `4` | `open` | — | Unikalus termino kodas | — |
| `terminas` | `string` | — | `4` | `open` | — | Skolintas terminas | — |
| `kirciuotas_terminas` | `string` | — | `4` | `open` | — | Kirčiuotas terminas | — |
| `termino_sinonimai` | `string` | — | `4` | `open` | — | Atitikmenys | — |
| `vertimai` | `string` | — | `4` | `open` | — | Kitų kalbų atitikmenys iš visų šaltinių | — |
| `straipsnis_lt` | `string` | — | `4` | `open` | — | Straipsnis, kuriame pateikti terminai, jų apibrėžtys, sinonimai ir atitikmenys kitomis kalbomis su nurodytais šaltiniais (pateiktas grynojo teksto formatu) | — |
| `straipsnis_html_lt` | `string` | — | `4` | `open` | — | Straipsnis, kuriame pateikti terminai, jų apibrėžtys, sinonimai, atitikmenys kitomis kalbomis su nurodytais šaltiniais (pateiktas html formatu) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `straipsnis_lt` | `update(property: "straipsnis_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `straipsnis_html_lt` | `update(property: "straipsnis_html_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lki/skolintu_terminu_zodynas.csv
