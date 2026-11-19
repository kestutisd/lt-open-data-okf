---
type: Dataset
title: "Viešojo transporto GPS padėties duomenys"
description: "Rinkiniuose pateikiama viešojo transporto GPS informacija."
resource: "https://get.data.gov.lt/datasets/gov/viesasis_transport/gps_duomenys"
tags: [gov, viesasis_transport, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/viesasis_transport/gps_duomenys.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/viesasis_transport/gps_duomenys.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3856/"
    title: "data.gov.lt DCAT-AP — datasets/gov/viesasis_transport/gps_duomenys"
    author: "team:vda"
    last_modified: "2026-01-15T00:00:00Z"
---

# Viešojo transporto GPS padėties duomenys

Rinkiniuose pateikiama viešojo transporto GPS informacija. Viešojo transporto padėties informacija matuojama kas 5-20 sekundžių. Duomenys atnaujinami kartą per dieną. Pateikiama informacija apie transporto rūšį, maršrutą, reiso identifikatorių, mašinos numerį, mašinos koordinates matavimo metu WGS-84 ir LKS-94 koordinačių sistemose, greitį, azimutą, reiso pradžią, nuokrypį nuo grafiko sekundėmis, mašinos tipą, matavimo datą ir laiką. Rinkinių objektas – vienos transporto priemonės GPS koordinatės laike. Duomenys nuo 2025-07-01. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/viesasis_transport/gps_duomenys`[^manifest]
- **Manifest CSV:** [datasets/gov/viesasis_transport/gps_duomenys.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/viesasis_transport/gps_duomenys.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/viesasis_transport/gps_duomenys` (`deployed`)[^manifest]
- **Provider:** `viesasis_transport` — Viešojo transporto duomenys *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `7` (7 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3856/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/viesasis_transport/gps_duomenys`[^dcat]
- **Portal Title (`@lt`):** Savivaldybių viešojo transporto GPS padėties duomenys[^dcat]
- **Portal Title (`@en`):** Data on the GPS situation of public transport in municipalities[^dcat]
- **Issued (`dct:issued`):** `2025-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-15`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2025-07-24` .. `2026-09-29`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkiniuose pateikiama viešojo transporto GPS informacija. Viešojo transporto padėties informacija matuojama kas 5-20 sekundžių. Duomenys atnaujinami kartą per dieną. Pateikiama informacija apie transporto rūšį, maršrutą, reiso identifikatorių, mašinos numerį, mašinos koordinates matavimo metu WGS-84 ir LKS-94 koordinačių sistemose, greitį, azimutą, reiso pradžią, nuokrypį nuo grafiko sekundėmis, mašinos tipą, matavimo datą ir laiką. Rinkinių objektas – vienos transporto priemonės GPS koordinatės laike. Duomenys nuo 2025-07-01. Paskutinių 7 dienų duomenys gali būti nepilnos apimties, nes įkėlimas vyksta palaipsniui. Senesni nei 7 dienos duomenys laikomi pilnos apimties. Duomenų teikėjai: VšĮ Klaipėdos keleivinis transportas (Klaipėdos miesto savivaldybė); VšĮ Panevėžio keleivinis transportas (Panevėžio miesto savivaldybė); VšĮ Žaliasis regionas (Tauragės rajono savivaldybė); Alytaus miesto savivaldybė; UAB Kauno autobusai; SĮ Susisiekimo paslaugos (Vilniaus miesto savivaldybė) duomenys nuo 2025-09-01; Druskininkų rajono savivaldybės administracija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

PEAK GPS system[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [KaunasViesasisTransportas](gps_duomenys/KaunasViesasisTransportas.md) | Kauno viešojo transporto GPS padėties duomenys | `4` | `vda_prime_key` | — | `16` | — |
| [VilniusViesasisTransportas](gps_duomenys/VilniusViesasisTransportas.md) | Vilniaus viešojo transporto GPS padėties duomenys | `4` | `vda_prime_key` | — | `16` | — |
| [KlaipedaViesasisTransportas](gps_duomenys/KlaipedaViesasisTransportas.md) | Klaipėdos viešojo transporto GPS padėties duomenys | `4` | `vda_prime_key` | — | `16` | — |
| [TaurageViesasisTransportas](gps_duomenys/TaurageViesasisTransportas.md) | Tauragės viešojo transporto GPS padėties duomenys | `4` | `vda_prime_key` | — | `16` | — |
| [AlytusViesasisTransportas](gps_duomenys/AlytusViesasisTransportas.md) | Alytaus viešojo transporto GPS padėties duomenys | `4` | `vda_prime_key` | — | `16` | — |
| [PanevezysViesasisTransportas](gps_duomenys/PanevezysViesasisTransportas.md) | Panevėžio viešojo transporto GPS padėties duomenys | `4` | `vda_prime_key` | — | `16` | — |
| [DruskininkaiViesasisTransportas](gps_duomenys/DruskininkaiViesasisTransportas.md) | Druskininkų viešojo transporto GPS padėties duomenys | `4` | `vda_prime_key` | — | `16` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/viesasis_transport/gps_duomenys.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/viesasis_transport/gps_duomenys.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/viesasis_transport/gps_duomenys (https://data.gov.lt/datasets/3856/)
