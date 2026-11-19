---
type: Dataset
title: "Varėnos rajono savivaldybės mokyklų informacija"
description: "Varėnos rajono savivaldybės mokyklų personalas Rinkinyje pateikiamas Varėnos rajono savivaldybės mokyklos personalo sąrašas."
resource: "https://get.data.gov.lt/datasets/gov/varenos_r_sav/mokyklos"
tags: [gov, varenos_r_sav, deployed, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/varenos_r_sav/mokyklu_personalas.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/varenos_r_sav/mokyklu_personalas.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2810/"
    title: "data.gov.lt DCAT-AP — datasets/gov/varenos_r_sav/mokyklos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Varėnos rajono savivaldybės mokyklų informacija

- **Namespace:** `datasets/gov/varenos_r_sav/mokyklos`[^manifest]
- **Manifest CSV:** [datasets/gov/varenos_r_sav/mokyklu_personalas.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/varenos_r_sav/mokyklu_personalas.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/varenos_r_sav/mokyklos` (`deployed`)[^manifest]
- **Provider:** `varenos_r_sav` — Varėnos rajono savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2810/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/varenos_r_sav/mokyklos`[^dcat]
- **Portal Title (`@lt`):** Varėnos rajono savivaldybės mokyklų personalas[^dcat]
- **Portal Title (`@en`):** Staff of schools in the district of Varėna[^dcat]
- **Issued (`dct:issued`):** `2024-09-25`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL_2` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL_2`)[^dcat]
- **Distribution Date Span:** `2024-09-20` .. `2024-09-23`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Varėnos rajono savivaldybės mokyklų personalas Rinkinyje pateikiamas Varėnos rajono savivaldybės mokyklos personalo sąrašas. Pateikiama tokia informacija kaip asmens lytis, užšifruotas asmens kodas, asmens amžius dešimtmečiais, pareigos, darbo laikotarpis ir ugdymo įstaiga. Viena eilutė atitinka vieno asmens darbo laikotarpį tam tikrose pareigose, tam tikroje įstaigoje. Duomenys pateikiami asmenų kurie įsidarbino nuo 1959 metų. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Staff of schools in the district of Varėna The package includes a list of staff of the Varena District Municipality School. Information such as the sex of the person, the encrypted personal number, the age of the person for decades, the duties, the period of work and the educational establishment shall be provided. One line corresponds to the period of work of one person in a particular position, in a particular institution. The data are provided by those who have been in employment since 1959. ENQUIRIES: State Data Control Opening Team: atverimas@stat.gov.lt[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [MokyklosPersonalas](mokyklos/MokyklosPersonalas.md) | Varėnos rajono savivaldybės mokyklų personalas | `4` | `vda_prime_key` | — | `10` | Rinkinyje pateikiamas Varėnos rajono savivaldybės mokyklos personalo sąrašas. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/varenos_r_sav/mokyklu_personalas.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/varenos_r_sav/mokyklu_personalas.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/varenos_r_sav/mokyklos (https://data.gov.lt/datasets/2810/)
