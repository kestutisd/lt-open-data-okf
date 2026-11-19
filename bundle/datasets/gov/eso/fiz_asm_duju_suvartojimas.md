---
type: Dataset
title: "Fizinių asmenų dujų suvartojimas"
description: "Rinkinyje pateikti Energijos skirstymo operatoriaus (ESO) fizinių asmenų deklaruoti dujų suvartojimo duomenys."
resource: "https://get.data.gov.lt/datasets/gov/eso/fiz_asm_duju_suvartojimas"
tags: [gov, eso, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eso/fiz_asm_duju_suvartojimas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/eso/fiz_asm_duju_suvartojimas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2622/"
    title: "data.gov.lt DCAT-AP — datasets/gov/eso/fiz_asm_duju_suvartojimas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Fizinių asmenų dujų suvartojimas

- **Namespace:** `datasets/gov/eso/fiz_asm_duju_suvartojimas`[^manifest]
- **Manifest CSV:** [datasets/gov/eso/fiz_asm_duju_suvartojimas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eso/fiz_asm_duju_suvartojimas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/eso/fiz_asm_duju_suvartojimas` (`deployed`)[^manifest]
- **Provider:** `eso` — Energijos skirstymo operatorius *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2622/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/eso/fiz_asm_duju_suvartojimas`[^dcat]
- **Portal Title (`@lt`):** Fizinių asmenų dujų suvartojimas[^dcat]
- **Portal Title (`@en`):** Gas consumption of natural persons[^dcat]
- **Issued (`dct:issued`):** `2024-05-13`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-04-19` .. `2025-04-17`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikti Energijos skirstymo operatoriaus (ESO) fizinių asmenų deklaruoti dujų suvartojimo duomenys. Adresai pateikiami 1 kilometro dydžio stačiakampėmis gardelėmis Lietuvos koordinačių sistemoje (LKS-94). Gardelės, kuriose yra 5 arba mažiau vartotojų, nerodomos. Duomenų laiko aprėptis – nuo 2019 m. sausio 1 d. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package contains data on the gas consumption of natural persons of the Energy Distribution Operator (ESO). Addresses are provided in rectangular stalls of 1 kilometre size in the Lithuanian coordinate system (LKS-94). Cells with 5 or fewer users are not displayed. Data time coverage: from 1 January 2019.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [FizAsmDujuSuvartojimas](fiz_asm_duju_suvartojimas/FizAsmDujuSuvartojimas.md) | Fizinių asmenų dujų suvartojimo duomenys | `4` | `iraso_id` | — | `16` | Lentelėje pateikti Energijos skirstymo operatoriaus (ESO) fizinių asmenų dujų suvartojimo duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/eso/fiz_asm_duju_suvartojimas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eso/fiz_asm_duju_suvartojimas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/eso/fiz_asm_duju_suvartojimas (https://data.gov.lt/datasets/2622/)
