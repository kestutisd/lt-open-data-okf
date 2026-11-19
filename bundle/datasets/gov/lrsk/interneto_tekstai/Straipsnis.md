---
type: Table
title: "Straipsnis — Lietuvos Respublikos Seimo interneto svetainėje paskelbtų tekstų duomenys"
description: "Lietuvos Respublikos Seimo interneto svetainėje paskelbtų tekstų duomenys"
resource: "https://get.data.gov.lt/datasets/gov/lrsk/interneto_tekstai/Straipsnis"
tags: [gov, lrsk, straipsnis, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/tekstai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lrsk/tekstai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2609/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lrsk/interneto_tekstai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Straipsnis — Lietuvos Respublikos Seimo interneto svetainėje paskelbtų tekstų duomenys

Lietuvos Respublikos Seimo interneto svetainėje paskelbtų tekstų duomenys[^manifest]

- **Model:** `datasets/gov/lrsk/interneto_tekstai/Straipsnis`[^manifest]
- **Dataset:** [Lietuvos Respublikos Seimo interneto svetainėje paskelbtų tekstų duomenys](../interneto_tekstai.md) (`datasets/gov/lrsk/interneto_tekstai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lrsk/tekstai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/tekstai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/interneto_tekstai/Straipsnis` (`deployed`)[^manifest]
- **Provider:** `lrsk` — Lietuvos Respublikos Seimo Kanceliarija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo unikalus identifikatorius | — |
| `tekst_pav_lt` | `string` | — | `2` | `open` | — | Teksto pavadinimas internetiniame puslapyje | — |
| `tekstas_lt` | `string` | — | `2` | `open` | — | Publikuoto teksto turinys | — |
| `kalba` | `string` | — | `4` | `open` | — | Teksto kalba | — |
| `paskelbimas` | `date` | `D` | `4` | `open` | — | Teksto paskelbimo data | — |
| `koregavimas` | `date` | `D` | `4` | `open` | — | Paskutinė teksto redagavimo data | — |
| `tekst_url` | `string` | — | `4` | `open` | — | Nuoroda į tekstą Lietuvos Respublikos Seimo portale | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tekst_pav_lt` | `update(property: "tekst_pav_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `tekstas_lt` | `update(property: "tekstas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

# Related References

- [ISO 639 Language Codes Reference](../../../../references/iso-639-kalbu-kodai.md) — ISO 639-1 / 639-2 / EU NAL codes and special markers `zxx`, `und`, `mul`, `mis`.

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/tekstai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/tekstai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lrsk/interneto_tekstai (https://data.gov.lt/datasets/2609/)
