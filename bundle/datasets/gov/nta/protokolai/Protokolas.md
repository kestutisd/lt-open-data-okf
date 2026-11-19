---
type: Table
title: "Protokolas"
description: "Spinta table datasets/gov/nta/protokolai/Protokolas (15 columns)."
tags: [gov, nta, protokolas, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nta/protokolai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/nta/protokolai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Protokolas

- **Model:** `datasets/gov/nta/protokolai/Protokolas`[^manifest]
- **Dataset:** [datasets/gov/nta/protokolai](../protokolai.md) (`datasets/gov/nta/protokolai`)[^manifest]
- **Manifest CSV:** [datasets/gov/nta/protokolai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nta/protokolai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `nta` — Nacionalinė teismų administracija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `teismo_rumai` | `ref` | [JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) (`level=4 UUID` via `JuridinisAsmuo[ja_pavadinimas]`: `teismo_rumai._id`) | `4` | `open` | — | Teismo rūmai | — |
| `bylos_numeris` | `string` | — | `2` | `open` | — | Bylos numeris | — |
| `paskyrimo_budas` | `string` | — | `4` | `open` | — | Paskyrimo būdas | — |
| `nagrinejimo_priezastis` | `string` | — | `3` | `open` | — | Nagrinėjimo priežastis | — |
| `id` | `string` | — | `4` | `open` | — | Protokolo ID | — |
| `url` | `string` | — | `3` | `open` | — | Protokolo URL | — |
| `paskirtas_panaikintas_teisejas` | `string` | — | `3` | `public` | — | Paskirtas ar panaikintas teisėjas | — |
| `procesinis_numeris` | `string` | — | `3` | `open` | — | Procesinis numeris | — |
| `gauta` | `date` | `D` | `4` | `open` | — | Gavimo data | — |
| `baigta` | `date` | `D` | `4` | `open` | — | Baigimo data | — |
| `teisejo_numeris` | `integer` | — | `4` | `open` | — | Taisėjo numeris | — |
| `esamas_teisejas` | `string` | — | `3` | `public` | — | Esamas teisėjas | — |
| `instancija` | `string` | — | `4` | `open` | — | Instancija | — |
| `tipas` | `string` | — | `2` | `open` | — | Tipas | — |
| `potipis` | `string` | — | `2` | `open` | — | — | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paskyrimo_budas` | `"Bylos skyrimas prioritetine tvarka"` | — | — | Bylos skyrimas prioritetine tvarka | — |
| `paskyrimo_budas` | `"Įprastiniu būdu"` | — | — | Įprastiniu būdu | — |
| `paskyrimo_budas` | `"Panaikintas teisėjo skyrimas"` | — | — | Panaikintas teisėjo skyrimas | — |
| `paskyrimo_budas` | `"Preliminarus protokolo išrašas"` | — | — | Preliminarus protokolo išrašas | — |
| `paskyrimo_budas` | `"Skubos tvarka"` | — | — | Skubos tvarka | — |
| `instancija` | `"I-a instancija"` | — | — | I-a instancija | — |
| `instancija` | `"Apeliacinė instancija"` | — | — | Apeliacinė instancija | — |
| `instancija` | `"Kasacinė instancija"` | — | — | Kasacinė instancija | — |
| `instancija` | `"Vienintelė instancija"` | — | — | Vienintelė instancija | — |
| `tipas` | `"administracinė byla"` | — | — | Administracinė byla | — |
| `tipas` | `"civilinė byla"` | — | — | Civilinė byla | — |
| `tipas` | `"baudžiamoji byla"` | — | — | Baudžiamoji byla | — |
| `tipas` | `"administracinių teisės pažeidimų/administracinių nusižengimų byla"` | — | — | Administracinių teisės pažeidimų/administracinių nusižengimų byla | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `bylos_numeris` | `create(property: "byla", type: "ref", ref: "Byla")` | `property` | `4` | `open` | — | — | — |
| `bylos_numeris` | `update(property: "byla.numeris", type: "")` | `type` | `4` | `open` | `spinta: 216` | — | — |
| `tipas` | `update(property: "byla.tipas", type: "")` | `type` | `4` | `open` | `spinta: 216` | — | — |
| `potipis` | `update(property: "byla.potipis", type: "")` | `type` | `4` | `open` | `spinta: 216` | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/nta/protokolai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nta/protokolai.csv#L6)
