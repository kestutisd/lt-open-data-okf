---
type: Table
title: "FaktoTipas — Juridinių asmenų registro faktų tipų klasifikatorius"
description: "Lietuvos Respublikos juridinių asmenų registro faktų tipų ir faktų potipių klasifikatoriai (duomenų rinkinių grupė, viso 2 vnt.) (JAR faktų tipų klasifikatorius; JAR faktų potipių klasifikatorius)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/faktu_tipai_potipiai/FaktoTipas"
tags: [gov, rc, faktotipas, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/faktu_tipai_potipiai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/faktu_tipai_potipiai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1626/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/faktu_tipai_potipiai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# FaktoTipas — Juridinių asmenų registro faktų tipų klasifikatorius

**Dataset Context:** Lietuvos Respublikos juridinių asmenų registro faktų tipų ir faktų potipių klasifikatoriai (duomenų rinkinių grupė, viso 2 vnt.) (JAR faktų tipų klasifikatorius; JAR faktų potipių klasifikatorius).[^manifest]

- **Model:** `datasets/gov/rc/jar/faktu_tipai_potipiai/FaktoTipas`[^manifest]
- **Dataset:** [Juridinių asmenų registro faktų tipų ir potipių klasifikatoriai](../faktu_tipai_potipiai.md) (`datasets/gov/rc/jar/faktu_tipai_potipiai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/faktu_tipai_potipiai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/faktu_tipai_potipiai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/faktu_tipai_potipiai/FaktoTipas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `integer` | — | `4` | `open` | — | Juridinių asmenų registro fakto tipo kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Juridinių asmenų registro fakto tipo pavadinimas | — |
| `name` | `string` | — | `3` | `open` | — | Juridinių asmenų registro fakto tipo pavadinimas anglų kalba | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/faktu_tipai_potipiai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/faktu_tipai_potipiai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/faktu_tipai_potipiai (https://data.gov.lt/datasets/1626/)
