---
type: Dataset
title: "Mokiniai einamiesiems mokslo metams"
description: "Lentelėje pateikta informacija apie einamųjų mokslo metų bendrojo, profesinio, ikimokyklinio, priešmokyklinio, neformalaus ugdymo mokinius iš Nacionalinės Švietimo agentūros (NŠA) Mokinių registro (MR)."
resource: "https://get.data.gov.lt/datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams"
tags: [gov, nsa, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2687/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Mokiniai einamiesiems mokslo metams

- **Namespace:** `datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams`[^manifest]
- **Manifest CSV:** [datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams` (`deployed`)[^manifest]
- **Provider:** `nsa` — Nacionalinė švietimo agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2687/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams`[^dcat]
- **Portal Title (`@lt`):** Mokiniai einamiesiems mokslo metams[^dcat]
- **Portal Title (`@en`):** Pupils for the current school year[^dcat]
- **Issued (`dct:issued`):** `2024-06-25`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-06-17` .. `2026-06-15`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lentelėje pateikta informacija apie einamųjų mokslo metų bendrojo, profesinio, ikimokyklinio, priešmokyklinio, neformalaus ugdymo mokinius iš Nacionalinės Švietimo agentūros (NŠA) Mokinių registro (MR). Šioje lentelėje matoma informacija tik tų mokinių, kurių mokymosi pradžios data yra lygi arba senesnė einamųjų mokslo metų pabaigos datai ir kurių mokymosi pabaigos data yra naujesnė arba lygi einamųjų mokslo metų pradžios datai arba yra tuščia, dar neįrašyta (galioja_nuo ≤ einamųjų mokslo metų pabaiga IR (galioja_iki ≥ einamųjų mokslo metų pradžia ARBA galioja_iki - neįrašyta, tuščia)). Pavyzdžiui, kai einamieji mokslo metai yra nuo 2023-09-01 iki 2024-08-31, lentelėje bus matomi įrašai tų mokinių, kurie pradėjo mokytis tam tikroje klasėje arba būrelyje nuo 2023-09-01 ir baigė mokytis 2024-06-01, tačiau nebus matomi įrašai tų mokinių, kurie pradėjo mokytis 2022-09-01 ir baigė mokytis 2023-06-01. Siekiant sustiprinti asmens duomenų apsaugą duomenys buvo triukšminti. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The table provides information on pupils in general, vocational, pre-school, pre-primary, non-formal education of the current school year from the National Agency for Education (NESA) Pupil Register (MR). This table shows information only for pupils whose starting date is equal to or older than the end date of the current school year and whose end date is newer or equal to the beginning date of the current school year OR is empty, not yet recorded (valid from ≤ the end of the current school year AND (valid until ≥ the beginning of the current school year OR valid until - unrecorded, blank). For example, when the current school year is between 2023-09-01 and 2024-08-31, the table will show records of those pupils who started learning in a particular class or group from 2023-09-01 and graduated from 2024-06-01, but will not see records of those pupils who started learning from 2022-09-01 and graduated from 2023-06-01. Data were noisy to enhance the protection of personal data. Contact the atverimas@stat.gov.lt for technical questions or possible errors[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [MokinysmMetams](mokiniai_einamiesiems_mokslo_metams/MokinysmMetams.md) | Mokiniai einamiesiems mokslo metams | `4` | `iraso_id` | — | `23` | Lentelėje pateikta informacija apie einamųjų mokslo metų bendrojo, profesinio, ikimokyklinio, priešmokyklinio, neformalaus ugdymo mokinius iš Nacionalinės... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nsa/mr/mokiniai_einamiesiems_mokslo_metams (https://data.gov.lt/datasets/2687/)
