---
type: Dataset
title: "Į Klaipėdos uostą atplaukiantys arba iš jo išplaukiantys tarptautiniai laivai."
description: "Informacija apie registruojamus į Klaipėdos uostą atplaukiančius arba iš jo išplaukiančius tarptautinius laivus."
resource: "https://get.data.gov.lt/datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras"
tags: [gov, kvjud, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2864/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Į Klaipėdos uostą atplaukiantys arba iš jo išplaukiantys tarptautiniai laivai.

Informacija apie registruojamus į Klaipėdos uostą atplaukiančius arba iš jo išplaukiančius tarptautinius laivus.[^manifest]

- **Namespace:** `datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras`[^manifest]
- **Manifest CSV:** [datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras` (`deployed`)[^manifest]
- **Provider:** `kvjud` — AB Klaipėdos valstybinio jūrų uosto direkcija *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2864/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras`[^dcat]
- **Portal Title (`@lt`):** Į Klaipėdos uostą atplaukiantys arba iš jo išplaukiantys tarptautiniai laivai[^dcat]
- **Portal Title (`@en`):** International ships arriving at or departing from Klaipeda Port[^dcat]
- **Issued (`dct:issued`):** `2024-11-22`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2026-04-07` .. `2026-07-03`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiama AB Klaipėdos valstybinio jūrų uosto direkcijos registruojamų į Klaipėdos uostą atplaukiančių arba iš jo išplaukiančių tarptautinių laivų informacija – laivo registracijos numeris, atvykimo ar išvykimo laikas, laivo techniniai duomenys ir agento įmonė. Karo laivai į rinkinį nėra įtraukti. Duomenys renkami nuo 2013 metų. Duomenų teikėjas – AB Klaipėdos valstybinio jūrų uosto direkcija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

KIPIS[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Laivas](atvykstanciu_isvykstanciu_laivu_registras/Laivas.md) | Į Klaipėdos uostą atplaukiantys arba iš jo išplaukiantys tarptautiniai laivai. | `4` | `laivo_id` | — | `16` | Informacija apie registruojamus į Klaipėdos uostą atplaukiančius arba iš jo išplaukiančius tarptautinius laivus. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras (https://data.gov.lt/datasets/2864/)
