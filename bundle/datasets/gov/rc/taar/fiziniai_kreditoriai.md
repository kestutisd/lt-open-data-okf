---
type: Dataset
title: "TAAR pirminiai duomenys (raw data) apie kreditorius (kreditoriai fiziniai asmenys)"
description: "Turto arešto aktų registro nuasmeninti duomenys (RAW DATA) apie kreditorius, kai kreditoriai fiziniai asmenys, jų amžiaus grupę ir pilietybę, turto arešto aktų jų statusus, įregistravimo / išregistravimo datas, areštuojančią instituciją."
resource: "https://get.data.gov.lt/datasets/gov/rc/taar/fiziniai_kreditoriai"
tags: [gov, rc, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/fiziniai_kreditoriai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/taar/fiziniai_kreditoriai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2234/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/taar/fiziniai_kreditoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# TAAR pirminiai duomenys (raw data) apie kreditorius (kreditoriai fiziniai asmenys)

Turto arešto aktų registro nuasmeninti duomenys (RAW DATA) apie kreditorius, kai kreditoriai fiziniai asmenys, jų amžiaus grupę ir pilietybę, turto arešto aktų jų statusus, įregistravimo / išregistravimo datas, areštuojančią instituciją.[^manifest]

- **Namespace:** `datasets/gov/rc/taar/fiziniai_kreditoriai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/taar/fiziniai_kreditoriai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/fiziniai_kreditoriai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/taar/fiziniai_kreditoriai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2234/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/taar/fiziniai_kreditoriai`[^dcat]
- **Portal Title (`@lt`):** TAAR pirminiai duomenys (raw data) apie kreditorius (kreditoriai fiziniai asmenys)[^dcat]
- **Portal Title (`@en`):** TAAR primary data (raw data) about creditors (creditors natural persons)[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2023-02-24` .. `2025-09-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@en`)

Depersonalized data (RAW DATA) of the register of property attachment deeds about creditors, when creditors are natural persons, their age group and citizenship, their statuses of property attachment deeds, dates of registration/deregistration, the foreclosing authority. The geographical sample of the data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [FizinisKreditorius](fiziniai_kreditoriai/FizinisKreditorius.md) | — | `4` | `id` | — | `10` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/taar/fiziniai_kreditoriai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/fiziniai_kreditoriai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/taar/fiziniai_kreditoriai (https://data.gov.lt/datasets/2234/)
