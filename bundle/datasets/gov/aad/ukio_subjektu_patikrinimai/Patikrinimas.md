---
type: Table
title: "Patikrinimas — Ūkio subjekto metinis patikrinimas"
description: "Spinta table datasets/gov/aad/ukio_subjektu_patikrinimai/Patikrinimas (31 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aad/ukio_subjektu_patikrinimai/Patikrinimas"
tags: [gov, aad, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aad/ukio_subjektu_patikrinimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aad/ukio_subjektu_patikrinimai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Patikrinimas — Ūkio subjekto metinis patikrinimas

- **Model:** `datasets/gov/aad/ukio_subjektu_patikrinimai/Patikrinimas`[^manifest]
- **Dataset:** [Ūkio subjektų metiniai patikrinimai](../ukio_subjektu_patikrinimai.md) (`datasets/gov/aad/ukio_subjektu_patikrinimai`)
- **Manifest CSV:** [datasets/gov/aad/ukio_subjektu_patikrinimai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aad/ukio_subjektu_patikrinimai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aad/ukio_subjektu_patikrinimai/Patikrinimas`
- **Primary Key (`ref`):** `eil_nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `integer` | — | `4` | `open` | — | Eilės Nr. | — |
| `metai` | `date` | `Y` | `4` | `open` | — | Patikrinimo metai | — |
| `valdyba_dep` | `string` | — | `4` | `open` | — | Valdyba, departamentas | — |
| `padalinys` | `string` | — | `4` | `open` | — | Padalinys | — |
| `akto_tipas` | `string` | — | `3` | `open` | — | Akto dokumento tipas | — |
| `dok_registruotas` | `date` | `D` | `4` | `open` | — | Dokumento registravimo data | — |
| `planinis` | `boolean` | — | `4` | `open` | — | Ar patikrinimas planinis | — |
| `objekto_tipas` | `string` | — | `4` | `open` | — | Objekto tipas | — |
| `dalyvav_pareigunu` | `integer` | `U` | `4` | `open` | — | Patikrinimą atlikusių ar dalyvavusių pareigūnų skaičius | — |
| `rusis` | `string` | — | `4` | `open` | — | Patikrinimo rūšis | — |
| `tikrinta_veikla` | `string` | — | `3` | `open` | — | Tikrinta ūkinė veikla | — |
| `tiksli_tikrinta_veikla` | `string` | — | `2` | `open` | — | Patikslinta tikrinta ūkinė veikla | — |
| `objekto_tipk_priedas` | `string` | — | `4` | `open` | — | Objektas turi TIPK I priedą, TL (TIPK II) | — |
| `objekto_kiti_aplinkosaug_leidimai` | `string` | — | `1` | `open` | — | Objektas turi kitus aplinkosauginius leidimus | Neprivaloma pildyti |
| `pazeidimai_pagal_ank` | `string` | — | `2` | `open` | — | Pažeidimų straipsniai pagal ANK | — |
| `skirta_adm_bauda` | `number` | — | `2` | `open` | — | Skirta suma (administracinė bauda) | Neprivaloma pildyti |
| `aplinkosauginio_pazeidimo_grupe` | `string` | — | `3` | `open` | — | Aplinkosauginio pažeidimo grupė | Neprivaloma pildyti |
| `nustatyti_mazareiksm_pazeidim` | `boolean` | — | `4` | `open` | — | Nustatyti mažareikšmiai pažeidimai | — |
| `duotas_zodin_nurodymas` | `boolean` | — | `4` | `open` | — | Duotas žodinis nurodymas | — |
| `surasyt_nurodym_pasal_pazeidim` | `boolean` | — | `4` | `open` | — | Surašytas nurodymas pašalinti mažareikšmį pažeidimą | — |
| `paskaiciuot_mokst_padidint_tarif` | `number` | — | `2` | `open` | — | Paskaičiuotas mokestis padidintu tarifu | — |
| `skirta_jur_bauda` | `number` | — | `2` | `open` | — | Skirta suma (juridinė bauda) | Neprivaloma pildyti |
| `paskaiciuotos_zalos_tipas` | `string` | — | `3` | `open` | — | Paskaičiuotos žalos tipas | Neprivaloma pildyti |
| `paimti_daiktai` | `string` | — | `1` | `open` | — | Paimti daiktai | — |
| `suteikta_konsultacija` | `boolean` | — | `4` | `open` | — | Patikrinimo metu suteikta konsultacija | — |
| `atvr` | `boolean` | — | `4` | `open` | — | Atliekų tvarkytojų valstybės registras | — |
| `entp` | `boolean` | — | `4` | `open` | — | Eksploatuoti netinkamos transporto priemonės | — |
| `gamintojai_importuotojai` | `string` | — | `2` | `open` | — | Gamintojai, importuotojai | — |
| `ozona_ardancios_medziagos` | `boolean` | — | `4` | `open` | — | Vykdyta ozoną ardančios medžiagų kontrolė | Nenaudoti |
| `nitratu_direktyva_tikrinta` | `string` | — | `2` | `open` | — | Nitratų direktyva. Tikrinta sritis | — |
| `nitratu_direktyva_nustatyti_pazeidimai` | `string` | — | `2` | `open` | — | Nitratų direktyva. Nustatyti pažeidimai pagal sritis | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `objekto_tipas` | `"Ūkio subjektas"` | — | — | — | — |
| `objekto_tipas` | `"Fizinis asmuo"` | — | — | — | — |
| `objekto_tipas` | `"Teritorija"` | — | — | — | — |
| `objekto_tipas` | `"Kita"` | — | — | — | — |
| `rusis` | `"Išplėstinis"` | — | — | — | — |
| `rusis` | `"Teminis"` | — | — | — | — |
| `rusis` | `"Bendras"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `skirta_adm_bauda` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `paskaiciuot_mokst_padidint_tarif` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `skirta_jur_bauda` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aad/ukio_subjektu_patikrinimai.csv
