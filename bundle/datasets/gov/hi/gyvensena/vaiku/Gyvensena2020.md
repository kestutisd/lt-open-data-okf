---
type: Table
title: "Gyvensena2020 — Vaikų gyvensenos 2020 metų duomenys"
description: "Spinta table datasets/gov/hi/gyvensena/vaiku/Gyvensena2020 (43 columns)."
resource: "https://get.data.gov.lt/datasets/gov/hi/gyvensena/vaiku/Gyvensena2020"
tags: [gov, hi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/hi/gyvensena/vaiku.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/gyvensena/vaiku.csv#L236"
    last_modified: "2026-11-11T14:39:20Z"
---

# Gyvensena2020 — Vaikų gyvensenos 2020 metų duomenys

- **Model:** `datasets/gov/hi/gyvensena/vaiku/Gyvensena2020`[^manifest]
- **Dataset:** [Vaikų gyvensenos duomenys](../vaiku.md) (`datasets/gov/hi/gyvensena/vaiku`)
- **Manifest CSV:** [datasets/gov/hi/gyvensena/vaiku.csv#L236](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/gyvensena/vaiku.csv#L236)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/gyvensena/vaiku/Gyvensena2020`
- **Primary Key (`ref`):** `resp_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `resp_kodas` | `string` | — | `4` | `open` | — | Respondento kodas | — |
| `fizine_veikla_su_pamokomis` | `string` | — | `4` | `open` | — | Fizinis aktyvumas – tai fizinė veikla, kai tu judi, mankštiniesi ar sportuoji, kai reikia didesnių nei įprasta pastangų, pagreitėja kvėpavimas ir pulsas, pvz., greitai eini, bėgioji, važiuoji dviračiu, riedučiais, žaidi aktyvius sporto žaidimus arba kitaip sportuoji, dirbi ūkio darbus ir panašiai (vienos tokios fizinio aktyvumo veiklos trukmė – ne mažiau 10 minučių). Kiek dienų per savaitę taip judi bent 60 min.? Skaičiuok kartu su fizinio ugdymo pamokomis | — |
| `fizine_veikla_be_pamoku` | `string` | — | `4` | `open` | — | Ar dažnai ne pamokų metu, laisvalaikiu taip mankštiniesi ir sportuoji bent 60 min.? | — |
| `ekranai_dd` | `string` | — | `4` | `open` | — | Kiek vidutiniškai laiko per dieną praleidi prie ekranų – televizoriaus, kompiuterio, planšetės, išmaniojo telefono ir pan.? Darbo dienomis. | — |
| `ekranai_savaitgaliai` | `string` | — | `4` | `open` | — | Kiek vidutiniškai laiko per dieną praleidi prie ekranų – televizoriaus, kompiuterio, planšetės, išmaniojo telefono ir pan.? Savaitgaliais | — |
| `vaisiai` | `string` | — | `4` | `open` | — | Kaip dažnai vartoji šiuos maisto produktus (vaisius (neskaitant sulčių))? | — |
| `darzoves` | `string` | — | `4` | `open` | — | Kaip dažnai vartoji šiuos maisto produktus (daržoves (neskaitant bulvių))? | — |
| `saldumynai` | `string` | — | `4` | `open` | — | Kaip dažnai vartoji šiuos maisto produktus (saldumynus (saldainius, saldžius kepinius, ledus ir kt.))? | — |
| `gazuoti_gerimai` | `string` | — | `4` | `open` | — | Kaip dažnai vartoji šiuos maisto produktus (gazuotus saldžius gėrimus)? | — |
| `energiniai_gerimai` | `string` | — | `4` | `open` | — | Kaip dažnai vartoji šiuos maisto produktus (energinius gėrimus)? | — |
| `pusryciai_dd` | `string` | — | `4` | `open` | — | Kiek vidutiniškai dienų per savaitę pusryčiauji (ne tik išgeri arbatos, sulčių ar kita)? Darbo dienomis | — |
| `pusryciai_savaitgaliai` | `string` | — | `4` | `open` | — | Kiek vidutiniškai dienų per savaitę pusryčiauji (ne tik išgeri arbatos, sulčių ar kita)? Savaitgaliais | — |
| `druska` | `string` | — | `4` | `open` | — | Ar papildomai dedi druskos į paruoštą maistą? | — |
| `men_tabakas` | `string` | — | `4` | `open` | — | Ar esi bent kartą rūkęs (-iusi) tabako gaminius per paskutines 30 dienų? | — |
| `metai_tabakas` | `string` | — | `4` | `open` | — | Ar esi bent kartą rūkęs (-iusi) tabako gaminius per paskutinius 12 mėnesių? | — |
| `men_elektronines_cigaretes` | `string` | — | `4` | `open` | — | Ar esi bent kartą rūkęs (-iusi) elektronines cigaretes ar naudojęs (-usi) panašius elektroninius įtaisus rūkymui (pvz., IQOS) per paskutines 30 dienų? | — |
| `metai_elektronines_cigaretes` | `string` | — | `4` | `open` | — | Ar esi bent kartą rūkęs (-iusi) elektronines cigaretes ar naudojęs (-usi) panašius elektroninius įtaisus rūkymui (pvz., IQOS) per paskutinius 12 mėnesių? | — |
| `men_alkoholis` | `string` | — | `4` | `open` | — | Ar bent kartą vartojai kokį nors alkoholinį gėrimą per paskutines 30 dienų? | — |
| `metai_alkoholis` | `string` | — | `4` | `open` | — | Ar bent kartą vartojai kokį nors alkoholinį gėrimą per paskutinius 12 mėnesių? | — |
| `men_apsvaigimas` | `string` | — | `4` | `open` | — | Ar bent kartą buvai išgėręs (-usi) tiek daug alkoholinių gėrimų, kad pasijutai apsvaigęs (-usi) per paskutines 30 dienų? | — |
| `metai_apsvaigimas` | `string` | — | `4` | `open` | — | Ar bent kartą buvai išgėręs (-usi) tiek daug alkoholinių gėrimų, kad pasijutai apsvaigęs (-usi) per paskutinius 12 mėnesių? | — |
| `men_kanapes` | `string` | — | `4` | `open` | — | Ar bent kartą vartojai kanapes („žolę“, marihuaną, hašišą) per paskutines 30 dienų? | — |
| `metai_kanapes` | `string` | — | `4` | `open` | — | Ar bent kartą vartojai kanapes („žolę“, marihuaną, hašišą) per paskutinius 12 mėnesių? | — |
| `gyvenimas_kanapes` | `string` | — | `4` | `open` | — | Ar bent kartą vartojai kanapes („žolę“, marihuaną, hašišą) per tavo gyvenimą? | — |
| `men_kiti_narkotikai` | `string` | — | `4` | `open` | — | Ar bent kartą vartojai kitus narkotikus nei kanapes per paskutinius 30 dienų? | — |
| `metai_kiti_narkotikai` | `string` | — | `4` | `open` | — | Ar bent kartą vartojai kitus narkotikus nei kanapes per paskutinius 12 mėnesių? | — |
| `gyvenimas_kiti_narkotikai` | `string` | — | `4` | `open` | — | Ar bent kartą vartojai kitus narkotikus nei kanapes per tavo gyvenimą? | — |
| `patirtos_patycios` | `string` | — | `4` | `open` | — | Kaip dažnai iš Tavęs tyčiojosi kiti mokiniai mokykloje per pastaruosius du mėnesius? | — |
| `patycios_is_kitu` | `string` | — | `4` | `open` | — | Kaip dažnai Tu pats (-ti) tyčiojaisi iš kitų mokinių mokykloje per pastaruosius du mėnesius? | — |
| `men_internetines_patycios` | `string` | — | `4` | `open` | — | Ar patyrei patyčias per socialinius tinklus, elektroniniu paštu ar telefonu per paskutines 30 dienų? | — |
| `metai_internetines_patycios` | `string` | — | `4` | `open` | — | Ar patyrei patyčias per socialinius tinklus, elektroniniu paštu ar telefonu per paskutinius 12 mėnesių? | — |
| `fizines_bausmes` | `string` | — | `4` | `open` | — | Kaip dažnai Tave per pastaruosius du mėnesius mušė ar kitaip fiziškai baudė tėvai? | — |
| `dantys` | `string` | — | `4` | `open` | — | Kaip dažnai valaisi dantis šepetėliu ir pasta? | — |
| `atsvaitai` | `string` | — | `4` | `open` | — | Ar būdamas (-a) lauke tamsiu paros metu nešioji atšvaitą (-us)? | — |
| `saugos_dirzai` | `string` | — | `4` | `open` | — | Ar segi saugos diržą važiuodamas (-a) automobiliu? | — |
| `salmai` | `string` | — | `4` | `open` | — | Ar važiuodamas (-a) dviračiu dėvi šalmą? | — |
| `laimingmas` | `string` | — | `4` | `open` | — | Kaip jautiesi galvodamas (-a) apie savo dabartinį gyvenimą? | — |
| `saugumas_mokykloje` | `string` | — | `4` | `open` | — | Ar jautiesi saugus (-i) mokyklos aplinkoje? | — |
| `saugumas_namuose` | `string` | — | `4` | `open` | — | Ar jautiesi saugus (-i) namų aplinkoje? | — |
| `saugumas_kitur` | `string` | — | `4` | `open` | — | Ar jautiesi saugus (-i) kitur? | — |
| `sveikata` | `string` | — | `4` | `open` | — | Kaip apibūdintum savo sveikatą? | — |
| `isvaizda` | `string` | — | `4` | `open` | — | Kaip vertini savo kūną? Pažymėk teiginį, kuris labiausiai atitinka Tavo požiūrį. | — |
| `pasitenkinimas_santykiais_seimoje` | `integer` | `U` | `4` | `open` | — | Kiek esi patenkintas (-a) santykiais šeimoje? Pažymėk tą langelį, kuris atspindi Tavo jausmus. | Juos gali vertinti nuo 0 (visai nepatenkintas) iki 10 (labai patenkintas). Reikšmė 999 - neatsakyta į klausimą |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `fizine_veikla_su_pamokomis` | `'1'` | — | — | nei vienos dienos | — |
| `fizine_veikla_su_pamokomis` | `'2'` | — | — | 1 dieną | — |
| `fizine_veikla_su_pamokomis` | `'3'` | — | — | 2 dienas | — |
| `fizine_veikla_su_pamokomis` | `'4'` | — | — | 3 dienas | — |
| `fizine_veikla_su_pamokomis` | `'5'` | — | — | 4 dienas | — |
| `fizine_veikla_su_pamokomis` | `'6'` | — | — | 5 ir daugiau dienų | — |
| `fizine_veikla_su_pamokomis` | `'9'` | — | — | neatsakyta į klausimą | — |
| `fizine_veikla_be_pamoku` | `'1'` | — | — | niekada | — |
| `fizine_veikla_be_pamoku` | `'2'` | — | — | rečiau nei kartą per mėnesį | — |
| `fizine_veikla_be_pamoku` | `'3'` | — | — | kartą per mėnesį | — |
| `fizine_veikla_be_pamoku` | `'4'` | — | — | kartą per savaitę | — |
| `fizine_veikla_be_pamoku` | `'5'` | — | — | 2-3 kartus per savaitę | — |
| `fizine_veikla_be_pamoku` | `'6'` | — | — | 4-6 kartus per savaitę | — |
| `fizine_veikla_be_pamoku` | `'7'` | — | — | kasdien | — |
| `fizine_veikla_be_pamoku` | `'9'` | — | — | neatsakyta į klausimą | — |
| `ekranai_dd` | `'1'` | — | — | visai to nedarau | — |
| `ekranai_dd` | `'2'` | — | — | apie pusę valandos per dieną | — |
| `ekranai_dd` | `'3'` | — | — | apie 1 valandą per dieną | — |
| `ekranai_dd` | `'4'` | — | — | apie 2 valandas per dieną | — |
| `ekranai_dd` | `'5'` | — | — | apie 3 valandas per dieną | — |
| `ekranai_dd` | `'6'` | — | — | apie 4 ir daugiau val. per dieną | — |
| `ekranai_dd` | `'9'` | — | — | neatsakyta į klausimą | — |
| `ekranai_savaitgaliai` | `'1'` | — | — | visai to nedarau | — |
| `ekranai_savaitgaliai` | `'2'` | — | — | apie pusę valandos per dieną | — |
| `ekranai_savaitgaliai` | `'3'` | — | — | apie 1 valandą per dieną | — |
| `ekranai_savaitgaliai` | `'4'` | — | — | apie 2 valandas per dieną | — |
| `ekranai_savaitgaliai` | `'5'` | — | — | apie 3 valandas per dieną | — |
| `ekranai_savaitgaliai` | `'6'` | — | — | apie 4 ir daugiau val. per dieną | — |
| `ekranai_savaitgaliai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `vaisiai` | `'1'` | — | — | niekada | — |
| `vaisiai` | `'2'` | — | — | rečiau nei kartą per savaitę | — |
| `vaisiai` | `'3'` | — | — | kartą per savaitę | — |
| `vaisiai` | `'4'` | — | — | 2-4 dienas per savaitę | — |
| `vaisiai` | `'5'` | — | — | 5-6 dienas per savaitę | — |
| `vaisiai` | `'6'` | — | — | kasdien, kartą per dieną | — |
| `vaisiai` | `'7'` | — | — | kasdien, kelis kartus per dieną | — |
| `vaisiai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `darzoves` | `'1'` | — | — | niekada | — |
| `darzoves` | `'2'` | — | — | rečiau nei kartą per savaitę | — |
| `darzoves` | `'3'` | — | — | kartą per savaitę | — |
| `darzoves` | `'4'` | — | — | 2-4 dienas per savaitę | — |
| `darzoves` | `'5'` | — | — | 5-6 dienas per savaitę | — |
| `darzoves` | `'6'` | — | — | kasdien, kartą per dieną | — |
| `darzoves` | `'7'` | — | — | kasdien, kelis kartus per dieną | — |
| `darzoves` | `'9'` | — | — | neatsakyta į klausimą | — |
| `saldumynai` | `'1'` | — | — | niekada | — |
| `saldumynai` | `'2'` | — | — | rečiau nei kartą per savaitę | — |
| `saldumynai` | `'3'` | — | — | kartą per savaitę | — |
| `saldumynai` | `'4'` | — | — | 2-4 dienas per savaitę | — |
| `saldumynai` | `'5'` | — | — | 5-6 dienas per savaitę | — |
| `saldumynai` | `'6'` | — | — | kasdien, kartą per dieną | — |
| `saldumynai` | `'7'` | — | — | kasdien, kelis kartus per dieną | — |
| `saldumynai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `gazuoti_gerimai` | `'1'` | — | — | niekada | — |
| `gazuoti_gerimai` | `'2'` | — | — | rečiau nei kartą per savaitę | — |
| `gazuoti_gerimai` | `'3'` | — | — | kartą per savaitę | — |
| `gazuoti_gerimai` | `'4'` | — | — | 2-4 dienas per savaitę | — |
| `gazuoti_gerimai` | `'5'` | — | — | 5-6 dienas per savaitę | — |
| `gazuoti_gerimai` | `'6'` | — | — | kasdien, kartą per dieną | — |
| `gazuoti_gerimai` | `'7'` | — | — | kasdien, kelis kartus per dieną | — |
| `gazuoti_gerimai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `energiniai_gerimai` | `'1'` | — | — | niekada | — |
| `energiniai_gerimai` | `'2'` | — | — | rečiau nei kartą per savaitę | — |
| `energiniai_gerimai` | `'3'` | — | — | kartą per savaitę | — |
| `energiniai_gerimai` | `'4'` | — | — | 2-4 dienas per savaitę | — |
| `energiniai_gerimai` | `'5'` | — | — | 5-6 dienas per savaitę | — |
| `energiniai_gerimai` | `'6'` | — | — | kasdien, kartą per dieną | — |
| `energiniai_gerimai` | `'7'` | — | — | kasdien, kelis kartus per dieną | — |
| `energiniai_gerimai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `pusryciai_dd` | `'1'` | — | — | niekada nepusryčiauju | — |
| `pusryciai_dd` | `'2'` | — | — | vieną dieną | — |
| `pusryciai_dd` | `'3'` | — | — | dvi dienas | — |
| `pusryciai_dd` | `'4'` | — | — | tris dienas | — |
| `pusryciai_dd` | `'5'` | — | — | keturias dienas | — |
| `pusryciai_dd` | `'6'` | — | — | penkias dienas | — |
| `pusryciai_dd` | `'9'` | — | — | neatsakyta į klausimą | — |
| `pusryciai_savaitgaliai` | `'1'` | — | — | nepusryčiauju savaitgaliais | — |
| `pusryciai_savaitgaliai` | `'2'` | — | — | pusryčiauju vieną dieną | — |
| `pusryciai_savaitgaliai` | `'3'` | — | — | pusryčiauju abi dienas | — |
| `pusryciai_savaitgaliai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `druska` | `'1'` | — | — | nededu | — |
| `druska` | `'2'` | — | — | taip, jei, mano nuomone, trūksta | — |
| `druska` | `'3'` | — | — | taip, beveik visada, neragavus | — |
| `druska` | `'9'` | — | — | neatsakyta į klausimą | — |
| `men_tabakas` | `'1'` | — | — | taip | — |
| `men_tabakas` | `'2'` | — | — | ne | — |
| `men_tabakas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `metai_tabakas` | `'1'` | — | — | taip | — |
| `metai_tabakas` | `'2'` | — | — | ne | — |
| `metai_tabakas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `men_elektronines_cigaretes` | `'1'` | — | — | taip | — |
| `men_elektronines_cigaretes` | `'2'` | — | — | ne | — |
| `men_elektronines_cigaretes` | `'9'` | — | — | neatsakyta į klausimą | — |
| `metai_elektronines_cigaretes` | `'1'` | — | — | taip | — |
| `metai_elektronines_cigaretes` | `'2'` | — | — | ne | — |
| `metai_elektronines_cigaretes` | `'9'` | — | — | neatsakyta į klausimą | — |
| `men_alkoholis` | `'1'` | — | — | taip | — |
| `men_alkoholis` | `'2'` | — | — | ne | — |
| `men_alkoholis` | `'9'` | — | — | neatsakyta į klausimą | — |
| `metai_alkoholis` | `'1'` | — | — | taip | — |
| `metai_alkoholis` | `'2'` | — | — | ne | — |
| `metai_alkoholis` | `'9'` | — | — | neatsakyta į klausimą | — |
| `men_apsvaigimas` | `'1'` | — | — | taip | — |
| `men_apsvaigimas` | `'2'` | — | — | ne | — |
| `men_apsvaigimas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `metai_apsvaigimas` | `'1'` | — | — | taip | — |
| `metai_apsvaigimas` | `'2'` | — | — | ne | — |
| `metai_apsvaigimas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `men_kanapes` | `'1'` | — | — | taip | — |
| `men_kanapes` | `'2'` | — | — | ne | — |
| `men_kanapes` | `'9'` | — | — | neatsakyta į klausimą | — |
| `metai_kanapes` | `'1'` | — | — | taip | — |
| `metai_kanapes` | `'2'` | — | — | ne | — |
| `metai_kanapes` | `'9'` | — | — | neatsakyta į klausimą | — |
| `gyvenimas_kanapes` | `'1'` | — | — | taip | — |
| `gyvenimas_kanapes` | `'2'` | — | — | ne | — |
| `gyvenimas_kanapes` | `'9'` | — | — | neatsakyta į klausimą | — |
| `men_kiti_narkotikai` | `'1'` | — | — | taip | — |
| `men_kiti_narkotikai` | `'2'` | — | — | ne | — |
| `men_kiti_narkotikai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `metai_kiti_narkotikai` | `'1'` | — | — | taip | — |
| `metai_kiti_narkotikai` | `'2'` | — | — | ne | — |
| `metai_kiti_narkotikai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `gyvenimas_kiti_narkotikai` | `'1'` | — | — | taip | — |
| `gyvenimas_kiti_narkotikai` | `'2'` | — | — | ne | — |
| `gyvenimas_kiti_narkotikai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `patirtos_patycios` | `'1'` | — | — | nepatyriau patyčių | — |
| `patirtos_patycios` | `'2'` | — | — | kartą arba du kartus | — |
| `patirtos_patycios` | `'3'` | — | — | 2 ar 3 kartus per mėnesį | — |
| `patirtos_patycios` | `'4'` | — | — | maždaug kartą per savaitę | — |
| `patirtos_patycios` | `'5'` | — | — | keletą kartų per savaitę | — |
| `patirtos_patycios` | `'9'` | — | — | neatsakyta į klausimą | — |
| `patycios_is_kitu` | `'1'` | — | — | nesityčiojau iš kitų | — |
| `patycios_is_kitu` | `'2'` | — | — | kartą arba du kartus | — |
| `patycios_is_kitu` | `'3'` | — | — | 2 ar 3 kartus per mėnesį | — |
| `patycios_is_kitu` | `'4'` | — | — | maždaug kartą per savaitę | — |
| `patycios_is_kitu` | `'5'` | — | — | keletą kartų per savaitę | — |
| `patycios_is_kitu` | `'9'` | — | — | neatsakyta į klausimą | — |
| `men_internetines_patycios` | `'1'` | — | — | taip | — |
| `men_internetines_patycios` | `'2'` | — | — | ne | — |
| `men_internetines_patycios` | `'9'` | — | — | neatsakyta į klausimą | — |
| `metai_internetines_patycios` | `'1'` | — | — | taip | — |
| `metai_internetines_patycios` | `'2'` | — | — | ne | — |
| `metai_internetines_patycios` | `'9'` | — | — | neatsakyta į klausimą | — |
| `fizines_bausmes` | `'1'` | — | — | niekada | — |
| `fizines_bausmes` | `'2'` | — | — | kartą ar du kartus | — |
| `fizines_bausmes` | `'3'` | — | — | 2 ar 3 kartus per mėnesį | — |
| `fizines_bausmes` | `'4'` | — | — | maždaug kartą per savaitę | — |
| `fizines_bausmes` | `'5'` | — | — | keletą kartų per savaitę | — |
| `fizines_bausmes` | `'9'` | — | — | neatsakyta į klausimą | — |
| `dantys` | `'1'` | — | — | niekada | — |
| `dantys` | `'2'` | — | — | nors kartą per sav., ne kasdien | — |
| `dantys` | `'3'` | — | — | vieną kartą per dieną | — |
| `dantys` | `'4'` | — | — | 2 ir daugiau kartų per dieną | — |
| `dantys` | `'9'` | — | — | neatsakyta į klausimą | — |
| `atsvaitai` | `'1'` | — | — | visada | — |
| `atsvaitai` | `'2'` | — | — | kartais | — |
| `atsvaitai` | `'3'` | — | — | ne | — |
| `atsvaitai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `saugos_dirzai` | `'1'` | — | — | visada | — |
| `saugos_dirzai` | `'2'` | — | — | kartais | — |
| `saugos_dirzai` | `'3'` | — | — | ne | — |
| `saugos_dirzai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `salmai` | `'1'` | — | — | visada | — |
| `salmai` | `'2'` | — | — | kartais | — |
| `salmai` | `'3'` | — | — | ne | — |
| `salmai` | `'4'` | — | — | nevažinėju dviračiu | — |
| `salmai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `laimingmas` | `'1'` | — | — | labai laimingas (-a) | — |
| `laimingmas` | `'2'` | — | — | pakankamai laimingas (-a) | — |
| `laimingmas` | `'3'` | — | — | nei laimingas, nei nelaimingas | — |
| `laimingmas` | `'4'` | — | — | nelaimingas(-a) | — |
| `laimingmas` | `'5'` | — | — | labai nelaimingas (-a) | — |
| `laimingmas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `saugumas_mokykloje` | `'1'` | — | — | taip | — |
| `saugumas_mokykloje` | `'2'` | — | — | ne | — |
| `saugumas_mokykloje` | `'9'` | — | — | neatsakyta į klausimą | — |
| `saugumas_namuose` | `'1'` | — | — | taip | — |
| `saugumas_namuose` | `'2'` | — | — | ne | — |
| `saugumas_namuose` | `'9'` | — | — | neatsakyta į klausimą | — |
| `saugumas_kitur` | `'1'` | — | — | taip | — |
| `saugumas_kitur` | `'2'` | — | — | ne | — |
| `saugumas_kitur` | `'9'` | — | — | neatsakyta į klausimą | — |
| `sveikata` | `'1'` | — | — | labai gera | — |
| `sveikata` | `'2'` | — | — | gera | — |
| `sveikata` | `'3'` | — | — | nei gera, nei bloga | — |
| `sveikata` | `'4'` | — | — | patenkinama | — |
| `sveikata` | `'5'` | — | — | bloga | — |
| `sveikata` | `'9'` | — | — | neatsakyta į klausimą | — |
| `isvaizda` | `'1'` | — | — | esu patenkintas (-a) išvaizda | — |
| `isvaizda` | `'2'` | — | — | patinka išvaizda, nepaisant kai kurių trūkumų | — |
| `isvaizda` | `'3'` | — | — | esu nusivylęs (-usi) išvaizda | — |
| `isvaizda` | `'4'` | — | — | jaučiu pyktį savo kūnui | — |
| `isvaizda` | `'5'` | — | — | nekenčiu savo kūno | — |
| `isvaizda` | `'9'` | — | — | neatsakyta į klausimą | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/gyvensena/vaiku.csv
