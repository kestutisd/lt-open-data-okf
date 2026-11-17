---
type: Table
title: "VezysRegistras — Lietuvos Vėžio Registras"
description: "Spinta table datasets/gov/nvi/vezio_registras/VezysRegistras (27 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nvi/vezio_registras/VezysRegistras"
tags: [gov, nvi, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nvi/vezio_registras.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvi/vezio_registras.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# VezysRegistras — Lietuvos Vėžio Registras

- **Model:** `datasets/gov/nvi/vezio_registras/VezysRegistras`[^manifest]
- **Dataset:** [datasets/gov/nvi/vezio_registras](../vezio_registras.md) (`datasets/gov/nvi/vezio_registras`)
- **Manifest CSV:** [datasets/gov/nvi/vezio_registras.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvi/vezio_registras.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nvi/vezio_registras/VezysRegistras`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `amz_gr` | `string` | — | `4` | `open` | — | Amžiaus grupė | — |
| `apskritis` | `ref` | [/datasets/gov/rc/ar/apskritis/Apskritis](../../rc/ar/apskritis/Apskritis.md) | `4` | `open` | — | Paciento apskritis | — |
| `cm` | `string` | — | `4` | `open` | — | Klininkinė klasifikacija – cTNM M dalis | M – tolimosios metastazės |
| `cn` | `string` | — | `4` | `open` | — | Klinikinė klasifikacija – cTNM N dalis | N – regioniniai limfmazgiai |
| `ct` | `string` | — | `4` | `open` | — | Klinikinė klasifikacija – cTNM T dalis | T – pirminis navikas |
| `daug` | `integer` | — | `4` | `open` | — | Daugybiškumas (onkologinio susirgimo eilės numeris) | — |
| `is_apl` | `string` | — | `4` | `open` | — | Išaiškinimo aplinkybės | — |
| `lat` | `string` | — | `4` | `open` | — | Laterališkumas | — |
| `lok_grupe` | `string` | — | `4` | `open` | — | Lokalizacijų grupė | — |
| `lok_tlk10` | `ref` | [/datasets/gov/vlk/tlk10am/Tlk10am](../../vlk/tlk10am/Tlk10am.md) | `4` | `open` | — | Lokalizacijų grupės TLK-10 kodai | — |
| `lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `metai` | `integer` | — | `2` | `open` | — | Diagnozės nustatymo metai | — |
| `mrfg` | `string` | — | `2` | `open` | — | Morfologijos diferenciacijos laipsnis | — |
| `mrfgr` | `string` | — | `2` | `open` | — | Morfologijos grupė | — |
| `patv_auto` | `integer` | — | `4` | `open` | — | Ar patvirtinta autopsijos metu? | — |
| `patv_cito` | `integer` | — | `4` | `open` | — | Ar patvirtinta citologiškai? | — |
| `patv_klin` | `integer` | — | `4` | `open` | — | Ar patvirtinta tiktai kliniškai? | — |
| `patv_met_hist` | `integer` | — | `4` | `open` | — | Ar patvirtinta metastazių histologija? | — |
| `patv_ml` | `integer` | — | `4` | `open` | — | Ar patvirtinta tik pagal mirties liudijimą? | — |
| `patv_nz` | `integer` | — | `4` | `open` | — | Ar patvirtinimo būdas nežinomas? | — |
| `patv_pirm_hist` | `integer` | — | `4` | `open` | — | Ar patvirtinta pirminio naviko histologija? | — |
| `patv_tyr` | `integer` | — | `4` | `open` | — | Ar patvirtinta klinikiniais tyrimais? | — |
| `patv_zym` | `integer` | — | `4` | `open` | — | Ar patvirtinta vėžio žymenimis? | — |
| `pm` | `string` | — | `4` | `open` | — | Patologinė klasifikacija – pTNM M dalis | M – tolimosios metastazės |
| `pn` | `string` | — | `4` | `open` | — | Patologinė klasifikacija – pTNM N dalis | N – regioniniai limfmazgiai |
| `pt` | `string` | — | `4` | `open` | — | Patologinė klasifikacija – pTNM T dalis | T – pirminis navikas |
| `stad` | `string` | — | `4` | `open` | — | Stadija | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `is_apl` | `"Išaiškinta profilaktiškai"` | — | — | Išaiškinta profilaktiškai | — |
| `is_apl` | `"Kreipėsi savarankiškai"` | — | — | Kreipėsi savarankiškai | — |
| `is_apl` | `"Vykdant atrankinės patikros programą"` | — | — | Vykdant atrankinės patikros programą | — |
| `lat` | `"dešinė"` | — | — | Dešinė | — |
| `lat` | `"kairė"` | — | — | Kairė | — |
| `lat` | `"neporinis"` | — | — | Neporinis organas | — |
| `lat` | `"porinis organas, bet nžn."` | — | — | Porinis organas | — |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |
| `patv_auto` | `0` | — | — | Ne | — |
| `patv_auto` | `1` | — | — | Taip | — |
| `patv_cito` | `0` | — | — | Ne | — |
| `patv_cito` | `1` | — | — | Taip | — |
| `patv_klin` | `0` | — | — | Ne | — |
| `patv_klin` | `1` | — | — | Taip | — |
| `patv_met_hist` | `0` | — | — | Ne | — |
| `patv_met_hist` | `1` | — | — | Taip | — |
| `patv_ml` | `0` | — | — | Ne | — |
| `patv_ml` | `1` | — | — | Taip | — |
| `patv_nz` | `0` | — | — | Ne | — |
| `patv_nz` | `1` | — | — | Taip | — |
| `patv_pirm_hist` | `0` | — | — | Ne | — |
| `patv_pirm_hist` | `1` | — | — | Taip | — |
| `patv_tyr` | `0` | — | — | Ne | — |
| `patv_tyr` | `1` | — | — | Taip | — |
| `patv_zym` | `0` | — | — | Ne | — |
| `patv_zym` | `1` | — | — | Taip | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nvi/vezio_registras.csv
