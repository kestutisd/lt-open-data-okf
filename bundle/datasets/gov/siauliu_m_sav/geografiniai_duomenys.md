---
type: Dataset
title: "Šiaulių miesto savivaldybės geografiniai duomenys"
description: "Geografinėje informacinėje sistemoje ArcGis kaupiami geografiniai Šiaulių miesto savivaldybės duomenys."
resource: "https://get.data.gov.lt/datasets/gov/siauliu_m_sav/geografiniai_duomenys"
tags: [gov, siauliu_m_sav, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2895/"
    title: "data.gov.lt DCAT-AP — datasets/gov/siauliu_m_sav/geografiniai_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Šiaulių miesto savivaldybės geografiniai duomenys

Geografinėje informacinėje sistemoje ArcGis kaupiami geografiniai Šiaulių miesto savivaldybės duomenys. Rinkinyje pateikiami šiuo metu aktualūs seniūnaitijų ribų bei sporto vietų duomenys. Tarp sporto vietų duomenų pateikiami ir atsakingų asmenų kontaktai, kurių pagalba galima rezervuoti aikštę, salę ir kt. Duomenų teikėjas – Šiaulių miesto savivaldybės administracija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/siauliu_m_sav/geografiniai_duomenys`[^manifest]
- **Manifest CSV:** [datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/siauliu_m_sav/geografiniai_duomenys` (`deployed`)[^manifest]
- **Provider:** `siauliu_m_sav` — Šiaulių miesto savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2895/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/siauliu_m_sav/geografiniai_duomenys`[^dcat]
- **Portal Title (`@lt`):** Šiaulių miesto savivaldybės seniūnaitijos ir savivaldybėje esančios sporto vietos[^dcat]
- **Portal Title (`@en`):** Neighborhoods of Šiauliai City Municipality and sports venues located in the municipality[^dcat]
- **Issued (`dct:issued`):** `2024-12-11`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-12-11` .. `2026-10-11`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Geografinėje informacinėje sistemoje ArcGis kaupiami geografiniai Šiaulių miesto savivaldybės duomenys. Rinkinyje pateikiami šiuo metu aktualūs seniūnaitijų ribų bei sporto vietų duomenys. Tarp sporto vietų duomenų pateikiami ir atsakingų asmenų kontaktai, kurių pagalba galima rezervuoti aikštę, salę ir kt. Duomenų teikėjas – Šiaulių miesto savivaldybės administracija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The geographical information system ArcGis accumulates geographical data of the city municipality of Šiauliai. The collection provides current data on the boundaries of elders and sports venues. The details of sports venues shall include contact between the persons responsible, through which the square, hall, etc. can be reserved. Data provider – administration of Šiauliai City Municipality. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SportoVieta](geografiniai_duomenys/SportoVieta.md) | Šiaulių miesto savivaldybės sporto vietos | `4` | `vda_prime_key` | — | `13` | Geografinėje informacinėje sistemoje ArcGis kaupiami geografiniai Šiaulių miesto savivaldybės duomenys. |
| [Seniunaitijos](geografiniai_duomenys/Seniunaitijos.md) | Šiaulių miesto savivaldybės seniūnaitijos | `4` | `vda_prime_key` | — | `6` | Geografinėje informacinėje sistemoje ArcGis kaupiami geografiniai Šiaulių miesto savivaldybės duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/siauliu_m_sav/geografiniai_duomenys (https://data.gov.lt/datasets/2895/)
