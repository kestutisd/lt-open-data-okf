---
type: Dataset
title: "Leidimų kirsti mišką statistika"
description: "Leidimų kirsti mišką statistika nuo 2005 m."
resource: "https://get.data.gov.lt/datasets/gov/miskai/leidimai"
tags: [gov, miskai, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/leidimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/miskai/leidimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2121/"
    title: "data.gov.lt DCAT-AP — datasets/gov/miskai/leidimai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Leidimų kirsti mišką statistika

- **Namespace:** `datasets/gov/miskai/leidimai`[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/leidimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/leidimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/leidimai` (`deployed`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `10` (10 lentelių)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2121/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė miškų tarnyba[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/miskai/leidimai`[^dcat]
- **Portal Title (`@lt`):** Leidimų kirsti mišką statistika[^dcat]
- **Portal Title (`@en`):** Statistics of logging permits[^dcat]
- **Issued (`dct:issued`):** `2023-08-21`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2022-12-22` .. `2024-02-27`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Leidimų kirsti mišką statistika nuo 2005 m.[^dcat]

### Portal Description (`@en`)

Statistics of logging permits since 2005.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [TMKPadalinys](leidimai/TMKPadalinys.md) | Teritoriniai miškų kontrolės padaliniai | `4` | — | — | `1` | — |
| [UkPriemGrupe](leidimai/UkPriemGrupe.md) | Ūkinių priemonių grupės | `4` | — | — | `1` | — |
| [STRUKPadalinys](leidimai/STRUKPadalinys.md) | Struktūriniai padaliniai | `4` | — | — | `2` | — |
| [UkinePriemone](leidimai/UkinePriemone.md) | Ūkinės priemonės | `4` | — | — | `2` | — |
| [Uredija](leidimai/Uredija.md) | Urėdijos | `4` | — | — | `1` | — |
| [UrGir](leidimai/UrGir.md) | Girininkijos | `4` | — | — | `2` | — |
| [Leidimas](leidimai/Leidimas.md) | Leidimai kirsti mišką | `4` | — | — | `7` | — |
| [LeidSklypas](leidimai/LeidSklypas.md) | Sklypai, kuriems išduotas leidimas | `4` | — | — | `4` | — |
| [PasikLeidimas](leidimai/PasikLeidimas.md) | Išduoti leidimai | `4` | — | — | `2` | — |
| [PasikSklypas](leidimai/PasikSklypas.md) | Išduotų leidimų sklypai | `4` | — | — | `3` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/leidimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/leidimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/miskai/leidimai (https://data.gov.lt/datasets/2121/)
