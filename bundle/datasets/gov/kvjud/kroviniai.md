---
type: Dataset
title: "Krovininių laivų operacijos Klaipėdos valstybiniame jūrų uoste"
description: "Duomenų rinkinyje pateikiami Klaipėdos valstybinio jūrų uosto direkcijos duomenys apie krovininių laivų operacijas Klaipėdos jūrų uoste."
resource: "https://get.data.gov.lt/datasets/gov/kvjud/kroviniai"
tags: [gov, kvjud, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kvjud/kroviniai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/kroviniai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Krovininių laivų operacijos Klaipėdos valstybiniame jūrų uoste

Duomenų rinkinyje pateikiami Klaipėdos valstybinio jūrų uosto direkcijos duomenys apie krovininių laivų operacijas Klaipėdos jūrų uoste. Rinkinio objektas - atvykimo arba išvykimo operacija. Duomenys pateikiami nuo 2002m. iki šių dienų. Nurodoma operacijos rūšis, laivo savininko atstovas, su laivo atvykimu/išvykimu (išvykimo ir atvykimo uostas, faktiniai išvykimo laikai) bei su laivu (pavadinimas, tipas, vėliava, IMO numeris, dedveitas ir bendroji talpa) susijusi informacija.

- **Namespace:** `datasets/gov/kvjud/kroviniai`[^manifest]
- **Manifest CSV:** [datasets/gov/kvjud/kroviniai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/kroviniai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kvjud/kroviniai`
- **Parent Namespace (`ns`):** AB Klaipėdos valstybinio jūrų uosto direkcija (`datasets/gov/kvjud`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Operacija](kroviniai/Operacija.md) | Krovininių laivų operacijos Klaipėdos valstybinio jūrų uoste | `4` | `vda_id` | — | 19 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/kvjud/kroviniai.csv
