---
type: Dataset
title: "TAAR pirminiai duomenys (raw data) apie areštuotą kitų rūšių turtą"
description: "Turto arešto aktų registro nuasmeninti duomenys (RAW DATA) apie areštuojamą kitų rūšių turtą, turto tipą ir potipį, turto arešto aktų jų statusus, įregistravimo / išregistravimo datas."
resource: "https://get.data.gov.lt/datasets/gov/rc/taar/kito_turto_arestai"
tags: [gov, rc, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/kito_turto_arestai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/taar/kito_turto_arestai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2238/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/taar/kito_turto_arestai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# TAAR pirminiai duomenys (raw data) apie areštuotą kitų rūšių turtą

Turto arešto aktų registro nuasmeninti duomenys (RAW DATA) apie areštuojamą kitų rūšių turtą, turto tipą ir potipį, turto arešto aktų jų statusus, įregistravimo / išregistravimo datas.[^manifest]

- **Namespace:** `datasets/gov/rc/taar/kito_turto_arestai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/taar/kito_turto_arestai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/kito_turto_arestai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/taar/kito_turto_arestai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2238/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/taar/kito_turto_arestai`[^dcat]
- **Portal Title (`@lt`):** TAAR pirminiai duomenys (raw data) apie areštuojamą kitų rūšių turtą[^dcat]
- **Portal Title (`@en`):** TAAR primary data (raw data) on seized other types of property[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2023-02-24` .. `2023-11-23`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@en`)

Depersonalized data (RAW DATA) of the Register of Property Seizure Acts on other types of property to be seized, type and subtype of property, status of property seizure acts, registration/deregistration dates. The geographical sample of the data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [KitoTurtoArestas](kito_turto_arestai/KitoTurtoArestas.md) | — | `4` | `id` | — | `8` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/taar/kito_turto_arestai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/kito_turto_arestai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/taar/kito_turto_arestai (https://data.gov.lt/datasets/2238/)
