---
type: Dataset
title: "Ūkio subjektai, kurių vykdomoje veikloje nustatyti Lietuvos metrologijos inspekcijos reikalavimų pažeidimai"
description: "Duomenų rinkinyje pateikiama informacija apie ūkio subjektus, juridinius ir fizinius (įskaitant ūkininkus) asmenis, kurių vykdomoje veikloje naudojamų matavimo priemonių arba fasuotų prekių patikrinimo metu Lietuvos metrologijos inspekcija nustatė pažeidimus."
resource: "https://get.data.gov.lt/datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus"
tags: [gov, lmi, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2909/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Ūkio subjektai, kurių vykdomoje veikloje nustatyti Lietuvos metrologijos inspekcijos reikalavimų pažeidimai

- **Namespace:** `datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus`[^manifest]
- **Manifest CSV:** [datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus` (`deployed`)[^manifest]
- **Provider:** `lmi` — Lietuvos metrologijos inspekcija *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2909/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus`[^dcat]
- **Portal Title (`@lt`):** Ūkio subjektai, kurių vykdomoje veikloje nustatyti Lietuvos metrologijos inspekcijos reikalavimų pažeidimai[^dcat]
- **Portal Title (`@en`):** Economic entities whose activities have revealed violations of requirements of the Lithuanian Metrology Inspectorate[^dcat]
- **Issued (`dct:issued`):** `2025-01-03`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2024-12-27` .. `2026-01-03`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiama informacija apie ūkio subjektus, juridinius ir fizinius (įskaitant ūkininkus) asmenis, kurių vykdomoje veikloje naudojamų matavimo priemonių arba fasuotų prekių patikrinimo metu Lietuvos metrologijos inspekcija nustatė pažeidimus. Fizinių asmenų duomenys yra užšifruoti. Jeigu įmonės kodas yra negaliojantis, įmonės kodo ir pavadinimo stulpeliai yra šifruojami. Taip pat, jeigu pažeidimą įvykdžiusios įmonės kodas nurodytas klaidingai, įmonės pavadinimo ir kodo stulpeliai gali būti užšifruoti. Ekonominės veiklos rūšių klasifikatoriaus (EVRK) kodai pateikti pagal EVRK 2 redakciją. Viena duomenų rinkinio eilutė atitinka vieną pažeidimą. Geografinė aprėptis – visa Lietuva. Duomenų aprėptis – nuo 2020 metų sausio 1 d. Duomenų teikėjas – Lietuvos metrologijos inspekcija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data set shall contain information on economic entities, legal and natural (including farmers) persons whose activities have been inspected by the Lithuanian Metrology Inspectorate for the detection of irregularities. Personal data is encrypted. If the company code is invalid, the company code and name columns are encrypted. Also, if the company code that committed the violation is misstated, the company name and code columns can be encrypted. The Economic Activities Classification (ECEC) codes are presented in the version 2 of the ECEC. One line in the dataset corresponds to one violation. Geographical coverage: Lithuania as a whole. Data coverage – from 1 January 2020. Data provider – Lithuanian Metrology Inspectorate. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [UkioSubjNustatytPazeidimas](us_kur_lmi_nustate_pazeidimus/UkioSubjNustatytPazeidimas.md) | Ūkio subjektai, kurių vykdomoje veikloje nustatyti Lietuvos metrologijos inspekcijos reikalavimų pažeidimai | `4` | `patikrinimo_akto_kodas` | — | `14` | Duomenų rinkinyje pateikiama informacija apie ūkio subjektus, juridinius ir fizinius (įskaitant ūkininkus) asmenis, kurių vykdomoje veikloje naudojamų... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus (https://data.gov.lt/datasets/2909/)
