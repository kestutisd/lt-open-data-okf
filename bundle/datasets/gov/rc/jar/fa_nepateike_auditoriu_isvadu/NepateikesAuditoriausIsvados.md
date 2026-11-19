---
type: Table
title: "NepateikesAuditoriausIsvados — Juridinių asmenų registre įregistruoto juridinio asmens kodas"
description: "Duomenys apie nepateikusius auditoriaus išvados, kai pagal įstatymus turi būti atliktas metinių finansinių ataskaitų (metinių konsoliduotųjų finansinių ataskaitų) auditas, juridinius asmenis"
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/fa_nepateike_auditoriu_isvadu/NepateikesAuditoriausIsvados"
tags: [gov, rc, nepateikesauditoriausisvados, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/fa_nepateike_auditoriu_isvadu.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/fa_nepateike_auditoriu_isvadu.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# NepateikesAuditoriausIsvados — Juridinių asmenų registre įregistruoto juridinio asmens kodas

**Dataset Context:** Duomenys apie nepateikusius auditoriaus išvados, kai pagal įstatymus turi būti atliktas metinių finansinių ataskaitų (metinių konsoliduotųjų finansinių ataskaitų) auditas, juridinius asmenis[^manifest]

- **Model:** `datasets/gov/rc/jar/fa_nepateike_auditoriu_isvadu/NepateikesAuditoriausIsvados`[^manifest]
- **Dataset:** [Juridiniai asmenys, nepateikę auditoriaus išvados, kai pagal įstatymus turi būti atliktas...](../fa_nepateike_auditoriu_isvadu.md) (`datasets/gov/rc/jar/fa_nepateike_auditoriu_isvadu`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/fa_nepateike_auditoriu_isvadu.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/fa_nepateike_auditoriu_isvadu.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/fa_nepateike_auditoriu_isvadu/NepateikesAuditoriausIsvados` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `juridinis_asmuo`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [JuridinisAsmuo](../iregistruoti/JuridinisAsmuo.md) (`level=4 UUID`: `juridinis_asmuo._id`) | `4` | `open` | — | Juridinis asmuo juridinių asmenų registre | — |
| `ja_reg_data` | `date` | `D` | `4` | `open` | — | juridinio asmens įregistravimo Juridinių asmenų registre data | — |
| `forma` | `ref` | [Forma](../formos_statusai/Forma.md) (`level=4 UUID`: `forma._id`) | `4` | `open` | — | juridinio asmens formos kodas | — |
| `statusas` | `ref` | [Statusas](../formos_statusai/Statusas.md) (`level=4 UUID`: `statusas._id`) | `4` | `open` | — | juridinio asmens teisinio statuso kodas | — |
| `audit_nepateikta_uz_metus` | `integer` | — | `2` | `open` | — | metai, už kuriuos metus juridinis asmuo nepateikė auditoriaus išvados | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `audit_nepateikta_uz_metus` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/fa_nepateike_auditoriu_isvadu.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/fa_nepateike_auditoriu_isvadu.csv#L5)
