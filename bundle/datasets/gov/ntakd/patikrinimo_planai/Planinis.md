---
type: Table
title: "Planinis — Metiniai planinių patikrinimų planai"
description: "Spinta table datasets/gov/ntakd/patikrinimo_planai/Planinis (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ntakd/patikrinimo_planai/Planinis"
tags: [gov, ntakd, planinis, deployed, level-4, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/patikrinimo_planai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/ntakd/patikrinimo_planai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1371/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ntakd/patikrinimo_planai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Planinis — Metiniai planinių patikrinimų planai

- **Model:** `datasets/gov/ntakd/patikrinimo_planai/Planinis`[^manifest]
- **Dataset:** [Ūkio subjektų besiverčiančių alkoholio ir tabako gaminių didmenine ir mažmenine prekyba metiniai...](../patikrinimo_planai.md) (`datasets/gov/ntakd/patikrinimo_planai`)[^manifest]
- **Manifest CSV:** [datasets/gov/ntakd/patikrinimo_planai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/patikrinimo_planai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ntakd/patikrinimo_planai/Planinis` (`deployed`)[^manifest]
- **Provider:** `ntakd` — Narkotikų, tabako ir alkoholio kontrolės departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `eil_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_2`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `integer` | — | `4` | `open` | — | Eilės numeris | — |
| `ukio_subj_pav` | `ref` | [JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) (`level=2` scalar) | `2` | `open` | — | Ūkio subjekto pavadinimas | — |
| `ukio_subj_kodas` | `ref` | [JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) (`level=3`: `ukio_subj_kodas.ja_kodas`) | `3` | `open` | — | Ūkio subjekto kodas | — |
| `ukio_subj_adresas` | `string` | — | `2` | `open` | — | Ūkio subjekto adresas | — |
| `licencija` | `string` | — | `2` | `open` | — | Licencijos numeris | — |
| `veikla` | `string` | — | `3` | `open` | — | Ūkinės veiklos rūšis | — |
| `sandelio_prek_adresas` | `string` | — | `2` | `open` | — | Numatomo tikrinti sandėlio ar prekybos vietos adresas | — |
| `patikr_terminas` | `string` | — | `2` | `open` | — | Patikrinimo terminas ketvirčiais | — |
| `pastabos` | `string` | — | `2` | `open` | — | Pastabos | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/ntakd/patikrinimo_planai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/patikrinimo_planai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ntakd/patikrinimo_planai (https://data.gov.lt/datasets/1371/)
