---
type: Dataset
title: "Sveikatos priežiūros įstaigų įsigytos medicininės priemonės"
description: "\"Duomenų rinkinyje pateikiami įrašai apie sveikatos priežiūros įstaigų įsigytas medicinines priemones."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/medicinos_priemones"
tags: [gov, vaspvt, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_priemones.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/medicinos_priemones.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2928/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vaspvt/medicinos_priemones"
    author: "team:vda"
    last_modified: "2026-07-02T00:00:00Z"
---

# Sveikatos priežiūros įstaigų įsigytos medicininės priemonės

"Duomenų rinkinyje pateikiami įrašai apie sveikatos priežiūros įstaigų įsigytas medicinines priemones. Viena eilutė atitinka vieną įsigytą priemonę. Įrašai apie įsigytas medicinines priemones pradėti fiksuoti apytiksliai nuo 2010 m. Rinkinį sudaro: priemonės pavadinimas, modelis, CE (pranc. Conformité Européene) žyma, CE numeris, priemonės savininko JAR kodas ir pavadinimas, priemonės pagaminimo, įsigyjimo, naudojimo pradžios ir nutraukimo datos bei nutraukimo priežastis. Duomenų teikėjas: Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba prie Sveikatos apsaugos ministerijos. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt."[^manifest]

- **Namespace:** `datasets/gov/vaspvt/medicinos_priemones`[^manifest]
- **Manifest CSV:** [datasets/gov/vaspvt/medicinos_priemones.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_priemones.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/medicinos_priemones` (`deployed`)[^manifest]
- **Provider:** `vaspvt` — Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2928/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vaspvt/medicinos_priemones`[^dcat]
- **Portal Title (`@lt`):** Sveikatos priežiūros įstaigų įsigytos medicininės priemonės[^dcat]
- **Portal Title (`@en`):** Medical supplies purchased by health care institutions[^dcat]
- **Issued (`dct:issued`):** `2025-02-05`[^dcat]
- **Last Modified (`dct:modified`):** `2026-07-02`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2025-02-03` .. `2025-02-05`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiami įrašai apie sveikatos priežiūros įstaigų įsigytas medicinines priemones. Viena eilutė atitinka vieną įsigytą priemonę. Įrašai apie įsigytas medicinines priemones pradėti fiksuoti apytiksliai nuo 2010 m. Rinkinį sudaro: priemonės pavadinimas, modelis, CE (pranc. Conformité Européene) žyma, CE numeris, priemonės savininko JAR kodas ir pavadinimas, priemonės pagaminimo, įsigyjimo, naudojimo pradžios ir nutraukimo datos bei nutraukimo priežastis. Duomenų teikėjas: Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba prie Sveikatos apsaugos ministerijos. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The dataset shall include records of medical devices purchased by healthcare institutions. One line corresponds to one purchase. Records of medical devices purchased started to be recorded around 2010. The kit consists of: name, model, CE. (conformité Européene) mark, CE number, Jaris code and name of the owner of the device, reason for the manufacture, purchase, start-up and termination of the device. Data provider: State Health Care Accreditation Service under the Ministry of Health. Contact the atverimas@stat.gov.lt for technical questions or possible errors[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [MedicininePriemone](medicinos_priemones/MedicininePriemone.md) | Sveikatos priežiūros įstaigų įsigytos medicininės priemonės | `4` | `pri_id` | — | `12` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/medicinos_priemones.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_priemones.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vaspvt/medicinos_priemones (https://data.gov.lt/datasets/2928/)
