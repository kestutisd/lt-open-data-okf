---
type: Dataset
title: "Vilkaviškio vandenų geriamojo vandens skaitiklių parodymai"
description: "Rinkinyje pateikiami UAB „Vilkaviškio vandenys“ nuo 2004 m. kaupiami ir saugomi Vilkaviškio vandenų geriamojo vandens skaitiklių duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vilkavi_vand/skaitikliai"
tags: [gov, vilkavi_vand, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilkavi_vand/skaitliuku_parodymai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/vilkavi_vand/skaitliuku_parodymai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2841/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilkavi_vand/skaitikliai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Vilkaviškio vandenų geriamojo vandens skaitiklių parodymai

- **Namespace:** `datasets/gov/vilkavi_vand/skaitikliai`[^manifest]
- **Manifest CSV:** [datasets/gov/vilkavi_vand/skaitliuku_parodymai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilkavi_vand/skaitliuku_parodymai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilkavi_vand/skaitikliai` (`deployed`)[^manifest]
- **Provider:** `vilkavi_vand` — UAB „Vilkaviškio vandenys“ *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2841/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vilkavi_vand/skaitikliai`[^dcat]
- **Portal Title (`@lt`):** UAB „Vilkaviškio vandenys“ geriamojo vandens skaitiklių rodmenų duomenys[^dcat]
- **Portal Title (`@en`):** Reading of drinking water meters of UAB “Vilkaviškio vandenys”[^dcat]
- **Issued (`dct:issued`):** `2024-11-07`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-10-30` .. `2026-10-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami UAB „Vilkaviškio vandenys“ nuo 2004 m. kaupiami ir saugomi Vilkaviškio vandenų geriamojo vandens skaitiklių duomenys. Duomenų viena eilutė, tai vieno skaitiklio vienas rodmenų deklaravimas. Be skaitiklio rodmenų, čia galiam rasti ir deklaravimo datą, tipą bei apytikslę skaitiklio koordinatę. Pačios koordinatės suskirstytos į 1500m. x 1500m. gardeles, bei juose visi esantys taškai sudėti į apatinį dešinį gardelės kampą. Duomenų teikėjas – UAB „Vilkaviškio vandenys“. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

“Vilkaviškis vandenys” UAB has been compiled and stored in the Vilkaviškis since 2004. A single row of data is a single reading declaration for one meter. In addition to the meter readings, here we can also find the date, type and approximate coordinates of the counter. The coordinates themselves are divided into 1500 m x 1500 m cells, and all the points in them are placed in the lower right corner of the cell. Technical questions or possible errors may be referred to the atverimas@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Parodymas](skaitikliai/Parodymas.md) | Vilkaviškio vandenų geriamojo vandens skaitiklių parodymai | `4` | `vda_prime_key` | — | `15` | Rinkinyje pateikiami UAB „Vilkaviškio vandenys“ nuo 2004 m. kaupiami ir saugomi Vilkaviškio vandenų geriamojo vandens skaitiklių duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilkavi_vand/skaitliuku_parodymai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilkavi_vand/skaitliuku_parodymai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilkavi_vand/skaitikliai (https://data.gov.lt/datasets/2841/)
