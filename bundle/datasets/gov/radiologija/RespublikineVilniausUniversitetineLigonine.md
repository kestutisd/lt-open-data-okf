---
type: Table
title: "RespublikineVilniausUniversitetineLigonine — Respublikinės Vilniaus universitetinės ligoninės pacientams atliktų radiologinių tyrimų duomenys"
description: "Informacinėje sistemoje „MedDream“ kaupiami Respublikinės VU ligoninės pacientams atliktų radiologinių tyrimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/radiologija/RespublikineVilniausUniversitetineLigonine"
tags: [gov, radiologija, respublikinevilniausuniversitetineligonine, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L444"
    title: "atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv#L444"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2762/"
    title: "data.gov.lt DCAT-AP — datasets/gov/radiologija"
    author: "team:vda"
    last_modified: "2026-10-26T00:00:00Z"
---

# RespublikineVilniausUniversitetineLigonine — Respublikinės Vilniaus universitetinės ligoninės pacientams atliktų radiologinių tyrimų...

Informacinėje sistemoje „MedDream“ kaupiami Respublikinės VU ligoninės pacientams atliktų radiologinių tyrimų duomenys. Duomenų rinkinyje pateikiami ir iki šiol atnaujinami nuo 2011 metų kaupiami duomenys. Vienas įrašas atitinka vieną tyrimo medicininį atvaizdą (visų tyrimo atvaizdų identifikatoriai unikalūs). Duomenų rinkinį sudaro: paciento pseudonimizuotas asmens kodas, tyrimo studijos identifikatorius, data, paciento gimimo metai iš paciento gimimo datos stulpelio ir iš validaus asmens kodo, lytis iš paciento lyties stulpelio ir asmens kodo, tyrimo serijos identifikatorius, paciento svoris, ūgis, tirta kūno dalis, serijos modalumas, aprašymas, tyrimo atvaizdo identifikatorius, apšvitos kampas, spinduliuotės dozė ir fotometrinė interpretacija. Dėl didelio medicininio atvaizdų kiekio įstaigos duomenų bazėje, rinkinys gali būti sudarytas panaudojus tik dalį visų galimų atvaizdų. Gimimo metai ir lytis iš validžių asmens kodų įtraukti, kad būtų galima nustatyti tikslesnius paciento duomenis, jeigu atitinkamuose paciento lentelės stulpeliuose nurodyta gimimo data ir lytis yra netiksli. Duomenų teikėjas – VšĮ Respublikinė Vilniaus universitetinė ligoninė. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^manifest]

- **Model:** `datasets/gov/radiologija/RespublikineVilniausUniversitetineLigonine`[^manifest]
- **Dataset:** [Pacientams atlikti radiologiniai tyrimai](../radiologija.md) (`datasets/gov/radiologija`)[^manifest]
- **Manifest CSV:** [datasets/gov/radiologija/radiologija.csv#L444](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L444)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/radiologija/RespublikineVilniausUniversitetineLigonine` (`deployed`)[^manifest]
- **Provider:** `radiologija`[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-10-26`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `paciento_asm_k` | `string` | — | `4` | `open` | — | Pseudonimizuotas paciento asmens kodas | — |
| `paciento_asm_k_val` | `string` | — | `4` | `open` | — | Paciento asmens kodo validumas | — |
| `tyrimo_studijos_uuid` | `string` | — | `4` | `open` | — | Tyrimo studijos identifikatorius | — |
| `tyrimo_studijos_data` | `date` | `D` | `4` | `open` | — | Tyrimo studijos data | — |
| `paciento_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai iš lentelės | — |
| `vda_paciento_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai iš validaus asmens kodo | — |
| `paciento_lytis` | `string` | — | `4` | `open` | — | Paciento lytis iš lentelės | — |
| `vda_paciento_lytis` | `string` | — | `4` | `open` | — | Paciento lytis iš validaus asmens kodo | — |
| `tyrimo_serijos_uuid` | `string` | — | `4` | `open` | — | Tyrimo serijos identifikatorius | — |
| `paciento_svoris` | `number` | — | `4` | `open` | — | Pacieno kūno svoris kilogramais | — |
| `paciento_ugis` | `integer` | — | `4` | `open` | — | Paciento ūgis centimetrais | — |
| `tirta_kuno_dalis` | `string` | — | `4` | `open` | — | Tirta paciento kūno dalis | — |
| `tyrimo_serijos_modalumas` | `string` | — | `4` | `open` | — | Tyrimo serijos modalumas | — |
| `tyrimo_serijos_aprasymas` | `string` | — | `3` | `open` | — | Tyrimo serijos aprašymas | — |
| `atvaizdo_uuid` | `string` | — | `4` | `open` | — | Atvaizdo pseudonimizuotas unikalus identifikatorius | — |
| `apsvita_as` | `number` | — | `4` | `open` | — | Apšvitos kampas arksekundėmis | — |
| `doze_dgy_cm2` | `number` | — | `4` | `open` | — | Spinduliuotė dozė decigrėjais kvadratiniame centimetre | — |
| `fotometrine_interpretacija` | `string` | — | `4` | `open` | — | Fotometrinė interpretacija | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paciento_asm_k_val` | `"Tinkamas"` | — | — | Tinkamas | — |
| `paciento_asm_k_val` | `"Netinkamas"` | — | — | Netinkamas | — |
| `paciento_lytis` | `"M"` | — | — | Moteris | — |
| `paciento_lytis` | `"V"` | — | — | Vyras | — |
| `paciento_lytis` | `"K"` | — | — | Kita | — |
| `vda_paciento_lytis` | `"M"` | — | — | Moteris | — |
| `vda_paciento_lytis` | `"V"` | — | — | Vyras | — |
| `fotometrine_interpretacija` | `"MONOCHROME1"` | — | — | Vienspalvis atvaizdas, kurio pikselio minimali vertė po transformacijų atitinka baltą | — |
| `fotometrine_interpretacija` | `"MONOCHROME2"` | — | — | Vienspalvis atvaizdas, kurio pikselio minimali vertė po transformacijų atitinka juodą | — |
| `fotometrine_interpretacija` | `"YBR_FULL_422"` | — | — | Atvaizdas, naudojantis vieną šviesumo ir dvi spalvų komponentes | — |
| `fotometrine_interpretacija` | `"RGB"` | — | — | Atvaizdas, naudojantis raudonos, žalios, mėlynos spalvų komponentes | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv#L444 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L444)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/radiologija (https://data.gov.lt/datasets/2762/)
