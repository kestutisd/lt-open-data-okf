---
type: Dataset
title: "datasets/gov/ivpk/registrai"
description: "Spinta dataset datasets/gov/ivpk/registrai (24 tables)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/registrai"
tags: [gov, ivpk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/ivpk/registrai

- **Namespace:** `datasets/gov/ivpk/registrai`[^manifest]
- **Manifest CSV:** [datasets/gov/ivpk/registrai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/registrai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [ClassificationType](registrai/ClassificationType.md) | Klasifikatoriaus tipas | `4` | — | — | 4 | — |
| [DataTrafficMode](registrai/DataTrafficMode.md) | Duomenų srauto režimas | `4` | — | — | 4 | — |
| [DocumentClosingMode](registrai/DocumentClosingMode.md) | Dokumento uždarymo režimas | `4` | — | — | 4 | — |
| [DocumentType](registrai/DocumentType.md) | Dokumento tipas | `4` | — | — | 10 | — |
| [InstitutionGroup](registrai/InstitutionGroup.md) | Institucijų grupė | `4` | — | — | 4 | — |
| [Institution](registrai/Institution.md) | Institucijų sąrašas | `4` | — | — | 14 | — |
| [ManagerType](registrai/ManagerType.md) | Valdymo tipas | `4` | — | — | 4 | — |
| [ProvisionAndSpecificationStatus](registrai/ProvisionAndSpecificationStatus.md) | Nuostatų ir specifikacijų statusas | `4` | — | — | 4 | — |
| [RegistryDevelopmentPhase](registrai/RegistryDevelopmentPhase.md) | Registro kūrimo etapas | `4` | — | — | 4 | — |
| [RegistryObjectType](registrai/RegistryObjectType.md) | Registro objekto tipas | `4` | — | — | 4 | — |
| [RegistryType](registrai/RegistryType.md) | Registro tipas | `4` | — | — | 4 | — |
| [Object](registrai/Object.md) | Registras/Informacinė sistema | `4` | — | — | 9 | — |
| [AcceptanceDocument](registrai/AcceptanceDocument.md) | Objektų priėmimo dokumentai | `4` | — | — | 6 | — |
| [ObjectClassification](registrai/ObjectClassification.md) | Objekto klasifikacija | `4` | — | — | 5 | — |
| [ObjectsFiles](registrai/ObjectsFiles.md) | Objektų failai | `4` | — | — | 9 | — |
| [FoundingDocument](registrai/FoundingDocument.md) | Objekto steigimo dokumentas | `4` | — | — | 10 | — |
| [ObjectIndicator](registrai/ObjectIndicator.md) | Objekto indikatorius | `4` | — | — | 6 | — |
| [ObjectInteraction](registrai/ObjectInteraction.md) | Sąveika su objektais | `4` | — | — | 5 | — |
| [LiquidationDocument](registrai/LiquidationDocument.md) | Objektų likvidavimo dokumentai | `4` | — | — | 12 | — |
| [ObjectManagerRelation](registrai/ObjectManagerRelation.md) | Registrų valdytojai | `4` | — | — | 4 | — |
| [ProjectSpecificationDocument](registrai/ProjectSpecificationDocument.md) | Objektų projekto spcifikacijos dokumentai | `4` | — | — | 8 | — |
| [ObjectRegistryObjectTypeRelation](registrai/ObjectRegistryObjectTypeRelation.md) | Registrų objekto tipai ir ryšiai | `4` | — | — | 4 | — |
| [ObjectRegistryTypeRelation](registrai/ObjectRegistryTypeRelation.md) | Objektų registrų tipai ir ryšiai | `4` | — | — | 4 | — |
| [ObjectRegulationDocument](registrai/ObjectRegulationDocument.md) | Objektų reglamentavimo dokumentai | `4` | — | — | 14 | — |

# Enumerations

| Enum (`ref`) | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `object_type` | `'rs'` | — | — | Registras | — |
| `object_type` | `'vis'` | — | — | Valstybės informacinės sistema | — |
| `object_type` | `'both'` | — | — | Registras ir Valstybės informacinė sistema | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv
