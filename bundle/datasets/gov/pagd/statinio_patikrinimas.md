---
type: Dataset
title: "Priešgaisrinės apsaugos ir gelbėjimo departamento statinių patikrinimai."
description: "\"Duomenų rikinyje pateikiami nuo 2012 metų kaupiami priešgaisrinės apsaugos ir gelbėjimo departamento statinių patikrinimų visoje Lietuvos teritorijoje duomenys."
resource: "https://get.data.gov.lt/datasets/gov/pagd/statinio_patikrinimas"
tags: [gov, pagd, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/statinio_patikrinimas/statinio_patikrinimas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/pagd/statinio_patikrinimas/statinio_patikrinimas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2861/"
    title: "data.gov.lt DCAT-AP — datasets/gov/pagd/statinio_patikrinimas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Priešgaisrinės apsaugos ir gelbėjimo departamento statinių patikrinimai.

"Duomenų rikinyje pateikiami nuo 2012 metų kaupiami priešgaisrinės apsaugos ir gelbėjimo departamento statinių patikrinimų visoje Lietuvos teritorijoje duomenys. Rinkinį sudaro: pranešimo numeris ir data, patikrinimo pradžia ir pabaiga, statinio paskirtis, objekto grupė, apskritis, seniūnija, gyvenvietė bei koordinatės."[^manifest]

- **Namespace:** `datasets/gov/pagd/statinio_patikrinimas`[^manifest]
- **Manifest CSV:** [datasets/gov/pagd/statinio_patikrinimas/statinio_patikrinimas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/statinio_patikrinimas/statinio_patikrinimas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pagd/statinio_patikrinimas` (`deployed`)[^manifest]
- **Provider:** `pagd` — Priešgaisrinės apsaugos ir gelbėjimo departamentas *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2861/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/pagd/statinio_patikrinimas`[^dcat]
- **Portal Title (`@lt`):** Priešgaisrinės apsaugos ir gelbėjimo departamento statinių patikrinimai[^dcat]
- **Portal Title (`@en`):** Inspections of structures of the Fire and Rescue Department[^dcat]
- **Issued (`dct:issued`):** `2024-11-25`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-11-21` .. `2026-10-07`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiami nuo 2012 metų kaupiami priešgaisrinės apsaugos ir gelbėjimo departamento statinių patikrinimų visoje Lietuvos teritorijoje duomenys. Rinkinį sudaro: pranešimo numeris ir data, patikrinimo pradžia ir pabaiga, statinio paskirtis, objekto grupė, apskritis, seniūnija, gyvenvietė bei koordinatės. Duomenų teikėjas – Priešgaisrinės apsaugos ir gelbėjimo departamentas prie VRM. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^dcat]

### Portal Description (`@en`)

The data collection shall contain data collected from 2012 on the inspections of structures of the Fire and Rescue Department throughout the territory of Lithuania. The package consists of: the number and date of the notification, the beginning and end of the inspection, the purpose of the construction works, the group of the object, the county, the neighborhood, the settlement and coordinates. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Patikrinimas](statinio_patikrinimas/Patikrinimas.md) | Priešgaisrinės apsaugos ir gelbėjimo departamento statinių patikrinimai. | `4` | `id` | — | `17` | "Duomenų rikinyje pateikiami nuo 2012 metų kaupiami priešgaisrinės apsaugos ir gelbėjimo departamento statinių patikrinimų visoje Lietuvos teritorijoje... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/pagd/statinio_patikrinimas/statinio_patikrinimas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/statinio_patikrinimas/statinio_patikrinimas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/pagd/statinio_patikrinimas (https://data.gov.lt/datasets/2861/)
