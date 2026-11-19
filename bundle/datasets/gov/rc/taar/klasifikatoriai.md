---
type: Dataset
title: "TAAR klasifikatoriai"
description: "Turto arešto aktų registro klasifikatoriai (duomenų rinkinių grupė, viso 4 vnt.): TAAR turto tipų klasifikatorius; TAAR tipų potipių klasifikatorius; TAAR dokumentų statusų klasifikatorius; TAAR areštuojančių institucijų klasifikatorius."
resource: "https://get.data.gov.lt/datasets/gov/rc/taar/klasifikatoriai"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/klasifikatoriai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/taar/klasifikatoriai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2240/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/taar/klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# TAAR klasifikatoriai

Turto arešto aktų registro klasifikatoriai (duomenų rinkinių grupė, viso 4 vnt.): TAAR turto tipų klasifikatorius; TAAR tipų potipių klasifikatorius; TAAR dokumentų statusų klasifikatorius; TAAR areštuojančių institucijų klasifikatorius.[^manifest]

- **Namespace:** `datasets/gov/rc/taar/klasifikatoriai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/taar/klasifikatoriai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/klasifikatoriai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/taar/klasifikatoriai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2240/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/taar/klasifikatoriai`[^dcat]
- **Portal Title (`@lt`):** TAAR klasifikatoriai (duomenų rinkinių grupė, viso 3 vnt.)[^dcat]
- **Portal Title (`@en`):** TAAR classifiers (group of data sets, total 3 pcs.)[^dcat]
- **Issued (`dct:issued`):** `2023-07-21`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-02-24` .. `2023-06-29`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Turto arešto aktų registro klasifikatoriai (duomenų rinkinių grupė, viso 3 vnt.): TAAR turto tipų klasifikatorius; TAAR dokumentų statusų klasifikatorius; TAAR areštuojančių institucijų klasifikatorius.[^dcat]

### Portal Description (`@en`)

Classifiers of the Register of Property Seizure Acts (group of data sets, 3 units in total): TAAR classifier of property types; TAAR document status classifier; TAAR Arresting Authority Classifier.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [TurtoTipas](klasifikatoriai/TurtoTipas.md) | Turto arešto aktų registro turto tipų klasifikatorius | `4` | `kodas` | — | `2` | — |
| [TurtoPotipis](klasifikatoriai/TurtoPotipis.md) | — | `4` | `kodas` | — | `2` | — |
| [DokumentoStatusas](klasifikatoriai/DokumentoStatusas.md) | Turto arešto aktų registro dokumentų statusų klasifikatorius | `4` | `kodas` | — | `2` | — |
| [AI](klasifikatoriai/AI.md) | Turto arešto aktų registro areštuojančių institucijų tipų klasifikatorius | `4` | `tipas` | — | `2` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/taar/klasifikatoriai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/klasifikatoriai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/taar/klasifikatoriai (https://data.gov.lt/datasets/2240/)
