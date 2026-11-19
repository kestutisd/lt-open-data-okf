---
type: Dataset
title: "Paraiškų dėl vaistinių preparatų ar medicinos pagalbos priemonių įrašymo į kompensavimo sąrašus svarstymo duomenys"
description: "Lietuvos Respublikos sveikatos apsaugos ministerija (LR SAM) renka ir skelbia duomenis apie svarstomas paraiškas dėl vaistinių preparatų ir medicinos pagalbos priemonių (MPP) įtraukimo į kompensuojamųjų sąrašus."
resource: "https://get.data.gov.lt/datasets/gov/sam/vaistai"
tags: [gov, sam, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sam/vaistai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/sam/vaistai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3822/"
    title: "data.gov.lt DCAT-AP — datasets/gov/sam/vaistai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Paraiškų dėl vaistinių preparatų ar medicinos pagalbos priemonių įrašymo į kompensavimo sąrašus svarstymo duomenys

Lietuvos Respublikos sveikatos apsaugos ministerija (LR SAM) renka ir skelbia duomenis apie svarstomas paraiškas dėl vaistinių preparatų ir medicinos pagalbos priemonių (MPP) įtraukimo į kompensuojamųjų sąrašus. Šie duomenys suteikia galimybę stebėti sveikatos technologijų vertinimo (STV) procesą ir priimamus sprendimus dėl kompensavimo. STV paraiškų duomenis teikia Valstybinė vaistų kontrolės tarnyba (VVKT). MPP duomenys gaunami iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos (VASPVT) duomenų bazių. Šio rinkinio duomenis galima praturtinti jungiant su VVKT atvertu rinkiniu (duomenys jungiami per stulpelį „paraiskos_numeris“): https://data.gov.lt/datasets/2897/.[^manifest]

- **Namespace:** `datasets/gov/sam/vaistai`[^manifest]
- **Manifest CSV:** [datasets/gov/sam/vaistai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sam/vaistai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sam/vaistai` (`deployed`)[^manifest]
- **Provider:** `sam` — Lietuvos Respublikos sveikatos apsaugos ministerija *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3822/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/sam/vaistai/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Paraiškų dėl vaistinių preparatų ar medicinos pagalbos priemonių įrašymo į kompensavimo sąrašus svarstymo duomenys[^dcat]
- **Portal Title (`@en`):** Data on the consideration of applications for the inclusion of medicinal products or medical aid products on the reimbursement lists[^dcat]
- **Issued (`dct:issued`):** `2025-04-04`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-04-04` .. `2026-09-11`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lietuvos Respublikos sveikatos apsaugos ministerija (LR SAM) renka ir skelbia duomenis apie svarstomas paraiškas dėl vaistinių preparatų ir medicinos pagalbos priemonių (MPP) įtraukimo į kompensuojamųjų sąrašus. Šie duomenys suteikia galimybę stebėti sveikatos technologijų vertinimo (STV) procesą ir priimamus sprendimus dėl kompensavimo. STV paraiškų duomenis teikia Valstybinė vaistų kontrolės tarnyba (VVKT). MPP duomenys gaunami iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos (VASPVT) duomenų bazių. Šio rinkinio duomenis galima praturtinti jungiant su VVKT atvertu rinkiniu (duomenys jungiami per stulpelį „paraiskos_numeris“): https://data.gov.lt/datasets/2897/. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Ministry of Health of the Republic of Lithuania (LR SAM) shall collect and publish data on the pending applications for the inclusion of medicinal products and medical aid products (MPPs) in the compensatory lists. These data provide an opportunity to monitor the Health Technology Assessment (STV) process and the compensation decisions taken. Data on CTVs applications shall be submitted by the State Medicines Control Agency (IWC). The MPP data are derived from the databases of the State Health Care Accreditation Service (VASPVT). This set of data can be enriched by connecting to a set opened by the IWT (data is combined through the “paraiskos_number” column): https://data.gov.lt/datasets/2897/. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Paraiska](vaistai/Paraiska.md) | Paraiškų dėl vaistinių preparatų ar medicinos pagalbos priemonių įrašymo į kompensavimo sąrašus svarstymo duomenys | `4` | `vda_prime_key` | — | `13` | Lietuvos Respublikos sveikatos apsaugos ministerija (LR SAM) renka ir skelbia duomenis apie svarstomas paraiškas dėl vaistinių preparatų ir medicinos... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/sam/vaistai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sam/vaistai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/sam/vaistai (https://data.gov.lt/datasets/3822/)
