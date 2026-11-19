---
type: Table
title: "Agency — Viešojo transporto paslaugų teikėjai"
description: "Viešojo transporto operatorių (autobusų, traukinių) duomenys."
resource: "https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/Agency"
tags: [gov, ltsa, agency, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L58"
    title: "atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L58"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1929/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ltsa/viesasis_transportas"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# Agency — Viešojo transporto paslaugų teikėjai

Viešojo transporto operatorių (autobusų, traukinių) duomenys. GTFS formato duomenys iš Lietuvos transporto saugos administracijos VINTRA sistemos (https://www.visimarsrutai.lt/gtfs/)[^manifest]

- **Model:** `datasets/gov/ltsa/viesasis_transportas/Agency`[^manifest]
- **Dataset:** [Lietuvos transporto saugos administracijos viešojo transporto kelionių duomenys](../viesasis_transportas.md) (`datasets/gov/ltsa/viesasis_transportas`)[^manifest]
- **Manifest CSV:** [datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L58](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L58)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ltsa/viesasis_transportas/Agency` (`deployed`)[^manifest]
- **Provider:** `ltsa` — Lietuvos transporto saugos administracija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `agency_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-10-20`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `agency_id` | `string` | — | `3` | `open` | — | Agentūros unikalus identifikatorius | — |
| `agency_name` | `string` | — | `3` | `open` | — | Agentūros pavadinimas | — |
| `agency_url` | `string` | — | `4` | `open` | — | Agentūros svetainės URL | — |
| `agency_timezone` | `string` | — | `4` | `open` | — | Agentūros laiko juosta | — |
| `agency_lang` | `string` | — | `4` | `open` | — | Agentūros kalbos kodas ISO 639-1 formatu | — |
| `agency_phone` | `string` | — | `4` | `open` | — | Agentūros telefono numeris | — |
| `agency_fare_url` | `string` | — | `4` | `open` | — | Bilietų kainos informacijos svetainės URL | — |
| `agency_email` | `string` | — | `4` | `open` | — | Agentūros kontaktinis el. paštas | — |

# Related References

- [ISO 639 Language Codes Reference](../../../../references/iso-639-kalbu-kodai.md) — ISO 639-1 / 639-2 / EU NAL codes and special markers `zxx`, `und`, `mul`, `mis`.

[^manifest]: atviriduomenys/manifest — datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L58 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ltsa/viesojo_transporto_kelioniu_duomenys.csv#L58)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ltsa/viesasis_transportas (https://data.gov.lt/datasets/1929/)
