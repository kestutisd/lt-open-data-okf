---
type: Dataset
title: "Klaipėdos valstybinio jūrų uosto vandens srovių matavimo duomenys"
description: "AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami geografiniai jūrų uosto duomenys."
resource: "https://get.data.gov.lt/datasets/gov/kvjud/sroviu_matavimai"
tags: [gov, kvjud, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kvjud/sroviu_matavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/sroviu_matavimai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Klaipėdos valstybinio jūrų uosto vandens srovių matavimo duomenys

AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami geografiniai jūrų uosto duomenys. Rinkinyje pateikiami nuo 2016 m. gegužės mėnesio kaupiami vertikaliu arba horizontaliu davikliu atliekamų vandens srovių matavimų duomenys. Šių matavimų metu nustatomas srovių greitis ir kryptis. Vienas įrašas atitinka vienu daviklių atliktą matavimą.

Duomenų teikėjas – AB Klaipėdos valstybinio jūrų uosto direkcija.

- **Namespace:** `datasets/gov/kvjud/sroviu_matavimai`[^manifest]
- **Manifest CSV:** [datasets/gov/kvjud/sroviu_matavimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/sroviu_matavimai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kvjud/sroviu_matavimai`
- **Parent Namespace (`ns`):** AB Klaipėdos valstybinio jūrų uosto direkcija (`datasets/gov/kvjud`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Srove](sroviu_matavimai/Srove.md) | Klaipėdos valstybinio jūrų uosto vandens srovių matavimo duomenys | `4` | `vda_prime_key` | — | 8 | AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami geografiniai jūrų uosto duomenys. |
| [Daviklis](sroviu_matavimai/Daviklis.md) | Klaipėdos valstybinio jūrų uosto vandens srovių daviklių duomenys | `4` | `vda_id` | — | 6 | AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami geografiniai jūrų uosto duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/kvjud/sroviu_matavimai.csv
