---
type: Dataset
title: "Aktualūs asmens sveikatos priežiūros įstaigų personalo duomenys"
description: "UAB „Varutis“ vystoma ir administruojama Elektroninė sveikatos istorijos sistema (ESIS) kaupia asmens sveikatos priežiūros įstaigose (ASPĮ), naudojančiose ESIS, dirbančio personalo tarnybinius duomenis."
resource: "https://get.data.gov.lt/datasets/gov/esis/med_personalas"
tags: [gov, esis, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/esis/med_personalas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/esis/med_personalas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2706/"
    title: "data.gov.lt DCAT-AP — datasets/gov/esis/med_personalas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Aktualūs asmens sveikatos priežiūros įstaigų personalo duomenys

- **Namespace:** `datasets/gov/esis/med_personalas`[^manifest]
- **Manifest CSV:** [datasets/gov/esis/med_personalas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/esis/med_personalas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/esis/med_personalas` (`deployed`)[^manifest]
- **Provider:** `esis`[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2706/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/esis/med_personalas`[^dcat]
- **Portal Title (`@lt`):** Asmens sveikatos priežiūros įstaigų medicininis personalas[^dcat]
- **Portal Title (`@en`):** Medical staff[^dcat]
- **Issued (`dct:issued`):** `2024-07-23`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-07-18` .. `2026-10-27`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

UAB „Varutis“ vystoma ir administruojama Elektroninė sveikatos istorijos sistema (ESIS) kaupia asmens sveikatos priežiūros įstaigose (ASPĮ), naudojančiose ESIS, dirbančio personalo tarnybinius duomenis. Priklausomai nuo ASPĮ, duomenų laiko aprėptis gali skirtis, tačiau duomenys yra atnaujinami kasdien. Duomenų rinkinį sudaro: ASPĮ JAR kodas, pavadinimas ir savivaldybė, darbuotojo pseudonimizuotas asmens kodas, darbuotojui priskirtas padalinys, einamos pareigos ir ataskaitinė data, nurodanti esamo duomenų įrašo aktualumą. Duomenų teikėjas – Asmens sveikatos priežiūros įstaigos. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Electronic Health History System (ESIS), developed and administered by UAB Varutis, collects official data of personnel working in individual health care institutions (ASPIS) using ESIS. Depending on THE SCOPE, data time coverage may vary, but data is updated daily. The dataset shall include THE ASPIS Jaris code, name and municipality, the division assigned to the employee, his/her pseudonymized personal number, his/her position and the reference date indicating the relevance of the existing data entry.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Darbuotojas](med_personalas/Darbuotojas.md) | Aktualūs asmens sveikatos priežiūros įstaigų personalo duomenys | `4` | `vda_id` | — | `8` | UAB „Varutis“ vystoma ir administruojama Elektroninė sveikatos istorijos sistema (ESIS) kaupia asmens sveikatos priežiūros įstaigose (ASPĮ), naudojančiose... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/esis/med_personalas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/esis/med_personalas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/esis/med_personalas (https://data.gov.lt/datasets/2706/)
