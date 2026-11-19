---
type: Dataset
title: "Metinis nedarbo lygis"
description: "Metinė visų nuolatinių Lietuvos gyventojų statistinė informacija apie bedarbių ir ekonomiškai neaktyvių gyventojų skaičių, jų pasiskirstymą pagal amžiaus grupes, lytį, gyvenamąją vietą ir regioną nuo 1998 metų."
resource: "https://get.data.gov.lt/datasets/gov/lsd/statistika/metinis_nedarbo_lygis"
tags: [gov, lsd, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistika/metinis_nedarbo_lygis.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/statistika/metinis_nedarbo_lygis.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2463/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/statistika/metinis_nedarbo_lygis"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Metinis nedarbo lygis

- **Namespace:** `datasets/gov/lsd/statistika/metinis_nedarbo_lygis`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/statistika/metinis_nedarbo_lygis.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistika/metinis_nedarbo_lygis.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/statistika/metinis_nedarbo_lygis` (`deployed`)[^manifest]
- **Provider:** `lsd` — Oficialiosios statistikos portalo rodiklių duomenų bazės rinkiniai *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2463/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/statistika/metinis_nedarbo_lygis`[^dcat]
- **Portal Title (`@lt`):** Metinis nedarbo lygis[^dcat]
- **Portal Title (`@en`):** Annual: Unemployment rate (by target age groups and gender)[^dcat]
- **Issued (`dct:issued`):** `2023-12-15`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2026-02-21` .. `2026-04-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Metinė visų nuolatinių Lietuvos gyventojų statistinė informacija apie bedarbių ir ekonomiškai neaktyvių gyventojų skaičių, jų pasiskirstymą pagal amžiaus grupes, lytį, gyvenamąją vietą ir regioną nuo 1998 metų. Rodiklis išreiškiamas bedarbių ir darbo jėgos santykiu. Naudojami LR Administracinių vienetų ir gyvenamųjų vietovių klasifikatorius (LR AVGVK 2018) ir Bendras teritorinių statistinių vienetų klasifikatorius (NUTS). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Annual statistical information of all permanent residents of Lithuania on the number of unemployed and economically inactive residents, their distribution by age group, gender, place of residence since 1998. The indicator is expressed in the ratio between the unemployed and the labour force. The classification of administrative units and residential areas of the Republic of Lithuania (LR AVGVK 2018) and the Common Classification of Territorial Statistical Units (NUTS) shall be used.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [S3R347M30309011](metinis_nedarbo_lygis/S3R347M30309011.md) | Metinis nedarbo lygis (pagal amžiaus grupes, lytį ir gyvenamąją vietovę) | `4` | `vda_id` | — | `13` | Metinė visų nuolatinių Lietuvos gyventojų statistinė informacija apie bedarbių ir ekonomiškai neaktyvių gyventojų skaičių, jų pasiskirstymą pagal amžiaus... |
| [S3R347M3030903](metinis_nedarbo_lygis/S3R347M3030903.md) | Metinis nedarbo lygis (pagal lytį ir regionus) | `4` | `vda_id` | — | `14` | Metinė visų nuolatinių Lietuvos gyventojų statistinė informacija apie bedarbių ir ekonomiškai neaktyvių gyventojų skaičių, jų pasiskirstymą pagal regioną... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/statistika/metinis_nedarbo_lygis.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistika/metinis_nedarbo_lygis.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/statistika/metinis_nedarbo_lygis (https://data.gov.lt/datasets/2463/)
