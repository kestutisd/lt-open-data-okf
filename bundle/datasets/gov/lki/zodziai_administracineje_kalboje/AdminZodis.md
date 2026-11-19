---
type: Table
title: "AdminZodis — Administracinės lietuvių kalbos žodžiai ir kiti reiškiniai"
description: "Lentelėje pateikta dalis lietuvių administracinėje kalboje aptinkamų probleminių žodžių ir kitų kalbos reiškinių su jų vartosenos paaiškinimais iš Lietuvių kalbos instituto (LKI) Administracinės kalbos aktualijų duomenų bazės, kuriai duomenys rinkti iš verstinių Europos..."
resource: "https://get.data.gov.lt/datasets/gov/lki/zodziai_administracineje_kalboje/AdminZodis"
tags: [gov, lki, adminzodis, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/zodziai_administracineje_kalboje.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lki/zodziai_administracineje_kalboje.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2686/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lki/zodziai_administracineje_kalboje"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# AdminZodis — Administracinės lietuvių kalbos žodžiai ir kiti reiškiniai

Lentelėje pateikta dalis lietuvių administracinėje kalboje aptinkamų probleminių žodžių ir kitų kalbos reiškinių su jų vartosenos paaiškinimais iš Lietuvių kalbos instituto (LKI) Administracinės kalbos aktualijų duomenų bazės, kuriai duomenys rinkti iš verstinių Europos Sąjungos dokumentų. Pirmą kartą duomenys surinkti 2014 m. Kiti šių duomenų atnaujinimai galimi ateityje, Lietuvių kalbos institutui vykdant papildomus duomenų rinkimo projektus.[^manifest]

- **Model:** `datasets/gov/lki/zodziai_administracineje_kalboje/AdminZodis`[^manifest]
- **Dataset:** [Administracinės lietuvių kalbos žodžiai ir kiti reiškiniai](../zodziai_administracineje_kalboje.md) (`datasets/gov/lki/zodziai_administracineje_kalboje`)[^manifest]
- **Manifest CSV:** [datasets/gov/lki/zodziai_administracineje_kalboje.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/zodziai_administracineje_kalboje.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lki/zodziai_administracineje_kalboje/AdminZodis` (`deployed`)[^manifest]
- **Provider:** `lki` — Lietuvių kalbos institutas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `zodis` | `string` | — | `4` | `open` | — | Žodis ar kitas kalbos reiškinys | — |
| `paaiskinimas_lt` | `string` | — | `4` | `open` | — | Žodžio ar kito kalbos reiškinio vartosenos paaiškinimas (pateiktas grynojo teksto formatu) | — |
| `paaiskinimas_html_lt` | `string` | — | `4` | `open` | — | Žodžio ar kito kalbos reiškinio vartosenos paaiškinimas (pateiktas html formatu) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paaiskinimas_lt` | `update(property: "paaiskinimas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `paaiskinimas_html_lt` | `update(property: "paaiskinimas_html_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lki/zodziai_administracineje_kalboje.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/zodziai_administracineje_kalboje.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lki/zodziai_administracineje_kalboje (https://data.gov.lt/datasets/2686/)
