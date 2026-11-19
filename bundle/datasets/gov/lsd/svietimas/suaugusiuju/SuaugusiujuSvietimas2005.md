---
type: Table
title: "SuaugusiujuSvietimas2005 — Suaugusiųjų švietimo statistinis tyrimas 2005 m."
description: "2005 metais atliktas suaugusiųjų švietimo statistinio tyrimas"
resource: "https://get.data.gov.lt/datasets/gov/lsd/svietimas/suaugusiuju/SuaugusiujuSvietimas2005"
tags: [gov, lsd, suaugusiujusvietimas2005, deployed, cadence-quinquennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/svietimas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lsd/svietimas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1621/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/svietimas/suaugusiuju"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# SuaugusiujuSvietimas2005 — Suaugusiųjų švietimo statistinis tyrimas 2005 m.

2005 metais atliktas suaugusiųjų švietimo statistinio tyrimas[^manifest]

- **Model:** `datasets/gov/lsd/svietimas/suaugusiuju/SuaugusiujuSvietimas2005`[^manifest]
- **Dataset:** [Suaugusiųjų švietimo statistinio tyrimo duomenys](../suaugusiuju.md) (`datasets/gov/lsd/svietimas/suaugusiuju`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/svietimas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/svietimas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/svietimas/suaugusiuju/SuaugusiujuSvietimas2005` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUINQUENNIAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `indyvidualno` | `integer` | — | — | `open` | — | Asmens ID | — |
| `sex` | `string` | — | — | `open` | — | Lytis | — |
| `age` | `string` | — | — | `open` | — | Amžius | — |
| `isced2d` | `string` | — | — | `open` | — | Įgytas aukščiausias išsilavinimas | — |
| `hatfield` | `string` | — | — | `open` | — | Specialybė ar kvalifikacija, kurią Jūs įgijote | — |
| `iscdyear` | `string` | — | — | `open` | — | Metai, kuriais įgytas aukščiausias išsilavinimas | — |
| `mainstat` | `integer` | — | — | `open` | — | Dabartinis užimtumo statusas | — |
| `stapro` | `integer` | — | — | `open` | — | Darbovietėje užimamos pareigos | — |
| `nace2d` | `integer` | — | — | `open` | — | Įmonės, kurioje dirbate, ekonominė veikla | — |
| `isco2d` | `integer` | — | — | `open` | — | Profesija | — |
| `nbpers` | `integer` | — | — | `open` | — | Asmenų skaičius Jūsų darbovietėje | — |
| `fedstat` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. mokėtės formaliojo švietimo įstaigoje | — |
| `fedlev1` | `integer` | — | — | `open` | — | Kur Jūs mokėtės per pastaruosius 12 mėn? | — |
| `fedfiel1` | `string` | — | — | `open` | — | Mokymo / studijų programa | — |
| `fedpur1` | `integer` | — | — | `open` | — | Pagrindinės priežastys lėmusios, kad Jūs mokėtės? | — |
| `fedlen1` | `integer` | — | — | `open` | — | Valandų, praleistų besimokant, skaičius | — |
| `fedwrk_hr1` | `integer` | — | — | `open` | — | Ar mokėtės darbo metu? | — |
| `fedemsups1` | `integer` | — | — | `open` | — | Ar Jūsų darbdavys visiškai ar iš dalies mokėjo už Jūsų mokslą? | — |
| `fedhouss1` | `integer` | — | — | `open` | — | Ar Jūs pats ar kuris nors Jūsų šeimos narys visiškai ar iš dalies mokėjo už Jūsų mokslą? | — |
| `fedinwests1` | `integer` | — | — | `open` | — | Suma, kurią Jūs ar Jūsų šeimos narys mokėjote už Jūsų mokslą? | — |
| `clasroom` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. lankėte kvalifikacijos kėlimo kursus, privačias pamokas | — |
| `distance` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. mokėtės nuotoliniuose kursuose? | — |
| `semwork` | `integer` | — | — | `open` | — | Ar per paskutinius 12 mėn. lankėte seminarus ir konferencijas? | — |
| `guiotjt` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. buvote mokomas darbo vietoje? | — |
| `nfe999` | `integer` | — | — | `open` | — | Mokymo kursų, privačių pamokų, seminarų, konferencijų, kuriuose dalyvavote per paskutinius 12 mėn., skaičius | — |
| `nfepurp1` | `integer` | — | — | `open` | — | Pagrindinės priežastys, lėmusios, kad Jūs mokėtės atsitiktinai išrinktuose mokymuose | — |
| `nferjob1` | `integer` | — | — | `open` | — | Jūs mokėtės šiuose mokymuose, kad galėtumėte geriau atlikti savo darbą | — |
| `nferlosj1` | `integer` | — | — | `open` | — | Jūs mokėtės šiuose mokymuose, norėdamas (-a) būti tikras (-a), kad neprarasite darbo | — |
| `nferprom1` | `integer` | — | — | `open` | — | Jūs mokėtės šiuose mokymuose, kad turėtumėte didesnes galimybes susirasti naują darbą, pakeisti specialybę, profesinę kvalifikaciją | — |
| `nfenbuis1` | `integer` | — | — | `open` | — | Jūs mokėtės šiuose mokymuose, kad pradėtumėte nuosavą verslą | — |
| `nferobl1` | `integer` | — | — | `open` | — | Jūs mokėtės šiuose mokymuose, nes to reikalavo darbdavys | — |
| `nferskil1` | `integer` | — | — | `open` | — | Jūs mokėtės šiuose mokymuose, nes norėjote įgyti žinių ir įgūdžių, naudingų kasdieniniame gyvenime | — |
| `nfersub1` | `integer` | — | — | `open` | — | Jūs mokėtės šiuose mokymuose, nes norėjote įgyti daugiau žinių apie Jus dominantį dalyką | — |
| `nfercer1` | `integer` | — | — | `open` | — | Jūs mokėtės šiuose mokymuose, kad gautumėte pažymėjimą, suteikiantį kvalifikaciją ar teisę atlikti darbą | — |
| `nferfun1` | `integer` | — | — | `open` | — | Jūs mokėtės šiuose mokymuose, kad susipažintumėte su naujais žmonėmis | — |
| `nfewrk_hr1` | `integer` | — | — | `open` | — | Ar mokėtės darbo metu? | — |
| `nfeemsups1` | `integer` | — | — | `open` | — | Ar Jūsų darbdavys visiškai arba iš dalies mokėjo už Jūsų mokslą? | — |
| `nfehouss1` | `integer` | — | — | `open` | — | Ar Jūs pats arba kuris nors Jūsų šeimos narys visiškai ar iš dalies mokėjo už Jūsų mokslą? | — |
| `nfelen1` | `integer` | — | — | `open` | — | Valandų, praleistų besimokant, skaičius | — |
| `nfeeval1` | `integer` | — | — | `open` | — | Ar pasinaudojote (tikitės pasinaudoti) mokymosi metu įgytomis žiniomis? | — |
| `wntpar` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. Jūs norėjote mokytis? | — |
| `nwntjob` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes darbe nebuvo poreikio mokytis | — |
| `nwntpers` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes nebuvo poreikio | — |
| `nwntperq` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes neturėjote reikalingų sugebėjimų | — |
| `nwntpric` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes mokymasis buvo per brangus | — |
| `nwntsup` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes trūko darbdavio paramos | — |
| `nwntwrsc` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes sunku buvo suderinti mokymosi ir darbo laiką | — |
| `nwntntim` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes buvote per daug užimtas namuose | — |
| `nwntdist` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes mokymosi vieta buvo per toli | — |
| `nwntshol` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes nenorėjote vėl grįžti į mokslus | — |
| `nwntager` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes trukdė sveikata, amžius | — |
| `wntperq` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes neturėjote reikalingų sugebėjimų | — |
| `wntpric` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes mokymasis buvo per brangus | — |
| `wntsup` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes trūko darbdavio paramos | — |
| `wntwrsc` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes buvote užsiėmęs darbe | — |
| `wntntim` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes buvote per daug užimtas namuose | — |
| `wntshol` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes nenorėjote vėl grįžti į mokslus | — |
| `wntdist` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes mokymosi vieta buvo per toli | — |
| `wntager` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes trukdė sveikata, amžius | — |
| `wntparmor` | `integer` | — | — | `open` | — | Jūs anksčiau sakėte, kad mokėtės per pastaruosius 12 mėn. Ar norėjote papildomai mokytis, lankyti kursus? | — |
| `selffam` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. Jūs bandėte savarankiškai mokytis iš draugo, šeimos nario, kolegos? | — |
| `selfprint` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. Jūs bandėte savarankiškai mokytis iš knygų, specialybės žurnalų? | — |
| `selfcom` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. Jūs bandėte savarankiškai mokytis naudodami kompiuterį ir/ar internetą? | — |
| `selftv` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. Jūs žiūrėjote mokomąsias televizijos laidas, naudojotės garso ir vaizdo juostomis arba kompaktiniais diskais? | — |
| `selfmuse` | `integer` | — | — | `open` | — | Ar per pataruosius 12 mėn. Jūs lankėtės su gidu muziejuose, istoriniuose, gamtos objektuose | — |
| `selflibr` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. Jūs lankėtės bibliotekose, kultūros ir mokymo centruose, kitose įstaigose, teikiančiose mokslo žinių | — |
| `ictlevel` | `integer` | — | — | `open` | — | Koks Jūsų kompiuterinis raštingumas? | — |
| `comuter` | `integer` | — | — | `open` | — | Kaip dažnai Jūs naudojatės kompiuteriu? | — |
| `internet` | `integer` | — | — | `open` | — | Kaip dažnai Jūs naudojatės internetu? | — |
| `lifeper` | `integer` | — | — | `open` | — | Kiek kartų per pastaruosius 12 mėn. lankėtės teatre, koncerte, muziejuje, parodoje, ekskursijoje | — |
| `cinema` | `integer` | — | — | `open` | — | Kiek kartų per pastaruosius 12 mėn. buvote kine | — |
| `cultsit` | `integer` | — | — | `open` | — | Kiek kartų per pastaruosius 12 mėn. lankėtės kultūros tinklalapiuose | — |
| `sport` | `integer` | — | — | `open` | — | Kiek kartų per pastaruosius 12 mėn. lankėtės sporto renginyje | — |
| `singdan` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. dalyvavote viešame pasirodyme, kuriame dainavote, vaidinote, grojote? | — |
| `photo` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. fotografavote, filmavote? | — |
| `paint` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. piešėte, konstravote? | — |
| `writing` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. kūrėte poeziją, prozą, muziką? | — |
| `bookhome` | `integer` | — | — | `open` | — | Kiek apytiksliai turite knygų namuose? | — |
| `readbok` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. skaitėte grožinę literatūrą? | — |
| `readboknb` | `integer` | — | — | `open` | — | Kiek grožinės literatūros knygų perskaitėte? | — |
| `newspafq` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. skaitėte laikraščius? | — |
| `attunempl` | `integer` | — | — | `open` | — | Ar sutinkate su teiginiu, kad žmonės, kurie būdami suaugę mokosi, rečiau tampa bedarbiais | — |
| `attskills` | `integer` | — | — | `open` | — | Ar sutinkate su teiginiu, kad siekdami karjeros turite nuolat gilinti žinias ir tobulinti įgūdžius | — |
| `attemplr` | `integer` | — | — | `open` | — | Ar sutinkate su teiginiu, kad darbdaviai turi būti atsakingi už visų savo darbuotojų mokymąsi | — |
| `attinclas` | `integer` | — | — | `open` | — | Ar sutinkate su teiginiu, kad reikalingų įgūdžių mokymo įstaigoje neišmoksite | — |
| `attlife` | `integer` | — | — | `open` | — | Ar sutinkate su teiginiu, kad mokslas ir mokymasis gali geriau padėti tvarkyti kasdienį gyvenimą | — |
| `attfun` | `integer` | — | — | `open` | — | Ar sutinkate su teiginiu, kad mokytis naujų dalykų smagu | — |
| `attselfc` | `integer` | — | — | `open` | — | Ar sutinkate su teiginiu, kad mokymasis suteikia pasitikėjimo savimi | — |
| `degurb` | `integer` | — | — | `open` | — | Urbanizacijos laipsnis | — |
| `weight` | `integer` | — | — | `open` | — | Asmens populiacijos svoris | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `age` | `"1"` | — | — | 25–34 | — |
| `age` | `"2"` | — | — | 35–54 | — |
| `age` | `"3"` | — | — | 55 ir vyresni | — |
| `isced2d` | `"1"` | — | — | Žemesnis išsilavinimas (ISCED 1,2) | — |
| `isced2d` | `"2"` | — | — | Vidutinis išsilavinimas (ISCED 3,4) | — |
| `isced2d` | `"3"` | — | — | Aukštas išsilavinimas (ISCED 5,6) | — |
| `hatfield` | `"000"` | — | — | Bendrosios programos | — |
| `hatfield` | `"100"` | — | — | Mokytojų rengimas ir pedagogika | — |
| `hatfield` | `"200"` | — | — | Humanitariniai mokslai, kalbos ir menas | — |
| `hatfield` | `"300"` | — | — | Socialiniai mokslai, verslas ir teisė | — |
| `hatfield` | `"400"` | — | — | Gamtos mokslai, matematika ir kompiuterija | — |
| `hatfield` | `"500"` | — | — | Inžinerija, gamyba ir statyba | — |
| `hatfield` | `"600"` | — | — | Žemės ūkis ir veterinarija | — |
| `hatfield` | `"700"` | — | — | Sveikatos priežiūra ir socialinė apsauga | — |
| `hatfield` | `"800"` | — | — | Paslaugos | — |
| `hatfield` | `"900"` | — | — | Nežinoma sritis | — |
| `iscdyear` | `"1"` | — | — | 1969-aisiais ir anksčiau | — |
| `iscdyear` | `"2"` | — | — | 1970–1989 | — |
| `iscdyear` | `"3"` | — | — | 1990-aisiais ir vėliau | — |
| `mainstat` | `1` | — | — | Užimtas | — |
| `mainstat` | `2` | — | — | Bedarbis | — |
| `mainstat` | `3` | — | — | Neaktyvus | — |
| `stapro` | `1` | — | — | Samdomas darbuotojas | — |
| `stapro` | `2` | — | — | Kita | — |
| `nace2d` | `1` | — | — | Žemės ūkis, medžioklė, miškininkystė ir žuvininkystė; kasyba, karjerų eksplotavimas ir apdirbamoji pramonė | — |
| `nace2d` | `2` | — | — | Elektros, dujų,vandens tiekimas ir statyba; didmeninė ir mažmeninė prekyba | — |
| `nace2d` | `3` | — | — | Viešbučiai, restoranai, transportas, saugojimas ir ryšiai; kita komunalinė, socialinė ir asmeninė aptarnavimo veikla, namų ūkių, samdančių darbininkus, veikla | — |
| `nace2d` | `4` | — | — | Finansinis tarpininkavimas, nekilnojamojo turto, nuomos ir verslo veikla; viešasis valdymas ir gynyba, švietimas ir sveikatos priežiūra, socialinis darbas | — |
| `isco2d` | `1` | — | — | Įstatymų leidėjai, vyresnieji pareigūnai, valdytojai, įmonių, istaigų, organizacijų ir kiti vadovai | — |
| `isco2d` | `2` | — | — | Specialistai | — |
| `isco2d` | `3` | — | — | Jaunesnieji specialistai, technikai ir tarnautojai | — |
| `isco2d` | `4` | — | — | Aptarnavimo srities ir prekybos darbuotojai | — |
| `isco2d` | `5` | — | — | Kvalifikuoti prekinio žemės ūkio ir žuvininkystės darbininkai | — |
| `isco2d` | `6` | — | — | Kvalifikuoti darbininkai ir amatininkai | — |
| `isco2d` | `7` | — | — | Įrenginių, mašinų operatoriai, surinkėjai ir nekvalifikuoti darbininkai | — |
| `nbpers` | `1` | — | — | 1–10 | — |
| `nbpers` | `2` | — | — | 11–19 | — |
| `nbpers` | `3` | — | — | 20–49 | — |
| `nbpers` | `4` | — | — | 50 ir daugiau | — |
| `nbpers` | `5` | — | — | Tiksliai nežinote | — |
| `fedstat` | `1` | — | — | Taip | — |
| `fedstat` | `2` | — | — | Ne | — |
| `fedlev1` | `1` | — | — | Žemesnis išsilavinimas (ISCED – 1, 2) | — |
| `fedlev1` | `2` | — | — | Vidutinis išsilavinimas (ISCED – 3, 4) | — |
| `fedlev1` | `3` | — | — | Aukštas išsilavinimas (ISCED – 5, 6) | — |
| `fedfiel1` | `"000"` | — | — | Bendrosios programos | — |
| `fedfiel1` | `"100"` | — | — | Mokytojų rengimas ir pedagogika | — |
| `fedfiel1` | `"200"` | — | — | Humanitariniai mokslai, kalbos ir menas | — |
| `fedfiel1` | `"300"` | — | — | Socialiniai mokslai, verslas ir teisė | — |
| `fedfiel1` | `"400"` | — | — | Gamtos mokslai, matematika ir kompiuterija | — |
| `fedfiel1` | `"500"` | — | — | Inžinerija, gamyba ir statyba | — |
| `fedfiel1` | `"600"` | — | — | Žemės ūkis ir veterinarija | — |
| `fedfiel1` | `"700"` | — | — | Sveikatos priežiūra ir socialinė apsauga | — |
| `fedfiel1` | `"800"` | — | — | Paslaugos | — |
| `fedfiel1` | `"900"` | — | — | Nežinoma sritis | — |
| `fedpur1` | `1` | — | — | Susijusios su darbu | — |
| `fedpur1` | `2` | — | — | Asmeninės | — |
| `fedlen1` | `1` | — | — | 1 - 200 | — |
| `fedlen1` | `2` | — | — | 201 - 400 | — |
| `fedlen1` | `3` | — | — | 401 ir daugiau | — |
| `fedwrk_hr1` | `1` | — | — | Tik mokamomis darbo valandomis | — |
| `fedwrk_hr1` | `2` | — | — | Dažniausiai mokamomis darbo valandomis | — |
| `fedwrk_hr1` | `3` | — | — | Dažniausiai nemokamomis darbo valandomis | — |
| `fedwrk_hr1` | `4` | — | — | Tik nemokamomis darbo valandomis | — |
| `fedwrk_hr1` | `5` | — | — | Tuo metu nedirbote | — |
| `fedemsups1` | `1` | — | — | Taip, visiškai | — |
| `fedemsups1` | `2` | — | — | Taip, iš dalies | — |
| `fedemsups1` | `3` | — | — | Ne, nemokėjo | — |
| `fedemsups1` | `4` | — | — | Mokėti nereikėjo | — |
| `fedemsups1` | `5` | — | — | Tuo metu nedirbote | — |
| `fedhouss1` | `1` | — | — | Taip, visiškai | — |
| `fedhouss1` | `2` | — | — | Taip, iš dalies | — |
| `fedhouss1` | `3` | — | — | Ne | — |
| `fedinwests1` | `1` | — | — | 1 - 500 | — |
| `fedinwests1` | `2` | — | — | 501 - 1000 | — |
| `fedinwests1` | `3` | — | — | 1001 ir daugiau | — |
| `clasroom` | `1` | — | — | Taip | — |
| `clasroom` | `2` | — | — | Ne | — |
| `distance` | `1` | — | — | Taip | — |
| `distance` | `2` | — | — | Ne | — |
| `semwork` | `1` | — | — | Taip | — |
| `semwork` | `2` | — | — | Ne | — |
| `guiotjt` | `1` | — | — | Taip | — |
| `guiotjt` | `2` | — | — | Ne | — |
| `nfe999` | `1` | — | — | 1 | — |
| `nfe999` | `2` | — | — | 2 | — |
| `nfe999` | `3` | — | — | 3-6 | — |
| `nfe999` | `4` | — | — | 7 ir daugiau | — |
| `nfepurp1` | `1` | — | — | Susijusios su darbu | — |
| `nfepurp1` | `2` | — | — | Asmeninės | — |
| `nferjob1` | `1` | — | — | Taip | — |
| `nferjob1` | `2` | — | — | Ne | — |
| `nferlosj1` | `1` | — | — | Taip | — |
| `nferlosj1` | `2` | — | — | Ne | — |
| `nferprom1` | `1` | — | — | Taip | — |
| `nferprom1` | `2` | — | — | Ne | — |
| `nfenbuis1` | `1` | — | — | Taip | — |
| `nfenbuis1` | `2` | — | — | Ne | — |
| `nferobl1` | `1` | — | — | Taip | — |
| `nferobl1` | `2` | — | — | Ne | — |
| `nferskil1` | `1` | — | — | Taip | — |
| `nferskil1` | `2` | — | — | Ne | — |
| `nfersub1` | `1` | — | — | Taip | — |
| `nfersub1` | `2` | — | — | Ne | — |
| `nfercer1` | `1` | — | — | Taip | — |
| `nfercer1` | `2` | — | — | Ne | — |
| `nferfun1` | `1` | — | — | Taip | — |
| `nferfun1` | `2` | — | — | Ne | — |
| `nfewrk_hr1` | `1` | — | — | Tik mokamomis darbo valandomis | — |
| `nfewrk_hr1` | `2` | — | — | Dažniausiai mokamomis darbo valandomis | — |
| `nfewrk_hr1` | `3` | — | — | Dažniausiai nemokamomis darbo valandomis | — |
| `nfewrk_hr1` | `4` | — | — | Tik nemokamomis darbo valandomis | — |
| `nfewrk_hr1` | `5` | — | — | Tuo metu nedirbote | — |
| `nfeemsups1` | `1` | — | — | Taip, visiškai | — |
| `nfeemsups1` | `2` | — | — | Taip, iš dalies | — |
| `nfeemsups1` | `3` | — | — | Ne, nemokėjo | — |
| `nfeemsups1` | `4` | — | — | Mokėti nereikėjo | — |
| `nfeemsups1` | `5` | — | — | Tuo metu nedirbote | — |
| `nfehouss1` | `1` | — | — | Taip, visiškai | — |
| `nfehouss1` | `2` | — | — | Taip, iš dalies | — |
| `nfehouss1` | `3` | — | — | Ne | — |
| `nfelen1` | `1` | — | — | 1 - 20 | — |
| `nfelen1` | `2` | — | — | 21 - 100 | — |
| `nfelen1` | `3` | — | — | 101 ir daugiau | — |
| `nfeeval1` | `1` | — | — | Taip, labai daug | — |
| `nfeeval1` | `2` | — | — | Šiek tiek | — |
| `nfeeval1` | `3` | — | — | Labai nedaug | — |
| `nfeeval1` | `4` | — | — | Visai nepasinaudojau ir nesitikiu pasinaudoti | — |
| `wntpar` | `1` | — | — | Taip | — |
| `wntpar` | `2` | — | — | Ne | — |
| `nwntjob` | `1` | — | — | Taip | — |
| `nwntjob` | `2` | — | — | Ne | — |
| `nwntpers` | `1` | — | — | Taip | — |
| `nwntpers` | `2` | — | — | Ne | — |
| `nwntperq` | `1` | — | — | Taip | — |
| `nwntperq` | `2` | — | — | Ne | — |
| `nwntpric` | `1` | — | — | Taip | — |
| `nwntpric` | `2` | — | — | Ne | — |
| `nwntsup` | `1` | — | — | Taip | — |
| `nwntsup` | `2` | — | — | Ne | — |
| `nwntwrsc` | `1` | — | — | Taip | — |
| `nwntwrsc` | `2` | — | — | Ne | — |
| `nwntntim` | `1` | — | — | Taip | — |
| `nwntntim` | `2` | — | — | Ne | — |
| `nwntdist` | `1` | — | — | Taip | — |
| `nwntdist` | `2` | — | — | Ne | — |
| `nwntshol` | `1` | — | — | Taip | — |
| `nwntshol` | `2` | — | — | Ne | — |
| `nwntager` | `1` | — | — | Taip | — |
| `nwntager` | `2` | — | — | Ne | — |
| `wntperq` | `1` | — | — | Taip | — |
| `wntperq` | `2` | — | — | Ne | — |
| `wntpric` | `1` | — | — | Taip | — |
| `wntpric` | `2` | — | — | Ne | — |
| `wntsup` | `1` | — | — | Taip | — |
| `wntsup` | `2` | — | — | Ne | — |
| `wntwrsc` | `1` | — | — | Taip | — |
| `wntwrsc` | `2` | — | — | Ne | — |
| `wntntim` | `1` | — | — | Taip | — |
| `wntntim` | `2` | — | — | Ne | — |
| `wntshol` | `1` | — | — | Taip | — |
| `wntshol` | `2` | — | — | Ne | — |
| `wntdist` | `1` | — | — | Taip | — |
| `wntdist` | `2` | — | — | Ne | — |
| `wntager` | `1` | — | — | Taip | — |
| `wntager` | `2` | — | — | Ne | — |
| `wntparmor` | `1` | — | — | Taip | — |
| `wntparmor` | `2` | — | — | Ne | — |
| `selffam` | `1` | — | — | Taip | — |
| `selffam` | `2` | — | — | Ne | — |
| `selfprint` | `1` | — | — | Taip | — |
| `selfprint` | `2` | — | — | Ne | — |
| `selfcom` | `1` | — | — | Taip | — |
| `selfcom` | `2` | — | — | Ne | — |
| `selftv` | `1` | — | — | Taip | — |
| `selftv` | `2` | — | — | Ne | — |
| `selfmuse` | `1` | — | — | Taip | — |
| `selfmuse` | `2` | — | — | Ne | — |
| `selflibr` | `1` | — | — | Taip | — |
| `selflibr` | `2` | — | — | Ne | — |
| `ictlevel` | `1` | — | — | Nežinote, kaip naudotis kompiuteriu | — |
| `ictlevel` | `2` | — | — | Galite naudotis kompiuteriu tik interneto tinklalapių peržiūrai | — |
| `ictlevel` | `3` | — | — | Išmanote kompiuterinui raštingumo pagrindus | — |
| `ictlevel` | `4` | — | — | Pažengęs kompiuterio naudotojas | — |
| `ictlevel` | `5` | — | — | Kompiuterio specialistas | — |
| `comuter` | `1` | — | — | Kasdien arba beveik kasdien | — |
| `comuter` | `2` | — | — | Bent kartą per savaitę | — |
| `comuter` | `3` | — | — | Bent kartą per mėnesį | — |
| `comuter` | `4` | — | — | Mažiau nei kartą per mėnesį | — |
| `comuter` | `5` | — | — | Niekada | — |
| `internet` | `1` | — | — | Kasdien arba beveik kasdien | — |
| `internet` | `2` | — | — | Bent kartą per savaitę | — |
| `internet` | `3` | — | — | Bent kartą per mėnesį | — |
| `internet` | `4` | — | — | Mažiau nei kartą per mėnesį | — |
| `internet` | `5` | — | — | Niekada | — |
| `lifeper` | `1` | — | — | 1–3 kartus | — |
| `lifeper` | `2` | — | — | 4–6 kartus | — |
| `lifeper` | `3` | — | — | 7–12 kartų | — |
| `lifeper` | `4` | — | — | Daugiau nei 12 kartų | — |
| `lifeper` | `5` | — | — | Nesilankėte | — |
| `cinema` | `1` | — | — | 1–3 kartus | — |
| `cinema` | `2` | — | — | 4–6 kartus | — |
| `cinema` | `3` | — | — | 7–12 kartų | — |
| `cinema` | `4` | — | — | Daugiau nei 12 kartų | — |
| `cinema` | `5` | — | — | Nesilankėte | — |
| `cultsit` | `1` | — | — | 1–3 kartus | — |
| `cultsit` | `2` | — | — | 4–6 kartus | — |
| `cultsit` | `3` | — | — | 7–12 kartų | — |
| `cultsit` | `4` | — | — | Daugiau nei 12 kartų | — |
| `cultsit` | `5` | — | — | Nesilankėte | — |
| `sport` | `1` | — | — | 1–3 kartus | — |
| `sport` | `2` | — | — | 4–6 kartus | — |
| `sport` | `3` | — | — | 7–12 kartų | — |
| `sport` | `4` | — | — | Daugiau nei 12 kartų | — |
| `sport` | `5` | — | — | Nesilankėte | — |
| `singdan` | `1` | — | — | Taip | — |
| `singdan` | `2` | — | — | Ne | — |
| `photo` | `1` | — | — | Taip | — |
| `photo` | `2` | — | — | Ne | — |
| `paint` | `1` | — | — | Taip | — |
| `paint` | `2` | — | — | Ne | — |
| `writing` | `1` | — | — | Taip | — |
| `writing` | `2` | — | — | Ne | — |
| `bookhome` | `1` | — | — | 1–25 | — |
| `bookhome` | `2` | — | — | 26–100 | — |
| `bookhome` | `3` | — | — | Daugiau nei 100 | — |
| `bookhome` | `4` | — | — | Neturite | — |
| `readbok` | `1` | — | — | Taip | — |
| `readbok` | `2` | — | — | Ne | — |
| `readboknb` | `1` | — | — | 1–3 | — |
| `readboknb` | `2` | — | — | 4–7 | — |
| `readboknb` | `3` | — | — | 8–12 | — |
| `readboknb` | `4` | — | — | Daugiau nei 12 knygų | — |
| `newspafq` | `1` | — | — | Kasdien arba beveik kasdien | — |
| `newspafq` | `2` | — | — | Bent kartą per savaitę | — |
| `newspafq` | `3` | — | — | Bent kartą per mėnesį | — |
| `newspafq` | `4` | — | — | Mažiau nei kartą per mėnesį | — |
| `newspafq` | `5` | — | — | Niekada | — |
| `attunempl` | `1` | — | — | Visiškai sutinkate | — |
| `attunempl` | `2` | — | — | Beveik sutinkate | — |
| `attunempl` | `3` | — | — | Nesutinkate, bet ir neprieštaraujate | — |
| `attunempl` | `4` | — | — | Iš dalies nesutinkate | — |
| `attunempl` | `5` | — | — | Visiškai nesutinkate | — |
| `attskills` | `1` | — | — | Visiškai sutinkate | — |
| `attskills` | `2` | — | — | Beveik sutinkate | — |
| `attskills` | `3` | — | — | Nesutinkate, bet ir neprieštaraujate | — |
| `attskills` | `4` | — | — | Iš dalies nesutinkate | — |
| `attskills` | `5` | — | — | Visiškai nesutinkate | — |
| `attemplr` | `1` | — | — | Visiškai sutinkate | — |
| `attemplr` | `2` | — | — | Beveik sutinkate | — |
| `attemplr` | `3` | — | — | Nesutinkate, bet ir neprieštaraujate | — |
| `attemplr` | `4` | — | — | Iš dalies nesutinkate | — |
| `attemplr` | `5` | — | — | Visiškai nesutinkate | — |
| `attinclas` | `1` | — | — | Visiškai sutinkate | — |
| `attinclas` | `2` | — | — | Beveik sutinkate | — |
| `attinclas` | `3` | — | — | Nesutinkate, bet ir neprieštaraujate | — |
| `attinclas` | `4` | — | — | Iš dalies nesutinkate | — |
| `attinclas` | `5` | — | — | Visiškai nesutinkate | — |
| `attlife` | `1` | — | — | Visiškai sutinkate | — |
| `attlife` | `2` | — | — | Beveik sutinkate | — |
| `attlife` | `3` | — | — | Nesutinkate, bet ir neprieštaraujate | — |
| `attlife` | `4` | — | — | Iš dalies nesutinkate | — |
| `attlife` | `5` | — | — | Visiškai nesutinkate | — |
| `attfun` | `1` | — | — | Visiškai sutinkate | — |
| `attfun` | `2` | — | — | Beveik sutinkate | — |
| `attfun` | `3` | — | — | Nesutinkate, bet ir neprieštaraujate | — |
| `attfun` | `4` | — | — | Iš dalies nesutinkate | — |
| `attfun` | `5` | — | — | Visiškai nesutinkate | — |
| `attselfc` | `1` | — | — | Visiškai sutinkate | — |
| `attselfc` | `2` | — | — | Beveik sutinkate | — |
| `attselfc` | `3` | — | — | Nesutinkate, bet ir neprieštaraujate | — |
| `attselfc` | `4` | — | — | Iš dalies nesutinkate | — |
| `attselfc` | `5` | — | — | Visiškai nesutinkate | — |
| `degurb` | `1` | — | — | Tankiai apgyvendinta vietovė | — |
| `degurb` | `2` | — | — | Vidutiniškai apgyvendinta vietovė | — |
| `degurb` | `3` | — | — | Menkai apgyvendinta vietovė | — |

# Related References

- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/svietimas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/svietimas.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/svietimas/suaugusiuju (https://data.gov.lt/datasets/1621/)
