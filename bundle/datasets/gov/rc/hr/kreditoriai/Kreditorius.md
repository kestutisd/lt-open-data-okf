---
type: Table
title: "Kreditorius — HR archyviniai duomenys apibūdinantys kreditorius"
description: "Spinta table datasets/gov/rc/hr/kreditoriai/Kreditorius (21 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/hr/kreditoriai/Kreditorius"
tags: [gov, rc, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/hr/kreditoriai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/hr/kreditoriai.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Kreditorius — HR archyviniai duomenys apibūdinantys kreditorius

- **Model:** `datasets/gov/rc/hr/kreditoriai/Kreditorius`[^manifest]
- **Dataset:** [Likviduoto hipotekos registro (HR) archyviniai duomenys apie kreditorius](../kreditoriai.md) (`datasets/gov/rc/hr/kreditoriai`)
- **Manifest CSV:** [datasets/gov/rc/hr/kreditoriai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/hr/kreditoriai.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/hr/kreditoriai/Kreditorius`
- **Primary Key (`ref`):** `sandorio_id, kreditoriaus_id`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sandorio_id` | `integer` | — | `2` | `open` | — | Sandorio identifikatorius dirbtinis | — |
| `kreditoriaus_id` | `integer` | — | `2` | `open` | — | Kreditoriaus identifikatorius dirbtinis | — |
| `amnt_grupe` | `string` | — | `3` | `open` | — | Kreditoriaus asmens tipo grupė | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Kreditoriaus amžiaus grupė | — |
| `reg_metai` | `integer` | — | `2` | `open` | — | Kreditoriaus registracijos metai | — |
| `sal_grupe` | `string` | — | `3` | `open` | — | Kreditoriaus šalies grupės pavadinimas | — |
| `sandorio_tipas` | `ref` | [/datasets/gov/rc/hr/tipu_klasifikatoriai/SandorioTipas](../tipu_klasifikatoriai/SandorioTipas.md) | `2` | `open` | — | Sandorio tipas | — |
| `sand_ireg_ketv` | `date` | `Q` | `2` | `open` | — | Sandorio įregistravimo metai - ketvirtis | — |
| `sand_isreg_ketv` | `date` | `Q` | `2` | `open` | — | Sandorio išregistravimo metai - ketvirtis | — |
| `iraso_priezastis` | `string` | — | `2` | `open` | — | Įrašo pagrindas | — |
| `sandorio_vieta` | `string` | — | `2` | `open` | — | Sandorio sudarymo vieta (sav. ; aps.) | — |
| `pri_dydis_rez` | `string` | — | `2` | `open` | — | Prievolės rėžių dydžiai | — |
| `pri_terminas_metai` | `integer` | — | `2` | `open` | — | Prievolės įvykdymo terminas (metai, NULL - nėra duomenų) | — |
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

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `reg_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `pri_terminas_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/hr/kreditoriai.csv
