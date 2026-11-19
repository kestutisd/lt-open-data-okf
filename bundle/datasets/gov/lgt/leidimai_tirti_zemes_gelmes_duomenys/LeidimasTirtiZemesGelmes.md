---
type: Table
title: "LeidimasTirtiZemesGelmes — Leidimai tirti žemės gelmes duomenys"
description: "Spinta table datasets/gov/lgt/leidimai_tirti_zemes_gelmes_duomenys/LeidimasTirtiZemesGelmes (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/leidimai_tirti_zemes_gelmes_duomenys/LeidimasTirtiZemesGelmes"
tags: [gov, lgt, leidimastirtizemesgelmes, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/leidimai_tirti_gelmes.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/lgt/leidimai_tirti_gelmes.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1328/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lgt/leidimai_tirti_zemes_gelmes_duomenys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# LeidimasTirtiZemesGelmes — Leidimai tirti žemės gelmes duomenys

- **Model:** `datasets/gov/lgt/leidimai_tirti_zemes_gelmes_duomenys/LeidimasTirtiZemesGelmes`[^manifest]
- **Dataset:** [Leidimai tirti žemės gelmes duomenys](../leidimai_tirti_zemes_gelmes_duomenys.md) (`datasets/gov/lgt/leidimai_tirti_zemes_gelmes_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/lgt/leidimai_tirti_gelmes.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/leidimai_tirti_gelmes.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/leidimai_tirti_zemes_gelmes_duomenys/LeidimasTirtiZemesGelmes` (`deployed`)[^manifest]
- **Provider:** `lgt` — Lietuvos geologijos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Įrašo numeris | — |
| `nr` | `integer` | — | `4` | `open` | — | Leidimo numeris | — |
| `data_nuo` | `date` | `D` | `4` | `open` | — | Leidimo išdavimo data | — |
| `data_iki` | `date` | `D` | `4` | `open` | — | Leidimas galioja iki | — |
| `ja_kodas` | `integer` | — | `2` | `open` | — | Juridinio asmens kodas arba fizinio asmens vardas pavardė | — |
| `ja_asmuo` | `string` | — | `1` | `open` | — | Juridinio asmens pavadinimas | — |
| `veiklos` | `string` | — | `2` | `open` | — | Leidžiamų vykdyti tyrimų rūšys | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ja_kodas` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `base` | `4` | `open` | — | — | — |
| `ja_kodas` | `update(type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |
| `veiklos` | `update(property: "veikla[]", type: "string", source: "")` | `property` | `4` | — | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/leidimai_tirti_gelmes.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/leidimai_tirti_gelmes.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lgt/leidimai_tirti_zemes_gelmes_duomenys (https://data.gov.lt/datasets/1328/)
