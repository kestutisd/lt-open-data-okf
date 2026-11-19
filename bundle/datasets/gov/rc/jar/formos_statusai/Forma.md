---
type: Table
title: "Forma — Juridinių asmenų registro teisinių formų klasifikatorius"
description: "Lietuvos Respublikos juridinių asmenų registro teisinių formų ir teisinių statusų klasifikatoriai (duomenų rinkinių grupė, viso 2vnt.) (JAR teisinių formų klasifikatorius; JAR teisinių statusų klasifikatorius)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/formos_statusai/Forma"
tags: [gov, rc, forma, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/formos_statusai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/formos_statusai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1624/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/formos_statusai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Forma — Juridinių asmenų registro teisinių formų klasifikatorius

**Dataset Context:** Lietuvos Respublikos juridinių asmenų registro teisinių formų ir teisinių statusų klasifikatoriai (duomenų rinkinių grupė, viso 2vnt.) (JAR teisinių formų klasifikatorius; JAR teisinių statusų klasifikatorius).[^manifest]

- **Model:** `datasets/gov/rc/jar/formos_statusai/Forma`[^manifest]
- **Dataset:** [Juridinių asmenų registro teisinių formų ir statusų klasifikatoriai](../formos_statusai.md) (`datasets/gov/rc/jar/formos_statusai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/formos_statusai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/formos_statusai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/formos_statusai/Forma` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `integer` | — | `4` | `open` | — | Juridinio asmens formos kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Juridinio asmens formos pavadinimas | — |
| `pav_ilgas` | `string` | — | `3` | `open` | — | Juridinio asmens formos ilgasis pavadinimas | — |
| `name` | `string` | — | `3` | `open` | — | Juridinio asmens formos pavadinimas anglų kalba | — |
| `tipas` | `string` | — | `4` | `open` | — | Juridinio asmens formos tipas | — |
| `type` | `string` | — | `4` | `open` | — | Juridinio asmens formos tipas anglų kalba | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"privatus"` | — | — | Privatus | — |
| `tipas` | `"viešasis"` | — | — | Viešasis | — |
| `type` | `"private"` | — | — | Private | — |
| `type` | `"public"` | — | — | Public | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/formos_statusai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/formos_statusai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/formos_statusai (https://data.gov.lt/datasets/1624/)
