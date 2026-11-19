---
type: Table
title: "NVInformacijaPPS21 — Lietuvos kaimo plėtros programos 2014-2020 priemonė \"Parama Nykstančių Lietuvos senųjų veislių gyvulių ir naminių paukščių išsaugojimui\" bendra informacija"
description: "Spinta table datasets/gov/nma/nv_bendra_informacija/NVInformacijaPPS21 (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nma/nv_bendra_informacija/NVInformacijaPPS21"
tags: [gov, nma, nvinformacijapps21, deployed, level-3, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/nv_bendra_informacija.csv#L27"
    title: "atviriduomenys/manifest — datasets/gov/nma/nv_bendra_informacija.csv#L27"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2251/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nma/nv_bendra_informacija"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NVInformacijaPPS21 — Lietuvos kaimo plėtros programos 2014-2020 priemonė "Parama Nykstančių Lietuvos senųjų veislių gyvulių ir naminių...

- **Model:** `datasets/gov/nma/nv_bendra_informacija/NVInformacijaPPS21`[^manifest]
- **Dataset:** [Lietuvos kaimo plėtros programos 2014-2020 priemonė "Parama Nykstančių Lietuvos senųjų veislių...](../nv_bendra_informacija.md) (`datasets/gov/nma/nv_bendra_informacija`)[^manifest]
- **Manifest CSV:** [datasets/gov/nma/nv_bendra_informacija.csv#L27](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/nv_bendra_informacija.csv#L27)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nma/nv_bendra_informacija/NVInformacijaPPS21` (`deployed`)[^manifest]
- **Provider:** `nma` — Nacionalinė mokėjimo agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pareiskejo_tipas` | `string` | — | `4` | `open` | — | Pareiškėjo tipas | — |
| `pareiskejo_lytis` | `string` | — | `4` | `open` | — | Pareiškėjo lytis | — |
| `paraiskos_pateikimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos pateikimo data | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybės ŽŪS | — |
| `programa` | `string` | — | `3` | `open` | — | Programa | — |
| `ismoketa_suma` | `number` | — | `2` | `open` | — | Išmokėta paramos suma | — |
| `valdos_numeris` | `string` | — | `4` | `open` | — | Valda | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pareiskejo_tipas` | `"Fizinis"` | — | — | Fizinis asmuo | — |
| `pareiskejo_tipas` | `"Juridinis"` | — | — | Juridinis asmuo | — |
| `pareiskejo_lytis` | `"V"` | — | — | Vyras | — |
| `pareiskejo_lytis` | `"M"` | — | — | Moteris | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `update(type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `ismoketa_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nma/nv_bendra_informacija.csv#L27 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/nv_bendra_informacija.csv#L27)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nma/nv_bendra_informacija (https://data.gov.lt/datasets/2251/)
