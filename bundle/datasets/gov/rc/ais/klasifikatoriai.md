---
type: Dataset
title: "AIS tipų ir potipių klasifikatoriai"
description: "AIS esančių aukcionų ir elektroninių varžytynių rūšių duomenys (paskelbta ir įvyko)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/klasifikatoriai"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/klasifikatoriai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/klasifikatoriai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2182/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ais/klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# AIS tipų ir potipių klasifikatoriai

AIS esančių aukcionų ir elektroninių varžytynių rūšių duomenys (paskelbta ir įvyko). Antstolių informacinės sistemos (AIS) pirminiai duomenys (RAW DATA) apie aukcionus ir elektronines varžytynes. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 3 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0[^manifest]

- **Namespace:** `datasets/gov/rc/ais/klasifikatoriai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ais/klasifikatoriai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/klasifikatoriai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/klasifikatoriai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2182/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ais/klasifikatoriai`[^dcat]
- **Portal Title (`@lt`):** AIS tipų ir potipių klasifikatoriai[^dcat]
- **Portal Title (`@en`):** Classifiers of AIS types and subtypes[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-01-10` .. `2025-06-03`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

AIS tipų ir potipių klasifikatoriai (duomenų rinkinių grupė, viso 4 vnt.) (AIS varžytynių ir aukcionų tipų klasifikatorius; AIS parduodamo turto tipų klasifikatorius; AIS parduodamo turto potipių klasifikatorius; AIS varžytynių ir aukcionų organizatorių klasifikatorius). Antstolių informacinės sistemos (AIS) klasifikatoriai.[^dcat]

### Portal Description (`@en`)

Classifiers of AIS types and subtypes (group of datasets, total 4 units) (Classifier of types of auctions and auctions of AIS; Classifier of types of property for sale in AIS; Classifier of subtypes of property of sale in AIS; Classifier of organizers of auctions and auctions of AIS). Bailiffs Information System (AIS) classifiers. The geographical sample of the data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [TurtoPotipis](klasifikatoriai/TurtoPotipis.md) | AIS parduodamo turto potipių klasifikatorius | — | `kodas` | — | `3` | — |
| [TurtoTipas](klasifikatoriai/TurtoTipas.md) | AIS parduodamo turto tipų klasifikatorius | — | `kodas` | — | `2` | — |
| [AukcionoOrganizatoriausTipas](klasifikatoriai/AukcionoOrganizatoriausTipas.md) | AIS elektroninių varžytynių ir aukcionų organizatorių klasifikatorius | — | `kodas` | — | `2` | — |
| [AukcionoTipas](klasifikatoriai/AukcionoTipas.md) | AIS elektroninių varžytynių ir aukcionų tipų klasifikatorius | — | `kodas` | — | `2` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/klasifikatoriai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/klasifikatoriai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ais/klasifikatoriai (https://data.gov.lt/datasets/2182/)
