---
type: Table
title: "Pareigos — Juridinių asmenų registro pareigų klasifikatorius"
description: "Lietuvos Respublikos juridinių asmenų registro išregistravimo priežasčių ir naudojamų pareigų klasifikatoriai (duomenų rinkinių grupė, viso 2 vnt.)"
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/kiti_atributai/Pareigos"
tags: [gov, rc, pareigos, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/kiti_atributai.csv#L9"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/kiti_atributai.csv#L9"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1628/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/kiti_atributai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Pareigos — Juridinių asmenų registro pareigų klasifikatorius

**Dataset Context:** Lietuvos Respublikos juridinių asmenų registro išregistravimo priežasčių ir naudojamų pareigų klasifikatoriai (duomenų rinkinių grupė, viso 2 vnt.)[^manifest]

- **Model:** `datasets/gov/rc/jar/kiti_atributai/Pareigos`[^manifest]
- **Dataset:** [Kiti juridinių asmenų registro atributų klasifikatoriai](../kiti_atributai.md) (`datasets/gov/rc/jar/kiti_atributai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/kiti_atributai.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/kiti_atributai.csv#L9)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/kiti_atributai/Pareigos` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `integer` | — | `4` | `open` | — | Juridinių asmenų registre naudojamų pareigų kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Juridinių asmenų registre naudojamų pareigų pavadinimas | — |
| `name` | `string` | — | `3` | `open` | — | Juridinių asmenų registre naudojamų pareigų pavadinimas anglų kalba | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/kiti_atributai.csv#L9 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/kiti_atributai.csv#L9)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/kiti_atributai (https://data.gov.lt/datasets/1628/)
