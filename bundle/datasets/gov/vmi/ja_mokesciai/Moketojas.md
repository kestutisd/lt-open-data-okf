---
type: Table
title: "Moketojas — Mokesčių mokėtojas"
description: "Juridinių asmenų sumokėti mokesčiai"
resource: "https://get.data.gov.lt/datasets/gov/vmi/ja_mokesciai/Moketojas"
tags: [gov, vmi, moketojas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/ja_sumoketi_mokesciai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/vmi/ja_sumoketi_mokesciai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/673/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/ja_mokesciai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Moketojas — Mokesčių mokėtojas

**Dataset Context:** Juridinių asmenų sumokėti mokesčiai[^manifest]

- **Model:** `datasets/gov/vmi/ja_mokesciai/Moketojas`[^manifest]
- **Dataset:** [Juridinių asmenų sumokėti mokesčiai duomenų rinkinys](../ja_mokesciai.md) (`datasets/gov/vmi/ja_mokesciai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/ja_sumoketi_mokesciai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/ja_sumoketi_mokesciai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/ja_mokesciai/Moketojas` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Mokėtojo ID VMI sistemoje | — |
| `mm_kodas` | `ref` | [JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) (`level=4 UUID`: `mm_kodas._id`) | `4` | `open` | — | Juridinio asmens kodas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Mokėtojo pavadinimas | — |
| `tipas` | `string` | — | `4` | `open` | — | Mokėtojo tipas | — |
| `apskritis` | `ref` | [Apskritis](../../rc/ar/apskritis/Apskritis.md) (`level=4 UUID`: `apskritis._id`) | `4` | `open` | — | Juridinio asmens apskritis | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Juridinio asmens savivaldybė | — |
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

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/ja_sumoketi_mokesciai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/ja_sumoketi_mokesciai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/ja_mokesciai (https://data.gov.lt/datasets/673/)
