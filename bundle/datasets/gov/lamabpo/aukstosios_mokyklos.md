---
type: Dataset
title: "Priėmimo į aukštojo mokslo įstaigas prašymų duomenys"
description: "Rinkinyje pateikiama informacija apie nuo 2024 m. pateiktus priėmimo prašymus į aukštojo mokslo įstaigas (akademijas, kolegijas, universitetus) Lietuvoje."
resource: "https://get.data.gov.lt/datasets/gov/lamabpo/aukstosios_mokyklos"
tags: [gov, lamabpo, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lamabpo/aukstuju_prasymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/aukstuju_prasymai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Priėmimo į aukštojo mokslo įstaigas prašymų duomenys

Rinkinyje pateikiama informacija apie nuo 2024 m. pateiktus priėmimo prašymus į aukštojo mokslo įstaigas (akademijas, kolegijas, universitetus) Lietuvoje. Rinkinį sudaro trys komponentai:

1. Aukštojo mokslo programų duomenys,

2. Priėmimo prašymų duomenys,

3. Priėmimo prašymus teikusių asmenų duomenys.

Duomenų teikėjas: Lietuvos aukštųjų mokyklų asociacija bendrajam priėmimui organizuoti (LAMA BPO).

- **Namespace:** `datasets/gov/lamabpo/aukstosios_mokyklos`[^manifest]
- **Manifest CSV:** [datasets/gov/lamabpo/aukstuju_prasymai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/aukstuju_prasymai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lamabpo/aukstosios_mokyklos`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Programa](aukstosios_mokyklos/Programa.md) | Aukštojo mokslo programų duomenys | `4` | `programos_id` | — | 11 | Pateikiami aukštojo mokslo programų duomenys Lietuvos aukštojo mokslo įstaigose. |
| [Prasymas](aukstosios_mokyklos/Prasymas.md) | Priėmimo prašymų į aukštojo mokslo įstaigas duomenys | `4` | `prasymo_id` | — | 13 | Lentelėje pateikiami priėmimo į aukštojo mokslo įstaigas duomenys. |
| [Profilis](aukstosios_mokyklos/Profilis.md) | Priėmimo prašymus į aukštojo mokslo įstaigas teikusių asmenų profiliai | `4` | `asmens_id` | — | 10 | Lentelėje pateikiami demografiniai duomenys apie asmenis, teikusius priėmimo prašymus į aukštojo mokslo įstaigas. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lamabpo/aukstuju_prasymai.csv
