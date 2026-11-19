---
type: Table
title: "SavivaldybeNtMokestis — NT mokesčio duomenys pagal savivaldybes"
description: "Nekilnojamo turto mokesčio (toliau - NTM) duomenų rinkinys"
resource: "https://get.data.gov.lt/datasets/gov/vmi/nt/SavivaldybeNtMokestis"
tags: [gov, vmi, savivaldybentmokestis, deployed, level-3, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/nt.csv#L56"
    title: "atviriduomenys/manifest — datasets/gov/vmi/nt.csv#L56"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1185/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/nt"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# SavivaldybeNtMokestis — NT mokesčio duomenys pagal savivaldybes

**Dataset Context:** Nekilnojamo turto mokesčio (toliau - NTM) duomenų rinkinys[^manifest]

- **Model:** `datasets/gov/vmi/nt/SavivaldybeNtMokestis`[^manifest]
- **Dataset:** [Nekilnojamo turto mokesčio duomenų rinkinys](../nt.md) (`datasets/gov/vmi/nt`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/nt.csv#L56](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/nt.csv#L56)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/nt/SavivaldybeNtMokestis` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Eilutės numeris | — |
| `sav_kodas` | `integer` | — | `2` | `open` | — | Savivaldybės kodas | Savivaldybės kodas (t. y. savivaldybės kodas, kuriame yra deklaruojamas avansinis NTM) |
| `sav_pav` | `string` | — | `2` | `open` | — | Savivaldybės pavadinimas | — |
| `tarifas` | `number` | `%` | `4` | `open` | — | Savivaldybės nustatytas mokesčio tarifas procentais | — |
| `metai` | `integer` | — | `2` | `open` | — | Deklaracijoje nurodyto mokestinio laikotarpio arba jo pradžios metai | — |
| `nt_verte_nuosavo` | `number` | — | `2` | `open` | — | S1 laukelyje nurodytoje savivaldybėje esančio nuosavo NT, apmokestinamo pagal S2 laukelyje nurodytą tarifą, vertė mokestinio laikotarpio pirmą dieną | Nurodytoje savivaldybėje esančio nuosavo NT, apmokestinamo pagal nurodytą tarifą, vertė mokestinio laikotarpio pirmą dieną, t. y. NTM deklaracijos KIT711S priedo S4 laukelis |
| `nt_verte_perimto` | `number` | — | `2` | `open` | — | S1 laukelyje nurodytoje savivaldybėje esančio perimto NT, apmokestinamo pagal S2 laukelyje nurodytą tarifą, vertė mokestinio laikotarpio pirmą dieną | Nurodytoje savivaldybėje esančio perimto NT, apmokestinamo pagal nurodytą tarifą, vertė mokestinio laikotarpio pirmą dieną, t. y. NTM deklaracijos KIT711S priedo S9 laukelis |
| `apskaiciuota_uz_nuosava_nt` | `number` | — | `2` | `open` | — | S8: pagal S2 laukelyje nurodytą tarifą apskaičiuota mokesčio suma už nuosavą nekilnojamąjį turtą | Pagal nurodytą tarifą apskaičiuota mokesčio suma už nuosavą NT, t. y. NTM deklaracijos KIT711S priedo S8 laukelis |
| `apskaiciuota_uz_perimta_nt` | `number` | — | `2` | `open` | — | S13: pagal S2 laukelyje nurodytą tarifą apskaičiuota mokesčio suma už perimtą nekilnojamąjį turtą | Pagal nurodytą tarifą apskaičiuota mokesčio suma už perimtą NT, t. y. NTM deklaracijos KIT711S priedo S13 laukelis |
| `apskaiciuota_pagal_tarifa` | `number` | — | `2` | `open` | — | S14: pagal S2 laukelyje įrašytą tarifą apskaičiuota mokesčio suma, tenkanti S1 laukelyje nurodytai savivaldybei | Pagal nurodytą tarifą apskaičiuota mokesčio suma (už nuosavą ir už perimtą NT), tenkanti nurodytai savivaldybei, dar neįvertinus suteiktų lengvatų, t. y. NTM deklaracijos KIT711S priedo S14 laukelis |
| `sav_apskaiciuota_suma` | `number` | — | `2` | `open` | — | S15: visa apskaičiuota mokesčio suma, tenkanti S1 laukelyje nurodytai savivaldybei (šio ir visų priedo KIT711S lapų su tokiais pačiais S1 laukelių kodais, kaip ir šiame lape, S14 laukelių suma) | Apskaičiuota mokesčio suma, tenkanti nurodytai savivaldybei (t. y. susumuojamos apskaičiuotos mokesčio sumos pagal skirtingus tarifus taikomus toje pačioje savivaldybėje), dar neįvertinus suteiktų lengvatų, t. y. NTM deklaracijos KIT711S priedo S15 laukelis |
| `sav_lengvata` | `number` | — | `2` | `open` | — | S16: mokesčio lengvata, suteikta S1 laukelyje nurodytos savivaldybės | Mokesčio lengvata, suteikta nurodytos savivaldybės, t. y. NTM deklaracijos KIT711S priedo S16 laukelis |
| `sav_mokescio_suma` | `number` | — | `2` | `open` | — | S17: visa mokesčio suma, tenkanti S1 laukelyje nurodytai savivaldybei | Visa mokesčio suma, tenkanti nurodytai savivaldybei, t. y. NTM deklaracijos KIT711S priedo S17 laukelis |
| `eilutes_nr_ffdata` | `integer` | — | `2` | `open` | — | Mėnuo. Sutampa su deklaracijos XML paketo eilutės Nr. (eilutės numeris lape pagal FFData numeraciją) | Mėnuo, kurį keitėsi (padidėjo ar sumažėjo) apmokestinamo NT mokestinės vertės |
| `nt_tipas` | `integer` | — | `4` | `open` | — | Apmokestinamo nekilnojamojo turto priklausomybė: nuosavas ar perimtas | Apmokestinamo NT priklausomybė: nuosavas ar perimtas, kai deklaruojamas NT vertės kitimas mėnesiais |
| `men_sk` | `integer` | — | `2` | `open` | — | S7: Mėnesių skaičius, kuriais mokestis skaičiuojamas nuo pasikeitusios vertės | Mėnesių skaičius, kuriais mokestis skaičiuojamas nuo pasikeitusios vertės |
| `nt_vertes_pokytis` | `number` | — | `2` | `open` | — | S5: S4 laukelyje nurodyto apmokestinamo turto vertės padidėjimas / sumažėjimas (sumažėjimas įrašomas su minuso ženklu) | Nurodyto apmokestinamo turto vertės padidėjimas / sumažėjimas (sumažėjimas įrašomas su minuso ženklu) |
| `isigijimas_netekimas` | `string` | — | `4` | `open` | — | S6: Vertės kitimo priežastys. Įsigijimas / netekimas | Vertės kitimo priežastys. Įsigijimas / netekimas |
| `rekonstrukcija` | `string` | — | `4` | `open` | — | S6: Vertės kitimo priežastys. Rekonstrukcija | Vertės kitimo priežastys. Rekonstrukcija |
| `kita` | `string` | — | `4` | `open` | — | S6: Vertės kitimo priežastys. Kita | Vertės kitimo priežastys. Kita |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `nt_tipas` | `1` | — | — | Nuosavas | — |
| `nt_tipas` | `2` | — | — | Perimtas | — |
| `isigijimas_netekimas` | `"Taip"` | `T` | — | Vertė kito dėl įsigijimo/netekimo | — |
| `isigijimas_netekimas` | `"Ne"` | `N` | — | Vertė nekito dėl įsigijimo/netekimo | — |
| `rekonstrukcija` | `"Taip"` | `T` | — | Vertė kito dėl rekonstrukcijos | — |
| `rekonstrukcija` | `"Ne"` | `N` | — | Vertė nekito dėl rekonstrukcijos | — |
| `kita` | `"Taip"` | `T` | — | Vertė kito dėl kitų priežasčių | — |
| `kita` | `"Ne"` | `N` | — | Vertė nekito dėl kitų priežasčių | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(ref: "id")` | `ref` | `4` | `open` | — | — | — |
| `(model)` | `update(model: "SavivaldybesNtMokestis")` | `ref` | — | — | — | — | — |
| `sav_kodas` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | — | — | — | — |
| `sav_kodas` | `update(property: "savivaldybe.sav_kodas", type: "")` | `type` | `4` | — | — | — | — |
| `sav_pav` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `4` | — | — | — | — |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `nt_verte_nuosavo` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `nt_verte_perimto` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `apskaiciuota_uz_nuosava_nt` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `apskaiciuota_uz_perimta_nt` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `apskaiciuota_pagal_tarifa` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `sav_apskaiciuota_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `sav_lengvata` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `sav_mokescio_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `eilutes_nr_ffdata` | `update(ref: "enum")` | `ref` | `4` | `open` | — | — | — |
| `nt_vertes_pokytis` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/nt.csv#L56 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/nt.csv#L56)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/nt (https://data.gov.lt/datasets/1185/)
