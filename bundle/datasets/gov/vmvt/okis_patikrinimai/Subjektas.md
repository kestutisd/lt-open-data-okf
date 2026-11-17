---
type: Table
title: "Subjektas — Valstybinės maisto ir veterinarijos tarnybos atlikti patikrinimai pas veterinarinės kontrolės subjektus"
description: "Duomenų rinkinyje pateikiami duomenys iš Valstybinės maisto ir veterinarinės tarnybos (VMVT) Oficialiosios kontrolės informacinės sistemos (OKIS) apie VMVT atliktus patikrinimus veterinarinės kontrolės subjektuose."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/okis_patikrinimai/Subjektas"
tags: [gov, vmvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmvt/okis_patikrinimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/okis_patikrinimai.csv#L10"
    last_modified: "2026-11-11T14:39:20Z"
---

# Subjektas — Valstybinės maisto ir veterinarijos tarnybos atlikti patikrinimai pas veterinarinės kontrolės subjektus

Duomenų rinkinyje pateikiami duomenys iš Valstybinės maisto ir veterinarinės tarnybos (VMVT) Oficialiosios kontrolės informacinės sistemos (OKIS) apie VMVT atliktus patikrinimus veterinarinės kontrolės subjektuose. Viena duomenų rinkinio eilutė atitinka vieną unikalų patikrinimą. Eilutėje nurodomi patikrinimo ir subjekto identifikaciniai numeriai, subjekto teisinė forma, savivaldybė, kurioje atliktas patikrinimas, patikrinimo data, požymiai, nurodantys, ar VMVT informavo apie patikrinimą prieš atvykstant, ar buvo nustatyti pažeidimai, ar po patikrinimo buvo skirta poveikio priemonė. Taip pat nurodomas paskutinio patikrinimo identifikacinis numeris, data ir laikas, kada įrašas buvo sukurtas arba atnaujintas OKIS duomenų bazėje.

Duomenys kaupiami nuo 2025-02-01.

Duomenų teikėjas – Valstybinė maisto ir veterinarijos tarnyba

- **Model:** `datasets/gov/vmvt/okis_patikrinimai/Subjektas`[^manifest]
- **Dataset:** [Valstybinės maisto ir veterinarijos tarnybos atlikti patikrinimai pas veterinarinės kontrolės subjektus](../okis_patikrinimai.md) (`datasets/gov/vmvt/okis_patikrinimai`)
- **Manifest CSV:** [datasets/gov/vmvt/okis_patikrinimai.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/okis_patikrinimai.csv#L10)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/okis_patikrinimai/Subjektas`
- **Primary Key (`ref`):** `patikrinimo_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `patikrinimo_id` | `string` | — | `4` | `open` | — | Patikrinimo identifikacinis numeris | — |
| `subjekto_id` | `string` | — | `4` | `open` | — | Subjekto identifikacinis numeris | — |
| `teisine_forma` | `string` | — | `4` | `open` | — | Subjekto teisinė forma | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė, kurioje buvo atliekamas patikrinimas | — |
| `patikrinimo_data` | `date` | `D` | `4` | `open` | — | Patikrinimo data | — |
| `apie_atvykima_pranesta` | `boolean` | — | `4` | `open` | — | Požymis, nurodantis, ar VMVT informavo apie patikrinimą prieš atvykstant | — |
| `ar_aptikta_pazeidimu` | `boolean` | — | `4` | `open` | — | Požymis, nurodantis, ar buvo nustatyti pažeidimai | — |
| `pritaikytos_sankcijos` | `boolean` | — | `4` | `open` | — | Požymis, nurodantis, ar buvo pritaikyta poveikio priemonė (įspėjimas/bauda) | — |
| `paskutinio_patikrinimo_id` | `string` | — | `4` | `open` | — | Paskutinio patikrinimo identifikacinis numeris | — |
| `irasas_sukurtas` | `datetime` | `U` | `4` | `open` | — | Data ir laikas kada įrašas buvo sukurtas OKIS duomenų bazėje | — |
| `irasas_atnaujintas` | `datetime` | `U` | `4` | `open` | — | Data ir laikas kada įrašas buvo atnaujintas OKIS duomenų bazėje | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `teisine_forma` | `"Juridinis asmuo"` | — | — | Juridinis asmuo | — |
| `teisine_forma` | `"Individualus asmuo"` | — | — | Individualus asmuo | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/okis_patikrinimai.csv
