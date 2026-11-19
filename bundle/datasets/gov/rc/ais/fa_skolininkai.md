---
type: Dataset
title: "Antstolių informacinės sistemos (AIS) duomenys apie skolininkus fizinius asmenis"
description: "AIS duomenys apie skolininkus fizinius asmenis (pagal gyvenamosios vietos savivaldybes, išieškojimo dalyką, išieškotina sumą, bylų kiekį)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/fa_skolininkai"
tags: [gov, rc, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/fa_skolininkai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/fa_skolininkai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2172/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ais/fa_skolininkai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Antstolių informacinės sistemos (AIS) duomenys apie skolininkus fizinius asmenis

AIS duomenys apie skolininkus fizinius asmenis (pagal gyvenamosios vietos savivaldybes, išieškojimo dalyką, išieškotina sumą, bylų kiekį). Antstolių informacinės sistemos (AIS) pirminiai duomenys (RAW DATA) apie skolininkus. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 3 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0[^manifest]

- **Namespace:** `datasets/gov/rc/ais/fa_skolininkai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ais/fa_skolininkai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/fa_skolininkai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/fa_skolininkai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2172/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ais/fa_skolininkai`[^dcat]
- **Portal Title (`@lt`):** Antstolių informacinės sistemos (AIS) duomenys apie skolininkus fizinius asmenis[^dcat]
- **Portal Title (`@en`):** Bailiffs Information System (AIS) data on natural persons debtors[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2023-01-09` .. `2025-09-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

AIS duomenys apie skolininkus fizinius asmenis (pagal gyvenamosios vietos savivaldybes, išieškojimo dalyką, išieškotina sumą, bylų kiekį). Antstolių informacinės sistemos (AIS) pirminiai duomenys (RAW DATA) apie skolininkus.[^dcat]

### Portal Description (`@en`)

AIS data on natural persons debtors (by municipality of residence, subject of recovery, amount to be recovered, number of cases). Bailiffs&#39; Information System (AIS) primary data (RAW DATA) about debtors. The geographical sample of the data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [FASkolininkas](fa_skolininkai/FASkolininkas.md) | Antstolių informacinės sistemos (AIS) duomenys apie skolininkus fizinius asmenis | `4` | `nr` | — | `6` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/fa_skolininkai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/fa_skolininkai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ais/fa_skolininkai (https://data.gov.lt/datasets/2172/)
