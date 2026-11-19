---
type: Dataset
title: "Lietuvos metrologijos inspekcijos įmonių patikrinimų ketvirčio planai"
description: "Duomenų rinkinyje kaupiami Lietuvos metrologijos inspekcijos įmonių patikrinimo ketvirčio planų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lmi/teis_metrol_patikrinimu_planai"
tags: [gov, lmi, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmi/teis_metrol_patikrinimu_planai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/lmi/teis_metrol_patikrinimu_planai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2832/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lmi/teis_metrol_patikrinimu_planai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Lietuvos metrologijos inspekcijos įmonių patikrinimų ketvirčio planai

- **Namespace:** `datasets/gov/lmi/teis_metrol_patikrinimu_planai`[^manifest]
- **Manifest CSV:** [datasets/gov/lmi/teis_metrol_patikrinimu_planai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmi/teis_metrol_patikrinimu_planai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lmi/teis_metrol_patikrinimu_planai` (`deployed`)[^manifest]
- **Provider:** `lmi` — Lietuvos metrologijos inspekcija *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2832/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lmi/teis_metrol_patikrinimu_planai/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Teisinės metrologijos ketvirčių patikrinimų planai[^dcat]
- **Portal Title (`@en`):** Legal Metrology Quarterly Verification Plans[^dcat]
- **Issued (`dct:issued`):** `2024-11-11`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2024-10-25` .. `2025-10-25`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje kaupiami Lietuvos metrologijos inspekcijos įmonių patikrinimo ketvirčio planų duomenys. Viena eilutė rinkinyje atitinka vieną planuojamą patikrinimą. Rinkinyje nurodomos įmonės, jų rizika, adresas ir (arba) veiklos vieta, veiklos rūšis pagal ekonominės veiklos rūšies klasifikatoriaus antrąją redakciją. Rinkinį sudaro nuo 2021 metų sausio 1 dienos sukaupti duomenys. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data collection shall compile the data of the quarterly plans of the inspection of enterprises of the Lithuanian Metrology Inspectorate. One line in the set corresponds to one planned check. The package shall identify the undertakings, their risk, address and/or place of activity, the type of activity in accordance with the second version of the economic activity classification. The collection consists of data accumulated from January 1, 2021. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [TeisMetrolPatikrinimPlanas](teis_metrol_patikrinimu_planai/TeisMetrolPatikrinimPlanas.md) | Lietuvos metrologijos inspekcijos įmonių patikrinimų ketvirčio planai | `4` | `vda_prime_key` | — | `13` | Duomenų rinkinyje kaupiami Lietuvos metrologijos inspekcijos įmonių patikrinimo ketvirčio planų duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lmi/teis_metrol_patikrinimu_planai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmi/teis_metrol_patikrinimu_planai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lmi/teis_metrol_patikrinimu_planai (https://data.gov.lt/datasets/2832/)
