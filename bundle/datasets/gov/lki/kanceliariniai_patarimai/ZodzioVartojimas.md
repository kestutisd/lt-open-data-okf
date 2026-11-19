---
type: Table
title: "ZodzioVartojimas — Kanceliarinės kalbos terminų ir kitų kalbos reiškinių vartojimo paaiškinimai"
description: "Lentelėje pateikti antraštinių žodžių, t.y. kanceliarinės kalbos terminų ir kitų kalbos reiškinių (prielinksnių, žodžių dalių, gramatinių kategorijų ir kt.), vartojimo paaiškinimai iš Lietuvių kalbos instituto Kanceliarinės kalbos patarimų duomenų bazės..."
resource: "https://get.data.gov.lt/datasets/gov/lki/kanceliariniai_patarimai/ZodzioVartojimas"
tags: [gov, lki, zodziovartojimas, deployed, level-4, cadence-annual_3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/kanceliariniai_patarimai.csv#L18"
    title: "atviriduomenys/manifest — datasets/gov/lki/kanceliariniai_patarimai.csv#L18"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2828/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lki/kanceliariniai_patarimai"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# ZodzioVartojimas — Kanceliarinės kalbos terminų ir kitų kalbos reiškinių vartojimo paaiškinimai

Lentelėje pateikti antraštinių žodžių, t.y. kanceliarinės kalbos terminų ir kitų kalbos reiškinių (prielinksnių, žodžių dalių, gramatinių kategorijų ir kt.), vartojimo paaiškinimai iš Lietuvių kalbos instituto Kanceliarinės kalbos patarimų duomenų bazės (http://kanceliariniaipatarimai.lki.lt/). Duomenys publikuojami internete nuo 2007 metų. Kiti šių duomenų atnaujinimai galimi ateityje, Lietuvių kalbos institutui vykdant duomenų rinkimo, atnaujinimo projektus. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/lki/kanceliariniai_patarimai/ZodzioVartojimas`[^manifest]
- **Dataset:** [Rinkinyje - antraštinių žodžių, t.y. kanceliarinės kalbos terminų ir kitų kalbos reiškinių...](../kanceliariniai_patarimai.md) (`datasets/gov/lki/kanceliariniai_patarimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lki/kanceliariniai_patarimai.csv#L18](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/kanceliariniai_patarimai.csv#L18)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lki/kanceliariniai_patarimai/ZodzioVartojimas` (`deployed`)[^manifest]
- **Provider:** `lki` — Lietuvių kalbos institutas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_3`, Modified `2026-10-20`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lki/kanceliariniai_patarimai.csv#L18 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/kanceliariniai_patarimai.csv#L18)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lki/kanceliariniai_patarimai (https://data.gov.lt/datasets/2828/)
