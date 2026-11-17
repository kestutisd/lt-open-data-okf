---
type: Dataset
title: "Muitinės importo ir eksporto deklaracijų duomenys ir deklaracijų prašomų įforminti procedūrų klasifikatorius"
description: "Muitinės importo ir eksporto (reeksporto) deklaracijų prekių rūšių lygio duomenys su prašomų įforminti procedūrų klasifikatoriumi"
resource: "https://get.data.gov.lt/datasets/gov/muitine/deklaraciju_apdorojimo_sistema"
tags: [gov, muitine, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Muitinės importo ir eksporto deklaracijų duomenys ir deklaracijų prašomų įforminti procedūrų klasifikatorius

Muitinės importo ir eksporto (reeksporto) deklaracijų prekių rūšių lygio duomenys su prašomų įforminti procedūrų klasifikatoriumi

- **Namespace:** `datasets/gov/muitine/deklaraciju_apdorojimo_sistema`[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/deklaraciju_apdorojimo_sistema`
- **Parent Namespace (`ns`):** Muitinės departamentas prie LR FM (`datasets/gov/muitine`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Deklaracija](deklaraciju_apdorojimo_sistema/Deklaracija.md) | Muitinės importo ir eksporto deklaracijų duomenys | `4` | `vda_prime_key` | — | 19 | Muitinės importo ir eksporto (reeksporto) deklaracijų prekių rūšių lygio duomenys |
| [Procedura](deklaraciju_apdorojimo_sistema/Procedura.md) | Prašomos įforminti procedūros aprašymai pagal kodus | `4` | `vda_prime_key` | — | 8 | Prašomos įforminti procedūros aprašymų klasifikatorius pagal kodus, naudojamas muitinės deklaracijų duomenyse nurodytoms procedūroms aprašyti |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv
