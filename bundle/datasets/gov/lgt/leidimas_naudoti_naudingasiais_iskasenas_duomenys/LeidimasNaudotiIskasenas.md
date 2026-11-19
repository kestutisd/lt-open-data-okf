---
type: Table
title: "LeidimasNaudotiIskasenas — Leidimų naudoti naudingųjų iškasenų (išskyrus angliavandenilius), požeminio vandens išteklius ir žemės gelmių ertmes, duomenys"
description: "Spinta table datasets/gov/lgt/leidimas_naudoti_naudingasiais_iskasenas_duomenys/LeidimasNaudotiIskasenas (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/leidimas_naudoti_naudingasiais_iskasenas_duomenys/LeidimasNaudotiIskasenas"
tags: [gov, lgt, leidimasnaudotiiskasenas, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geo_naud_iskasenos_leid.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lgt/geo_naud_iskasenos_leid.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1327/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lgt/leidimas_naudoti_naudingasiais_iskasenas_duomenys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# LeidimasNaudotiIskasenas — Leidimų naudoti naudingųjų iškasenų (išskyrus angliavandenilius), požeminio vandens išteklius ir žemės gelmių...

- **Model:** `datasets/gov/lgt/leidimas_naudoti_naudingasiais_iskasenas_duomenys/LeidimasNaudotiIskasenas`[^manifest]
- **Dataset:** [Leidimų naudoti naudingųjų iškasenų (išskyrus angliavandenilius), požeminio vandens išteklius ir...](../leidimas_naudoti_naudingasiais_iskasenas_duomenys.md) (`datasets/gov/lgt/leidimas_naudoti_naudingasiais_iskasenas_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/lgt/geo_naud_iskasenos_leid.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geo_naud_iskasenos_leid.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/leidimas_naudoti_naudingasiais_iskasenas_duomenys/LeidimasNaudotiIskasenas` (`deployed`)[^manifest]
- **Provider:** `lgt` — Lietuvos geologijos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/geo_naud_iskasenos_leid.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geo_naud_iskasenos_leid.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lgt/leidimas_naudoti_naudingasiais_iskasenas_duomenys (https://data.gov.lt/datasets/1327/)
