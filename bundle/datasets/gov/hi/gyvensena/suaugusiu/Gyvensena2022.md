---
type: Table
title: "Gyvensena2022 — Suaugusiųjų gyvensenos tyrimo 2022 metų duomenys"
description: "Klausimynas skelbiamas internete: https://www.hi.lt/uploads/Visuomenes_sveikatos_technologiju_centras/Suaugusiu_gyventoju_gyvensenos_stebesenos_tyrimo_klausimynas.pdf"
resource: "https://get.data.gov.lt/datasets/gov/hi/gyvensena/suaugusiu/Gyvensena2022"
tags: [gov, hi, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/hi/gyvensena/suaugusiu.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/gyvensena/suaugusiu.csv#L587"
    last_modified: "2026-11-11T14:39:20Z"
---

# Gyvensena2022 — Suaugusiųjų gyvensenos tyrimo 2022 metų duomenys

Klausimynas skelbiamas internete: https://www.hi.lt/uploads/Visuomenes_sveikatos_technologiju_centras/Suaugusiu_gyventoju_gyvensenos_stebesenos_tyrimo_klausimynas.pdf

- **Model:** `datasets/gov/hi/gyvensena/suaugusiu/Gyvensena2022`[^manifest]
- **Dataset:** [Suaugusiųjų gyvensenos duomenys](../suaugusiu.md) (`datasets/gov/hi/gyvensena/suaugusiu`)
- **Manifest CSV:** [datasets/gov/hi/gyvensena/suaugusiu.csv#L587](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/gyvensena/suaugusiu.csv#L587)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/gyvensena/suaugusiu/Gyvensena2022`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `resp_kodas` | `string` | — | `4` | `open` | — | Respondento kodas | — |
| `vaisiai` | `string` | — | `4` | `open` | — | 1. Kaip dažnai vartojate šiuos maisto produktus? Vaisius (neskaitant sulčių) | — |
| `darzoves` | `string` | — | `4` | `open` | — | 1. Kaip dažnai vartojate šiuos maisto produktus? Daržoves (neskaitant bulvių) | — |
| `saldumynai` | `string` | — | `4` | `open` | — | 1. Kaip dažnai vartojate šiuos maisto produktus? Saldumynus (saldainius, saldžius kepinius, ledus ir kt.) | — |
| `gazuoti_gerimai` | `string` | — | `4` | `open` | — | 1. Kaip dažnai vartojate šiuos maisto produktus? Gazuotus saldžius gėrimus | — |
| `energiniai_gerimai` | `string` | — | `4` | `open` | — | 1. Kaip dažnai vartojate šiuos maisto produktus? Energinius gėrimus | — |
| `druska` | `string` | — | `4` | `open` | — | 2. Ar papildomai dedate druskos į paruoštą maistą? | — |
| `men_tabakas` | `string` | — | `4` | `open` | — | 3. Ar vartojote tabako gaminius per paskutines 30 dienų? | — |
| `metai_tabakas` | `string` | — | `4` | `open` | — | 3. Ar vartojote tabako gaminius per paskutinius 12 mėnesių? | — |
| `cigareciu_per_diena` | `string` | — | `4` | `open` | — | 4. Kiek vidutiniškai cigarečių surūkote per dieną? | -9 - neatsakyta į klausimą |
| `men_elektronines_cigaretes` | `string` | — | `4` | `open` | — | 5. Ar rūkėte elektronines cigaretes arba naudojote panašius elektroninius įtaisus rūkymui (pvz.,IQOS) per paskutines 30 dienų? | — |
| `metai_elektronines_cigaretes` | `string` | — | `4` | `open` | — | 5. Ar rūkėte elektronines cigaretes arba naudojote panašius elektroninius įtaisus rūkymui (pvz.,IQOS) per paskutinius 12 mėnesių? | — |
| `rukymo_metai` | `string` | — | `4` | `open` | — | 6. Kiek metų rūkote? | -9 - neatsakyta į klausimą |
| `men_alkoholis` | `string` | — | `4` | `open` | — | 7. Ar vartojote alkoholinius gėrimus per paskutines 30 dienų? | — |
| `metai_alkoholis` | `string` | — | `4` | `open` | — | 7. Ar vartojote alkoholinius gėrimus per paskutinius 12 mėnesių? | — |
| `men_narkotikai` | `string` | — | `4` | `open` | — | 8. Ar bent kartą vartojote narkotinių ar psichotropinių medžiagų (narkotikų) be gydytojo paskyrimo? Per paskutines 30 dienų? | — |
| `metai_narkotikai` | `string` | — | `4` | `open` | — | 8. Ar bent kartą vartojote narkotinių ar psichotropinių medžiagų (narkotikų) be gydytojo paskyrimo? Per paskutinius 12 mėnesių | — |
| `gyvenimas_narkotikai` | `string` | — | `4` | `open` | — | 8. Ar bent kartą vartojote narkotinių ar psichotropinių medžiagų (narkotikų) be gydytojo paskyrimo? Per savo gyvenimą | — |
| `fizine_veikla` | `string` | — | `4` | `open` | — | 9. Kiek dienų per savaitę mažiausiai 30 min. užsiimate energinga fizine veikla, kai reikia didesnių nei įprasta pastangų, pagreitėja kvėpavimas ir pulsas, pvz., aktyviai mankštinatės, sportuojate, bėgiojate, greitai einate, važiuojate dviračiu, energingai dirbate namų ūkio darbus ir pan. ? (30 min. trukmė vienos paros metu gali susidėti iš kelių dalių, ne trumpesnių nei 10 min., pvz., 10+10+10 min., 15+15 min., 10+20 min.). | — |
| `atsvaitai` | `string` | — | `4` | `open` | — | 10. Ar būdamas (-a) lauke tamsiu paros metu nešiojate atšvaitą (-us)? | — |
| `saugos_dirzai` | `string` | — | `4` | `open` | — | 11. Ar segite saugos diržą važiuodamas (-a) automobiliu? | — |
| `salmai` | `string` | — | `4` | `open` | — | 12. Ar važiuodamas (-a) dviračiu dėvite šalmą? | — |
| `artimi_zmones` | `string` | — | `4` | `open` | — | 13. Kiek turite artimų žmonių, kuriais galėtumėte pasitikėti susidūrus su sunkiomis asmeninėmis problemomis? | — |
| `nerimas` | `string` | — | `4` | `open` | — | 14. Ar per praėjusį mėnesį buvo apėmusi prislėgta nuotaika, nerimas? | — |
| `gyvenimo_kokybe` | `string` | — | `4` | `open` | — | 15. Kaip vertintumėte savo gyvenimo kokybę? | — |
| `sveikata` | `string` | — | `4` | `open` | — | 16. Kaip vertintumėte dabartinę savo sveikatos būklę? | — |
| `laimingumas` | `string` | — | `4` | `open` | — | 17. Ar jaučiatės laimingas (-a)? | — |
| `ilgalaike_sveikatos_problema` | `string` | — | `4` | `open` | — | 18. Ar turite ilgalaikę sveikatos problemą? | (Ilgalaike vadinama liga ar sveikatos sutrikimas, kuris trunka ar, tikėtina, kad truks mažiausiai 6 mėn.) |
| `sveikiau_maitintis` | `string` | — | `4` | `open` | — | 19. Ar per paskutinius 12 mėnesių esate bandęs (-džiusi) pakeisti gyvenseną? Sveikiau maitintis | (Gyvensena – tai mitybos, fizinio aktyvumo, alkoholio bei tabako vartojimo ir kiti įpročiai). |
| `tapti_fiziskai_aktyvesniu` | `string` | — | `4` | `open` | — | 19. Ar per paskutinius 12 mėnesių esate bandęs (-džiusi) pakeisti gyvenseną? Būti fiziškai aktyvesniam (-ei) | — |
| `maziau_rukyti` | `string` | — | `4` | `open` | — | 19. Ar per paskutinius 12 mėnesių esate bandęs (-džiusi) pakeisti gyvenseną? Mažiau rūkyti arba mesti rūkyti | — |
| `maziau_vartoti_alkoholio` | `string` | — | `4` | `open` | — | 19. Ar per paskutinius 12 mėnesių esate bandęs (-džiusi) pakeisti gyvenseną? Mažiau vartoti alkoholio arba nustoti jį vartoti | — |
| `lytis` | `string` | — | `4` | `open` | — | 20. Lytis | — |
| `gyvenamoji_vietove` | `string` | — | `4` | `open` | — | 22. Gyvenamoji vietovė | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vaisiai` | `'1'` | — | — | Niekada | — |
| `vaisiai` | `'2'` | — | — | Rečiau nei kartą per savaitę | — |
| `vaisiai` | `'3'` | — | — | Kartą per savaitę | — |
| `vaisiai` | `'4'` | — | — | 2–4 dienas per savaitę | — |
| `vaisiai` | `'5'` | — | — | 5–6 dienas per savaitę | — |
| `vaisiai` | `'6'` | — | — | Kasdien, kartą per dieną | — |
| `vaisiai` | `'7'` | — | — | Kasdien, kelis kartus per dieną | — |
| `vaisiai` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `darzoves` | `'1'` | — | — | Niekada | — |
| `darzoves` | `'2'` | — | — | Rečiau nei kartą per savaitę | — |
| `darzoves` | `'3'` | — | — | Kartą per savaitę | — |
| `darzoves` | `'4'` | — | — | 2–4 dienas per savaitę | — |
| `darzoves` | `'5'` | — | — | 5–6 dienas per savaitę | — |
| `darzoves` | `'6'` | — | — | Kasdien, kartą per dieną | — |
| `darzoves` | `'7'` | — | — | Kasdien, kelis kartus per dieną | — |
| `darzoves` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `saldumynai` | `'1'` | — | — | Niekada | — |
| `saldumynai` | `'2'` | — | — | Rečiau nei kartą per savaitę | — |
| `saldumynai` | `'3'` | — | — | Kartą per savaitę | — |
| `saldumynai` | `'4'` | — | — | 2–4 dienas per savaitę | — |
| `saldumynai` | `'5'` | — | — | 5–6 dienas per savaitę | — |
| `saldumynai` | `'6'` | — | — | Kasdien, kartą per dieną | — |
| `saldumynai` | `'7'` | — | — | Kasdien, kelis kartus per dieną | — |
| `saldumynai` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `gazuoti_gerimai` | `'1'` | — | — | Niekada | — |
| `gazuoti_gerimai` | `'2'` | — | — | Rečiau nei kartą per savaitę | — |
| `gazuoti_gerimai` | `'3'` | — | — | Kartą per savaitę | — |
| `gazuoti_gerimai` | `'4'` | — | — | 2–4 dienas per savaitę | — |
| `gazuoti_gerimai` | `'5'` | — | — | 5–6 dienas per savaitę | — |
| `gazuoti_gerimai` | `'6'` | — | — | Kasdien, kartą per dieną | — |
| `gazuoti_gerimai` | `'7'` | — | — | Kasdien, kelis kartus per dieną | — |
| `gazuoti_gerimai` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `energiniai_gerimai` | `'1'` | — | — | Niekada | — |
| `energiniai_gerimai` | `'2'` | — | — | Rečiau nei kartą per savaitę | — |
| `energiniai_gerimai` | `'3'` | — | — | Kartą per savaitę | — |
| `energiniai_gerimai` | `'4'` | — | — | 2–4 dienas per savaitę | — |
| `energiniai_gerimai` | `'5'` | — | — | 5–6 dienas per savaitę | — |
| `energiniai_gerimai` | `'6'` | — | — | Kasdien, kartą per dieną | — |
| `energiniai_gerimai` | `'7'` | — | — | Kasdien, kelis kartus per dieną | — |
| `energiniai_gerimai` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `druska` | `'1'` | — | — | Nededu | — |
| `druska` | `'2'` | — | — | Taip, jei, mano nuomone, trūksta druskos | — |
| `druska` | `'3'` | — | — | Taip, beveik visada, net neragavęs (-usi) | — |
| `druska` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `men_tabakas` | `'1'` | — | — | Ne | — |
| `men_tabakas` | `'2'` | — | — | Taip, kasdien | — |
| `men_tabakas` | `'3'` | — | — | Taip, retkarčiais | — |
| `men_tabakas` | `'4'` | — | — | Taip, bent kartą | — |
| `men_tabakas` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `metai_tabakas` | `'1'` | — | — | Ne | — |
| `metai_tabakas` | `'2'` | — | — | Taip, kasdien | — |
| `metai_tabakas` | `'3'` | — | — | Taip, retkarčiais | — |
| `metai_tabakas` | `'4'` | — | — | Taip, bent kartą | — |
| `metai_tabakas` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `men_elektronines_cigaretes` | `'1'` | — | — | Ne | — |
| `men_elektronines_cigaretes` | `'2'` | — | — | Taip, kasdien | — |
| `men_elektronines_cigaretes` | `'3'` | — | — | Taip, retkarčiais | — |
| `men_elektronines_cigaretes` | `'4'` | — | — | Taip, bent kartą | — |
| `men_elektronines_cigaretes` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `metai_elektronines_cigaretes` | `'1'` | — | — | Ne | — |
| `metai_elektronines_cigaretes` | `'2'` | — | — | Taip, kasdien | — |
| `metai_elektronines_cigaretes` | `'3'` | — | — | Taip, retkarčiais | — |
| `metai_elektronines_cigaretes` | `'4'` | — | — | Taip, bent kartą | — |
| `metai_elektronines_cigaretes` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `men_alkoholis` | `'1'` | — | — | Ne | — |
| `men_alkoholis` | `'2'` | — | — | Taip, kasdien | — |
| `men_alkoholis` | `'3'` | — | — | Taip, 2–3 kartus per savaitę | — |
| `men_alkoholis` | `'4'` | — | — | Taip, kartą per savaitę | — |
| `men_alkoholis` | `'5'` | — | — | Taip, 2–3 kartus per mėnesį | — |
| `men_alkoholis` | `'6'` | — | — | Taip, kelis kartus per metus | — |
| `men_alkoholis` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `metai_alkoholis` | `'1'` | — | — | Ne | — |
| `metai_alkoholis` | `'2'` | — | — | Taip, kasdien | — |
| `metai_alkoholis` | `'3'` | — | — | Taip, 2–3 kartus per savaitę | — |
| `metai_alkoholis` | `'4'` | — | — | Taip, kartą per savaitę | — |
| `metai_alkoholis` | `'5'` | — | — | Taip, 2–3 kartus per mėnesį | — |
| `metai_alkoholis` | `'6'` | — | — | Taip, kelis kartus per metus | — |
| `metai_alkoholis` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `men_narkotikai` | `'1'` | — | — | Taip | — |
| `men_narkotikai` | `'2'` | — | — | Ne | — |
| `men_narkotikai` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `metai_narkotikai` | `'1'` | — | — | Taip | — |
| `metai_narkotikai` | `'2'` | — | — | Ne | — |
| `metai_narkotikai` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `gyvenimas_narkotikai` | `'1'` | — | — | Taip | — |
| `gyvenimas_narkotikai` | `'2'` | — | — | Ne | — |
| `gyvenimas_narkotikai` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `fizine_veikla` | `'1'` | — | — | Neužsiimu tokia fizine veikla | — |
| `fizine_veikla` | `'2'` | — | — | 1 dieną | — |
| `fizine_veikla` | `'3'` | — | — | 2 dienas | — |
| `fizine_veikla` | `'4'` | — | — | 3 dienas | — |
| `fizine_veikla` | `'5'` | — | — | 4 dienas | — |
| `fizine_veikla` | `'6'` | — | — | 5 dienas ir daugiau | — |
| `fizine_veikla` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `atsvaitai` | `'1'` | — | — | Visada | — |
| `atsvaitai` | `'2'` | — | — | Kartais | — |
| `atsvaitai` | `'3'` | — | — | Ne | — |
| `atsvaitai` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `saugos_dirzai` | `'1'` | — | — | Visada | — |
| `saugos_dirzai` | `'2'` | — | — | Kartais | — |
| `saugos_dirzai` | `'3'` | — | — | Ne | — |
| `saugos_dirzai` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `salmai` | `'1'` | — | — | Visada | — |
| `salmai` | `'2'` | — | — | Kartais | — |
| `salmai` | `'3'` | — | — | Ne | — |
| `salmai` | `'4'` | — | — | Nevažinėju dviračiu | — |
| `salmai` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `artimi_zmones` | `'1'` | — | — | Nė vieno | — |
| `artimi_zmones` | `'2'` | — | — | 1–2 | — |
| `artimi_zmones` | `'3'` | — | — | 3–5 | — |
| `artimi_zmones` | `'4'` | — | — | 6 ir daugiau | — |
| `artimi_zmones` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `nerimas` | `'1'` | — | — | Ne, nebuvo | — |
| `nerimas` | `'2'` | — | — | Taip, bet ne labiau nei anksčiau | — |
| `nerimas` | `'3'` | — | — | Taip, ir šiek tiek labiau nei anksčiau | — |
| `nerimas` | `'4'` | — | — | Taip, ir daug labiau nei anksčiau | — |
| `nerimas` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `gyvenimo_kokybe` | `'1'` | — | — | Labai gera | — |
| `gyvenimo_kokybe` | `'2'` | — | — | Gera | — |
| `gyvenimo_kokybe` | `'3'` | — | — | Patenkinama | — |
| `gyvenimo_kokybe` | `'4'` | — | — | Bloga | — |
| `gyvenimo_kokybe` | `'5'` | — | — | Labai bloga | — |
| `gyvenimo_kokybe` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `sveikata` | `'1'` | — | — | Labai gera | — |
| `sveikata` | `'2'` | — | — | Gera | — |
| `sveikata` | `'3'` | — | — | Patenkinama | — |
| `sveikata` | `'4'` | — | — | Bloga | — |
| `sveikata` | `'5'` | — | — | Labai bloga | — |
| `sveikata` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `laimingumas` | `'1'` | — | — | Labai laimingas (-a) | — |
| `laimingumas` | `'2'` | — | — | Laimingas (-a) | — |
| `laimingumas` | `'3'` | — | — | Nei laimingas (-a), nei nelaimingas (-a) | — |
| `laimingumas` | `'4'` | — | — | Nelaimingas (-a) | — |
| `laimingumas` | `'5'` | — | — | Labai nelaimingas (-a) | — |
| `laimingumas` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `ilgalaike_sveikatos_problema` | `'1'` | — | — | Taip | — |
| `ilgalaike_sveikatos_problema` | `'2'` | — | — | Ne | — |
| `ilgalaike_sveikatos_problema` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `sveikiau_maitintis` | `'1'` | — | — | Taip, bandžiau ir pakeičiau | — |
| `sveikiau_maitintis` | `'2'` | — | — | Taip, bandžiau, bet nepakeičiau | — |
| `sveikiau_maitintis` | `'3'` | — | — | Nebandžiau keisti | — |
| `sveikiau_maitintis` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `tapti_fiziskai_aktyvesniu` | `'1'` | — | — | Taip, bandžiau ir pakeičiau | — |
| `tapti_fiziskai_aktyvesniu` | `'2'` | — | — | Taip, bandžiau, bet nepakeičiau | — |
| `tapti_fiziskai_aktyvesniu` | `'3'` | — | — | Nebandžiau keisti | — |
| `tapti_fiziskai_aktyvesniu` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `maziau_rukyti` | `'1'` | — | — | Taip, bandžiau ir pakeičiau | — |
| `maziau_rukyti` | `'2'` | — | — | Taip, bandžiau, bet nepakeičiau | — |
| `maziau_rukyti` | `'3'` | — | — | Nebandžiau keisti | — |
| `maziau_rukyti` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `maziau_vartoti_alkoholio` | `'1'` | — | — | Taip, bandžiau ir pakeičiau | — |
| `maziau_vartoti_alkoholio` | `'2'` | — | — | Taip, bandžiau, bet nepakeičiau | — |
| `maziau_vartoti_alkoholio` | `'3'` | — | — | Nebandžiau keisti | — |
| `maziau_vartoti_alkoholio` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `lytis` | `'1'` | — | — | Vyras | — |
| `lytis` | `'2'` | — | — | Moteris | — |
| `lytis` | `'9'` | — | — | Neatsakyta į klausimą | — |
| `gyvenamoji_vietove` | `'1'` | — | — | Miestas | — |
| `gyvenamoji_vietove` | `'2'` | — | — | Kaimas | — |
| `gyvenamoji_vietove` | `'9'` | — | — | Neatsakyta į klausimą | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/gyvensena/suaugusiu.csv
