---
type: Table
title: "DalyviuSarasas — Juridinių asmenų dalyvių sąrašų duomenys"
description: "Juridinių asmenų dalyvių informacinsė sistemos (JADIS) duomenys apie juridinių asmenų dalyvių sąrašus."
resource: "https://get.data.gov.lt/datasets/gov/rc/jadis/dalyviu_sarasas/DalyviuSarasas"
tags: [gov, rc, dalyviusarasas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/dalyviu_sarasas.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/jadis/dalyviu_sarasas.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1710/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jadis/dalyviu_sarasas"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# DalyviuSarasas — Juridinių asmenų dalyvių sąrašų duomenys

**Dataset Context:** Juridinių asmenų dalyvių informacinsė sistemos (JADIS) duomenys apie juridinių asmenų dalyvių sąrašus.[^manifest]

- **Model:** `datasets/gov/rc/jadis/dalyviu_sarasas/DalyviuSarasas`[^manifest]
- **Dataset:** [Juridinių asmenų dalyvių sąrašų duomenys](../dalyviu_sarasas.md) (`datasets/gov/rc/jadis/dalyviu_sarasas`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jadis/dalyviu_sarasas.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/dalyviu_sarasas.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jadis/dalyviu_sarasas/DalyviuSarasas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `juridinis_asmuo`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [JuridinisAsmuo](../../jar/iregistruoti/JuridinisAsmuo.md) (`level=4 UUID`: `juridinis_asmuo._id`) | `4` | `open` | — | Juridinio asmuo iš Juridinių asmenų registro | — |
| `forma` | `ref` | [Forma](../../jar/formos_statusai/Forma.md) (`level=4 UUID`: `forma._id`) | `4` | `open` | — | Juridinio asmens teisinė forma iš Juridinių asmenų registro | — |
| `statusas` | `ref` | [Statusas](../../jar/formos_statusai/Statusas.md) (`level=4 UUID`: `statusas._id`) | `4` | `open` | — | Juridinio asmens teisinio statusas iš Juridinių asmenų registro | — |
| `ja_reg_data` | `date` | `D` | `4` | `open` | — | Juridinio asmens įregistravimo į Juridinių asmenų registrą data | — |
| `pateikimo_poz` | `integer` | — | `4` | `open` | — | Juridinio asmens JAD sąrašo pateikimo požymis | — |
| `saraso_data` | `date` | `D` | `4` | `open` | — | Juridinio asmens JAD sąrašo pateikimo data | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pateikimo_poz` | `0` | — | — | Nepateikė | — |
| `pateikimo_poz` | `1` | — | — | Pateikė | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jadis/dalyviu_sarasas.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/dalyviu_sarasas.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jadis/dalyviu_sarasas (https://data.gov.lt/datasets/1710/)
