---
type: Dataset
title: "TAAR pirminiai duomenys (raw data) apie turto arešto aktus"
description: "Turto arešto aktų registro nuasmeninti duomenys (RAW DATA) apie turto arešto aktus, jų statusus, įregistravimo / išregistravimo datas, areštuojančią instituciją, turto arešto mastą (rėžius), jeigu nustatomas."
resource: "https://get.data.gov.lt/datasets/gov/rc/taar/turto_aresto_aktai"
tags: [gov, rc, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/turto_aresto_aktai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/taar/turto_aresto_aktai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2231/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/taar/turto_aresto_aktai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# TAAR pirminiai duomenys (raw data) apie turto arešto aktus

Turto arešto aktų registro nuasmeninti duomenys (RAW DATA) apie turto arešto aktus, jų statusus, įregistravimo / išregistravimo datas, areštuojančią instituciją, turto arešto mastą (rėžius), jeigu nustatomas.[^manifest]

- **Namespace:** `datasets/gov/rc/taar/turto_aresto_aktai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/taar/turto_aresto_aktai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/turto_aresto_aktai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/taar/turto_aresto_aktai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2231/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/taar/turto_aresto_aktai`[^dcat]
- **Portal Title (`@lt`):** TAAR pirminiai duomenys (raw data) apie turto arešto aktus[^dcat]
- **Portal Title (`@en`):** TAAR raw data on foreclosure acts[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2023-02-24` .. `2023-11-23`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@en`)

Depersonalized data (RAW DATA) of the register of asset seizure acts, their statuses, registration/deregistration dates, seizing authority, extent of asset seizure, if determined. The geographical sample of the data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [TurtoArestoAktas](turto_aresto_aktai/TurtoArestoAktas.md) | — | `4` | `id` | — | `8` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/taar/turto_aresto_aktai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/turto_aresto_aktai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/taar/turto_aresto_aktai (https://data.gov.lt/datasets/2231/)
