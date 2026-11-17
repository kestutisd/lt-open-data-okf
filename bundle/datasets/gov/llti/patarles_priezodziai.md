---
type: Dataset
title: "Patarlių ir priežodžių elektroninis sąvadas"
description: "Rinkinyje pateikiami duomenys iš Lietuvių literatūros ir tautosakos instituto Patarlių ir priežodžių elektroninio sąvado (eLPP)."
resource: "https://get.data.gov.lt/datasets/gov/llti/patarles_priezodziai"
tags: [gov, llti, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/llti/patarles_priezodziai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/patarles_priezodziai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Patarlių ir priežodžių elektroninis sąvadas

Rinkinyje pateikiami duomenys iš Lietuvių literatūros ir tautosakos instituto Patarlių ir priežodžių elektroninio sąvado (eLPP). Jo pagrindas – Lietuvių literatūros ir tautosakos instituto sisteminės Patarlių ir priežodžių kartotekos duomenys. Kiekvienos patarlės ar priežodžio variantai sutelkiami į tipus, vienijamus panašių motyvų. Daugiau informacijos rasite <https://elpp.archyvas.llti.lt/lt/savadas>. Nuo 2026 m. sausio papildomai atveriami patarlių atitikmenys kitomis kalbomis ir šaltinių sąrašas.

- **Namespace:** `datasets/gov/llti/patarles_priezodziai`[^manifest]
- **Manifest CSV:** [datasets/gov/llti/patarles_priezodziai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/patarles_priezodziai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/llti/patarles_priezodziai`
- **Parent Namespace (`ns`):** Lietuvių literatūros ir tautosakos institutas (`datasets/gov/llti`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Tipas](patarles_priezodziai/Tipas.md) | Patarlės ir priežodžiai | `4` | `tipo_id` | — | 15 | Lietuvių patarlių ir priežodžių tipų sąrašas. |
| [Atitikmuo](patarles_priezodziai/Atitikmuo.md) | Atitikmenys kitomis kalbomis pagal šaltinius | `4` | `iraso_id` | — | 6 | Prie populiarių tarptautinių tipų teikiami patarlių atitikmenys latvių, lenkų, vokiečių, anglų, lotynų bei rusų kalbomis. |
| [Saltinis](patarles_priezodziai/Saltinis.md) | Šaltiniai | `4` | `saltinio_id` | — | 3 | Literatūros šaltiniai su pilnomis bibliografinėmis nuorodomis ir jų santrumpomis. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/llti/patarles_priezodziai.csv
