---
type: Table
title: "PacientoRegistracija — Pacientų registracijų sąrašas"
description: "Vaikų reabilitacijos sanatorijos „Palangos gintaras“ pacientų registracijų sąrašas."
resource: "https://get.data.gov.lt/datasets/gov/palangos_gintaras/pacientai/PacientoRegistracija"
tags: [gov, palangos_gintaras, pacientoregistracija, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/palangos_gintaras/pacientai.csv#L14"
    title: "atviriduomenys/manifest — datasets/gov/palangos_gintaras/pacientai.csv#L14"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2720/"
    title: "data.gov.lt DCAT-AP — datasets/gov/palangos_gintaras/pacientai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PacientoRegistracija — Pacientų registracijų sąrašas

Vaikų reabilitacijos sanatorijos „Palangos gintaras“ pacientų registracijų sąrašas. Duomenys pateikiami nuo 2010 metų ir iki dabar.[^manifest]

- **Model:** `datasets/gov/palangos_gintaras/pacientai/PacientoRegistracija`[^manifest]
- **Dataset:** [Palangos vaikų reabilitacijos sanatorijos „Palangos gintaras“ pacientų registracijų sąrašas](../pacientai.md) (`datasets/gov/palangos_gintaras/pacientai`)[^manifest]
- **Manifest CSV:** [datasets/gov/palangos_gintaras/pacientai.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/palangos_gintaras/pacientai.csv#L14)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/palangos_gintaras/pacientai/PacientoRegistracija` (`deployed`)[^manifest]
- **Provider:** `palangos_gintaras` — Vaikų reabilitacijos sanatorija "Palangos gintaras" *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Identifikacinis numeris | — |
| `registracijos_nr` | `string` | — | `4` | `open` | — | Paciento registracijos identifikacinis numeris | — |
| `paciento_id` | `string` | — | `4` | `open` | — | Paciento identifikacinis numeris | — |
| `atvykimo_data` | `date` | `D` | `4` | `open` | — | Paciento atvykimo data | — |
| `isvykimo_data` | `date` | `D` | `4` | `open` | — | Paciento išvykimo data | — |
| `atvykimo_registracijos_data` | `datetime` | `S` | `4` | `open` | — | Paciento atvykimo registracijos data | — |
| `tlk_kodas` | `string` | — | `4` | `open` | — | Teritorinės ligonių kasos kodas | — |
| `tlk_pav` | `string` | — | `4` | `open` | — | Teritorinės ligonių kasos pavadinimas | — |
| `lovadieniu_skaicius` | `integer` | — | `4` | `open` | — | Lovadienių skaičius | — |
| `tlk_pasl_kodas` | `string` | — | `4` | `open` | — | Teritorinės ligonių kasos paslaugos kodas | — |
| `tlk_pasl_pavad` | `string` | — | `4` | `open` | — | Teritorinės ligonių kasos paslaugos pavadinimas | — |
| `gyd_prof_kodas` | `string` | — | `4` | `open` | — | Gydymo profilio kodas | — |
| `gyd_prof_pavad` | `string` | — | `4` | `open` | — | Gydymo profilio pavadinimas | — |
| `diagnozes_grupe` | `string` | — | `4` | `open` | — | Diagnozės grupė | — |
| `gyd_prof_gr` | `string` | — | `4` | `open` | — | Gydymo profilio grupė | — |
| `lovos_kaina` | `number` | — | `4` | `open` | — | Lovos kaina | — |
| `lovu_sk` | `integer` | `U` | `4` | `open` | — | Lovų skaičius | — |
| `suma` | `number` | — | `4` | `open` | — | Suma | — |
| `skausmas_atvykus` | `string` | — | `4` | `open` | — | Skausmo lygis atvykus | — |
| `skausmas_isvykstant` | `string` | — | `4` | `open` | — | Skausmo lygis išvykstant | — |
| `skaus_iraso_reg_data` | `datetime` | `S` | `4` | `open` | — | Skausmo lygio registravimo data | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tlk_pasl_pavad` | `"A: vaikų kvėpavimo sistemos ligos"` | — | — | Vaikų kvėpavimo sistemos ligos | — |
| `tlk_pasl_pavad` | `"A: vaikų ausų, nosies, gerklės ligos"` | — | — | Vaikų ausų, nosies, gerklės ligos | — |
| `tlk_pasl_pavad` | `"A: vaikų judamojo-atramos aparato ligos"` | — | — | Vaikų judamojo-atramos aparato ligos | — |
| `tlk_pasl_pavad` | `"A: vaikų virškinimo sistemos ligos"` | — | — | Vaikų virškinimo sistemos ligos | — |
| `tlk_pasl_pavad` | `"A: vaikų endokrininės ligos"` | — | — | Vaikų endokrininės ligos | — |
| `tlk_pasl_pavad` | `"A: vaikų psichikos ir elgesio sutrikimai"` | — | — | Vaikų psichikos ir elgesio sutrikimai | — |
| `tlk_pasl_pavad` | `"A: vaikų nervų sistemos ligos"` | — | — | Vaikų nervų sistemos ligos | — |
| `tlk_pasl_pavad` | `"A: vaikų inkstų ligos"` | — | — | Vaikų inkstų ligos | — |
| `tlk_pasl_pavad` | `"A: vaikų kraujotakos sistemos ligos"` | — | — | Vaikų kraujotakos sistemos ligos | — |
| `gyd_prof_pavad` | `"Antirecidyvinis gydymas"` | — | — | Antirecidyvinis gydymas | — |
| `gyd_prof_pavad` | `"Sveikatą grąžinantis gydymas"` | — | — | Sveikatą grąžinantis gydymas | — |
| `gyd_prof_pavad` | `"Palaikomoji reabilitacija"` | — | — | Palaikomoji reabilitacija | — |
| `gyd_prof_pavad` | `"Reabilitacinis gydymas"` | — | — | Reabilitacinis gydymas | — |
| `gyd_prof_pavad` | `"Reabilitacinis gyd.,pakart .R"` | — | — | Reabilitacinis gyd.,pakart .R | — |
| `gyd_prof_pavad` | `"Ambulatorinė reabilitacija"` | — | — | Ambulatorinė reabilitacija | — |
| `gyd_prof_pavad` | `"Sveikatos grąžinam.gyd.(suaug."` | — | — | Sveikatos grąžinam.gyd.(suaug. | — |
| `gyd_prof_pavad` | `"Mokamos procedūros"` | — | — | Mokamos procedūros | — |
| `gyd_prof_pavad` | `"Sveikatinimo savaitgalis"` | — | — | Sveikatinimo savaitgalis | — |
| `gyd_prof_pavad` | `"Palaikomoji reab.(regos,klaus."` | — | — | Palaikomoji reab.(regos,klaus. | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/palangos_gintaras/pacientai.csv#L14 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/palangos_gintaras/pacientai.csv#L14)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/palangos_gintaras/pacientai (https://data.gov.lt/datasets/2720/)
