---
type: Table
title: "Atitikmuo — Atitikmenys kitomis kalbomis pagal šaltinius"
description: "Prie populiarių tarptautinių tipų teikiami patarlių atitikmenys latvių, lenkų, vokiečių, anglų, lotynų bei rusų kalbomis."
resource: "https://get.data.gov.lt/datasets/gov/llti/patarles_priezodziai/Atitikmuo"
tags: [gov, llti, atitikmuo, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/patarles_priezodziai.csv#L29"
    title: "atviriduomenys/manifest — datasets/gov/llti/patarles_priezodziai.csv#L29"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2920/"
    title: "data.gov.lt DCAT-AP — datasets/gov/llti/patarles_priezodziai"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# Atitikmuo — Atitikmenys kitomis kalbomis pagal šaltinius

Prie populiarių tarptautinių tipų teikiami patarlių atitikmenys latvių, lenkų, vokiečių, anglų, lotynų bei rusų kalbomis. Šie atitikmenys skiriasi nuo tipų lentelėje esančių patarlių vertimų į kitas kalbas, nes pastarieji vertimai yra tiesioginiai. Ši lentelė ir šaltinių lentelė susijungia per „saltinio_id“ stulpelį.[^manifest]

- **Model:** `datasets/gov/llti/patarles_priezodziai/Atitikmuo`[^manifest]
- **Dataset:** [Patarlių ir priežodžių elektroninis sąvadas](../patarles_priezodziai.md) (`datasets/gov/llti/patarles_priezodziai`)[^manifest]
- **Manifest CSV:** [datasets/gov/llti/patarles_priezodziai.csv#L29](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/patarles_priezodziai.csv#L29)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/llti/patarles_priezodziai/Atitikmuo` (`deployed`)[^manifest]
- **Provider:** `llti` — Lietuvių literatūros ir tautosakos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-10-20`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

# Related References

- [ISO 639 Language Codes Reference](../../../../references/iso-639-kalbu-kodai.md) — ISO 639-1 / 639-2 / EU NAL codes and special markers `zxx`, `und`, `mul`, `mis`.

[^manifest]: atviriduomenys/manifest — datasets/gov/llti/patarles_priezodziai.csv#L29 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/patarles_priezodziai.csv#L29)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/llti/patarles_priezodziai (https://data.gov.lt/datasets/2920/)
