---
type: Table
title: "Dalyvis — Juridinių asmenų dalyvių duomenys iš JADIS"
description: "Juridinių asmenų dalyvių informacinės sistemos (JADIS) duomenys apie juridinių asmenų dalyvius, t."
resource: "https://get.data.gov.lt/datasets/gov/rc/jadis/dalyviai/Dalyvis"
tags: [gov, rc, dalyvis, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/dalyviai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/jadis/dalyviai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1732/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jadis/dalyviai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Dalyvis — Juridinių asmenų dalyvių duomenys iš JADIS

**Dataset Context:** Juridinių asmenų dalyvių informacinės sistemos (JADIS) duomenys apie juridinių asmenų dalyvius, t. y. juridinių asmenų sudėtį iš fizinių ir juridinių asmenų[^manifest]

- **Model:** `datasets/gov/rc/jadis/dalyviai/Dalyvis`[^manifest]
- **Dataset:** [Juridinių asmenų dalyvių duomenys iš JADIS](../dalyviai.md) (`datasets/gov/rc/jadis/dalyviai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jadis/dalyviai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/dalyviai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jadis/dalyviai/Dalyvis` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `juridinis_asmuo`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [JuridinisAsmuo](../../jar/iregistruoti/JuridinisAsmuo.md) (`level=4 UUID`: `juridinis_asmuo._id`) | `4` | `open` | — | Juridinio asmuo iš Juridinių asmenų registro | — |
| `form_kodas` | `ref` | [Forma](../../jar/formos_statusai/Forma.md) (`level=4 UUID`: `form_kodas._id`) | `4` | `open` | — | Juridinio asmens teisinė forma iš Juridinių asmenų registro | — |
| `stat_statusas` | `ref` | [Statusas](../../jar/formos_statusai/Statusas.md) (`level=4 UUID`: `stat_statusas._id`) | `4` | `open` | — | Juridinio asmens teisinis statusas iš Juridinių asmenų registro | — |
| `lr_fiziniai` | `integer` | `U` | `4` | `open` | — | Juridiniame asmenyje dalyvaujančių Lietuvos Respublikos piliečių skaičius | — |
| `lr_juridiniai` | `integer` | `U` | `4` | `open` | — | Juridiniame asmenyje dalyvaujančių Lietuvos Respublikoje įregistruotų juridinių asmenų skaičius | — |
| `uzsienio_fiziniai` | `integer` | `U` | `4` | `open` | — | Juridiniame asmenyje dalyvaujančių užsienio fizinių asmenų skaičius | — |
| `uzsienio_juridiniai` | `integer` | `U` | `4` | `open` | — | Juridiniame asmenyje dalyvaujančių užsienio juridinių asmenų skaičius | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jadis/dalyviai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/dalyviai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jadis/dalyviai (https://data.gov.lt/datasets/1732/)
