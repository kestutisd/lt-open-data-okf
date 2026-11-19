---
type: Table
title: "PosedisTvarkarastis"
description: "Spinta table datasets/gov/nta/posedziai/PosedisTvarkarastis (15 columns)."
tags: [gov, nta, posedistvarkarastis, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nta/posedziai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/nta/posedziai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# PosedisTvarkarastis

- **Model:** `datasets/gov/nta/posedziai/PosedisTvarkarastis`[^manifest]
- **Dataset:** [datasets/gov/nta/posedziai](../posedziai.md) (`datasets/gov/nta/posedziai`)[^manifest]
- **Manifest CSV:** [datasets/gov/nta/posedziai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nta/posedziai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `nta` — Nacionalinė teismų administracija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `teismo_rumai` | `ref` | [JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) (`level=4 UUID` via `JuridinisAsmuo[ja_pavadinimas]`: `teismo_rumai._id`) | `4` | `open` | — | Teismo rūmai | — |
| `sale` | `string` | — | `3` | `open` | — | Teismo rūmų salė | — |
| `data_laikas` | `datetime` | `S` | `4` | `open` | — | Posėdžio data ir laikas | — |
| `bylos_numeris` | `string` | — | `2` | `open` | — | Bylos numeris | — |
| `procesinis_numeris` | `string` | — | `3` | `open` | — | Procesinis numeris | — |
| `esme` | `string` | — | `3` | `open` | — | Posėdžio tikslas | — |
| `id` | `string` | — | `4` | `open` | — | Posėdžio ID | — |
| `ar_uzdaras_posedis` | `string` | — | `4` | `open` | — | Uždaras/Neuždaras posėdis | — |
| `instancija` | `string` | — | `4` | `open` | — | Instancija | — |
| `bylos_id` | `string` | — | `2` | `open` | — | Bylos ID | — |
| `kolegija` | `string` | — | `3` | `public` | — | Kolegija | — |
| `tipas` | `string` | — | `2` | `open` | — | Bylos tipas | — |
| `procesas` | `string` | — | `4` | `open` | — | — | — |
| `rezultatas` | `string` | — | `3` | `open` | — | — | — |
| `ar_nuotolinis` | `string` | — | `4` | `open` | — | — | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ar_uzdaras_posedis` | `"ne"` | — | — | Neuždaras | — |
| `ar_uzdaras_posedis` | `"taip"` | — | — | Uždaras | — |
| `instancija` | `"I-a instancija"` | — | — | I-a instancija | — |
| `instancija` | `"Apeliacinė instancija"` | — | — | Apeliacinė instancija | — |
| `instancija` | `"Kasacinė instancija"` | — | — | Kasacinė instancija | — |
| `instancija` | `"Vienintelė instancija"` | — | — | Vienintelė instancija | — |
| `tipas` | `"administracinė byla"` | — | — | Administracinė byla | — |
| `tipas` | `"civilinė byla"` | — | — | Civilinė byla | — |
| `tipas` | `"baudžiamoji byla"` | — | — | Baudžiamoji byla | — |
| `tipas` | `"administracinių nusižengimų byla"` | — | — | Administracinių nusižengimų byla | — |
| `tipas` | `"Dėl bylos teisingumo (specialioji kolegija)"` | — | — | Dėl bylos teisingumo (specialioji kolegija) | — |
| `procesas` | `"rašytinis"` | — | — | Rašytinis procesas | — |
| `procesas` | `"žodinis"` | — | — | Žodinis procesas | — |
| `ar_nuotolinis` | `"ne"` | — | — | Ne nuotolinis | — |
| `ar_nuotolinis` | `"taip"` | — | — | Nuotolinis | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `bylos_numeris` | `update(property: "byla.numeris", type: "")` | `type` | `4` | `open` | `spinta: 216` | — | — |
| `bylos_id` | `create(property: "byla", type: "ref", ref: "Byla")` | `property` | `4` | `open` | — | — | — |
| `bylos_id` | `update(property: "byla.id", type: "")` | `type` | `4` | `open` | `spinta: 216` | — | — |
| `tipas` | `update(property: "byla.tipas", type: "")` | `type` | `4` | `open` | `spinta: 216` | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/nta/posedziai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nta/posedziai.csv#L6)
