---
type: Table
title: "LeidimasNaudotiIskasenas — Leidimų naudoti naudingųjų iškasenų (išskyrus angliavandenilius), požeminio vandens išteklius ir žemės gelmių ertmes, duomenys"
description: "Spinta table datasets/gov/lgt/leidimas_naudoti_naudingasiais_iskasenas_duomenys/LeidimasNaudotiIskasenas (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/leidimas_naudoti_naudingasiais_iskasenas_duomenys/LeidimasNaudotiIskasenas"
tags: [gov, lgt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lgt/geo_naud_iskasenos_leid.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geo_naud_iskasenos_leid.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# LeidimasNaudotiIskasenas — Leidimų naudoti naudingųjų iškasenų (išskyrus angliavandenilius), požeminio vandens išteklius ir žemės gelmių ertmes, duomenys

- **Model:** `datasets/gov/lgt/leidimas_naudoti_naudingasiais_iskasenas_duomenys/LeidimasNaudotiIskasenas`[^manifest]
- **Dataset:** [Leidimų naudoti naudingųjų iškasenų (išskyrus angliavandenilius), požeminio vandens išteklius ir žemės gelmių ertmes, duomenys](../leidimas_naudoti_naudingasiais_iskasenas_duomenys.md) (`datasets/gov/lgt/leidimas_naudoti_naudingasiais_iskasenas_duomenys`)
- **Manifest CSV:** [datasets/gov/lgt/geo_naud_iskasenos_leid.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geo_naud_iskasenos_leid.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/leidimas_naudoti_naudingasiais_iskasenas_duomenys/LeidimasNaudotiIskasenas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Įrašo numeris | — |
| `nr` | `string` | — | `4` | `open` | — | Leidimo numeris | — |
| `data_nuo` | `date` | `D` | `4` | `open` | — | Leidimo išdavimo data | — |
| `data_iki` | `date` | `D` | `4` | `open` | — | Leidimas galioja iki | — |
| `ja_kodas` | `integer` | — | `2` | `open` | — | Juridinis asmuo | — |
| `ja_asmuo` | `string` | — | `1` | `open` | — | Įmonės pavadinimas arba asmens vardas pavardė, kuriam priklauso leidimas | — |
| `obj_sarasas` | `string` | — | `2` | `open` | — | Leidžiamų eksploatuoti objektų sąrašas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ja_kodas` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `base` | `4` | `open` | — | — | — |
| `ja_kodas` | `update(type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/geo_naud_iskasenos_leid.csv
