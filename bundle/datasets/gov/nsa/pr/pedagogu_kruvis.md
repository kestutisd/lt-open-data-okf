---
type: Dataset
title: "Pedagogų darbo krūvis"
description: "Lentelėje pateikti Nacionalinės Švietimo agentūros (NŠA) pedagogų (bendrojo, ikimokyklinio ugdymo mokyklų, profesinio mokymo įstaigų, neformaliojo vaikų švietimo mokyklų ir formalųjį švietimą papildančio ugdymo mokyklų, mokslo ir studijų institucijų pedagoginių darbuotojų..."
resource: "https://get.data.gov.lt/datasets/gov/nsa/pr/pedagogu_kruvis"
tags: [gov, nsa, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/pr/pedagogu_kruvis.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/nsa/pr/pedagogu_kruvis.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2615/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nsa/pr/pedagogu_kruvis"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pedagogų darbo krūvis

- **Namespace:** `datasets/gov/nsa/pr/pedagogu_kruvis`[^manifest]
- **Manifest CSV:** [datasets/gov/nsa/pr/pedagogu_kruvis.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/pr/pedagogu_kruvis.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/pr/pedagogu_kruvis` (`deployed`)[^manifest]
- **Provider:** `nsa` — Nacionalinė švietimo agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2615/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/nsa/pr/pedagogu_kruvis`[^dcat]
- **Portal Title (`@lt`):** Pedagogų darbo krūvis[^dcat]
- **Portal Title (`@en`):** Workload for educators[^dcat]
- **Issued (`dct:issued`):** `2024-04-17`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `WEEKLY` (`http://publications.europa.eu/resource/authority/frequency/WEEKLY`)[^dcat]
- **Distribution Date Span:** `2026-04-07` .. `2026-10-25`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lentelėje pateikti Nacionalinės Švietimo agentūros (NŠA) pedagogų (bendrojo, ikimokyklinio ugdymo mokyklų, profesinio mokymo įstaigų, neformaliojo vaikų švietimo mokyklų ir formalųjį švietimą papildančio ugdymo mokyklų, mokslo ir studijų institucijų pedagoginių darbuotojų ir/arba tyrėjų) pareigybių ir darbo krūvio duomenys iš Pedagogų registro (PR). Duomenys kaupiami nuo 2010 m. Siekiant užtikrinti asmens duomenų apsaugą duomenys buvo triukšminti. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The table provides data on the positions and workload of National Agency for Education (NESA) educators (general, pre-school, vocational training institutions, non-formal children's education schools and teaching schools, academic and study institutions and/or researchers) from the Register of Teachers (PR). Data have been collected since 2010. Data have been noisy to ensure the protection of personal data.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [DarboKruvis](pedagogu_kruvis/DarboKruvis.md) | Pedagogų darbo krūvis | `4` | `iraso_id` | — | `13` | Lentelėje pateikti Nacionalinės Švietimo agentūros (NŠA) pedagogų (bendrojo, ikimokyklinio ugdymo mokyklų, profesinio mokymo įstaigų, neformaliojo vaikų... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/pr/pedagogu_kruvis.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/pr/pedagogu_kruvis.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nsa/pr/pedagogu_kruvis (https://data.gov.lt/datasets/2615/)
