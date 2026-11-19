---
type: Dataset
title: "Klientų aptarnavimas vietinės rinkliavos administravimo klausimais pagal nekilnojamo turto objektų duomenis"
description: "UAB Klaipėdos regiono atliekų tvarkymo centro naudojamoje sistemoje „KRATIS“ kaupiami klientų aptarnavimo rinkliavos administracijos klausimais duomenys."
resource: "https://get.data.gov.lt/datasets/gov/kratc/kratis"
tags: [gov, kratc, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kratc/kratis.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/kratc/kratis.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2906/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kratc/kratis"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Klientų aptarnavimas vietinės rinkliavos administravimo klausimais pagal nekilnojamo turto objektų duomenis

- **Namespace:** `datasets/gov/kratc/kratis`[^manifest]
- **Manifest CSV:** [datasets/gov/kratc/kratis.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kratc/kratis.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kratc/kratis` (`deployed`)[^manifest]
- **Provider:** `kratc` — UAB Klaipėdos regiono atliekų tvarkymo centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2906/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/kratc/kratis`[^dcat]
- **Portal Title (`@lt`):** Klientų aptarnavimas vietinės rinkliavos administravimo klausimais pagal nekilnojamo turto objektų duomenis[^dcat]
- **Portal Title (`@en`):** Customer service on local toll administration issues based on real estate object data[^dcat]
- **Issued (`dct:issued`):** `2024-12-19`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-12-19` .. `2026-09-11`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

UAB Klaipėdos regiono atliekų tvarkymo centro naudojamoje sistemoje „KRATIS“ kaupiami klientų aptarnavimo rinkliavos administracijos klausimais duomenys. Sistemoje duomenys kaupiami nuo 2008 m. rugpjūčio 1 d., duomenų rinkinyje – nuo 2013 m. balandžio 22 d. Rinkinyje kaupiami klientų aptarnavimo vietinės rinkliavos administracijos klausimais duomenys pagal nekilnojamojo turto (NT) objektus. Duomenų rinkinį sudaro: NT objekto identifikatorius ir paskirtis, kreipimosi data, būdas, tema, pagrįstumas su veiksmu ir išorinis raktas į 100x100 m geografinę gardelę. NT objektų identifikatoriai pseudoniminti, siekiant užtikrinti konfidencialumą, nes sistemos „KRATIS“ vartotojai gali matyti dalies objektų nepseudonimintus identifikatorius, panaudotus šiame rinkinyje. Tuo pačiu tikslu dalies įrašų paskirties stulpelio reikšmės paslėptos, kadangi adresas nurodytas kaip NT objekto paskirtis. Kadangi NT objektai gali užimti keletą gardelių, paprastumo dėlei parinktos toliausiai šiaurės vakarų kryptimi esančios gardelės, kad NT objektų ir gardelių įrašus pavyktų sujungti principu „vienas su vienu“. Vienas įrašas atitinka vieną aptarnavimo įvykį. Duomenų teikėjas – UAB Klaipėdos regiono atliekų tvarkymo centras. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The system “KRATIS” used by UAB Klaipėda Region Waste Management Centre accumulates customer service charge data on administration issues. Data shall be collected in the system from 1 August 2008 and in the data set from 22 April 2013. The collection shall collect customer service data on local toll administration issues according to real estate (NT) objects. The dataset consists of: NT object identifier and purpose, date of referral, method, subject, validity with action, and external key to the 100 x 100 m geographic cell. NT object identifiers are pseudonymised to ensure confidentiality, as users of the “SHAKE” system may see non-pseudonymized identifiers of some objects used in this collection. For the same purpose, the values of the destination column for part of the records are hidden because the address is specified as the purpose of the NT object. Since NT objects can occupy several cells, for the sake of simplicity, the chambers farthest north-west have been selected so that the recordings of NT objects and cells can be combined on a one-to-one basis. One record corresponds to one service event. Data provider – UAB Klaipėda Region Waste Management Centre. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Kreipimasis](kratis/Kreipimasis.md) | Klientų aptarnavimas vietinės rinkliavos administravimo klausimais pagal nekilnojamo turto objektų duomenis | `4` | `vda_prime_key` | — | `8` | UAB Klaipėdos regiono atliekų tvarkymo centro naudojamoje sistemoje „KRATIS“ kaupiami klientų aptarnavimo rinkliavos administracijos klausimais duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/kratc/kratis.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kratc/kratis.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kratc/kratis (https://data.gov.lt/datasets/2906/)
