---
type: Dataset
title: "Ligų sąrašas (TLK-10-AM)"
description: "Ligų klasifikacija. TLK-10-AM – Tarptautinė statistinė ligų ir sveikatos sutrikimų klasifikacija, dešimtasis pataisytas ir papildytas leidimas, Australijos modifikacija (TLK-10-AM) – Sisteminis ligų sąrašas."
resource: "https://get.data.gov.lt/datasets/gov/vlk/tlk10am"
tags: [gov, vlk, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/tlk10am.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vlk/tlk10am.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1259/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/tlk10am"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Ligų sąrašas (TLK-10-AM)

- **Namespace:** `datasets/gov/vlk/tlk10am`[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/tlk10am.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/tlk10am.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/tlk10am` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1259/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė ligonių kasa prie Sveikatos apsaugos ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vlk/tlk10am`[^dcat]
- **Portal Title (`@lt`):** Ligų sąrašas (TLK-10-AM)[^dcat]
- **Portal Title (`@en`):** List of diseases (ICD-10-AM)[^dcat]
- **Issued (`dct:issued`):** `2023-06-30`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2021-11-11` .. `2025-12-05`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Ligų klasifikacija. TLK-10-AM – Tarptautinė statistinė ligų ir sveikatos sutrikimų klasifikacija, dešimtasis pataisytas ir papildytas leidimas, Australijos modifikacija (TLK-10-AM) – Sisteminis ligų sąrašas.[^dcat]

### Portal Description (`@en`)

Classification of diseases. ICD-10-AM - International Statistical Classification of Diseases and Related Disorders, Tenth Revised Edition, Australian Modification (ICD-10-AM) - Systematic List of Diseases.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Tlk10am](tlk10am/Tlk10am.md) | Ligų sąrašas (TLK-10-AM) | `4` | `ad_id` | — | `10` | Ligų klasifikacija. TLK-10-AM – Tarptautinė statistinė ligų ir sveikatos sutrikimų klasifikacija, dešimtasis pataisytas ir papildytas leidimas, Australijos... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/tlk10am.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/tlk10am.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/tlk10am (https://data.gov.lt/datasets/1259/)
