---
type: Table
title: "PreparatasPakuote — Valstybinės vaistų kontrolės tarnybos duomenys apie vaistinius preparatus ir jų pakuotes"
description: "\"Duomenys apie VVKT (Valstybinės vaistų kontrolės tarnybos) registruotus vaistinius preparatus ir jų pakuotes."
resource: "https://get.data.gov.lt/datasets/gov/vvkt/vaistiniai_preparatai/PreparatasPakuote"
tags: [gov, vvkt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkt/vaistiniai_preparatai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistiniai_preparatai.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# PreparatasPakuote — Valstybinės vaistų kontrolės tarnybos duomenys apie vaistinius preparatus ir jų pakuotes

"Duomenys apie VVKT (Valstybinės vaistų kontrolės tarnybos) registruotus vaistinius preparatus ir jų pakuotes. Vieną eilutę sudaro - unikalus vaistinio preparato identifikacinis numeris, vaistinio preparato pakuotės identifikaciniai numeriai, taip pat informacija apie tai, kokia veiklioji(-iosios) medžiaga(-os) sudaro vaistinį preparatą, koks vaistinio preparato stiprumas, farmacinė forma(-os), grupė ir pogrupis, recepto poreikis, vaistinio preparato stebėjimo ir kontrolės būsenos, tiekimo Lietuvos Respublikos rinkai pagrindas, kada vaistinis preparatas pirmą kartą užregistruotas, kada paskutinį kartą perregistruotas ir kokia dabartinė vaistinio preparato stadija ("Registruotas", "Išregistruotas", "Perregistruotas"), bei informacija apie vaistinio preparato tiekėją - juridinio asmens pavadinimas ir šalis, bei paraiškos tipas. Eilutėje taip pat yra informacija apie vaistinio preparato pakuotę - pakuotės tiekimo būsena, registracijos numeris, tipas, aprašymas, recepto poreikis. Paskutiniai du stulpeliai nurodo informacija apie duomenų naujumą, t.y., kada įrašas apie vaistinį preparatą (vid_atnaujintas) arba vaistinio preparato pakuotę (pakid_atnaujintas) buvo atnaujintas paskutinį kartą VVKT informacinėje sistemoje."

- **Model:** `datasets/gov/vvkt/vaistiniai_preparatai/PreparatasPakuote`[^manifest]
- **Dataset:** [Valstybinės vaistų kontrolės registruotų vaistinių preparatų duomenų rinkinys](../vaistiniai_preparatai.md) (`datasets/gov/vvkt/vaistiniai_preparatai`)
- **Manifest CSV:** [datasets/gov/vvkt/vaistiniai_preparatai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistiniai_preparatai.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkt/vaistiniai_preparatai/PreparatasPakuote`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | VDA ID | Valstybės Duomenų Agentūros įrašo identifikatorius. |
| `vid` | `string` | — | `4` | `open` | — | Vaisto ID | Unikalus vaistinio preparato identifikatorius, automatiškai generuojamas sistemos. |
| `pak_id` | `string` | — | `4` | `open` | — | Pakuotės ID | Unikalus vaistinio preparato pakuotės identifikatorius, automatiškai generuojamas sistemos, kiekvienai naujai vaistinio preparato pakuotei didinamas vienetu. |
| `npak_id` | `string` | — | `4` | `open` | — | Nacionalinis pakuotės ID | Unikalus nacionalinis vaistinio preparato pakuotės identifikatorius, automatiškai generuojamas sistemos, kiekvienai naujai vaistinio preparato pakuotei didinamas vienetu. |
| `npak7_id` | `string` | — | `4` | `open` | — | Septynių skaitmenų pakuotės ID | Unikalus nacionalinis septynženklis vaistinio preparato pakuotės identifikatorius, automatiškai generuojamas sistemos: prie npak_id pridedamas skaičius 1000000. |
| `atc_kodas` | `string` | — | `4` | `open` | — | ATC kodas | Veikliosios medžiagos anatominės-terapinės-cheminės klasifikacijos kodas. |
| `preparato_pav` | `string` | — | `2` | `open` | — | Vaistinio preparato pavadinimas | Vaistinio preparato sugalvotas pavadinimas, vietoje formalaus ilgo pavadinimo. |
| `veiklioji_medz_lt` | `string` | — | `4` | `open` | — | Veiklioji medžiaga | "Vaistinio preparato veikliosios medžiagos pavadinimas. Jei vaistinį preparatą sudaro keli komponentai, tai skirtingų komponentų veikliosios medžiagos atskiriamos "+" simboliu." |
| `veikl_angl_pavad` | `string` | — | `4` | `open` | — | Angliškas pavadinimas | Veikliosios medžiagos angliškas pavadinimas. |
| `stiprumas` | `string` | — | `2` | `open` | — | Stiprumas | "Veikliosios medžiagos kiekis vienoje dozėje. Jei vaistinį preparatą sudaro keli komponentai, tai skirtingų komponentų veikliųjų medžiagų stiprumai atskiriami"+" simboliu." |
| `farmacine_forma_lt` | `string` | — | `4` | `open` | — | Farmacinė forma | "Vaistinio preparato farmacinė forma. Kuomet vaistinis preparatas turi kelias veikliąsias medžiagas, jų formos gali būti atskirtos "+". Tuo atveju, kai farmacinės formos sutampa forma rašoma 1 kartą." |
| `vartojimo_budas` | `string` | — | `4` | `open` | — | Vartojimo būdas | Vaistinio preparato vartojimo būdas. |
| `vaist_prep_grupe` | `string` | — | `4` | `open` | — | Vaistinio preparato grupe | Vaistinio preparato grupės pavadinimas. |
| `vaist_prep_pogrupis` | `string` | — | `4` | `open` | — | Vaistinio preparato pogrupis | Vaistinio preparato pogrupio pavadinimas. |
| `recepto_poreikis` | `string` | — | `4` | `open` | — | Recepto poreikis | Vaistinio preparato recepto poreikis. |
| `ar_kontroliuojamas` | `boolean` | — | `4` | `open` | — | Kontrolės būsena | Požymis, nurodantis, ar vaistinis preparatas yra įtrauktas į kontroliuojamų vaistinių preparatų sąrašą. |
| `ar_stebimas` | `boolean` | — | `4` | `open` | — | Stebėjimo būsena | Požymis, nurodantis, ar yra vykdoma papildoma vaistinio preparato stebėsena. |
| `tiekimo_lr_rinkai_pagr` | `string` | — | `4` | `open` | — | Tiekimo Lietuvos Respublikos rinkai pagrindas | Tiekimo Lietuvos Respublikos rinkai pagrindas, kitaip registracijos procedūros pavadinimas. |
| `registracijos_data` | `date` | `1D` | `4` | `open` | — | Registracijos data | Kada vaistinis preparatas buvo užregistruotas pirmą kartą. |
| `perregistravimo_data` | `date` | `1D` | `4` | `open` | — | Perregistravimo data | Kada vaistas buvo paskutinį kartą perregistruotas. |
| `stadija` | `string` | — | `4` | `open` | — | Stadija | Dabartinė vaistinio preparato stadija. |
| `pak_tiekimo_busena` | `string` | — | `4` | `open` | — | Pakuotės tiekimo būsena | Dabartinė vaistinio preparato pakuotės tiekimo būsena. |
| `pak_reg_nr` | `string` | — | `4` | `open` | — | Pakuotės registracijos numeris | Vaistinio preparato pakuotės registracijos eilės numeris, unikalus vienos vaistinio preparato pakuotės ribose. |
| `pakuotes_tipas` | `string` | — | `4` | `open` | — | Pakuotės tipas | Vaistinio preparato talpyklės tipas. |
| `pak_aprasymas` | `string` | — | `2` | `open` | — | Pakuotės aprašymas | Vaistinio preparato pakuotės aprašymas. |
| `pak_recepto_poreikis` | `string` | — | `4` | `open` | — | Pakuotės recepto poreikis | "Šio lauko reikšmė dažniausiai sutampa su "recepto_poreikis" lauko reikšme, tačiau būna atvėjų, kai šių laukų reikšmės skiriasi, pvz, 10 ir 20 pakuotės yra nereceptinės, o 50 receptinė. Vaistiniam preparatui tokiu atveju priskirtas požymis "Nereceptinis/Receptinis"." |
| `registruotojas` | `string` | — | `2` | `open` | — | Registruotojas | Juridinio asmens, kuris registruoja vaistinį preparatą, pavadinimas. |
| `registruotojo_vals` | `string` | — | `4` | `open` | — | Registruotojo valstybė | Valstybės pavadinimas, kurioje yra registruotas juridinis asmuo. |
| `paraiskos_tipas` | `string` | — | `4` | `open` | — | Paraiškos tipas | "Paraiškos tipas, nusakantis pagai kokį Direktyvos 2001/83/EB straipsnį paraiška teikiama, pavyzdžiui, "pagai 8(3) straipsnį", "pagal 10 (1) straipsnį" ir pan." |
| `vid_atnaujintas` | `datetime` | `1L` | `4` | `open` | — | VID atnaujintas | Laiko žyma kada paskutinį kartą buvo atnaujinta informacija apie vaistinį preparatą VVKT informacinėje sistemoje. |
| `pakid_atnaujintas` | `datetime` | `1L` | `4` | `open` | — | Pakuotės ID atnaujintas | Laiko žyma kada paskutinį kartą buvo atnaujinta informacija apie vaistinio preparato pakuotę VVKT informacinėje sistemoje. |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vaist_prep_grupe` | `"Vaistinis preparatas"` | — | — | Vaistinis preparatas | — |
| `recepto_poreikis` | `"Receptinis"` | — | — | Receptinis | — |
| `recepto_poreikis` | `"Nereceptinis"` | — | — | Nereceptinis | — |
| `recepto_poreikis` | `"Nereceptinis/Receptinis"` | — | — | Nereceptinis/Receptinis | — |
| `stadija` | `"Išregistruotas"` | — | — | Išregistruotas | — |
| `stadija` | `"Perregistruotas"` | — | — | Perregistruotas | — |
| `stadija` | `"Sustabdytas"` | — | — | Sustabdytas | — |
| `stadija` | `"Registruotas"` | — | — | Registruotas | — |
| `pak_tiekimo_busena` | `"Netiekiama"` | — | — | Netiekiama | — |
| `pak_tiekimo_busena` | `"Tiekiama"` | — | — | Tiekiama | — |
| `pak_tiekimo_busena` | `"Nepradėtas tiekti"` | — | — | Nepradėtas tiekti | — |
| `pak_recepto_poreikis` | `"Receptinis"` | — | — | Receptinis | — |
| `pak_recepto_poreikis` | `"Nereceptinis"` | — | — | Nereceptinis | — |
| `pak_recepto_poreikis` | `"Nenurodytas"` | — | — | Nenurodytas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `veiklioji_medz_lt` | `update(property: "veiklioji_medz_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `farmacine_forma_lt` | `update(property: "farmacine_forma_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkt/vaistiniai_preparatai.csv
