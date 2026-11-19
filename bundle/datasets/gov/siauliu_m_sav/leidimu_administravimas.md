---
type: Dataset
title: "Šiaulių miesto savivaldybės išduoti leidimai ir jų apmokėjimai"
description: "Informacija apie Šiaulių miesto savivaldybės išduotus leidimus fiziniams ir juridiniams asmenims bei leidimų apmokėjimus"
resource: "https://get.data.gov.lt/datasets/gov/siauliu_m_sav/leidimu_administravimas"
tags: [gov, siauliu_m_sav, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/leidimu_administravimas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/siauliu_m_sav/leidimu_administravimas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2912/"
    title: "data.gov.lt DCAT-AP — datasets/gov/siauliu_m_sav/leidimu_administravimas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Šiaulių miesto savivaldybės išduoti leidimai ir jų apmokėjimai

Informacija apie Šiaulių miesto savivaldybės išduotus leidimus fiziniams ir juridiniams asmenims bei leidimų apmokėjimus[^manifest]

- **Namespace:** `datasets/gov/siauliu_m_sav/leidimu_administravimas`[^manifest]
- **Manifest CSV:** [datasets/gov/siauliu_m_sav/leidimu_administravimas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/leidimu_administravimas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/siauliu_m_sav/leidimu_administravimas` (`deployed`)[^manifest]
- **Provider:** `siauliu_m_sav` — Šiaulių miesto savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `5` (5 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2912/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/siauliu_m_sav/leidimu_administravimas`[^dcat]
- **Portal Title (`@lt`):** Šiaulių miesto savivaldybės išduoti leidimai ir jų apmokėjimai[^dcat]
- **Portal Title (`@en`):** Permits issued by Siauliai City Municipality[^dcat]
- **Issued (`dct:issued`):** `2025-01-03`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-06` .. `2026-04-06`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiama informacija apie Šiaulių miesto žemės kasimo darbų, prekybos taškų (kioskų) ir paviljonų bei lauko mažmeninės prekybos leidimus, išduotus fiziniams ir juridiniams asmenims, Šiaulių miesto savivaldybės reklamų leidimus ir reklamų įrenginių vietas bei fizinių ir juridinių asmenų kasmetinius apmokėjimus į valstybės biudžetą už Šiaulių miesto savivaldybės išduodamus leidimus. Į rinkinį įtraukta nuo 2023 m. išduodamų žemės kasimo darbų bei prekybos leidimų, nuo 2018 m. išduodamų reklamos leidimų ir nuo 2022 m. gautų apmokėjimų informacija. Duomenų teikėjas – Šiaulių miesto savivaldybė. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data collection contains information about retail sales permits issued to natural and legal persons for advertising of Šiauliai City Municipality, excavation works of Šiauliai City Land, shopping points (kiosks) and pavilions and outdoor retail sales. The package includes information on excavation and marketing authorisations issued from 2023 onwards and on advertising authorisations issued from 2018 onwards. Data provider – Siauliai City Municipality.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Reklama](leidimu_administravimas/Reklama.md) | Šiaulių miesto savivaldybės išduoti leidimai reklamai | `4` | `leidimo_id` | — | `16` | Informacija apie Šiaulių miesto savivaldybės išduotus leidimus reklamai |
| [ZemesDarbas](leidimu_administravimas/ZemesDarbas.md) | Šiaulių miesto savivaldybės išduoti leidimai žemės darbams | `4` | `leidimo_id` | — | `18` | Informacija apie Šiaulių miesto savivaldybės išduotus leidimus žemės darbams |
| [PrekybosTaskas](leidimu_administravimas/PrekybosTaskas.md) | Šiaulių miesto savivaldybės išduoti leidimai kioskams ir pavilionams | `4` | `leidimo_id` | — | `13` | Informacija apie Šiaulių miesto savivaldybės išduotus leidimus kioskams ir pavilionams |
| [LaukoPrekyba](leidimu_administravimas/LaukoPrekyba.md) | Šiaulių miesto savivaldybės išduoti leidimai lauko mažmeninei prekybai | `4` | `leidimo_id` | — | `16` | Informacija apie Šiaulių miesto savivaldybės išduotus leidimus lauko mažmeninei prekybai |
| [LeidimuImokos](leidimu_administravimas/LeidimuImokos.md) | Įmokos už Šiaulių miesto savivaldybės išduodamus reklamos leidimus | `4` | `vda_prime_key` | — | `12` | Informacija apie imokas už Šiaulių miesto savivaldybės išduodamus reklamos leidimus |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/siauliu_m_sav/leidimu_administravimas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/leidimu_administravimas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/siauliu_m_sav/leidimu_administravimas (https://data.gov.lt/datasets/2912/)
