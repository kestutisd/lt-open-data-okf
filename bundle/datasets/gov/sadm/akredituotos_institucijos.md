---
type: Dataset
title: "Prašymai teikti akredituotas socialines paslaugas"
description: "Duomenų rinkinyje pateikiama informacija apie juridinių asmenų prašymus teikti akredituotas socialines paslaugas: akredituotą socialinę priežiūrą ir laikino atokvėpio paslaugas."
resource: "https://get.data.gov.lt/datasets/gov/sadm/akredituotos_institucijos"
tags: [gov, sadm, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/akredituotos_institucijos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/sadm/akredituotos_institucijos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4118/"
    title: "data.gov.lt DCAT-AP — datasets/gov/sadm/akredituotos_institucijos"
    author: "team:vda"
    last_modified: "2026-10-22T00:00:00Z"
---

# Prašymai teikti akredituotas socialines paslaugas

- **Namespace:** `datasets/gov/sadm/akredituotos_institucijos`[^manifest]
- **Manifest CSV:** [datasets/gov/sadm/akredituotos_institucijos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/akredituotos_institucijos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sadm/akredituotos_institucijos` (`deployed`)[^manifest]
- **Provider:** `sadm` — Lietuvos Respublikos socialinės apsaugos ir darbo ministerija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]
- **URI:** `Akredituotos socialinės paslaugos.`[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/4118/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/sadm/akredituotos_institucijos`[^dcat]
- **Portal Title (`@lt`):** Prašymai teikti akredituotas socialines paslaugas[^dcat]
- **Portal Title (`@en`):** Applications for accredited social services[^dcat]
- **Issued (`dct:issued`):** `2026-02-04`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-22`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-02-05` .. `2026-10-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiama informacija apie juridinių asmenų prašymus teikti akredituotas socialines paslaugas: akredituotą socialinę priežiūrą ir laikino atokvėpio paslaugas. Rinkinyje nurodomi prašymų pateikimo ir sprendimų duomenys, paslaugų teikėjų identifikacinė informacija, paslaugų teikimo pajėgumai, darbuotojų skaičius ir kvalifikacija, paslaugų gavėjų priėmimo galimybės pagal negalių ir poreikių lygius bei patalpų pritaikymas. Pateikiami buveinių ir paslaugų teikimo vietų geografiniai duomenys. Teikiamų socialinių paslaugų sąrašas Duomenų rinkinyje pateikiama informacija apie konkrečias socialines paslaugas, susietas su pateiktais prašymais. Nurodomas paslaugos tipas, paslaugų grupė ir rūšis. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu sveikata@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Prasymas](akredituotos_institucijos/Prasymas.md) | Prašymai istaigų, teikti akredituotas socialines paslaugas | `4` | `prasymo_id` | — | `47` | — |
| [Paslauga](akredituotos_institucijos/Paslauga.md) | Akredituotų institucijų teikiamos paslaugos, jų grupės ir rūšys | `4` | `paslaugos_id` | — | `5` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/sadm/akredituotos_institucijos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/akredituotos_institucijos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/sadm/akredituotos_institucijos (https://data.gov.lt/datasets/4118/)
