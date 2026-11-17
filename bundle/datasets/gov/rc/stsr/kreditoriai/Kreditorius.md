---
type: Table
title: "Kreditorius — Duomenys apie įkeitimo ir hipotekos sandorių kreditorius (tipą, formą, šalį, amžių ir t. t.)"
description: "Spinta table datasets/gov/rc/stsr/kreditoriai/Kreditorius (23 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/stsr/kreditoriai/Kreditorius"
tags: [gov, rc, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/stsr/kreditoriai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/stsr/kreditoriai.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Kreditorius — Duomenys apie įkeitimo ir hipotekos sandorių kreditorius (tipą, formą, šalį, amžių ir t. t.)

- **Model:** `datasets/gov/rc/stsr/kreditoriai/Kreditorius`[^manifest]
- **Dataset:** [STSR duomenys apie įkeitimo ir hipotekos sandorių kreditorius](../kreditoriai.md) (`datasets/gov/rc/stsr/kreditoriai`)
- **Manifest CSV:** [datasets/gov/rc/stsr/kreditoriai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/stsr/kreditoriai.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/stsr/kreditoriai/Kreditorius`
- **Primary Key (`ref`):** `kreditoriaus_id`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kreditoriaus_id` | `integer` | — | `2` | `open` | — | Kreditoriaus dirbtinis identifikatorius šiame duomenų rinkinyje | — |
| `st_nr` | `integer` | — | `2` | `open` | — | Hipotekos / įkeitimo dirbtinis identifikatorius šiame duomenų rinkinyje | — |
| `amnt_grupe` | `string` | — | `4` | `open` | — | Kreditoriaus asmens tipo grupė | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Kreditoriaus amžiaus grupė | — |
| `reg_metai` | `date` | `Y` | `4` | `open` | — | Kreditoriaus registracijos metai | — |
| `sal_grupe` | `string` | — | `3` | `open` | — | Kreditoriaus šalies grupės pavadinimas | — |
| `st_tipas` | `string` | — | `2` | `open` | — | Hipotekos / įkeitimo tipas šiame duomenų rinkinyje | — |
| `st_ireg_ketv` | `date` | `Q` | `4` | `open` | — | Hipotekos / įkeitimo įregistravimo data (metai - ketvirtis) | — |
| `st_isreg_ketv` | `date` | `Q` | `4` | `open` | — | Hipotekos / įkeitimo išregistravimo data (metai - ketvirtis) | — |
| `iraso_priezastis` | `string` | — | `2` | `open` | — | Hipotekos / įkeitimo paskutinio įregistruoto įrašo tipas Sutarčių ir teisių suvaržymų registre | — |
| `sudarymo_vieta` | `string` | — | `3` | `open` | — | Hipotekos / įkeitimo sudarymo vieta (sav.; apskr.) | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Hipotekos / įkeitimo sudarymo vietos savivaldybės kodas iš Adresų registro (tik didmiesčių savivaldybės) | — |
| `apskritis` | `ref` | [/datasets/gov/rc/ar/apskritis/Apskritis](../../ar/apskritis/Apskritis.md) | `4` | `open` | — | Hipotekos / įkeitimo sudarymo vietos apskrities kodas iš Adresų registro | — |
| `pri_dydis_rez` | `string` | — | `3` | `open` | — | Prievolės rėžių dydžiai | — |
| `pri_terminas_metai` | `date` | `Y` | `4` | `open` | — | Prievolės įvykdymo terminas (metai) | — |
| `maksimalus` | `integer` | — | `4` | `open` | — | Ar maksimalioji hipoteka (1 - taip; 0 - ne) | — |
| `paprastas` | `integer` | — | `4` | `open` | — | Ar paprastoji hipoteka (1 - taip; 0 - ne) | — |
| `jungtinis` | `integer` | — | `4` | `open` | — | Ar jungtinė hipoteka (1 - taip; 0 - ne) | — |
| `svetimas` | `integer` | — | `4` | `open` | — | Ar svetimo turto hipoteka (1 - taip; 0 - ne) | — |
| `bendras` | `integer` | — | `4` | `open` | — | Ar bendroji hipoteka (1 - taip; 0 - ne) | — |
| `salyginis` | `integer` | — | `4` | `open` | — | Ar sąlyginė hipoteka (1 - taip; 0 - ne) | — |
| `pareikstinis` | `integer` | — | `4` | `open` | — | Ar pareikštinė (1 - taip; 0 - ne) | — |
| `imones` | `integer` | — | `4` | `open` | — | Ar įmonės hipoteka (1 - taip; 0 - ne) | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `amnt_grupe` | `"FA"` | — | — | Fizinis asmuo | — |
| `amnt_grupe` | `"JA"` | — | — | Juridinis asmuo | — |
| `amnt_grupe` | `"UFA"` | — | — | Užsienio fizinis asmuo | — |
| `amnt_grupe` | `"UJA"` | — | — | Užsienio juridinis asmuo | — |
| `amnt_grupe` | `"NEID"` | — | — | — | — |
| `maksimalus` | `0` | — | — | Ne | — |
| `maksimalus` | `1` | — | — | Taip | — |
| `paprastas` | `0` | — | — | Ne | — |
| `paprastas` | `1` | — | — | Taip | — |
| `jungtinis` | `0` | — | — | Ne | — |
| `jungtinis` | `1` | — | — | Taip | — |
| `svetimas` | `0` | — | — | Ne | — |
| `svetimas` | `1` | — | — | Taip | — |
| `bendras` | `0` | — | — | Ne | — |
| `bendras` | `1` | — | — | Taip | — |
| `salyginis` | `0` | — | — | Ne | — |
| `salyginis` | `1` | — | — | Taip | — |
| `pareikstinis` | `0` | — | — | Ne | — |
| `pareikstinis` | `1` | — | — | Taip | — |
| `imones` | `0` | — | — | Ne | — |
| `imones` | `1` | — | — | Taip | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/stsr/kreditoriai.csv
