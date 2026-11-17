---
type: Dataset
title: "Klaipėdos uosto šiaurinio molo meteo informacija"
description: "AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami uoste esančių meteorologinių stotelių matavimo duomenys."
resource: "https://get.data.gov.lt/datasets/gov/kvjud/meteo_duomenys"
tags: [gov, kvjud, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kvjud/meteo_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/meteo_duomenys.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Klaipėdos uosto šiaurinio molo meteo informacija

AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami uoste esančių meteorologinių stotelių matavimo duomenys. Rinkinyje pateikiami nuo 2024 m. gruodžio mėnesio kaupiami šiaurinio molo meteorologiniai duomenys. Šių matavimų metu matuojamas slėgis, rasos taškas, santykinė drėgmė, temperatūra, vėjo kryptis bei greitis. Vienas įrašas atitinka vieną matavimą.

Matavimo stotelės koordinatės: 55.73057 21.07975.

Duomenų teikėjas – AB Klaipėdos valstybinio jūrų uosto direkcija.

- **Namespace:** `datasets/gov/kvjud/meteo_duomenys`[^manifest]
- **Manifest CSV:** [datasets/gov/kvjud/meteo_duomenys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/meteo_duomenys.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kvjud/meteo_duomenys`
- **Parent Namespace (`ns`):** AB Klaipėdos valstybinio jūrų uosto direkcija (`datasets/gov/kvjud`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Matavimas](meteo_duomenys/Matavimas.md) | Klaipėdos uosto šiaurinio molo meteo informacija | `4` | `matavimo_laikas` | — | 10 | AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami uoste esančių meteorologinių stotelių matavimo duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/kvjud/meteo_duomenys.csv
