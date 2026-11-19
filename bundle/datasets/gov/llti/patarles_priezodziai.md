---
type: Dataset
title: "Patarlių ir priežodžių elektroninis sąvadas"
description: "Rinkinyje pateikiami duomenys iš Lietuvių literatūros ir tautosakos instituto Patarlių ir priežodžių elektroninio sąvado (eLPP)."
resource: "https://get.data.gov.lt/datasets/gov/llti/patarles_priezodziai"
tags: [gov, llti, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/patarles_priezodziai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/llti/patarles_priezodziai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2920/"
    title: "data.gov.lt DCAT-AP — datasets/gov/llti/patarles_priezodziai"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# Patarlių ir priežodžių elektroninis sąvadas

Rinkinyje pateikiami duomenys iš Lietuvių literatūros ir tautosakos instituto Patarlių ir priežodžių elektroninio sąvado (eLPP). Jo pagrindas – Lietuvių literatūros ir tautosakos instituto sisteminės Patarlių ir priežodžių kartotekos duomenys. Kiekvienos patarlės ar priežodžio variantai sutelkiami į tipus, vienijamus panašių motyvų. Daugiau informacijos rasite <https://elpp.archyvas.llti.lt/lt/savadas>. Nuo 2026 m. sausio papildomai atveriami patarlių atitikmenys kitomis kalbomis ir šaltinių sąrašas. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^manifest]

- **Namespace:** `datasets/gov/llti/patarles_priezodziai`[^manifest]
- **Manifest CSV:** [datasets/gov/llti/patarles_priezodziai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/patarles_priezodziai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/llti/patarles_priezodziai` (`deployed`)[^manifest]
- **Provider:** `llti` — Lietuvių literatūros ir tautosakos institutas *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2920/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/llti/patarles_priezodziai`[^dcat]
- **Portal Title (`@lt`):** Patarlių ir priežodžių elektroninis sąvadas[^dcat]
- **Portal Title (`@en`):** Electronic Input of Proverbs and Explanations[^dcat]
- **Issued (`dct:issued`):** `2025-01-16`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-20`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-01-16` .. `2026-10-15`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@en`)

The collection contains data from the Lithuanian Institute of Literature and Folklore's Electronic Recipe of Advertisements and Advertisements (eLPP). It is based on the data of the Lithuanian Institute of Literature and Folklore's Systematic Circuit of Advertisements and Advertisements. Each proverb or proverb will focus on types united by similar motives. For more information, see https://elpp.archyvas.llti.lt/lt/savadas. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Tipas](patarles_priezodziai/Tipas.md) | Patarlės ir priežodžiai | `4` | `tipo_id` | — | `15` | Lietuvių patarlių ir priežodžių tipų sąrašas. |
| [Atitikmuo](patarles_priezodziai/Atitikmuo.md) | Atitikmenys kitomis kalbomis pagal šaltinius | `4` | `iraso_id` | — | `6` | Prie populiarių tarptautinių tipų teikiami patarlių atitikmenys latvių, lenkų, vokiečių, anglų, lotynų bei rusų kalbomis. |
| [Saltinis](patarles_priezodziai/Saltinis.md) | Šaltiniai | `4` | `saltinio_id` | — | `3` | Literatūros šaltiniai su pilnomis bibliografinėmis nuorodomis ir jų santrumpomis. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/llti/patarles_priezodziai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/patarles_priezodziai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/llti/patarles_priezodziai (https://data.gov.lt/datasets/2920/)
