---
type: Table
title: "AdresoGardele — Aktualių adresų gardelės"
description: "Grafinio adresų registro aktualių (galiojančių) adresų geoerdviniai duomenys (taškai) su skirtingų dydžių gardelių identifikatoriais."
resource: "https://get.data.gov.lt/datasets/gov/lsd/aktualiu_adresu_gardeles/AdresoGardele"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/aktualiu_adresu_gardeles.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/aktualiu_adresu_gardeles.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# AdresoGardele — Aktualių adresų gardelės

Grafinio adresų registro aktualių (galiojančių) adresų geoerdviniai duomenys (taškai) su skirtingų dydžių gardelių identifikatoriais. Gardelių identifikatoriai paimti iš tinklelių lentelių (https://get.data.gov.lt/datasets/gov/lsd/grid/:ns).

- **Model:** `datasets/gov/lsd/aktualiu_adresu_gardeles/AdresoGardele`[^manifest]
- **Dataset:** [Aktualių adresų gardelės](../aktualiu_adresu_gardeles.md) (`datasets/gov/lsd/aktualiu_adresu_gardeles`)
- **Manifest CSV:** [datasets/gov/lsd/aktualiu_adresu_gardeles.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/aktualiu_adresu_gardeles.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/aktualiu_adresu_gardeles/AdresoGardele`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `aob_kodas` | `ref` | [/datasets/gov/rc/ar/adresai/Adresas](../../rc/ar/adresai/Adresas.md) | `4` | `open` | — | Adreso (sklypo, statinio, patalpos) identifikavimo kodas | — |
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
| `sen_kodas` | `ref` | [/datasets/gov/rc/ar/seniunija/Seniunija](../../rc/ar/seniunija/Seniunija.md) | `4` | `open` | — | Seniūnijos, kurios teritorijoje yra objektas, identifikavimo kodas | — |
| `sen_pav` | `string` | — | `4` | `open` | — | Seniūnijos, kurios teritorijoje yra objektas, pavadinimas | — |
| `sav_kodas` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybės, kurios teritorijoje yra objektas, identifikavimo kodas | — |
| `sav_pav` | `string` | — | `4` | `open` | — | Savivaldybės, kurios teritorijoje yra objektas, pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/aktualiu_adresu_gardeles.csv
