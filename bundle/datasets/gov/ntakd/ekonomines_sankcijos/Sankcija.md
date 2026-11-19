---
type: Table
title: "Sankcija — Ekonominės sankcijos"
description: "Juridinių asmenų įrašai, turintys požymius: priimtas sprendimas, apmokejimo_data"
resource: "https://get.data.gov.lt/datasets/gov/ntakd/ekonomines_sankcijos/Sankcija"
tags: [gov, ntakd, sankcija, deployed, level-4, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/ekonomines_sankcijos.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/ntakd/ekonomines_sankcijos.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1413/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ntakd/ekonomines_sankcijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Sankcija — Ekonominės sankcijos

Juridinių asmenų įrašai, turintys požymius: priimtas sprendimas, apmokejimo_data[^manifest]

- **Model:** `datasets/gov/ntakd/ekonomines_sankcijos/Sankcija`[^manifest]
- **Dataset:** [Duomenys apie ūkio subjektams taikytas ekonomines sankcijas už Alkoholio kontrolės įstatymo ir...](../ekonomines_sankcijos.md) (`datasets/gov/ntakd/ekonomines_sankcijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/ntakd/ekonomines_sankcijos.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/ekonomines_sankcijos.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ntakd/ekonomines_sankcijos/Sankcija` (`deployed`)[^manifest]
- **Provider:** `ntakd` — Narkotikų, tabako ir alkoholio kontrolės departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `eil_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_2`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eilės numeris | — |
| `pavadinimas` | `ref` | [JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) (`level=4 UUID`: `pavadinimas._id`) | `4` | `open` | — | Įmonės pavadinimas | — |
| `kodas` | `ref` | [JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) (`level=4 UUID`: `kodas._id`) | `4` | `open` | — | Įmonės kodas | — |
| `nutarimas` | `string` | — | `2` | `open` | — | Nutarimo numeris | — |
| `nutarimo_priemimas` | `date` | `D` | `4` | `open` | — | Nutarimo priėmimo data | — |
| `pazeistas_aki_tki` | `string` | — | `4` | `open` | — | Pažeistas AKĮ ar TKĮ straipsnis | — |
| `sprendimas` | `number` | — | `2` | `open` | — | Priimtas sprendimas | — |
| `ar_apmoketa` | `string` | — | `2` | `open` | — | Požymis nurodantis, ar apmokėta | — |
| `apmoketa` | `date` | `D` | `4` | `open` | — | Apmokėjimo data | — |
| `suma` | `number` | — | `2` | `open` | — | Apmokėjimo suma | — |
| `apskundimas` | `string` | — | `2` | `open` | — | Apskundimas | — |
| `vaat` | `string` | — | `2` | `open` | — | VAAT sprendimas | — |
| `lvat` | `string` | — | `2` | `open` | — | LVAT sprendimas | — |
| `antstolis` | `string` | — | `4` | `open` | — | Antstolių kontora | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sprendimas` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/ntakd/ekonomines_sankcijos.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/ekonomines_sankcijos.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ntakd/ekonomines_sankcijos (https://data.gov.lt/datasets/1413/)
