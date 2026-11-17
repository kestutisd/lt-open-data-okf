---
type: Dataset
title: "Vilniaus miesto savivaldybės skelbiamų konkursų paraiškų duomenys"
description: "Rinkinyje pateikiami duomenys apie Vilniaus miesto savivaldybės skelbiamus ir vykdomus konkursus jaunimo, bendruomenės, sporto, aplinkos, miesto plėtros, socialinės apsaugos, kultūros, sveikatingumo programose bei konkursams teiktas..."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/paraiskos"
tags: [gov, vilniaus_m_sav, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/paraiskos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/paraiskos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Vilniaus miesto savivaldybės skelbiamų konkursų paraiškų duomenys

Rinkinyje pateikiami duomenys apie Vilniaus miesto savivaldybės skelbiamus ir vykdomus konkursus jaunimo, bendruomenės, sporto, aplinkos, miesto plėtros, socialinės apsaugos, kultūros, sveikatingumo programose bei konkursams teiktas paraiškas.

- **Namespace:** `datasets/gov/vilniaus_m_sav/paraiskos`[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/paraiskos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/paraiskos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/paraiskos`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Konkursas](paraiskos/Konkursas.md) | Vilniaus miesto savivaldybės administracijos konkursų skelbimai | `4` | `konkurso_id` | — | 11 | Pateikiami duomenys apie kiekvieną skelbtą konkursą, tikslus, aprašymą, programą, maksimalią finansavimo sumą, paraiškų teikimo pradžios ir pabaigos datas... |
| [Paraiska](paraiskos/Paraiska.md) | Vilniaus miesto savivaldybės skelbiamų konkursų paraiškų duomenys | `4` | `teikejo_id` | — | 5 | Aprašomos konkursams teiktos paraiškos, nurodant paraiškos statusą, programos kodą, teikimo datą ir galutinį paraiškos įvertį po vertinimo. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/paraiskos.csv
