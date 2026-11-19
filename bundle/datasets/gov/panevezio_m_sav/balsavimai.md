---
type: Dataset
title: "Panevėžio miesto tarybos posėdžių balsavimų rezultatai"
description: "Rinkinyje pateikiami Panevėžio miesto tarybos bendri rezultatai ir asmeniniai balsavimai dėl Tarybos posėdžiuose teikiamų klausimų."
resource: "https://get.data.gov.lt/datasets/gov/panevezio_m_sav/balsavimai"
tags: [gov, panevezio_m_sav, deployed, cadence-annual_3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/balsavimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/panevezio_m_sav/balsavimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2715/"
    title: "data.gov.lt DCAT-AP — datasets/gov/panevezio_m_sav/balsavimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Panevėžio miesto tarybos posėdžių balsavimų rezultatai

Rinkinyje pateikiami Panevėžio miesto tarybos bendri rezultatai ir asmeniniai balsavimai dėl Tarybos posėdžiuose teikiamų klausimų. Duomenys apima laikotarpį nuo 2023m. balandžio iki šių dienų. Iškilus klausimams, kreiptis į Valstybės duomenų valdysenos komandą: vdv@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/panevezio_m_sav/balsavimai`[^manifest]
- **Manifest CSV:** [datasets/gov/panevezio_m_sav/balsavimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/balsavimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/panevezio_m_sav/balsavimai` (`deployed`)[^manifest]
- **Provider:** `panevezio_m_sav` — Panevėžio miesto savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2715/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/panevezio_m_sav/balsavimai`[^dcat]
- **Portal Title (`@lt`):** Panevėžio miesto tarybos posėdžių balsavimų rezultatai[^dcat]
- **Portal Title (`@en`):** Results of votes of Panevezys City Council meetings[^dcat]
- **Issued (`dct:issued`):** `2024-07-23`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL_3` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL_3`)[^dcat]
- **Distribution Date Span:** `2024-12-19` .. `2026-09-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami agreguoti Panevėžio miesto tarybos narių balsavimų rezultatai dėl posėdžių metu iškeltų klausimų nuo 2023m. iki šių dienų. Pateikiami agreguoti balsavimų rezultatai: tarybos narių, balsavusių už, prieš ir susilaikiusių, skaičius; taip pat nurodoma, ar balsavimo metu susidarė kvorumas ir ar pasiūlymas buvo priimtas. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package includes personal votes of Panevezys City Council members on the issues raised at Council meetings. Data were collected in this database from 2011 to the year, and the data being opened covers the period from 2023 to the present day.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Balsavimas](balsavimai/Balsavimas.md) | Panevėžio miesto tarybos narių asmeniniai balsavimų rezultatai | `4` | `vda_id` | — | `9` | Lentelėje pateikiami Panevėžio miesto tarybos narių asmeniniai balsavimai dėl Tarybos posėdžiuose teikiamų klausimų. |
| [Sesija](balsavimai/Sesija.md) | Panevėžio miesto tarybos posėdžių balsavimų rezultatai | `4` | `vda_id` | — | `14` | Lentelėje pateikiami agreguoti Panevėžio miesto tarybos narių balsavimų rezultatai dėl posėdžių metu iškeltų klausimų nuo 2023m. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/panevezio_m_sav/balsavimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/balsavimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/panevezio_m_sav/balsavimai (https://data.gov.lt/datasets/2715/)
