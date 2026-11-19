---
type: Dataset
title: "Vilniaus miesto savivaldybės darbo skelbimai"
description: "Rinkinyje pateikiamos Vilniaus miesto savivaldybės administracijos skelbiamos laisvos darbo vietos savivaldybės ugdymo, gydymo bei kitose biudžetinėse įstaigose Vilniaus mieste."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/laisvos_darbo_vietos"
tags: [gov, vilniaus_m_sav, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/darbo_vietos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/darbo_vietos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3851/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/laisvos_darbo_vietos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Vilniaus miesto savivaldybės darbo skelbimai

Rinkinyje pateikiamos Vilniaus miesto savivaldybės administracijos skelbiamos laisvos darbo vietos savivaldybės ugdymo, gydymo bei kitose biudžetinėse įstaigose Vilniaus mieste. Duomenys apima laikotarpį nuo 2021m. iki dabar. Rinkinio objektas - vienos darbo vietos skelbimas. Pateikiami duomenys apie darbovietę (adresas, koordinatės, įstaigos tipas) ir siūlomą darbo vietą (pareigos, darbo vietos aprašymas, reikalavimai, atlyginimas, kontaktai pasiteiravimui). Duomenų teikėjas: Vilniaus miesto savivaldybės administracija Vilniaus miesto savivaldybės administracija Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/vilniaus_m_sav/laisvos_darbo_vietos`[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/darbo_vietos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/darbo_vietos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/laisvos_darbo_vietos` (`deployed`)[^manifest]
- **Provider:** `vilniaus_m_sav` — Vilniaus miesto savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3851/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/laisvos_darbo_vietos`[^dcat]
- **Portal Title (`@lt`):** Vilniaus miesto savivaldybės darbo skelbimai[^dcat]
- **Portal Title (`@en`):** Job advertisements of Vilnius City Municipality[^dcat]
- **Issued (`dct:issued`):** `2025-06-13`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `WEEKLY` (`http://publications.europa.eu/resource/authority/frequency/WEEKLY`)[^dcat]
- **Distribution Date Span:** `2026-04-01` .. `2026-04-08`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiamos Vilniaus miesto savivaldybės administracijos skelbiamos laisvos darbo vietos savivaldybės ugdymo, gydymo bei kitose biudžetinėse įstaigose Vilniaus mieste. Duomenys apima laikotarpį nuo 2021 m. iki dabar. Rinkinio objektas – vienos darbo vietos skelbimas. Pateikiami duomenys apie darbovietę (adresas, koordinatės, įstaigos tipas) ir siūlomą darbo vietą (pareigos, darbo vietos aprašymas, reikalavimai, atlyginimas, kontaktai pasiteiravimui). Duomenų teikėjas – Vilniaus miesto savivaldybės administracija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package presents vacancies announced by Vilnius City Municipality Administration in municipal education, treatment and other budgetary institutions in Vilnius City. The data cover the period from 2021 to now. The object of the kit is an ad for one workplace. Details of the workplace (address, coordinates, type of institution) and the proposed job (job description, requirements, salary, contact details) shall be provided. Data provider – Vilnius City Municipality Administration. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Skelbimas](laisvos_darbo_vietos/Skelbimas.md) | Vilniaus miesto savivaldybės darbo skelbimai | `4` | `skelbimo_id` | — | `17` | Rinkinyje pateikiamos Vilniaus miesto savivaldybės administracijos skelbiamos laisvos darbo vietos savivaldybės ugdymo, gydymo bei kitose biudžetinėse... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/darbo_vietos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/darbo_vietos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/laisvos_darbo_vietos (https://data.gov.lt/datasets/3851/)
