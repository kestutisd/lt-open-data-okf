---
type: Dataset
title: "SARS-CoV-2 viruso sekoskaitos duomenys"
description: "Duomenų rinkinys iš Nacionalinės visuomenės sveikatos priežiūros laboratorijos sekoskaitos tyrimų duomenų bazės apie SARS-CoV-2 atliktus testų ir sekoskaitos rezultatus."
resource: "https://get.data.gov.lt/datasets/gov/nvspl/sekoskaita"
tags: [gov, nvspl, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nvspl/sars_cov_sekoskaitos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvspl/sars_cov_sekoskaitos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# SARS-CoV-2 viruso sekoskaitos duomenys

Duomenų rinkinys iš Nacionalinės visuomenės sveikatos priežiūros laboratorijos sekoskaitos tyrimų duomenų bazės apie SARS-CoV-2 atliktus testų ir sekoskaitos rezultatus. Duomenų rinkinį sudaro trys lentelės:

1. Žmonėms atlikti SARS-CoV-2 PGR ir antigeno testai,

2. SARS-CoV-2 sekoskaitos Nextclade rezultatų ataskaita,

3. SARS-CoV-2 sekoskaitos Pangolin rezultatų ataskaita.

Duomenų teikėjas – Nacionalinė visuomenės sveikatos priežiūros laboratorija.

Duomenys kaupiami nuo 2022 m. lapkričio 1 d.

- **Namespace:** `datasets/gov/nvspl/sekoskaita`[^manifest]
- **Manifest CSV:** [datasets/gov/nvspl/sars_cov_sekoskaitos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvspl/sars_cov_sekoskaitos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nvspl/sekoskaita`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SARSCoVTestas](sekoskaita/SARSCoVTestas.md) | Žmonėms atlikti SARS-CoV-2 PGR ir antigeno testai | `4` | `iraso_id` | — | 9 | Duomenys iš Nacionalinės visuomenės sveikatos priežiūros laboratorijos sekoskaitos tyrimų duomenų bazės apie žmonėms atliktus SARS-CoV-2 polimerazinės... |
| [NextcladeAtaskaita](sekoskaita/NextcladeAtaskaita.md) | SARS-CoV-2 sekoskaitos Nextclade rezultatų ataskaita | `4` | `meg_id` | — | 97 | Duomenys iš Nacionalinės visuomenės sveikatos priežiūros laboratorijos sekoskaitos tyrimų duomenų bazės apie SARS-CoV-2 viruso atliktos sekoskaitos rezultatus. |
| [PangolinAtaskaita](sekoskaita/PangolinAtaskaita.md) | SARS-CoV-2 sekoskaitos Pangolin rezultatų ataskaita | `4` | `meg_id` | — | 15 | Duomenys iš Nacionalinės visuomenės sveikatos priežiūros laboratorijos sekoskaitos tyrimų duomenų bazės apie SARS-CoV-2 viruso atliktos sekoskaitos rezultatus. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues` |

[^manifest]: atviriduomenys/manifest — datasets/gov/nvspl/sars_cov_sekoskaitos.csv
