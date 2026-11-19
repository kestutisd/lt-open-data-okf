---
type: Dataset
title: "Valstybės registrų ir informacinių sistemų registro duomenys"
description: "IVPK registrų duomenys - Informacinės visuomenės plėtros stebėsenos ir valstybės IT paslaugų valdymo informacinės sistemos; Administracinių nusižengimų registras; Tarpžinybinė mokestinių duomenų saugykla; Registrų ir valstybės informacinių sistemų registras; Valstybės..."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/registrai"
tags: [gov, ivpk, deployed, cadence-other]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1196/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ivpk/registrai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Valstybės registrų ir informacinių sistemų registro duomenys

- **Namespace:** `datasets/gov/ivpk/registrai`[^manifest]
- **Manifest CSV:** [datasets/gov/ivpk/registrai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/registrai` (`deployed`)[^manifest]
- **Provider:** `ivpk` — Valstybės skaitmeninių sprendimų agentūra (VSSA, buv. IVPK) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `24` (24 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1196/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės skaitmeninių sprendimų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/ivpk/registrai`[^dcat]
- **Portal Title (`@lt`):** Valstybės registrų ir informacinių sistemų registro duomenys[^dcat]
- **Portal Title (`@en`):** IVPK Register data[^dcat]
- **Issued (`dct:issued`):** `2023-06-26`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `OTHER` (`http://publications.europa.eu/resource/authority/frequency/OTHER`)[^dcat]
- **Distribution Date Span:** `2023-12-17` .. `2023-12-17`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

IVPK registrų duomenys - Informacinės visuomenės plėtros stebėsenos ir valstybės IT paslaugų valdymo informacinės sistemos; Administracinių nusižengimų registras; Tarpžinybinė mokestinių duomenų saugykla; Registrų ir valstybės informacinių sistemų registras; Valstybės informacinių išteklių sąveikumo platforma; registrų nuostatai ir specifikacijos.[^dcat]

### Portal Description (`@en`)

Data of IVPK registers - Information society development monitoring and state IT service management information systems; Register of Administrative Offenses; Interdepartmental tax data repository; Register of Registers and State Information Systems; State Information Resource Interoperability Platform; regulations and specifications of registers.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [ClassificationType](registrai/ClassificationType.md) | Klasifikatoriaus tipas | `4` | — | — | `4` | — |
| [DataTrafficMode](registrai/DataTrafficMode.md) | Duomenų srauto režimas | `4` | — | — | `4` | — |
| [DocumentClosingMode](registrai/DocumentClosingMode.md) | Dokumento uždarymo režimas | `4` | — | — | `4` | — |
| [DocumentType](registrai/DocumentType.md) | Dokumento tipas | `4` | — | — | `10` | — |
| [InstitutionGroup](registrai/InstitutionGroup.md) | Institucijų grupė | `4` | — | — | `4` | — |
| [Institution](registrai/Institution.md) | Institucijų sąrašas | `4` | — | — | `14` | — |
| [ManagerType](registrai/ManagerType.md) | Valdymo tipas | `4` | — | — | `4` | — |
| [ProvisionAndSpecificationStatus](registrai/ProvisionAndSpecificationStatus.md) | Nuostatų ir specifikacijų statusas | `4` | — | — | `4` | — |
| [RegistryDevelopmentPhase](registrai/RegistryDevelopmentPhase.md) | Registro kūrimo etapas | `4` | — | — | `4` | — |
| [RegistryObjectType](registrai/RegistryObjectType.md) | Registro objekto tipas | `4` | — | — | `4` | — |
| [RegistryType](registrai/RegistryType.md) | Registro tipas | `4` | — | — | `4` | — |
| [Object](registrai/Object.md) | Registras/Informacinė sistema | `4` | — | — | `9` | — |
| [AcceptanceDocument](registrai/AcceptanceDocument.md) | Objektų priėmimo dokumentai | `4` | — | — | `6` | — |
| [ObjectClassification](registrai/ObjectClassification.md) | Objekto klasifikacija | `4` | — | — | `5` | — |
| [ObjectsFiles](registrai/ObjectsFiles.md) | Objektų failai | `4` | — | — | `9` | — |
| [FoundingDocument](registrai/FoundingDocument.md) | Objekto steigimo dokumentas | `4` | — | — | `10` | — |
| [ObjectIndicator](registrai/ObjectIndicator.md) | Objekto indikatorius | `4` | — | — | `6` | — |
| [ObjectInteraction](registrai/ObjectInteraction.md) | Sąveika su objektais | `4` | — | — | `5` | — |
| [LiquidationDocument](registrai/LiquidationDocument.md) | Objektų likvidavimo dokumentai | `4` | — | — | `12` | — |
| [ObjectManagerRelation](registrai/ObjectManagerRelation.md) | Registrų valdytojai | `4` | — | — | `4` | — |
| [ProjectSpecificationDocument](registrai/ProjectSpecificationDocument.md) | Objektų projekto spcifikacijos dokumentai | `4` | — | — | `8` | — |
| [ObjectRegistryObjectTypeRelation](registrai/ObjectRegistryObjectTypeRelation.md) | Registrų objekto tipai ir ryšiai | `4` | — | — | `4` | — |
| [ObjectRegistryTypeRelation](registrai/ObjectRegistryTypeRelation.md) | Objektų registrų tipai ir ryšiai | `4` | — | — | `4` | — |
| [ObjectRegulationDocument](registrai/ObjectRegulationDocument.md) | Objektų reglamentavimo dokumentai | `4` | — | — | `14` | — |

# Enumerations

| Enum (ref) | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `object_type` | `'rs'` | — | — | Registras | — |
| `object_type` | `'vis'` | — | — | Valstybės informacinės sistema | — |
| `object_type` | `'both'` | — | — | Registras ir Valstybės informacinė sistema | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ivpk/registrai (https://data.gov.lt/datasets/1196/)
