---
type: Table
title: "Subjektas — Valstybinės veterinarinės kontrolės subjektų sąrašas"
description: "Duomenų rinkinyje pateikiami duomenys iš Valstybinės maisto ir veterinarijos tarnybos (VMVT) Oficialiosios kontrolės informacinės sistemos (OKIS) apie valstybinės veterinarinės kontrolės subjektus."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/okis_subjektai/Subjektas"
tags: [gov, vmvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmvt/okis_subjektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/okis_subjektai.csv#L10"
    last_modified: "2026-11-11T14:39:20Z"
---

# Subjektas — Valstybinės veterinarinės kontrolės subjektų sąrašas

Duomenų rinkinyje pateikiami duomenys iš Valstybinės maisto ir veterinarijos tarnybos (VMVT) Oficialiosios kontrolės informacinės sistemos (OKIS) apie valstybinės veterinarinės kontrolės subjektus. Viena duomenų rinkinio eilutė atitinka vieną unikalų valstybinės veterinarinės kontrolės ūkio subjektą. Eilutėje nurodomas subjekto identifikacinis numeris, pavadinimas, teisinė forma (juridinis / fizinis), veiklos pradžios ir sustabdymo datos, JAR kodas ir jo validavimo stulpelis, subjekto veikla ir veiklos tipas, veterinarinio patvirtinimo numeris, VMVT padalinys, subjekto adresas ir geolokacija, telefono numeris ir elektroninis paštas. Paskutiniai du stulpeliai nurodo įrašo sukūrimo arba atnaujinimo OKIS duomenų bazėje datą.

Duomenys kaupiami nuo 2025-02-01.

Duomenų teikėjas – Valstybinė maisto ir veterinarijos tarnyba.

- **Model:** `datasets/gov/vmvt/okis_subjektai/Subjektas`[^manifest]
- **Dataset:** [Valstybinės veterinarinės kontrolės subjektų sąrašas](../okis_subjektai.md) (`datasets/gov/vmvt/okis_subjektai`)
- **Manifest CSV:** [datasets/gov/vmvt/okis_subjektai.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/okis_subjektai.csv#L10)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/okis_subjektai/Subjektas`
- **Primary Key (`ref`):** `subjekto_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `subjekto_id` | `string` | — | `4` | `open` | — | Subjekto identifikacinis numeris | — |
| `subjekto_pavadinimas` | `string` | — | `4` | `open` | — | Subjekto pavadinimas | — |
| `teisine_forma` | `string` | — | `4` | `open` | — | Subjekto teisinė forma | — |
| `busena` | `string` | — | `4` | `open` | — | Subjekto veiklos būsena | — |
| `veikla_vykdoma_nuo` | `string` | — | `2` | `open` | — | Subjekto veiklos pradžios data | — |
| `veikla_nutraukta` | `string` | — | `2` | `open` | — | Subjekto veiklos nutraukimo data | — |
| `sustabdyta_iki` | `datetime` | `U` | `4` | `open` | — | Subjekto veikla sustabdoma iki | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Juridinio asmens kodas | — |
| `jar_validacija` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros sugeneruotas stulpelis, kuris patikrina ar JAR kodas yra validus | — |
| `veikla` | `string` | — | `4` | `open` | — | Subjekto veikla | — |
| `veiklos_tipas` | `string` | — | `4` | `open` | — | Subjekto veiklos tipas | — |
| `vet_patvirtinimo_nr` | `string` | — | `4` | `open` | — | Ūkio subjektui suteiktas veterinarinio patvirtinimo / registracijos numeris | — |
| `vmvt_padalinys` | `string` | — | `4` | `open` | — | Valstybinės maisto ir veterinarijos tarnybos padalinys, kuris piržiūri ūkio subjektą | — |
| `adresas` | `string` | — | `4` | `open` | — | Subjekto adresas | — |
| `adreso_tipas` | `string` | — | `4` | `open` | — | Adreso tipas | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Adreso ilgumos koordinatė WGS-84 koordinačių sistemoje | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Adreso platumos koordinatė WGS-84 koordinačių sistemoje | — |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | Taškinė WGS-84 koordinatė | — |
| `telefono_numeris` | `string` | — | `4` | `open` | — | Subjekto telefono numeris | — |
| `el_pastas` | `string` | — | `4` | `open` | — | Subjekto elektroninis paštas | — |
| `irasas_sukurtas` | `datetime` | `U` | `4` | `open` | — | Data ir laikas kada įrašas buvo atnaujintas OKIS duomenų bazėje | — |
| `irasas_atnaujintas` | `datetime` | `U` | `4` | `open` | — | Data ir laikas kada įrašas buvo atnaujintas OKIS duomenų bazėje | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `teisine_forma` | `"Individualus asmuo"` | — | — | Individualus asmuo | — |
| `teisine_forma` | `"Juridinis asmuo"` | — | — | Juridinis asmuo | — |
| `busena` | `"Aktyvus"` | — | — | Aktyvus | — |
| `busena` | `"Sustabdytas"` | — | — | Sustabdytas | — |
| `busena` | `"Panaikintas"` | — | — | Panaikintas | — |
| `busena` | `"Vertinamas"` | — | — | Vertinamas | — |
| `busena` | `"Laikinai patvirtintas"` | — | — | Laikinai patvirtintas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/okis_subjektai.csv
