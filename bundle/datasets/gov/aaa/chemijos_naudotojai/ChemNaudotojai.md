---
type: Table
title: "ChemNaudotojai — Asmenys"
description: "Spinta table datasets/gov/aaa/chemijos_naudotojai/ChemNaudotojai (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/chemijos_naudotojai/ChemNaudotojai"
tags: [gov, aaa, chemnaudotojai, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/chemijos_naudotojai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/aaa/chemijos_naudotojai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1559/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/chemijos_naudotojai"
    author: "team:vda"
    last_modified: "2026-02-25T00:00:00Z"
---

# ChemNaudotojai — Asmenys

- **Model:** `datasets/gov/aaa/chemijos_naudotojai/ChemNaudotojai`[^manifest]
- **Dataset:** [Juridiniai ir fiziniai asmenys savo ūkinėje ar pramoninėje veikloje naudojantys chemines...](../chemijos_naudotojai.md) (`datasets/gov/aaa/chemijos_naudotojai`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/chemijos_naudotojai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/chemijos_naudotojai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/chemijos_naudotojai/ChemNaudotojai` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-02-25`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eilės nr. | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Įmonės kodas | — |
| `metai` | `integer` | — | `4` | `open` | — | Dokumento (ataskaitos) atsiskaitymo metai | Nuo 2017 m. |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `jar_kodas` | `create(property: "imone", type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | — | — | — | — |
| `jar_kodas` | `update(property: "imone.ja_kodas", type: "")` | `property` | `4` | — | — | — | — |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/chemijos_naudotojai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/chemijos_naudotojai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/chemijos_naudotojai (https://data.gov.lt/datasets/1559/)
