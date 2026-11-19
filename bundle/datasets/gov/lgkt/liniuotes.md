---
type: Dataset
title: "Liniuočių taikymo duomenys"
description: "Lygių galimybių kontrolieriaus tarnybos organizuojamas liniuočių registras kaupia Lyčių lygybės ir Lygių galimybių liniuočių (atitinkamai, LLL ir LGL) taikymo duomenis atitinkamose organizacijose."
resource: "https://get.data.gov.lt/datasets/gov/lgkt/liniuotes"
tags: [gov, lgkt, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgkt/liniuotes.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lgkt/liniuotes.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2815/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lgkt/liniuotes"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Liniuočių taikymo duomenys

- **Namespace:** `datasets/gov/lgkt/liniuotes`[^manifest]
- **Manifest CSV:** [datasets/gov/lgkt/liniuotes.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgkt/liniuotes.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgkt/liniuotes` (`deployed`)[^manifest]
- **Provider:** `lgkt` — Lygių galimybių kontrolieriaus tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2815/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lgkt/liniuotes`[^dcat]
- **Portal Title (`@lt`):** Liniuočių taikymo duomenys[^dcat]
- **Portal Title (`@en`):** Data on the application of rulers[^dcat]
- **Issued (`dct:issued`):** `2024-10-04`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2024-09-27` .. `2024-09-27`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lygių galimybių kontrolieriaus tarnybos organizuojamas liniuočių registras kaupia Lyčių lygybės ir Lygių galimybių liniuočių (atitinkamai, LLL ir LGL) taikymo duomenis atitinkamose organizacijose. Duomenys kaupiami nuo 2018 m. Duomenų rinkinys apima liniuotės registracijos numerį, tipą, organizaciją, kurioje ji taikyta, prašymų gavimo, anketų pildymo pabaigos bei liniuotės registravimo datas. Nuo 2022 m. kovo prašymų gavimo datos nebepildomos. Vienas duomenų rinkinio įrašas atitinka vieną organizaciją ir laikotarpį, kada buvo gautas prašymas, baigta pildyti anketa ir užregistruota liniuotė. Duomenų teikėjas – Lygių galimybių kontrolieriaus tarnyba. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Register of Directors organised by the Office of the Equal Opportunities Ombudsperson collects data on Gender Equality and Application of Equal Opportunities Regulators (LLL and LGL respectively) in respective organisations. The data has been compiled since 2018 and is up-to-date. The data set shall include the registration number of the ruler, the type, the organization in which it was applied, the dates of receipt of applications, completion of questionnaires and registration of the ruler. As of March 2022, the date of receipt of applications shall no longer be filled in. One data set entry corresponds to one organization and the period during which the request was received, completed the questionnaire and registered the ruler. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Liniuote](liniuotes/Liniuote.md) | Liniuočių taikymo duomenys | `4` | `vda_prime_key` | — | `7` | Lygių galimybių kontrolieriaus tarnybos organizuojamas liniuočių registras kaupia Lyčių lygybės ir Lygių galimybių liniuočių (atitinkamai, LLL ir LGL)... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lgkt/liniuotes.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgkt/liniuotes.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lgkt/liniuotes (https://data.gov.lt/datasets/2815/)
