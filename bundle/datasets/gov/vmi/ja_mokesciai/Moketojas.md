---
type: Table
title: "Moketojas — Mokesčių mokėtojas"
description: "Spinta table datasets/gov/vmi/ja_mokesciai/Moketojas (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/ja_mokesciai/Moketojas"
tags: [gov, vmi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmi/ja_sumoketi_mokesciai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/ja_sumoketi_mokesciai.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Moketojas — Mokesčių mokėtojas

- **Model:** `datasets/gov/vmi/ja_mokesciai/Moketojas`[^manifest]
- **Dataset:** [Juridinių asmenų sumokėti mokesčiai duomenų rinkinys](../ja_mokesciai.md) (`datasets/gov/vmi/ja_mokesciai`)
- **Manifest CSV:** [datasets/gov/vmi/ja_sumoketi_mokesciai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/ja_sumoketi_mokesciai.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/ja_mokesciai/Moketojas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Mokėtojo ID VMI sistemoje | — |
| `mm_kodas` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Juridinio asmens kodas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Mokėtojo pavadinimas | — |
| `tipas` | `string` | — | `4` | `open` | — | Mokėtojo tipas | — |
| `apskritis` | `ref` | [/datasets/gov/rc/ar/apskritis/Apskritis](../../rc/ar/apskritis/Apskritis.md) | `4` | `open` | — | Juridinio asmens apskritis | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Juridinio asmens savivaldybė | — |
| `praeitu_metu_suma` | `number` | — | `4` | `open` | — | Sumokėta suma praeitais metais | — |
| `einamu_metu_suma` | `number` | — | `4` | `open` | — | Sumokėta suma einamaisiais metais | — |
| `metai` | `integer` | — | `4` | `open` | — | Mokesčių mokėjimo metai | — |
| `menuo` | `integer` | — | `4` | `open` | — | Mokesčių mokėjimo mėnesis | — |
| `suma` | `number` | — | `4` | `open` | — | Sumokėta suma | — |
| `atnaujinta` | `date` | `D` | `4` | `open` | — | Įrašo atnaujinimo data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `praeitu_metu_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/ja_sumoketi_mokesciai.csv
