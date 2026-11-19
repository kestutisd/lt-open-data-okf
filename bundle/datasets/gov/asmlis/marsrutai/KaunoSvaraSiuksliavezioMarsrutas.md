---
type: Table
title: "KaunoSvaraSiuksliavezioMarsrutas — UAB Kauno švara šiukšliavežių maršrutai"
description: "UAB Kauno švara informacinėje sistemoje MOKESTA kaupiami atliekų tvarkymo rinkliavų duomenys ir kitus duomenis."
resource: "https://get.data.gov.lt/datasets/gov/asmlis/marsrutai/KaunoSvaraSiuksliavezioMarsrutas"
tags: [gov, asmlis, kaunosvarasiuksliaveziomarsrutas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/marsrutai.csv#L33"
    title: "atviriduomenys/manifest — datasets/gov/asmlis/marsrutai.csv#L33"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2918/"
    title: "data.gov.lt DCAT-AP — datasets/gov/asmlis/marsrutai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# KaunoSvaraSiuksliavezioMarsrutas — UAB Kauno švara šiukšliavežių maršrutai

UAB Kauno švara informacinėje sistemoje MOKESTA kaupiami atliekų tvarkymo rinkliavų duomenys ir kitus duomenis. Duomenų rinkinyje pateikiami šiukšliavežių maršrutų duomenys:šifruotas automobilio valstybinis numeris, automobilio markė, laikas ir koordinatės, nurodančios vietą, kurioje tuo metu buvo automobilis.[^manifest]

- **Model:** `datasets/gov/asmlis/marsrutai/KaunoSvaraSiuksliavezioMarsrutas`[^manifest]
- **Dataset:** [Šiukšliavežių maršrutai](../marsrutai.md) (`datasets/gov/asmlis/marsrutai`)[^manifest]
- **Manifest CSV:** [datasets/gov/asmlis/marsrutai.csv#L33](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/marsrutai.csv#L33)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/asmlis/marsrutai/KaunoSvaraSiuksliavezioMarsrutas` (`deployed`)[^manifest]
- **Provider:** `asmlis` — MOKESTA ir ASMLIS sistemos *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `marsrutas` | `string` | — | `4` | `open` | — | Maršrutas | — |
| `automobilio_nr` | `string` | — | `4` | `open` | — | Automobilio numeris (šifruotas) | — |
| `marke` | `string` | — | `4` | `open` | — | Automobilio markė | — |
| `data` | `datetime` | `S` | `4` | `open` | — | Data | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Platumos koordinatė WGS84 koordinačių sistemoje | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Ilgumos koordinatė WGS84 koordinačių sistemoje | — |
| `tikslumas` | `number` | — | `4` | `open` | — | TIklsumas | — |
| `koodinates_saltinis` | `string` | — | `4` | `open` | — | Koordinatės šaltinis (gps - navigaciją, foreign - išoriniai, kiti šaltiniai) | — |
| `geometrija` | `geometry(point, 4326)` | — | `4` | `open` | — | Geometrija | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/asmlis/marsrutai.csv#L33 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/marsrutai.csv#L33)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/asmlis/marsrutai (https://data.gov.lt/datasets/2918/)
