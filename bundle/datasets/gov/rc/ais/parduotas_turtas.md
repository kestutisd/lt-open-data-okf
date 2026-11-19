---
type: Dataset
title: "Aukcionuose ir elektroninėse varžytynėse parduoto turto duomenys iš AIS"
description: "Aukcionuose ir elektroninėse varžytynėse parduoto turto duomenys iš AIS (pagal rūšį parduoto turto vertė, pagal rūšį parduoto nekilnojamojo turto vertė, parduoto nekilnojamojo turto vieta (savivaldybė)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/parduotas_turtas"
tags: [gov, rc, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/parduotas_turtas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/parduotas_turtas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2180/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ais/parduotas_turtas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Aukcionuose ir elektroninėse varžytynėse parduoto turto duomenys iš AIS

Aukcionuose ir elektroninėse varžytynėse parduoto turto duomenys iš AIS (pagal rūšį parduoto turto vertė, pagal rūšį parduoto nekilnojamojo turto vertė, parduoto nekilnojamojo turto vieta (savivaldybė). Antstolių informacinės sistemos (AIS) pirminiai duomenys (RAW DATA) apie aukcionus ir elektronines varžytynes. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 3 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0[^manifest]

- **Namespace:** `datasets/gov/rc/ais/parduotas_turtas`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ais/parduotas_turtas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/parduotas_turtas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/parduotas_turtas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2180/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ais/parduotas_turtas`[^dcat]
- **Portal Title (`@lt`):** Aukcionuose ir elektroninėse varžytynėse parduoto turto duomenys iš AIS[^dcat]
- **Portal Title (`@en`):** Data of assets sold in auctions and electronic competitions from AIS[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2023-01-10` .. `2025-04-07`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Aukcionuose ir elektroninėse varžytynėse parduoto turto duomenys iš AIS (pagal rūšį parduoto turto vertė, pagal rūšį parduoto nekilnojamojo turto vertė, parduoto nekilnojamojo turto vieta (savivaldybė). Antstolių informacinės sistemos (AIS) pirminiai duomenys (RAW DATA) apie aukcionus ir elektronines varžytynes.[^dcat]

### Portal Description (`@en`)

Data of property sold in auctions and electronic tenders from AIS (value of property sold by type, value of real estate sold by type, location of real estate sold (municipality). Bailiff Information System (AIS) primary data (RAW DATA) about auctions and electronic tenders. Data geographic sample — the entire territory of the country[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [ParduotasTurtas](parduotas_turtas/ParduotasTurtas.md) | Aukcionuose ir elektroninėse varžytynėse parduoto turto duomenys iš AIS | `4` | `nr` | — | `7` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/parduotas_turtas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/parduotas_turtas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ais/parduotas_turtas (https://data.gov.lt/datasets/2180/)
