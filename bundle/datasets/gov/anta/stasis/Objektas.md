---
type: Table
title: "Objektas — Objektai"
description: "\"Duomenys apie įvairios paskirties objektus iš Asmens su negalia teisių apsaugos agentūros statinių prieinamumo neįgaliems stebėsenos ir kontrolės įrankio."
resource: "https://get.data.gov.lt/datasets/gov/anta/stasis/Objektas"
tags: [gov, anta, objektas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anta/anta_stasis_objektu_vertinimas.csv#L11"
    title: "atviriduomenys/manifest — datasets/gov/anta/anta_stasis_objektu_vertinimas.csv#L11"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3870/"
    title: "data.gov.lt DCAT-AP — datasets/gov/anta/stasis"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Objektas — Objektai

"Duomenys apie įvairios paskirties objektus iš Asmens su negalia teisių apsaugos agentūros statinių prieinamumo neįgaliems stebėsenos ir kontrolės įrankio. Viena eilutė atitinka vieną unikalų objektą, kurio pritaikomumas yra įvertintas Asmens su negalia teisių apsaugos agentūros. Eilutėje nurodomas unikalaus objekto identifikacinis numeris, kategorija, pavadinimas, savininko identifikacinis numeris ir tipas, objekto savivaldybė, miestas, gatvė ir koordinatės."[^manifest]

- **Model:** `datasets/gov/anta/stasis/Objektas`[^manifest]
- **Dataset:** [Objektų pritaikomumo negalią turintiems asmenims vertinimai](../stasis.md) (`datasets/gov/anta/stasis`)[^manifest]
- **Manifest CSV:** [datasets/gov/anta/anta_stasis_objektu_vertinimas.csv#L11](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anta/anta_stasis_objektu_vertinimas.csv#L11)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/anta/stasis/Objektas` (`deployed`)[^manifest]
- **Provider:** `anta` — Asmens su negalia teisių apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `objekto_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `objekto_id` | `string` | — | `4` | `open` | — | Objekto ID | Unikalaus objekto identifikacinis numeris |
| `kategorija` | `string` | — | `4` | `open` | — | Objekto kategorija | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Objekto pavadinimas | — |
| `savininko_id` | `string` | — | `4` | `open` | — | Savininko ID | Objekto savininko identifikacinis numeris |
| `savininko_tipas` | `string` | — | `4` | `open` | — | Objekto savininko tipas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė | "Savivaldybė, kurioje objektas yra" |
| `miestas` | `string` | — | `4` | `open` | — | Miestas | "Miestas, kuriame objektas yra" |
| `gatve` | `string` | — | `4` | `open` | — | Gatvė | "Gatvės, kurioje objektas yra, pavadinimas" |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | Geometrija | Geolokacinis WGS-84 koordinačių taškas nurodantis objekto tikslią vietą |
| `aukstu_sk` | `string` | — | `4` | `open` | — | Objekto aukštų skaičius | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/anta/anta_stasis_objektu_vertinimas.csv#L11 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anta/anta_stasis_objektu_vertinimas.csv#L11)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/anta/stasis (https://data.gov.lt/datasets/3870/)
