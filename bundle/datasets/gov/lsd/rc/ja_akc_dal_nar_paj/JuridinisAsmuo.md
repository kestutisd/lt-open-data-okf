---
type: Table
title: "JuridinisAsmuo — Juridinių asmenų akcininkų, dalininkų, narių ir pajininkų skaičiai pagal tipą"
description: "Registrų centro Juridinių asmenų dalyvių informacinė sistema (JADIS) tvarko ir apdoroja juridinių asmenų dalyvių duomenis."
resource: "https://get.data.gov.lt/datasets/gov/lsd/rc/ja_akc_dal_nar_paj/JuridinisAsmuo"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/rc/ja_akc_dal_nar_paj.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/rc/ja_akc_dal_nar_paj.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# JuridinisAsmuo — Juridinių asmenų akcininkų, dalininkų, narių ir pajininkų skaičiai pagal tipą

Registrų centro Juridinių asmenų dalyvių informacinė sistema (JADIS) tvarko ir apdoroja juridinių asmenų dalyvių duomenis. Duomenys kaupiami nuo 2014 m. ir yra atnaujinami kasdien. Duomenų rinkinys apima juridinio asmens kodą ir pavadinimą, akcininkų, dalininkų, narių ir pajininkų skaičius pagal tipą. Galimi tipai yra Lietuvos arba užsienio fizinis asmuo, Lietuvos arba užsienio juridinis asmuo bei Lietuvos Respublikos savivaldybės.

- **Model:** `datasets/gov/lsd/rc/ja_akc_dal_nar_paj/JuridinisAsmuo`[^manifest]
- **Dataset:** [Juridinių asmenų akcininkų, dalininkų, narių ir pajininkų skaičiai pagal tipą](../ja_akc_dal_nar_paj.md) (`datasets/gov/lsd/rc/ja_akc_dal_nar_paj`)
- **Manifest CSV:** [datasets/gov/lsd/rc/ja_akc_dal_nar_paj.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/rc/ja_akc_dal_nar_paj.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/rc/ja_akc_dal_nar_paj/JuridinisAsmuo`
- **Primary Key (`ref`):** `org_jar_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `org_jar_kodas` | `string` | — | `4` | `open` | — | Juridinio asmens kodas | — |
| `org_pavadinimas` | `string` | — | `4` | `open` | — | Juridinio asmens pavadinimas | — |
| `vda_lr_fiz_akc_sk` | `integer` | `U` | `4` | `open` | — | Juridinio asmens akcininkų skaičius, kurie yra Lietuvos fiziniai asmenys | — |
| `vda_uzs_fiz_akc_sk` | `integer` | `U` | `4` | `open` | — | Juridinio asmens akcininkų skaičius, kurie yra užsienio fiziniai asmenys | — |
| `vda_lr_jur_akc_sk` | `integer` | `U` | `4` | `open` | — | Juridinio asmens akcininkų skaičius, kurie yra Lietuvos juridiniai asmenys | — |
| `vda_uzs_jur_akc_sk` | `integer` | `U` | `4` | `open` | — | Juridinio asmens akcininkų skaičius, kurie yra užsienio juridiniai asmenys | — |
| `vda_lr_sav_akc_sk` | `integer` | `U` | `4` | `open` | — | Juridinio asmens akcininkų skaičius, kurie yra Lietuvos savivaldybės | — |
| `vda_lr_fiz_nar_sk` | `integer` | `U` | `4` | `open` | — | Juridinio asmens narių skaičius, kurie yra Lietuvos fiziniai asmenys | — |
| `vda_uzs_fiz_nar_sk` | `integer` | `U` | `4` | `open` | — | Juridinio asmens narių skaičius, kurie yra užsienio fiziniai asmenys | — |
| `vda_lr_jur_nar_sk` | `integer` | `U` | `4` | `open` | — | Juridinio asmens narių skaičius, kurie yra Lietuvos juridiniai asmenys | — |
| `vda_uzs_jur_nar_sk` | `integer` | `U` | `4` | `open` | — | Juridinio asmens narių skaičius, kurie yra užsienio juridiniai asmenys | — |
| `vda_lr_sav_nar_sk` | `integer` | `U` | `4` | `open` | — | Juridinio asmens narių skaičius, kurie yra Lietuvos savivaldybės | — |
| `vda_lr_fiz_dal_sk` | `integer` | `U` | `4` | `open` | — | Juridinio asmens dalininkų skaičius, kurie yra Lietuvos fiziniai asmenys | — |
| `vda_uzs_fiz_dal_sk` | `integer` | `U` | `4` | `open` | — | Juridinio asmens dalininkų skaičius, kurie yra užsienio fiziniai asmenys | — |
| `vda_lr_jur_dal_sk` | `integer` | `U` | `4` | `open` | — | Juridinio asmens dalininkų skaičius, kurie yra Lietuvos juridiniai asmenys | — |
| `vda_uzs_jur_dal_sk` | `integer` | `U` | `4` | `open` | — | Juridinio asmens dalininkų skaičius, kurie yra užsienio juridiniai asmenys | — |
| `vda_lr_sav_dal_sk` | `integer` | `U` | `4` | `open` | — | Juridinio asmens dalininkų skaičius, kurie yra Lietuvos savivaldybės | — |
| `vda_lr_fiz_paj_sk` | `integer` | `U` | `4` | `open` | — | Juridinio asmens pajininkų skaičius, kurie yra Lietuvos fiziniai asmenys | — |
| `vda_uzs_fiz_paj_sk` | `integer` | `U` | `4` | `open` | — | Juridinio asmens pajininkų skaičius, kurie yra užsienio fiziniai asmenys | — |
| `vda_lr_jur_paj_sk` | `integer` | `U` | `4` | `open` | — | Juridinio asmens pajininkų skaičius, kurie yra Lietuvos juridiniai asmenys | — |
| `vda_uzs_jur_paj_sk` | `integer` | `U` | `4` | `open` | — | Juridinio asmens pajininkų skaičius, kurie yra užsienio juridiniai asmenys | — |
| `vda_lr_sav_paj_sk` | `integer` | `U` | `4` | `open` | — | Juridinio asmens pajininkų skaičius, kurie yra Lietuvos savivaldybės | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/rc/ja_akc_dal_nar_paj.csv
