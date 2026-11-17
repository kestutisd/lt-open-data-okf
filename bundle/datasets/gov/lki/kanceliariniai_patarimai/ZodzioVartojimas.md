---
type: Table
title: "ZodzioVartojimas — Kanceliarinės kalbos terminų ir kitų kalbos reiškinių vartojimo paaiškinimai"
description: "Lentelėje pateikti antraštinių žodžių, t.y. kanceliarinės kalbos terminų ir kitų kalbos reiškinių (prielinksnių, žodžių dalių, gramatinių kategorijų ir kt.), vartojimo paaiškinimai iš Lietuvių kalbos instituto Kanceliarinės kalbos..."
resource: "https://get.data.gov.lt/datasets/gov/lki/kanceliariniai_patarimai/ZodzioVartojimas"
tags: [gov, lki, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lki/kanceliariniai_patarimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/kanceliariniai_patarimai.csv#L18"
    last_modified: "2026-11-11T14:39:20Z"
---

# ZodzioVartojimas — Kanceliarinės kalbos terminų ir kitų kalbos reiškinių vartojimo paaiškinimai

Lentelėje pateikti antraštinių žodžių, t.y. kanceliarinės kalbos terminų ir kitų kalbos reiškinių (prielinksnių, žodžių dalių, gramatinių kategorijų ir kt.), vartojimo paaiškinimai iš Lietuvių kalbos instituto Kanceliarinės kalbos patarimų duomenų bazės (http://kanceliariniaipatarimai.lki.lt/). Duomenys publikuojami internete nuo 2007 metų. Kiti šių duomenų atnaujinimai galimi ateityje, Lietuvių kalbos institutui vykdant duomenų rinkimo, atnaujinimo projektus.

- **Model:** `datasets/gov/lki/kanceliariniai_patarimai/ZodzioVartojimas`[^manifest]
- **Dataset:** [Rinkinyje - antraštinių žodžių, t.y. kanceliarinės kalbos terminų ir kitų kalbos reiškinių (prielinksnių, žodžių dalių, gramatinių kategorijų ir kt.), reikšmės ir vartojimo paaiškinimai iš Lietuvių kalbos instituto...](../kanceliariniai_patarimai.md) (`datasets/gov/lki/kanceliariniai_patarimai`)
- **Manifest CSV:** [datasets/gov/lki/kanceliariniai_patarimai.csv#L18](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/kanceliariniai_patarimai.csv#L18)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lki/kanceliariniai_patarimai/ZodzioVartojimas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `zodzio_kodas` | `string` | — | `4` | `open` | — | Antraštinio žodžio identifikatorius | — |
| `a_zodis_kirc` | `string` | — | `4` | `open` | — | Antraštinis žodis (sukirčiuotas) | — |
| `a_zodis_norm` | `string` | — | `4` | `open` | — | Antraštinis žodis (nekirčiuotas) | — |
| `paaiskinimas_html` | `string` | — | `4` | `open` | — | Žodžio paaiškinimas (-ai) (html formatu) | — |
| `paaiskinimas_txt_lt` | `string` | — | `4` | `open` | — | Žodžio paaiškinimas (-ai) (paprasto teksto formatu) | — |
| `paaiskinimo_nr` | `integer` | — | `4` | `open` | — | Paaiškinimo numeris | — |
| `paaiskinimo_eiles_nr` | `integer` | — | `4` | `open` | — | Paaiškinimo eilės numeris | — |
| `data_pildymo` | `datetime` | `S` | `4` | `open` | — | Duomenų eilutės įrašo pildymo data | — |
| `data_taisymo` | `datetime` | `S` | `4` | `open` | — | Duomenų eilutės įrašo taisymo data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paaiskinimas_txt_lt` | `update(property: "paaiskinimas_txt_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lki/kanceliariniai_patarimai.csv
