---
type: Dataset
title: "Pirkimų, vykdytų po 2017-07-01 duomenys"
description: "Šioje duomenų bazėje saugomos ataskaitos už pirkimus, vykdytus po 2017 m. liepos 1 d."
resource: "https://get.data.gov.lt/datasets/gov/vpt/new"
tags: [gov, vpt, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vpt/new.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/389/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpt/new"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Pirkimų, vykdytų po 2017-07-01 duomenys

- **Namespace:** `datasets/gov/vpt/new`[^manifest]
- **Manifest CSV:** [datasets/gov/vpt/new.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpt/new` (`deployed`)[^manifest]
- **Provider:** `vpt` — Viešųjų pirkimų tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `57` (57 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/389/`[^dcat]
- **Publisher (`dct:publisher`):** Viešųjų pirkimų tarnyba[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vpt/new`[^dcat]
- **Portal Title (`@lt`):** Pirkimai, vykdyti 2017 m. liepos 1 d. - 2023 m. sausio 1 d. laikotarpiu[^dcat]
- **Portal Title (`@en`):** Tenders executed after 1st July 2017[^dcat]
- **Issued (`dct:issued`):** `2022-05-12`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2022-05-12` .. `2024-12-05`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Šioje duomenų bazėje saugomos ataskaitos už pirkimus, vykdytus po 2017 m. liepos 1 d. iki 2023 m. sausio 1 d.[^dcat]

### Portal Description (`@en`)

This database stores advertisements, reports on purchases made after 2017. July 1 and annual procurement plans after 2018. January 1[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Atgn1](new/Atgn1.md) | AtGn-1 tipinė forma | — | — | — | `76` | Viešojo pirkimo arba pirkimo, atlikto gynybos ir saugumo srityje, procedūrų ataskaita |
| [Atgn1ContractList](new/Atgn1ContractList.md) | AtGn-1 IX. SUTARTYS | — | — | — | `15` | — |
| [Atgn1ContractListSubcontractorsConcludedTendererList](new/Atgn1ContractListSubcontractorsConcludedTendererList.md) | AtGn-1 IX.2.1 Subtiekėjai, subrangovai | — | — | — | `14` | — |
| [Atgn1ContractListSubcontractorsUnknownTendererList](new/Atgn1ContractListSubcontractorsUnknownTendererList.md) | — | — | — | — | `15` | — |
| [Atgn1ContractedCandidateList](new/Atgn1ContractedCandidateList.md) | AtGn-1 VI.3.1. Nustatyta pasiūlymų eilė arba priimtas sprendimas dėl laimėjusio pasiūlymo | — | — | — | `12` | — |
| [Atgn1EndOfDesignContestProcedureList](new/Atgn1EndOfDesignContestProcedureList.md) | AtGn-1 VIII.2 Priežastys nutraukti procedūras | — | — | — | `9` | — |
| [Atgn1EndOfProcurementProcedureList](new/Atgn1EndOfProcurementProcedureList.md) | AtGn-1 VIII.1 PROCEDŪRŲ PABAIGA | — | — | — | `7` | — |
| [Atgn1PartOfObjectPurchaseList](new/Atgn1PartOfObjectPurchaseList.md) | AtGn-1 III.3 Pirkimo objekto kodas (-ai) pagal BVPŽ | — | — | — | `13` | — |
| [Atgn1RejectedCandidateList](new/Atgn1RejectedCandidateList.md) | VI. 2 Pasiūlymų nepateikę kandidatai (dalyviai) ir atmesti pasiūlymai (galutiniai pasiūlymai) | — | — | — | `14` | — |
| [Atgn1TendererGroupList](new/Atgn1TendererGroupList.md) | AtGn-1 V.1 Dalyviai, kandidatai (grupės) | — | — | — | `6` | — |
| [Atgn1TendererGroupListTendererSelectedTendererValues](new/Atgn1TendererGroupListTendererSelectedTendererValues.md) | AtGn-1 | — | — | — | `5` | — |
| [Atgn1TendererGroupListTendererValues](new/Atgn1TendererGroupListTendererValues.md) | AtGn-1 | — | — | — | `5` | — |
| [Atgn1TendererList](new/Atgn1TendererList.md) | AtGn-1 V.1 Dalyviai, kandidatai | — | — | — | `15` | — |
| [Atgn2](new/Atgn2.md) | Pirkimų ataskaita už mažos vertės viešuosius pirkimus, atliktus gynybos ir saugumo srityje | — | — | — | `54` | — |
| [Atkn1](new/Atkn1.md) | Koncesijos suteikimo procedūrų ataskaita | — | — | — | `44` | — |
| [Atkn1ContractingAuthorityOrEntityAddressList](new/Atkn1ContractingAuthorityOrEntityAddressList.md) | AtK-1 II. Suteikiančioji (-iosios) institucija (-os) | — | — | — | `13` | — |
| [Atkn1EndOfConcessionProcedureList](new/Atkn1EndOfConcessionProcedureList.md) | AtK-1 VII. Koncesijos suteikimo procedūrų pabaiga | — | — | — | `8` | — |
| [Atkn1GroundsForExclusionList](new/Atkn1GroundsForExclusionList.md) | AtK-1 VII.2 Priežastys, dėl kurių buvo nutrauktos koncesijos suteikimo procedūros | — | — | — | `6` | — |
| [Atkn1InformationAboutConcessionContractList](new/Atkn1InformationAboutConcessionContractList.md) | AtK-1 | — | — | — | `8` | — |
| [Atkn1PartOfObjectPurchaseList](new/Atkn1PartOfObjectPurchaseList.md) | AtK-1 III.3 Koncesijos objekto dalys | — | — | — | `13` | — |
| [Atkn1TendererAssessmentList](new/Atkn1TendererAssessmentList.md) | — | — | — | — | `6` | — |
| [Atkn1TendererGroupList](new/Atkn1TendererGroupList.md) | AtK-1 V.1 Informacija apie koncesijos dalyvius (grupės) | — | — | — | `6` | — |
| [Atkn1TendererList](new/Atkn1TendererList.md) | V. KONCESIJOS DALYVIAI | — | — | — | `15` | — |
| [Atkn1TerminationOfConcessionProcedureList](new/Atkn1TerminationOfConcessionProcedureList.md) | — | — | — | — | `8` | — |
| [Atn1](new/Atn1.md) | — | — | — | — | `115` | — |
| [Atn1CandidateRejectedTenderList](new/Atn1CandidateRejectedTenderList.md) | — | — | — | — | `17` | — |
| [Atn1ContractList](new/Atn1ContractList.md) | — | — | — | — | `26` | — |
| [Atn1ContractListSubcontractorsConcludedTendererList](new/Atn1ContractListSubcontractorsConcludedTendererList.md) | — | — | — | — | `18` | — |
| [Atn1ContractListSubcontractorsUnknownTendererList](new/Atn1ContractListSubcontractorsUnknownTendererList.md) | — | — | — | — | `18` | — |
| [Atn1ContractedCandidateList](new/Atn1ContractedCandidateList.md) | — | — | — | — | `14` | — |
| [Atn1DesignContestWinnersList](new/Atn1DesignContestWinnersList.md) | — | — | — | — | `18` | — |
| [Atn1EndOfDesignContestProcedureList](new/Atn1EndOfDesignContestProcedureList.md) | — | — | — | — | `9` | — |
| [Atn1EndOfProcurementProcedureList](new/Atn1EndOfProcurementProcedureList.md) | — | — | — | — | `9` | — |
| [Atn1PartOfObjectPurchaseList](new/Atn1PartOfObjectPurchaseList.md) | — | — | — | — | `13` | — |
| [Atn1ProcurementOfPreviousPublicationList](new/Atn1ProcurementOfPreviousPublicationList.md) | — | — | — | — | `7` | — |
| [Atn1RejectedCandidateList](new/Atn1RejectedCandidateList.md) | — | — | — | — | `17` | — |
| [Atn1SectionIvPartOfObjectPurchaseList](new/Atn1SectionIvPartOfObjectPurchaseList.md) | — | — | — | — | `13` | — |
| [Atn1SequenceOfDesignsList](new/Atn1SequenceOfDesignsList.md) | — | — | — | — | `10` | — |
| [Atn1SubcontractorsConcludedTendererList](new/Atn1SubcontractorsConcludedTendererList.md) | — | — | — | — | `18` | — |
| [Atn1SubcontractorsUnknownTendererList](new/Atn1SubcontractorsUnknownTendererList.md) | — | — | — | — | `18` | — |
| [Atn1TendererList](new/Atn1TendererList.md) | — | — | — | — | `18` | — |
| [Atn2](new/Atn2.md) | — | — | — | — | `92` | — |
| [Atn2ContractList](new/Atn2ContractList.md) | — | — | — | — | `27` | — |
| [Atn2ContractListSubcontractorsConcludedTendererList](new/Atn2ContractListSubcontractorsConcludedTendererList.md) | — | — | — | — | `18` | — |
| [Atn2ContractListSubcontractorsUnknownTendererList](new/Atn2ContractListSubcontractorsUnknownTendererList.md) | — | — | — | — | `18` | — |
| [Atn2ContractedCandidateList](new/Atn2ContractedCandidateList.md) | — | — | — | — | `14` | — |
| [Atn2EndOfDesignContestProcedureList](new/Atn2EndOfDesignContestProcedureList.md) | — | — | — | — | `9` | — |
| [Atn2EndOfProcurementProcedureList](new/Atn2EndOfProcurementProcedureList.md) | — | — | — | — | `9` | — |
| [Atn2PartOfObjectPurchaseList](new/Atn2PartOfObjectPurchaseList.md) | — | — | — | — | `13` | — |
| [Atn2RejectedCandidateList](new/Atn2RejectedCandidateList.md) | — | — | — | — | `17` | — |
| [Atn2SubcontractorsConcludedTendererList](new/Atn2SubcontractorsConcludedTendererList.md) | — | — | — | — | `18` | — |
| [Atn2SubcontractorsUnknownTendererList](new/Atn2SubcontractorsUnknownTendererList.md) | — | — | — | — | `18` | — |
| [Atn3](new/Atn3.md) | Atn-3 Metinė ataskaita | — | — | — | `57` | — |
| [Atn3ProcurementList](new/Atn3ProcurementList.md) | Atn-3 VII Viešųjų pirkimų įstatymo 10 straipsnyje arba komunalinio sektoriaus pirkimų įstatymo 19 straipsnyje nurodyti vidaus sandoriai | — | — | — | `14` | — |
| [CodeOfContractingAuthorityOrEntity](new/CodeOfContractingAuthorityOrEntity.md) | — | — | — | — | `5` | — |
| [Country](new/Country.md) | Šalių kodai | — | — | — | `6` | — |
| [CvpCode](new/CvpCode.md) | BVPŽ kodai | — | — | — | `5` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `pii` | `https://data.gov.lt/pii/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpt/new.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpt/new (https://data.gov.lt/datasets/389/)
