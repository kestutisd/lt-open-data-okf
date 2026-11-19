---
type: Dataset
title: "Aplinkos projektams pateiktų kvietimų duomenys"
description: "Aplinkos projektų valdymo informacinėje sistemoje (APVIS) nuo 2019-04-18 kaupiami ir iki šiol atnaujinami Aplinkos projektų valdymo agentūros (APVA) paviešintų kvietimų įstaigos inicijuotiems projektams duomenys."
resource: "https://get.data.gov.lt/datasets/gov/apva/apvis"
tags: [gov, apva, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/apva/apvis.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/apva/apvis.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2854/"
    title: "data.gov.lt DCAT-AP — datasets/gov/apva/apvis"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Aplinkos projektams pateiktų kvietimų duomenys

- **Namespace:** `datasets/gov/apva/apvis`[^manifest]
- **Manifest CSV:** [datasets/gov/apva/apvis.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/apva/apvis.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/apva/apvis` (`deployed`)[^manifest]
- **Provider:** `apva` — Aplinkos projektų valdymo agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2854/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/apva/apvis`[^dcat]
- **Portal Title (`@lt`):** Aplinkos projektams pateiktų kvietimų duomenys[^dcat]
- **Portal Title (`@en`):** Data on invitations submitted to environmental projects[^dcat]
- **Issued (`dct:issued`):** `2024-11-18`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-11-15` .. `2026-10-08`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Aplinkos projektų valdymo informacinėje sistemoje (APVIS) nuo 2019-04-18 kaupiami ir iki šiol atnaujinami Aplinkos projektų valdymo agentūros (APVA) paviešintų kvietimų įstaigos inicijuotiems projektams duomenys. Duomenų rinkinį sudaro: kvietimo identifikatorius, kodas ir pavadinimas, nurodyta, ar kviečiami dalyviai yra fiziniai arba juridiniai asmenys, kvietimo projektą įgyvendinti parinktos priemonės kodas ir pavadinimas, įstaigos kodas, kvietime numatytas finansavimas, kompensacinė išmoka, paraiškų priėmimo laikotarpis bei kvietimo puslapio nuoroda. Vienas įrašas atitinka vieną kvietimą. Dalies kvietimų nuorodos nenukreipia į aktyvų kvietimo puslapį, nes yra nebeaktualūs. Duomenų teikėjas – Lietuvos Respublikos aplinkos ministerijos Aplinkos projektų valdymo agentūra. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The Environmental Project Management Agency (AVA) Environmental Project Management Information System (APIS) collects data on calls made public for projects initiated by THE Agency. The data is being compiled from 2019-04-18 and has been updated so far. The dataset shall comprise: the identifier, code, name of the invitation, whether the participants invited are natural or legal persons, the code, name, institutional code of the measure chosen to implement the call, the financing provided for in the invitation, the compensation payment, the time period for accepting applications and the indication of the invitation page. One entry matches one invitation. Some invitations don't link to an active invitation page because the invitations mentioned above are no longer relevant. Contact the atverimas@stat.gov.lt for technical questions or possible errors[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Kvietimas](apvis/Kvietimas.md) | Aplinkos projektams pateiktų kvietimų duomenys | `4` | `id` | — | `12` | Aplinkos projektų valdymo informacinėje sistemoje (APVIS) nuo 2019-04-18 kaupiami ir iki šiol atnaujinami Aplinkos projektų valdymo agentūros (APVA)... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/apva/apvis.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/apva/apvis.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/apva/apvis (https://data.gov.lt/datasets/2854/)
