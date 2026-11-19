---
type: Table
title: "PrekePaslauga"
description: "Spinta table datasets/gov/mita/prekiu_paslaugos/PrekePaslauga (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/mita/prekiu_paslaugos/PrekePaslauga"
tags: [gov, mita, prekepaslauga, deployed, level-3, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/mita/prekes_paslaugos.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/mita/prekes_paslaugos.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1445/"
    title: "data.gov.lt DCAT-AP — datasets/gov/mita/prekiu_paslaugos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# PrekePaslauga

- **Model:** `datasets/gov/mita/prekiu_paslaugos/PrekePaslauga`[^manifest]
- **Dataset:** [Mokslo, inovacijų ir technologijų agentūros duomenų bazėse registruotų žinioms imlių produktų...](../prekiu_paslaugos.md) (`datasets/gov/mita/prekiu_paslaugos`)[^manifest]
- **Manifest CSV:** [datasets/gov/mita/prekes_paslaugos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/mita/prekes_paslaugos.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/mita/prekiu_paslaugos/PrekePaslauga` (`deployed`)[^manifest]
- **Provider:** `mita` — Mokslo, inovacijų ir technologijų agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `produktas` | `string` | — | `3` | `open` | — | Produkto pavadinimas | — |
| `savininkas` | `string` | — | `2` | `open` | — | Juridinio asmens pavadinimas | — |
| `jar_kodas` | `string` | — | `2` | `open` | — | Juridinio asmens kodas | — |
| `aprasymas` | `string` | — | `2` | `open` | — | Produkto aprašymas | — |
| `nuoroda` | `url` | — | `4` | `open` | — | URL nuoroda į detalų produkto aprašymą | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savininkas` | `create(property: "savininkas", type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | — | — | — | — |
| `savininkas` | `update(property: "savininkas.ja_pavadinimas", type: "")` | `property` | `2` | — | — | — | — |
| `jar_kodas` | `update(property: "savininkas.ja_kodas", type: "")` | `type` | `4` | `open` | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/mita/prekes_paslaugos.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/mita/prekes_paslaugos.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/mita/prekiu_paslaugos (https://data.gov.lt/datasets/1445/)
