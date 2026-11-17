---
type: Table
title: "Pacientas — Traumas ir apsinuodijimus patyrusių pacientų duomenys"
description: "Duomenys iš Higienos instituto apie traumas arba apsinuodijimus patyrusius pacientus."
resource: "https://get.data.gov.lt/datasets/gov/hi/traumos_apsinuodijimai/Pacientas"
tags: [gov, hi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/hi/traumos_apsinuodijimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/traumos_apsinuodijimai.csv#L13"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pacientas — Traumas ir apsinuodijimus patyrusių pacientų duomenys

Duomenys iš Higienos instituto apie traumas arba apsinuodijimus patyrusius pacientus. Vieną eilutę sudaro informacija apie paciento traumą / apsinuodijimą. Eilutėje pateikiama informacija apie pacientą: lytis, gimimo metai, savivaldybė, kurioje registruotas paciento gyvenamasis adresas, ir gyvenvietės tipas. Taip pat pateikiama pagrindinė su trauma susijusi informacija: gydymo lapo pradžios data, gydymo tipas (jei gydymas stacionarinis, nurodomas ir stacionaro tipas) ir traumą / apsinuodijimą apibūdinantys TLK-10-AM kodai, nurodantys traumos pavadinimą, aplinkybes, veiklą (įvykstant traumai) ir įvykio vietą.

- **Model:** `datasets/gov/hi/traumos_apsinuodijimai/Pacientas`[^manifest]
- **Dataset:** [Stacionaro ir ambulatoriniai ligoniai, gydyti nuo traumų ir apsinuodijimų](../traumos_apsinuodijimai.md) (`datasets/gov/hi/traumos_apsinuodijimai`)
- **Manifest CSV:** [datasets/gov/hi/traumos_apsinuodijimai.csv#L13](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/traumos_apsinuodijimai.csv#L13)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/traumos_apsinuodijimai/Pacientas`
- **Primary Key (`ref`):** `vda_pk`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_pk` | `string` | — | `4` | `open` | — | VDA PK | Valstybės Duomenų Agentūros įrašo identifikatorius (pirminis raktas) |
| `paciento_id` | `string` | — | `4` | `open` | — | Paciento ID | Paciento identifikacinis numeris iš vidinės informacinės sistemos |
| `atvejo_id` | `string` | — | `4` | `open` | — | Atvejo ID | Gydymo lapo (klinikinio atvejo) identifikacinis numeris |
| `gyd_lap_pradzia` | `date` | `M` | `4` | `open` | — | Gydymo lapo pradžia | Data, mėnesio tikslumu, kada gydymo lapas buvo užregistruotas |
| `lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `vda_gim_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | Paciento gimimo metai, metų tikslumu. Apskaičiuoti atimant paciento amžių, apsilankymo gydymo įstaigoje metu, iš gydymo lapo užregistravimo laiko žymos. Paciento, kuris lankėsi kelis kartus gydymo įstaigoje, skaičiuojama jo gimimo metų mediana iš visų apsilankymų. Apie 20% pacientų gimimo metų įrašų yra modifikuoti pridedant atsitiktines vertes – triukšmą. |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė | Savivaldybės pavadinimas, kurioje pacientas registravęs savo gyvenamąją vietą |
| `gyvenviete` | `string` | — | `4` | `open` | — | Gyvenvietė | Paciento gyvenvietės tipas |
| `gydymas` | `string` | — | `4` | `open` | — | Gydymo tipas | Kokio tipo gydymas taikomas pacientui |
| `stacionaro_tipas` | `string` | — | `4` | `open` | — | Stacionaro tipas | — |
| `tlk_trauma` | `string` | — | `4` | `open` | — | Traumos kodas | Traumų ir apsinuodijimų kodas pagal TLK-10-AM (S00-T98), nusakantis klinikinę traumą (sužalojimai, apsinuodijimai ir tam tikri išorinių poveikių padariniai) |
| `tlk_aplinkybe` | `string` | — | `4` | `open` | — | Traumos aplinkybės kodas | Traumų ir apsinuodijimų kodas pagal TLK-10-AM kodus (V00-Y89), nusakantis traumos pobūdį/ketinimą |
| `tlk_veikla` | `string` | — | `4` | `open` | — | Traumos veiklos kodas | Traumos ir apsinuodijimo veiklos kodas pagal TLK-10-AM (U50-U73) |
| `tlk_vieta` | `string` | — | `4` | `open` | — | Traumos vietovės kodas | Traumos ir apsinuodijimo vietos kodas pagal TLK-10-AM (Y92) |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Vyras"` | — | — | Vyras | — |
| `lytis` | `"Moteris"` | — | — | Moteris | — |
| `lytis` | `"Nežinoma"` | — | — | Nežinoma | — |
| `gyvenviete` | `"Miestas"` | — | — | Mietas | — |
| `gyvenviete` | `"Kaimas"` | — | — | Kaimas | — |
| `gyvenviete` | `"Nežinoma"` | — | — | Nežinoma | — |
| `gydymas` | `"Ambulatorinis"` | — | — | Ambulatorinis | — |
| `gydymas` | `"Stacionarinis"` | — | — | Stacionarinis | — |
| `stacionaro_tipas` | `"A"` | — | — | Aktyvus | Paslaugos, teikiamos pacientams dėl ūmios ligos, lėtinės ligos paūmėjimo ar sužalojimo. Teikiant šias paslaugas reikalingas ištyrimas ir (ar) aktyvus medikamentinis, ir (ar) chirurginis gydymas, kuris negali būti taikomas ambulatorinėmis sąlygomis. |
| `stacionaro_tipas` | `"I"` | — | — | Ilgalaikis | Paslaugos, teikiamos lėtinėmis ligomis sergantiems pacientams, kai reikalingas ilgai (dažniausiai ilgiau nei mėnesį) trunkantis gydymas ir (ar) slauga. Šioms paslaugoms priskiriamos slaugos ir palaikomojo gydymo, tuberkuliozės, specialiosios psichiatrijos, psichikos ligų ilgalaikio gydymo paslaugos ir pan. |
| `stacionaro_tipas` | `"R"` | — | — | Reabilitacinis | Reabilitacijos priemonių (fizioterapijos, kineziterapijos, ergoterapijos, ortopedinių ir techninės pagalbos priemonių, psichologinės pagalbos, gydymo vaistais, pacientų ir jų artimųjų mokymo, gydymo dieta ir kt.) taikymas siekiant kuo daugiau sugrąžinti sutrikusias funkcijas arba, esant negrįžtamiems pakitimams, jas kompensuoti, arba palaikyti pasiektą funkcinio pajėgumo lygį. Susirgimai ir būklės, kada reabilitacijos paslaugos gali būti teikiamos stacionare, yra patvirtintos Sveikatos apsaugos ministro įsakymu. |
| `stacionaro_tipas` | `"T"` | — | — | Transplantacinis | Paslaugos, kurias teikiant iš vieno asmens paimti audiniai, ląstelės ir (ar) organai persodinami kitam arba tam pačiam asmeniui gydymo tikslu. Yra atliekamos inkstų, širdies, kepenų, plaučių, širdies ir plaučių komplekso, kasos ir inksto komplekso, ragenos, kaulų čiulpų transplantacijos. |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/traumos_apsinuodijimai.csv
