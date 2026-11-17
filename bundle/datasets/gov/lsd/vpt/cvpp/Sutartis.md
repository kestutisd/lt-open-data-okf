---
type: Table
title: "Sutartis — Viešųjų pirkimų sutartys"
description: "Viešųjų pirkimų sutarčių lentelė."
resource: "https://get.data.gov.lt/datasets/gov/lsd/vpt/cvpp/Sutartis"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/vpt/cvpp.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/cvpp.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sutartis — Viešųjų pirkimų sutartys

Viešųjų pirkimų sutarčių lentelė. Lentelė sudaryta iš dokumento bei vidinio sistemos identifikatorių, sutarties sekos, CPV kodo, sutarties tipo, registracijos numerio, sutarties numerio, pirkimo numerio, statuso, sutarties objekto rūšies, jo pavadinimo, sutarties vertės, sutarties faktinio įvykdymo datos ir vertės, dokumento sudarymo, registracijos, įvedimo ir išsiuntimo datų, sutarties formos tipo, sutarties turinio, registruoto subjekto bei sisteminio vartotojo identifikatorių bei požymių, ar sutartis importuota ir, ar tinka išsiuntimui. Vienas įrašas atitinka vieną sutarties dokumentą.

- **Model:** `datasets/gov/lsd/vpt/cvpp/Sutartis`[^manifest]
- **Dataset:** [Viešųjų pirkimų duomenys](../cvpp.md) (`datasets/gov/lsd/vpt/cvpp`)
- **Manifest CSV:** [datasets/gov/lsd/vpt/cvpp.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/cvpp.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/vpt/cvpp/Sutartis`
- **Primary Key (`ref`):** `dok_id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dok_id` | `string` | — | `4` | `open` | — | Pagrindinis identifikatorius | — |
| `internal_id` | `string` | — | `4` | `open` | — | Vidinis identifikatorius | — |
| `cpv_codes` | `string` | — | `4` | `open` | — | Sutarties CPV kodas | — |
| `dok_sut_tipas` | `string` | — | `4` | `open` | — | Sutarties tipas | — |
| `dok_reg_nr` | `integer` | — | `4` | `open` | — | Sutarties registracijos numeris | — |
| `dok_sut_numeris` | `string` | — | `4` | `open` | — | Sutarties numeris | — |
| `dok_pirk_numeris` | `string` | — | `4` | `open` | — | Pirkimo numeris | — |
| `dok_statusas` | `string` | — | `4` | `open` | — | Sutarties statusas | — |
| `dok_sut_obj_rusis` | `string` | — | `4` | `open` | — | Sutarties objekto rūšis | — |
| `dok_sut_obj_pav` | `string` | — | `4` | `open` | — | Sutarties objektas | — |
| `dm` | `datetime` | `S` | `4` | `open` | — | DM data ir laikas | — |
| `dok_fakt_sut_ivyk_data` | `date` | `D` | `4` | `open` | — | Faktinė sutarties įvykdymo data | — |
| `dok_sut_verte` | `number` | — | `4` | `open` | — | Sutarties vertė | — |
| `dok_fakt_sut_ivyk_verte` | `number` | — | `4` | `open` | — | Faktinė sutarties įvykdymo vertė | — |
| `dok_sudarymo_data` | `date` | `D` | `4` | `open` | — | Dokumento sudarymo data | — |
| `dok_reg_data` | `date` | `D` | `4` | `open` | — | Dokumento registracijos data | — |
| `dok_sys_reg_data` | `date` | `D` | `4` | `open` | — | Dokumento registracijos sistemoje data | — |
| `dok_ivedimo_data` | `date` | `D` | `4` | `open` | — | Dokumento įvedimo data | — |
| `dok_issiuntimo_data` | `date` | `D` | `4` | `open` | — | Dokumento išsiuntimo data | — |
| `dok_sut_galiojimo_data` | `date` | `D` | `4` | `open` | — | Sutarties galiojimo data | — |
| `dok_formos_tipas` | `string` | — | `4` | `open` | — | Sutarties formos tipas | — |
| `dok_turinys` | `string` | — | `4` | `open` | — | Sutarties turinys | — |
| `dok_reg_sbj_id` | `string` | — | `4` | `open` | — | Išorinis raktas į sutarties registruotą subjektą | — |
| `dok_po_tinka_issiuntimui` | `integer` | — | `4` | `open` | — | Ar sutartis tinka išsiuntimui | — |
| `imported` | `boolean` | — | `4` | `open` | — | Ar sutartis importuota | — |
| `user_id` | `string` | — | `4` | `open` | — | Išorinis raktas į vartotoją | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/vpt/cvpp.csv
