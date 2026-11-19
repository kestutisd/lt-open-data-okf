---
type: Dataset
title: "Krovininių transporto priemonių rezervacijų kirsti Lietuvos Respublikos sieną statistika"
description: "Lentelėje pateikiama krovininių transporto priemonių rezervacijų kirsti Lietuvos Respublikos sieną statistika iš Pasienio kontrolės punktų direkcijos (PKPD) eilių valdymo informacinės sistemos (EVIS)."
resource: "https://get.data.gov.lt/datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika"
tags: [gov, pkpd, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3850/"
    title: "data.gov.lt DCAT-AP — datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Krovininių transporto priemonių rezervacijų kirsti Lietuvos Respublikos sieną statistika

- **Namespace:** `datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika`[^manifest]
- **Manifest CSV:** [datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika` (`deployed`)[^manifest]
- **Provider:** `pkpd` — Pasienio kontrolės punktų direkcija prie Susisiekimo ministerijos *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3850/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika`[^dcat]
- **Portal Title (`@lt`):** Krovininių transporto priemonių rezervacijų kirsti Lietuvos Respublikos sieną statistika[^dcat]
- **Portal Title (`@en`):** Statistics on the reservation of goods vehicles to cross the border of the Republic of Lithuania[^dcat]
- **Issued (`dct:issued`):** `2025-06-13`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-06-10` .. `2025-06-12`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lentelėje pateikiama krovininių transporto priemonių rezervacijų kirsti Lietuvos Respublikos sieną statistika iš Pasienio kontrolės punktų direkcijos (PKPD) eilių valdymo informacinės sistemos (EVIS). Duomenys kaupiami nuo 2013 metų ir atnaujinami kas mėnesį. Svarbu paminėti, kad lentelėje baigtų rezervacijų skaičiai apima tiek sėkmingai įgyvendintas rezervacijas (kai transporto priemonė pervažiuoja iš laukimo aikštelės į pasienio kontrolės punktą), tiek atšauktas, neįvykdytas rezervacijas. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The table provides statistics on reservations of goods vehicles to cross the border of the Republic of Lithuania from the BORDER Control Points Directorate (PKPD) Queue Management Information System (EVIS). The data has been compiled since 2013 and is updated monthly. It is important to note that the number of reservations closed in the table includes both successfully implemented reservations (when the vehicle moves from the waiting area to the border checkpoint) and cancelled, unfulfilled reservations. Technical questions or errors can be referred to the atverimas@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [RezervacijosDatai](sienos_kirtimu_rezervaciju_statistika/RezervacijosDatai.md) | Krovininių transporto priemonių rezervacijų kirsti Lietuvos Respublikos sieną statistika | `4` | `iraso_id` | — | `13` | Lentelėje pateikiama krovininių transporto priemonių rezervacijų kirsti Lietuvos Respublikos sieną statistika iš Pasienio kontrolės punktų direkcijos (PKPD)... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika (https://data.gov.lt/datasets/3850/)
