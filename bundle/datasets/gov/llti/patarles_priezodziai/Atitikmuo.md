---
type: Table
title: "Atitikmuo — Atitikmenys kitomis kalbomis pagal šaltinius"
description: "Prie populiarių tarptautinių tipų teikiami patarlių atitikmenys latvių, lenkų, vokiečių, anglų, lotynų bei rusų kalbomis."
resource: "https://get.data.gov.lt/datasets/gov/llti/patarles_priezodziai/Atitikmuo"
tags: [gov, llti, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/llti/patarles_priezodziai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/patarles_priezodziai.csv#L29"
    last_modified: "2026-11-11T14:39:20Z"
---

# Atitikmuo — Atitikmenys kitomis kalbomis pagal šaltinius

Prie populiarių tarptautinių tipų teikiami patarlių atitikmenys latvių, lenkų, vokiečių, anglų, lotynų bei rusų kalbomis. Šie atitikmenys skiriasi nuo tipų lentelėje esančių patarlių vertimų į kitas kalbas, nes pastarieji vertimai yra tiesioginiai. Ši lentelė ir šaltinių lentelė susijungia per „saltinio_id“ stulpelį.

- **Model:** `datasets/gov/llti/patarles_priezodziai/Atitikmuo`[^manifest]
- **Dataset:** [Patarlių ir priežodžių elektroninis sąvadas](../patarles_priezodziai.md) (`datasets/gov/llti/patarles_priezodziai`)
- **Manifest CSV:** [datasets/gov/llti/patarles_priezodziai.csv#L29](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/patarles_priezodziai.csv#L29)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/llti/patarles_priezodziai/Atitikmuo`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Atitikmens ir šaltinio derinio unikalus identifikatorius | — |
| `tipo_id` | `string` | — | `4` | `open` | — | Tipo identifikatorius | — |
| `kalba` | `string` | — | `4` | `open` | — | Užsienio kalbos santrumpa | — |
| `atitikmuo` | `string` | — | `4` | `open` | — | Tipo atitikmuo užsienio kalba | — |
| `saltinio_id` | `string` | — | `4` | `open` | — | Šaltinio identifikatorius | — |
| `saltinio_puslapis` | `string` | — | `4` | `open` | — | Šaltinio puslapis, kuriame minimas atitikmuo | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `atitikmuo` | `update(property: "atitikmuo", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/llti/patarles_priezodziai.csv
