---
type: Table
title: "Liniuote — Liniuočių taikymo duomenys"
description: "Lygių galimybių kontrolieriaus tarnybos organizuojamas liniuočių registras kaupia Lyčių lygybės ir Lygių galimybių liniuočių (atitinkamai, LLL ir LGL) taikymo duomenis atitinkamose organizacijose."
resource: "https://get.data.gov.lt/datasets/gov/lgkt/liniuotes/Liniuote"
tags: [gov, lgkt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lgkt/liniuotes.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgkt/liniuotes.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Liniuote — Liniuočių taikymo duomenys

Lygių galimybių kontrolieriaus tarnybos organizuojamas liniuočių registras kaupia Lyčių lygybės ir Lygių galimybių liniuočių (atitinkamai, LLL ir LGL) taikymo duomenis atitinkamose organizacijose. Duomenys kaupiami nuo 2018 m. ir yra atnaujinami. Duomenų rinkinys apima liniuotės registracijos numerį, tipą, organizaciją, kurioje ji taikyta, prašymų gavimo, anketų pildymo pabaigos bei liniuotės registravimo datas. Nuo 2022 m. kovo prašymų gavimo datos nebepildomos. Vienas duomenų rinkinio įrašas atitinka vieną organizaciją ir laikotarpį, kada buvo gautas prašymas, baigta pildyti anketa ir užregistruota liniuotė.

- **Model:** `datasets/gov/lgkt/liniuotes/Liniuote`[^manifest]
- **Dataset:** [Liniuočių taikymo duomenys](../liniuotes.md) (`datasets/gov/lgkt/liniuotes`)
- **Manifest CSV:** [datasets/gov/lgkt/liniuotes.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgkt/liniuotes.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgkt/liniuotes/Liniuote`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `registracijos_nr` | `string` | — | `4` | `open` | — | Liniuotės registracijos numeris | — |
| `liniuotes_tipas` | `string` | — | `4` | `open` | — | Liniuotės tipas | — |
| `institucija` | `string` | — | `4` | `open` | — | Organizacija, kurioje pritaikyta liniuotė | — |
| `prasymo_gavimo_data` | `date` | `D` | `4` | `open` | — | Prašymo gavimo data | — |
| `anketu_pildymo_pabaigos_data` | `date` | `D` | `4` | `open` | — | Anketų pildymo pabaigos data | — |
| `liniuotes_registravimo_data` | `date` | `D` | `4` | `open` | — | Liniuotės registravimo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `liniuotes_tipas` | `"Lyčių lygybės liniuotė"` | — | — | Lyčių lygybės liniuotė | — |
| `liniuotes_tipas` | `"Lygių galimybių liniuotė"` | — | — | Lygių galimybių liniuotė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lgkt/liniuotes.csv
