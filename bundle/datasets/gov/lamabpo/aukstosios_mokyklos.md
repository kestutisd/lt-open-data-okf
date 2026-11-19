---
type: Dataset
title: "Priėmimo į aukštojo mokslo įstaigas prašymų duomenys"
description: "Rinkinyje pateikiama informacija apie nuo 2024 m. pateiktus priėmimo prašymus į aukštojo mokslo įstaigas (akademijas, kolegijas, universitetus) Lietuvoje."
resource: "https://get.data.gov.lt/datasets/gov/lamabpo/aukstosios_mokyklos"
tags: [gov, lamabpo, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/aukstuju_prasymai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lamabpo/aukstuju_prasymai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2914/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lamabpo/aukstosios_mokyklos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Priėmimo į aukštojo mokslo įstaigas prašymų duomenys

Rinkinyje pateikiama informacija apie nuo 2024 m. pateiktus priėmimo prašymus į aukštojo mokslo įstaigas (akademijas, kolegijas, universitetus) Lietuvoje. Rinkinį sudaro trys komponentai: 1. Aukštojo mokslo programų duomenys, 2. Priėmimo prašymų duomenys, 3. Priėmimo prašymus teikusių asmenų duomenys. Duomenų teikėjas: Lietuvos aukštųjų mokyklų asociacija bendrajam priėmimui organizuoti (LAMA BPO). Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/lamabpo/aukstosios_mokyklos`[^manifest]
- **Manifest CSV:** [datasets/gov/lamabpo/aukstuju_prasymai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/aukstuju_prasymai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lamabpo/aukstosios_mokyklos` (`deployed`)[^manifest]
- **Provider:** `lamabpo` — Lietuvos aukštųjų mokyklų asociacija bendrajam priėmimui organizuoti (LAMA BPO) *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2914/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lamabpo/aukstosios_mokyklos`[^dcat]
- **Portal Title (`@lt`):** Bendrojo priėmimo į pirmosios pakopos ir vientisųjų studijų programas prašymai[^dcat]
- **Portal Title (`@en`):** Requests for general admission to first-cycle and single-level programmes[^dcat]
- **Issued (`dct:issued`):** `2025-01-22`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2025-01-22` .. `2026-01-16`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiama informacija apie nuo 2024 m. pateiktus priėmimo prašymus į aukštojo mokslo įstaigas (akademijas, kolegijas, universitetus) Lietuvoje. Rinkinį sudaro trys komponentai: 1. Aukštojo mokslo programų duomenys, 2. Priėmimo prašymų duomenys, 3. Priėmimo prašymus teikusių asmenų duomenys. Duomenų teikėjas – Lietuvos aukštųjų mokyklų asociacija bendrajam priėmimui organizuoti (LAMA BPO). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Requests for general admission to first-cycle and single-level programmes[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Programa](aukstosios_mokyklos/Programa.md) | Aukštojo mokslo programų duomenys | `4` | `programos_id` | — | `11` | Pateikiami aukštojo mokslo programų duomenys Lietuvos aukštojo mokslo įstaigose. |
| [Prasymas](aukstosios_mokyklos/Prasymas.md) | Priėmimo prašymų į aukštojo mokslo įstaigas duomenys | `4` | `prasymo_id` | — | `13` | Lentelėje pateikiami priėmimo į aukštojo mokslo įstaigas duomenys. |
| [Profilis](aukstosios_mokyklos/Profilis.md) | Priėmimo prašymus į aukštojo mokslo įstaigas teikusių asmenų profiliai | `4` | `asmens_id` | — | `10` | Lentelėje pateikiami demografiniai duomenys apie asmenis, teikusius priėmimo prašymus į aukštojo mokslo įstaigas. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lamabpo/aukstuju_prasymai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/aukstuju_prasymai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lamabpo/aukstosios_mokyklos (https://data.gov.lt/datasets/2914/)
