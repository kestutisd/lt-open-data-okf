---
type: Dataset
title: "Antstolių informacinės sistemos (AIS) duomenys apie antstolių vykdomas bylas – I"
description: "AIS duomenys apie antstolių vykdomas bylas – I (pagal skolininko gyvenamą teritoriją, išieškojimo dalyką, bylų skaičių, išieškotina sumą)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/bylos_i"
tags: [gov, rc, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/bylos_i.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/bylos_i.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2169/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ais/bylos_i"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Antstolių informacinės sistemos (AIS) duomenys apie antstolių vykdomas bylas – I

AIS duomenys apie antstolių vykdomas bylas – I (pagal skolininko gyvenamą teritoriją, išieškojimo dalyką, bylų skaičių, išieškotina sumą). Antstolių informacinės sistemos (AIS) pirminiai duomenys (RAW DATA) apie antstolių vykdomas bylas. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 3 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0[^manifest]

- **Namespace:** `datasets/gov/rc/ais/bylos_i`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ais/bylos_i.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/bylos_i.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/bylos_i` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2169/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ais/bylos_i`[^dcat]
- **Portal Title (`@lt`):** Antstolių informacinės sistemos (AIS) duomenys apie antstolių vykdomas bylas – I[^dcat]
- **Portal Title (`@en`):** Bailiff Information System (AIS) data on cases handled by bailiffs - I[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2023-01-09` .. `2025-09-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

AIS duomenys apie antstolių vykdomas bylas – I (pagal skolininko gyvenamą teritoriją, išieškojimo dalyką, bylų skaičių, išieškotina sumą). Antstolių informacinės sistemos (AIS) pirminiai duomenys (RAW DATA) apie antstolių vykdomas bylas.[^dcat]

### Portal Description (`@en`)

AIS data on cases conducted by bailiffs - I (according to the territory where the debtor lives, subject of recovery, number of cases, amount to be recovered). Bailiffs Information System (AIS) primary data (RAW DATA) about cases executed by bailiffs. The geographical sample of the data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [VykdomaByla](bylos_i/VykdomaByla.md) | Antstolių informacinės sistemos (AIS) duomenys apie antstolių vykdomas bylas – I | `4` | `nr` | — | `5` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/bylos_i.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/bylos_i.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ais/bylos_i (https://data.gov.lt/datasets/2169/)
