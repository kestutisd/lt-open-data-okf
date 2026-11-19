---
type: Dataset
title: "Sumedžioti vilkai Lietuvoje"
description: "Rinkinyje pateikiami išsamūs nuo 2018 m. iki dabar kaupiami vilkų medžioklės Lietuvos Respublikos teritorijoje duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vstt/vilku_medziokles"
tags: [gov, vstt, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/medziokles.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/vstt/medziokles.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2889/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vstt/vilku_medziokles"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Sumedžioti vilkai Lietuvoje

Rinkinyje pateikiami išsamūs nuo 2018 m. iki dabar kaupiami vilkų medžioklės Lietuvos Respublikos teritorijoje duomenys. Rinkinio objektas – vienas sumedžiotas vilkas. Rinkinyje nurodomas medžioklės laikas, vieta, būdas, duomenys apie vilką (amžius, lytis, sveikatos būklė) ir gaują (jauniklių ir suaugusių vilkų skaičius). Atskirai pateikiama ir sumedžiotų vilkų statistika savivaldybės ir datos tikslumu. Duomenų teikėjas – Valstybinė saugomų teritorijų tarnyba prie Aplinkos ministerijos. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/vstt/vilku_medziokles`[^manifest]
- **Manifest CSV:** [datasets/gov/vstt/medziokles.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/medziokles.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/vilku_medziokles` (`deployed`)[^manifest]
- **Provider:** `vstt` — Valstybinė saugomų teritorijų tarnyba prie Aplinkos ministerijos *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2889/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vstt/vilku_medziokles`[^dcat]
- **Portal Title (`@lt`):** Sumedžioti vilkai Lietuvoje[^dcat]
- **Portal Title (`@en`):** Hunted wolves in Lithuania[^dcat]
- **Issued (`dct:issued`):** `2024-12-10`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `WEEKLY` (`http://publications.europa.eu/resource/authority/frequency/WEEKLY`)[^dcat]
- **Distribution Date Span:** `2024-12-05` .. `2026-10-22`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami išsamūs nuo 2018 m. iki dabar kaupiami vilkų medžioklės Lietuvos Respublikos teritorijoje duomenys. Rinkinio objektas – vienas sumedžiotas vilkas. Rinkinyje nurodomas medžioklės laikas, vieta, būdas, duomenys apie vilką (amžius, lytis, sveikatos būklė) ir gaują (jauniklių ir suaugusių vilkų skaičius). Atskirai pateikiama ir sumedžiotų vilkų statistika savivaldybės ir datos tikslumu. Duomenų teikėjas – Valstybinė saugomų teritorijų tarnyba prie Aplinkos ministerijos. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package provides comprehensive data on wolf hunting in the territory of the Republic of Lithuania from 2018 until now. The object of the kit is one hunted wolf. The set shall include the time, place, method of hunting, wolf data (age, sex, state of health) and gang data (number of juveniles and adult wolves). The statistics of the hunted wolves shall also be presented separately with the accuracy of the municipality and date. Data provider shall mean the State Service of Protected Areas under the Ministry of Environment. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SavivaldybeDiena](vilku_medziokles/SavivaldybeDiena.md) | Statistika apie sumedžiotus vilkus Lietuvos savivaldybėse | `4` | `vda_id` | — | `4` | Pateikiama sumedžiotų vilkų statistika savivaldybės ir datos tikslumu. |
| [Vilkas](vilku_medziokles/Vilkas.md) | Duomenys apie sumedžiotus vilkus | `4` | `vda_id` | — | `14` | Rinkinyje pateikiami išsamūs nuo 2018 m. iki dabar kaupiami vilkų medžioklės Lietuvos Respublikos teritorijoje duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/medziokles.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/medziokles.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vstt/vilku_medziokles (https://data.gov.lt/datasets/2889/)
