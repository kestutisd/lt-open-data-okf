---
type: Dataset
title: "Valstybinės veterinarinės kontrolės subjektų sąrašas"
description: "Duomenų rinkinyje pateikiami duomenys iš Valstybinės maisto ir veterinarijos tarnybos (VMVT) Oficialiosios kontrolės informacinės sistemos (OKIS) apie valstybinės veterinarinės kontrolės subjektus."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/okis_subjektai"
tags: [gov, vmvt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmvt/okis_subjektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/okis_subjektai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Valstybinės veterinarinės kontrolės subjektų sąrašas

Duomenų rinkinyje pateikiami duomenys iš Valstybinės maisto ir veterinarijos tarnybos (VMVT) Oficialiosios kontrolės informacinės sistemos (OKIS) apie valstybinės veterinarinės kontrolės subjektus. Viena duomenų rinkinio eilutė atitinka vieną unikalų valstybinės veterinarinės kontrolės ūkio subjektą. Eilutėje nurodomas subjekto identifikacinis numeris, pavadinimas, teisinė forma (juridinis / fizinis), veiklos pradžios ir sustabdymo datos, JAR kodas ir jo validavimo stulpelis, subjekto veikla ir veiklos tipas, veterinarinio patvirtinimo numeris, VMVT padalinys, subjekto adresas ir geolokacija, telefono numeris ir elektroninis paštas. Paskutiniai du stulpeliai nurodo įrašo sukūrimo arba atnaujinimo OKIS duomenų bazėje datą.

Duomenys kaupiami nuo 2025-02-01.

Duomenų teikėjas – Valstybinė maisto ir veterinarijos tarnyba.

- **Namespace:** `datasets/gov/vmvt/okis_subjektai`[^manifest]
- **Manifest CSV:** [datasets/gov/vmvt/okis_subjektai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/okis_subjektai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/okis_subjektai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Subjektas](okis_subjektai/Subjektas.md) | Valstybinės veterinarinės kontrolės subjektų sąrašas | `4` | `subjekto_id` | — | 22 | Duomenų rinkinyje pateikiami duomenys iš Valstybinės maisto ir veterinarijos tarnybos (VMVT) Oficialiosios kontrolės informacinės sistemos (OKIS) apie... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/okis_subjektai.csv
