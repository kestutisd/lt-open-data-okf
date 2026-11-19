---
type: Table
title: "AdresoGardele — Aktualių adresų gardelės"
description: "Grafinio adresų registro aktualių (galiojančių) adresų geoerdviniai duomenys (taškai) su skirtingų dydžių gardelių identifikatoriais."
resource: "https://get.data.gov.lt/datasets/gov/lsd/aktualiu_adresu_gardeles/AdresoGardele"
tags: [gov, lsd, adresogardele, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/aktualiu_adresu_gardeles.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lsd/aktualiu_adresu_gardeles.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2693/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/aktualiu_adresu_gardeles"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# AdresoGardele — Aktualių adresų gardelės

Grafinio adresų registro aktualių (galiojančių) adresų geoerdviniai duomenys (taškai) su skirtingų dydžių gardelių identifikatoriais. Gardelių identifikatoriai paimti iš tinklelių lentelių (https://get.data.gov.lt/datasets/gov/lsd/grid/:ns).[^manifest]

- **Model:** `datasets/gov/lsd/aktualiu_adresu_gardeles/AdresoGardele`[^manifest]
- **Dataset:** [Aktualių adresų gardelės](../aktualiu_adresu_gardeles.md) (`datasets/gov/lsd/aktualiu_adresu_gardeles`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/aktualiu_adresu_gardeles.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/aktualiu_adresu_gardeles.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/aktualiu_adresu_gardeles/AdresoGardele` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `aob_kodas` | `ref` | [Adresas](../../rc/ar/adresai/Adresas.md) (`level=4 UUID`: `aob_kodas._id`) | `4` | `open` | — | Adreso (sklypo, statinio, patalpos) identifikavimo kodas | — |
| `x_koord` | `number` | — | `4` | `open` | — | Adreso objekto x koordinatė (LKS94) | — |
| `y_koord` | `number` | — | `4` | `open` | — | Adreso objekto y koordinatė (LKS94) | — |
| `geometrija` | `geometry(point, 4326)` | — | `4` | `open` | — | Adreso taško koordinatės (WGS84) | WGS-84 |
| `sq_100m_grid_id` | `string` | — | `4` | `open` | — | Stačiakampės 100 m gardelės unikalus identifikatorius (LKS-94) | — |
| `sq_250m_grid_id` | `string` | — | `4` | `open` | — | Stačiakampės 250 m gardelės unikalus identifikatorius (LKS-94) | — |
| `sq_500m_grid_id` | `string` | — | `4` | `open` | — | Stačiakampės 500 m gardelės unikalus identifikatorius (LKS-94) | — |
| `sq_1km_grid_id` | `string` | — | `4` | `open` | — | Stačiakampės 1 km gardelės unikalus identifikatorius (LKS-94) | — |
| `sq_2_5km_grid_id` | `string` | — | `4` | `open` | — | Stačiakampės 2,5 km gardelės unikalus identifikatorius (LKS-94) | — |
| `sq_5km_grid_id` | `string` | — | `4` | `open` | — | Stačiakampės 5 km gardelės unikalus identifikatorius (LKS-94) | — |
| `sq_10km_grid_id` | `string` | — | `4` | `open` | — | Stačiakampės 10 km gardelės unikalus identifikatorius (LKS-94) | — |
| `hx_1km_grid_id` | `string` | — | `4` | `open` | — | Šešiakampės 1 km gardelės unikalus identifikatorius (LKS-94) | — |
| `hx_2km_grid_id` | `string` | — | `4` | `open` | — | Šešiakampės 2 km gardelės unikalus identifikatorius (LKS-94) | — |
| `hx_5km_grid_id` | `string` | — | `4` | `open` | — | Šešiakampės 5 km gardelės unikalus identifikatorius (LKS-94) | — |
| `sen_kodas` | `ref` | [Seniunija](../../rc/ar/seniunija/Seniunija.md) (`level=4 UUID`: `sen_kodas._id`) | `4` | `open` | — | Seniūnijos, kurios teritorijoje yra objektas, identifikavimo kodas | — |
| `sen_pav` | `string` | — | `4` | `open` | — | Seniūnijos, kurios teritorijoje yra objektas, pavadinimas | — |
| `sav_kodas` | `ref` | [Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `sav_kodas._id`) | `4` | `open` | — | Savivaldybės, kurios teritorijoje yra objektas, identifikavimo kodas | — |
| `sav_pav` | `string` | — | `4` | `open` | — | Savivaldybės, kurios teritorijoje yra objektas, pavadinimas | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/aktualiu_adresu_gardeles.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/aktualiu_adresu_gardeles.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/aktualiu_adresu_gardeles (https://data.gov.lt/datasets/2693/)
