---
type: Dataset
title: "Pacientų registracijos paslaugoms Žalgirio klinikoje"
description: "Vilniaus universiteto ligoninės Žalgirio klinikos sveikatos priežiūros sistema kaupia pacientų asmeninius duomenis, kaip registracija vizitams pas gydytoją."
resource: "https://get.data.gov.lt/datasets/gov/vulzk/registracija"
tags: [gov, vulzk, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vulzk/registracija.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vulzk/registracija.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2661/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vulzk/registracija"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pacientų registracijos paslaugoms Žalgirio klinikoje

- **Namespace:** `datasets/gov/vulzk/registracija`[^manifest]
- **Manifest CSV:** [datasets/gov/vulzk/registracija.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vulzk/registracija.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vulzk/registracija` (`deployed`)[^manifest]
- **Provider:** `vulzk` — VšĮ Vilniaus universiteto ligoninės Žalgirio klinika *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2661/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vulzk/registracija`[^dcat]
- **Portal Title (`@lt`):** Pacientų registracijos paslaugoms Žalgirio klinikoje[^dcat]
- **Portal Title (`@en`):** Patient Registration Services at Žalgiris Clinic[^dcat]
- **Issued (`dct:issued`):** `2024-05-22`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2024-05-17` .. `2025-06-30`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Vilniaus universiteto ligoninės Žalgirio klinikos sveikatos priežiūros sistema kaupia pacientų asmeninius duomenis, kaip registracija vizitams pas gydytoją. Duomenys kaupiami nuo 2010 m. iki 2020 m. Duomenų rinkinys sudarytas iš registracijos identifikatoriaus, datos, kuriai registruotasi, įrašo sukūrimo bei keitimo datų, paciento duomenų: šifruoto identifikatoriaus, lyties, gimimo metų bei gydytojo duomenų: identifikatoriaus ir specialybės. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Žalgiris Clinic health care system at Vilnius University Hospital collects patients' personal data as registration for visits to the doctor. Data shall be collected between 2010 and 2020. The dataset shall consist of the registration identifier, the date of registration, the date of creation and modification of the entry, patient data: encrypted identifier, sex, year of birth and physician data: identifier and specialty.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Registracija](registracija/Registracija.md) | Pacientų registracijos paslaugoms Žalgirio klinikoje | `4` | `registracijos_id` | — | `9` | Vilniaus universiteto ligoninės Žalgirio klinikos sveikatos priežiūros sistema kaupia pacientų asmeninius duomenis, kaip registracija vizitams pas gydytoją. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vulzk/registracija.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vulzk/registracija.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vulzk/registracija (https://data.gov.lt/datasets/2661/)
