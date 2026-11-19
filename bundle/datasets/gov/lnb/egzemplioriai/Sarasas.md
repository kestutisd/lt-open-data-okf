---
type: Table
title: "Sarasas — LIBIS egzempliorių sąrašas"
description: "Bibliotekų turimų egzempliorių sąrašas"
resource: "https://get.data.gov.lt/datasets/gov/lnb/egzemplioriai/Sarasas"
tags: [gov, lnb, sarasas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/egzemplioriai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lnb/egzemplioriai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2796/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lnb/egzemplioriai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Sarasas — LIBIS egzempliorių sąrašas

Bibliotekų turimų egzempliorių sąrašas[^manifest]

- **Model:** `datasets/gov/lnb/egzemplioriai/Sarasas`[^manifest]
- **Dataset:** [LIBIS egzempliorių sąrašas](../egzemplioriai.md) (`datasets/gov/lnb/egzemplioriai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lnb/egzemplioriai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/egzemplioriai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lnb/egzemplioriai/Sarasas` (`deployed`)[^manifest]
- **Provider:** `lnb` — Lietuvos nacionalinė Martyno Mažvydo biblioteka *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Egzemplioriaus unikalus identifikatorius | — |
| `bibliografinio_iraso_id` | `string` | — | `4` | `open` | — | Bibliografinio įrašo unikalus identifikatorius. Referuoja į bibliografinius įrašus | — |
| `savininko_padalinio_id` | `string` | — | `4` | `open` | — | Egzemplioriaus savininko unikalus identifikatorius. Referuoja į bibliotekos padalinio unikalų identifikatorių | — |
| `saugotojo_padalinio_id` | `string` | — | `4` | `open` | — | Egzemplioriaus saugotojo unikalus identifikatorius. Referuoja į bibliotekos padalinio unikalų identifikatorių | — |
| `savininko_spaudos_zenklas` | `string` | — | `4` | `open` | — | Savininko spaudos ženklas | — |
| `saugotojo_spaudos_zenklas` | `string` | — | `4` | `open` | — | Saugotojo spaudos ženklas | — |
| `bruksninis_kodas` | `string` | — | `4` | `open` | — | Barkodas | — |
| `inventoriaus_tipas` | `string` | — | `4` | `open` | — | Inventoriaus tipas | — |
| `inventoriaus_id` | `string` | — | `4` | `open` | — | Inventoriaus id | — |
| `inventoriaus_data` | `date` | `D` | `4` | `open` | — | Inventoriaus id data | — |
| `periodikos_tipas` | `string` | — | `4` | `open` | — | Periodikos tipas | — |
| `periodinio_leidinio_antraste` | `string` | — | `4` | `open` | — | Antraštė | — |
| `periodinio_leidinio_pavadinimas_lt` | `string` | — | `4` | `open` | — | Periodikos pavadinimas | — |
| `periodikos_isleidimo_data` | `date` | `D` | `4` | `open` | — | Išleidimo data | — |
| `periodikos_tomo_nr` | `string` | — | `4` | `open` | — | Periodikos numeris | — |
| `periodikos_metai` | `string` | — | `4` | `open` | — | Periodikos metai | — |
| `max_isdavimo_dienos` | `integer` | `d` | `4` | `open` | — | Išduodama dienų | — |
| `leisti_kopijuoti` | `boolean` | — | `4` | `open` | — | Leidžiama kopijuoti | — |
| `leisti_isduoti` | `boolean` | — | `4` | `open` | — | Leidžiama išduoti | — |
| `isdavimo_salyga` | `string` | — | `4` | `open` | — | Išdavimo sąlygos | — |
| `dabartine_kaina` | `number` | — | `4` | `open` | — | Dabartinė kaina | — |
| `dabartines_kainos_valiuta` | `string` | — | `4` | `open` | — | Dabartinės kainos valiuta | — |
| `pradine_kaina` | `number` | — | `4` | `open` | — | Pradinė kaina | — |
| `pradines_kainos_valiuta` | `string` | — | `4` | `open` | — | Pradinės kainos valiuta | — |
| `nurasymo_data` | `date` | `D` | `4` | `open` | — | Nurašymo data | — |
| `nurasymo_priezastis_lt` | `string` | — | `4` | `open` | — | Egzemplioriaus nurašymo priežastis | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `inventoriaus_tipas` | `"Inventorinis"` | — | — | Inventorinis | — |
| `inventoriaus_tipas` | `"Neapskaitomas"` | — | — | Neapskaitomas | — |
| `inventoriaus_tipas` | `"Periodikos inventorinis"` | — | — | Periodikos inventorinis | — |
| `inventoriaus_tipas` | `"Fiktyvus"` | — | — | Fiktyvus | — |
| `inventoriaus_tipas` | `"Archyvinis"` | — | — | Archyvinis | — |
| `inventoriaus_tipas` | `"Periodikos archyvinis"` | — | — | Periodikos archyvinis | — |
| `inventoriaus_tipas` | `"Licencijos"` | — | — | Licencijos | — |
| `inventoriaus_tipas` | `"El. inventorinis"` | — | — | El. inventorinis | — |
| `periodikos_tipas` | `"MAGAZINE"` | — | — | Žurnalas | — |
| `periodikos_tipas` | `"NEWSPAPER"` | — | — | Laikraštis | — |
| `isdavimo_salyga` | `"IN_PLACE"` | — | — | Vietoje | — |
| `isdavimo_salyga` | `"TO_HOME"` | — | — | Į namus | — |
| `dabartines_kainos_valiuta` | `"Euras"` | — | — | Euras | — |
| `dabartines_kainos_valiuta` | `"Litas"` | — | — | Litas | — |
| `pradines_kainos_valiuta` | `"Litas"` | — | — | Litas | — |
| `pradines_kainos_valiuta` | `"Euras"` | — | — | Euras | — |
| `pradines_kainos_valiuta` | `"Rublis"` | — | — | Rublis | — |
| `pradines_kainos_valiuta` | `"Talonas"` | — | — | Talonas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `periodinio_leidinio_pavadinimas_lt` | `update(property: "periodinio_leidinio_pavadinimas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `nurasymo_priezastis_lt` | `update(property: "nurasymo_priezastis_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lnb/egzemplioriai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/egzemplioriai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lnb/egzemplioriai (https://data.gov.lt/datasets/2796/)
