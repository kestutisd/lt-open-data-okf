---
type: Table
title: "Tipas — Patarlės ir priežodžiai"
description: "Lietuvių patarlių ir priežodžių tipų sąrašas."
resource: "https://get.data.gov.lt/datasets/gov/llti/patarles_priezodziai/Tipas"
tags: [gov, llti, tipas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/patarles_priezodziai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/llti/patarles_priezodziai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2920/"
    title: "data.gov.lt DCAT-AP — datasets/gov/llti/patarles_priezodziai"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# Tipas — Patarlės ir priežodžiai

Lietuvių patarlių ir priežodžių tipų sąrašas. Tipas – tai populiariausias ar reprezentatyviausias, į svarbiausius rinkinius įtrauktas lietuviškos patarlės arba priežodžio variantas. Tipų antraštės (pavadinimai) pateikiamos su atraminiais žodžiais, interpretacija, vertimu į anglų, vokiečių bei rusų kalbas, variantų skaičiumi, sąsajomis su kitais tipais ir nuoroda į atitinkamo tipo puslapį Lietuvių literatūros ir tautosakos instituto patarlių ir priežodžių elektroniniame sąvade <https://elpp.archyvas.llti.lt/lt>. Ta pati tipų antraštė gali pasikartoti tarp kelių susijusių tipų ir tuomet turės skirtingus variantų (kurie šioje lentelėje nepateikiami) atraminius žodžius.[^manifest]

- **Model:** `datasets/gov/llti/patarles_priezodziai/Tipas`[^manifest]
- **Dataset:** [Patarlių ir priežodžių elektroninis sąvadas](../patarles_priezodziai.md) (`datasets/gov/llti/patarles_priezodziai`)[^manifest]
- **Manifest CSV:** [datasets/gov/llti/patarles_priezodziai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/patarles_priezodziai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/llti/patarles_priezodziai/Tipas` (`deployed`)[^manifest]
- **Provider:** `llti` — Lietuvių literatūros ir tautosakos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `tipo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-10-20`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tipo_id` | `string` | — | `4` | `open` | — | Tipo identifikatorius | — |
| `tipo_antraste` | `string` | — | `4` | `open` | — | Tipo antraštė | — |
| `frml_atraminis_zodis` | `string` | — | `4` | `open` | — | Formalusis atraminis žodis | — |
| `smnt_atraminis_zodis` | `string` | — | `4` | `open` | — | Semantinis atraminis žodis | — |
| `interpretacija` | `string` | — | `4` | `open` | — | Interpretacija lietuvių kalba | — |
| `interpretacija_en` | `string` | — | `4` | `open` | — | Interpretacija anglų kalba | — |
| `vertimas_en` | `string` | — | `4` | `open` | — | Vertimas į anglų kalbą | — |
| `vertimas_de` | `string` | — | `4` | `open` | — | Vertimas į vokiečių kalbą | — |
| `vertimas_ru` | `string` | — | `4` | `open` | — | Vertimas į rusų kalbą | — |
| `pastabos` | `string` | — | `4` | `open` | — | Pastabos | — |
| `variantu_skaicius_orig` | `integer` | — | `4` | `open` | — | Variantų originalus skaičius | — |
| `variantu_skaicius` | `integer` | — | `4` | `open` | — | Variantų atnaujintas skaičius | — |
| `tipo_id_nuoroda` | `string` | — | `4` | `open` | — | Išsamesnį aprašą turinčio panašaus tipo identifikatorius | — |
| `susijusiu_tipu_id` | `string` | — | `4` | `open` | — | Susijusių tipų identifikatoriai | — |
| `savado_url` | `url` | — | `4` | `open` | — | Žiniatinklio puslapis „Patarlių ir priežodžių elektroniniame sąvade“ | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tipo_antraste` | `update(property: "tipo_antraste@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `interpretacija` | `update(property: "interpretacija@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `interpretacija_en` | `update(property: "interpretacija_en@en", type: "text")` | `type` | `4` | `open` | — | — | — |
| `vertimas_en` | `update(property: "vertimas_en@en", type: "text")` | `type` | `4` | `open` | — | — | — |
| `vertimas_de` | `update(property: "vertimas_de@de", type: "text")` | `type` | `4` | `open` | — | — | — |
| `vertimas_ru` | `update(property: "vertimas_ru@ru", type: "text")` | `type` | `4` | `open` | — | — | — |
| `pastabos` | `update(property: "pastabos@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/llti/patarles_priezodziai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/patarles_priezodziai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/llti/patarles_priezodziai (https://data.gov.lt/datasets/2920/)
