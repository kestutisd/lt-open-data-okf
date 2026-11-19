---
type: Table
title: "GeologinisTyrimas — Geologinių tyrimų ataskaitų katalogas"
description: "Spinta table datasets/gov/lgt/geologiniai_tyrimai/GeologinisTyrimas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/geologiniai_tyrimai/GeologinisTyrimas"
tags: [gov, lgt, geologinistyrimas, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geologiniai_tyrimai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/lgt/geologiniai_tyrimai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1325/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lgt/geologiniai_tyrimai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# GeologinisTyrimas — Geologinių tyrimų ataskaitų katalogas

- **Model:** `datasets/gov/lgt/geologiniai_tyrimai/GeologinisTyrimas`[^manifest]
- **Dataset:** [Geologinių tyrimų ataskaitų katalogas](../geologiniai_tyrimai.md) (`datasets/gov/lgt/geologiniai_tyrimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lgt/geologiniai_tyrimai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geologiniai_tyrimai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/geologiniai_tyrimai/GeologinisTyrimas` (`deployed`)[^manifest]
- **Provider:** `lgt` — Lietuvos geologijos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `fondo_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fondo_nr` | `string` | — | `4` | `open` | — | Dokumento numeris Geologijos fondo kataloge | — |
| `rusis` | `string` | — | `3` | `open` | — | Dokumento rūšis | — |
| `rubrikos` | `string` | — | `2` | `open` | — | Rubrikos | — |
| `autoriai` | `string` | — | `2` | `open` | — | Autoriai | — |
| `antraste` | `string` | — | `2` | `open` | — | Antrastė | — |
| `parengimo_metai` | `integer` | — | `2` | `open` | — | Parengimo metai | — |
| `apribota_iki` | `date` | `D` | `4` | `open` | — | Apribota iki | — |
| `aprasas` | `string` | — | `2` | `open` | — | Aprašas | — |
| `iraso_data` | `date` | `D` | `4` | `open` | — | Įrašo data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `rubrikos` | `update(property: "rubrika[]", type: "string", source: "Rubrika")` | `property` | `4` | — | — | — | — |
| `autoriai` | `update(property: "autorius[]", type: "string", source: "Autorius")` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/geologiniai_tyrimai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geologiniai_tyrimai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lgt/geologiniai_tyrimai (https://data.gov.lt/datasets/1325/)
