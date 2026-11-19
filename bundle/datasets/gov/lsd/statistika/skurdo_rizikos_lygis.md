---
type: Dataset
title: "Skurdo rizikos lygis"
description: "Metinė visų Lietuvos privačių namų ūkių ir nuolatinių Lietuvos gyventojų statistinė informacija apie asmenų, kurių ekvivalentinės piniginės disponuojamosios pajamos mažesnės už skurdo rizikos ribą, dalį, jų pasiskirstymą pagal amžių ir pilietybę, pajamų kvintilines grupes..."
resource: "https://get.data.gov.lt/datasets/gov/lsd/statistika/skurdo_rizikos_lygis"
tags: [gov, lsd, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistika/skurdo_rizikos_lygis.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/statistika/skurdo_rizikos_lygis.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2549/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/statistika/skurdo_rizikos_lygis"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Skurdo rizikos lygis

- **Namespace:** `datasets/gov/lsd/statistika/skurdo_rizikos_lygis`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/statistika/skurdo_rizikos_lygis.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistika/skurdo_rizikos_lygis.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/statistika/skurdo_rizikos_lygis` (`deployed`)[^manifest]
- **Provider:** `lsd` — Oficialiosios statistikos portalo rodiklių duomenų bazės rinkiniai *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2549/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/statistika/skurdo_rizikos_lygis`[^dcat]
- **Portal Title (`@lt`):** Skurdo rizikos lygis[^dcat]
- **Portal Title (`@en`):** Poverty risk level[^dcat]
- **Issued (`dct:issued`):** `2024-02-14`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2024-03-02` .. `2025-04-24`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Metinė visų Lietuvos privačių namų ūkių ir nuolatinių Lietuvos gyventojų statistinė informacija apie asmenų, kurių ekvivalentinės piniginės disponuojamosios pajamos mažesnės už skurdo rizikos ribą, dalį, jų pasiskirstymą pagal amžių ir pilietybę, pajamų kvintilines grupes, amžių ir gimimo šalį nuo 2021 m. Pagrindiniu skurdo kriterijumi laikoma skurdo rizikos riba, lygi 60 proc. ekvivalentinių piniginių disponuojamųjų pajamų medianos. Naudojami LR Administracinių vienetų ir gyvenamųjų vietovių klasifikatorius (LR AVGVK 2018) ir Bendras teritorinių statistinių vienetų klasifikatorius (NUTS). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Annual statistical information of all private households of Lithuania and residents of Lithuania on the share of persons whose equivalent cash disposable income is below the poverty risk threshold, their distribution by age and citizenship, income quintile groups, age and country of birth from 2021. The main poverty criterion shall be the poverty risk threshold equal to 60% of the median equivalent cash disposable income. The classification of administrative units and residential areas of the Republic of Lithuania (LR AVGVK 2018) and the Common Classification of Territorial Statistical Units (NUTS) shall be used.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [S3R453M3080360](skurdo_rizikos_lygis/S3R453M3080360.md) | Skurdo rizikos lygis (pagal amžių ir pilietybę) | `4` | `vda_id` | — | `11` | Metinė visų Lietuvos privačių namų ūkių ir nuolatinių Lietuvos gyventojų statistinė informacija apie asmenų, kurių ekvivalentinės piniginės disponuojamosios... |
| [S3R453M3080361](skurdo_rizikos_lygis/S3R453M3080361.md) | Skurdo rizikos lygis (pagal pajamų kvintilines grupes) | `4` | `vda_id` | — | `9` | Metinė visų Lietuvos privačių namų ūkių ir nuolatinių Lietuvos gyventojų statistinė informacija apie asmenų, kurių ekvivalentinės piniginės disponuojamosios... |
| [S3R453M3080362](skurdo_rizikos_lygis/S3R453M3080362.md) | Skurdo rizikos lygis (pagal amžių ir gimimo šalį) | `4` | `vda_id` | — | `11` | Metinė visų Lietuvos privačių namų ūkių ir nuolatinių Lietuvos gyventojų statistinė informacija apie asmenų, kurių ekvivalentinės piniginės disponuojamosios... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/statistika/skurdo_rizikos_lygis.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistika/skurdo_rizikos_lygis.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/statistika/skurdo_rizikos_lygis (https://data.gov.lt/datasets/2549/)
