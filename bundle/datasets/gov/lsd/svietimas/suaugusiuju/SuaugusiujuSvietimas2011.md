---
type: Table
title: "SuaugusiujuSvietimas2011 — Suaugusiųjų švietimo statistinis tyrimas 2011 m."
description: "2011 metais atliktas suaugusiųjų švietimo statistinio tyrimas"
resource: "https://get.data.gov.lt/datasets/gov/lsd/svietimas/suaugusiuju/SuaugusiujuSvietimas2011"
tags: [gov, lsd, suaugusiujusvietimas2011, deployed, cadence-quinquennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/svietimas.csv#L374"
    title: "atviriduomenys/manifest — datasets/gov/lsd/svietimas.csv#L374"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1621/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/svietimas/suaugusiuju"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# SuaugusiujuSvietimas2011 — Suaugusiųjų švietimo statistinis tyrimas 2011 m.

2011 metais atliktas suaugusiųjų švietimo statistinio tyrimas[^manifest]

- **Model:** `datasets/gov/lsd/svietimas/suaugusiuju/SuaugusiujuSvietimas2011`[^manifest]
- **Dataset:** [Suaugusiųjų švietimo statistinio tyrimo duomenys](../suaugusiuju.md) (`datasets/gov/lsd/svietimas/suaugusiuju`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/svietimas.csv#L374](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/svietimas.csv#L374)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/svietimas/suaugusiuju/SuaugusiujuSvietimas2011` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUINQUENNIAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `indyvidualno` | `integer` | — | — | `open` | — | Asmens ID | — |
| `sex` | `integer` | `enum: sex` | — | `open` | — | Lytis | — |
| `age` | `integer` | — | — | `open` | — | Amžius | — |
| `isced2d` | `integer` | — | — | `open` | — | Įgytas aukščiausias išsilavinimas | — |
| `hatfield1` | `string` | — | — | `open` | — | Specialybė ar kvalifikacija, kurią Jūs įgijote | — |
| `iscdyear` | `integer` | — | — | `open` | — | Metai, kuriais įgytas aukščiausias išsilavinimas | — |
| `mainstat1` | `integer` | — | — | `open` | — | Dabartinis užimtumo statusas | — |
| `nace2d` | `integer` | — | — | `open` | — | Įmonės, kurioje dirbate, ekonominė veikla | — |
| `isco2d` | `integer` | — | — | `open` | — | Profesija | — |
| `fed` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. mokėtės formaliojo švietimo įstaigoje | — |
| `fedlev1` | `integer` | — | — | `open` | — | Kur Jūs mokėtės per pastaruosius 12 mėn? | — |
| `fedfiel1` | `integer` | — | — | `open` | — | Mokymo / studijų programa | — |
| `fedlen1` | `integer` | — | — | `open` | — | Valandų, praleistų besimokant, skaičius | — |
| `fedwrk_hr1` | `integer` | — | — | `open` | — | Ar mokėtės darbo metu? | — |
| `fedhouss1` | `integer` | — | — | `open` | — | Ar Jūs pats ar kuris nors Jūsų šeimos narys visiškai ar iš dalies mokėjo už Jūsų mokslą? | — |
| `fedinwests1` | `integer` | — | — | `open` | — | Suma, kurią Jūs ar Jūsų šeimos narys mokėjote už Jūsų mokslą? | — |
| `nfecourse` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. lankėte kursus (darbo laiku ar laisvalaikiu)? | — |
| `nfeworkshop` | `integer` | — | — | `open` | — | Ar per paskutinius 12 mėn. lankėte seminarus ir konferencijas? | — |
| `nfeguidedjt` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. buvote mokomas darbo vietoje? | — |
| `nfelesson` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. lankėte privačias pamokas? | — |
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
| `nfeval1` | `integer` | — | — | `open` | — | Ar pasinaudojote (tikitės pasinaudoti) mokymosi metu įgytomis žiniomis? | — |
| `difficulty` | `integer` | — | — | `open` | — | Sunkumai, susiję su mokymusi per paskutinius 12 mėnesių | — |
| `difftype_01` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes neturėjote reikalingų sugebėjimų | — |
| `difftype_02` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes mokymasis buvo per brangus | — |
| `difftype_03` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes trūko darbdavio paramos | — |
| `difftype_04` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes sunku buvo suderinti mokymosi ir darbo laiką | — |
| `difftype_05` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes mokymosi vieta buvo per toli | — |
| `difftype_06` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes neturėjote galimybės naudotis kompiuteriu ar internetu | — |
| `difftype_07` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes buvote per daug užimtas namuose | — |
| `difftype_08` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes trukdė sveikata, amžius | — |
| `difftype_09` | `integer` | — | — | `open` | — | Jūs nesimokėte, dėl kitų asmeninių priežasčių | — |
| `difftype_10` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes neradote tinkamų mokymų | — |
| `difftype_11` | `integer` | — | — | `open` | — | Jūs nesimokėte, nes nebuvo poreikio | — |
| `inf` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. Jūs bandėte savarankiškai mokytis? | — |
| `infmethod` | `integer` | — | — | `open` | — | Kokiu būdu Jūs mokėtės savarankiškai? | — |
| `lifeper` | `integer` | — | — | `open` | — | Kiek kartų per pastaruosius 12 mėn. lankėtės teatre, koncerte, muziejuje, operoje, balete | — |
| `cinema` | `integer` | — | — | `open` | — | Kiek kartų per pastaruosius 12 mėn. buvote kine | — |
| `cultsit` | `integer` | — | — | `open` | — | Kiek kartų per pastaruosius 12 mėn. lankėtės kultūros objektuose | — |
| `sport` | `integer` | — | — | `open` | — | Kiek kartų per pastaruosius 12 mėn. lankėtės sporto renginyje | — |
| `readbok` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. skaitėte grožinę literatūrą? | — |
| `readboknb` | `integer` | — | — | `open` | — | Kiek grožinės literatūros knygų perskaitėte? | — |
| `newspafq` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. skaitėte laikraščius? | — |
| `degurb` | `integer` | — | — | `open` | — | Urbanizacijos laipsnis | — |
| `weight` | `string` | — | — | `open` | — | Asmens populiacijos svoris | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `sex` | `1` | — | — | Vyras | — |
| `sex` | `2` | — | — | Moteris | — |
| `age` | `1` | — | — | 25–34 | — |
| `age` | `2` | — | — | 35–54 | — |
| `age` | `3` | — | — | 55 ir vyresni | — |
| `isced2d` | `1` | — | — | Žemesnis išsilavinimas (ISCED 1,2) | — |
| `isced2d` | `2` | — | — | Vidutinis išsilavinimas (ISCED 3,4) | — |
| `isced2d` | `3` | — | — | Aukštas išsilavinimas (ISCED 5,6) | — |
| `hatfield1` | `"0"` | — | — | Bendrosios programos | — |
| `hatfield1` | `"1"` | — | — | Mokytojų rengimas ir pedagogika; humanitariniai mokslai, kalbos ir menas | — |
| `hatfield1` | `"2"` | — | — | Socialiniai mokslai, verslas ir teisė | — |
| `hatfield1` | `"3"` | — | — | Gamtos mokslai, matematika ir kompiuterija; inžinerija, gamyba ir statyba | — |
| `hatfield1` | `"4"` | — | — | Žemės ūkis ir veterinarija | — |
| `hatfield1` | `"5"` | — | — | Sveikatos priežiūra ir socialinė apsauga; paslaugos | — |
| `iscdyear` | `1` | — | — | 1980-aisiais ir anksčiau | — |
| `iscdyear` | `2` | — | — | 1981–1989 | — |
| `iscdyear` | `3` | — | — | 1992-aisiais ir vėliau | — |
| `mainstat1` | `1` | — | — | Užimtas | — |
| `mainstat1` | `2` | — | — | Bedarbis | — |
| `mainstat1` | `3` | — | — | Neaktyvus | — |
| `nace2d` | `1` | — | — | Žemės ūkis, medžioklė, miškininkystė ir žuvininkystė; kasyba, karjerų eksplotavimas ir apdirbamoji pramonė | — |
| `nace2d` | `2` | — | — | Elektros, dujų, vandens tiekimas; statyba; didmeninė ir mažmeninė prekyba | — |
| `nace2d` | `3` | — | — | Apgyvendinimo ir maitinimo paslaugos; transportas ir saugojimas; informacija ir ryšiai; meninė, pramoginė ir poilsio organizavimo; kita aptarnavimo veikla; namų ūkių, samdančių darbininkus, veikla | — |
| `nace2d` | `4` | — | — | Finansinė ir draudimo veikla; nekilnojamojo turto operacijos; profesinė, mokslinė ir techninė veikla; administracinė ir aptarnavimo veikla; viešasis valdymas ir gynyba; švietimas; žmonių sveikatos priežiūra ir socialinis darbas | — |
| `isco2d` | `1` | — | — | Įstatymų leidėjai, vyresnieji pareigūnai, valdytojai, įmonių, istaigų, organizacijų ir kiti vadovai | — |
| `isco2d` | `2` | — | — | Specialistai | — |
| `isco2d` | `3` | — | — | Jaunesnieji specialistai, technikai ir tarnautojai | — |
| `isco2d` | `4` | — | — | Aptarnavimo srities ir prekybos darbuotojai | — |
| `isco2d` | `5` | — | — | Kvalifikuoti prekinio žemės ūkio ir žuvininkystės darbininkai, kvalifikuoti darbininkai ir amatininkai | — |
| `isco2d` | `6` | — | — | Įrenginių, mašinų operatoriai, surinkėjai ir nekvalifikuoti darbininkai | — |
| `fed` | `1` | — | — | Taip | — |
| `fed` | `2` | — | — | Ne | — |
| `fedlev1` | `1` | — | — | Žemesnis išsilavinimas (ISCED – 1, 2) | — |
| `fedlev1` | `2` | — | — | Vidutinis išsilavinimas (ISCED – 3, 4) | — |
| `fedlev1` | `3` | — | — | Aukštas išsilavinimas (ISCED – 5, 6) | — |
| `fedlev1` | `0` | — | — | Netaikoma | — |
| `fedfiel1` | `1` | — | — | Bendrosios programos, mokytojų rengimas ir pedagogika, humanitariniai mokslai, kalbos ir menas | — |
| `fedfiel1` | `2` | — | — | Socialiniai mokslai, verslas ir teisė | — |
| `fedfiel1` | `3` | — | — | Gamtos mokslai, matematika ir kompiuterija; inžinerija, gamyba ir statyba | — |
| `fedfiel1` | `4` | — | — | Žemės ūkis ir veterinarija; sveikatos priežiūra ir socialinė apsauga; paslaugos | — |
| `fedfiel1` | `0` | — | — | Netaikoma | — |
| `fedlen1` | `1` | — | — | 1 - 200 | — |
| `fedlen1` | `2` | — | — | 201 - 400 | — |
| `fedlen1` | `3` | — | — | 401 ir daugiau | — |
| `fedlen1` | `0` | — | — | Netaikoma | — |
| `fedwrk_hr1` | `1` | — | — | Tik mokamomis darbo valandomis arba dažniausiai mokamomis darbo valandomis | — |
| `fedwrk_hr1` | `2` | — | — | Dažniausiai nemokamomis darbo valandomis arba tik nemokamomis darbo valandomis | — |
| `fedwrk_hr1` | `3` | — | — | Tuo metu nedirbote | — |
| `fedwrk_hr1` | `0` | — | — | Netaikoma | — |
| `fedhouss1` | `1` | — | — | Taip | — |
| `fedhouss1` | `2` | — | — | Ne | — |
| `fedhouss1` | `0` | — | — | Netaikoma | — |
| `fedinwests1` | `1` | — | — | 1 - 500 | — |
| `fedinwests1` | `2` | — | — | 501 - 1000 | — |
| `fedinwests1` | `3` | — | — | 1001 ir daugiau | — |
| `fedinwests1` | `0` | — | — | Netaikoma | — |
| `nfecourse` | `1` | — | — | Taip | — |
| `nfecourse` | `2` | — | — | Ne | — |
| `nfeworkshop` | `1` | — | — | Taip | — |
| `nfeworkshop` | `2` | — | — | Ne | — |
| `nfeguidedjt` | `1` | — | — | Taip | — |
| `nfeguidedjt` | `2` | — | — | Ne | — |
| `nfelesson` | `1` | — | — | Taip | — |
| `nfelesson` | `2` | — | — | Ne | — |
| `nfe999` | `1` | — | — | 1 | — |
| `nfe999` | `2` | — | — | 2 | — |
| `nfe999` | `3` | — | — | 3-5 | — |
| `nfe999` | `4` | — | — | 6 ir daugiau | — |
| `nfe999` | `0` | — | — | Nei vienas | — |
| `nfepurp1` | `1` | — | — | Susijusios su darbu | — |
| `nfepurp1` | `2` | — | — | Asmeninės | — |
| `nfepurp1` | `0` | — | — | Netaikoma | — |
| `nferjob1` | `1` | — | — | Taip | — |
| `nferjob1` | `2` | — | — | Ne | — |
| `nferjob1` | `0` | — | — | Netaikoma | — |
| `nferlosj1` | `1` | — | — | Taip | — |
| `nferlosj1` | `2` | — | — | Ne | — |
| `nferlosj1` | `0` | — | — | Netaikoma | — |
| `nferprom1` | `1` | — | — | Taip | — |
| `nferprom1` | `2` | — | — | Ne | — |
| `nferprom1` | `0` | — | — | Netaikoma | — |
| `nfenbuis1` | `1` | — | — | Taip | — |
| `nfenbuis1` | `2` | — | — | Ne | — |
| `nfenbuis1` | `0` | — | — | Netaikoma | — |
| `nferobl1` | `1` | — | — | Taip | — |
| `nferobl1` | `2` | — | — | Ne | — |
| `nferobl1` | `0` | — | — | Netaikoma | — |
| `nferskil1` | `1` | — | — | Taip | — |
| `nferskil1` | `2` | — | — | Ne | — |
| `nferskil1` | `0` | — | — | Netaikoma | — |
| `nfersub1` | `1` | — | — | Taip | — |
| `nfersub1` | `2` | — | — | Ne | — |
| `nfersub1` | `0` | — | — | Netaikoma | — |
| `nfercer1` | `1` | — | — | Taip | — |
| `nfercer1` | `2` | — | — | Ne | — |
| `nfercer1` | `0` | — | — | Netaikoma | — |
| `nferfun1` | `1` | — | — | Taip | — |
| `nferfun1` | `2` | — | — | Ne | — |
| `nferfun1` | `0` | — | — | Netaikoma | — |
| `nfewrk_hr1` | `1` | — | — | Tik mokamomis darbo valandomis arba dažniausiai mokamomis darbo valandomis | — |
| `nfewrk_hr1` | `2` | — | — | Dažniausiai nemokamomis darbo valandomis arba tik nemokamomis darbo valandomis | — |
| `nfewrk_hr1` | `3` | — | — | Tuo metu nedirbote | — |
| `nfewrk_hr1` | `0` | — | — | Netaikoma | — |
| `nfeemsups1` | `1` | — | — | Taip | — |
| `nfeemsups1` | `2` | — | — | Ne | — |
| `nfeemsups1` | `0` | — | — | Netaikoma | — |
| `nfehouss1` | `1` | — | — | Taip | — |
| `nfehouss1` | `2` | — | — | Ne | — |
| `nfehouss1` | `0` | — | — | Netaikoma | — |
| `nfeval1` | `1` | — | — | Taip, labai daug | — |
| `nfeval1` | `2` | — | — | Šiek tiek | — |
| `nfeval1` | `3` | — | — | Labai nedaug arba visai nepasinaudojau ir nesitikiu pasinaudoti | — |
| `nfeval1` | `0` | — | — | Netaikoma | — |
| `difficulty` | `1` | — | — | Jūs mokėtės formaliame ar neformaliame švietime ir daugiau mokytis nenorėjote | — |
| `difficulty` | `2` | — | — | Jūs mokėtės formaliame a neformaliame švietime ir norėjote papildomai mokytis | — |
| `difficulty` | `3` | — | — | Jūs nesimokėte formaliane ar neformaliame švietime ir mokytis nenorėjote | — |
| `difficulty` | `4` | — | — | Jūs nesimokėte formaliame ar neformaliame švietime, bet norėjote mokytis | — |
| `difftype_01` | `1` | — | — | Taip | — |
| `difftype_01` | `2` | — | — | Ne | — |
| `difftype_02` | `1` | — | — | Taip | — |
| `difftype_02` | `2` | — | — | Ne | — |
| `difftype_03` | `1` | — | — | Taip | — |
| `difftype_03` | `2` | — | — | Ne | — |
| `difftype_04` | `1` | — | — | Taip | — |
| `difftype_04` | `2` | — | — | Ne | — |
| `difftype_05` | `1` | — | — | Taip | — |
| `difftype_05` | `2` | — | — | Ne | — |
| `difftype_06` | `1` | — | — | Taip | — |
| `difftype_06` | `2` | — | — | Ne | — |
| `difftype_07` | `1` | — | — | Taip | — |
| `difftype_07` | `2` | — | — | Ne | — |
| `difftype_08` | `1` | — | — | Taip | — |
| `difftype_08` | `2` | — | — | Ne | — |
| `difftype_09` | `1` | — | — | Taip | — |
| `difftype_09` | `2` | — | — | Ne | — |
| `difftype_10` | `1` | — | — | Taip | — |
| `difftype_10` | `2` | — | — | Ne | — |
| `difftype_11` | `1` | — | — | Taip | — |
| `difftype_11` | `2` | — | — | Ne | — |
| `inf` | `1` | — | — | Taip, vienos veiklos | — |
| `inf` | `2` | — | — | Taip, bent dviejų veiklų | — |
| `inf` | `3` | — | — | Ne | — |
| `infmethod` | `1` | — | — | Bandėte mokytis iš šeimos nario, draugo, kolegos | — |
| `infmethod` | `2` | — | — | Bandėte mokytis iš knygų, specialybės žurnalų | — |
| `infmethod` | `3` | — | — | Bandėte mokytis naudodami kompiuterį ir/ar internetą | — |
| `infmethod` | `4` | — | — | Bandėte mokytis žiūrėdami mokomąsias televizijos laidas, naudojotės garso ir vaizdo juostomis arba kompaktiniais diskais | — |
| `infmethod` | `0` | — | — | Netaikoma | — |
| `lifeper` | `1` | — | — | 1–6 kartus | — |
| `lifeper` | `2` | — | — | Daugiau nei 6 kartus | — |
| `lifeper` | `3` | — | — | Nesilankėte | — |
| `cinema` | `1` | — | — | 1–6 kartus | — |
| `cinema` | `2` | — | — | Daugiau nei 6 kartus | — |
| `cinema` | `3` | — | — | Nesilankėte | — |
| `cultsit` | `1` | — | — | 1–6 kartus | — |
| `cultsit` | `2` | — | — | Daugiau nei 6 kartus | — |
| `cultsit` | `3` | — | — | Nesilankėte | — |
| `sport` | `1` | — | — | 1–6 kartus | — |
| `sport` | `2` | — | — | Daugiau nei 6 kartus | — |
| `sport` | `3` | — | — | Nesilankėte | — |
| `readbok` | `1` | — | — | Taip | — |
| `readbok` | `2` | — | — | Ne | — |
| `readboknb` | `1` | — | — | 1–4 | — |
| `readboknb` | `2` | — | — | 5–9 | — |
| `readboknb` | `3` | — | — | Daugiau nei 9 knygas | — |
| `newspafq` | `1` | — | — | Kasdien arba beveik kasdien | — |
| `newspafq` | `2` | — | — | Bent kartą per savaitę | — |
| `newspafq` | `3` | — | — | Bent kartą per mėnesį | — |
| `newspafq` | `4` | — | — | Mažiau nei kartą per mėnesį | — |
| `newspafq` | `5` | — | — | Niekada | — |
| `degurb` | `1` | — | — | Tankiai apgyvendinta vietovė | — |
| `degurb` | `2` | — | — | Vidutiniškai apgyvendinta vietovė | — |
| `degurb` | `3` | — | — | Menkai apgyvendinta vietovė | — |

# Related References

- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/svietimas.csv#L374 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/svietimas.csv#L374)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/svietimas/suaugusiuju (https://data.gov.lt/datasets/1621/)
