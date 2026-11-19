---
type: Dataset
title: "PSDN paraiškos"
description: "Valstybės duomenų agentūra, įgyvendindama Lietuvos Respublikos pakartotinio sveikatos duomenų naudojimo įstatymą, pagal paraiškas išduoda leidimus pakartotinai naudoti sveikatos duomenis."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/psdn_paraiskos"
tags: [gov, lsd, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/psdn_paraiskos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/psdn_paraiskos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3858/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/psdn_paraiskos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# PSDN paraiškos

- **Namespace:** `datasets/gov/lsd/sveikata/psdn_paraiskos`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/psdn_paraiskos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/psdn_paraiskos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/psdn_paraiskos` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3858/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/psdn_paraiskos`[^dcat]
- **Portal Title (`@lt`):** Leidimai pakartotinai naudoti sveikatos duomenis[^dcat]
- **Portal Title (`@en`):** Authorisation for re-use of health data[^dcat]
- **Issued (`dct:issued`):** `2025-07-01`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `WEEKLY` (`http://publications.europa.eu/resource/authority/frequency/WEEKLY`)[^dcat]
- **Distribution Date Span:** `2025-07-01` .. `2026-10-26`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Valstybės duomenų agentūra, įgyvendindama Lietuvos Respublikos pakartotinio sveikatos duomenų naudojimo įstatymą, pagal paraiškas išduoda leidimus pakartotinai naudoti sveikatos duomenis. Duomenų rinkinyje pateikiami visi šio įstatymo pagrindu išduoti leidimai, paraiškos tikslas, projekte tyrinėjami subjektai, trumpas pateiktų duomenų aprašymas ir leidimo galiojimo laikotarpis. Kai paraišką teikia juridinis asmuo, tada nurodytas paraiškos teikėjas, apie fizinius asmenis informacija nerodoma. ŠALTINIAI Pakartotinio sveikatos duomenų naudojimo paraiškoje pareiškėjų pateikti duomenys. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The State Data Agency, in accordance with the Law of the Republic of Lithuania on the Reuse of Health Data, issues permissions for the reuse of health data. This dataset contains all permissions granted under this law, including the purpose of the application, the subjects of the research project, a brief description of the data, and the validity period of the permission. When the applicant is a legal entity, the name of the entity is provided. Information about natural persons is not disclosed. SOURCES Data submitted by applicants in the application form for the reuse of health data. Contact the atverimas@stat.gov.lt for technical questions or possible errors[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PSDNParaiska](psdn_paraiskos/PSDNParaiska.md) | Pakartotinio sveikatos duomenų naudojimo paraiškos | — | `vda_id` | — | `12` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/psdn_paraiskos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/psdn_paraiskos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/psdn_paraiskos (https://data.gov.lt/datasets/3858/)
