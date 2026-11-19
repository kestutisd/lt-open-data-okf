---
type: Table
title: "GyventojuSveikata2014 — Gyventojų sveikatos statistinis tyrimas 2014 m."
description: "2014 metais atliktas gyventojų sveikatos statistinis tyrimas"
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/GyventojuSveikata2014"
tags: [gov, lsd, gyventojusveikata2014, deployed, cadence-quinquennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1622/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# GyventojuSveikata2014 — Gyventojų sveikatos statistinis tyrimas 2014 m.

2014 metais atliktas gyventojų sveikatos statistinis tyrimas[^manifest]

- **Model:** `datasets/gov/lsd/sveikata/GyventojuSveikata2014`[^manifest]
- **Dataset:** [Gyventojų sveikatos statistinio tyrimo duomenys](../sveikata.md) (`datasets/gov/lsd/sveikata`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/GyventojuSveikata2014` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUINQUENNIAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pid` | `integer` | — | — | `open` | — | Respondento identifikacinis numeris | — |
| `wgt` | `string` | — | — | `open` | — | Asmens populiacijos svoris | — |
| `proxy` | `integer` | — | — | `open` | — | Dalyvavimo tyrime pobūdis | — |
| `refyear` | `integer` | — | — | `open` | — | Apklausos ataskaitiniai metai | — |
| `refmonth` | `integer` | — | — | `open` | — | Apklausos ataskaitinis mėnuo | — |
| `sex` | `integer` | `enum: sex` | — | `open` | — | Lytis | — |
| `age` | `integer` | — | — | `open` | — | Amžius | — |
| `birthplace` | `integer` | — | — | `open` | — | Gimimo šalis | — |
| `citizen` | `integer` | — | — | `open` | — | Pilietybė | — |
| `ap` | `integer` | — | — | `open` | — | Apskritys | — |
| `deg_urb` | `integer` | — | — | `open` | — | Urbanizacijos laipsnis | — |
| `m_k` | `integer` | — | — | `open` | — | Miestas ar kaimas | — |
| `marstalegal` | `integer` | — | — | `open` | — | Juridinė santuokinė padėtis | — |
| `hatlevel` | `integer` | — | — | `open` | — | Įgytas aukščiausias išsilavinimas (ISCED 2011) | — |
| `mainstat` | `integer` | — | — | `open` | — | Užimtumo statusas | — |
| `ft_pt` | `integer` | — | — | `open` | — | Dirba visą ar ne visą darbo dienos ar savaitės laiką | — |
| `jobstat` | `integer` | — | — | `open` | — | Užimtumo statusas | — |
| `jobisco` | `integer` | — | — | `open` | — | Profesija | — |
| `locnace` | `string` | — | — | `open` | — | Pagrindinė darbovietės ekonominės veiklos rūšis | — |
| `hhnbpers` | `integer` | — | — | `open` | — | Namų ūkio narių skaičius (įskaitant respondentą) | — |
| `hhnbpers_0_4` | `integer` | — | — | `open` | — | 4 metų ir jaunesnių vaikų skaičius namų ūkyje | — |
| `hhnbpers_5_13` | `integer` | — | — | `open` | — | 5 − 13 metų amžiaus vaikų skaičius namų ūkyje | — |
| `hhnbpers_14_15` | `integer` | — | — | `open` | — | 14 − 15 metų amžiaus vaikų skaičius namų ūkyje | — |
| `hhnbpers_16_24` | `integer` | — | — | `open` | — | 16 − 24 metų amžiaus asmenų skaičius namų ūkyje | — |
| `hhnbpers_25_64` | `integer` | — | — | `open` | — | 25 − 64 metų amžiaus asmenų skaičius namų ūkyje | — |
| `hhnbpers_65plus` | `integer` | — | — | `open` | — | 65 metų ir vyresnių asmenų skaičius namų ūkyje | — |
| `hhtype` | `integer` | — | — | `open` | — | Namų ūkio tipas | — |
| `hh_act` | `integer` | — | — | `open` | — | Dirbančių 16 - 64 metų amžiaus asmenų skaičius namų ūkyje | — |
| `hh_inact` | `integer` | — | — | `open` | — | Nedirbančių ir ekonomiškai neaktyvių 16 - 64 metų amžiaus asmenų skaičius namų ūkyje | — |
| `hhincome` | `integer` | — | — | `open` | — | Namų ūkio grynosios mėnesio ekvivalentinės pajamos | — |
| `hs1` | `integer` | — | — | `open` | — | Kaip apibūdintumėte savo sveikatą? | — |
| `hs2` | `integer` | — | — | `open` | — | Ar Jūs sergate kokia nors lėtine (chroniška) liga arba turite ilgalaikių sveikatos sutrikimų? (Ilgalaike vadinama liga ar sveikatos sutrikimas, kuris truko ar, tikėtina, kad truks mažiausiai 6 mėn.) | — |
| `hs3` | `integer` | — | — | `open` | — | Ar per pastaruosius bent 6 mėn. Jūsų veikla, palyginti su įprastine žmogaus veikla, buvo apribota dėl sveikatos sutrikimų? Ar sakytumėte, kad ji buvo... | — |
| `cd1a` | `integer` | `bool` | — | `open` | — | a) Astma (įskaitant alerginę astmą) | — |
| `cd1b` | `integer` | `bool` | — | `open` | — | b) Lėtinis bronchitas, lėtinė obstrukcinė plaučių liga, emfizema | — |
| `cd1c` | `integer` | `bool` | — | `open` | — | c) Miokardo infarktas (širdies smūgis) arba infarkto lėtinės pasekmės | — |
| `cd1d` | `integer` | `bool` | — | `open` | — | d) Koronarinė širdies liga ar krūtinės angina | — |
| `cd1e` | `integer` | `bool` | — | `open` | — | e) Aukštas kraujospūdis (hipertenzija) | — |
| `cd1f` | `integer` | `bool` | — | `open` | — | f) Galvos smegenų insultas (kraujo išsiliejimas į smegenis, smegenų trombozė) arba insulto lėtinės pasekmės | — |
| `cd1g` | `integer` | `bool` | — | `open` | — | g) Artrozė (išskyrus artritą) | — |
| `cd1h` | `integer` | `bool` | — | `open` | — | h) Apatinės nugaros dalies liga ar kitos lėtinės nugaros problemos | — |
| `cd1i` | `integer` | `bool` | — | `open` | — | i) Kaklo srities liga ar kitos lėtinės kaklo problemos | — |
| `cd1j` | `integer` | `bool` | — | `open` | — | j) Cukrinis diabetas | — |
| `cd1k` | `integer` | `bool` | — | `open` | — | k) Alergija, tokia kaip alerginė sloga (šienligė), akių uždegimas, dermatitas, alergija maistui ar kita alergija (išskyrus alerginę astmą) | — |
| `cd1l` | `integer` | `bool` | — | `open` | — | l) Kepenų cirozė | — |
| `cd1m` | `integer` | `bool` | — | `open` | — | m) Šlapimo nelaikymas, šlapimo pūslės kontrolės problemos | — |
| `cd1n` | `integer` | `bool` | — | `open` | — | n) Inkstų problemos | — |
| `cd1o` | `integer` | `bool` | — | `open` | — | o) Depresija | — |
| `ac1a` | `integer` | `bool` | — | `open` | — | a) Kelių eismo įvykis | — |
| `ac1b` | `integer` | `bool` | — | `open` | — | b) Nelaimingas atsitikimas namuose | — |
| `ac1c` | `integer` | `bool` | — | `open` | — | c) Nelaimingas atsitikimas laisvalaikio metu | — |
| `ac2` | `integer` | — | — | `open` | — | Ar dėl šio nelaimingo atsitikimo Jums reikėjo medicinos pagalbos? | — |
| `aw1` | `integer` | — | — | `open` | — | Ar per pastaruosius 12 mėn. pasitaikė atvejų, kai nedirbote dėl savo sveikatos problemų? (Pagalvokite apie visas ligas, sužeidimus ir kitas sveikatos problemas, kurių turėjote ir dėl kurių nedirbote) | — |
| `aw2` | `integer` | — | — | `open` | — | Kiek iš viso dienų per pastaruosius 12 mėn. nedirbote dėl savo sveikatos problemų? | — |
| `pl1` | `integer` | — | — | `open` | — | Ar nešiojate akinius ar kontaktinius lęšius? | — |
| `pl2` | `integer` | — | — | `open` | — | Jei PL1 = 1: Ar prastai matote net nešiodamas (-a) akinius ar kontaktinius lęšius? / Jei PL1 = 2: Ar prastai matote (ar turite regėjimo sutrikimų)? | — |
| `pl3` | `integer` | — | — | `open` | — | Ar naudojatės klausos aparatu? | — |
| `pl4` | `integer` | — | — | `open` | — | Jei PL3 = 1: Ar bendraudamas (-a) su kitu asmeniu, kai kambaryje tylu, prastai girdite net jei naudojatės klausos aparatu? / Jei PL3 = 2: Ar bendraudamas (-a) su kitu asmeniu, kai kambaryje tylu prastai girdite? | — |
| `pl5` | `integer` | — | — | `open` | — | Jei PL3 = 1: Ar bendraudamas (-a) su kitu asmeniu, kai kambaryje triukšminga, prastai girdite net jei naudojatės klausos aparatu? / Jei PL3 = 2: Ar bendraudamas (-a) su kitu asmeniu, kai kambaryje triukšminga, prastai girdite? | — |
| `pl6` | `integer` | — | — | `open` | — | Ar Jums sunku lygiu paviršiumi be lazdos ar kitos vaikščiojimą lengvinančios priemonės nueiti pusės kilometro atstumą? | — |
| `pl7` | `integer` | — | — | `open` | — | Ar Jums sunku užlipti ar nulipti 12 laiptelių? | — |
| `pc1a` | `integer` | — | — | `open` | — | a) Pavalgyti | — |
| `pc1b` | `integer` | — | — | `open` | — | b) Atsigulti į lovą ar atsikelti iš jos, atsisėsti ant kėdės ar pasikelti nuo jos | — |
| `pc1c` | `integer` | — | — | `open` | — | c) Apsirengti ir nusirengti | — |
| `pc1d` | `integer` | — | — | `open` | — | d) Naudotis tualetu | — |
| `pc1e` | `integer` | — | — | `open` | — | e) Maudytis vonioje ar duše | — |
| `pc2` | `integer` | — | — | `open` | — | Ar paprastai Jums kas nors padeda atlikti šiuos veiksmus (PC1A - PC1E)? | — |
| `pc3` | `integer` | — | — | `open` | — | Jei PC2 = 1: Ar Jums reikia daugiau pagalbos? / Jei PC2 = 2: Ar Jums reikalinga pagalba? | — |
| `ha1a` | `integer` | — | — | `open` | — | a) Ruošti valgį | — |
| `ha1b` | `integer` | — | — | `open` | — | b) Naudotis telefonu | — |
| `ha1c` | `integer` | — | — | `open` | — | c) Apsipirkti | — |
| `ha1d` | `integer` | — | — | `open` | — | d) Vartoti vaistus | — |
| `ha1e` | `integer` | — | — | `open` | — | e) Atlikti lengvus namų ruošos darbus | — |
| `ha1f` | `integer` | — | — | `open` | — | f) Retkarčiais atlikti sunkius namų ruošos darbus | — |
| `ha1g` | `integer` | — | — | `open` | — | g) Tvarkyti finansus ir kasdienes administracines užduotis | — |
| `ha2` | `integer` | — | — | `open` | — | Ar Jums paprastai kas nors padeda atlikti šiuos darbus (HA1A - HA1G)? | — |
| `ha3` | `integer` | — | — | `open` | — | Jei HA2 = 1: Ar Jums reikia daugiau pagalbos? / Jei HA2 = 2: Ar Jums reikalinga pagalba? | — |
| `pn1` | `integer` | — | — | `open` | — | Kokio intensyvumo kūno skausmą jautėte per pastarąsias 4 savaites? | — |
| `pn2` | `integer` | — | — | `open` | — | Ar per pastarąsias 4 savaites skausmas trukdė vykdyti įprastą veiklą (tiek dirbti ne namie, tiek atlikti namų ruošos darbus)? | — |
| `mh1a` | `integer` | — | — | `open` | — | a) Įprasta veikla mažai domino ar teikė mažai malonumo | — |
| `mh1b` | `integer` | — | — | `open` | — | b) Jautėtės nusiminęs (-usi), prislėgtas (-a) ar nusivylęs (-usi) | — |
| `mh1c` | `integer` | — | — | `open` | — | c) Buvo sunku užmigti, kankino nemiga arba miegojote per ilgai | — |
| `mh1d` | `integer` | — | — | `open` | — | d) Jautėte nuovargį, energijos trūkumą | — |
| `mh1e` | `integer` | — | — | `open` | — | e) Neturėjote apetito arba persivalgėte | — |
| `mh1f` | `integer` | — | — | `open` | — | f) Jautėtės blogai, manėte, kad esate nevykėlis (-ė), nuvylėte savo šeimą arba nusivylėte savimi | — |
| `mh1g` | `integer` | — | — | `open` | — | g) Buvo sunku susitelkti kokiai nors veiklai, pvz., skaityti laikraštį ar žiūrėti televizorių | — |
| `mh1h` | `integer` | — | — | `open` | — | h) Judėjote ar kalbėjote taip lėtai, kad kiti žmonės atkreipė į tai dėmesį. Arba atvirkščiai – buvote toks (-ia) neramus (-i) ir nenustygstantis (-i), todėl judėjote žymiai daugiau nei įprastai | — |
| `ho1` | `integer` | `bool` | — | `open` | — | Ar per pastaruosius 12 mėn. buvote paguldytas (-a) į ligoninę ir joje praleidote mažiausiai vieną naktį? (Neįskaitant apsilankymų skubios pagalbos skyriuje (neliekant jame nakvoti) ar kitoje ambulatorinėje įstaigoje) | — |
| `ho2` | `integer` | — | — | `open` | — | Kiek iš viso naktų Jūs praleidote ligoninėje? | — |
| `ho3` | `integer` | `bool` | — | `open` | — | Ar per pastaruosius 12 mėn. buvote paguldytas (-a) į dienos stacionarą, t. y. buvote paguldytas (-a) į ligoninę diagnozei nustatyti, gydymui ar kitoms procedūroms, bet Jums nereikėjo likti nakvoti? | — |
| `ho4` | `integer` | — | — | `open` | — | Kiek kartų per pastaruosius 12 mėn. gydėtės dienos stacionare? | — |
| `am1` | `integer` | — | — | `open` | — | Kada paskutinį kartą lankėtės pas odontologą (dantų gydytoją) ar ortodontą dėl savo sveikatos (t. y. neįskaitant tų atvejų, kai lydėjote vaiką ar sutuoktinį (-ę) ir kt.)? | — |
| `am2` | `integer` | — | — | `open` | — | Kada paskutinį kartą kreipėtės į bendrosios praktikos ar šeimos gydytoją dėl savo sveikatos? | — |
| `am3` | `integer` | — | — | `open` | — | Kiek kartų per pastarąsias 4 savaites kreipėtės į bendrosios praktikos ar šeimos gydytoją dėl savo sveikatos? | — |
| `am4` | `integer` | — | — | `open` | — | Kada paskutinį kartą kreipėtės į gydytoją specialistą ar chirurgą dėl savo sveikatos? (Įskaitant apsilankymus pas odontologą-chirurgą, bet neįskaitant apsilankymų pas odontologą) | — |
| `am5` | `integer` | — | — | `open` | — | Kiek kartų per pastarąsias 4 savaites kreipėtės į gydytoją specialistą ar chirurgą dėl savo sveikatos? | — |
| `am6a` | `integer` | `bool` | — | `open` | — | a) Fizioterapeutą ar kineziterapeutą | — |
| `am6b` | `integer` | `bool` | — | `open` | — | b) Psichologą, psichiatrą ar psichoterapeutą | — |
| `am7` | `integer` | `bool` | — | `open` | — | Ar per pastaruosius 12 mėn. Jūs pats (-i) naudojotės priežiūros namuose paslaugomis? (Gydytojo vizitai į namus neįskaitomi) | — |
| `md1` | `integer` | — | — | `open` | — | Ar per pastarąsias 2 savaites vartojote gydytojo Jums išrašytų (receptinių) vaistų? (Moterims neįskaitant kontraceptinių piliulių ir kitų hormoninių preparatų) | — |
| `md2` | `integer` | — | — | `open` | — | Ar per pastarąsias 2 savaites vartojote kokių nors Jums gydytojo neišrašytų vaistų, vaistažolių preparatų, vitaminų? | — |
| `pa1` | `string` | — | — | `open` | — | Kada paskutinį kartą skiepijotės nuo gripo? | — |
| `pa2` | `integer` | — | — | `open` | — | a) Kraujospūdį | — |
| `pa3` | `integer` | — | — | `open` | — | b) Cholesterolio kiekį kraujyje | — |
| `pa4` | `integer` | — | — | `open` | — | c) Cukraus kiekį kraujyje | — |
| `pa5` | `integer` | — | — | `open` | — | Kada paskutinį kartą Jums buvo atliktas slapto kraujavimo (kraujo likučių išmatose) tyrimas? (Testas kraujavimui virškinimo trakte nustatyti) | — |
| `pa6` | `integer` | — | — | `open` | — | Kada paskutinį kartą Jums darė kolonoskopiją (endoskopinį žarnyno tyrimą)? (Žarnyno apžiūra kolonoskopu) | — |
| `pa7` | `integer` | — | — | `open` | — | Kada paskutinį kartą Jums buvo atlikta mamografija (krūtų rentgenograma)? ( Atsakė tik moterys). | — |
| `pa8` | `integer` | — | — | `open` | — | Kada paskutinį kartą Jums buvo tirtas gimdos kaklelio tepinėlis (atliktas PAP testas)? (Atsakė tik moterys). | — |
| `un1a` | `integer` | — | — | `open` | — | a) ilgos eilės (buvo sunku gauti taloną, nukreipimą ir kt.) | — |
| `un1b` | `integer` | — | — | `open` | — | b) atstumo ar transporto problemų | — |
| `un2a` | `integer` | — | — | `open` | — | a) Gydytojo paslaugų (išskyrus odontologo) | — |
| `un2b` | `integer` | — | — | `open` | — | b) Odontologo (dantų gydytojo) paslaugų | — |
| `un2c` | `integer` | — | — | `open` | — | c) Gydytojo išrašytų vaistų | — |
| `un2d` | `integer` | — | — | `open` | — | d) Psichikos sveikatos paslaugų (pvz., teikiamų psichologo ar psichiatro) | — |
| `bm1` | `integer` | — | — | `open` | — | Koks Jūsų ūgis? | — |
| `bm2` | `integer` | — | — | `open` | — | Koks Jūsų svoris? | — |
| `pe1` | `integer` | — | — | `open` | — | Kas geriausiai apibūdintų tai, ką veikiate dirbdamas (-a)? | — |
| `pe2` | `integer` | — | — | `open` | — | Kiek paprastai dienų per savaitę einate pėsčiomis į tam tikras vietas ir grįžtate iš jų užtrukdamas (-a) mažiausiai 10 min. be pertraukos? | — |
| `pe3` | `integer` | — | — | `open` | — | Kiek paprastai laiko per dieną užtrunkate eidamas (-a) pėsčiomis į tam tikras vietas ir grįždamas (-a) iš jų? | — |
| `pe4` | `integer` | — | — | `open` | — | Kiek paprastai dienų per savaitę važiuojate dviračiu į tam tikras vietas ir grįžtate iš jų užtrukdamas (-a) mažiausiai 10 min. be pertraukos? | — |
| `pe5` | `integer` | — | — | `open` | — | Kiek paprastai laiko per dieną užtrunkate važiuodamas (-a) dviračiu į tam tikras vietas ir grįždamas (-a) iš jų? | — |
| `pe6` | `integer` | — | — | `open` | — | Kiek paprastai dienų per savaitę sportuojate, užsiimate kūno rengyba ar aktyvia laisvalaikio veikla mažiausiai 10 min. be pertraukos? | — |
| `pe7` | `string` | — | — | `open` | — | Kiek paprastai laiko per savaitę sportuojate, užsiimate kūno rengyba ar aktyvia laisvalaikio veikla? | — |
| `pe8` | `integer` | — | — | `open` | — | Kiek paprastai dienų per savaitę atliekate konkrečius veiksmus, skirtus sustiprinti raumenis, pvz., darote ištvermės ar jėgos pratimus? | — |
| `fv1` | `integer` | — | — | `open` | — | Kaip dažnai valgote vaisius? (Įskaitant šviežių vaisių sultis, bet neįskaitant sulčių, pagamintų iš koncentrato ar perdirbtų vaisių) | — |
| `fv2` | `integer` | — | — | `open` | — | Kiek bet kokios rūšies vaisių porcijų suvalgote kiekvieną dieną? | — |
| `fv3` | `integer` | — | — | `open` | — | Kaip dažnai valgote daržoves ar salotas (išskyrus bulves ir iš koncentrato pagamintas sultis)? (Įskaitant šiltas ir šaltas daržovių sriubas ir šviežių daržovių sultis) | — |
| `fv4` | `integer` | — | — | `open` | — | Kiek daržovių ar salotų porcijų suvalgote kiekvieną dieną? | — |
| `sk1` | `integer` | — | — | `open` | — | Ar Jūs rūkote? | — |
| `sk2` | `integer` | — | — | `open` | — | Kokius tabako gaminius dažniausiai rūkote? | — |
| `sk3` | `integer` | — | — | `open` | — | Kiek vidutiniškai cigarečių surūkote kiekvieną dieną? | — |
| `sk4` | `integer` | — | — | `open` | — | Kaip dažnai tenka būti prirūkytose patalpose? | — |
| `al1` | `integer` | — | — | `open` | — | Kaip dažnai per pastaruosius 12 mėn. vartojote bet kokios rūšies alkoholinius gėrimus (alų, vyną, sidrą, stipriuosius gėrimus, kokteilius, likerį, namų gamybos alkoholinius gėrimus ir pan.)? | — |
| `al2` | `integer` | — | — | `open` | — | Prašau pagalvoti apie dienas nuo pirmadienio iki ketvirtadienio. Kiek paprastai iš šių 4 dienų vartojate alkoholį? | — |
| `al3` | `integer` | — | — | `open` | — | Nuo pirmadienio iki ketvirtadienio, kai vartojate alkoholį, kiek alkoholinių gėrimų Jūs vidutiniškai išgeriate per dieną? | — |
| `al4` | `integer` | — | — | `open` | — | Prašau pagalvoti apie dienas nuo penktadienio iki sekmadienio. Kiek paprastai iš šių 3 dienų vartojate alkoholį? | — |
| `al5` | `integer` | — | — | `open` | — | Nuo penktadienio iki sekmadienio, kai vartojate alkoholį, kiek alkoholinių gėrimų Jūs vidutiniškai išgeriate per dieną? | — |
| `al6` | `integer` | — | — | `open` | — | Kaip dažnai per pastaruosius 12 mėn. pasitaikė atvejų, kai viena proga išgėrėte 1,5 litro ar daugiau alaus, 6 taures (600 ml) ar daugiau vyno arba 5 taureles (200 ml) ar daugiau degtinės, arba kitų stiprių alkoholinių gėrimų? Pvz., pobūvyje, vakarieniaudamas (-a), pramogaudamas (-a) su draugais ar namuose būdamas (-a) vienas (-a) ir t. t. (Nurodytas alkoholio kiekis prilygsta 6 ir daugiau SAV) | — |
| `ss1` | `integer` | — | — | `open` | — | Kiek turite artimų žmonių, kuriais galėtumėte pasikliauti kilus rimtai asmeninei problemai? | — |
| `ss2` | `integer` | — | — | `open` | — | Kiek artimieji (šeimos nariai, draugai ir kt.) domisi tuo, ką Jūs veikiate? | — |
| `ss3` | `integer` | — | — | `open` | — | Ar Jums būtų lengva gauti praktiškos pagalbos iš kaimynų, jei jos prireiktų? (Pvz., atliekant darbus, kai reikia patarimo, pinigų ir kt.) | — |
| `ic1` | `integer` | — | — | `open` | — | Ar Jūs bent kartą per savaitę prižiūrite ar padedate vienam ar daugiau asmenų, turinčių su senatve, lėtiniais susirgimais ar negalia susijusių problemų? (Neįskaitant priežiūros, kuri yra Jūsų tiesioginis darbas) | — |
| `ic2` | `integer` | — | — | `open` | — | Ar šis asmuo (asmenys) yra: | — |
| `ic3` | `integer` | — | — | `open` | — | Kiek valandų per savaitę prižiūrite ar padedate šiam asmeniui (šiems asmenims)? | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `proxy` | `1` | — | — | Pats respondentas | — |
| `proxy` | `2` | — | — | Už respondentą atsakė kitas to paties namų ūkio narys | — |
| `proxy` | `3` | — | — | Už respondentą atsakė kito namų ūkio narys | — |
| `sex` | `1` | — | — | Vyras | — |
| `sex` | `2` | — | — | Moteris | — |
| `sex` | `1` | — | — | Taip | — |
| `sex` | `2` | — | — | Ne | — |
| `birthplace` | `10` | — | — | Lietuvos Respublika | — |
| `birthplace` | `21` | — | — | ES šalis | — |
| `birthplace` | `22` | — | — | Ne ES šalis | — |
| `citizen` | `10` | — | — | Lietuvos Respublikos | — |
| `citizen` | `21` | — | — | Kitos ES šalies | — |
| `citizen` | `22` | — | — | Ne ES šalies | — |
| `ap` | `1` | — | — | Alytaus apskritis | — |
| `ap` | `2` | — | — | Kauno apskritis | — |
| `ap` | `3` | — | — | Klaipėdos apskritis | — |
| `ap` | `4` | — | — | Marijampolės apskritis | — |
| `ap` | `5` | — | — | Panevėžio apskritis | — |
| `ap` | `6` | — | — | Šiaulių apskritis | — |
| `ap` | `7` | — | — | Tauragės apskritis | — |
| `ap` | `8` | — | — | Telšių apskritis | — |
| `ap` | `9` | — | — | Utenos apskritis | — |
| `ap` | `10` | — | — | Vilniaus apskritis | — |
| `deg_urb` | `1` | — | — | Tankiai apgyvendinta vietovė | — |
| `deg_urb` | `2` | — | — | Vidutiniškai apgyvendinta vietovė | — |
| `deg_urb` | `3` | — | — | Menkai apgyvendinta vietovė | — |
| `m_k` | `1` | — | — | Miestas | — |
| `m_k` | `2` | — | — | Kaimas | — |
| `marstalegal` | `1` | — | — | Niekada nebuvo vedęs (ištekėjusi) | — |
| `marstalegal` | `2` | — | — | Vedęs (ištekėjusi) | — |
| `marstalegal` | `3` | — | — | Našlys (-ė) | — |
| `marstalegal` | `4` | — | — | Išsituokęs (-usi) | — |
| `hatlevel` | `0` | — | — | Neturi pradinio (ISCED 0) | — |
| `hatlevel` | `1` | — | — | Pradinis išsilavinimas (ISCED 1) | — |
| `hatlevel` | `2` | — | — | Pagrindinis išsilavinimas (ISCED 2) | — |
| `hatlevel` | `3` | — | — | Vidurinis išsilavinimas (ISCED 3) | — |
| `hatlevel` | `4` | — | — | Profesinis mokymas turint vidurinį išsilavinimą (ISCED 4) | — |
| `hatlevel` | `6` | — | — | Bakalauro studijos (ISCED 6) | — |
| `hatlevel` | `7` | — | — | Magistrantūros studijos (ISCED 7) | — |
| `hatlevel` | `8` | — | — | Doktorantūra (ISCED 8) | — |
| `mainstat` | `10` | — | — | Samdomasis darbuotojas arba savarankiškai dirbantis asmuo (įskaitant šeimos versle dirbančius ir atlyginimo negaunančius asmenis) | — |
| `mainstat` | `20` | — | — | Bedarbis (-ė) | — |
| `mainstat` | `31` | — | — | Mokinys (-ė), nedirbantis (-i) studentas (-ė) | — |
| `mainstat` | `32` | — | — | Nedirbantis (-i) senatvės pensininkas (-ė) | — |
| `mainstat` | `33` | — | — | Dėl negalios nedirbantis asmuo | — |
| `mainstat` | `34` | — | — | Atliekantis privalomąją karo ar alternatyviąją tarnybą | — |
| `mainstat` | `35` | — | — | Namų šeimininkas (-ė) | — |
| `mainstat` | `36` | — | — | Kitas neaktyvus asmuo | — |
| `ft_pt` | `1` | — | — | Visą | — |
| `ft_pt` | `2` | — | — | Ne visą | — |
| `ft_pt` | `-2` | — | — | Netaikoma | — |
| `jobstat` | `10` | — | — | Savarankiškai dirbantis asmuo | — |
| `jobstat` | `21` | — | — | Samdomasis darbuotojas (-a), dirbantis (-i) pagal neterminuotą darbo sutartį | — |
| `jobstat` | `22` | — | — | Samdomasis darbuotojas (-a), dirbantis (-i) pagal terminuotą darbo sutartį, žodinį susitarimą | — |
| `jobstat` | `-2` | — | — | Netaikoma | — |
| `hhtype` | `10` | — | — | Vienas asmuo | — |
| `hhtype` | `21` | — | — | Viena motina ar vienas tėvas su vaiku (-ais) iki 25 metų amžiaus | — |
| `hhtype` | `22` | — | — | Pora, neturinti vaiko (-ų) iki 25 metų amžiaus | — |
| `hhtype` | `23` | — | — | Pora su vaiku (-ais) iki 25 metų amžiaus | — |
| `hhtype` | `24` | — | — | Pora arba viena motina (tėvas) su vaiku (-ais) iki 25 metų amžiaus ir kitais kartu gyvenančiais asmenimis | — |
| `hhtype` | `25` | — | — | Kita | — |
| `hhincome` | `1` | — | — | Mažesnės nei pirmojo kvintilio | — |
| `hhincome` | `2` | — | — | Tarp pirmojo ir antrojo kvintilių | — |
| `hhincome` | `3` | — | — | Tarp antrojo ir trečiojo kvintilių | — |
| `hhincome` | `4` | — | — | Tarp trečiojo ir ketvirtojo kvintilių | — |
| `hhincome` | `5` | — | — | Tarp ketvirtojo ir penktojo kvintilių | — |
| `hs1` | `1` | — | — | Labai gera | — |
| `hs1` | `2` | — | — | Gera | — |
| `hs1` | `3` | — | — | Vidutiniška | — |
| `hs1` | `4` | — | — | Bloga | — |
| `hs1` | `5` | — | — | Labai bloga | — |
| `hs1` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `hs2` | `1` | — | — | Taip | — |
| `hs2` | `2` | — | — | Ne | — |
| `hs3` | `1` | — | — | Labai apribota | — |
| `hs3` | `2` | — | — | Šiek tiek apribota | — |
| `hs3` | `3` | — | — | Visiškai neapribota | — |
| `ac2` | `1` | — | — | Taip, buvau paguldytas (-a) į ligoninę ar kitą sveikatos priežiūros įstaigą | — |
| `ac2` | `2` | — | — | Taip, buvo suteikta gydytojo ar slaugytojo ambulatorinė pagalba | — |
| `ac2` | `3` | — | — | Sveikatos priežiūros specialisto pagalbos neprireikė | — |
| `ac2` | `-2` | — | — | Netaikoma | — |
| `aw1` | `1` | — | — | Taip | — |
| `aw1` | `2` | — | — | Ne | — |
| `aw1` | `-2` | — | — | Netaikoma | — |
| `pl1` | `1` | — | — | Taip | — |
| `pl1` | `2` | — | — | Ne | — |
| `pl1` | `3` | — | — | Aš aklas (-a), visai nematau | — |
| `pl2` | `1` | — | — | Ne, matau gerai | — |
| `pl2` | `2` | — | — | Šiek tiek prastai | — |
| `pl2` | `3` | — | — | Labai prastai | — |
| `pl2` | `-2` | — | — | Netaikoma | — |
| `pl3` | `1` | — | — | Taip | — |
| `pl3` | `2` | — | — | Ne | — |
| `pl3` | `3` | — | — | Esu visiškai kurčias (-ia) | — |
| `pl4` | `1` | — | — | Ne, girdžiu gerai | — |
| `pl4` | `2` | — | — | Šiek tiek prastai | — |
| `pl4` | `3` | — | — | Labai prastai | — |
| `pl4` | `4` | — | — | Negirdžiu / negaliu girdėti | — |
| `pl4` | `-2` | — | — | Netaikoma | — |
| `pl5` | `1` | — | — | Ne, girdžiu gerai | — |
| `pl5` | `2` | — | — | Šiek tiek prastai | — |
| `pl5` | `3` | — | — | Labai prastai | — |
| `pl5` | `4` | — | — | Negirdžiu / negaliu girdėti | — |
| `pl5` | `-2` | — | — | Netaikoma | — |
| `pl6` | `1` | — | — | Nesunku | — |
| `pl6` | `2` | — | — | Šiek tiek sunku | — |
| `pl6` | `3` | — | — | Labai sunku | — |
| `pl6` | `4` | — | — | Negaliu / neįstengiu to padaryti | — |
| `pl7` | `1` | — | — | Nesunku | — |
| `pl7` | `2` | — | — | Šiek tiek sunku | — |
| `pl7` | `3` | — | — | Labai sunku | — |
| `pl7` | `4` | — | — | Negaliu / neįstengiu to padaryti | — |
| `pc1a` | `1` | — | — | Nesunku | — |
| `pc1a` | `2` | — | — | Šiek tiek sunku | — |
| `pc1a` | `3` | — | — | Labai sunku | — |
| `pc1a` | `4` | — | — | Negaliu / neįstengiu to atlikti | — |
| `pc1a` | `-2` | — | — | Netaikoma | — |
| `pc1b` | `1` | — | — | Nesunku | — |
| `pc1b` | `2` | — | — | Šiek tiek sunku | — |
| `pc1b` | `3` | — | — | Labai sunku | — |
| `pc1b` | `4` | — | — | Negaliu / neįstengiu to atlikti | — |
| `pc1b` | `-2` | — | — | Netaikoma | — |
| `pc1c` | `1` | — | — | Nesunku | — |
| `pc1c` | `2` | — | — | Šiek tiek sunku | — |
| `pc1c` | `3` | — | — | Labai sunku | — |
| `pc1c` | `4` | — | — | Negaliu / neįstengiu to atlikti | — |
| `pc1c` | `-2` | — | — | Netaikoma | — |
| `pc1d` | `1` | — | — | Nesunku | — |
| `pc1d` | `2` | — | — | Šiek tiek sunku | — |
| `pc1d` | `3` | — | — | Labai sunku | — |
| `pc1d` | `4` | — | — | Negaliu / neįstengiu to atlikti | — |
| `pc1d` | `-2` | — | — | Netaikoma | — |
| `pc1e` | `1` | — | — | Nesunku | — |
| `pc1e` | `2` | — | — | Šiek tiek sunku | — |
| `pc1e` | `3` | — | — | Labai sunku | — |
| `pc1e` | `4` | — | — | Negaliu / neįstengiu to atlikti | — |
| `pc1e` | `-2` | — | — | Netaikoma | — |
| `pc2` | `1` | — | — | Taip, bent vieną iš šių veiksmų | — |
| `pc2` | `2` | — | — | Ne | — |
| `pc2` | `-2` | — | — | Netaikoma | — |
| `pc3` | `1` | — | — | Taip, bent vienam iš šių veiksmų | — |
| `pc3` | `2` | — | — | Ne | — |
| `pc3` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `pc3` | `-2` | — | — | Netaikoma | — |
| `ha1a` | `1` | — | — | Nesunku | — |
| `ha1a` | `2` | — | — | Šiek tiek sunku | — |
| `ha1a` | `3` | — | — | Labai sunku | — |
| `ha1a` | `4` | — | — | Negaliu / neįstengiu to atlikti | — |
| `ha1a` | `5` | — | — | Netaikytina (niekada nebandė ar nėra būtinybės) | — |
| `ha1a` | `-2` | — | — | Netaikoma | — |
| `ha1b` | `1` | — | — | Nesunku | — |
| `ha1b` | `2` | — | — | Šiek tiek sunku | — |
| `ha1b` | `3` | — | — | Labai sunku | — |
| `ha1b` | `4` | — | — | Negaliu / neįstengiu to atlikti | — |
| `ha1b` | `5` | — | — | Netaikytina (niekada nebandė ar nėra būtinybės) | — |
| `ha1b` | `-2` | — | — | Netaikoma | — |
| `ha1c` | `1` | — | — | Nesunku | — |
| `ha1c` | `2` | — | — | Šiek tiek sunku | — |
| `ha1c` | `3` | — | — | Labai sunku | — |
| `ha1c` | `4` | — | — | Negaliu / neįstengiu to atlikti | — |
| `ha1c` | `5` | — | — | Netaikytina (niekada nebandė ar nėra būtinybės) | — |
| `ha1c` | `-2` | — | — | Netaikoma | — |
| `ha1d` | `1` | — | — | Nesunku | — |
| `ha1d` | `2` | — | — | Šiek tiek sunku | — |
| `ha1d` | `3` | — | — | Labai sunku | — |
| `ha1d` | `4` | — | — | Negaliu / neįstengiu to atlikti | — |
| `ha1d` | `5` | — | — | Netaikytina (niekada nebandė ar nėra būtinybės) | — |
| `ha1d` | `-2` | — | — | Netaikoma | — |
| `ha1e` | `1` | — | — | Nesunku | — |
| `ha1e` | `2` | — | — | Šiek tiek sunku | — |
| `ha1e` | `3` | — | — | Labai sunku | — |
| `ha1e` | `4` | — | — | Negaliu / neįstengiu to atlikti | — |
| `ha1e` | `5` | — | — | Netaikytina (niekada nebandė ar nėra būtinybės) | — |
| `ha1e` | `-2` | — | — | Netaikoma | — |
| `ha1f` | `1` | — | — | Nesunku | — |
| `ha1f` | `2` | — | — | Šiek tiek sunku | — |
| `ha1f` | `3` | — | — | Labai sunku | — |
| `ha1f` | `4` | — | — | Negaliu / neįstengiu to atlikti | — |
| `ha1f` | `5` | — | — | Netaikytina (niekada nebandė ar nėra būtinybės) | — |
| `ha1f` | `-2` | — | — | Netaikoma | — |
| `ha1g` | `1` | — | — | Nesunku | — |
| `ha1g` | `2` | — | — | Šiek tiek sunku | — |
| `ha1g` | `3` | — | — | Labai sunku | — |
| `ha1g` | `4` | — | — | Negaliu / neįstengiu to atlikti | — |
| `ha1g` | `5` | — | — | Netaikytina (niekada nebandė ar nėra būtinybės) | — |
| `ha1g` | `-2` | — | — | Netaikoma | — |
| `ha2` | `1` | — | — | Taip, bent vienam iš šių darbų | — |
| `ha2` | `2` | — | — | Ne | — |
| `ha2` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `ha2` | `-2` | — | — | Netaikoma | — |
| `ha3` | `1` | — | — | Taip, bent vienam iš šių darbų | — |
| `ha3` | `2` | — | — | Ne | — |
| `ha3` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `ha3` | `-2` | — | — | Netaikoma | — |
| `pn1` | `1` | — | — | Nejaučiau | — |
| `pn1` | `2` | — | — | Labai silpną | — |
| `pn1` | `3` | — | — | Silpną | — |
| `pn1` | `4` | — | — | Vidutinį | — |
| `pn1` | `5` | — | — | Stiprų | — |
| `pn1` | `6` | — | — | Labai stiprų | — |
| `pn1` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `pn2` | `1` | — | — | Tokių atvejų nebuvo | — |
| `pn2` | `2` | — | — | Šiek tiek trukdė | — |
| `pn2` | `3` | — | — | Vidutiniškai trukdė | — |
| `pn2` | `4` | — | — | Ganėtinai trukdė | — |
| `pn2` | `5` | — | — | Labai trukdė | — |
| `pn2` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `mh1a` | `1` | — | — | Tokių atvejų nebuvo | — |
| `mh1a` | `2` | — | — | Keletą dienų | — |
| `mh1a` | `3` | — | — | Daugiau kaip savaitę | — |
| `mh1a` | `4` | — | — | Beveik kasdien | — |
| `mh1a` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `mh1b` | `1` | — | — | Tokių atvejų nebuvo | — |
| `mh1b` | `2` | — | — | Keletą dienų | — |
| `mh1b` | `3` | — | — | Daugiau kaip savaitę | — |
| `mh1b` | `4` | — | — | Beveik kasdien | — |
| `mh1b` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `mh1c` | `1` | — | — | Tokių atvejų nebuvo | — |
| `mh1c` | `2` | — | — | Keletą dienų | — |
| `mh1c` | `3` | — | — | Daugiau kaip savaitę | — |
| `mh1c` | `4` | — | — | Beveik kasdien | — |
| `mh1c` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `mh1d` | `1` | — | — | Tokių atvejų nebuvo | — |
| `mh1d` | `2` | — | — | Keletą dienų | — |
| `mh1d` | `3` | — | — | Daugiau kaip savaitę | — |
| `mh1d` | `4` | — | — | Beveik kasdien | — |
| `mh1d` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `mh1e` | `1` | — | — | Tokių atvejų nebuvo | — |
| `mh1e` | `2` | — | — | Keletą dienų | — |
| `mh1e` | `3` | — | — | Daugiau kaip savaitę | — |
| `mh1e` | `4` | — | — | Beveik kasdien | — |
| `mh1e` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `mh1f` | `1` | — | — | Tokių atvejų nebuvo | — |
| `mh1f` | `2` | — | — | Keletą dienų | — |
| `mh1f` | `3` | — | — | Daugiau kaip savaitę | — |
| `mh1f` | `4` | — | — | Beveik kasdien | — |
| `mh1f` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `mh1g` | `1` | — | — | Tokių atvejų nebuvo | — |
| `mh1g` | `2` | — | — | Keletą dienų | — |
| `mh1g` | `3` | — | — | Daugiau kaip savaitę | — |
| `mh1g` | `4` | — | — | Beveik kasdien | — |
| `mh1g` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `mh1h` | `1` | — | — | Tokių atvejų nebuvo | — |
| `mh1h` | `2` | — | — | Keletą dienų | — |
| `mh1h` | `3` | — | — | Daugiau kaip savaitę | — |
| `mh1h` | `4` | — | — | Beveik kasdien | — |
| `mh1h` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `am1` | `1` | — | — | Mažiau nei prieš 6 mėn. | — |
| `am1` | `2` | — | — | Nuo 6 mėn. iki 12 mėn. | — |
| `am1` | `3` | — | — | Prieš 12 mėn. ar daugiau | — |
| `am1` | `4` | — | — | Niekada | — |
| `am2` | `1` | — | — | Mažiau nei prieš 12 mėn. | — |
| `am2` | `2` | — | — | Prieš 12 mėn. ar daugiau | — |
| `am2` | `3` | — | — | Niekada | — |
| `am4` | `1` | — | — | Mažiau nei prieš 12 mėn. | — |
| `am4` | `2` | — | — | Prieš 12 mėn. ar daugiau | — |
| `am4` | `3` | — | — | Niekada | — |
| `md1` | `1` | — | — | Taip | — |
| `md1` | `2` | — | — | Ne | — |
| `md1` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `md2` | `1` | — | — | Taip | — |
| `md2` | `2` | — | — | Ne | — |
| `md2` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `pa1` | `"0"` | — | — | Seniai (daugiau nei prieš metus) / Niekada | — |
| `pa1` | `"-1"` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `pa2` | `1` | — | — | Per pastaruosius 12 mėn. | — |
| `pa2` | `2` | — | — | Nuo 1 m. iki 5 m. | — |
| `pa2` | `3` | — | — | Nuo 5 m. iki 10 m. | — |
| `pa2` | `4` | — | — | Prieš 10 m. ir daugiau | — |
| `pa2` | `5` | — | — | Niekada | — |
| `pa2` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `pa3` | `1` | — | — | Per pastaruosius 12 mėn. | — |
| `pa3` | `2` | — | — | Nuo 1 m. iki 5 m. | — |
| `pa3` | `3` | — | — | Nuo 5 m. iki 10 m. | — |
| `pa3` | `4` | — | — | Prieš 10 m. ir daugiau | — |
| `pa3` | `5` | — | — | Niekada | — |
| `pa3` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `pa4` | `1` | — | — | Per pastaruosius 12 mėn. | — |
| `pa4` | `2` | — | — | Nuo 1 m. iki 5 m. | — |
| `pa4` | `3` | — | — | Nuo 5 m. iki 10 m. | — |
| `pa4` | `4` | — | — | Prieš 10 m. ir daugiau | — |
| `pa4` | `5` | — | — | Niekada | — |
| `pa4` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `pa5` | `1` | — | — | Per pastaruosius 12 mėn. | — |
| `pa5` | `2` | — | — | Nuo 1 m. iki 5 m. | — |
| `pa5` | `3` | — | — | Nuo 5 m. iki 10 m. | — |
| `pa5` | `4` | — | — | Prieš 10 m. ir daugiau | — |
| `pa5` | `5` | — | — | Niekada | — |
| `pa5` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `pa6` | `1` | — | — | Per pastaruosius 12 mėn. | — |
| `pa6` | `2` | — | — | Nuo 1 m. iki 5 m. | — |
| `pa6` | `3` | — | — | Nuo 5 m. iki 10 m. | — |
| `pa6` | `4` | — | — | Prieš 10 m. ir daugiau | — |
| `pa6` | `5` | — | — | Niekada | — |
| `pa6` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `pa7` | `1` | — | — | Per pastaruosius 12 mėn. | — |
| `pa7` | `2` | — | — | Nuo 1 m. iki 2 m. | — |
| `pa7` | `3` | — | — | Nuo 2 m. iki 3 m. | — |
| `pa7` | `4` | — | — | Prieš 3 m. ir daugiau | — |
| `pa7` | `5` | — | — | Niekada | — |
| `pa7` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `pa7` | `-2` | — | — | Netaikoma | — |
| `pa8` | `1` | — | — | Per pastaruosius 12 mėn. | — |
| `pa8` | `2` | — | — | Nuo 1 m. iki 2 m. | — |
| `pa8` | `3` | — | — | Nuo 2 m. iki 3 m. | — |
| `pa8` | `4` | — | — | Prieš 3 m. ir daugiau | — |
| `pa8` | `5` | — | — | Niekada | — |
| `pa8` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `pa8` | `-2` | — | — | Netaikoma | — |
| `un1a` | `1` | — | — | Taip | — |
| `un1a` | `2` | — | — | Ne | — |
| `un1a` | `3` | — | — | Nereikėjo sveikatos priežiūros paslaugų | — |
| `un1a` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `un1b` | `1` | — | — | Taip | — |
| `un1b` | `2` | — | — | Ne | — |
| `un1b` | `3` | — | — | Nereikėjo sveikatos priežiūros paslaugų | — |
| `un1b` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `un2a` | `1` | — | — | Taip | — |
| `un2a` | `2` | — | — | Ne | — |
| `un2a` | `3` | — | — | Nereikėjo teikiamų paslaugų | — |
| `un2a` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `un2b` | `1` | — | — | Taip | — |
| `un2b` | `2` | — | — | Ne | — |
| `un2b` | `3` | — | — | Nereikėjo teikiamų paslaugų | — |
| `un2b` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `un2c` | `1` | — | — | Taip | — |
| `un2c` | `2` | — | — | Ne | — |
| `un2c` | `3` | — | — | Nereikėjo teikiamų paslaugų | — |
| `un2c` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `un2d` | `1` | — | — | Taip | — |
| `un2d` | `2` | — | — | Ne | — |
| `un2d` | `3` | — | — | Nereikėjo teikiamų paslaugų | — |
| `un2d` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `pe1` | `1` | — | — | Daugiausia sėdite ar stovite | — |
| `pe1` | `2` | — | — | Daugiausia vaikštote ar atliekate vidutinių fizinių pastangų reikalaujantį darbą | — |
| `pe1` | `3` | — | — | Daugiausia dirbate sunkų fizinį darbą | — |
| `pe1` | `4` | — | — | Neatlieka jokių darbinių užduočių | — |
| `pe1` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `pe3` | `1` | — | — | 10 – 29 min. | — |
| `pe3` | `2` | — | — | 30 – 59 min. | — |
| `pe3` | `3` | — | — | Nuo 1 val. iki 2 val. | — |
| `pe3` | `4` | — | — | Nuo 2 val. iki 3 val. | — |
| `pe3` | `5` | — | — | 3 val. ar daugiau | — |
| `pe3` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `pe3` | `-2` | — | — | Netaikoma | — |
| `pe5` | `1` | — | — | 10 – 29 min. | — |
| `pe5` | `2` | — | — | 30 – 59 min. | — |
| `pe5` | `3` | — | — | Nuo 1 val. iki 2 val. | — |
| `pe5` | `4` | — | — | Nuo 2 val. iki 3 val. | — |
| `pe5` | `5` | — | — | 3 val. ar daugiau | — |
| `pe5` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `pe5` | `-2` | — | — | Netaikoma | — |
| `fv1` | `1` | — | — | Vieną ar daugiau kartų per dieną | — |
| `fv1` | `2` | — | — | 4 – 6 kartus per savaitę | — |
| `fv1` | `3` | — | — | 1 – 3 kartus per savaitę | — |
| `fv1` | `4` | — | — | Rečiau nei kartą per savaitę | — |
| `fv1` | `5` | — | — | Niekada | — |
| `fv1` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `fv3` | `1` | — | — | Vieną ar daugiau kartų per dieną | — |
| `fv3` | `2` | — | — | 4 – 6 kartus per savaitę | — |
| `fv3` | `3` | — | — | 1 – 3 kartus per savaitę | — |
| `fv3` | `4` | — | — | Rečiau nei kartą per savaitę | — |
| `fv3` | `5` | — | — | Niekada | — |
| `fv3` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `sk1` | `1` | — | — | Taip, kasdien | — |
| `sk1` | `2` | — | — | Taip, kartais | — |
| `sk1` | `3` | — | — | Nerūkau | — |
| `sk1` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `sk2` | `1` | — | — | Cigaretes (pramoninės gamybos arba rankų darbo) | — |
| `sk2` | `2` | — | — | Cigarus | — |
| `sk2` | `3` | — | — | Pypkinį tabaką | — |
| `sk2` | `4` | — | — | Kita (kaljanas ir pan.) | — |
| `sk2` | `-2` | — | — | Netaikoma | — |
| `sk4` | `1` | — | — | Niekada arba beveik niekada | — |
| `sk4` | `2` | — | — | Trumpiau nei 1 val. per dieną | — |
| `sk4` | `3` | — | — | 1 val. per dieną arba ilgiau | — |
| `sk4` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `al1` | `1` | — | — | Kasdien arba beveik kasdien | — |
| `al1` | `2` | — | — | 5 – 6 dienas per savaitę | — |
| `al1` | `3` | — | — | 3 – 4 dienas per savaitę | — |
| `al1` | `4` | — | — | 1 – 2 dienas per savaitę | — |
| `al1` | `5` | — | — | 2 – 3 dienas per mėnesį | — |
| `al1` | `6` | — | — | Kartą per mėnesį | — |
| `al1` | `7` | — | — | Rečiau nei kartą per mėnesį | — |
| `al1` | `8` | — | — | Nevartojau per pastaruosius 12 mėn., nes aš nebevartoju alkoholio | — |
| `al1` | `9` | — | — | Niekada arba ragavau tik keletą kartų gyvenime | — |
| `al1` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `al2` | `1` | — | — | Visas 4 dienas | — |
| `al2` | `2` | — | — | 3-is iš 4 dienų | — |
| `al2` | `3` | — | — | 2-i iš 4 dienų | — |
| `al2` | `4` | — | — | 1-ą iš 4 dienų | — |
| `al2` | `5` | — | — | Nei vieną iš 4 dienų | — |
| `al2` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `al2` | `-2` | — | — | Netaikoma | — |
| `al3` | `1` | — | — | 16 arba daugiau standartinių alkoholio vienetų (1 SAV laikoma 10 g gryno etilo alkoholio) per dieną | — |
| `al3` | `2` | — | — | 10 - 15 SAV per dieną | — |
| `al3` | `3` | — | — | 6 - 9 SAV per dieną | — |
| `al3` | `4` | — | — | 4 - 5 SAV per dieną | — |
| `al3` | `5` | — | — | 3 SAV per dieną | — |
| `al3` | `6` | — | — | 2 SAV per dieną | — |
| `al3` | `7` | — | — | 1 SAV per dieną | — |
| `al3` | `8` | — | — | 0 SAV per dieną | — |
| `al3` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `al3` | `-2` | — | — | Netaikoma | — |
| `al4` | `1` | — | — | Visas 3 dienas | — |
| `al4` | `2` | — | — | 2-i iš 3 dienų | — |
| `al4` | `3` | — | — | 1-ą iš 3 dienų | — |
| `al4` | `4` | — | — | Nei vieną iš trijų dienų | — |
| `al4` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `al4` | `-2` | — | — | Netaikoma | — |
| `al5` | `1` | — | — | 16 arba daugiau standartinių alkoholio vienetų (1 SAV laikoma 10 g gryno etilo alkoholio) per dieną | — |
| `al5` | `2` | — | — | 10 - 15 SAV per dieną | — |
| `al5` | `3` | — | — | 6 - 9 SAV per dieną | — |
| `al5` | `4` | — | — | 4 - 5 SAV per dieną | — |
| `al5` | `5` | — | — | 3 SAV per dieną | — |
| `al5` | `6` | — | — | 2 SAV per dieną | — |
| `al5` | `7` | — | — | 1 SAV per dieną | — |
| `al5` | `8` | — | — | 0 SAV per dieną | — |
| `al5` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `al5` | `-2` | — | — | Netaikoma | — |
| `al6` | `1` | — | — | Kasdien ar beveik kasdien | — |
| `al6` | `2` | — | — | 5 – 6 dienas per savaitę | — |
| `al6` | `3` | — | — | 3 – 4 dienas per savaitę | — |
| `al6` | `4` | — | — | 1 – 2 dienas per savaitę | — |
| `al6` | `5` | — | — | 2 – 3 dienas per mėnesį | — |
| `al6` | `6` | — | — | Kartą per mėnesį | — |
| `al6` | `7` | — | — | Rečiau nei kartą per mėnesį | — |
| `al6` | `8` | — | — | Nei karto per pastaruosius 12 mėn. | — |
| `al6` | `9` | — | — | Niekada gyvenime | — |
| `al6` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `al6` | `-2` | — | — | Netaikoma | — |
| `ss1` | `1` | — | — | Nei vieno | — |
| `ss1` | `2` | — | — | 1 ar 2 asmenis | — |
| `ss1` | `3` | — | — | 3 – 5 asmenis | — |
| `ss1` | `4` | — | — | 6 ir daugiau asmenų | — |
| `ss1` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `ss2` | `1` | — | — | Labai | — |
| `ss2` | `2` | — | — | Šiek tiek | — |
| `ss2` | `3` | — | — | Vidutiniškai | — |
| `ss2` | `4` | — | — | Mažai | — |
| `ss2` | `5` | — | — | Nesidomi | — |
| `ss2` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `ss3` | `1` | — | — | Labai lengva | — |
| `ss3` | `2` | — | — | Lengva | — |
| `ss3` | `3` | — | — | Vidutiniškai lengva | — |
| `ss3` | `4` | — | — | Sunku | — |
| `ss3` | `5` | — | — | Labai sunku | — |
| `ss3` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `ic1` | `1` | — | — | Taip | — |
| `ic1` | `2` | — | — | Ne | — |
| `ic1` | `-1` | — | — | Nėra (nežino, atsisako nurodyti) | — |
| `ic2` | `1` | — | — | Jūsų šeimos narys (-iai) | — |
| `ic2` | `2` | — | — | Ne Jūsų šeimos narys (-iai) | — |
| `ic2` | `-2` | — | — | Netaikoma | — |
| `ic3` | `1` | — | — | Mažiau nei 10 val. per savaitę | — |
| `ic3` | `2` | — | — | Nuo 10 val. iki 20 val. per savaitę | — |
| `ic3` | `3` | — | — | 20 ar daugiau val. per savaitę | — |
| `ic3` | `-2` | — | — | Netaikoma | — |

# Related References

- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata.csv#L8)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata (https://data.gov.lt/datasets/1622/)
