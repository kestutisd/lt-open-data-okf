---
type: Table
title: "Liniuote — Liniuočių taikymo duomenys"
description: "Lygių galimybių kontrolieriaus tarnybos organizuojamas liniuočių registras kaupia Lyčių lygybės ir Lygių galimybių liniuočių (atitinkamai, LLL ir LGL) taikymo duomenis atitinkamose organizacijose."
resource: "https://get.data.gov.lt/datasets/gov/lgkt/liniuotes/Liniuote"
tags: [gov, lgkt, liniuote, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgkt/liniuotes.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lgkt/liniuotes.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2815/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lgkt/liniuotes"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Liniuote — Liniuočių taikymo duomenys

Lygių galimybių kontrolieriaus tarnybos organizuojamas liniuočių registras kaupia Lyčių lygybės ir Lygių galimybių liniuočių (atitinkamai, LLL ir LGL) taikymo duomenis atitinkamose organizacijose. Duomenys kaupiami nuo 2018 m. ir yra atnaujinami. Duomenų rinkinys apima liniuotės registracijos numerį, tipą, organizaciją, kurioje ji taikyta, prašymų gavimo, anketų pildymo pabaigos bei liniuotės registravimo datas. Nuo 2022 m. kovo prašymų gavimo datos nebepildomos. Vienas duomenų rinkinio įrašas atitinka vieną organizaciją ir laikotarpį, kada buvo gautas prašymas, baigta pildyti anketa ir užregistruota liniuotė. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/lgkt/liniuotes/Liniuote`[^manifest]
- **Dataset:** [Liniuočių taikymo duomenys](../liniuotes.md) (`datasets/gov/lgkt/liniuotes`)[^manifest]
- **Manifest CSV:** [datasets/gov/lgkt/liniuotes.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgkt/liniuotes.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgkt/liniuotes/Liniuote` (`deployed`)[^manifest]
- **Provider:** `lgkt` — Lygių galimybių kontrolieriaus tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `liniuotes_tipas` | `"Lyčių lygybės liniuotė"` | — | — | Lyčių lygybės liniuotė | — |
| `liniuotes_tipas` | `"Lygių galimybių liniuotė"` | — | — | Lygių galimybių liniuotė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lgkt/liniuotes.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgkt/liniuotes.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lgkt/liniuotes (https://data.gov.lt/datasets/2815/)
