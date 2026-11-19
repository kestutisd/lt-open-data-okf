---
type: Dataset
title: "Parkavimo ir kelių eismo taisyklių pažeidimai Vilniaus mieste"
description: "Rinkinyje skelbiami Vilniaus mieste fiksuoti parkavimo bei kiti kelių eismo taisyklių pažeidimai iš Administracinių nusižengimų administracinio modulio."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/nusizengimai"
tags: [gov, vilniaus_m_sav, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/nusizengimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/nusizengimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3874/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/nusizengimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Parkavimo ir kelių eismo taisyklių pažeidimai Vilniaus mieste

Rinkinyje skelbiami Vilniaus mieste fiksuoti parkavimo bei kiti kelių eismo taisyklių pažeidimai iš Administracinių nusižengimų administracinio modulio. Viena eilutė yra vienas nusižengimas. Duomenys skelbiami nuo 2018 m. Pateikiama informacija apie nusižengimą atlikusio asmens automobilį (valstybinio numerio žymėjimas, registracijos valstybė, elektromobilio ar automobilio nutempimo požymiai) ir pažeidimą (laikas, vietos koordinatės bei duomenys apie pažeistą teisės aktą). Duomenų teikėjas – Vilniaus miesto savivaldybės administracija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/vilniaus_m_sav/nusizengimai`[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/nusizengimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/nusizengimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/nusizengimai` (`deployed`)[^manifest]
- **Provider:** `vilniaus_m_sav` — Vilniaus miesto savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3874/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/nusizengimai`[^dcat]
- **Portal Title (`@lt`):** Parkavimo ir kelių eismo taisyklių pažeidimai Vilniaus mieste[^dcat]
- **Portal Title (`@en`):** Violations of parking and road traffic regulations in Vilnius City[^dcat]
- **Issued (`dct:issued`):** `2025-08-20`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-07-25` .. `2026-10-06`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje skelbiami Vilniaus mieste fiksuoti parkavimo bei kiti kelių eismo taisyklių pažeidimai iš Administracinių nusižengimų administracinio modulio. Viena eilutė yra vienas nusižengimas. Duomenys skelbiami nuo 2018 m. Pateikiama informacija apie nusižengimą atlikusio asmens automobilį (valstybinio numerio žymėjimas, registracijos valstybė, elektromobilio ar automobilio nutempimo požymiai) ir pažeidimą (laikas, vietos koordinatės bei duomenys apie pažeistą teisės aktą). Duomenų teikėjas – Vilniaus miesto savivaldybės administracija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package publishes parking and other road traffic offences recorded in Vilnius City from the Administrative Offences Administration module. One line is one offense. The data shall be published from 2018. Information shall be provided on the vehicle of the offender (registration plate, registration state, signs of towing the electric vehicle or vehicle) and violation (time, local coordinates and data on the breached legislation). Data provider – Vilnius City Municipality Administration. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Pazeidimas](nusizengimai/Pazeidimas.md) | Parkavimo ir kelių eismo taisyklių pažeidimai Vilniaus mieste | `4` | `pazeidimo_id` | — | `14` | Rinkinyje skelbiami Vilniaus mieste fiksuoti parkavimo bei kiti kelių eismo taisyklių pažeidimai iš Administracinių nusižengimų administracinio modulio. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/nusizengimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/nusizengimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/nusizengimai (https://data.gov.lt/datasets/3874/)
