---
type: Table
title: "Subjektas — Viešojo maitinimo įmonių atitikties higienos reikalavimams vertinimas"
description: "Spinta table datasets/gov/vmvt/higienos_atitiktys/Subjektas (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/higienos_atitiktys/Subjektas"
tags: [gov, vmvt, subjektas, deployed, level-3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/higienos_atitiktis.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/vmvt/higienos_atitiktis.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Subjektas — Viešojo maitinimo įmonių atitikties higienos reikalavimams vertinimas

- **Model:** `datasets/gov/vmvt/higienos_atitiktys/Subjektas`[^manifest]
- **Dataset:** [Viešojo maitinimo įmonių atitikties higienos reikalavimams vertinimo duomenys](../higienos_atitiktys.md) (`datasets/gov/vmvt/higienos_atitiktys`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmvt/higienos_atitiktis.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/higienos_atitiktis.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/higienos_atitiktys/Subjektas` (`deployed`)[^manifest]
- **Provider:** `vmvt` — Valstybinė maisto ir veterinarijos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `string` | — | `0` | `open` | — | Juridinio asmens kodas | Šiuo metu požymis tuščias, nes tvarkoma VMVT maisto informacinė sistema |
| `mt_pavadinimas` | `string` | — | `1` | `open` | — | Maisto tvarkymo subjekto pavadinimas | — |
| `pavadinimas` | `string` | — | `0` | `open` | — | Juridinio asmens pavadinimas | Šiuo metu požymis tuščias, nes tvarkoma VMVT maisto informacinė sistema |
| `mt_adresas` | `string` | — | `0` | `open` | — | Maisto tvarkymo subjekto adresas | Šiuo metu požymis tuščias, nes tvarkoma VMVT maisto informacinė sistema |
| `riz_grupe` | `string` | — | `3` | `open` | — | Rizikos grupė | Padidintos rizikos grupei priskiriama įstaiga tikrinama kasmet. Vidutinės rizikos grupei priskiriama įstaiga tikrinama kartą per du metus. Mažos rizikos grupei priskiriama įstaiga tikrinama kartą per tris metus. Labai mažos rizikos grupei priskiriama įstaiga tikrinama kartą per šešis metus. Platesnis aprašymas apie rizikos grupes: https://vmvt.lt/maisto-sauga/kontrole/ukio-subjektu-registrai/subjektai-pagal-rizikos-grupes |
| `patikrinimas` | `date` | `D` | `4` | `open` | — | Viešojo maitinimo įstaigos patikrinimo data | — |
| `vertinimo_balas` | `number` | — | `4` | `open` | — | Vertinimo balas ("Kavos puodelių" reitingas) | Atliekant tokios įstaigos vertinimą, žiūrima bendra patalpų higiena, vertinama įrenginių priežiūra, patalpų ir inventoriaus būklė, darbuotojų asmens higienos laikymasis, taip pat visas maisto tvarkymo procesas: nuo žaliavų priėmimo iki temperatūrinio rėžimo palaikymo galutiniuose patiekaluose pateikiant vartotojams. Taip pat kontroliuojamas žaliavų, produktų ir patiekalų atsekamumas, laikymo sąlygos, tinkamumo vartoti terminai, terminis apdorojimas, maisto ruošimo patalpų ir naudojamos įrangos bei inventoriaus valymas ir dezinfekcija, susidariusių maisto atliekų tvarkymas. Aprašymas apie reitingavimą: https://vmvt.lt/maisto-sauga/verslui/viesasis-maitinimas/viesojo-maitinimo-imoniu-vertinimas. Plačiau: https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/TAIS.453987?jfwid=bkaxlbuo |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/higienos_atitiktis.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/higienos_atitiktis.csv#L5)
