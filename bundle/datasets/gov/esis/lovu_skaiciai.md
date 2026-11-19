---
type: Dataset
title: "Aktualūs asmens sveikatos priežiūros įstaigų lovų skaičiai"
description: "UAB „Varutis“ vystoma ir administruojama Elektroninė sveikatos istorijos sistema (ESIS) kaupia asmens sveikatos priežiūros įstaigų (ASPĮ), naudojančių ESIS, turimų lovų duomenis."
resource: "https://get.data.gov.lt/datasets/gov/esis/lovu_skaiciai"
tags: [gov, esis, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/esis/lovu_skaiciai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/esis/lovu_skaiciai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2707/"
    title: "data.gov.lt DCAT-AP — datasets/gov/esis/lovu_skaiciai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Aktualūs asmens sveikatos priežiūros įstaigų lovų skaičiai

- **Namespace:** `datasets/gov/esis/lovu_skaiciai`[^manifest]
- **Manifest CSV:** [datasets/gov/esis/lovu_skaiciai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/esis/lovu_skaiciai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/esis/lovu_skaiciai` (`deployed`)[^manifest]
- **Provider:** `esis`[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2707/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/esis/lovu_skaiciai`[^dcat]
- **Portal Title (`@lt`):** Asmens sveikatos priežiūros įstaigų lovų skaičiai[^dcat]
- **Portal Title (`@en`):** Number of beds of personal health care institutions[^dcat]
- **Issued (`dct:issued`):** `2024-07-23`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-07-18` .. `2026-10-26`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

UAB „Varutis“ vystoma ir administruojama Elektroninė sveikatos istorijos sistema (ESIS) kaupia asmens sveikatos priežiūros įstaigų (ASPĮ), naudojančių ESIS, turimų lovų duomenis. Priklausomai nuo ASPĮ, duomenų laiko aprėptis gali skirtis, tačiau duomenys yra atnaujinami kasdien. Duomenų rinkinį sudaro: ASPĮ JAR kodas, pavadinimas ir savivaldybė, lovos profilio pavadinimas, bendras visų atitinkamo profilio lovų skaičius ir laikinai nepildomas, einamąją dieną užimtų lovų skaičius. Duomenų teikėjas – Asmens sveikatos priežiūros įstaigos. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Electronic Health History System (ESIS), developed and administered by UAB Varutis, collects the data of the beds held by individual health care institutions (ASPIS) using ESIS. Depending on THE SCOPE, data time coverage may vary, but data is updated daily. The dataset shall include THE ASPIS Jaris code, name and municipality, the name of the bed profile, the total number of beds of the relevant profile and the temporarily incomplete number of beds occupied on the current day.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [LovuProfilis](lovu_skaiciai/LovuProfilis.md) | Aktualūs asmens sveikatos priežiūros įstaigų lovų skaičiai | `4` | `vda_id` | — | `7` | UAB „Varutis“ vystoma ir administruojama Elektroninė sveikatos istorijos sistema (ESIS) kaupia asmens sveikatos priežiūros įstaigų (ASPĮ), naudojančių ESIS... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/esis/lovu_skaiciai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/esis/lovu_skaiciai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/esis/lovu_skaiciai (https://data.gov.lt/datasets/2707/)
