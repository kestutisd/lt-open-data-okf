---
type: Dataset
title: "Prisirašiusių prie pirminės ambulatorinės asmens sveikatos priežiūros paslaugas teikiančių įstaigų asmenų skaičius"
description: "Informacija apie prisirašiusių prie pirminės ambulatorinės asmens sveikatos priežiūros paslaugas teikiančių įstaigų asmenų skaičių"
resource: "https://get.data.gov.lt/datasets/gov/vlk/prisirase"
tags: [gov, vlk, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/prisirase.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vlk/prisirase.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1586/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/prisirase"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Prisirašiusių prie pirminės ambulatorinės asmens sveikatos priežiūros paslaugas teikiančių įstaigų asmenų skaičius

- **Namespace:** `datasets/gov/vlk/prisirase`[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/prisirase.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/prisirase.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/prisirase` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1586/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė ligonių kasa prie Sveikatos apsaugos ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vlk/prisirase`[^dcat]
- **Portal Title (`@lt`):** Prisirašiusių prie pirminės ambulatorinės asmens sveikatos priežiūros paslaugas teikiančių įstaigų asmenų skaičius[^dcat]
- **Portal Title (`@en`):** Number of signatories[^dcat]
- **Issued (`dct:issued`):** `2023-09-18`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2023-01-12` .. `2026-01-18`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Informacija apie prisirašiusių prie pirminės ambulatorinės asmens sveikatos priežiūros paslaugas teikiančių įstaigų asmenų skaičių[^dcat]

### Portal Description (`@en`)

Number of signatories[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PrisirasesPaasp](prisirase/PrisirasesPaasp.md) | Prisirašiusių prie PAASP asmenų skaičius | `4` | `ad_id` | — | `11` | Informacija apie prisirašiusių prie pirminės ambulatorinės asmens sveikatos priežiūros paslaugas teikiančių įstaigų asmenų skaičių |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/prisirase.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/prisirase.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/prisirase (https://data.gov.lt/datasets/1586/)
