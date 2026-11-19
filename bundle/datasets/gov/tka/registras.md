---
type: Dataset
title: "Civilinių orlaivių registro duomenys"
description: "Rinkinyje pateikiami duomenys registruotus ir jau išregistruotus civilnius orlaivius Lietuvos Respublikoje."
resource: "https://get.data.gov.lt/datasets/gov/tka/registras"
tags: [gov, tka, deployed, cadence-annual_3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tka/cor.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/tka/cor.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2735/"
    title: "data.gov.lt DCAT-AP — datasets/gov/tka/registras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Civilinių orlaivių registro duomenys

Rinkinyje pateikiami duomenys registruotus ir jau išregistruotus civilnius orlaivius Lietuvos Respublikoje. Duomenys apima laikotarpį nuo 1991m. iki šių dienų. Nurodoma orlaivio kategorija, rūšis, tipas, keleivių skaičius, maksimali pakilimo masė, oro sraigto tipas, orlaivio bazė ir jos adresas. Papildomai taip pat nurodyti orlaivio savininko ir naudotojo tipai.[^manifest]

- **Namespace:** `datasets/gov/tka/registras`[^manifest]
- **Manifest CSV:** [datasets/gov/tka/cor.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tka/cor.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/tka/registras` (`deployed`)[^manifest]
- **Provider:** `tka` — VšĮ Transporto kompetencijų agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2735/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/tka/registras`[^dcat]
- **Portal Title (`@lt`):** Civilinių orlaivių registro duomenys[^dcat]
- **Portal Title (`@en`):** Civil Aircraft Register Data[^dcat]
- **Issued (`dct:issued`):** `2024-08-13`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL_3` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL_3`)[^dcat]
- **Distribution Date Span:** `2026-03-31` .. `2026-04-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami VšĮ Transporto kompetencijų agentūros duomenys apie registruotus ir jau išregistruotus civilinius orlaivius Lietuvos Respublikoje. Duomenys apima laikotarpį nuo 1991 m. iki šių dienų. Nurodoma orlaivio kategorija, rūšis, tipas, keleivių skaičius, maksimali pakilimo masė, oro sraigto tipas, orlaivio bazė ir jos adresas. Papildomai taip pat nurodyti orlaivio savininko ir naudotojo tipai. Duomenų teikėjas – VšĮ Transporto kompetencijų agentūra. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package contains data of the Public Enterprise Transport Competences Agency on registered and already deregistered civil aircraft in the Republic of Lithuania. The data cover the period 1991 to the present day. Specify the category, type, type, number of passengers, maximum take-off mass, type of air screw, base and address of the aircraft. In addition, the types of aircraft owner and operator are specified. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Irasas](registras/Irasas.md) | Civilinių orlaivių registro duomenys | `4` | `vda_id` | — | `19` | Rinkinyje pateikiami duomenys registruotus ir jau išregistruotus civilnius orlaivius Lietuvos Respublikoje. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/tka/cor.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tka/cor.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/tka/registras (https://data.gov.lt/datasets/2735/)
