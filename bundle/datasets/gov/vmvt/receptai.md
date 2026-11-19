---
type: Dataset
title: "Duomenys apie veterinarinius vaistus bei jų išrašymus"
description: "Rinkinyje pateikiami Valstybinės maisto ir veterinarijos tarnybos sistemoje nuo 2022 metų kaupiami ir saugomi veterinarų išrašytų receptų veterinariniams vaistams įsigyti duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/receptai"
tags: [gov, vmvt, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/receptai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vmvt/receptai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2820/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmvt/receptai"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# Duomenys apie veterinarinius vaistus bei jų išrašymus

- **Namespace:** `datasets/gov/vmvt/receptai`[^manifest]
- **Manifest CSV:** [datasets/gov/vmvt/receptai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/receptai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/receptai` (`deployed`)[^manifest]
- **Provider:** `vmvt` — Valstybinė maisto ir veterinarijos tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2820/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vmvt/receptai/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Veterinarinių klinikų išrašyti vaistų receptai[^dcat]
- **Portal Title (`@en`):** Prescriptions for medicinal products issued by veterinary clinics[^dcat]
- **Issued (`dct:issued`):** `2024-10-15`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-20`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-10-03` .. `2024-12-17`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami Valstybinės maisto ir veterinarijos tarnybos sistemoje nuo 2022 metų kaupiami ir saugomi veterinarų išrašytų receptų veterinariniams vaistams įsigyti duomenys. Duomenų rinkinį sudaro: recepto numeris, vaistas, gyvūno rūšies identifikacinis numeris, lytis, vaistus paskyręs veterinaras ar įstaiga. Viena duomenų rinkinio eilutė atitinka vieno recepto vaistą. Duomenų teikėjas – Valstybinė maisto ir veterinarijos tarnyba. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package includes data collected and stored in the system of the State Food and Veterinary Service from 2022 on prescriptions issued by veterinarians for the purchase of veterinary medicines. The dataset shall comprise: prescription number, medicinal product, animal species identification number, sex, veterinarian or body who prescribed the medicinal product. One line of the dataset corresponds to a single prescription drug. Technical questions or possible errors may be referred to the atverimas@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [IsrasytasReceptas](receptai/IsrasytasReceptas.md) | Veterinarinių klinikų išrašyti vaistų receptai | `4` | `vda_prime_key` | — | `19` | Rinkinyje pateikiamas Valstybinė maisto ir veterinarijos tarnybos sistemos duomenys apie veterinarų išrašytus receptus gyvūnų vaistams įsigyti. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/receptai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/receptai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmvt/receptai (https://data.gov.lt/datasets/2820/)
