---
type: Dataset
title: "Paukščių ir šikšnosparnių aptikimų, žiedavimų ir biometriniai duomenys"
description: "Rinkinyje pateikti Kauno Tado Ivanausko zoologijos muziejaus Paukščių ir šikšnosparnių, žieduotų Lietuvoje, aptikimų, žiedavimų ir biometriniai duomenys iš Paukščių žiedavimo ir aptikimo duomenų bazės."
resource: "https://get.data.gov.lt/datasets/gov/ktizm/pauksciai_ir_siksnosparniai"
tags: [gov, ktizm, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2714/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ktizm/pauksciai_ir_siksnosparniai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Paukščių ir šikšnosparnių aptikimų, žiedavimų ir biometriniai duomenys

- **Namespace:** `datasets/gov/ktizm/pauksciai_ir_siksnosparniai`[^manifest]
- **Manifest CSV:** [datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ktizm/pauksciai_ir_siksnosparniai` (`deployed`)[^manifest]
- **Provider:** `ktizm` — Kauno Tado Ivanausko zoologijos muziejus *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2714/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/ktizm/pauksciai_ir_siksnosparniai`[^dcat]
- **Portal Title (`@lt`):** Paukščių ir šikšnosparnių aptikimų, žiedavimų ir biometriniai duomenys[^dcat]
- **Portal Title (`@en`):** Bird and bat detection, ringing and biometric data[^dcat]
- **Issued (`dct:issued`):** `2024-07-22`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2024-07-22` .. `2024-07-22`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikti Kauno Tado Ivanausko zoologijos muziejaus Paukščių ir šikšnosparnių, žieduotų Lietuvoje, aptikimų, žiedavimų ir biometriniai duomenys iš Paukščių žiedavimo ir aptikimo duomenų bazės. Duomenų atnaujinimas vykdomas kartą per metus. Duomenų teikėjas – Kauno Tado Ivanausko zoologijos muziejus. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The collection contains the findings, ringing and biometric data from the Birds Ring and Detection Database of the Kaunas Tado Ivanauskas Zoological Museum. The data update is carried out once a year.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PaukscioAptikimas](pauksciai_ir_siksnosparniai/PaukscioAptikimas.md) | Paukščių ir šikšnosparnių aptikimų duomenys | `4` | `iraso_id` | — | `20` | Lentelėje pateikti Kauno Tado Ivanausko zoologijos muziejaus Paukščių ir šikšnosparnių, žieduotų Lietuvoje, aptikimų duomenys iš Paukščių žiedavimo ir... |
| [PaukscioZiedavimas](pauksciai_ir_siksnosparniai/PaukscioZiedavimas.md) | Paukščių ir šikšnosparnių žiedavimo duomenys | `4` | `iraso_id` | — | `14` | Lentelėje pateikti Kauno Tado Ivanausko zoologijos muziejaus Lietuvoje atliktų paukščių ir šikšnosparnių žiedavimų duomenys iš Paukščių žiedavimo ir... |
| [PaukscioBiometrija](pauksciai_ir_siksnosparniai/PaukscioBiometrija.md) | Paukščių ir šikšnosparnių biometriniai duomenys (išmatuoti žieduojant) | `4` | `iraso_id` | — | `18` | Lentelėje pateikti Kauno Tado Ivanausko zoologijos muziejaus Lietuvoje atliktų paukščių ir šikšnosparnių žiedavimų biometriniai duomenys iš Paukščių... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ktizm/pauksciai_ir_siksnosparniai (https://data.gov.lt/datasets/2714/)
