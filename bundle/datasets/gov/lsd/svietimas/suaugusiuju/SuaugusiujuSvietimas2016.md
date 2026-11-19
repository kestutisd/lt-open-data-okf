---
type: Table
title: "SuaugusiujuSvietimas2016 — Suaugusiųjų švietimo statistinis tyrimas 2016 m."
description: "2016 metais atliktas suaugusiųjų švietimo statistinio tyrimas"
resource: "https://get.data.gov.lt/datasets/gov/lsd/svietimas/suaugusiuju/SuaugusiujuSvietimas2016"
tags: [gov, lsd, suaugusiujusvietimas2016, deployed, cadence-quinquennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/svietimas.csv#L604"
    title: "atviriduomenys/manifest — datasets/gov/lsd/svietimas.csv#L604"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1621/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/svietimas/suaugusiuju"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# SuaugusiujuSvietimas2016 — Suaugusiųjų švietimo statistinis tyrimas 2016 m.

2016 metais atliktas suaugusiųjų švietimo statistinio tyrimas[^manifest]

- **Model:** `datasets/gov/lsd/svietimas/suaugusiuju/SuaugusiujuSvietimas2016`[^manifest]
- **Dataset:** [Suaugusiųjų švietimo statistinio tyrimo duomenys](../suaugusiuju.md) (`datasets/gov/lsd/svietimas/suaugusiuju`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/svietimas.csv#L604](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/svietimas.csv#L604)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/svietimas/suaugusiuju/SuaugusiujuSvietimas2016` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUINQUENNIAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | — | `open` | — | Respondento indentifikavimo kodas | — |
| `deg_urb` | `integer` | — | — | `open` | — | Namų ūkio vietovės urbanizacijos lygis | — |
| `vietove` | `integer` | — | — | `open` | — | Miestas ar kaimas | — |
| `respweight` | `string` | — | — | `open` | — | Asmenų svorinis daugiklis | — |
| `nfeactweight` | `string` | — | — | `open` | — | Neformalios mokymo veiklos svorinis daugiklis | — |
| `hhnbpers_tot` | `integer` | — | — | `open` | — | Bendras namų ūkyje gyvenančių asmenų skaičius (įskaitant respondentą) | — |
| `hhnbpers_0_13` | `integer` | — | — | `open` | — | Namų ūkyje gyvenančių 0–13 metų amžiaus asmenų skaičius | — |
| `hhnbpers_14_24` | `integer` | — | — | `open` | — | Namų ūkyje gyvenančių 14–24 metų amžiaus asmenų skaičius | — |
| `hhnbpers_25plus` | `integer` | — | — | `open` | — | Namų ūkyje gyvenančių 25 metų ir vyresnio amžiaus asmenų skaičius | — |
| `hhtype` | `integer` | — | — | `open` | — | Namų ūkio tipas | — |
| `hhincome` | `integer` | — | — | `open` | — | Namų ūkio grynosios mėnesio ekvivalentinės pajamos | — |
| `sex` | `integer` | `enum: sex` | — | `open` | — | Lytis | — |
| `age` | `integer` | — | — | `open` | — | Amžiaus grupės | — |
| `citizen` | `integer` | — | — | `open` | — | Pilietybė | — |
| `birthplace` | `integer` | — | — | `open` | — | Gimimo šalis | — |
| `restime` | `integer` | — | — | `open` | — | Gyvenimo Lietuvoje metų skaičius | — |
| `marstadefacto` | `integer` | — | — | `open` | — | De facto santuokinė padėtis (bendras gyvenimas neįregistravus santuokos) | — |
| `hatlevel` | `integer` | — | — | `open` | — | Aukščiausias įgytas išsilavinimas (ISCED 2011) | — |
| `hatfield` | `integer` | — | — | `open` | — | Aukščiausias įgytas išsilavinimas pagal mokymo/studijų sritis | — |
| `hatyear` | `integer` | — | — | `open` | — | Metai, kuriais įgytas aukščiausias išsilavinimas | — |
| `hatvoc` | `integer` | — | — | `open` | — | Aukščiausio įgyto išsilavinimo mokymo lygio kryptis | — |
| `dropeduc` | `integer` | — | — | `open` | — | Nebaigtas formalusis mokymas | — |
| `dropeduclevel` | `integer` | — | — | `open` | — | Nebaigtos formaliojo švietimo programos lygmuo (bandė įgyti aukštesnį išsilavinimą, bet nebaigė mokslų) | — |
| `dropeducvoc` | `integer` | — | — | `open` | — | Nebaigtos formaliojo švietimo programos mokymo lygio kryptis | — |
| `mainstat` | `integer` | — | — | `open` | — | Pagrindinis dabartinio užimtumo statusas | — |
| `emp12m` | `integer` | — | — | `open` | — | Užimtumas per pastaruosius 12 mėnesių | — |
| `jobstat` | `integer` | — | — | `open` | — | Profesinis statusas | — |
| `locsizefirm` | `integer` | — | — | `open` | — | Respondento darbovietėje ar šeimos ūkyje dirbančių asmenų skaičius | — |
| `jobtime` | `integer` | — | — | `open` | — | Metai, kuriais asmuo pradėjo dirbti dabartinį pagrindinį darbą | — |
| `hatfather` | `integer` | — | — | `open` | — | Aukščiausias tėvų (globėjų) įgytas išsilavinimas | — |
| `hatmother` | `integer` | — | — | `open` | — | Motina (globėja) | — |
| `birthfather` | `integer` | — | — | `open` | — | Tėvo gimimo šalis | — |
| `birthmother` | `integer` | — | — | `open` | — | Motinos gimimo šalis | — |
| `fed` | `integer` | — | — | `open` | — | Dalyvavimas formaliojo švietimo veikloje per pastaruosius 12 mėn. | — |
| `fednum` | `integer` | — | — | `open` | — | Dalyvavimo formaliojo švietimo veikloje, kurioje dalyvavo per pastaruosius 12 mėn., kartų skaičius | — |
| `fedlevel` | `integer` | — | — | `open` | — | Paskiausios formaliojo švietimo veiklos lygmuo (ISCED 2011) | — |
| `seekinfo` | `integer` | — | — | `open` | — | Per pastaruosius 12 mėnesių ieškota informacijos apie mokymosi galimybes (formalųjį ir neformalųjį švietimą ir profesinį mokymą) | — |
| `guideinst_1` | `integer` | — | — | `open` | — | Nemokamai gavau informacijos arba konsultacijų ir (arba) pagalbos dėl mokymosi galimybių iš institucijų ir (arba) organizacijų | — |
| `guideinst_2` | `integer` | — | — | `open` | — | Sumokėjau už iš institucijų ir (arba) organizacijų gautą informaciją arba konsultacijas ir (arba) pagalbą dėl mokymosi galimybių | — |
| `guideinst_3` | `integer` | — | — | `open` | — | Informacijos arba konsultacijų ir (arba) pagalbos dėl mokymosi galimybių iš institucijų ir (arba) organizacijų negavau | — |
| `guideinst` | `integer` | — | — | `open` | — | Per pastaruosius 12 mėnesių gautos nemokamos informacijos arba konsultacijų ir (arba) pagalbos dėl mokymosi galimybių šaltinis | — |
| `guidesource_1` | `integer` | — | — | `open` | — | Iš švietimo įstaigų (mokyklos, kolegijos, universiteto, profesinio rengimo ir mokymo centro, suaugusiųjų mokymo institucijos ) | — |
| `guidesource_2` | `integer` | — | — | `open` | — | Iš užimtumo tarnybos (Darbo biržos) | — |
| `guidesource_3` | `integer` | — | — | `open` | — | Iš darbdavio ar darbdavių organizacijų | — |
| `guidesource_4` | `integer` | — | — | `open` | — | Iš profesinių sąjungų, darbo tarybos | — |
| `guidesource_5` | `integer` | — | — | `open` | — | Iš kitų institucijų/organizacijų, teikiančių nemokamą informaciją arba konsultacijas ir (arba) pagalbą dėl mokymosi galimybių | — |
| `guidesource` | `integer` | — | — | `open` | — | Per pastaruosius 12 mėnesių gautos nemokamos informacijos arba konsultacijų ir (arba) pagalbos dėl mokymosi galimybių šaltinis | — |
| `guidetype_1` | `integer` | — | — | `open` | — | Informacija arba konsultacijos ir (arba) pagalba dėl mokymosi galimybių | — |
| `guidetype_2` | `integer` | — | — | `open` | — | Įgūdžių ir gebėjimų vertinimas naudojant testus, įgūdžių patikrinimus arba pokalbius | — |
| `guidetype_3` | `integer` | — | — | `open` | — | Informacija ar konsultacijos ir (arba) pagalba dėl įgūdžių, kompetencijos ar ankstesnio mokymosi įteisinimo/pripažinimo tvarkos patvirtinimo | — |
| `guidetype_4` | `integer` | — | — | `open` | — | Kitų rūšių informacija ar konsultacijos ir (arba) pagalba | — |
| `guidetype` | `integer` | — | — | `open` | — | Per pastaruosius 12 mėnesių gautos nemokamos informacijos arba konsultacijų ir (arba) pagalbos dėl mokymosi galimybių tipas | — |
| `guidemode_1` | `integer` | — | — | `open` | — | Asmeninis bendravimas | — |
| `guidemode_2` | `integer` | — | — | `open` | — | Bendravimas su asmeniu internetu, telefonu, elektroniniu paštu arba bet kokiomis kitomis medijų priemonėmis | — |
| `guidemode_3` | `integer` | — | — | `open` | — | Bendravimas informacijos arba konsultacijų ir (arba) pagalbos teikimui naudojant kompiuterinę programėlę | — |
| `guidemode_4` | `integer` | — | — | `open` | — | Jokio bendravimo, informacija suteikta tik naudojant specialią medžiagą (knygas, plakatus, žiniatinklį, informacinius lapelius, TV programų medžiagą, ir kt.) | — |
| `guidemode` | `integer` | — | — | `open` | — | Per pastaruosius 12 mėnesių gautos nemokamos informacijos arba konsultacijų ir (arba) pagalbos dėl mokymosi galimybių teikimo būdas | — |
| `fedstartyear` | `integer` | — | — | `open` | — | Metai, kuriais prasidėjo paskiausia formaliojo švietimo veikla | — |
| `fedcomp` | `integer` | — | — | `open` | — | Paskiausios formaliojo švietimo veiklos baigimas | — |
| `fedfield` | `integer` | — | — | `open` | — | Paskiausios formaliojo švietimo veiklos sritis | — |
| `fedvoc` | `integer` | — | — | `open` | — | Paskiausios formaliojo švietimo veiklos kryptis | — |
| `feddist` | `integer` | — | — | `open` | — | Paskiausia formaliojo švietimo veikla, organizuota kaip nuotolinis mokymasis | — |
| `feddistol` | `integer` | — | — | `open` | — | Nuotolinis mokymasis, rengiamas kaip mokymo kursai internetu | — |
| `fedoera` | `integer` | — | — | `open` | — | Naudojimasis internetiniais švietimo ištekliais paskiausiai formaliojo švietimo veiklai | — |
| `fedoerb` | `integer` | — | — | `open` | — | Bendravimas su kitais asmenimis (pvz. mokytojais, studentais) naudojant švietimo interneto svetaines ir(arba) portalus, vykstant paskiausiai formaliojo švietimo veiklai | — |
| `fedreason_01a` | `integer` | — | — | `open` | — | Kad geriau atlikčiau darbą | — |
| `fedreason_01b` | `integer` | — | — | `open` | — | Kad pagerinčiau savo karjeros perspektyvas | — |
| `fedreason_02` | `integer` | — | — | `open` | — | Kad sumažinčiau galimybes netekti darbo | — |
| `fedreason_03` | `integer` | — | — | `open` | — | Kad turėčiau daugiau galimybių gauti ar pakeisti darbą arba profesiją | — |
| `fedreason_04` | `integer` | — | — | `open` | — | Kad galėčiau pradėti savo verslą | — |
| `fedreason_05` | `integer` | — | — | `open` | — | Buvo privaloma dalyvauti | — |
| `fedreason_06` | `integer` | — | — | `open` | — | Kad įgyčiau kasdieniame gyvenime praversiančių žinių ir (arba) įgūdžių | — |
| `fedreason_07` | `integer` | — | — | `open` | — | Kad gaučiau daugiau žinių ir (arba) ugdyčiau įgūdžius, susijusius su dominančiu dalyku | — |
| `fedreason_08` | `integer` | — | — | `open` | — | Kad gaučiau pažymėjimą | — |
| `fedreason_09` | `integer` | — | — | `open` | — | Kad susipažinčiau su naujais žmonėmis ir (arba) smagiai praleisčiau laiką | — |
| `fedreason` | `integer` | — | — | `open` | — | Dalyvavimo paskiausioje formaliojo švietimo veikloje priežastys | — |
| `fedworktime` | `integer` | — | — | `open` | — | Paskiausia formaliojo švietimo veikla darbo valandomis, už kurias mokamas atlyginimas (įskaitant mokamas atostogas ar kompensacinius laisvadienius) | — |
| `fedpaid` | `integer` | — | — | `open` | — | Mokesčiai už mokslą, registraciją, egzaminus, išlaidos knygoms ar techninėms mokymosi priemonėms, skirtoms paskiausiai formaliojo švietimo veiklai | — |
| `fedpaidby_1` | `integer` | — | — | `open` | — | Esamas ar būsimas darbdavys | — |
| `fedpaidby_2` | `integer` | — | — | `open` | — | Valstybės užimtumo tarnybos | — |
| `fedpaidby_3` | `integer` | — | — | `open` | — | Kitos valstybės institucijos | — |
| `fedpaidby_4` | `integer` | — | — | `open` | — | Namų ūkio narys ar giminaitis | — |
| `fedpaidby` | `integer` | — | — | `open` | — | Už mokslą, registraciją, egzaminus, knygas ar technines mokymosi priemones, skirtas paskiausiai formaliojo švietimo veiklai, iš dalies arba visiškai apmokėjo: | — |
| `fedusea` | `integer` | — | — | `open` | — | Įgūdžių ar žinių, įgytų dalyvaujant paskiausioje formaliojo švietimo veikloje, dabartinis naudojimas | — |
| `feduseb` | `integer` | — | — | `open` | — | Įgūdžių ar žinių, įgytų dalyvaujant paskiausioje formaliojo švietimo veikloje, tikėtinas naudojimas | — |
| `fedoutcome_1` | `integer` | — | — | `open` | — | Naujas darbas | — |
| `fedoutcome_3` | `integer` | — | — | `open` | — | Didesnis darbo užmokestis | — |
| `fedoutcome_2` | `integer` | — | — | `open` | — | Paaukštinimas | — |
| `fedoutcome_4` | `integer` | — | — | `open` | — | Naujos užduotys | — |
| `fedoutcome_5` | `integer` | — | — | `open` | — | Geresni darbo rezultatai | — |
| `fedoutcome_6` | `integer` | — | — | `open` | — | Asmeninės priežastys (susipažino su naujais žmonėmis, atnaujino bendruosius gebėjimus, kt.) | — |
| `fedoutcome_7` | `integer` | — | — | `open` | — | Kol kas jokių rezultatų | — |
| `fedoutcome` | `integer` | — | — | `open` | — | Rezultatai, susiję su naujais įgūdžiais ir (arba) žiniomis, įgytomis dalyvaujant paskiausioje formaliojo švietimo veikloje | — |
| `nfecourse` | `integer` | — | — | `open` | — | Kvalifikacijos tobulinimo kursai | — |
| `nfeworkshop` | `integer` | — | — | `open` | — | Praktiniai ir teoriniai mokymo seminarai | — |
| `nfeguidedjt` | `integer` | — | — | `open` | — | Mokymas darbo vietoje | — |
| `nfelesson` | `integer` | — | — | `open` | — | Privačios pamokos | — |
| `nfenum` | `integer` | — | — | `open` | — | Dalyvavimo neformaliojo švietimo veikloje, kurioje dalyvauta per pastaruosius 12 mėn., kartų skaičius | — |
| `nfeact01_type` | `integer` | — | — | `open` | — | Pirma veiklos rūšis | — |
| `nfeact01_purp` | `integer` | — | — | `open` | — | Mokymosi veiklos tikslas | — |
| `nfeact01_worktime` | `integer` | — | — | `open` | — | Mokymosi veikla vyko visiškai ar daugiausia darbo valandomis, už kurias buvo mokamas atlygis (įskaitant mokamas atostogas ir kompensacinius laisvadienius) | — |
| `nfeact01_paidby` | `integer` | — | — | `open` | — | Mokymosi veikla, kurios dalį išlaidų arba visas išlaidas apmokėjo darbdavys | — |
| `nfeact02_type` | `integer` | — | — | `open` | — | Antros veiklos rūšis | — |
| `nfeact02_purp` | `integer` | — | — | `open` | — | Mokymosi veiklos tikslas | — |
| `nfeact02_worktime` | `integer` | — | — | `open` | — | Mokymosi veikla vyko visiškai ar daugiausia darbo valandomis, už kurias buvo mokamas atlygis (įskaitant mokamas atostogas ir kompensacinius laisvadienius) | — |
| `nfeact02_paidby` | `integer` | — | — | `open` | — | Mokymosi veikla, kurios dalį išlaidų arba visas išlaidas apmokėjo darbdavys | — |
| `nfeact03_type` | `integer` | — | — | `open` | — | Trečios veiklos rūšis | — |
| `nfeact03_purp` | `integer` | — | — | `open` | — | Mokymosi veiklos tikslas | — |
| `nfeact03_worktime` | `integer` | — | — | `open` | — | Mokymosi veikla vyko visiškai ar daugiausia darbo valandomis, už kurias buvo mokamas atlygis (įskaitant mokamas atostogas ir kompensacinius laisvadienius) | — |
| `nfeact03_paidby` | `integer` | — | — | `open` | — | Mokymosi veikla, kurios dalį išlaidų arba visas išlaidas apmokėjo darbdavys | — |
| `nfeact04_type` | `integer` | — | — | `open` | — | Ketvirtos veiklos rūšis | — |
| `nfeact04_purp` | `integer` | — | — | `open` | — | Mokymosi veiklos tikslas | — |
| `nfeact04_worktime` | `integer` | — | — | `open` | — | Mokymosi veikla vyko visiškai ar daugiausia darbo valandomis, už kurias buvo mokamas atlygis (įskaitant mokamas atostogas ir kompensacinius laisvadienius) | — |
| `nfeact04_paidby` | `integer` | — | — | `open` | — | Mokymosi veikla, kurios dalį išlaidų arba visas išlaidas apmokėjo darbdavys | — |
| `nfeact05_type` | `integer` | — | — | `open` | — | Penktos veiklos rūšis | — |
| `nfeact05_purp` | `integer` | — | — | `open` | — | Mokymosi veiklos tikslas | — |
| `nfeact05_worktime` | `integer` | — | — | `open` | — | Mokymosi veikla vyko visiškai ar daugiausia darbo valandomis, už kurias buvo mokamas atlygis (įskaitant mokamas atostogas ir kompensacinius laisvadienius) | — |
| `nfeact05_paidby` | `integer` | — | — | `open` | — | Mokymosi veikla, kurios dalį išlaidų arba visas išlaidas apmokėjo darbdavys | — |
| `nfeact06_type` | `integer` | — | — | `open` | — | Šeštos veiklos rūšis | — |
| `nfeact06_purp` | `integer` | — | — | `open` | — | Mokymosi veiklos tikslas | — |
| `nfeact06_worktime` | `integer` | — | — | `open` | — | Mokymosi veikla vyko visiškai ar daugiausia darbo valandomis, už kurias buvo mokamas atlygis (įskaitant mokamas atostogas ir kompensacinius laisvadienius) | — |
| `nfeact06_paidby` | `integer` | — | — | `open` | — | Mokymosi veikla, kurios dalį išlaidų arba visas išlaidas apmokėjo darbdavys | — |
| `nfeact07_type` | `integer` | — | — | `open` | — | Septintos veiklos rūšis | — |
| `nfeact07_pur` | `integer` | — | — | `open` | — | Mokymosi veiklos tikslas | — |
| `nfeact07_worktime` | `integer` | — | — | `open` | — | Mokymosi veikla vyko visiškai ar daugiausia darbo valandomis, už kurias buvo mokamas atlygis (įskaitant mokamas atostogas ir kompensacinius laisvadienius) | — |
| `nfeact07_paidby` | `integer` | — | — | `open` | — | Mokymosi veikla, kurios dalį išlaidų arba visas išlaidas apmokėjo darbdavys | — |
| `nferand1` | `integer` | — | — | `open` | — | Pirmos atsitiktinai atrinktos švietimo veiklos kodas | — |
| `nferand1_type` | `integer` | — | — | `open` | — | Kaip ir NFEACT01_TYPE – NFEACT07_TYPE nurodytas pirmos atsitiktinai atrinktos mokymo veiklos kodas | — |
| `nfefield1` | `integer` | — | — | `open` | — | Pirmos švietimo veiklos mokymo sritis | — |
| `nfedist1` | `integer` | — | — | `open` | — | Pirma švietimo veikla, organizuojama kaip nuotolinis mokymasis | — |
| `nfedistol1` | `integer` | — | — | `open` | — | Nuotolinis mokymasis, vykdant pirmą veiklą, organizuotas kaip mokymo kursai internetu | — |
| `nfeoera1` | `integer` | — | — | `open` | — | Naudojimasis internetiniais švietimo ištekliais vykdant pirmą švietimo veiklą | — |
| `nfeoerb1` | `integer` | — | — | `open` | — | Bendravimas su kitais asmenimis (pvz.mokytojais, studentais) naudojant švietimo interneto svetaines ir(arba) portalus, vykdant pirmą švietimo veiklą | — |
| `nfereason1_01a` | `integer` | — | — | `open` | — | Kad geriau atlikčiau darbą | — |
| `nfereason1_01b` | `integer` | — | — | `open` | — | Kad pagerinčiau savo karjeros perspektyvas | — |
| `nfereason1_02` | `integer` | — | — | `open` | — | Kad sumažinčiau galimybes netekti darbo | — |
| `nfereason1_03` | `integer` | — | — | `open` | — | Kad turėčiau daugiau galimybių gauti ar pakeisti darbą arba profesiją | — |
| `nfereason1_04` | `integer` | — | — | `open` | — | Kad galėčiau pradėti savo verslą | — |
| `nfereason1_13` | `integer` | — | — | `open` | — | Dėl organizacinių ir (arba) technologinių pokyčių darbe | — |
| `nfereason1_11` | `integer` | — | — | `open` | — | Reikalauja darbdavys arba yra teisiškai privalomas | — |
| `nfereason1_06` | `integer` | — | — | `open` | — | Kad įgyčiau kasdieniame gyvenime praversiančių žinių ir (arba) įgūdžių | — |
| `nfereason1_07` | `integer` | — | — | `open` | — | Kad gaučiau daugiau žinių ir (arba) ugdyčiau įgūdžius, susijusius su dominančiu dalyku | — |
| `nfereason1_08` | `integer` | — | — | `open` | — | Kad gaučiau pažymėjimą | — |
| `nfereason1_09` | `integer` | — | — | `open` | — | Kad susipažinčiau su naujais žmonėmis ir (arba) smagiai praleisčiau laiką | — |
| `nfereason1_10` | `integer` | — | — | `open` | — | Dėl sveikatos | — |
| `nfereason1_12` | `integer` | — | — | `open` | — | Kad geriau atlikčiau savanorišką darbą | — |
| `nfereason1` | `integer` | — | — | `open` | — | Dalyvavimo pirmoje švietimo veikloje priežastys: | — |
| `nfeprovider1` | `integer` | — | — | `open` | — | Pirmos mokymo veiklos paslaugų teikėjas | — |
| `nfecert1` | `integer` | — | — | `open` | — | Pirmos veiklos baigimo pažymėjimas | — |
| `nfepaid1` | `integer` | — | — | `open` | — | Mokesčiai už mokslą, registraciją, egzaminus, išlaidos knygoms ar techninėms mokymosi priemonėms | — |
| `nfepaidby1_1` | `integer` | — | — | `open` | — | Esamas ar būsimas darbdavys | — |
| `nfepaidby1_2` | `integer` | — | — | `open` | — | Valstybės užimtumo tarnybos | — |
| `nfepaidby1_3` | `integer` | — | — | `open` | — | Kitos valstybės institucijos | — |
| `nfepaidby1_4` | `integer` | — | — | `open` | — | Namų ūkio narys ar giminaitis | — |
| `nfepaidby1` | `integer` | — | — | `open` | — | Dalies išlaidų arba visų išlaidų už pirmos veiklos mokslą, registraciją, egzaminus, knygas ar technines mokymosi priemones apmokėjimas | — |
| `nfeusea1` | `integer` | — | — | `open` | — | Įgūdžių ar žinių, įgytų dalyvaujant pirmoje veikloje, dabartinis naudojimas | — |
| `nfeuseb1` | `integer` | — | — | `open` | — | Įgūdžių ar žinių, įgytų dalyvaujant pirmoje mokymo veikloje, tikėtinas naudojimas | — |
| `nfeoutcome1_1` | `integer` | — | — | `open` | — | Naujas darbas | — |
| `nfeoutcome1_3` | `integer` | — | — | `open` | — | Didesnis darbo užmokestis | — |
| `nfeoutcome1_2` | `integer` | — | — | `open` | — | Paaukštinimas | — |
| `nfeoutcome1_4` | `integer` | — | — | `open` | — | Naujos užduotys | — |
| `nfeoutcome1_5` | `integer` | — | — | `open` | — | Geresni darbo rezultatai | — |
| `nfeoutcome1_6` | `integer` | — | — | `open` | — | Asmeninės priežastys (susipažino su naujais žmonėmis, atnaujino bendruosius gebėjimus, kt.) | — |
| `nfeoutcome1_7` | `integer` | — | — | `open` | — | Kol kas jokių rezultatų | — |
| `nfeoutcome1` | `integer` | — | — | `open` | — | Rezultatai, susiję su naujais įgūdžiais ir (arba) žiniomis, įgytomis dalyvaujant pirmoje mokymo veikloje | — |
| `nferand2` | `integer` | — | — | `open` | — | Antros atsitiktinai atrinktos mokymo veiklos kodas | — |
| `nferand2_type` | `integer` | — | — | `open` | — | — | — |
| `nfefield2` | `integer` | — | — | `open` | — | — | — |
| `nfedist2` | `integer` | — | — | `open` | — | — | — |
| `nfedistol2` | `integer` | — | — | `open` | — | — | — |
| `nfeoera2` | `integer` | — | — | `open` | — | — | — |
| `nfeoerb2` | `integer` | — | — | `open` | — | — | — |
| `nfereason2_01a` | `integer` | — | — | `open` | — | — | — |
| `nfereason2_01b` | `integer` | — | — | `open` | — | — | — |
| `nfereason2_02` | `integer` | — | — | `open` | — | — | — |
| `nfereason2_03` | `integer` | — | — | `open` | — | — | — |
| `nfereason2_04` | `integer` | — | — | `open` | — | — | — |
| `nfereason2_13` | `integer` | — | — | `open` | — | — | — |
| `nfereason2_11` | `integer` | — | — | `open` | — | — | — |
| `nfereason2_06` | `integer` | — | — | `open` | — | — | — |
| `nfereason2_07` | `integer` | — | — | `open` | — | — | — |
| `nfereason2_08` | `integer` | — | — | `open` | — | — | — |
| `nfereason2_09` | `integer` | — | — | `open` | — | — | — |
| `nfereason2_10` | `integer` | — | — | `open` | — | — | — |
| `nfereason2_12` | `integer` | — | — | `open` | — | — | — |
| `nfereason2` | `integer` | — | — | `open` | — | — | — |
| `nfeprovider2` | `integer` | — | — | `open` | — | — | — |
| `nfecert2` | `integer` | — | — | `open` | — | — | — |
| `nfepaid2` | `integer` | — | — | `open` | — | — | — |
| `nfepaidby2_1` | `integer` | — | — | `open` | — | — | — |
| `nfepaidby2_2` | `integer` | — | — | `open` | — | — | — |
| `nfepaidby2_3` | `integer` | — | — | `open` | — | — | — |
| `nfepaidby2_4` | `integer` | — | — | `open` | — | — | — |
| `nfepaidby2` | `integer` | — | — | `open` | — | — | — |
| `nfeusea2` | `integer` | — | — | `open` | — | — | — |
| `nfeuseb2` | `integer` | — | — | `open` | — | — | — |
| `nfeoutcome2_1` | `integer` | — | — | `open` | — | — | — |
| `nfeoutcome2_3` | `integer` | — | — | `open` | — | — | — |
| `nfeoutcome2_2` | `integer` | — | — | `open` | — | — | — |
| `nfeoutcome2_4` | `integer` | — | — | `open` | — | — | — |
| `nfeoutcome2_5` | `integer` | — | — | `open` | — | — | — |
| `nfeoutcome2_6` | `integer` | — | — | `open` | — | — | — |
| `nfeoutcome2_7` | `integer` | — | — | `open` | — | — | — |
| `nfeoutcome2` | `integer` | — | — | `open` | — | — | — |
| `difficulty` | `integer` | — | — | `open` | — | Sunkumai, patirti dalyvaujant formaliojo ar neformaliojo švietimo veikloje per pastaruosius 12 mėn. | — |
| `need` | `integer` | — | — | `open` | — | Nėra poreikio toliau mokytis | — |
| `difftype_01` | `integer` | — | — | `open` | — | Nebuvo tinkamų sąlygų, sugebėjimų | — |
| `difftype_02` | `integer` | — | — | `open` | — | Mokymo kursų kaina (mokymasis per brangus) | — |
| `difftype_03` | `integer` | — | — | `open` | — | Nėra darbdavio ar valstybės tarnybų paramos | — |
| `difftype_04` | `integer` | — | — | `open` | — | Mokymosi ir darbo laiko tvarkaraščio nesuderinamumas | — |
| `difftype_05` | `integer` | — | — | `open` | — | Nuotolis iki mokymosį vietos | — |
| `difftype_06` | `integer` | — | — | `open` | — | Nėra galimybės naudotis kompiuteriu ar internetu | — |
| `difftype_07` | `integer` | — | — | `open` | — | Pareigos šeimoje | — |
| `difftype_08a` | `integer` | — | — | `open` | — | Neleido sveikata | — |
| `difftype_08b` | `integer` | — | — | `open` | — | Trukdė amžius | — |
| `difftype_09` | `integer` | — | — | `open` | — | Kitos asmeninės priežastys | — |
| `difftype_10` | `integer` | — | — | `open` | — | Nėra tinkamų mokymų | — |
| `difftype_12` | `integer` | — | — | `open` | — | Neigiama ankstesnio mokymosi patirtis | — |
| `difftype` | `integer` | — | — | `open` | — | Priežastys, dėl kurių nesimokė | — |
| `diffmain` | `string` | — | — | `open` | — | Pagrindinė priežastis (didžiausias sunkumas) | — |
| `inffamily` | `integer` | — | — | `open` | — | Mokomasi iš šeimos nario, draugo ar bendradarbio | — |
| `infmaterial` | `integer` | — | — | `open` | — | Mokomasi naudojant spausdintą medžiagą (knygas, specialybės žurnalus, kt.) | — |
| `infcomputer` | `integer` | — | — | `open` | — | Mokomasi naudojantis kompiuteriu ir(arba) internetu | — |
| `infmedia` | `integer` | — | — | `open` | — | Mokomasi naudojantis televizija, radiju, vaizdo medžiaga | — |
| `infmuseum` | `integer` | — | — | `open` | — | Mokomasi lankantis su gidu muziejuose, istoriniuose, gamtos objektuose | — |
| `inflibraries` | `integer` | — | — | `open` | — | Mokomasi lankantis bibliotekose, kultūros ir mokymo centruose ir pan. | — |
| `inf` | `integer` | — | — | `open` | — | Mokėsi savarankiškai | — |
| `langmother1` | `integer` | — | — | `open` | — | Gimtoji (-osios) kalba (-os) | — |
| `langmother2` | `integer` | — | — | `open` | — | — | — |
| `langused` | `integer` | — | — | `open` | — | Kitos kalbos, kurias moka (išskyrus gimtąją kalbą) | — |
| `langused_1` | `string` | — | — | `open` | — | Pirmos kalbos kodas | — |
| `langused_2` | `string` | — | — | `open` | — | Antros kalbos kodas | — |
| `langused_3` | `string` | — | — | `open` | — | Trečios kalbos kodas | — |
| `langused_4` | `string` | — | — | `open` | — | Ketvirtos kalbos kodas | — |
| `langused_5` | `string` | — | — | `open` | — | Penktos kalbos kodas | — |
| `langused_6` | `string` | — | — | `open` | — | Šeštos kalbos kodas | — |
| `langused_7` | `string` | — | — | `open` | — | Septintos kalbos kodas | — |
| `langbest1` | `string` | — | — | `open` | — | Pirma geriausiai mokama kalba (išskyrus gimtąją kalbą) | — |
| `langlevel1` | `integer` | — | — | `open` | — | Pirmos geriausiai mokamos kalbos mokėjimas (išskyrus gimtąją kalbą) | — |
| `langbest2` | `string` | — | — | `open` | — | Antra geriausiai mokama kalba (išskyrus gimtąją kalbą) | — |
| `langlevel2` | `integer` | — | — | `open` | — | Antros geriausiai mokamos kalbos mokėjimas (išskyrus gimtąją kalbą) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `deg_urb` | `1` | — | — | Tankiai apgyvendinta vietovė | — |
| `deg_urb` | `2` | — | — | Vidutiniškai apgyvendinta vietovė | — |
| `deg_urb` | `3` | — | — | Retai apgyvendinta vietovė | — |
| `vietove` | `1` | — | — | Miestas | — |
| `vietove` | `2` | — | — | Kaimas | — |
| `hhtype` | `10` | — | — | Vieno asmens namų ūkis | — |
| `hhtype` | `21` | — | — | Vieniša motina ar vienišas tėvas su vaiku (-ais), jaunesniu (-iais) nei 25 m. | — |
| `hhtype` | `22` | — | — | Pora, neturinti vaiko (-ų), jaunesnio (-ių) nei 25 m. | — |
| `hhtype` | `23` | — | — | Pora su vaiku (-ais), jaunesniu (-iais) nei 25 m. | — |
| `hhtype` | `24` | — | — | Pora arba vieniša motina ar vienišas tėvas, su vaiku (-ais), jaunesniu (-iais) nei 25 m., ir kitais kartu namų ūkyje gyvenančiais asmenimis | — |
| `hhtype` | `30` | — | — | Kita | — |
| `hhincome` | `1` | — | — | Mažesnės nei pirmojo kvintilio | — |
| `hhincome` | `2` | — | — | Tarp pirmojo ir antrojo kvintilių | — |
| `hhincome` | `3` | — | — | Tarp antrojo ir trečiojo kvintilių | — |
| `hhincome` | `4` | — | — | Tarp trečiojo ir ketvirtojo kvintilių | — |
| `hhincome` | `5` | — | — | Didesnės nei 4 kvintilio | — |
| `sex` | `1` | — | — | Vyras | — |
| `sex` | `2` | — | — | Moteris | — |
| `age` | `1` | — | — | 25–34 metų amžius | — |
| `age` | `2` | — | — | 35–54 metų amžius | — |
| `age` | `3` | — | — | 55 metų ir vyresnio amžiaus | — |
| `citizen` | `0` | — | — | Lietuvos pilietybė | — |
| `citizen` | `1` | — | — | Kitos šalies pilietybė | — |
| `birthplace` | `0` | — | — | Lietuva | — |
| `birthplace` | `1` | — | — | Kita šalis | — |
| `restime` | `1` | — | — | Gyvena Lietuvoje iki 10 metų | — |
| `restime` | `2` | — | — | Gyvena Lietuvoje 11 metų ir ilgiau | — |
| `restime` | `-2` | — | — | Gimė Lietuvoje | — |
| `marstadefacto` | `1` | — | — | Gyvenate poroje įregistravę ar neįregistravę santuokos | — |
| `marstadefacto` | `2` | — | — | Gyvenate vienas ar su kitais asmenimis, bet ne poroje | — |
| `marstadefacto` | `-1` | — | — | Nėra atsakymo | — |
| `hatlevel` | `0` | — | — | Jokio formaliojo išsilavinimo arba žemesnis nei ISCED 1 išsilavinimas | — |
| `hatlevel` | `1` | — | — | Žemesnis išsilavinimas (ISCED 1-2) | — |
| `hatlevel` | `2` | — | — | Vidutinis išsilavinimas (ISCED 3-4) | — |
| `hatlevel` | `3` | — | — | Aukščiausias išsilavinimas (ISCED 6-8) | — |
| `hatfield` | `0` | — | — | Pagrindinės programos ir kvalifikacijos | — |
| `hatfield` | `1` | — | — | Švietimas | — |
| `hatfield` | `2` | — | — | Menai ir humanitariniai mokslai | — |
| `hatfield` | `3` | — | — | Socialiniai mokslai, žurnalistika ir informacija | — |
| `hatfield` | `4` | — | — | Verslas, administravimas ir teisė | — |
| `hatfield` | `5` | — | — | Gamtos mokslai, matematika ir statistika | — |
| `hatfield` | `6` | — | — | Informacijos ir ryšio technologijos | — |
| `hatfield` | `7` | — | — | Inžinerija, gamyba ir statyba | — |
| `hatfield` | `8` | — | — | Žemės ūkis, miškininkystė, žuvininkystė ir veterinarija | — |
| `hatfield` | `9` | — | — | Sveikatos priežiūra ir socialinė gerovė | — |
| `hatfield` | `10` | — | — | Paslaugos | — |
| `hatfield` | `-2` | — | — | Netaikoma | — |
| `hatvoc` | `1` | — | — | Bendrasis lavinimas | — |
| `hatvoc` | `2` | — | — | Profesinis mokymas | — |
| `hatvoc` | `-2` | — | — | Netaikoma | — |
| `dropeduc` | `1` | — | — | Taip | — |
| `dropeduc` | `2` | — | — | Ne | — |
| `dropeduc` | `-2` | — | — | Netaikoma | — |
| `dropeduclevel` | `2` | — | — | Vidutinis išsilavinimas (ISCED 3-4) | — |
| `dropeduclevel` | `3` | — | — | Aukščiausias išsilavinimas (ISCED 6-8) | — |
| `dropeduclevel` | `-2` | — | — | Netaikoma | — |
| `dropeducvoc` | `1` | — | — | Bendrasis lavinimas | — |
| `dropeducvoc` | `2` | — | — | Profesinis mokymas | — |
| `dropeducvoc` | `-2` | — | — | Netaikoma | — |
| `mainstat` | `1` | — | — | Užimtasis | — |
| `mainstat` | `2` | — | — | Bedarbis | — |
| `mainstat` | `3` | — | — | Neaktyvus asmuo | — |
| `emp12m` | `1` | — | — | Taip | — |
| `emp12m` | `2` | — | — | Ne | — |
| `emp12m` | `-2` | — | — | Netaikoma | — |
| `jobstat` | `11` | — | — | Savarankiškai dirbantis asmuo, samdantis darbuotojus | — |
| `jobstat` | `12` | — | — | Savarankiškai dirbantis asmuo, nesamdantis darbuotojų | — |
| `jobstat` | `21` | — | — | Nuolatinis arba pagal neterminuotą darbo sutartį dirbantis samdomasis darbuotojas | — |
| `jobstat` | `22` | — | — | Laikinas arba pagal terminuotą darbo sutartį dirbantis samdomasis darbuotojas | — |
| `jobstat` | `30` | — | — | Šeimos darbuotojas | — |
| `jobstat` | `-2` | — | — | Netaikoma | — |
| `locsizefirm` | `1` | — | — | 1–9 asmenys | — |
| `locsizefirm` | `2` | — | — | 10–49 asmenų | — |
| `locsizefirm` | `3` | — | — | 50–249 asmenys | — |
| `locsizefirm` | `4` | — | — | 250 ar daugiau asmenų | — |
| `locsizefirm` | `7` | — | — | Tiksliai nežinau, bet ne mažiau kaip 10 asmenų | — |
| `locsizefirm` | `-2` | — | — | Netaikoma | — |
| `hatfather` | `1` | — | — | Žemesnis išsilavinimas (ISCED 0-2) | — |
| `hatfather` | `2` | — | — | Vidutinis išsilavinimas (ISCED 3-4) | — |
| `hatfather` | `3` | — | — | Aukščiausias išsilavinimas (ISCED 6-8) | — |
| `hatfather` | `-1` | — | — | Nėra atsakymo | — |
| `hatfather` | `-2` | — | — | Netaikoma (tėvas nežinomas) | — |
| `hatmother` | `1` | — | — | Žemesnis išsilavinimas (ISCED 0-2) | — |
| `hatmother` | `2` | — | — | Vidutinis išsilavinimas (ISCED 3-4) | — |
| `hatmother` | `3` | — | — | Aukščiausias išsilavinimas (ISCED 6-8) | — |
| `hatmother` | `-1` | — | — | Nėra atsakymo | — |
| `hatmother` | `-2` | — | — | Netaikoma (motina nežinoma) | — |
| `birthfather` | `0` | — | — | Gimė Lietuvoje | — |
| `birthfather` | `1` | — | — | Gimė ne Lietuvoje | — |
| `birthfather` | `-2` | — | — | Netaikoma (tėvas nežinomas) | — |
| `birthmother` | `0` | — | — | Gimė Lietuvoje | — |
| `birthmother` | `1` | — | — | Gimė ne Lietuvoje | — |
| `birthmother` | `-2` | — | — | Netaikoma (motina nežinoma) | — |
| `fed` | `1` | — | — | Taip | — |
| `fed` | `2` | — | — | Ne | — |
| `fedlevel` | `1` | — | — | Žemesnis išsilavinimas (ISCED 1-2) | — |
| `fedlevel` | `2` | — | — | Vidutinis išsilavinimas (ISCED 3-4) | — |
| `fedlevel` | `3` | — | — | Aukščiausias išsilavinimas (ISCED 6-8) | — |
| `fedlevel` | `-2` | — | — | Netaikoma | — |
| `seekinfo` | `1` | — | — | Taip | — |
| `seekinfo` | `2` | — | — | Ne | — |
| `guideinst_1` | `1` | — | — | Taip | — |
| `guideinst_1` | `2` | — | — | Ne | — |
| `guideinst_2` | `1` | — | — | Taip | — |
| `guideinst_2` | `2` | — | — | Ne | — |
| `guideinst_3` | `1` | — | — | Taip | — |
| `guideinst_3` | `2` | — | — | Ne | — |
| `guidesource_1` | `1` | — | — | Pasirinkta | — |
| `guidesource_1` | `2` | — | — | Nepasirinkta | — |
| `guidesource_1` | `-2` | — | — | Netaikoma | — |
| `guidesource_2` | `1` | — | — | Pasirinkta | — |
| `guidesource_2` | `2` | — | — | Nepasirinkta | — |
| `guidesource_2` | `-2` | — | — | Netaikoma | — |
| `guidesource_3` | `1` | — | — | Pasirinkta | — |
| `guidesource_3` | `2` | — | — | Nepasirinkta | — |
| `guidesource_3` | `-2` | — | — | Netaikoma | — |
| `guidesource_4` | `1` | — | — | Pasirinkta | — |
| `guidesource_4` | `2` | — | — | Nepasirinkta | — |
| `guidesource_4` | `-2` | — | — | Netaikoma | — |
| `guidesource_5` | `1` | — | — | Pasirinkta | — |
| `guidesource_5` | `2` | — | — | Nepasirinkta | — |
| `guidesource_5` | `-2` | — | — | Netaikoma | — |
| `guidesource` | `1` | — | — | Atsakymas pasirinktas | — |
| `guidesource` | `-2` | — | — | Netaikoma | — |
| `guidetype_1` | `1` | — | — | Pasirinkta | — |
| `guidetype_1` | `2` | — | — | Nepasirinkta | — |
| `guidetype_1` | `-2` | — | — | Netaikoma | — |
| `guidetype_2` | `1` | — | — | Pasirinkta | — |
| `guidetype_2` | `2` | — | — | Nepasirinkta | — |
| `guidetype_2` | `-2` | — | — | Netaikoma | — |
| `guidetype_3` | `1` | — | — | Pasirinkta | — |
| `guidetype_3` | `2` | — | — | Nepasirinkta | — |
| `guidetype_3` | `-2` | — | — | Netaikoma | — |
| `guidetype_4` | `1` | — | — | Pasirinkta | — |
| `guidetype_4` | `2` | — | — | Nepasirinkta | — |
| `guidetype_4` | `-2` | — | — | Netaikoma | — |
| `guidetype` | `1` | — | — | Atsakymas pasirinktas | — |
| `guidetype` | `-2` | — | — | Netaikoma | — |
| `guidemode_1` | `1` | — | — | Pasirinkta | — |
| `guidemode_1` | `2` | — | — | Nepasirinkta | — |
| `guidemode_1` | `-2` | — | — | Netaikoma | — |
| `guidemode_2` | `1` | — | — | Pasirinkta | — |
| `guidemode_2` | `2` | — | — | Nepasirinkta | — |
| `guidemode_2` | `-2` | — | — | Netaikoma | — |
| `guidemode_3` | `1` | — | — | Pasirinkta | — |
| `guidemode_3` | `2` | — | — | Nepasirinkta | — |
| `guidemode_3` | `-2` | — | — | Netaikoma | — |
| `guidemode_4` | `1` | — | — | Pasirinkta | — |
| `guidemode_4` | `2` | — | — | Nepasirinkta | — |
| `guidemode_4` | `-2` | — | — | Netaikoma | — |
| `guidemode` | `1` | — | — | Atsakymas pasirinktas | — |
| `guidemode` | `-2` | — | — | Netaikoma | — |
| `fedcomp` | `2` | — | — | Ne, ji tebevyksta | — |
| `fedcomp` | `3` | — | — | Taip, ją užbaigiau | — |
| `fedcomp` | `-2` | — | — | Netaikoma | — |
| `fedfield` | `0` | — | — | Pagrindinės programos ir kvalifikacijos | — |
| `fedfield` | `1` | — | — | Švietimas | — |
| `fedfield` | `2` | — | — | Menai ir humanitariniai mokslai | — |
| `fedfield` | `3` | — | — | Socialiniai mokslai, žurnalistika ir informacija | — |
| `fedfield` | `4` | — | — | Verslas, administravimas ir teisė | — |
| `fedfield` | `5` | — | — | Gamtos mokslai, matematika ir statistika | — |
| `fedfield` | `6` | — | — | Informacijos ir ryšio technologijos | — |
| `fedfield` | `7` | — | — | Inžinerija, gamyba ir statyba | — |
| `fedfield` | `8` | — | — | Žemės ūkis, miškininkystė, žuvininkystė ir veterinarija | — |
| `fedfield` | `9` | — | — | Sveikatos priežiūra ir socialinė gerovė | — |
| `fedfield` | `10` | — | — | Paslaugos | — |
| `fedfield` | `-2` | — | — | Netaikoma | — |
| `fedvoc` | `1` | — | — | Bendrasis lavinimas | — |
| `fedvoc` | `2` | — | — | Profesinis mokymas | — |
| `fedvoc` | `-2` | — | — | Netaikoma | — |
| `feddist` | `1` | — | — | Taip | — |
| `feddist` | `2` | — | — | Ne | — |
| `feddist` | `-2` | — | — | Netaikoma | — |
| `feddistol` | `1` | — | — | Taip | — |
| `feddistol` | `2` | — | — | Ne | — |
| `feddistol` | `-2` | — | — | Netaikoma | — |
| `fedoera` | `1` | — | — | Labai dažnai | — |
| `fedoera` | `2` | — | — | Dažnai | — |
| `fedoera` | `3` | — | — | Kartais | — |
| `fedoera` | `4` | — | — | Niekada | — |
| `fedoera` | `-2` | — | — | Netaikoma | — |
| `fedoerb` | `1` | — | — | Taip | — |
| `fedoerb` | `2` | — | — | Ne | — |
| `fedoerb` | `-2` | — | — | Netaikoma | — |
| `fedreason_01a` | `1` | — | — | Pasirinkta | — |
| `fedreason_01a` | `2` | — | — | Nepasirinkta | — |
| `fedreason_01a` | `-2` | — | — | Netaikoma | — |
| `fedreason_01b` | `1` | — | — | Pasirinkta | — |
| `fedreason_01b` | `2` | — | — | Nepasirinkta | — |
| `fedreason_01b` | `-2` | — | — | Netaikoma | — |
| `fedreason_02` | `1` | — | — | Pasirinkta | — |
| `fedreason_02` | `2` | — | — | Nepasirinkta | — |
| `fedreason_02` | `-2` | — | — | Netaikoma | — |
| `fedreason_03` | `1` | — | — | Pasirinkta | — |
| `fedreason_03` | `2` | — | — | Nepasirinkta | — |
| `fedreason_03` | `-2` | — | — | Netaikoma | — |
| `fedreason_04` | `1` | — | — | Pasirinkta | — |
| `fedreason_04` | `2` | — | — | Nepasirinkta | — |
| `fedreason_04` | `-2` | — | — | Netaikoma | — |
| `fedreason_05` | `1` | — | — | Pasirinkta | — |
| `fedreason_05` | `2` | — | — | Nepasirinkta | — |
| `fedreason_05` | `-2` | — | — | Netaikoma | — |
| `fedreason_06` | `1` | — | — | Pasirinkta | — |
| `fedreason_06` | `2` | — | — | Nepasirinkta | — |
| `fedreason_06` | `-2` | — | — | Netaikoma | — |
| `fedreason_07` | `1` | — | — | Pasirinkta | — |
| `fedreason_07` | `2` | — | — | Nepasirinkta | — |
| `fedreason_07` | `-2` | — | — | Netaikoma | — |
| `fedreason_08` | `1` | — | — | Pasirinkta | — |
| `fedreason_08` | `2` | — | — | Nepasirinkta | — |
| `fedreason_08` | `-2` | — | — | Netaikoma | — |
| `fedreason_09` | `1` | — | — | Pasirinkta | — |
| `fedreason_09` | `2` | — | — | Nepasirinkta | — |
| `fedreason_09` | `-2` | — | — | Netaikoma | — |
| `fedreason` | `1` | — | — | Atsakymas pasirinktas | — |
| `fedreason` | `-2` | — | — | Netaikoma | — |
| `fedworktime` | `1` | — | — | Tik darbo valandomis, už kurias mokamas atlygis | — |
| `fedworktime` | `2` | — | — | Daugiausia darbo valandomis, už kurias mokamas atlygis | — |
| `fedworktime` | `3` | — | — | Daugiausia po darbo valandų, už kurias mokamas atlygis | — |
| `fedworktime` | `4` | — | — | Tik po darbo valandų, už kurias mokamas atlygis | — |
| `fedworktime` | `5` | — | — | Tuo metu nedirbo | — |
| `fedworktime` | `-2` | — | — | Netaikoma | — |
| `fedpaid` | `1` | — | — | Viską apmokėjo respondentas | — |
| `fedpaid` | `2` | — | — | Iš dalies apmokėjo respondentas, o dalį – kitas asmuo | — |
| `fedpaid` | `3` | — | — | Viską apmokėjo kitas asmuo | — |
| `fedpaid` | `4` | — | — | Nemokama veikla | — |
| `fedpaid` | `5` | — | — | Nežinoma | — |
| `fedpaid` | `-2` | — | — | Netaikoma | — |
| `fedpaidby_1` | `1` | — | — | Pasirinkta | — |
| `fedpaidby_1` | `2` | — | — | Nepasirinkta | — |
| `fedpaidby_1` | `-2` | — | — | Netaikoma | — |
| `fedpaidby_2` | `1` | — | — | Pasirinkta | — |
| `fedpaidby_2` | `2` | — | — | Nepasirinkta | — |
| `fedpaidby_2` | `-2` | — | — | Netaikoma | — |
| `fedpaidby_3` | `1` | — | — | Pasirinkta | — |
| `fedpaidby_3` | `2` | — | — | Nepasirinkta | — |
| `fedpaidby_3` | `-2` | — | — | Netaikoma | — |
| `fedpaidby_4` | `1` | — | — | Pasirinkta | — |
| `fedpaidby_4` | `2` | — | — | Nepasirinkta | — |
| `fedpaidby_4` | `-2` | — | — | Netaikoma | — |
| `fedpaidby` | `1` | — | — | Atsakymas pasirinktas | — |
| `fedpaidby` | `-2` | — | — | Netaikoma | — |
| `fedusea` | `1` | — | — | Labai didelis | — |
| `fedusea` | `2` | — | — | Pakankamas | — |
| `fedusea` | `3` | — | — | Labai mažas | — |
| `fedusea` | `-2` | — | — | Netaikoma | — |
| `feduseb` | `1` | — | — | Labai didelis | — |
| `feduseb` | `2` | — | — | Pakankamas | — |
| `feduseb` | `3` | — | — | Labai mažas | — |
| `feduseb` | `-2` | — | — | Netaikoma | — |
| `fedoutcome_1` | `1` | — | — | Pasirinkta | — |
| `fedoutcome_1` | `2` | — | — | Nepasirinkta | — |
| `fedoutcome_1` | `-2` | — | — | Netaikoma | — |
| `fedoutcome_3` | `1` | — | — | Pasirinkta | — |
| `fedoutcome_3` | `2` | — | — | Nepasirinkta | — |
| `fedoutcome_3` | `-2` | — | — | Netaikoma | — |
| `fedoutcome_2` | `1` | — | — | Pasirinkta | — |
| `fedoutcome_2` | `2` | — | — | Nepasirinkta | — |
| `fedoutcome_2` | `-2` | — | — | Netaikoma | — |
| `fedoutcome_4` | `1` | — | — | Pasirinkta | — |
| `fedoutcome_4` | `2` | — | — | Nepasirinkta | — |
| `fedoutcome_4` | `-2` | — | — | Netaikoma | — |
| `fedoutcome_5` | `1` | — | — | Pasirinkta | — |
| `fedoutcome_5` | `2` | — | — | Nepasirinkta | — |
| `fedoutcome_5` | `-2` | — | — | Netaikoma | — |
| `fedoutcome_6` | `1` | — | — | Pasirinkta | — |
| `fedoutcome_6` | `2` | — | — | Nepasirinkta | — |
| `fedoutcome_6` | `-2` | — | — | Netaikoma | — |
| `fedoutcome_7` | `1` | — | — | Pasirinkta | — |
| `fedoutcome_7` | `2` | — | — | Nepasirinkta | — |
| `fedoutcome_7` | `-2` | — | — | Netaikoma | — |
| `fedoutcome` | `1` | — | — | Atsakymas pasirinktas | — |
| `fedoutcome` | `-2` | — | — | Netaikoma | — |
| `nfecourse` | `1` | — | — | Taip | — |
| `nfecourse` | `2` | — | — | Ne | — |
| `nfeworkshop` | `1` | — | — | Taip | — |
| `nfeworkshop` | `2` | — | — | Ne | — |
| `nfeguidedjt` | `1` | — | — | Taip | — |
| `nfeguidedjt` | `2` | — | — | Ne | — |
| `nfelesson` | `1` | — | — | Taip | — |
| `nfelesson` | `2` | — | — | Ne | — |
| `nfeact01_type` | `1` | — | — | Kvalifikacijos tobulinimo kursai | — |
| `nfeact01_type` | `2` | — | — | Praktiniai ir teoriniai seminarai | — |
| `nfeact01_type` | `3` | — | — | Mokymas darbo vietoje | — |
| `nfeact01_type` | `4` | — | — | Privačios pamokos | — |
| `nfeact01_type` | `-2` | — | — | Netaikoma | — |
| `nfeact01_purp` | `1` | — | — | Daugiausia susijęs su darbu | — |
| `nfeact01_purp` | `2` | — | — | Daugiausia susijęs su asmeninėmis ir (arba) su darbu nesusijusiomis priežastimis | — |
| `nfeact01_purp` | `-2` | — | — | Netaikoma | — |
| `nfeact01_worktime` | `1` | — | — | Taip | — |
| `nfeact01_worktime` | `2` | — | — | Ne (įskaitant, jei tuo metu nedirbo) | — |
| `nfeact01_worktime` | `-2` | — | — | Netaikoma | — |
| `nfeact01_paidby` | `1` | — | — | Taip | — |
| `nfeact01_paidby` | `2` | — | — | Ne (įskaitant, jei tuo metu nedirbo) | — |
| `nfeact01_paidby` | `-2` | — | — | Netaikoma | — |
| `nfeact02_type` | `1` | — | — | Kvalifikacijos tobulinimo kursai | — |
| `nfeact02_type` | `2` | — | — | Praktiniai ir teoriniai seminarai | — |
| `nfeact02_type` | `3` | — | — | Mokymas darbo vietoje | — |
| `nfeact02_type` | `4` | — | — | Privačios pamokos | — |
| `nfeact02_type` | `-2` | — | — | Netaikoma | — |
| `nfeact02_purp` | `1` | — | — | Daugiausia susijęs su darbu | — |
| `nfeact02_purp` | `2` | — | — | Daugiausia susijęs su asmeninėmis ir (arba) su darbu nesusijusiomis priežastimis | — |
| `nfeact02_purp` | `-2` | — | — | Netaikoma | — |
| `nfeact02_worktime` | `1` | — | — | Taip | — |
| `nfeact02_worktime` | `2` | — | — | Ne (įskaitant, jei tuo metu nedirbo) | — |
| `nfeact02_worktime` | `-2` | — | — | Netaikoma | — |
| `nfeact02_paidby` | `1` | — | — | Taip | — |
| `nfeact02_paidby` | `2` | — | — | Ne (įskaitant, jei tuo metu nedirbo) | — |
| `nfeact02_paidby` | `-2` | — | — | Netaikoma | — |
| `nfeact03_type` | `1` | — | — | Kvalifikacijos tobulinimo kursai | — |
| `nfeact03_type` | `2` | — | — | Praktiniai ir teoriniai seminarai | — |
| `nfeact03_type` | `3` | — | — | Mokymas darbo vietoje | — |
| `nfeact03_type` | `4` | — | — | Privačios pamokos | — |
| `nfeact03_type` | `-2` | — | — | Netaikoma | — |
| `nfeact03_purp` | `1` | — | — | Daugiausia susijęs su darbu | — |
| `nfeact03_purp` | `2` | — | — | Daugiausia susijęs su asmeninėmis ir (arba) su darbu nesusijusiomis priežastimis | — |
| `nfeact03_purp` | `-2` | — | — | Netaikoma | — |
| `nfeact03_worktime` | `1` | — | — | Taip | — |
| `nfeact03_worktime` | `2` | — | — | Ne (įskaitant, jei tuo metu nedirbo) | — |
| `nfeact03_worktime` | `-2` | — | — | Netaikoma | — |
| `nfeact03_paidby` | `1` | — | — | Taip | — |
| `nfeact03_paidby` | `2` | — | — | Ne (įskaitant, jei tuo metu nedirbo) | — |
| `nfeact03_paidby` | `-2` | — | — | Netaikoma | — |
| `nfeact04_type` | `1` | — | — | Kvalifikacijos tobulinimo kursai | — |
| `nfeact04_type` | `2` | — | — | Praktiniai ir teoriniai seminarai | — |
| `nfeact04_type` | `3` | — | — | Mokymas darbo vietoje | — |
| `nfeact04_type` | `4` | — | — | Privačios pamokos | — |
| `nfeact04_type` | `-2` | — | — | Netaikoma | — |
| `nfeact04_purp` | `1` | — | — | Daugiausia susijęs su darbu | — |
| `nfeact04_purp` | `2` | — | — | Daugiausia susijęs su asmeninėmis ir (arba) su darbu nesusijusiomis priežastimis | — |
| `nfeact04_purp` | `-2` | — | — | Netaikoma | — |
| `nfeact04_worktime` | `1` | — | — | Taip | — |
| `nfeact04_worktime` | `2` | — | — | Ne (įskaitant, jei tuo metu nedirbo) | — |
| `nfeact04_worktime` | `-2` | — | — | Netaikoma | — |
| `nfeact04_paidby` | `1` | — | — | Taip | — |
| `nfeact04_paidby` | `2` | — | — | Ne (įskaitant, jei tuo metu nedirbo) | — |
| `nfeact04_paidby` | `-2` | — | — | Netaikoma | — |
| `nfeact05_type` | `1` | — | — | Kvalifikacijos tobulinimo kursai | — |
| `nfeact05_type` | `2` | — | — | Praktiniai ir teoriniai seminarai | — |
| `nfeact05_type` | `3` | — | — | Mokymas darbo vietoje | — |
| `nfeact05_type` | `4` | — | — | Privačios pamokos | — |
| `nfeact05_type` | `-2` | — | — | Netaikoma | — |
| `nfeact05_purp` | `1` | — | — | Daugiausia susijęs su darbu | — |
| `nfeact05_purp` | `2` | — | — | Daugiausia susijęs su asmeninėmis ir (arba) su darbu nesusijusiomis priežastimis | — |
| `nfeact05_purp` | `-2` | — | — | Netaikoma | — |
| `nfeact05_worktime` | `1` | — | — | Taip | — |
| `nfeact05_worktime` | `2` | — | — | Ne (įskaitant, jei tuo metu nedirbo) | — |
| `nfeact05_worktime` | `-2` | — | — | Netaikoma | — |
| `nfeact05_paidby` | `1` | — | — | Taip | — |
| `nfeact05_paidby` | `2` | — | — | Ne (įskaitant, jei tuo metu nedirbo) | — |
| `nfeact05_paidby` | `-2` | — | — | Netaikoma | — |
| `nfeact06_type` | `1` | — | — | Kvalifikacijos tobulinimo kursai | — |
| `nfeact06_type` | `2` | — | — | Praktiniai ir teoriniai seminarai | — |
| `nfeact06_type` | `3` | — | — | Mokymas darbo vietoje | — |
| `nfeact06_type` | `4` | — | — | Privačios pamokos | — |
| `nfeact06_type` | `-2` | — | — | Netaikoma | — |
| `nfeact06_purp` | `1` | — | — | Daugiausia susijęs su darbu | — |
| `nfeact06_purp` | `2` | — | — | Daugiausia susijęs su asmeninėmis ir (arba) su darbu nesusijusiomis priežastimis | — |
| `nfeact06_purp` | `-2` | — | — | Netaikoma | — |
| `nfeact06_worktime` | `1` | — | — | Taip | — |
| `nfeact06_worktime` | `2` | — | — | Ne (įskaitant, jei tuo metu nedirbo) | — |
| `nfeact06_worktime` | `-2` | — | — | Netaikoma | — |
| `nfeact06_paidby` | `1` | — | — | Taip | — |
| `nfeact06_paidby` | `2` | — | — | Ne (įskaitant, jei tuo metu nedirbo) | — |
| `nfeact06_paidby` | `-2` | — | — | Netaikoma | — |
| `nfeact07_type` | `1` | — | — | Kvalifikacijos tobulinimo kursai | — |
| `nfeact07_type` | `2` | — | — | Praktiniai ir teoriniai seminarai | — |
| `nfeact07_type` | `3` | — | — | Mokymas darbo vietoje | — |
| `nfeact07_type` | `4` | — | — | Privačios pamokos | — |
| `nfeact07_type` | `-2` | — | — | Netaikoma | — |
| `nfeact07_pur` | `1` | — | — | Daugiausia susijęs su darbu | — |
| `nfeact07_pur` | `2` | — | — | Daugiausia susijęs su asmeninėmis ir (arba) su darbu nesusijusiomis priežastimis | — |
| `nfeact07_pur` | `-2` | — | — | Netaikoma | — |
| `nfeact07_worktime` | `1` | — | — | Taip | — |
| `nfeact07_worktime` | `2` | — | — | Ne (įskaitant, jei tuo metu nedirbo) | — |
| `nfeact07_worktime` | `-2` | — | — | Netaikoma | — |
| `nfeact07_paidby` | `1` | — | — | Taip | — |
| `nfeact07_paidby` | `2` | — | — | Ne (įskaitant, jei tuo metu nedirbo) | — |
| `nfeact07_paidby` | `-2` | — | — | Netaikoma | — |
| `nferand1_type` | `1` | — | — | Kvalifikacijos tobulinimo kursai | — |
| `nferand1_type` | `2` | — | — | Praktiniai ir teoriniai seminarai | — |
| `nferand1_type` | `3` | — | — | Mokymas darbo vietoje | — |
| `nferand1_type` | `4` | — | — | Privačios pamokos | — |
| `nferand1_type` | `-2` | — | — | Netaikoma | — |
| `nfefield1` | `0` | — | — | Pagrindinės programos ir kvalifikacijos | — |
| `nfefield1` | `1` | — | — | Švietimas | — |
| `nfefield1` | `2` | — | — | Menai ir humanitariniai mokslai | — |
| `nfefield1` | `3` | — | — | Socialiniai mokslai, žurnalistika ir informacija | — |
| `nfefield1` | `4` | — | — | Verslas, administravimas ir teisė | — |
| `nfefield1` | `5` | — | — | Gamtos mokslai, matematika ir statistika | — |
| `nfefield1` | `6` | — | — | Informacijos ir ryšio technologijos | — |
| `nfefield1` | `7` | — | — | Inžinerija, gamyba ir statyba | — |
| `nfefield1` | `8` | — | — | Žemės ūkis, miškininkystė, žuvininkystė ir veterinarija | — |
| `nfefield1` | `9` | — | — | Sveikatos priežiūra ir socialinė gerovė | — |
| `nfefield1` | `10` | — | — | Paslaugos | — |
| `nfefield1` | `-2` | — | — | Netaikoma | — |
| `nfedist1` | `1` | — | — | Taip | — |
| `nfedist1` | `2` | — | — | Ne | — |
| `nfedist1` | `-2` | — | — | Netaikoma | — |
| `nfedistol1` | `1` | — | — | Taip | — |
| `nfedistol1` | `2` | — | — | Ne | — |
| `nfedistol1` | `-2` | — | — | Netaikoma | — |
| `nfeoera1` | `1` | — | — | Taip | — |
| `nfeoera1` | `2` | — | — | Ne | — |
| `nfeoera1` | `-2` | — | — | Netaikoma | — |
| `nfeoerb1` | `1` | — | — | Taip | — |
| `nfeoerb1` | `2` | — | — | Ne | — |
| `nfeoerb1` | `-2` | — | — | Netaikoma | — |
| `nfereason1_01a` | `1` | — | — | Pasirinkta | — |
| `nfereason1_01a` | `2` | — | — | Nepasirinkta | — |
| `nfereason1_01a` | `-2` | — | — | Netaikoma | — |
| `nfereason1_01b` | `1` | — | — | Pasirinkta | — |
| `nfereason1_01b` | `2` | — | — | Nepasirinkta | — |
| `nfereason1_01b` | `-2` | — | — | Netaikoma | — |
| `nfereason1_02` | `1` | — | — | Pasirinkta | — |
| `nfereason1_02` | `2` | — | — | Nepasirinkta | — |
| `nfereason1_02` | `-2` | — | — | Netaikoma | — |
| `nfereason1_03` | `1` | — | — | Pasirinkta | — |
| `nfereason1_03` | `2` | — | — | Nepasirinkta | — |
| `nfereason1_03` | `-2` | — | — | Netaikoma | — |
| `nfereason1_04` | `1` | — | — | Pasirinkta | — |
| `nfereason1_04` | `2` | — | — | Nepasirinkta | — |
| `nfereason1_04` | `-2` | — | — | Netaikoma | — |
| `nfereason1_13` | `1` | — | — | Pasirinkta | — |
| `nfereason1_13` | `2` | — | — | Nepasirinkta | — |
| `nfereason1_13` | `-2` | — | — | Netaikoma | — |
| `nfereason1_11` | `1` | — | — | Pasirinkta | — |
| `nfereason1_11` | `2` | — | — | Nepasirinkta | — |
| `nfereason1_11` | `-2` | — | — | Netaikoma | — |
| `nfereason1_06` | `1` | — | — | Pasirinkta | — |
| `nfereason1_06` | `2` | — | — | Nepasirinkta | — |
| `nfereason1_06` | `-2` | — | — | Netaikoma | — |
| `nfereason1_07` | `1` | — | — | Pasirinkta | — |
| `nfereason1_07` | `2` | — | — | Nepasirinkta | — |
| `nfereason1_07` | `-2` | — | — | Netaikoma | — |
| `nfereason1_08` | `1` | — | — | Pasirinkta | — |
| `nfereason1_08` | `2` | — | — | Nepasirinkta | — |
| `nfereason1_08` | `-2` | — | — | Netaikoma | — |
| `nfereason1_09` | `1` | — | — | Pasirinkta | — |
| `nfereason1_09` | `2` | — | — | Nepasirinkta | — |
| `nfereason1_09` | `-2` | — | — | Netaikoma | — |
| `nfereason1_10` | `1` | — | — | Pasirinkta | — |
| `nfereason1_10` | `2` | — | — | Nepasirinkta | — |
| `nfereason1_10` | `-2` | — | — | Netaikoma | — |
| `nfereason1_12` | `1` | — | — | Pasirinkta | — |
| `nfereason1_12` | `2` | — | — | Nepasirinkta | — |
| `nfereason1_12` | `-2` | — | — | Netaikoma | — |
| `nfereason1` | `0` | — | — | Nė vienas (-a) iš toliau nurodytų atsakymų | — |
| `nfereason1` | `1` | — | — | Pasirinkta | — |
| `nfereason1` | `-2` | — | — | Netaikoma | — |
| `nfeprovider1` | `1` | — | — | Formaliojo švietimo įstaiga | — |
| `nfeprovider1` | `2` | — | — | Neformaliojo švietimo ir mokymo įstaigos | — |
| `nfeprovider1` | `3` | — | — | Komercinė įmonė, kurios pagrindinė veikla nėra švietimas ir mokymas (pvz., įrangos tiekėjai) | — |
| `nfeprovider1` | `4` | — | — | Darbdavys | — |
| `nfeprovider1` | `5` | — | — | Darbdavių organizacijos, prekybos rūmai | — |
| `nfeprovider1` | `6` | — | — | Profesinės sąjungos | — |
| `nfeprovider1` | `7` | — | — | Ne pelno organizacijos, pvz., kultūros draugija, politinė partija | — |
| `nfeprovider1` | `8` | — | — | Pavieniai asmenys (pvz., studentai, teikiantys privačių pamokų paslaugas) | — |
| `nfeprovider1` | `9` | — | — | Nekomercinė įstaiga, kurios pagrindė veikla nėra švietimas ir mokymas (pvz., bibliotekos, muziejai, ministerijos) | — |
| `nfeprovider1` | `10` | — | — | Kita | — |
| `nfeprovider1` | `-1` | — | — | Nėra atsakymo | — |
| `nfeprovider1` | `-2` | — | — | Netaikoma | — |
| `nfecert1` | `1` | — | — | Taip, jo reikalauja darbdavys arba profesinė organizacija, arba jis yra teisiškai privalomas | — |
| `nfecert1` | `2` | — | — | Taip, bet jo nereikalauja darbdavys arba profesinė organizacija, arba jis nėra teisiškai neprivalomas | — |
| `nfecert1` | `3` | — | — | Ne (tik dalyvavimo patvirtinimas) | — |
| `nfecert1` | `-2` | — | — | Netaikoma | — |
| `nfepaid1` | `0` | — | — | Nė vienas (-a) iš toliau nurodytų atsakymų | — |
| `nfepaid1` | `1` | — | — | Pasirikta | — |
| `nfepaid1` | `-2` | — | — | Netaikoma | — |
| `nfepaidby1_1` | `1` | — | — | Pasirinkta | — |
| `nfepaidby1_1` | `2` | — | — | Nepasirinkta | — |
| `nfepaidby1_1` | `-2` | — | — | Netaikoma | — |
| `nfepaidby1_2` | `1` | — | — | Pasirinkta | — |
| `nfepaidby1_2` | `2` | — | — | Nepasirinkta | — |
| `nfepaidby1_2` | `-2` | — | — | Netaikoma | — |
| `nfepaidby1_3` | `1` | — | — | Pasirinkta | — |
| `nfepaidby1_3` | `2` | — | — | Nepasirinkta | — |
| `nfepaidby1_3` | `-2` | — | — | Netaikoma | — |
| `nfepaidby1_4` | `1` | — | — | Pasirinkta | — |
| `nfepaidby1_4` | `2` | — | — | Nepasirinkta | — |
| `nfepaidby1_4` | `-2` | — | — | Netaikoma | — |
| `nfepaidby1` | `0` | — | — | Nė vienas (-a) iš toliau nurodytų atsakymų | — |
| `nfepaidby1` | `1` | — | — | Pasirikta | — |
| `nfepaidby1` | `-2` | — | — | Netaikoma | — |
| `nfeusea1` | `1` | — | — | Labai didelis | — |
| `nfeusea1` | `2` | — | — | Pakankamas | — |
| `nfeusea1` | `3` | — | — | Labai mažas | — |
| `nfeusea1` | `4` | — | — | Jokio | — |
| `nfeusea1` | `-2` | — | — | Netaikoma | — |
| `nfeuseb1` | `1` | — | — | Labai didelis | — |
| `nfeuseb1` | `2` | — | — | Pakankamas | — |
| `nfeuseb1` | `3` | — | — | Labai mažas | — |
| `nfeuseb1` | `4` | — | — | Jokio | — |
| `nfeuseb1` | `-2` | — | — | Netaikoma | — |
| `nfeoutcome1_1` | `1` | — | — | Pasirinkta | — |
| `nfeoutcome1_1` | `2` | — | — | Nepasirinkta | — |
| `nfeoutcome1_1` | `-2` | — | — | Netaikoma | — |
| `nfeoutcome1_3` | `1` | — | — | Pasirinkta | — |
| `nfeoutcome1_3` | `2` | — | — | Nepasirinkta | — |
| `nfeoutcome1_3` | `-2` | — | — | Netaikoma | — |
| `nfeoutcome1_2` | `1` | — | — | Pasirinkta | — |
| `nfeoutcome1_2` | `2` | — | — | Nepasirinkta | — |
| `nfeoutcome1_2` | `-2` | — | — | Netaikoma | — |
| `nfeoutcome1_4` | `1` | — | — | Pasirinkta | — |
| `nfeoutcome1_4` | `2` | — | — | Nepasirinkta | — |
| `nfeoutcome1_4` | `-2` | — | — | Netaikoma | — |
| `nfeoutcome1_5` | `1` | — | — | Pasirinkta | — |
| `nfeoutcome1_5` | `2` | — | — | Nepasirinkta | — |
| `nfeoutcome1_5` | `-2` | — | — | Netaikoma | — |
| `nfeoutcome1_6` | `1` | — | — | Pasirinkta | — |
| `nfeoutcome1_6` | `2` | — | — | Nepasirinkta | — |
| `nfeoutcome1_6` | `-2` | — | — | Netaikoma | — |
| `nfeoutcome1_7` | `1` | — | — | Pasirinkta | — |
| `nfeoutcome1_7` | `2` | — | — | Nepasirinkta | — |
| `nfeoutcome1_7` | `-2` | — | — | Netaikoma | — |
| `nfeoutcome1` | `1` | — | — | Atsakymas pasirinktas | — |
| `nfeoutcome1` | `-2` | — | — | Netaikoma | — |
| `difficulty` | `1` | — | — | Asmuo dalyvavo formaliojo ar neformaliojo švietimo veikloje ir nenorėjo dalyvauti daugiau | — |
| `difficulty` | `2` | — | — | Asmuo dalyvavo formaliojo arba neformaliojo švietimo veikloje ir norėjo dalyvauti daugiau | — |
| `difficulty` | `3` | — | — | Asmuo nedalyvavo formaliojo arba neformaliojo švietimo veikloje ir dalyvauti nenorėjo | — |
| `difficulty` | `4` | — | — | Asmuo nedalyvavo formaliojo arba neformaliojo švietimo veikloje, bet dalyvauti norėjo | — |
| `need` | `1` | — | — | Taip | — |
| `need` | `2` | — | — | Ne | — |
| `need` | `-2` | — | — | Netaikoma | — |
| `difftype_01` | `1` | — | — | Pasirinkta | — |
| `difftype_01` | `2` | — | — | Nepasirinkta | — |
| `difftype_01` | `-2` | — | — | Netaikoma | — |
| `difftype_02` | `1` | — | — | Pasirinkta | — |
| `difftype_02` | `2` | — | — | Nepasirinkta | — |
| `difftype_02` | `-2` | — | — | Netaikoma | — |
| `difftype_03` | `1` | — | — | Pasirinkta | — |
| `difftype_03` | `2` | — | — | Nepasirinkta | — |
| `difftype_03` | `-2` | — | — | Netaikoma | — |
| `difftype_04` | `1` | — | — | Pasirinkta | — |
| `difftype_04` | `2` | — | — | Nepasirinkta | — |
| `difftype_04` | `-2` | — | — | Netaikoma | — |
| `difftype_05` | `1` | — | — | Pasirinkta | — |
| `difftype_05` | `2` | — | — | Nepasirinkta | — |
| `difftype_05` | `-2` | — | — | Netaikoma | — |
| `difftype_06` | `1` | — | — | Pasirinkta | — |
| `difftype_06` | `2` | — | — | Nepasirinkta | — |
| `difftype_06` | `-2` | — | — | Netaikoma | — |
| `difftype_07` | `1` | — | — | Pasirinkta | — |
| `difftype_07` | `2` | — | — | Nepasirinkta | — |
| `difftype_07` | `-2` | — | — | Netaikoma | — |
| `difftype_08a` | `1` | — | — | Pasirinkta | — |
| `difftype_08a` | `2` | — | — | Nepasirinkta | — |
| `difftype_08a` | `-2` | — | — | Netaikoma | — |
| `difftype_08b` | `1` | — | — | Pasirinkta | — |
| `difftype_08b` | `2` | — | — | Nepasirinkta | — |
| `difftype_08b` | `-2` | — | — | Netaikoma | — |
| `difftype_09` | `1` | — | — | Pasirinkta | — |
| `difftype_09` | `2` | — | — | Nepasirinkta | — |
| `difftype_09` | `-2` | — | — | Netaikoma | — |
| `difftype_10` | `1` | — | — | Pasirinkta | — |
| `difftype_10` | `2` | — | — | Nepasirinkta | — |
| `difftype_10` | `-2` | — | — | Netaikoma | — |
| `difftype_12` | `1` | — | — | Pasirinkta | — |
| `difftype_12` | `2` | — | — | Nepasirinkta | — |
| `difftype_12` | `-2` | — | — | Netaikoma | — |
| `difftype` | `1` | — | — | Atsakymas pasirinktas | — |
| `difftype` | `-2` | — | — | Netaikoma | — |
| `inffamily` | `1` | — | — | Taip | — |
| `inffamily` | `2` | — | — | Ne | — |
| `infmaterial` | `1` | — | — | Taip | — |
| `infmaterial` | `2` | — | — | Ne | — |
| `infcomputer` | `1` | — | — | Taip | — |
| `infcomputer` | `2` | — | — | Ne | — |
| `infmedia` | `1` | — | — | Taip | — |
| `infmedia` | `2` | — | — | Ne | — |
| `infmuseum` | `1` | — | — | Taip | — |
| `infmuseum` | `2` | — | — | Ne | — |
| `inflibraries` | `1` | — | — | Taip | — |
| `inflibraries` | `2` | — | — | Ne | — |
| `inf` | `1` | — | — | Taip, vieną dalyką | — |
| `inf` | `2` | — | — | Taip, keletą dalykų | — |
| `langmother1` | `1` | — | — | Lietuvių | — |
| `langmother1` | `2` | — | — | Nelietuvių | — |
| `langmother2` | `0` | — | — | Nėra | — |
| `langmother2` | `1` | — | — | Lietuvių | — |
| `langmother2` | `2` | — | — | Nelietuvių | — |
| `langlevel1` | `0` | — | — | Aš tik suprantu ir moku kelis žodžius ir frazes | — |
| `langlevel1` | `1` | — | — | Suprantu ir vartoju nesudėtingus kasdieninius posakius. Kalbą vartoju, kai aptariami žinomi dalykai ir situacijos | — |
| `langlevel1` | `2` | — | — | Suvokiu prasmę, kai kalbama aiškiai, ir galiu parengti nesudėtingą tekstą. Galiu apibūdinti patirtį bei įvykius ir bendrauti pakankamai sklandžiai | — |
| `langlevel1` | `3` | — | — | Suprantu įvairių sričių sudėtingesnius tekstus ir lanksčiai vartoju kalbą. Kalbą moku beveik puikiai | — |
| `langlevel1` | `-2` | — | — | Netaikoma | — |
| `langlevel2` | `0` | — | `open` | Aš tik suprantu ir moku kelis žodžius ir frazes | — |
| `langlevel2` | `1` | — | `open` | Suprantu ir vartoju nesudėtingus kasdieninius posakius. Kalbą vartoju, kai aptariami žinomi dalykai ir situacijos | — |
| `langlevel2` | `2` | — | `open` | Suvokiu prasmę, kai kalbama aiškiai, ir galiu parengti nesudėtingą tekstą. Galiu apibūdinti patirtį bei įvykius ir bendrauti pakankamai sklandžiai | — |
| `langlevel2` | `3` | — | `open` | Suprantu įvairių sričių sudėtingesnius tekstus ir lanksčiai vartoju kalbą. Kalbą moku beveik puikiai | — |
| `langlevel2` | `-2` | — | `open` | Netaikoma | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/svietimas.csv#L604 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/svietimas.csv#L604)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/svietimas/suaugusiuju (https://data.gov.lt/datasets/1621/)
