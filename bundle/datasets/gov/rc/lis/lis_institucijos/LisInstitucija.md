---
type: Table
title: "LisInstitucija — Licencijas išduodančių institucijų klasifikatorius"
description: "Spinta table datasets/gov/rc/lis/lis_institucijos/LisInstitucija (1 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/lis/lis_institucijos/LisInstitucija"
tags: [gov, rc, lisinstitucija, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_institucijos.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/lis/lis_institucijos.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1807/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/lis/lis_institucijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# LisInstitucija — Licencijas išduodančių institucijų klasifikatorius

- **Model:** `datasets/gov/rc/lis/lis_institucijos/LisInstitucija`[^manifest]
- **Dataset:** [Licencijų informacinės sistemos licencijas išduodančių institucijų klasifikatorius](../lis_institucijos.md) (`datasets/gov/rc/lis/lis_institucijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/lis/lis_institucijos.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_institucijos.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/lis/lis_institucijos/LisInstitucija` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `juridinis_asmuo`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [JuridinisAsmuo](../../jar/iregistruoti/JuridinisAsmuo.md) (`level=4 UUID`: `juridinis_asmuo._id`) | `4` | `open` | — | Licencijas išduodančios institucijos kodas | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/lis/lis_institucijos.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_institucijos.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/lis/lis_institucijos (https://data.gov.lt/datasets/1807/)
