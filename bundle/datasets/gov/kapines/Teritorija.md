---
type: Table
title: "Teritorija — Savivaldybių kapinių duomenys"
description: "Rinkinyje pateikiama Lietuvos savivaldybių kapinių bendro pobūdžio informacija, atvaizduojama kapinių skaitmeninimo ir duomenų valdymo sistemose „CEMETY“ ir „LIKSGIS“: kapinių pavadinimas, adresas, savivaldybė, kontaktiniai duomenys ir..."
resource: "https://get.data.gov.lt/datasets/gov/kapines/Teritorija"
tags: [gov, kapines, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kapines/informacija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kapines/informacija.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Teritorija — Savivaldybių kapinių duomenys

Rinkinyje pateikiama Lietuvos savivaldybių kapinių bendro pobūdžio informacija, atvaizduojama kapinių skaitmeninimo ir duomenų valdymo sistemose „CEMETY“ ir „LIKSGIS“: kapinių pavadinimas, adresas, savivaldybė, kontaktiniai duomenys ir kt. Rinkinio objektas – įrašas apie vienerias kapines.

- **Model:** `datasets/gov/kapines/Teritorija`[^manifest]
- **Dataset:** [Savivaldybių kapinių duomenys](../kapines.md) (`datasets/gov/kapines`)
- **Manifest CSV:** [datasets/gov/kapines/informacija.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kapines/informacija.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kapines/Teritorija`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `kapines` | `string` | — | `4` | `open` | — | Kapinių pavadinimas | — |
| `adresas_lt` | `string` | — | `1` | `open` | — | Fizinis kapinių adresas/Kapines administruojančios įstaigos adresas | — |
| `regionas` | `string` | — | `4` | `open` | — | Regionas | — |
| `miestas` | `string` | — | `4` | `open` | — | Miestas | — |
| `uzsakovas` | `string` | — | `4` | `open` | — | Kapinių savininkas | — |
| `statusas` | `string` | — | `4` | `open` | — | Kapinių būklės statusas duomenų atnaujinimo datai | — |
| `atverimo_valanda` | `integer` | — | `4` | `open` | — | Kapinių atidarymo valanda | — |
| `uzdarymo_valanda` | `integer` | — | `4` | `open` | — | Kapinių uždarymo valanda | — |
| `tel_nr` | `string` | — | `2` | `open` | — | Telefono numeris | — |
| `el_pastas` | `string` | — | `4` | `open` | — | Kontaktinis elektroninio pašto adresas | — |
| `interneto_adresas_lt` | `string` | — | `2` | `open` | — | Kapinių administratoriaus interneto adresas | — |
| `informacija_internete` | `boolean` | — | `4` | `open` | — | Požymis, ar duomenys apie kapines viešinamos internete | — |
| `ar_kulturinis` | `boolean` | — | `4` | `open` | — | Požymis, ar kapinės yra kultūrinis paminklas | — |
| `velioniu_sk` | `integer` | `U` | `4` | `open` | — | Velionių skaičius kapinėse duomenų atnaujinimo datai | — |
| `aprasymas_lt` | `string` | — | `1` | `open` | — | Kapinių aprašymas. Taip pat gali būti nurodoma papildoma kontaktinė informacija. | — |
| `ar_skaitmenizuotos` | `boolean` | — | `4` | `open` | — | Požymis, ar kapinės yra skaitmenizuotos | — |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | Kapinių vietos WGS koordinatės | — |
| `ar_nepriziurimi_viesinami` | `boolean` | — | `4` | `open` | — | Požymis, ar neprižiūrimos kapavietės yra viešinamos. | — |
| `ar_urnos_zemelapyje` | `boolean` | — | `4` | `open` | — | Požymis, ar urnos atvaizduojamos viešame žemėlapyje | — |
| `duomenu_atnaujinimas` | `date` | `D` | `4` | `open` | — | Paskutinė duomenų atnaujinimo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `statusas` | `"veikia"` | — | — | — | — |
| `statusas` | `"draudžiama laidoti"` | — | — | — | — |
| `statusas` | `"uždaryta"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `adresas_lt` | `update(property: "adresas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `el_pastas` | `"update(property: ""el_pastas[]"", type: ""array"", source: ""El_pastas"")"` | `property` | `4` | `open` | — | — | — |
| `interneto_adresas_lt` | `update(property: "adresas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `aprasymas_lt` | `update(property: "aprasymas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kapines/informacija.csv
