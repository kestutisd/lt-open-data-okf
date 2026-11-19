---
type: Dataset
title: "Savininkų užimtų būstų kainų indekso svoriai"
description: "Rinkinyje pateikiama informacija apie savininkų užimtų būstų kainų indekso svorius."
resource: "https://get.data.gov.lt/datasets/gov/lsd/statistika/sbki_svoriai"
tags: [gov, lsd, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistika/sbki_svoriai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/statistika/sbki_svoriai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2523/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/statistika/sbki_svoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Savininkų užimtų būstų kainų indekso svoriai

- **Namespace:** `datasets/gov/lsd/statistika/sbki_svoriai`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/statistika/sbki_svoriai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistika/sbki_svoriai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/statistika/sbki_svoriai` (`deployed`)[^manifest]
- **Provider:** `lsd` — Oficialiosios statistikos portalo rodiklių duomenų bazės rinkiniai *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2523/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/statistika/sbki_svoriai/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Savininkų užimtų būstų kainų indekso svoriai[^dcat]
- **Portal Title (`@en`):** Weights of owner-occupied housing price index[^dcat]
- **Issued (`dct:issued`):** `2023-12-18`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2024-12-03` .. `2026-04-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiama informacija apie savininkų užimtų būstų kainų indekso svorius. Svoris – procentais arba promilėmis išreikšta namų ūkių piniginių išlaidų lyginamoji dalis tam tikrai BKI elementariajai visumai priklausantiems būstams su žeme įsigyti. Kuo didesnis svoris, tuo didesnė tam tikro būsto su žeme klasifikavimo lygio kainų pokyčio įtaka aukštesnio būsto su žeme klasifikavimo lygio kainų pokyčiui. Svorių bazinis laikotarpis – laikotarpis, kurio duomenimis remiantis skaičiuojami indekso svoriai. SUBKI svorių duomenų šaltiniai – nacionalinių sąskaitų duomenys apie bendrojo pagrindinio kapitalo formavimą naujiems būstams, VĮ Registrų centro Nekilnojamojo turto registro ir Sandorių duomenų bazės, Lietuvos banko duomenys apie būsto draudimo įmokas ir išmokas, eksperto parengta gyvenamųjų pastatų sąmatinė dokumentacija. SUBKI svorių bazinis laikotarpis yra t–2 metai, o BKI – t–1 metai. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package contains information on the weights of the owner-occupied housing price index. “Weight” means the percentage or promil of the relative share of household monetary expenditure for the purchase of land-based housing belonging to the basic population of the CCI. The higher the weight, the greater the impact of a change in the price level of a land-based housing classification on the price development of a higher level of land-based housing classification. “Weight reference period” means the period during which the weight of the index is calculated. DATA sources of SUBKI weights shall mean data of national accounts on the formation of gross fixed capital for new dwellings, Real Property Register and Transaction Database of the Centre of Registers of the SE, data of the Bank of Lithuania on housing insurance premiums and benefits, estimate documentation of residential buildings prepared by an expert. THE reference period for SUBKI weights is between T–2 years and for CCIs it is between T–1 years.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [S7R264M2021006](sbki_svoriai/S7R264M2021006.md) | Savininkų užimtų būstų kainų indekso svoriai | `4` | `vda_id` | — | `9` | Rinkinyje pateikiama informacija apie savininkų užimtų būstų kainų indekso svorius. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/statistika/sbki_svoriai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistika/sbki_svoriai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/statistika/sbki_svoriai (https://data.gov.lt/datasets/2523/)
