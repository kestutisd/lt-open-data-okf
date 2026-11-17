---
type: Table
title: "Dangtis — Šulinių dangčių ir lietaus grotelių lokacijos"
description: "UAB „Šiaulių vandenys“ GIS informacinės sistemos lentelėje pateikiamos vandentiekio, fekalinių nuotekų ir lietaus nuotekų dangčių bei lietaus grotelių buvimo vietos."
resource: "https://get.data.gov.lt/datasets/gov/siauliu_vand/inzineriniai_tinklai/Dangtis"
tags: [gov, siauliu_vand, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/siauliu_vand/inzineriniai_tinklai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_vand/inzineriniai_tinklai.csv#L11"
    last_modified: "2026-11-11T14:39:20Z"
---

# Dangtis — Šulinių dangčių ir lietaus grotelių lokacijos

UAB „Šiaulių vandenys“ GIS informacinės sistemos lentelėje pateikiamos vandentiekio, fekalinių nuotekų ir lietaus nuotekų dangčių bei lietaus grotelių buvimo vietos. Siekiant užtikrinti konfidencialumą, pateiktų koordinačių įrašai yra modifikuoti pridedant atsitiktines vertes - triukšmą, sugeneruotą pagal normalųjį skirstinį su 50 metrų standartinio nuokrypio parametru. Naudojant šį parametrą, šulinys paslenkamas vidutiniškai per 62 metrus atsitiktine kryptimi.

Duomenų aprėptis – Šiaulių miesto savivaldybė.

Duomenų teikėjas – UAB „Šiaulių vandenys“.

- **Model:** `datasets/gov/siauliu_vand/inzineriniai_tinklai/Dangtis`[^manifest]
- **Dataset:** [Šulinių dangčių ir lietaus grotelių lokacijos](../inzineriniai_tinklai.md) (`datasets/gov/siauliu_vand/inzineriniai_tinklai`)
- **Manifest CSV:** [datasets/gov/siauliu_vand/inzineriniai_tinklai.csv#L11](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_vand/inzineriniai_tinklai.csv#L11)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/siauliu_vand/inzineriniai_tinklai/Dangtis`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `tipas` | `string` | — | `4` | `open` | — | Šulinio tipas | — |
| `erdvinio_obj_kodas` | `string` | — | `4` | `open` | — | Erdvinio objekto kodas | — |
| `igyvendintas` | `boolean` | — | `4` | `open` | — | Įgyvendintas | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Platumos koordinatė WGS84 koordinačių sistemoje | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Ilgumos koordinatė WGS84 koordinačių sistemoje | — |
| `geometrija` | `geometry(point, 4326)` | — | `3` | `open` | — | Geometrija WGS formatu | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Fekalinių nuotekų dangčiai"` | — | — | Fekalinių nuotekų dangčiai | — |
| `tipas` | `"Lietaus nuotekų dangčiai"` | — | — | Lietaus nuotekų dangčiai | — |
| `tipas` | `"Vandentekio dangčiai"` | — | — | Vandentekio dangčiai | — |
| `tipas` | `"Lietaus grotelės"` | — | — | Lietaus grotelės | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/siauliu_vand/inzineriniai_tinklai.csv
