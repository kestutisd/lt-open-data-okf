---
type: Dataset
title: "Duomenys apie VVTAT klasifikatorius"
description: "Rinkinyje pateikiami duomenys apie Valstybinės vartotojų teisių apsaugos tarnybos naudojamus klasifikatorius"
resource: "https://get.data.gov.lt/datasets/gov/vvtat/klasifikatoriai"
tags: [gov, vvtat, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/klasifikatoriai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vvtat/klasifikatoriai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2682/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vvtat/klasifikatoriai"
    author: "team:vda"
    last_modified: "2026-08-17T00:00:00Z"
---

# Duomenys apie VVTAT klasifikatorius

Rinkinyje pateikiami duomenys apie Valstybinės vartotojų teisių apsaugos tarnybos naudojamus klasifikatorius[^manifest]

- **Namespace:** `datasets/gov/vvtat/klasifikatoriai`[^manifest]
- **Manifest CSV:** [datasets/gov/vvtat/klasifikatoriai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/klasifikatoriai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvtat/klasifikatoriai` (`deployed`)[^manifest]
- **Provider:** `vvtat` — Valstybinė vartotojų teisių apsaugos tarnyba *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `12` (12 lentelių)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2682/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė vartotojų teisių apsaugos tarnyba[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vvtat/klasifikatoriai/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Duomenys apie Valstybinės vartotojų teisių apsaugos tarnybos klasifikatorius[^dcat]
- **Portal Title (`@en`):** Data on LATAT classifications[^dcat]
- **Issued (`dct:issued`):** `2024-06-07`[^dcat]
- **Last Modified (`dct:modified`):** `2026-08-17`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2024-06-07` .. `2025-05-29`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@en`)

The collection contains data on classifications used by the State Consumer Rights Protection Authority[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Nenustatyta](klasifikatoriai/Nenustatyta.md) | VVTAT nenustatytų skundų priežasčių klasifikatorius | `4` | `vda_id` | — | `5` | — |
| [Nepagrista](klasifikatoriai/Nepagrista.md) | VVTAT nepagrįstų skundų priežasčių klasifikatorius | `4` | `vda_id` | — | `5` | — |
| [Priemone](klasifikatoriai/Priemone.md) | VVTAT patikrintų įmonių savanoriškų priemonių klasifikatorius | `4` | `vda_id` | — | `5` | — |
| [Rizika](klasifikatoriai/Rizika.md) | VVTAT rizikos vertinimų klasifikatorius | `4` | `vda_id` | — | `5` | — |
| [Sritis](klasifikatoriai/Sritis.md) | VVTAT taikymo sričių klasifikatorius | `4` | `vda_id` | — | `6` | — |
| [Rezultatas](klasifikatoriai/Rezultatas.md) | VVTAT tirtų skundų rezultatų klasifikatorius | `4` | `vda_id` | — | `5` | — |
| [Nusiskundimas](klasifikatoriai/Nusiskundimas.md) | VVTAT vartotojų nusiskundimo pobūdžių klasifikatorius | `4` | `kodas` | — | `4` | — |
| [Pozymis](klasifikatoriai/Pozymis.md) | VVTAT patikrinimų metu nustatytų pažeidimų požymių klasifikatorius | `4` | `vda_id` | — | `4` | — |
| [Straipsnis](klasifikatoriai/Straipsnis.md) | VVTAT Administracinių teisės pažeidimų kodekso klasifikatorius | `4` | `vda_id` | — | `6` | — |
| [Patikrinimas](klasifikatoriai/Patikrinimas.md) | VVTAT atliekamų patikrinimų klasifikatorius | `4` | `vda_id` | — | `5` | — |
| [Isvada](klasifikatoriai/Isvada.md) | VVTAT atliktų patikrinimų išvadų klasifikatorius | `4` | `vda_id` | — | `4` | — |
| [Sablonas](klasifikatoriai/Sablonas.md) | VVTAT naudojamų šablonų tipų klasifikatorius | `4` | `vda_id` | — | `5` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvtat/klasifikatoriai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/klasifikatoriai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vvtat/klasifikatoriai (https://data.gov.lt/datasets/2682/)
