---
type: Table
title: "VersloLiudijimas — Gyventojams išduotų verslo liudijimų duomenys"
description: "Spinta table datasets/gov/vmi/verslo_liudijimai/VersloLiudijimas (22 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/verslo_liudijimai/VersloLiudijimas"
tags: [gov, vmi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmi/verslo_liudijimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/verslo_liudijimai.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# VersloLiudijimas — Gyventojams išduotų verslo liudijimų duomenys

- **Model:** `datasets/gov/vmi/verslo_liudijimai/VersloLiudijimas`[^manifest]
- **Dataset:** [datasets/gov/vmi/verslo_liudijimai](../verslo_liudijimai.md) (`datasets/gov/vmi/verslo_liudijimai`)
- **Manifest CSV:** [datasets/gov/vmi/verslo_liudijimai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/verslo_liudijimai.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/verslo_liudijimai/VersloLiudijimas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eiles_nr` | `string` | — | `4` | `open` | — | Įrašo eilės numeris | — |
| `mm_kodas` | `string` | — | `4` | `open` | — | Mokesčių mokėtojo kodas | — |
| `registracija` | `date` | `D` | `4` | `open` | — | Verslo liūdijimo reistracijos data | — |
| `metai` | `integer` | — | `2` | `open` | — | Mokestinio laikotarpio"," kuriam išduotas verslo liudijimas"," metai | — |
| `grupe` | `integer` | — | `4` | `open` | — | Veiklos grupė"," priskirta pagal prašyme išduoti VL nurodytą veiklos rūšies arba jos porūšių grupę. Veiklos rūšies grupė. | — |
| `teritorija` | `integer` | — | `4` | `open` | — | Veiklos teritorija. Veiklos teritorija ("," "," išskyrus išskirtąsias savivaldybes",") | — |
| `savivaldybe` | `integer` | — | `2` | `open` | — | Asmens"," kuriam išduotas verslo liudijimas"," gyvenamosios vietos savivaldybės kodas | — |
| `teritorija_kodas` | `integer` | — | `2` | `open` | — | Savivaldybė, kurią asmuo nurodo pildydamas prašymą, kai pasirenka teritoriją „konkrečioje savivaldybėje“ (nuo pasirinktos teritorijos priklauso VL kaina) | — |
| `rusies_kodas` | `string` | — | `2` | `open` | — | Veiklos"," kuria verčiamasi įsigijus verslo liudijimą"," rūšies kodas (pirmoji kodo dalis) | — |
| `rusis_pavadinimas` | `string` | — | `2` | `open` | — | Veiklos"," kuria verčiamasi įsigijus verslo liudijimą"," rūšies pavadinimas | — |
| `evrk_klases` | `string` | — | `2` | `open` | — | EVRK klasės pavadinimas | — |
| `data_nuo` | `date` | `D` | `4` | `open` | — | Verslo liūdijimo įsigaliojimo pradžia | — |
| `data_iki` | `date` | `D` | `4` | `open` | — | Verslo liūdijimo įsigaliojimo pabaiga | — |
| `sprendimo_data` | `date` | `D` | `4` | `open` | — | Sprendimo data dėl prašymo"," atitinkančio aktualią VL versiją (VL pratęsimo) | — |
| `veiklos_pabaiga` | `date` | `D` | `4` | `open` | — | Prašyme "Nutraukti veiklą" nurodyta pirmoji diena"," kurią nebevykdoma veikla jai nutrūkus dėl VL įsigijusio asmens mirties"," ligos"," išvykimo ar kitų priežasčių | — |
| `anuliavimo_data` | `date` | `D` | `4` | `open` | — | Verslo liudijimo anuliavimo VMI data ir laikas | — |
| `nutraukimo_pozymis` | `string` | — | `4` | `open` | — | Požymis"," nurodantis priežasčių"," dėl kurių nutrūko veikla pagal verslo liudijimą"," grupę. | — |
| `veiklos_vieta_veiksmas` | `integer` | — | `4` | `open` | — | VL veiklos galiojimas: | — |
| `veiklos_sav` | `integer` | — | `2` | `open` | — | Adreso, kuriame asmuo nurodo, kad vykdys veiklą, savivaldybė. | — |
| `anuliavimo_priezastis_aprasymas` | `string` | — | `4` | `open` | — | VL anuliavimo priežastis | — |
| `veiklos_tipas` | `integer` | — | `4` | `open` | — | Ar tai stacionarioje vietoje vykdoma veikla. | — |
| `lengvata` | `string` | — | `4` | `open` | — | Lengvatos priežasties pavadinimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `grupe` | `1` | — | — | 1 - gamyba | — |
| `grupe` | `2` | — | — | 2 - paslaugos | — |
| `grupe` | `3` | — | — | 3 - prekyba | — |
| `teritorija` | `1` | — | — | 1- neribota | — |
| `teritorija` | `2` | — | — | 2 - visur | — |
| `teritorija` | `3` | — | — | 3 - konkrečioje savivaldybėje | — |
| `nutraukimo_pozymis` | `"I"` | — | — | I - išvykimas | — |
| `nutraukimo_pozymis` | `"L"` | — | — | L - liga | — |
| `nutraukimo_pozymis` | `"K"` | — | — | K - kita su mokesčio grąžinimu | — |
| `nutraukimo_pozymis` | `"A"` | — | — | A - nutraukimas be mokesčio grąžinimo | — |
| `veiklos_vieta_veiksmas` | `0` | — | — | 0 - išbraukti (anksčiau įrašyta) nuo laukelyje PRADZIA datos"," | — |
| `veiklos_vieta_veiksmas` | `1` | — | — | 1 - įrašyti nuo laukelyje PRADZIA datos"," | — |
| `veiklos_vieta_veiksmas` | `2` | — | — | 2 - įrašyti nuo laukelyje PRADZIA datos iki laukelyje PABAIGA | — |
| `anuliavimo_priezastis_aprasymas` | `"Anuliuota"` | — | — | VL anuliuotas | — |
| `anuliavimo_priezastis_aprasymas` | `"Galioja"` | — | — | Ne - VL galioja | — |
| `veiklos_tipas` | `0` | — | — | 0 - nestacionari | — |
| `veiklos_tipas` | `1` | — | — | 1 - stacionari | — |
| `lengvata` | `"Taip"` | — | — | Taip - lengvatą turi | — |
| `lengvata` | `"Ne"` | — | — | Ne - lengvatos neturi | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.sav_kodas", type: "")` | `type` | `4` | — | — | — | — |
| `teritorija_kodas` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `teritorija_kodas` | `update(property: "savivaldybe.sav_kodas", type: "")` | `type` | `4` | — | — | — | — |
| `veiklos_sav` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `veiklos_sav` | `update(property: "savivaldybe.sav_kodas", type: "")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/verslo_liudijimai.csv
