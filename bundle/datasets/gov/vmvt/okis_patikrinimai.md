---
type: Dataset
title: "Valstybinės maisto ir veterinarijos tarnybos atlikti patikrinimai pas veterinarinės kontrolės subjektus"
description: "Duomenų rinkinyje pateikiami duomenys iš Valstybinės maisto ir veterinarinės tarnybos (VMVT) Oficialiosios kontrolės informacinės sistemos (OKIS) apie VMVT atliktus patikrinimus veterinarinės kontrolės subjektuose."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/okis_patikrinimai"
tags: [gov, vmvt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmvt/okis_patikrinimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/okis_patikrinimai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Valstybinės maisto ir veterinarijos tarnybos atlikti patikrinimai pas veterinarinės kontrolės subjektus

Duomenų rinkinyje pateikiami duomenys iš Valstybinės maisto ir veterinarinės tarnybos (VMVT) Oficialiosios kontrolės informacinės sistemos (OKIS) apie VMVT atliktus patikrinimus veterinarinės kontrolės subjektuose. Viena duomenų rinkinio eilutė atitinka vieną unikalų patikrinimą. Eilutėje nurodomi patikrinimo ir subjekto identifikaciniai numeriai, subjekto teisinė forma, savivaldybė, kurioje atliktas patikrinimas, patikrinimo data, požymiai, nurodantys, ar VMVT informavo apie patikrinimą prieš atvykstant, ar buvo nustatyti pažeidimai, ar po patikrinimo buvo skirta poveikio priemonė. Taip pat nurodomas paskutinio patikrinimo identifikacinis numeris, data ir laikas, kada įrašas buvo sukurtas arba atnaujintas OKIS duomenų bazėje.

Duomenys kaupiami nuo 2025-02-01.

Duomenų teikėjas – Valstybinė maisto ir veterinarijos tarnyba

- **Namespace:** `datasets/gov/vmvt/okis_patikrinimai`[^manifest]
- **Manifest CSV:** [datasets/gov/vmvt/okis_patikrinimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/okis_patikrinimai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/okis_patikrinimai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Subjektas](okis_patikrinimai/Subjektas.md) | Valstybinės maisto ir veterinarijos tarnybos atlikti patikrinimai pas veterinarinės kontrolės subjektus | `4` | `patikrinimo_id` | — | 11 | Duomenų rinkinyje pateikiami duomenys iš Valstybinės maisto ir veterinarinės tarnybos (VMVT) Oficialiosios kontrolės informacinės sistemos (OKIS) apie VMVT... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/okis_patikrinimai.csv
