---
type: Table
title: "NepateikesAuditoriausIsvados — Juridinių asmenų registre įregistruoto juridinio asmens kodas"
description: "Spinta table datasets/gov/rc/jar/fa_nepateike_auditoriu_isvadu/NepateikesAuditoriausIsvados (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/fa_nepateike_auditoriu_isvadu/NepateikesAuditoriausIsvados"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/fa_nepateike_auditoriu_isvadu.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/fa_nepateike_auditoriu_isvadu.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# NepateikesAuditoriausIsvados — Juridinių asmenų registre įregistruoto juridinio asmens kodas

- **Model:** `datasets/gov/rc/jar/fa_nepateike_auditoriu_isvadu/NepateikesAuditoriausIsvados`[^manifest]
- **Dataset:** [Juridiniai asmenys, nepateikę auditoriaus išvados, kai pagal įstatymus turi būti atliktas ataskaitų auditas](../fa_nepateike_auditoriu_isvadu.md) (`datasets/gov/rc/jar/fa_nepateike_auditoriu_isvadu`)
- **Manifest CSV:** [datasets/gov/rc/jar/fa_nepateike_auditoriu_isvadu.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/fa_nepateike_auditoriu_isvadu.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/fa_nepateike_auditoriu_isvadu/NepateikesAuditoriausIsvados`
- **Primary Key (`ref`):** `juridinis_asmuo`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Juridinis asmuo juridinių asmenų registre | — |
| `ja_reg_data` | `date` | `D` | `4` | `open` | — | juridinio asmens įregistravimo Juridinių asmenų registre data | — |
| `forma` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Forma](../formos_statusai/Forma.md) | `4` | `open` | — | juridinio asmens formos kodas | — |
| `statusas` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Statusas](../formos_statusai/Statusas.md) | `4` | `open` | — | juridinio asmens teisinio statuso kodas | — |
| `audit_nepateikta_uz_metus` | `integer` | — | `2` | `open` | — | metai, už kuriuos metus juridinis asmuo nepateikė auditoriaus išvados | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `audit_nepateikta_uz_metus` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/fa_nepateike_auditoriu_isvadu.csv
