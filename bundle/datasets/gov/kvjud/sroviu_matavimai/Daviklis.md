---
type: Table
title: "Daviklis — Klaipėdos valstybinio jūrų uosto vandens srovių daviklių duomenys"
description: "AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami geografiniai jūrų uosto duomenys."
resource: "https://get.data.gov.lt/datasets/gov/kvjud/sroviu_matavimai/Daviklis"
tags: [gov, kvjud, daviklis, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/sroviu_matavimai.csv#L21"
    title: "atviriduomenys/manifest — datasets/gov/kvjud/sroviu_matavimai.csv#L21"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2860/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kvjud/sroviu_matavimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Daviklis — Klaipėdos valstybinio jūrų uosto vandens srovių daviklių duomenys

AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami geografiniai jūrų uosto duomenys. Rinkinyje pateikiami nuo 2016 m. gegužės veikaintys vertikalaus ir horizontaliojo daviklių duomenys.Vienas įrašas atitinka vieną daviklį. Duomenų teikėjas – AB Klaipėdos valstybinio jūrų uosto direkcija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/kvjud/sroviu_matavimai/Daviklis`[^manifest]
- **Dataset:** [Klaipėdos valstybinio jūrų uosto vandens srovių matavimo duomenys](../sroviu_matavimai.md) (`datasets/gov/kvjud/sroviu_matavimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/kvjud/sroviu_matavimai.csv#L21](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/sroviu_matavimai.csv#L21)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kvjud/sroviu_matavimai/Daviklis` (`deployed`)[^manifest]
- **Provider:** `kvjud` — AB Klaipėdos valstybinio jūrų uosto direkcija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `daviklio_id` | `string` | — | `4` | `open` | — | Daviklio identifikacinis numeris | — |
| `dav_pavadinimas` | `string` | — | `4` | `open` | — | Daviklio pavadinimas | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | X koordinatė LKS94 koordinačių sistemoje | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Y koordinatė LKS94 koordinačių sistemoje | — |
| `geometrija` | `geometry(point, 3346)` | — | `3` | `open` | — | Geometrija (lokacija) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `dav_pavadinimas` | `"Horizontalus daviklis"` | — | — | Horizontalus daviklis | — |
| `dav_pavadinimas` | `"Vertikalus daviklis"` | — | — | Vertikalus daviklis | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/kvjud/sroviu_matavimai.csv#L21 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/sroviu_matavimai.csv#L21)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kvjud/sroviu_matavimai (https://data.gov.lt/datasets/2860/)
