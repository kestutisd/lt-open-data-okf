---
type: Table
title: "NVInformacija — Lietuvos kaimo plėtros programos 2014-2020 priemonė \"Parama Nykstančių Lietuvos senųjų veislių gyvulių ir naminių paukščių išsaugojimui\" bendra informacija"
description: "Spinta table datasets/gov/nma/nv_bendra_informacija/NVInformacija (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nma/nv_bendra_informacija/NVInformacija"
tags: [gov, nma, nvinformacija, deployed, level-3, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/nv_bendra_informacija.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/nma/nv_bendra_informacija.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2251/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nma/nv_bendra_informacija"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NVInformacija — Lietuvos kaimo plėtros programos 2014-2020 priemonė "Parama Nykstančių Lietuvos senųjų veislių gyvulių ir naminių...

- **Model:** `datasets/gov/nma/nv_bendra_informacija/NVInformacija`[^manifest]
- **Dataset:** [Lietuvos kaimo plėtros programos 2014-2020 priemonė "Parama Nykstančių Lietuvos senųjų veislių...](../nv_bendra_informacija.md) (`datasets/gov/nma/nv_bendra_informacija`)[^manifest]
- **Manifest CSV:** [datasets/gov/nma/nv_bendra_informacija.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/nv_bendra_informacija.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nma/nv_bendra_informacija/NVInformacija` (`deployed`)[^manifest]
- **Provider:** `nma` — Nacionalinė mokėjimo agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `programa` | `string` | — | `3` | `open` | — | Priemonės pavadinimas | — |
| `veiklos_sritis` | `string` | — | `3` | `open` | — | Veiklos sritis | — |
| `pareiskejo_tipas` | `string` | — | `4` | `open` | — | Pareiškėjo tipas | — |
| `pareiskejo_lytis` | `string` | — | `4` | `open` | — | Pareiškėjo lytis | — |
| `paraiskos_pateikimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos pateikimo data | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Projekto įgyvendinimo vieta | — |
| `bylos_etapas` | `string` | — | `3` | `open` | — | Bylos etapas | — |
| `sutarties_pasirasymo_data` | `date` | `D` | `4` | `open` | — | Paramos sutarties pasirašymo data | — |
| `ismoketa_paramos_suma` | `number` | — | `2` | `open` | — | Išmokėta paramos suma, Eur | — |
| `sankciju_suma` | `number` | — | `2` | `open` | — | Bendra pritaikytų sankcijų suma, Eur | — |
| `paraiskos_nutr_data` | `date` | `D` | `4` | `open` | — | Paraiškos nutraukimo data | — |
| `kvietimo_pradzia` | `date` | `D` | `4` | `open` | — | Kvietimo pradžia | — |
| `kvietimo_pabaiga` | `date` | `D` | `4` | `open` | — | Kvietimo pabaiga | — |
| `bylos_numeris` | `string` | — | `4` | `open` | — | Projektas | — |

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
| `ismoketa_paramos_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `sankciju_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nma/nv_bendra_informacija.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/nv_bendra_informacija.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nma/nv_bendra_informacija (https://data.gov.lt/datasets/2251/)
