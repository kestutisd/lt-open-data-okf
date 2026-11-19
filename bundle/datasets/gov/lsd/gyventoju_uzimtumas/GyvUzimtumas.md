---
type: Table
title: "GyvUzimtumas — Gyventojų užimtumo statistinis tyrimas"
description: "Gyventojų užimtumo statistinis tyrimas"
resource: "https://get.data.gov.lt/datasets/gov/lsd/gyventoju_uzimtumas/GyvUzimtumas"
tags: [gov, lsd, gyvuzimtumas, deployed, level-3, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/gyventoju_uzimtumas.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/lsd/gyventoju_uzimtumas.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/678/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/gyventoju_uzimtumas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# GyvUzimtumas — Gyventojų užimtumo statistinis tyrimas

Gyventojų užimtumo statistinis tyrimas[^manifest]

- **Model:** `datasets/gov/lsd/gyventoju_uzimtumas/GyvUzimtumas`[^manifest]
- **Dataset:** [Gyventojų užimtumo statistinio tyrimo duomenys](../gyventoju_uzimtumas.md) (`datasets/gov/lsd/gyventoju_uzimtumas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/gyventoju_uzimtumas.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/gyventoju_uzimtumas.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/gyventoju_uzimtumas/GyvUzimtumas` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `hhseqnum` | `string` | — | `4` | `open` | — | Respondento eilės numeris namų ūkyje | — |
| `hhlink` | `integer` | — | `4` | `open` | — | Ryšys su tiriamuoju asmeniu namų ūkyje | — |
| `sex` | `integer` | — | `4` | `open` | — | Lytis | — |
| `age` | `integer` | — | `4` | `open` | — | Amžius | — |
| `marstat` | `integer` | — | `4` | `open` | — | Šeiminė padėtis | — |
| `national` | `string` | — | `4` | `open` | — | Pilietybė | — |
| `countryb` | `string` | — | `4` | `open` | — | Gimimo šalis | — |
| `proxy` | `integer` | — | `4` | `open` | — | Dalyvavimo tyrime pobūdis | — |
| `wstator` | `integer` | — | `4` | `open` | — | Ekonominio aktyvumo statusas tiriamąją savaitę | — |
| `stapro` | `integer` | — | `4` | `open` | — | Užimtumo statusas | — |
| `nace3d` | `string` | — | `4` | `open` | — | Pagrindinės darbovietės ekonominės veiklos rūšis | — |
| `isco4d` | `string` | — | `4` | `open` | — | Profesija | — |
| `sizefirm` | `string` | — | `4` | `open` | — | Darbovietėje dirbančių asmenų skaičius | — |
| `countryw` | `string` | — | `4` | `open` | — | Šalis, kurioje yra darbovietė | — |
| `ystartwk` | `integer` | — | `4` | `open` | — | Metai, kuriais asmuo pradėjo dirbti šioje darbovietėje arba kaip savarankiškai dirbantis | — |
| `ftpt` | `integer` | — | `4` | `open` | — | Dirba visą ar ne visą darbo dienos ar savaitės laiką | — |
| `ftptreas` | `integer` | — | `4` | `open` | — | Priežastis, dėl kurios pasirinktas darbas ne visą darbo dienos ar savaitės laiką | — |
| `temp` | `integer` | — | `4` | `open` | — | Laikinas ar nuolatinis darbas | — |
| `tempreas` | `integer` | — | `4` | `open` | — | Priežastis, dėl kurios asmuo turi laikiną darbą | — |
| `tempdur` | `integer` | — | `4` | `open` | — | Terminuotos darbo sutarties trukmė | — |
| `shiftwk` | `integer` | — | `4` | `open` | — | Darbas pamainomis | — |
| `evenwk` | `integer` | — | `4` | `open` | — | Vakarinis darbas | — |
| `nightwk` | `integer` | — | `4` | `open` | — | Naktinis darbas | — |
| `wdwk` | `integer` | — | `4` | `open` | — | Darbas savaitgaliais | — |
| `hwusual` | `string` | — | `4` | `open` | — | Paprastai per savaitę pagrindiniame darbe dirbamų valandų skaičius | — |
| `hwactual` | `string` | — | `4` | `open` | — | Tiriamąją savaitę pagrindianiame darbe dirbtų valandų skaičius | — |
| `hwoverp` | `string` | — | `4` | `open` | — | Tiriamąją savaitę pagrindinėje darbovetėje apmokėti viršvalandžiai | — |
| `hwoverpu` | `string` | — | `4` | `open` | — | Tiramąją savaitę pagrindinėje darbovietėje neapmokėti viršvalandžiai | — |
| `wishmore` | `integer` | — | `4` | `open` | — | Noras paprastai dirbti daugiau valandų negu dabartinis dirbamų valandų skaičius | — |
| `hwwish` | `string` | — | `4` | `open` | — | Valandų skaičius, kurį asmuo norėtų dirbti | — |
| `homewk` | `integer` | — | `4` | `open` | — | Darbas namie | — |
| `lookoj` | `integer` | — | `4` | `open` | — | Kito darbo paieškos | — |
| `lookreas` | `integer` | — | `4` | `open` | — | Kito darbo paieškos priežastys | — |
| `exist2j` | `integer` | — | `4` | `open` | — | Daugiau kaip vienas darbas arba verslas | — |
| `stapro2j` | `integer` | — | `4` | `open` | — | Užimtumo statusas (nepagrindinėje darbovietėje) | — |
| `nace2j2d` | `string` | — | `4` | `open` | — | Nepagrindinės darbovietės ekonominės veiklos rūšis | — |
| `hwactua2` | `string` | — | `4` | `open` | — | Tiriamąją savaitę dirbtų valandų skaičius nepagrindinėje darbovietėje | — |
| `existpr` | `integer` | — | `4` | `open` | — | Ankstesnė darbo patirtis | — |
| `yearpr` | `integer` | — | `4` | `open` | — | Metai kuriais asmuo dirbo paskutinį kartą | — |
| `leavreas` | `string` | — | `4` | `open` | — | Pagrindinė priežastis, kodėl paliko paskutinį darbą arba verslą | — |
| `stapropr` | `integer` | — | `4` | `open` | — | Užimtumo statusas paskutinėje darbovietėje | — |
| `nacepr2d` | `string` | — | `4` | `open` | — | Darbovietės, kurioje asmuo dirbo paskutinį kartą, ekonominės veiklos rūšis | — |
| `iscopr3d` | `string` | — | `4` | `open` | — | Profesija paskutinėje darbovietėje | — |
| `seekwork` | `integer` | — | `4` | `open` | — | Ieškojo darbo per paskutines keturias savaites | — |
| `seekreas` | `integer` | — | `4` | `open` | — | Priežastys, dėl kurių asmuo neieško darbo | — |
| `seekdur` | `integer` | — | `4` | `open` | — | Darbo paieškų trukmė | — |
| `methoda` | `integer` | — | `4` | `open` | — | Ieškodamas darbo, kreipėsi į valstybinę darbo biržą | — |
| `methodb` | `integer` | — | `4` | `open` | — | Ieškodamas darbo, kreipėsi į privačią įdarbinimo agentūrą | — |
| `methodc` | `integer` | — | `4` | `open` | — | Kreipėsi tiesiogiai į darbdavius | — |
| `methodd` | `integer` | — | `4` | `open` | — | Kreiptėsi į draugus, gimines ir pan. | — |
| `methode` | `integer` | — | `4` | `open` | — | Skelbė apie darbo paiešką žiniasklaidoje | — |
| `methodf` | `integer` | — | `4` | `open` | — | Nagrinėjo skelbimus žiniasklaidoje | — |
| `methodm` | `integer` | — | `4` | `open` | — | Ieškojo darbo kitais būdais | — |
| `wantwork` | `integer` | — | `4` | `open` | — | Darbo neieškančio asmens noras dirbti | — |
| `availble` | `integer` | — | `4` | `open` | — | Galimybė pradėti darbą per artimiausias dvi savaites po tiriamosios savaitės | — |
| `avaireas` | `integer` | — | `4` | `open` | — | Priežastys, dėl kurių asmuo negalėtų pradėti dirbti per artimiausias 2 savaites | — |
| `register` | `integer` | — | `4` | `open` | — | Registracija valstybinėje įdarbinimo agentūroje | — |
| `educstat` | `integer` | — | `4` | `open` | — | Asmens mokymasis aukštojoje, profesinėje arba bendrojo ugdymo mokykloje per pastarąsias 4 savaites | — |
| `educlevl` | `integer` | — | `4` | `open` | — | Švietimo arba mokymo lygmuo | — |
| `educfild` | `string` | — | `4` | `open` | — | Švietimo arba mokymo sritis | — |
| `couratt` | `integer` | — | `4` | `open` | — | Ar asmuo lankė kursus, privačias pamokas (sporto klubą, mokėsi groti, dainuoti, šokti ir pan.), dalyvavo seminaruose, konferencijose per pastarąsias 4 savaites? | — |
| `courlen` | `integer` | — | `4` | `open` | — | Valandų skaičius, skirtas laikui mokymuose per pastarąsias 4 savaites | — |
| `hatlevel` | `integer` | — | `4` | `open` | — | Aukščiausias sėkmingai įgytas išsilavinimas | — |
| `hatfield` | `string` | — | `4` | `open` | — | Aukščiausio įgyto išsilavinimo mokymo/studijų programa | — |
| `refyear` | `integer` | — | `2` | `open` | — | Tyrimo metai | — |
| `refweek` | `string` | — | `4` | `open` | — | Tiriamoji savaitė | — |
| `region` | `string` | — | `4` | `open` | — | Regionas, kuriame yra namų ūkis | — |
| `hhnum` | `integer` | — | `4` | `open` | — | Namų ūkio eilės numeris | — |
| `coeff` | `number` | — | `4` | `open` | — | Svoris | — |
| `intwave` | `integer` | — | `4` | `open` | — | Tyrimo etapo eilės numeris | — |
| `courpurp` | `integer` | — | `4` | `open` | — | Pagrindinės dalyvavimo šiuose mokymuose priežastys | — |
| `courfild` | `string` | — | `4` | `open` | — | Paskutinio mokymosi mokymo programa | — |
| `metai` | `integer` | — | `2` | `open` | — | Statistinio tyrimo metai | — |
| `ketvirtis` | `integer` | — | `4` | `open` | — | Tyrimo metų ketvirtis | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `hhseqnum` | `"1"` | — | — | eilės numeris, priskirtas kiekvienam namų ūkio nariui | — |
| `hhseqnum` | `"2"` | — | — | eilės numeris, priskirtas kiekvienam namų ūkio nariui | — |
| `hhseqnum` | `"3"` | — | — | eilės numeris, priskirtas kiekvienam namų ūkio nariui | — |
| `hhseqnum` | `"4"` | — | — | eilės numeris, priskirtas kiekvienam namų ūkio nariui | — |
| `hhseqnum` | `"5"` | — | — | eilės numeris, priskirtas kiekvienam namų ūkio nariui | — |
| `hhseqnum` | `"6"` | — | — | eilės numeris, priskirtas kiekvienam namų ūkio nariui | — |
| `hhseqnum` | `"7"` | — | — | eilės numeris, priskirtas kiekvienam namų ūkio nariui | — |
| `hhseqnum` | `"8"` | — | — | eilės numeris, priskirtas kiekvienam namų ūkio nariui | — |
| `hhseqnum` | `"9"` | — | — | eilės numeris, priskirtas kiekvienam namų ūkio nariui | — |
| `hhseqnum` | `"10"` | — | — | eilės numeris, priskirtas kiekvienam namų ūkio nariui | — |
| `hhseqnum` | `"11"` | — | — | eilės numeris, priskirtas kiekvienam namų ūkio nariui | — |
| `hhseqnum` | `"12"` | — | — | eilės numeris, priskirtas kiekvienam namų ūkio nariui | — |
| `hhlink` | `1` | — | — | Tiriamasis asmuo | — |
| `hhlink` | `2` | — | — | Tiriamojo asmens sutuoktinis/ė (arba sugyventinis/ė) | — |
| `hhlink` | `3` | — | — | Tiriamojo asmens (arba jo/jos sutuoktinio/ės ar sugyventinio/ės) vaikas | — |
| `hhlink` | `4` | — | — | Tiriamojo asmens (arba jo/jos sutuoktinio/ės ar sugyventinio/ės) tėvas, motina, senelis/ė, prosenelis/ė | — |
| `hhlink` | `5` | — | — | Kitas giminaitis | — |
| `hhlink` | `6` | — | — | Kitas | — |
| `hhlink` | `9` | — | — | Netaikoma | — |
| `sex` | `1` | — | — | Vyras | — |
| `sex` | `2` | — | — | Moteris | — |
| `age` | `1` | — | — | 0,14 metų | — |
| `age` | `2` | — | — | 15,19 metų | — |
| `age` | `3` | — | — | 20,24 metų | — |
| `age` | `4` | — | — | 25,29 metų | — |
| `age` | `5` | — | — | 30,34 metų | — |
| `age` | `6` | — | — | 35,39 metų | — |
| `age` | `7` | — | — | 40,44 metų | — |
| `age` | `8` | — | — | 45,49 metų | — |
| `age` | `9` | — | — | 50,54 metų | — |
| `age` | `10` | — | — | 55,59 metų | — |
| `age` | `11` | — | — | 60,64 metų | — |
| `age` | `12` | — | — | 65,69 metų | — |
| `age` | `13` | — | — | 70,74 metų | — |
| `age` | `14` | — | — | 75 metų ir vyresni | — |
| `marstat` | `1` | — | — | Nevedęs/netekėjusi | — |
| `marstat` | `2` | — | — | Vedęs/ištekėjusi | — |
| `marstat` | `3` | — | — | Našlys/našlė, išsituokęs/išsituokusi | — |
| `national` | `"LT"` | — | — | Lietuvos | — |
| `national` | `"00"` | — | — | Kitos šalies | — |
| `countryb` | `"LT"` | — | — | Lietuva | — |
| `countryb` | `"00"` | — | — | Kita šalis | — |
| `proxy` | `1` | — | — | Atsakė pats respondentas | — |
| `proxy` | `2` | — | — | Informaciją pateikė kitas namų ūkio narys | — |
| `proxy` | `9` | — | — | Netaikoma (jaunesniems kaip 15 metų asmenims) | — |
| `wstator` | `1` | — | — | Užimtasis | — |
| `wstator` | `2` | — | — | Bedarbis | — |
| `wstator` | `3` | — | — | Neaktyvus | — |
| `wstator` | `9` | — | — | Netaikoma (jaunesniems kaip 15 metų asmenims) | — |
| `stapro` | `1` | — | — | Samdomasis darbuotojas | — |
| `stapro` | `2` | — | — | Kitas | — |
| `stapro` | `9` | — | — | Netaikoma | — |
| `nace3d` | `"A"` | — | — | Žemės ūkis, miškininkystė ir žuvininkystė | — |
| `nace3d` | `"B_E"` | — | — | Pramonė | — |
| `nace3d` | `"F"` | — | — | Statyba | — |
| `nace3d` | `"G_J"` | — | — | Didmeninė ir mažmeninė prekyba, transportas, apgyvendinimo ir maitinimo paslaugų veikla, informacija ir ryšiai | — |
| `nace3d` | `"K_N"` | — | — | Finansinė ir draudimo veikla, nekilnojamojo turto operacijos, profesinė, mokslinė ir techninė veikla, administracinė ir aptarnavimo veikla | — |
| `nace3d` | `"O_U"` | — | — | Viešasis valdymas, paslaugos socialinei sferai ir komunalinė veikla | — |
| `nace3d` | `"000"` | — | — | Netaikoma | — |
| `isco4d` | `"01"` | — | — | Vadovai | — |
| `isco4d` | `"02"` | — | — | Specialistai | — |
| `isco4d` | `"03"` | — | — | Technikai ir jaunesnieji specialistai | — |
| `isco4d` | `"04"` | — | — | Įstaigų tarnautojai | — |
| `isco4d` | `"05"` | — | — | Paslaugų sektoriaus darbuotojai ir pardavėjai | — |
| `isco4d` | `"06"` | — | — | Kvalifikuoti žemės, miškų ir žuvininkystės ūkio darbuotojai | — |
| `isco4d` | `"07"` | — | — | Kvalifikuoti darbininkai ir amatininkai | — |
| `isco4d` | `"08"` | — | — | Įrenginių ir mašinų operatoriai ir surinkėjai | — |
| `isco4d` | `"9_0"` | — | — | Nekvalifikuoti darbininkai, ginkluotųjų pajėgų profesijos | — |
| `isco4d` | `"99"` | — | — | Netaikoma | — |
| `sizefirm` | `"01"` | — | — | Nuo 1 iki 10 asmenų | — |
| `sizefirm` | `"02"` | — | — | Nuo 11 iki 49 asmenų | — |
| `sizefirm` | `"03"` | — | — | 50 asmenų ir daugiau | — |
| `sizefirm` | `"15"` | — | — | Nežinoma, bet daugiau kaip 10 asmenų | — |
| `sizefirm` | `"99"` | — | — | Netaikoma | — |
| `countryw` | `"LT"` | — | — | Lietuva | — |
| `countryw` | `"00"` | — | — | Kita šalis | — |
| `countryw` | `"99"` | — | — | Netaikoma | — |
| `ystartwk` | `1` | — | — | iki 1990 m. | — |
| `ystartwk` | `2` | — | — | 1991,2001 m. | — |
| `ystartwk` | `3` | — | — | 2002 m. arba vėliau | — |
| `ystartwk` | `9` | — | — | Netaikoma | — |
| `ftpt` | `1` | — | — | Visą | — |
| `ftpt` | `2` | — | — | Ne visą | — |
| `ftpt` | `9` | — | — | Netaikoma | — |
| `ftptreas` | `1` | — | — | asmuo mokėsi mokykloje arba kėlė kvalifikaciją dalyvaujant mokymuose | — |
| `ftptreas` | `2` | — | — | dėl asmeninių, šeiminių priežasčių ar savo ligos, negalios | — |
| `ftptreas` | `3` | — | — | asmuo negalėjo rasti darbo, kuriame galėtų dirbti visą darbo dienos ar savaitės laiką | — |
| `ftptreas` | `4` | — | — | dėl kitų priežasčių | — |
| `ftptreas` | `9` | — | — | Netaikoma | — |
| `temp` | `1` | — | — | Nuolatinis, asmuo dirba pagal neterminuotą darbo sutartį | — |
| `temp` | `2` | — | — | Laikinas, asmuo dirba pagal terminuotą darbo sutartį | — |
| `temp` | `9` | — | — | Netaikoma | — |
| `tempreas` | `1` | — | — | asmuo mokėsi, atliko praktiką, kėlė kvalifikaciją, stažavosi | — |
| `tempreas` | `2` | — | — | asmuo negalėjo rasti nuolatinio darbo | — |
| `tempreas` | `3` | — | — | asmuo nenorėjo dirbti nuolatinio darbo | — |
| `tempreas` | `4` | — | — | tai sutartis bandomajam laikotarpiui | — |
| `tempreas` | `9` | — | — | Netaikoma | — |
| `tempdur` | `1` | — | — | Trumpiau nei vienas mėnuo | — |
| `tempdur` | `2` | — | — | Vienas mėnuo ar ilgiau | — |
| `tempdur` | `9` | — | — | Netaikoma | — |
| `shiftwk` | `1` | — | — | Asmuo dirba pamainomis | — |
| `shiftwk` | `3` | — | — | Asmuo niekada nedirba pamainomis | — |
| `shiftwk` | `9` | — | — | Netaikoma | — |
| `evenwk` | `1` | — | — | Asmuo paprastai dirba vakarais | — |
| `evenwk` | `2` | — | — | Asmuo kartais dirba vakarais | — |
| `evenwk` | `3` | — | — | Asmuo niekada nedirba vakarais | — |
| `evenwk` | `9` | — | — | Netaikoma | — |
| `nightwk` | `1` | — | — | Asmuo paprastai dirba naktį | — |
| `nightwk` | `2` | — | — | Asmuo kartais dirba naktį | — |
| `nightwk` | `3` | — | — | Asmuo niekada nedirba naktį | — |
| `nightwk` | `9` | — | — | Netaikoma | — |
| `wdwk` | `1` | — | — | Asmuo paprastai dirba šeštadieniais ar sekmadieniais | — |
| `wdwk` | `2` | — | — | Asmuo kartais dirba šeštadieniais ar sekmadieniais | — |
| `wdwk` | `3` | — | — | Asmuo niekada nedirba šeštadieniais ar sekmadieniais | — |
| `wdwk` | `9` | — | — | Netaikoma | — |
| `hwusual` | `"00"` | — | — | Įprasto darbo valandų skaičiaus negalėjo nurodyti, kadangi per savaitę ar mėnesį dirbtų valandų skaičius labai skiriasi | — |
| `hwusual` | `"01"` | — | — | iki 20 val. | — |
| `hwusual` | `"02"` | — | — | 21,29 val. | — |
| `hwusual` | `"03"` | — | — | 30,39 val. | — |
| `hwusual` | `"04"` | — | — | 40,44 val. | — |
| `hwusual` | `"05"` | — | — | 45 val. ar daugiau | — |
| `hwusual` | `"99"` | — | — | Netaikoma | — |
| `hwactual` | `"00"` | — | — | Visai nedirbo | — |
| `hwactual` | `"01"` | — | — | iki 20 val. | — |
| `hwactual` | `"02"` | — | — | 21,29 val. | — |
| `hwactual` | `"03"` | — | — | 30,39 val. | — |
| `hwactual` | `"04"` | — | — | 40,44 val. | — |
| `hwactual` | `"05"` | — | — | 45 val. ar daugiau | — |
| `hwactual` | `"99"` | — | — | Netaikoma | — |
| `hwoverp` | `"00"` | — | — | 0 val. | — |
| `hwoverp` | `"01"` | — | — | 1,10 val. | — |
| `hwoverp` | `"02"` | — | — | 11,20 val. | — |
| `hwoverp` | `"03"` | — | — | 21 val. ar daugiau | — |
| `hwoverp` | `"99"` | — | — | Netaikoma | — |
| `hwoverpu` | `"00"` | — | — | 0 val. | — |
| `hwoverpu` | `"01"` | — | — | 1,10 val. | — |
| `hwoverpu` | `"02"` | — | — | 11 val. ar daugiau | — |
| `hwoverpu` | `"99"` | — | — | Netaikoma | — |
| `wishmore` | `0` | — | — | Ne | — |
| `wishmore` | `1` | — | — | Taip | — |
| `wishmore` | `9` | — | — | Netaikoma | — |
| `hwwish` | `"01"` | — | — | iki 20 val. | — |
| `hwwish` | `"02"` | — | — | 21,29 val. | — |
| `hwwish` | `"03"` | — | — | 30,39 val. | — |
| `hwwish` | `"04"` | — | — | 40,44 val. | — |
| `hwwish` | `"05"` | — | — | 45 val. ar daugiau | — |
| `hwwish` | `"99"` | — | — | Netaikoma | — |
| `homewk` | `1` | — | — | Asmuo paprastai dirba namie | — |
| `homewk` | `2` | — | — | Asmuo kartais dirba namie | — |
| `homewk` | `3` | — | — | Asmuo niekada nedirba namie | — |
| `homewk` | `9` | — | — | Netaikoma | — |
| `lookoj` | `0` | — | — | Asmuo neieškojo kito darbo | — |
| `lookoj` | `1` | — | — | Asmuo ieškojo kito darbo | — |
| `lookoj` | `9` | — | — | Netaikoma | — |
| `lookreas` | `1` | — | — | Grėsmė ar įsitikinimas, kad gali prarasti esamą darbą | — |
| `lookreas` | `2` | — | — | Dabartinis darbas yra laikinas | — |
| `lookreas` | `3` | — | — | Ieškojo papildomo darbo, kuriame reikėtų dirbti daugiau valandų nei dabartinėje darbovietėje | — |
| `lookreas` | `4` | — | — | Ieško darbo, kuriame reikėtų dirbti daugiau valandų nei dabartinėje darbovietėje | — |
| `lookreas` | `5` | — | — | Ieškojo darbo, kuriame reikėtų dirbti mažiau valandų nei dabartinėje darbovietėje | — |
| `lookreas` | `6` | — | — | Pageidavo turėti geresnes darbo sąlygas (pvz., darbo užmokestis, darbo ar laikas, skirtas atvykti į darbą arba grįžti, darbo kokybė) | — |
| `lookreas` | `7` | — | — | Kitos priežastys | — |
| `lookreas` | `9` | — | — | Netaikoma | — |
| `exist2j` | `1` | — | — | Tiriamąją savaitę asmuo turėjo tik vieną darbą arba verslą | — |
| `exist2j` | `2` | — | — | Tiriamąją savaitę asmuo turėjo daugiau kaip vieną darbą arba verslą (ne dėl darbo ar verslo keitimo) | — |
| `exist2j` | `9` | — | — | Netaikoma | — |
| `stapro2j` | `1` | — | — | Samdomasis darbuotojas | — |
| `stapro2j` | `2` | — | — | Kitas | — |
| `stapro2j` | `9` | — | — | Netaikoma | — |
| `nace2j2d` | `"A"` | — | — | Žemės ūkis, miškininkystė ir žuvininkystė | — |
| `nace2j2d` | `"B_E"` | — | — | Pramonė | — |
| `nace2j2d` | `"F"` | — | — | Statyba | — |
| `nace2j2d` | `"G_J"` | — | — | Didmeninė ir mažmeninė prekyba, transportas, apgyvendinimo ir maitinimo paslaugų veikla, informacija ir ryšiai | — |
| `nace2j2d` | `"K_N"` | — | — | Finansinė ir draudimo veikla, nekilnojamojo turto operacijos, profesinė, mokslinė ir techninė veikla, administracinė ir aptarnavimo veikla | — |
| `nace2j2d` | `"O_U"` | — | — | Viešasis valdymas, paslaugos socialinei sferai ir komunalinė veikla | — |
| `nace2j2d` | `"000"` | — | — | Netaikoma | — |
| `hwactua2` | `"00"` | — | — | Asmuo, kuris nedirbo nepagrindinėje darbovietėje tiriamąją savaitę | — |
| `hwactua2` | `"01"` | — | — | iki 20 val. | — |
| `hwactua2` | `"02"` | — | — | 21 val. ar daugiau | — |
| `hwactua2` | `"99"` | — | — | Netaikoma | — |
| `existpr` | `0` | — | — | Asmuo niekada nedirbo (visiškai atsitiktinis darbas, toks, kaip darbas atostogų metu, privalomoji karinė tarnyba arba viešieji darbai nelaikomi užimtumu) | — |
| `existpr` | `1` | — | — | Asmuo jau yra dirbęs (visiškai atsitiktinis darbas, toks, kaip darbas atostogų metu, privalomoji karinė tarnyba arba viešieji darbai nelaikomi užimtumu) | — |
| `existpr` | `9` | — | — | Netaikoma | — |
| `yearpr` | `1` | — | — | iki 1990 m. | — |
| `yearpr` | `2` | — | — | 1991,2001 m. | — |
| `yearpr` | `3` | — | — | 2002 m. arba vėliau | — |
| `yearpr` | `9` | — | — | Netaikoma | — |
| `leavreas` | `"00"` | — | — | Asmuo atleistas iš darbo arba atleistas dėl etatų mažinimo | — |
| `leavreas` | `"01"` | — | — | Pasibaigė terminuoto, sezoninio darbo sutartis | — |
| `leavreas` | `"02"` | — | — | Asmeninės, šeiminės priežastys arba dėl savo ligos, negalios | — |
| `leavreas` | `"03"` | — | — | Mokėsi ar kėlė kvalifikaciją | — |
| `leavreas` | `"04"` | — | — | Išėjo į pensiją | — |
| `leavreas` | `"05"` | — | — | Kitos priežastys | — |
| `leavreas` | `"99"` | — | — | Netaikoma | — |
| `stapropr` | `1` | — | — | Samdomasis darbuotojas | — |
| `stapropr` | `2` | — | — | Kitas | — |
| `nacepr2d` | `"A"` | — | — | Žemės ūkis, miškininkystė ir žuvininkystė | — |
| `nacepr2d` | `"B_E"` | — | — | Pramonė | — |
| `nacepr2d` | `"F"` | — | — | Statyba | — |
| `nacepr2d` | `"G_J"` | — | — | Didmeninė ir mažmeninė prekyba, transportas, apgyvendinimo ir maitinimo paslaugų veikla, informacija ir ryšiai | — |
| `nacepr2d` | `"K_N"` | — | — | Finansinė ir draudimo veikla, nekilnojamojo turto operacijos, profesinė, mokslinė ir techninė veikla, administracinė ir aptarnavimo veikla | — |
| `nacepr2d` | `"O_U"` | — | — | Viešasis valdymas, paslaugos socialinei sferai ir komunalinė veikla | — |
| `nacepr2d` | `"000"` | — | — | Netaikoma | — |
| `iscopr3d` | `"1"` | — | — | Vadovai | — |
| `iscopr3d` | `"2"` | — | — | Specialistai | — |
| `iscopr3d` | `"3"` | — | — | Technikai ir jaunesnieji specialistai | — |
| `iscopr3d` | `"4"` | — | — | Įstaigų tarnautojai | — |
| `iscopr3d` | `"5"` | — | — | Paslaugų sektoriaus darbuotojai ir pardavėjai | — |
| `iscopr3d` | `"6"` | — | — | Kvalifikuoti žemės, miškų ir žuvininkystės ūkio darbuotojai | — |
| `iscopr3d` | `"7"` | — | — | Kvalifikuoti darbininkai ir amatininkai | — |
| `iscopr3d` | `"8"` | — | — | Įrenginių ir mašinų operatoriai ir surinkėjai | — |
| `iscopr3d` | `"9_0"` | — | — | Nekvalifikuoti darbininkai, ginkluotųjų pajėgų profesijos | — |
| `iscopr3d` | `"99"` | — | — | Netaikoma | — |
| `seekwork` | `1` | — | — | Asmuo jau surado darbą arba ieško darbo | — |
| `seekwork` | `2` | — | — | Asmuo neieško darbo arba nerado darbo, kuriame pradėtų dirbti vėliau | — |
| `seekwork` | `9` | — | — | Netaikoma | — |
| `seekreas` | `1` | — | — | laukė grąžinimo į darbą, nes nedirbo dėl prastovų trūkstant darbo ar "priverstinių" atostogų | — |
| `seekreas` | `2` | — | — | dėl asmeninių, šeiminių priežasčių arba sirgo, buvo neįgalus | — |
| `seekreas` | `3` | — | — | mokėsi ar kėlė kvalifikaciją | — |
| `seekreas` | `4` | — | — | buvo pensininkas | — |
| `seekreas` | `5` | — | — | manė, kad neįmanoma rasti darbo | — |
| `seekreas` | `6` | — | — | kitų priežasčių | — |
| `seekreas` | `9` | — | — | Netaikoma | — |
| `seekdur` | `1` | — | — | Trumpiau nei 6 mėnesiai | — |
| `seekdur` | `2` | — | — | 6–11 mėnesių | — |
| `seekdur` | `3` | — | — | 12 mėnesių ar ilgiau | — |
| `seekdur` | `9` | — | — | Netaikoma | — |
| `methoda` | `0` | — | — | Ne | — |
| `methoda` | `1` | — | — | Taip | — |
| `methoda` | `9` | — | — | Netaikoma | — |
| `methodb` | `0` | — | — | Ne | — |
| `methodb` | `1` | — | — | Taip | — |
| `methodb` | `9` | — | — | Netaikoma | — |
| `methodc` | `0` | — | — | Ne | — |
| `methodc` | `1` | — | — | Taip | — |
| `methodc` | `9` | — | — | Netaikoma | — |
| `methodd` | `0` | — | — | Ne | — |
| `methodd` | `1` | — | — | Taip | — |
| `methodd` | `9` | — | — | Netaikoma | — |
| `methode` | `0` | — | — | Ne | — |
| `methode` | `1` | — | — | Taip | — |
| `methode` | `9` | — | — | Netaikoma | — |
| `methodf` | `0` | — | — | Ne | — |
| `methodf` | `1` | — | — | Taip | — |
| `methodf` | `9` | — | — | Netaikoma | — |
| `methodm` | `0` | — | — | Ne | — |
| `methodm` | `1` | — | — | Taip | — |
| `methodm` | `9` | — | — | Netaikoma | — |
| `wantwork` | `1` | — | — | tačiau, nepaisant to, norėtų turėti darbą | — |
| `wantwork` | `2` | — | — | ir nenori jo turėti | — |
| `wantwork` | `9` | — | — | Netaikoma | — |
| `availble` | `1` | — | — | asmuo galėtų pradėti dirbti tuoj pat (per 2 savaites) | — |
| `availble` | `2` | — | — | asmuo negalėtų pradėti dirbti tuoj pat (per 2 savaites) | — |
| `availble` | `9` | — | — | Netaikoma | — |
| `avaireas` | `1` | — | — | turi baigti mokslus | — |
| `avaireas` | `2` | — | — | negali palikti dabartinio darbo per artimiausias 2 savaites | — |
| `avaireas` | `3` | — | — | dėl asmeninių, šeiminių priežasčių ar sirgo, buvo neįgalus | — |
| `avaireas` | `4` | — | — | dėl kitų priežasčių | — |
| `avaireas` | `9` | — | — | Netaikoma | — |
| `register` | `1` | — | — | Taip | — |
| `register` | `2` | — | — | Ne | — |
| `register` | `9` | — | — | Netaikoma (asmenims, jaunesniems nei 15 metų arba vyresniems nei 75 metų) | — |
| `educstat` | `1` | — | — | Mokėsi | — |
| `educstat` | `2` | — | — | Nesimokė | — |
| `educstat` | `9` | — | — | Netaikoma (jaunesniems kaip 15 metų asmenims) | — |
| `educlevl` | `1` | — | — | Žemesnis (ISCED 0,2) | — |
| `educlevl` | `2` | — | — | Vidutinis (ISCED 3,4) | — |
| `educlevl` | `3` | — | — | Aukščiausias (ISCED 5,6) | — |
| `educlevl` | `9` | — | — | Netaikoma | — |
| `educfild` | `"000"` | — | — | Bendrosios programos | — |
| `educfild` | `"100"` | — | — | Mokytojų rengimas ir švietimo mokslas | — |
| `educfild` | `"200"` | — | — | Humanitariniai mokslai, kalbos ir menai | — |
| `educfild` | `"300"` | — | — | Socialiniai mokslai, verslas ir teisė | — |
| `educfild` | `"400"` | — | — | Gamtos mokslai, matematika ir naudojimasis kompiuteriu | — |
| `educfild` | `"500"` | — | — | Inžinerija, gamyba ir statyba | — |
| `educfild` | `"600"` | — | — | Žemės ūkis ir veterinarija | — |
| `educfild` | `"700"` | — | — | Sveikata ir rūpyba | — |
| `educfild` | `"800"` | — | — | Paslaugos | — |
| `educfild` | `"900"` | — | — | Nežinomas | — |
| `educfild` | `"999"` | — | — | Netaikoma | — |
| `couratt` | `1` | — | — | Taip | — |
| `couratt` | `2` | — | — | Ne | — |
| `couratt` | `9` | — | — | Netaikoma (jaunesniems kaip 15 metų asmenims) | — |
| `courlen` | `1` | — | — | 1,10 val | — |
| `courlen` | `2` | — | — | 11,40 val. | — |
| `courlen` | `3` | — | — | Daugiau kaip 40 val. | — |
| `courlen` | `9` | — | — | Netaikoma | — |
| `hatlevel` | `1` | — | — | Žemesnis (ISCED 0,2) | — |
| `hatlevel` | `2` | — | — | Vidutinis (ISCED 3,4) | — |
| `hatlevel` | `3` | — | — | Aukščiausias (ISCED 5,6) | — |
| `hatlevel` | `9` | — | — | Netaikoma (jaunesniems nei 15 metų amžiaus) | — |
| `hatfield` | `"000"` | — | — | Bendrosios programos | — |
| `hatfield` | `"100"` | — | — | Mokytojų rengimas ir švietimo mokslas | — |
| `hatfield` | `"200"` | — | — | Humanitariniai mokslai, kalbos ir menai | — |
| `hatfield` | `"300"` | — | — | Socialiniai mokslai, verslas ir teisė | — |
| `hatfield` | `"400"` | — | — | Gamtos mokslai, matematika ir naudojimasis kompiuteriu | — |
| `hatfield` | `"500"` | — | — | Inžinerija, gamyba ir statyba | — |
| `hatfield` | `"600"` | — | — | Žemės ūkis ir veterinarija | — |
| `hatfield` | `"700"` | — | — | Sveikata ir rūpyba | — |
| `hatfield` | `"800"` | — | — | Paslaugos | — |
| `hatfield` | `"900"` | — | — | Nežinomas | — |
| `hatfield` | `"999"` | — | — | Netaikoma | — |
| `refweek` | `"01"` | — | — | Savaitės, trunkančios nuo pirmadienio iki sekmadienio, numeris | — |
| `refweek` | `"02"` | — | — | Savaitės, trunkančios nuo pirmadienio iki sekmadienio, numeris | — |
| `refweek` | `"03"` | — | — | Savaitės, trunkančios nuo pirmadienio iki sekmadienio, numeris | — |
| `refweek` | `"04"` | — | — | Savaitės, trunkančios nuo pirmadienio iki sekmadienio, numeris | — |
| `refweek` | `"05"` | — | — | Savaitės, trunkančios nuo pirmadienio iki sekmadienio, numeris | — |
| `refweek` | `"06"` | — | — | Savaitės, trunkančios nuo pirmadienio iki sekmadienio, numeris | — |
| `refweek` | `"07"` | — | — | Savaitės, trunkančios nuo pirmadienio iki sekmadienio, numeris | — |
| `refweek` | `"08"` | — | — | Savaitės, trunkančios nuo pirmadienio iki sekmadienio, numeris | — |
| `refweek` | `"09"` | — | — | Savaitės, trunkančios nuo pirmadienio iki sekmadienio, numeris | — |
| `refweek` | `"10"` | — | — | Savaitės, trunkančios nuo pirmadienio iki sekmadienio, numeris | — |
| `refweek` | `"11"` | — | — | Savaitės, trunkančios nuo pirmadienio iki sekmadienio, numeris | — |
| `refweek` | `"12"` | — | — | Savaitės, trunkančios nuo pirmadienio iki sekmadienio, numeris | — |
| `refweek` | `"13"` | — | — | Savaitės, trunkančios nuo pirmadienio iki sekmadienio, numeris | — |
| `region` | `"001"` | — | — | Alytaus apskritis | — |
| `region` | `"002"` | — | — | Kauno apskritis | — |
| `region` | `"003"` | — | — | Klaipėdos apskritis | — |
| `region` | `"004"` | — | — | Marijampolės apskritis | — |
| `region` | `"005"` | — | — | Panevežio apskritis | — |
| `region` | `"006"` | — | — | Šiaulių apskritis | — |
| `region` | `"007"` | — | — | Tauragės apskritis | — |
| `region` | `"008"` | — | — | Telšių apskritis | — |
| `region` | `"009"` | — | — | Utenos apskritis | — |
| `region` | `"00A"` | — | — | Vilniaus apskritis | — |
| `intwave` | `1` | — | — | Dalyvauja tyrime pirmą kartą | — |
| `intwave` | `2` | — | — | Dalyvauja tyrime antrą kartą | — |
| `intwave` | `3` | — | — | Dalyvauja tyrime trečią kartą | — |
| `intwave` | `4` | — | — | Dalyvauja tyrime ketvirtą kartą | — |
| `intwave` | `900` | — | — | Nežinomas | — |
| `intwave` | `999` | — | — | Netaikoma | — |
| `courpurp` | `1` | — | — | Susijusios su darbu | — |
| `courpurp` | `2` | — | — | Asmeninės | — |
| `courpurp` | `9` | — | — | Netaikoma | — |
| `courfild` | `"000"` | — | — | Bendrosios programos | — |
| `courfild` | `"100"` | — | — | Mokytojų rengimas ir švietimo mokslas | — |
| `courfild` | `"200"` | — | — | Humanitariniai mokslai, kalbos ir menai | — |
| `courfild` | `"300"` | — | — | Socialiniai mokslai, verslas ir teisė | — |
| `courfild` | `"400"` | — | — | Gamtos mokslai, matematika ir naudojimasis kompiuteriu | — |
| `courfild` | `"500"` | — | — | Inžinerija, gamyba ir statyba | — |
| `courfild` | `"600"` | — | — | Žemės ūkis ir veterinarija | — |
| `courfild` | `"700"` | — | — | Sveikata ir rūpyba | — |
| `courfild` | `"800"` | — | — | Paslaugos | — |
| `courfild` | `"900"` | — | — | Nežinomas | — |
| `courfild` | `"999"` | — | — | Netaikoma | — |
| `ketvirtis` | `1` | — | — | Pirmas | — |
| `ketvirtis` | `2` | — | — | Antras | — |
| `ketvirtis` | `3` | — | — | Trečias | — |
| `ketvirtis` | `4` | — | — | Ketvirtas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(ref: "hhseqnum")` | `ref` | `4` | `open` | — | — | — |
| `refyear` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

# Related References

- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/gyventoju_uzimtumas.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/gyventoju_uzimtumas.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/gyventoju_uzimtumas (https://data.gov.lt/datasets/678/)
