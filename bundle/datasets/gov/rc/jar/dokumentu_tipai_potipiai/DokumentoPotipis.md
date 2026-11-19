---
type: Table
title: "DokumentoPotipis — Juridinių asmenų registro dokumentų potipių klasifikatorius"
description: "Lietuvos Respublikos juridinių asmenų registro dokumentų tipų ir dokumentų potipių klasifikatoriai (duomenų rinkinių grupė, viso 2 vnt.) (JAR dokumentų tipų klasifikatorius; JAR dokumentų potipių klasifikatorius)"
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/dokumentu_tipai_potipiai/DokumentoPotipis"
tags: [gov, rc, dokumentopotipis, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/dokumentu_tipai_potipiai.csv#L9"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/dokumentu_tipai_potipiai.csv#L9"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1625/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/dokumentu_tipai_potipiai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# DokumentoPotipis — Juridinių asmenų registro dokumentų potipių klasifikatorius

**Dataset Context:** Lietuvos Respublikos juridinių asmenų registro dokumentų tipų ir dokumentų potipių klasifikatoriai (duomenų rinkinių grupė, viso 2 vnt.) (JAR dokumentų tipų klasifikatorius; JAR dokumentų potipių klasifikatorius)[^manifest]

- **Model:** `datasets/gov/rc/jar/dokumentu_tipai_potipiai/DokumentoPotipis`[^manifest]
- **Dataset:** [Juridinių asmenų registro dokumentų klasifikatoriai](../dokumentu_tipai_potipiai.md) (`datasets/gov/rc/jar/dokumentu_tipai_potipiai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/dokumentu_tipai_potipiai.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/dokumentu_tipai_potipiai.csv#L9)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/dokumentu_tipai_potipiai/DokumentoPotipis` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dokumento_tipas` | `ref` | [DokumentoTipas](DokumentoTipas.md) (`level=4 UUID`: `dokumento_tipas._id`) | `4` | `open` | — | Juridinių asmenų registro dokumento tipo kodas | — |
| `kodas` | `integer` | — | `4` | `open` | — | Juridinių asmenų registro dokumento potipio kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Juridinių asmenų registro dokumento potipio pavadinimas | — |
| `name` | `string` | — | `3` | `open` | — | Juridinių asmenų registro dokumento potipio pavadinimas anglų kalba | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/dokumentu_tipai_potipiai.csv#L9 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/dokumentu_tipai_potipiai.csv#L9)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/dokumentu_tipai_potipiai (https://data.gov.lt/datasets/1625/)
