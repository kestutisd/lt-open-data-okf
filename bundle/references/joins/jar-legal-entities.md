---
type: Reference
title: "JAR Legal Entities Cross-Register Join Reference (JuridinisAsmuo)"
description: "Canonical join rules for VĮ Registrų centras Legal Entities Register (rc/jar): level>=4 UUID lookups, level=3 ja_kodas keys, deregistration dates, formos_statusai, and GDPR-masked scalar codes."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo"
tags: [join, jar, rc, legal-entities]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: jar-manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/iregistruoti.csv"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/iregistruoti.csv"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: spinta-dsa
    resource: "https://atviriduomenys.readthedocs.io/latest/dsa/index.html"
    title: "Spinta DSA Foreign-Key & Access Level Specification"
    author: "team:vssa"
---

# JAR Legal Entities Cross-Register Join Reference (JuridinisAsmuo)

The **Legal Entities Register** (*Juridinių asmenų registras* — **JAR**, maintained by *VĮ Registrų centras*) is the primary organizational backbone of Lithuanian open data, anchored on [rc/jar/iregistruoti/JuridinisAsmuo](../../datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo.md) (`model.ref = ja_kodas`, `level = 4`).[^jar-manifest]

## 1. Core JAR Hub Tables & Deregistered Entities

- **Master Entity Table ([rc/jar/iregistruoti/JuridinisAsmuo](../../datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo.md)):** Contains 9-digit integer `ja_kodas`, `ja_pavadinimas`, registration date `reg_data`, **deregistration date `isreg_data`**, legal form FK `forma` -> [rc/jar/formos_statusai/Forma](../../datasets/gov/rc/jar/formos_statusai/Forma.md), legal status FK `statusas` -> [rc/jar/formos_statusai/Statusas](../../datasets/gov/rc/jar/formos_statusai/Statusas.md), and address FK `adresas`.[^jar-manifest]
- **Active vs Deregistered Scope:** There is no separate `rc/jar/isregistruoti/JuridinisAsmuo` table in `atviriduomenys/manifest`; deregistered entities either carry a populated `isreg_data` / deregistered status in [rc/jar/iregistruoti/JuridinisAsmuo](../../datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo.md) and [rc/jar/formos_statusai/Statusas](../../datasets/gov/rc/jar/formos_statusai/Statusas.md) (with reason codes in [rc/jar/kiti_atributai/IsregistravimoPriezastis](../../datasets/gov/rc/jar/kiti_atributai/IsregistravimoPriezastis.md) and tag-specific tables such as [rc/jar/isregistruotos_nvo/IsregistruotaNVO](../../datasets/gov/rc/jar/isregistruotos_nvo/IsregistruotaNVO.md)), or appear as historical unlinked codes in agency datasets (VMI, Sodra, VPT). Always use `LEFT JOIN` when enriching multi-year historical records against JAR.[^jar-manifest]

## 2. Three Join Patterns on `get.data.gov.lt`

| Foreign Column Pattern | Example Column | API Serialization & Join Method |
| --- | --- | --- |
| `type: ref`, **`level >= 4`** | [vmi/ja_mokesciai/Moketojas](../../datasets/gov/vmi/ja_mokesciai/Moketojas.md) (`mm_kodas`) | Serializes as `{"_id": "<UUID>"}` (`mm_kodas._id` in CSV) **even if `JuridinisAsmuo[ja_kodas]` is written in DSA CSV**. Step 1: query `JuridinisAsmuo?ja_kodas=188659752&select(_id,ja_kodas,ja_pavadinimas)`. Step 2: filter `?mm_kodas._id="<UUID>"`.[^spinta-dsa] |
| `type: ref`, **`level = 3`** | `ExternalRef` (`juridinis_asmuo`) | Serializes as `{"ja_kodas": 188659752}` (`juridinis_asmuo.ja_kodas` in CSV). Join directly on `ja_kodas`.[^spinta-dsa] |
| Scalar `string` / `integer` (`level <= 2` or non-`ref`) | `jar_kodas`, `ja_kodas`, `imones_kodas`, `pirkejo_kodas`, `tiekejo_kodas` | Normalize whitespace and integer/string type (`CAST(TRIM(col) AS INT64)` only after regex check `^[0-9]{9}$`).[^spinta-dsa] |

## 3. GDPR Masking, Sole Proprietorships & Foreign Entities

- **GDPR Redaction (`BDAR nuasmeninimas`):** In tax, procurement, grant, and NVO/charity tables, records belonging to natural persons, sole proprietorships (*individualios įmonės* — IĮ), or partnerships (*ūkinės bendrijos* — TŪB/KŪB) frequently redact names or replace `jar_kodas` / `mm_kodas` with `NULL`, `0`, `"-"`, or anonymized placeholders.[^jar-manifest]
- **Foreign & Non-JAR Identifiers:** Public procurement (`vpt/*`) and customs/transport datasets mix 9-digit Lithuanian `ja_kodas` values with foreign registration numbers, VAT prefixes (`LT...`), or non-legal-entity registry codes (`rc/jar/ne_juridiniai_asmenys/NeJuridinisAsmuo`). Never blindly cast `string` organization code columns to integer without filtering to 9-digit numeric codes.[^jar-manifest][^spinta-dsa]

- See also: [Spinta DSA & API Reference](../spinta-dsa-guide.md) and [AR Address Hierarchy Reference](ar-address-hierarchy.md).

[^jar-manifest]: atviriduomenys/manifest — `datasets/gov/rc/jar/iregistruoti.csv` (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/iregistruoti.csv)
[^spinta-dsa]: Spinta DSA Foreign-Key & Access Level Specification (https://atviriduomenys.readthedocs.io/latest/dsa/index.html)
