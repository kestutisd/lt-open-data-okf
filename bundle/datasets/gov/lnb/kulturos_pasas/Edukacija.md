---
type: Table
title: "Edukacija — KEIS Kultūros paso edukacijos"
description: "Rinkinyje pateikiamos edukacinės programos, kurias gali(-ėjo) įsigyti mokiniai pagal kultūros paso programą."
resource: "https://get.data.gov.lt/datasets/gov/lnb/kulturos_pasas/Edukacija"
tags: [gov, lnb, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lnb/kulturos_pasas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/kulturos_pasas.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Edukacija — KEIS Kultūros paso edukacijos

Rinkinyje pateikiamos edukacinės programos, kurias gali(-ėjo) įsigyti mokiniai pagal kultūros paso programą. Kultūros pasas – priemonė, leidžianti moksleiviams valstybės lėšomis lankytis įvairiausiuose kultūros ir meno renginiuose: spektakliuose, koncertuose, parodose ir kitose pažintinėse bei edukacinėse kultūros veiklose. Priklausomai nuo amžiaus grupės, moksleiviai kultūros ir meno paslaugomis gali pasinaudoti dalyvaudami kartu su klase ar grupe, o nuo 16 metų paslaugomis gali pasinaudoti ir individualiai. Kultūrines edukacijas kultūros paveldo, etninės kultūros, architektūros, cirko, baleto, kino, lėlių teatro, dramos teatro, literatūros ir kt.

- **Model:** `datasets/gov/lnb/kulturos_pasas/Edukacija`[^manifest]
- **Dataset:** [KEIS Kultūros paso edukacijos](../kulturos_pasas.md) (`datasets/gov/lnb/kulturos_pasas`)
- **Manifest CSV:** [datasets/gov/lnb/kulturos_pasas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/kulturos_pasas.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lnb/kulturos_pasas/Edukacija`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `edukacijos_pavadinimas` | `string` | — | `4` | `open` | — | Edukacijos pavadinimas | — |
| `edukacijos_tiekejas` | `string` | — | `4` | `open` | — | Edukacijos tiekėjas | — |
| `pritaikyta_klasems` | `string` | — | `4` | `open` | — | Pritaikyta klasėms | — |
| `kaina` | `number` | — | `4` | `open` | — | Kaina, EUR | — |
| `trukme` | `integer` | `min` | `4` | `open` | — | Trukmė minutėmis | — |
| `aprasas` | `string` | — | `4` | `open` | — | Aprašas | — |
| `galioja_nuo` | `date` | `D` | `4` | `open` | — | Galioja nuo | — |
| `galioja_iki` | `date` | `D` | `4` | `open` | — | Galioja iki | — |
| `vykdymo_vieta` | `string` | — | `4` | `open` | — | Edukacijos vykdymo vieta | — |
| `sritis` | `string` | — | `4` | `open` | — | Edukacijos sritis | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybė, kur vykdoma edukacija | — |
| `metine_tema` | `string` | — | `4` | `open` | — | Metinė tema atliepianti atminties metus | — |
| `ugdomos_kompetencijos` | `string` | — | `4` | `open` | — | Edukacijoje ugdomos bendrosios ir kūrybinės kompetencijos | — |
| `pritaikyta_kurtiesiems` | `boolean` | — | `4` | `open` | — | Pritaikyta kurtiesiems | — |
| `pritaikyta_judejimo_negaliai` | `boolean` | — | `4` | `open` | — | Pritaikyta judėjimo negaliai | — |
| `pritaikyta_intelektualiniam_sutrikimui` | `boolean` | — | `4` | `open` | — | Pritaikyta intelektualiniam sutrikimui | — |
| `pritaikyta_regejimo_negaliai` | `boolean` | — | `4` | `open` | — | Pritaikyta regėjimo negaliai | — |
| `gali_uzsisakyti_savarankiskai` | `boolean` | — | `4` | `open` | — | Gali užsisakyti savarankiškai | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `edukacijos_pavadinimas` | `update(property: "edukacijos_pavadinimas@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `pritaikyta_klasems` | `"update(property: ""pritaikyta_klasems[]"", type: ""array"", source: ""pritaikyta_klasems"")"` | `property` | `4` | — | — | — | — |
| `kaina` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `aprasas` | `update(property: "aprasas@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `sritis` | `"update(property: ""sritis[]"", type: ""array"", source: ""sritis"")"` | `property` | `4` | — | — | — | — |
| `ugdomos_kompetencijos` | `"update(property: ""ugdomos_kompetencijos[]"", type: ""array"", source: ""ugdomos_kompetencijos"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lnb/kulturos_pasas.csv
