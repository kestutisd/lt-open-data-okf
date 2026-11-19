---
type: Dataset
title: "Fitosanitarinių tikrinimų duomenys"
description: "Pateikiama informacija apie atliktus fitosanitarinius tikrinimus (tikrinimą atlikęs teritorinis padalinys; tikrinimo data; žyma, kad tikrinami ne LR ūkio subjektai; metodinė sritis; tikrinimo sritis; tikrinimo pobūdis; rizikingumo kategorija; tikrinimo rūšis; pildyti veiklos..."
resource: "https://get.data.gov.lt/datasets/gov/vat/fitosanitarijos_tikrinimai"
tags: [gov, vat, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r8_fitosanitarijos_tikrinimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vat/r8_fitosanitarijos_tikrinimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1864/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/fitosanitarijos_tikrinimai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Fitosanitarinių tikrinimų duomenys

- **Namespace:** `datasets/gov/vat/fitosanitarijos_tikrinimai`[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r8_fitosanitarijos_tikrinimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r8_fitosanitarijos_tikrinimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/fitosanitarijos_tikrinimai` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1864/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė augalininkystės tarnyba prie Žemės ūkio ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vat/fitosanitarijos_tikrinimai`[^dcat]
- **Portal Title (`@lt`):** Fitosanitarinių tikrinimų duomenys[^dcat]
- **Portal Title (`@en`):** Data from phytosanitary inspections[^dcat]
- **Issued (`dct:issued`):** `2023-06-26`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2023-06-26` .. `2026-10-29`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Pateikiama informacija apie atliktus fitosanitarinius tikrinimus (tikrinimą atlikęs teritorinis padalinys; tikrinimo data; žyma, kad tikrinami ne LR ūkio subjektai; metodinė sritis; tikrinimo sritis; tikrinimo pobūdis; rizikingumo kategorija; tikrinimo rūšis; pildyti veiklos priežiūros klausimynai; ūkio subjektams nustatyti veiklos neatitikimai (pastabos, mažareikšmiai ir kt. neatitikimai); tikrinamas objektas; žyma apie ūkio subjekto informavimą dėl numatomo patikrinimo; žyma, ar paimtas mėginys; įtariami kenksmingi organizmai; rasti kenksmingi organizmai; registruotas kenkėjo židinys; žyma, kad tikrinta turgavietėje; žyma, kad tikrinta su kita institucija). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Information on the performed phytosanitary inspections is provided (territorial unit that performed the inspection; date of inspection; notation that non-Lithuanian economic entities are inspected; methodological area; scope of inspection; type of inspection; type of inspection; completed activity questionnaires; remarks, minor discrepancies, etc.); other institution)[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Patikrinimas](fitosanitarijos_tikrinimai/Patikrinimas.md) | Pateikiama informacija apie atliktus fitosanitarinius tikrinimus (tikrinimą atlikęs teritorinis padalinys; tikrinimo data; žyma, kad tikrinami ne LR ūkio subjektai; metodinė sritis; tikrinimo sritis; tikrinimo pobūdis; rizikingumo kategorija; tikrinimo rūšis; pildyti veiklos priežiūros klausimynai; ūkio subjektams nustatyti veiklos neatitikimai (pastabos, mažareikšmiai ir kt. neatitikimai); tikrinamas objektas; žyma apie ūkio subjekto informavimą dėl numatomo patikrinimo; žyma, ar paimtas mėginys; įtariami kenksmingi organizmai; rasti kenksmingi organizmai; registruotas kenkėjo židinys; žyma, kad tikrinta turgavietėje; žyma, kad tikrinta su kita institucija) | `4` | `id` | `open` | `7` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r8_fitosanitarijos_tikrinimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r8_fitosanitarijos_tikrinimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/fitosanitarijos_tikrinimai (https://data.gov.lt/datasets/1864/)
