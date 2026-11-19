---
type: Table
title: "KasimoLokacija — Kauno miesto savivaldybėje vykdomų kasimo darbų lokacijos"
description: "Šiame rinkinyje pateikiamos Kauno miesto savivaldybės kasimo darbų lokacijos."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/kasimai/KasimoLokacija"
tags: [gov, kauno_m_sav, kasimolokacija, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/kasimai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/kasimai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2708/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/kasimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# KasimoLokacija — Kauno miesto savivaldybėje vykdomų kasimo darbų lokacijos

Šiame rinkinyje pateikiamos Kauno miesto savivaldybės kasimo darbų lokacijos. Lokacijos pateikiamos WGS ir LKS koordinačių sistemose. Rinkinys jungiasi su „Kasimai“ rinkiniu per „prasymo_id“ raktą (kasimai.id = kasimoLokacija.prasymo_id).[^manifest]

- **Model:** `datasets/gov/kauno_m_sav/kasimai/KasimoLokacija`[^manifest]
- **Dataset:** [Kauno miesto savivaldybėje vykdomų kasimo darbų lokacijos](../kasimai.md) (`datasets/gov/kauno_m_sav/kasimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/kauno_m_sav/kasimai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/kasimai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/kasimai/KasimoLokacija` (`deployed`)[^manifest]
- **Provider:** `kauno_m_sav` — Kauno miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Identifikacinis numeris | — |
| `leidimo_id` | `string` | — | `4` | `open` | — | Leidimo identifikacinis numeris | — |
| `leidimo_nr` | `string` | — | `4` | `open` | — | Leidimo numeris | — |
| `leidimo_isdavimo_data` | `date` | `D` | `4` | `open` | — | Leidimo išdavimo data | — |
| `prasymo_id` | `string` | — | `4` | `open` | — | Prašymo identifikacinis numeris | — |
| `prasymo_nr` | `string` | — | `4` | `open` | — | Prašymo numeris | — |
| `pasymo_teikimo_data` | `date` | `D` | `4` | `open` | — | Prašymo pateikimo data | — |
| `x_koord_lks` | `number` | — | `4` | `open` | — | X koordinatė LKS94 koordinačių sistemoje | — |
| `y_koord_lks` | `number` | — | `4` | `open` | — | Y koordinatė LKS94 koordinačių sistemoje | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Platumos koordinatė WGS84 koordinačių sistemoje | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Ilgumos koordinatė WGS84 koordinačių sistemoje | — |
| `geometrija` | `geometry(point, 4326)` | — | `4` | `open` | — | Geometrija | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/kasimai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/kasimai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/kasimai (https://data.gov.lt/datasets/2708/)
