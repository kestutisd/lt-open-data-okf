---
type: Dataset
title: "Saugiųjų dokumentų ir saugiųjų dokumentų blankų registro duomenys"
description: "Valstybės saugiųjų dokumentų ir saugiųjų dokumentų blankų, tokių kaip tokių kaip pasai, asmens tapatybės kortelės, kelionės dokumentai, vairuotojo pažymėjimai, akcizais apmokestinamų prekių banderolės, aukštojo mokslo diplomai ir kt., registro duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vdtat/saugiuju_dokumentu_registras"
tags: [gov, vdtat, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2781/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vdtat/saugiuju_dokumentu_registras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Saugiųjų dokumentų ir saugiųjų dokumentų blankų registro duomenys

Valstybės saugiųjų dokumentų ir saugiųjų dokumentų blankų, tokių kaip tokių kaip pasai, asmens tapatybės kortelės, kelionės dokumentai, vairuotojo pažymėjimai, akcizais apmokestinamų prekių banderolės, aukštojo mokslo diplomai ir kt., registro duomenys[^manifest]

- **Namespace:** `datasets/gov/vdtat/saugiuju_dokumentu_registras`[^manifest]
- **Manifest CSV:** [datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vdtat/saugiuju_dokumentu_registras` (`deployed`)[^manifest]
- **Provider:** `vdtat` — Valstybės dokumentų technologinės apsaugos tarnyba prie FM *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2781/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vdtat/saugiuju_dokumentu_registras`[^dcat]
- **Portal Title (`@lt`):** Dokumentai ir blankai įtraukti į Saugiųjų dokumentų ir saugiųjų dokumentų blankų registrą[^dcat]
- **Portal Title (`@en`):** Documents and forms are entered in the Register of Secure Documents and Secure Documents Forms[^dcat]
- **Issued (`dct:issued`):** `2024-09-27`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-02` .. `2026-09-28`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinį sudaro Valstybės dokumentų technologinės apsaugos tarnybos Saugiųjų dokumentų ir saugiųjų dokumentų blankų registro duomenys. Registro duomenų bazėje nuo 2004 m. sausio 1 d. kaupiama pasų, asmens tapatybės kortelių, kelionės dokumentų, vairuotojo pažymėjimų, akcizais apmokestinamų prekių banderolių, aukštojo mokslo diplomų ir kita informacija. Duomenų teikėjas – Valstybės dokumentų technologinės apsaugos tarnyba prie Finansų ministerijos. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data set shall comprise the data of the Register of Secure Documents and Safe Document Forms of the State Document Technological Protection Service. The Register database has accumulated passports, identity cards, travel documents, driving licences, excise stamps, higher education diplomas and other information since 2010. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Dokumentas](saugiuju_dokumentu_registras/Dokumentas.md) | Saugiųjų dokumentų ir saugiųjų dokumentų blankų aprašomieji duomenys | `4` | `vda_prime_key` | — | `18` | Valstybės saugiųjų dokumentų ir saugiųjų dokumentų blankų, tokių kaip tokių kaip pasai, asmens tapatybės kortelės, kelionės dokumentai, vairuotojo... |
| [Pavyzdys](saugiuju_dokumentu_registras/Pavyzdys.md) | Saugiųjų dokumentų ir blankų pavyzdžių sąrašas | — | `vda_prime_key` | — | `6` | Valstybės saugiųjų dokumentų ir saugiųjų dokumentų blankų, tokių kaip tokių kaip pasai, asmens tapatybės kortelės, kelionės dokumentai, vairuotojo... |
| [ApsaugosPriemone](saugiuju_dokumentu_registras/ApsaugosPriemone.md) | Saugiųjų dokumentų ir blankų apsaugos priemonių sąrašas | — | `vda_prime_key` | — | `6` | Valstybės saugiųjų dokumentų ir saugiųjų dokumentų blankų, tokių kaip tokių kaip pasai, asmens tapatybės kortelės, kelionės dokumentai, vairuotojo... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vdtat/saugiuju_dokumentu_registras (https://data.gov.lt/datasets/2781/)
