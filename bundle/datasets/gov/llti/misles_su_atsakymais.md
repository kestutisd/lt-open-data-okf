---
type: Dataset
title: "Mįslės su atsakymais"
description: "Rinkinys „Mįslės su atsakymais“ pateikia mįsles su jų įminimais (atsakymais) iš Lietuvių literatūros ir tautosakos instituto Lituanistikos paveldo informacinės sistemos „Aruodai“ (https://www.aruodai.lt/)."
resource: "https://get.data.gov.lt/datasets/gov/llti/misles_su_atsakymais"
tags: [gov, llti, deployed, cadence-weekly_3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/misles_su_atsakymais.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/llti/misles_su_atsakymais.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2835/"
    title: "data.gov.lt DCAT-AP — datasets/gov/llti/misles_su_atsakymais"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Mįslės su atsakymais

- **Namespace:** `datasets/gov/llti/misles_su_atsakymais`[^manifest]
- **Manifest CSV:** [datasets/gov/llti/misles_su_atsakymais.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/misles_su_atsakymais.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/llti/misles_su_atsakymais` (`deployed`)[^manifest]
- **Provider:** `llti` — Lietuvių literatūros ir tautosakos institutas *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2835/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/llti/misles_su_atsakymais`[^dcat]
- **Portal Title (`@lt`):** Mįslės su atsakymais[^dcat]
- **Portal Title (`@en`):** Riddles with answers of Lithuanian Institute of Literature and Folklore[^dcat]
- **Issued (`dct:issued`):** `2024-10-25`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `WEEKLY_3` (`http://publications.europa.eu/resource/authority/frequency/WEEKLY_3`)[^dcat]
- **Distribution Date Span:** `2024-10-25` .. `2025-11-03`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinys „Mįslės su atsakymais“ pateikia mįsles su jų įminimais (atsakymais) iš Lietuvių literatūros ir tautosakos instituto Lituanistikos paveldo informacinės sistemos „Aruodai“ (https://www.aruodai.lt/). Duomenys į sistemą įtraukti nuo 2013 metų, atnaujinami kas ketvirtį. Nuo 2025 m. rugsėjo rinkinys papildytas naujais stulpeliais, kurie suteikia daugiau konteksto mįslėms bei jų pateikėjams: užrašymo_vietovė – konkreti vietovė (kaimas, miestelis, parapija ar pan.), kurioje buvo užrašyta mįslė. užrašymo_vietovės_pastabos – papildomos pastabos apie užrašymo vietą, leidžiančios tiksliau suprasti kultūrinį ir geografinį kontekstą. mįslės_pateikėjo_amžius – pateikėjo amžius mįslės pateikimo metu. Tai suteikia vertingos informacijos folkloristikos analizei. mįslės_kilimo_metai – metai, iš kurių laikoma kilusi mįslė (jeigu tokia informacija buvo pažymėta). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The table contains riddles with their memories (answers) from the Lithuanian Institute of Lituanistic Heritage Information System “Aruodai” (https://www.aruodai.lt/). All data shall be provided from the date of their introduction into the system (2013) by updating every quarter of the year. Technical questions or possible errors may be referred to the atverimas@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Misle](misles_su_atsakymais/Misle.md) | Mįslės su atsakymais | `4` | `misles_id` | — | `14` | Lentelėje pateiktos mįslės su jų įminimais (atsakymais) iš Lietuvių literatūros ir tautosakos instituto Lituanistikos paveldo informacinės sistemos... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/llti/misles_su_atsakymais.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/misles_su_atsakymais.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/llti/misles_su_atsakymais (https://data.gov.lt/datasets/2835/)
