---
type: Dataset
title: "Nuotekų valymo įrenginiai bei jų kokacijos"
description: "Duomenys pateikiami iš aplinkos apsaugos departamento nuotekų tvarkymo informacinės sistemos."
resource: "https://get.data.gov.lt/datasets/gov/aad/nuoteku_irenginiai"
tags: [gov, aad, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aad/nuoteku_irenginiai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/aad/nuoteku_irenginiai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2855/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aad/nuoteku_irenginiai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Nuotekų valymo įrenginiai bei jų kokacijos

Duomenys pateikiami iš aplinkos apsaugos departamento nuotekų tvarkymo informacinės sistemos. Pateikiamos dvi lentelės kuriuos jungiasi per „aglomeracijos_id“ stulpelį. Vienoje lentelėje pateikiami visi užregistruoti nuotekų įrenginiai, o kitoje preliminarios nuotekų tvarkymo sistemų aglomeracijų ribos. Registruojant nuotekų įrenginį (jei vartotojas nurodė), pateikiama tokia informacija kaip įrenginio tipas, gamintojas, modelis, koordinatės ir t.t. Įrenginių lentelėje viena eilutė atitinka vieną įrenginį, aglomeracijų lentelėje – vieną aglomeraciją. Duomenų aprėptis – visa Lietuva. Duomenų teikėjas: Aplinkos apsaugos departamentas prie Aplinkos ministerijos Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/aad/nuoteku_irenginiai`[^manifest]
- **Manifest CSV:** [datasets/gov/aad/nuoteku_irenginiai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aad/nuoteku_irenginiai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aad/nuoteku_irenginiai` (`deployed`)[^manifest]
- **Provider:** `aad` — Aplinkos apsaugos departamentas prie Aplinkos ministerijos *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2855/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/aad/nuoteku_irenginiai`[^dcat]
- **Portal Title (`@lt`):** Nuotekų valymo įrenginiai bei jų lokacijos[^dcat]
- **Portal Title (`@en`):** Wastewater treatment plants and their locations[^dcat]
- **Issued (`dct:issued`):** `2024-11-22`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-11-15` .. `2026-10-27`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenys pateikiami iš Aplinkos apsaugos departamento nuotekų tvarkymo informacinės sistemos. Rinkinį sudaro dvi lentelės, sujungtos per stulpelį „aglomeracijos_id“. Vienoje lentelėje pateikiami visi užregistruoti nuotekų įrenginiai, o kitoje – preliminarios nuotekų tvarkymo sistemų aglomeracijų ribos. Registruojant nuotekų įrenginį (jei vartotojas jį nurodė), nurodomas įrenginio tipas, gamintojas, modelis, koordinatės ir kita informacija. Įrenginių lentelėje viena eilutė atitinka vieną įrenginį, aglomeracijų lentelėje – vieną aglomeraciją. Duomenų aprėptis – visa Lietuva. Nuo 2025 m. rugsėjo 5 d. rinkinys papildytas informacija apie nuotekų išleidimo būdus („isleidimo_budas“) ir jų lokacijas lentelėje „Nuotekų įrenginiai“. Duomenų teikėjas – Aplinkos apsaugos departamentas prie Aplinkos ministerijos. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data shall be provided from the waste water management information system of the Department of Environmental Protection. Here are two tables that you connect through the agglomeration _id column. One table shows all registered sewage plants and the other provides preliminary limits for agglomerations of sewage treatment systems. When registering a waste water plant (if indicated by the user), information such as type of installation, manufacturer, model, coordinates, etc. shall be provided. In the equipment table, one row corresponds to one unit and one agglomeration in the agglomeration table. Data coverage – Lithuania as a whole. Data provider: Department of Environmental Protection under the Ministry of Environment Contact the atverimas@stat.gov.lt for technical questions or possible errors[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Irenginys](nuoteku_irenginiai/Irenginys.md) | Nuotekų valymo įrenginiai bei jų lokacijos | `4` | `irenginio_id` | — | `19` | Duomenys pateikiami iš aplinkos apsaugos departamento nuotekų tvarkymo informacinės sistemos. |
| [Aglomeracija](nuoteku_irenginiai/Aglomeracija.md) | Preliminarios nuotekų tvarkymo sistemų aglomeracijų ribos | `4` | `vda_prime_key` | — | `8` | Duomenys pateikiami iš aplinkos apsaugos departamento nuotekų tvarkymo informacinės sistemos. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/aad/nuoteku_irenginiai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aad/nuoteku_irenginiai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aad/nuoteku_irenginiai (https://data.gov.lt/datasets/2855/)
