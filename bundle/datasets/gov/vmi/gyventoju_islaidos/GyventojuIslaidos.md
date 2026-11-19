---
type: Table
title: "GyventojuIslaidos — Duomenys apie mokėtojo deklaruotas išlaidas, kuriomis pagal GPMĮ 21 str. gali būti mažinamos apmokestinamosios pajamos"
description: "Spinta table datasets/gov/vmi/gyventoju_islaidos/GyventojuIslaidos (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/gyventoju_islaidos/GyventojuIslaidos"
tags: [gov, vmi, gyventojuislaidos, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/gyventoju_islaidos.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/vmi/gyventoju_islaidos.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1183/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/gyventoju_islaidos"
    author: "team:vda"
    last_modified: "2026-03-09T00:00:00Z"
---

# GyventojuIslaidos — Duomenys apie mokėtojo deklaruotas išlaidas, kuriomis pagal GPMĮ 21 str. gali būti mažinamos apmokestinamosios pajamos

- **Model:** `datasets/gov/vmi/gyventoju_islaidos/GyventojuIslaidos`[^manifest]
- **Dataset:** [Gyventojų patirtos išlaidos](../gyventoju_islaidos.md) (`datasets/gov/vmi/gyventoju_islaidos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/gyventoju_islaidos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/gyventoju_islaidos.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/gyventoju_islaidos/GyventojuIslaidos` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-03-09`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `4` | `open` | — | Mokestinio laikotarpio metai | — |
| `sav_kodas` | `string` | — | `4` | `open` | — | Sistemos subjekto savivaldybes kodas | — |
| `sav_pavadinimas` | `string` | — | `4` | `open` | — | Sistemos subjekto savivaldybes pavadinimas | — |
| `mm_kodas` | `string` | — | `4` | `open` | — | Mokesčių mokėtojo identifikacinis numeris | — |
| `ir_kodas` | `string` | — | `4` | `open` | — | Išlaidų rūšies kodas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Išlaidų pavadinimas | — |
| `suma` | `number` | — | `4` | `open` | — | Išlaidų suma | Išlaidų suma esanti virš 600000 eurų yra fiksuojama 600000 verte |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/gyventoju_islaidos.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/gyventoju_islaidos.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/gyventoju_islaidos (https://data.gov.lt/datasets/1183/)
