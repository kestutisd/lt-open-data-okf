---
type: Dataset
title: "Laboratorijos tyrimų užsakymai ir atsakymai"
description: "Vilniaus universiteto ligoninės Žalgirio klinikų (VULŽK) laboratorijos informacinė sistema \"Labor IS\" kaupia duomenis apie atliktus laboratorinius tyrimus."
resource: "https://get.data.gov.lt/datasets/gov/vulzk/lab_tyrimai"
tags: [gov, vulzk, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vulzk/lab_tyrimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vulzk/lab_tyrimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2658/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vulzk/lab_tyrimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Laboratorijos tyrimų užsakymai ir atsakymai

- **Namespace:** `datasets/gov/vulzk/lab_tyrimai`[^manifest]
- **Manifest CSV:** [datasets/gov/vulzk/lab_tyrimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vulzk/lab_tyrimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vulzk/lab_tyrimai` (`deployed`)[^manifest]
- **Provider:** `vulzk` — VšĮ Vilniaus universiteto ligoninės Žalgirio klinika *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2658/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vulzk/lab_tyrimai`[^dcat]
- **Portal Title (`@lt`):** Laboratorijos tyrimų užsakymai ir atsakymai (VULŽK)[^dcat]
- **Portal Title (`@en`):** Laboratory test orders and answers (VULGK)[^dcat]
- **Issued (`dct:issued`):** `2024-05-20`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2024-05-15` .. `2025-09-30`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Vilniaus universiteto ligoninės Žalgirio klinikų (VULŽK) laboratorijos informacinė sistema "Labor IS" kaupia duomenis apie atliktus laboratorinius tyrimus. Taikomas vienkartinis duomenų, kurie kaupiami nuo 2006 metų, teikimas. Duomenis papildomai numatoma atnaujinti priėmus sprendimą dėl informacinės sistemos jungimo prie VšĮ Vilniaus universiteto ligoninės Santaros klinikos ir pabaigus aktyviai eksploatuoti esamą sistemą. Duomenys apie VULŽK laboratorijoje atliktus tyrimus, jų užsakymus ir atsakymus. Informacija apie pacientą - gimimo metai, lytis, tyrimo atlikimo data. Pateikti tyrimų atsakymai, matavimo vienetai, norma, skyriai, iš kurių pateikti užsakymai, mėginio paėmimo bei priėmimo data ir laikas. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The information system “Labor IS” of the Laboratory of Žalgiris Clinics (VULŽK) of Vilnius University Hospital collects data on laboratory tests carried out. There shall be a one-off provision of data which has been collected since 2006. The data is further updated upon the decision on the connection of the information system to the Santara Clinic of Vilnius University Hospital and upon the completion of active operation of the existing system. Data on the tests carried out in the VULGIN laboratory, their orders and responses. Patient information - year of birth, gender, date of study. Submitted survey responses, units of measure, rate, sections from which orders have been submitted, date and time of sampling and acceptance.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Atsakymas](lab_tyrimai/Atsakymas.md) | Laboratorijos tyrimų užsakymai ir atsakymai | `4` | `vda_id` | — | `15` | Duomenys apie VULŽK (VšĮ Vilniaus universiteto ligoninės Žalgirio klinikų) laboratorijoje atliktus tyrimus. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vulzk/lab_tyrimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vulzk/lab_tyrimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vulzk/lab_tyrimai (https://data.gov.lt/datasets/2658/)
