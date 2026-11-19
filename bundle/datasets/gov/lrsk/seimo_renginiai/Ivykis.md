---
type: Table
title: "Ivykis — Duomenys apie Seime vykusius renginius"
description: "Rinkinyje pateikiami duomenys apie Seime organizuotus renginius nuo 2015m."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/seimo_renginiai/Ivykis"
tags: [gov, lrsk, ivykis, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/seimo_renginiai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lrsk/seimo_renginiai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2612/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lrsk/seimo_renginiai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Ivykis — Duomenys apie Seime vykusius renginius

Rinkinyje pateikiami duomenys apie Seime organizuotus renginius nuo 2015m. Pateikiama informacija: renginio pavadinimas, kalba, pradžios ir pabaigos laikas, renginio vieta ir vietų skaičius.[^manifest]

- **Model:** `datasets/gov/lrsk/seimo_renginiai/Ivykis`[^manifest]
- **Dataset:** [Duomenys apie Seime vykusius renginius](../seimo_renginiai.md) (`datasets/gov/lrsk/seimo_renginiai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lrsk/seimo_renginiai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/seimo_renginiai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/seimo_renginiai/Ivykis` (`deployed`)[^manifest]
- **Provider:** `lrsk` — Lietuvos Respublikos Seimo Kanceliarija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo unikalus identifikatorius | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Renginio pavadinimas | — |
| `kalba` | `string` | — | `4` | `open` | — | Renginio kalba | — |
| `pradzia` | `date` | `D` | `4` | `open` | — | Renginio pradžios data | — |
| `pabaiga` | `date` | `D` | `4` | `open` | — | Renginio pabaigos data | — |
| `vieta` | `string` | — | `4` | `open` | — | Renginio vieta | — |

# Related References

- [ISO 639 Language Codes Reference](../../../../references/iso-639-kalbu-kodai.md) — ISO 639-1 / 639-2 / EU NAL codes and special markers `zxx`, `und`, `mul`, `mis`.

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/seimo_renginiai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/seimo_renginiai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lrsk/seimo_renginiai (https://data.gov.lt/datasets/2612/)
