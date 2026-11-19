---
type: Dataset
title: "Teisinės pagalbos paslaugų informacinės sistemos (TEISIS) klasifikatoriai"
description: "Teisinės pagalbos paslaugų informacinės sistemos (TEISIS) klasifikatoriai, 3 vnt., Teisinės pagalbos paslaugų informacinės sistemos teritorijos klasifikatorius"
resource: "https://get.data.gov.lt/datasets/gov/vgtpt/teisis/klasifikatoriai"
tags: [gov, vgtpt, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/klasifikatoriai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vgtpt/teisis/klasifikatoriai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2288/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vgtpt/teisis/klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Teisinės pagalbos paslaugų informacinės sistemos (TEISIS) klasifikatoriai

Teisinės pagalbos paslaugų informacinės sistemos (TEISIS) klasifikatoriai, 3 vnt., Teisinės pagalbos paslaugų informacinės sistemos teritorijos klasifikatorius[^manifest]

- **Namespace:** `datasets/gov/vgtpt/teisis/klasifikatoriai`[^manifest]
- **Manifest CSV:** [datasets/gov/vgtpt/teisis/klasifikatoriai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/klasifikatoriai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vgtpt/teisis/klasifikatoriai` (`deployed`)[^manifest]
- **Provider:** `vgtpt` — Valstybės garantuojamos teisinės pagalbos tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2288/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės garantuojamos teisinės pagalbos tarnyba[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vgtpt/teisis/klasifikatoriai`[^dcat]
- **Portal Title (`@lt`):** Valstybės garantuojamos teisinės pagalbos tarnybos informacinės sistemos (TEISIS) klasifikatoriai[^dcat]
- **Portal Title (`@en`):** Classifiers of the information system of the state-guaranteed legal assistance service (TEISIS).[^dcat]
- **Issued (`dct:issued`):** `2023-06-06`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-06-06` .. `2025-09-18`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Valstybės garantuojamos teisinės pagalbos tarnybos paslaugų informacinės sistemos (TEISIS) susisteminti duomenų sąrašai į kuriuos įeina šie klasifikatoriai: teritorijos klasifikatorius (pagalbą gaunančio asmens gyvenamosios vietos teritorijos pagal savivaldybes kodas); pagalbos teikimo pagrindo klasifikatorius (baudžiamojo proceso kodekso straipsnis); bylos rūšies klasifikatorius (byla, kurioje reikalinga teisinės pagalba).[^dcat]

### Portal Description (`@en`)

Systematized data lists of the state-guaranteed legal aid service information system (TEISIS), which include the following classifiers: territory classifier (territory of residence of the person receiving assistance according to municipal codes); the classifier of the basis for providing assistance (Article of the Code of Criminal Procedure); case type classifier (a case requiring legal assistance).[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Teritorija](klasifikatoriai/Teritorija.md) | Teisinės pagalbos paslaugų informacinės sistemos teritorijos klasifikatorius | `4` | `nr` | — | `4` | — |
| [ParinkimoPagrindas](klasifikatoriai/ParinkimoPagrindas.md) | Teisinės pagalbos paslaugų informacinės sistemos pagalbos teikimo pagrindų klasifikatorius | `4` | `nr` | — | `3` | — |
| [BylosRusis](klasifikatoriai/BylosRusis.md) | Teisinės pagalbos paslaugų informacinės sistemos bylų rūšių klasifikatorius | `4` | `nr` | — | `3` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vgtpt/teisis/klasifikatoriai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/klasifikatoriai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vgtpt/teisis/klasifikatoriai (https://data.gov.lt/datasets/2288/)
