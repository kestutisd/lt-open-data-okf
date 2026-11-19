---
type: Table
title: "TycinisBankrotas — Duomenys apie tyčinius bankrotus"
description: "Spinta table datasets/gov/avnt/tyciniai_bankrotai/TycinisBankrotas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/avnt/tyciniai_bankrotai/TycinisBankrotas"
tags: [gov, avnt, tycinisbankrotas, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/tyciniai_bankrotai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/avnt/tyciniai_bankrotai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1334/"
    title: "data.gov.lt DCAT-AP — datasets/gov/avnt/tyciniai_bankrotai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# TycinisBankrotas — Duomenys apie tyčinius bankrotus

- **Model:** `datasets/gov/avnt/tyciniai_bankrotai/TycinisBankrotas`[^manifest]
- **Dataset:** [Duomenys apie tyčinius bankrotus](../tyciniai_bankrotai.md) (`datasets/gov/avnt/tyciniai_bankrotai`)[^manifest]
- **Manifest CSV:** [datasets/gov/avnt/tyciniai_bankrotai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/tyciniai_bankrotai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/avnt/tyciniai_bankrotai/TycinisBankrotas` (`deployed`)[^manifest]
- **Provider:** `avnt` — Audito, apskaitos, turto vertinimo ir nemokumo valdymo tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `integer` | — | `4` | `open` | — | Eilės numeris | — |
| `imones_kodas` | `string` | — | `2` | `open` | — | Įmonės kodas | — |
| `imones_pavadinimas` | `string` | — | `2` | `open` | — | Įmonės pavadinimas | — |
| `bankroto_pradzia` | `date` | `D` | `4` | `open` | — | Bankroto proceso pradžios data | — |
| `apygardos_teismas` | `string` | — | `2` | `open` | — | Apygardos teismo pavadinimas | — |
| `likvidavimo_data` | `date` | `D` | `4` | `open` | — | Likvidavimo data | — |
| `tycinis_bankrotas` | `date` | `D` | `4` | `open` | — | Pripažinti bankrotą tyčiniu data | Data, kuomet teismo sprendimu bankrotas pripažintas tyčiniu |
| `sprendimas_del_pabaigos` | `date` | `D` | `4` | `open` | — | Sprendimo dėl įmonės veiklos pabaigos data | — |
| `isregistravimo_data` | `date` | `D` | `4` | `open` | — | Įmonės išregistravimo data | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/avnt/tyciniai_bankrotai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/tyciniai_bankrotai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/avnt/tyciniai_bankrotai (https://data.gov.lt/datasets/1334/)
