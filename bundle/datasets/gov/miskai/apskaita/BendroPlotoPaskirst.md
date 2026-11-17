---
type: Table
title: "BendroPlotoPaskirst — Bendro žemės ploto pasiskirstymas pagal žemės naudmenas (ha)"
description: "Spinta table datasets/gov/miskai/apskaita/BendroPlotoPaskirst (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/apskaita/BendroPlotoPaskirst"
tags: [gov, miskai, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/miskai/apskaita.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/apskaita.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# BendroPlotoPaskirst — Bendro žemės ploto pasiskirstymas pagal žemės naudmenas (ha)

- **Model:** `datasets/gov/miskai/apskaita/BendroPlotoPaskirst`[^manifest]
- **Dataset:** [datasets/gov/miskai/apskaita](../apskaita.md) (`datasets/gov/miskai/apskaita`)
- **Manifest CSV:** [datasets/gov/miskai/apskaita.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/apskaita.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/apskaita/BendroPlotoPaskirst`
- **Primary Key (`ref`):** `zemes_misku_gr`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `zemes_misku_gr` | `string` | — | `3` | — | — | — | — |
| `bendras_plotas` | `number` | `ha` | `4` | `open` | — | Bendras žemės plotas | — |
| `misko_zeme` | `number` | `ha` | `4` | `open` | — | Miško žemė | — |
| `viso_zem_uk_naudm` | `number` | `ha` | `4` | `open` | — | Žemės ūkio naudmenos. Iš viso | — |
| `ariama` | `number` | `ha` | `4` | `open` | — | Žemės ūkio naudmenos. Iš jų - ariama | — |
| `sodai` | `number` | `ha` | `4` | `open` | — | Žemės ūkio naudmenos. Iš jų - sodai | — |
| `pievos_ganykl` | `number` | `ha` | `4` | `open` | — | Žemės ūkio naudmenos. Iš jų - pievos ir ganyklos | — |
| `viso_keliai` | `number` | `ha` | `4` | `open` | — | Keliai. Iš viso | — |
| `bendro_naud_keliai` | `number` | `ha` | `4` | `open` | — | Keliai. Iš jų - bendro naudojimo | — |
| `uzstatyta_terit` | `number` | `ha` | `4` | `open` | — | Užstatyta teritorija | — |
| `vandenys` | `number` | `ha` | `4` | `open` | — | Vandenys | — |
| `viso_kita_zem` | `number` | `ha` | `4` | `open` | — | Kita žemė. Iš viso | — |
| `krumai` | `number` | `ha` | `4` | `open` | — | Kita žemė. Iš jos - krūmai | — |
| `pelkes` | `number` | `ha` | `4` | `open` | — | Kita žemė. Iš jos - pelkės | — |
| `pazeista_zeme` | `number` | `ha` | `4` | `open` | — | Kita žemė. Iš jos - pažeista žemė | — |
| `nenaudojama_zeme` | `number` | `ha` | `4` | `open` | — | Kita žemė. Iš jos - nenaudojama žemė | — |
| `nusausinta_zeme` | `number` | `ha` | `4` | `open` | — | Nusausinta žemė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/apskaita.csv
