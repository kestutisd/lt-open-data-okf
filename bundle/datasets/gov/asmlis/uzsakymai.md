---
type: Dataset
title: "Atliekų tvarkymo užsakymų duomenys"
description: "Atliekų surinkimo, monitoringo ir logistikos informacinė sistemos (ASMLIS, MOKESTA) naudojamos atliekų tvarkymo organizavimui ir atsiskaitymui už komunalinių atliekų surinkimo ir išvežimo paslaugas."
resource: "https://get.data.gov.lt/datasets/gov/asmlis/uzsakymai"
tags: [gov, asmlis, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/uzsakymai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/asmlis/uzsakymai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2763/"
    title: "data.gov.lt DCAT-AP — datasets/gov/asmlis/uzsakymai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Atliekų tvarkymo užsakymų duomenys

Savivaldybių MOKESTA ir ASMLIS sistemų duomenys[^manifest]

- **Namespace:** `datasets/gov/asmlis/uzsakymai`[^manifest]
- **Manifest CSV:** [datasets/gov/asmlis/uzsakymai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/uzsakymai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/asmlis/uzsakymai` (`deployed`)[^manifest]
- **Provider:** `asmlis` — MOKESTA ir ASMLIS sistemos *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2763/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/asmlis/uzsakymai`[^dcat]
- **Portal Title (`@lt`):** Atliekų tvarkymo užsakymų duomenys[^dcat]
- **Portal Title (`@en`):** Waste Management Order Data[^dcat]
- **Issued (`dct:issued`):** `2024-08-30`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-10-02` .. `2025-02-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Atliekų surinkimo, monitoringo ir logistikos informacinė sistemos (ASMLIS, MOKESTA) naudojamos atliekų tvarkymo organizavimui ir atsiskaitymui už komunalinių atliekų surinkimo ir išvežimo paslaugas. Priklausomai nuo naudojančios įstaigos duomenų aprėptis gali skirtis, tačiau duomenys numatyti būti atnaujinami kasdien. Duomenų rinkinį sudaro: pateikto paslaugos užsakymo identifikatorius, adresas, data, užsakytos paslaugos veiksmas, atliekų kodas, rūšis ir nurodytos vietovės apibūdinimas. Vienas įrašas atitinka vieną pateiktą užsakymą. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Waste collection, monitoring and logistics information system (ASMLIS) used by the Marijampolė County Waste Management Centre is intended to organise waste management and settle for municipal waste collection and disposal services. The data has been compiled since 2017 and is updated on a daily basis. The dataset consists of: identifier, address, date, outsourced service action, waste code, type and description of the specified location. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Uzsakymas](uzsakymai/Uzsakymas.md) | Atliekų tvarkymo užsakymų duomenys | `4` | `vda_prime_key` | — | `16` | Atliekų surinkimo, monitoringo ir logistikos informacinė sistemos (ASMLIS, MOKESTA) naudojamos atliekų tvarkymo organizavimui ir atsiskaitymui už... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/asmlis/uzsakymai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/uzsakymai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/asmlis/uzsakymai (https://data.gov.lt/datasets/2763/)
