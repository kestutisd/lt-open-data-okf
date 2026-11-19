---
type: Table
title: "VersloLiudijimas — Gyventojams išduotų verslo liudijimų duomenys"
description: "Spinta table datasets/gov/vmi/verslo_liudijimai/VersloLiudijimas (22 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/verslo_liudijimai/VersloLiudijimas"
tags: [gov, vmi, versloliudijimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/verslo_liudijimai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/vmi/verslo_liudijimai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2069/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/verslo_liudijimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# VersloLiudijimas — Gyventojams išduotų verslo liudijimų duomenys

- **Model:** `datasets/gov/vmi/verslo_liudijimai/VersloLiudijimas`[^manifest]
- **Dataset:** [Fizinių asmenų, vykdančių veiklą pagal verslo liudijimą, duomenys](../verslo_liudijimai.md) (`datasets/gov/vmi/verslo_liudijimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/verslo_liudijimai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/verslo_liudijimai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/verslo_liudijimai/VersloLiudijimas` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
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

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/verslo_liudijimai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/verslo_liudijimai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/verslo_liudijimai (https://data.gov.lt/datasets/2069/)
