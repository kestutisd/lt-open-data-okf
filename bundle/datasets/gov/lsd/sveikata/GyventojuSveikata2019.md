---
type: Table
title: "GyventojuSveikata2019 — Gyventojų sveikatos statistinis tyrimas 2019 m."
description: "2019 metais atliktas gyventojų sveikatos statistinis tyrimas"
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/GyventojuSveikata2019"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata.csv#L634"
    last_modified: "2026-11-11T14:39:20Z"
---

# GyventojuSveikata2019 — Gyventojų sveikatos statistinis tyrimas 2019 m.

2019 metais atliktas gyventojų sveikatos statistinis tyrimas

- **Model:** `datasets/gov/lsd/sveikata/GyventojuSveikata2019`[^manifest]
- **Dataset:** [datasets/gov/lsd/sveikata](../sveikata.md) (`datasets/gov/lsd/sveikata`)
- **Manifest CSV:** [datasets/gov/lsd/sveikata.csv#L634](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata.csv#L634)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/GyventojuSveikata2019`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pid` | `integer` | — | — | `open` | — | Respondento identifikacinis numeris | — |
| `wgt` | `string` | — | — | `open` | — | Asmens populiacijos svoris | — |
| `proxy` | `integer` | — | — | `open` | — | Dalyvavimo tyrime pobūdis | — |
| `refdate` | `date` | — | — | `open` | — | Apklausos ataskaitinė data | — |
| `sex` | `integer` | `sex` | — | `open` | — | Lytis | — |
| `age` | `integer` | — | — | `open` | — | Amžius | — |
| `ap` | `integer` | — | — | `open` | — | Gimimo šalis | — |
| `deg_urb` | `integer` | — | — | `open` | — | Pilietybė | — |
| `m_k` | `integer` | — | — | `open` | — | Apskritys | — |
| `birthplace` | `integer` | — | — | `open` | — | Urbanizacijos lygis | — |
| `citizen` | `integer` | — | — | `open` | — | Miestas ar kaimas | — |
| `hatlevel` | `integer` | — | — | `open` | — | Juridinė santuokinė padėtis | — |
| `mainstat` | `integer` | — | — | `open` | — | Įgytas aukščiausias išsilavinimas (ISCED 2011) | — |
| `ft_pt` | `integer` | — | — | `open` | — | Ekonominio aktyvumo statusas | — |
| `jobstat` | `integer` | — | — | `open` | — | Dirba visą ar ne visą darbo dienos ar savaitės laiką | — |
| `jobisco` | `integer` | — | — | `open` | — | Užimtumo statusas | — |
| `locnace` | `string` | — | — | `open` | — | Profesija | — |
| `marstalegal` | `integer` | — | — | `open` | — | Pagrindinė darbovietės ekonominės veiklos rūšis | — |
| `hhnbpers` | `integer` | — | — | `open` | — | Namų ūkio narių skaičius (įskaitant respondentą) | — |
| `hhnbpers_0_13` | `integer` | — | — | `open` | — | 13 metų ir jaunesnių vaikų skaičius namų ūkyje | — |
| `hhtype` | `integer` | — | — | `open` | — | Namų ūkio tipas | — |
| `hhincome` | `integer` | — | — | `open` | — | Namų ūkio grynosios mėnesio ekvivalentinės pajamos | — |
| `hs1` | `integer` | — | — | `open` | — | Bendra sveikatos būklė | — |
| `hs2` | `integer` | `bool` | — | `open` | — | Sergate kokia nors lėtine (chroniška) liga arba turite ilgalaikių sveikatos sutrikimų? | — |
| `hs3` | `integer` | — | — | `open` | — | Veiklos apribojimas dėl sveikatos sutrikimų bent 6 mėn. per pastarąjį laiką | — |
| `cd1a` | `integer` | `bool` | — | `open` | — | Per pastaruosius 12 mėn. sirgote astma (įskaitant alerginę) | — |
| `cd1b` | `integer` | `bool` | — | `open` | — | Per pastaruosius 12 mėn. sirgote lėtiniu bronchitu, lėtine obstrukcine plaučių liga ar emfizema | — |
| `cd1c` | `integer` | `bool` | — | `open` | — | Per pastaruosius 12 mėn. patyrėte miokardo infarktą (širdies smūgį) arba jo lėtines pasekmes | — |
| `cd1d` | `integer` | `bool` | — | `open` | — | Per pastaruosius 12 mėn. sirgote koronarine širdies liga arba krūtinės angina | — |
| `cd1e` | `integer` | `bool` | — | `open` | — | Per pastaruosius 12 mėn. buvo padidėjęs kraujospūdis | — |
| `cd1f` | `integer` | `bool` | — | `open` | — | Per pastaruosius 12 mėn. patyrėte insultą (kraujo išsiliejimą į smegenis, smegenų trombozę) arba lėtines jo pasekmes | — |
| `cd1g` | `integer` | `bool` | — | `open` | — | Per pastaruosius 12 mėn. sirgote artroze (išskyrus artritą) | — |
| `cd1h` | `integer` | `bool` | — | `open` | — | Per pastaruosius 12 mėn. sirgote apatinės nugaros dalies liga ar turėjo kitą lėtinę nugaros ydą | — |
| `cd1i` | `integer` | `bool` | — | `open` | — | Per pastaruosius 12 mėn. sirgote kaklo srities liga ar turėjo kitą lėtinę kaklo ydą | — |
| `cd1j` | `integer` | `bool` | — | `open` | — | Per pastaruosius 12 mėn. sirgote cukriniu diabetu | — |
| `cd1k` | `integer` | `bool` | — | `open` | — | Per pastaruosius 12 mėn. sirgote alergija, tokia kaip alerginė sloga (šienligė), akių uždegimas, dermatitas, alergija maistui ar kita alergija (išskyrus alerginę astmą) | — |
| `cd1l` | `integer` | `bool` | — | `open` | — | Per pastaruosius 12 mėn. sirgote kepenų ciroze | — |
| `cd1m` | `integer` | `bool` | — | `open` | — | Per pastaruosius 12 mėn. sirgote šlapimo nelaikymu, turėjo šlapimo pūslės kontrolės problemų | — |
| `cd1n` | `integer` | `bool` | — | `open` | — | Per pastaruosius 12 mėn. sirgote inkstų ligomis | — |
| `cd1o` | `integer` | `bool` | — | `open` | — | Per pastaruosius 12 mėn. sirgote depresija | — |
| `cd1p` | `integer` | `bool` | — | `open` | — | Per pastaruosius 12 mėn. buvo padidėjęs cholesterolio, kraujo lipidų ar trigliceridų kiekis kraujyje | — |
| `cd2` | `integer` | — | — | `open` | — | Bendra dantų ir dantenų būklė | — |
| `ac1a` | `integer` | `bool` | — | `open` | — | Per pastaruosius 12 mėn. buvote patekęs (-usi) į kelių eismo įvykį | — |
| `ac1b` | `integer` | `bool` | — | `open` | — | Per pastaruosius 12 mėn. buvote patekęs (-usi) į nelaimingą atsitikimą namuose | — |
| `ac1c` | `integer` | `bool` | — | `open` | — | Per pastaruosius 12 mėn. buvote patekęs (-usi) į nelaimingą atsitikimą laisvalaikio metu | — |
| `ac2` | `integer` | — | — | `open` | — | Rimčiausio medicininio įsikišimo atvejis dėl sunkiausio nelaimingo atsitikimo per pastaruosius 12 mėn. | — |
| `aw1` | `integer` | — | — | `open` | — | Per pastaruosius 12 mėn. nedirbote dėl savo sveikatos problemų | — |
| `aw2` | `integer` | — | — | `open` | — | Kiek iš viso dienų nedirbote per pastaruosius 12 mėn. dėl savo sveikatos problemų? | — |
| `pl1` | `integer` | — | — | `open` | — | Nešiojate akinius ar kontaktinius lęšius | — |
| `pl2` | `integer` | — | — | `open` | — | Jei PL1 = 1: Ar prastai matote net nešiodamas (-a) akinius ar kontaktinius lęšius? / Jei PL1 = 2: Ar prastai matote (ar turite regėjimo sutrikimų)? | — |
| `pl3` | `integer` | — | — | `open` | — | Naudojatės klausos aparatu | — |
| `pl4` | `integer` | — | — | `open` | — | Jei PL3 = 1: Ar bendraudamas (-a) su kitu asmeniu, kai kambaryje tylu, prastai girdite, net jei naudojatės klausos aparatu? / Jei PL3 = 2: Ar bendraudamas (-a) su kitu asmeniu, kai kambaryje tylu, prastai girdite? | — |
| `pl5` | `integer` | — | — | `open` | — | Jei PL3 = 1: Ar bendraudamas (-a) su kitu asmeniu, kai kambaryje triukšminga, prastai girdite, net jei naudojatės klausos aparatu? / Jei PL3 = 2: Ar bendraudamas (-a) su kitu asmeniu, kai kambaryje triukšminga, prastai girdite? | — |
| `pl6` | `integer` | — | — | `open` | — | Ar sunku nueiti pusės kilometro atstumą lygiu paviršiumi be jokios pagalbos (pvz., lazdos, ramento, kito asmens pagalbos)? | — |
| `pl7` | `integer` | — | — | `open` | — | Ar sunku užlipti ar nulipti 12 laiptelių? | — |
| `pl8` | `integer` | — | — | `open` | — | Ar sunku įsiminti ar sutelkti dėmesį? | — |
| `pl9` | `integer` | — | — | `open` | — | Ar sunku atsikąsti ir kramtyti kietą maistą? | — |
| `pc1a` | `integer` | — | — | `open` | — | Ar sunku pavalgyti? | — |
| `pc1b` | `integer` | — | — | `open` | — | Ar sunku atsigulti į lovą ar atsikelti iš jos, atsisėsti ant kėdės ar pasikelti nuo jos? | — |
| `pc1c` | `integer` | — | — | `open` | — | Ar sunku apsirengti ir nusirengti? | — |
| `pc1d` | `integer` | — | — | `open` | — | Ar sunku naudotis tualetu? | — |
| `pc1e` | `integer` | — | — | `open` | — | Ar sunku maudytis vonioje ar duše? | — |
| `pc2` | `integer` | — | — | `open` | — | Ar paprastai kas nors padeda atlikti šiuos veiksmus (PC1A - PC1E)? | — |
| `pc3` | `integer` | — | — | `open` | — | Jei PC2 = 1: Ar reikia daugiau pagalbos? / Jei PC2 = 2: Ar reikalinga pagalba? | — |
| `ha1a` | `integer` | — | — | `open` | — | Ar sunku ruošti valgį? | — |
| `ha1b` | `integer` | — | — | `open` | — | Ar sunku naudotis telefonu? | — |
| `ha1c` | `integer` | — | — | `open` | — | Ar sunku apsipirkti? | — |
| `ha1d` | `integer` | — | — | `open` | — | Ar sunku vartoti vaistus? | — |
| `ha1e` | `integer` | — | — | `open` | — | Ar sunku atlikti lengvus namų ruošos darbus? | — |
| `ha1f` | `integer` | — | — | `open` | — | Ar sunku retkarčiais atlikti sunkius namų ruošos darbus? | — |
| `ha1g` | `integer` | — | — | `open` | — | Ar sunku tvarkyti finansus ir kasdienius reikalus? | — |
| `ha2` | `integer` | — | — | `open` | — | Ar paprastai kas nors padeda atlikti šiuos darbus (HA1A - HA1G)? | — |
| `ha3` | `integer` | — | — | `open` | — | Jei HA2 = 1: Ar reikia daugiau pagalbos? / Jei HA2 = 2: Ar reikalinga pagalba? | — |
| `pn1` | `integer` | — | — | `open` | — | Kūno skausmo intensyvumas per pastarąsias 4 sav. | — |
| `pn2` | `integer` | — | — | `open` | — | Ar per pastarąsias 4 savaites skausmas trukdė vykdyti įprastą veiklą (tiek dirbti ne namie, tiek atlikti namų ruošos darbus)? | — |
| `mh1a` | `integer` | — | — | `open` | — | Per pastarąsias 2 sav. įprasta veikla mažai domino ar teikė mažai malonumo | — |
| `mh1b` | `integer` | — | — | `open` | — | Per pastarąsias 2 sav. jautėtės nusiminęs (-usi), prislėgtas (-a) ar nusivylęs (-usi) | — |
| `mh1c` | `integer` | — | — | `open` | — | Per pastarąsias 2 sav.buvo sunku užmigti, kankino nemiga arba miegojote per ilgai | — |
| `mh1d` | `integer` | — | — | `open` | — | Per pastarąsias 2 sav. jautėte nuovargį, energijos trūkumą | — |
| `mh1e` | `integer` | — | — | `open` | — | Per pastarąsias 2 sav. neturėjote apetito arba persivalgėte | — |
| `mh1f` | `integer` | — | — | `open` | — | Per pastarąsias 2 sav. jautėtės blogai, manėte, kad esate nevykėlis (-ė), nuvylėte savo šeimą arba nusivylėte savimi | — |
| `mh1g` | `integer` | — | — | `open` | — | Per pastarąsias 2 sav. buvo sunku susitelkti kokiai nors veiklai, pvz., skaityti laikraštį ar žiūrėti televizorių | — |
| `mh1h` | `integer` | — | — | `open` | — | Per pastarąsias 2 sav. judėjote ar kalbėjote taip lėtai, kad kiti žmonės atkreipė į tai dėmesį. Arba atvirkščiai – buvote toks (-ia) neramus (-i) ir nenustygstantis (-i), todėl judėjote žymiai daugiau nei įprastai | — |
| `ho12` | `integer` | — | — | `open` | — | Ligoninėje per pastaruosius 12 mėn. praleistų naktų skaičius | — |
| `ho34` | `integer` | — | — | `open` | — | Gulėjimo dienos stacionare per pastaruosius 12 mėn. atvejų skaičius | — |
| `am1` | `integer` | — | — | `open` | — | Kada paskutinį kartą lankėtės pas odontologą ar ortodontą? | — |
| `am2` | `integer` | — | — | `open` | — | Kada paskutinį kartą kreipėtės į bendrosios praktikos ar šeimos gydytoją dėl savo sveikatos? | — |
| `am3` | `integer` | — | — | `open` | — | Kiek kartų per pastarąsias 4 savaites kreipėtės į bendrosios praktikos ar šeimos gydytoją dėl savo sveikatos? | — |
| `am4` | `integer` | — | — | `open` | — | Kada paskutinį kartą kreipėtės į gydytoją specialistą ar chirurgą dėl savo sveikatos? | — |
| `am5` | `integer` | — | — | `open` | — | Kiek kartų per pastarąsias 4 savaites kreipėtės į gydytoją specialistą ar chirurgą dėl savo sveikatos? | — |
| `am6a` | `integer` | `bool` | — | `open` | — | Fizioterapeuto ar kineziterapeuto konsultacija per pastaruosius 12 mėn. | — |
| `am6b` | `integer` | `bool` | — | `open` | — | Psichologo, psichoterapeuto ar psichiatro konsultacija per pastaruosius 12 mėn. | — |
| `am7` | `integer` | `bool` | — | `open` | — | Priežiūros namuose paslaugų naudojimas asmeninėms reikmėms per pastaruosius 12 mėn. | — |
| `md1` | `integer` | — | — | `open` | — | Bet kokių gydytojo išrašytų vaistų vartojimas per pastarąsias dvi savaites (išskyrus kontraceptinius vaistus) | — |
| `md2` | `integer` | — | — | `open` | — | Bet kokių gydytojo neišrašytų vaistų, vaistažolių preparatų ar vitaminų vartojimas per pastarąsias dvi savaites (išskyrus kontraceptinius vaistus) | — |
| `pa1` | `integer` | — | — | `open` | — | Kada paskutinį kartą skiepijotės nuo gripo? | — |
| `pa2` | `integer` | — | — | `open` | — | Kada paskutinį kartą medicinos specialistas matavo kraujospūdį? | — |
| `pa3` | `integer` | — | — | `open` | — | Kada paskutinį kartą medicinos specialistas matavo cholesterolio kiekį kraujyje? | — |
| `pa4` | `integer` | — | — | `open` | — | Kada paskutinį kartą medicinos specialistas matavo cukraus kiekį kraujyje? | — |
| `pa5` | `integer` | — | — | `open` | — | Kada paskutinį kartą buvo atliktas slapto kraujavimo (kraujo likučių išmatose) tyrimas? | — |
| `pa6` | `integer` | — | — | `open` | — | Kada paskutinį kartą atlikta kolonoskopija? | — |
| `pa7` | `integer` | — | — | `open` | — | Kada paskutinį kartą atlikta mamografija (krūtų rentgenograma)? (Atsakė tik moterys). | — |
| `pa8` | `integer` | — | — | `open` | — | Kada paskutinį kartą imtas gimdos kaklelio tepinėlis? (Atsakė tik moterys). | — |
| `un1a` | `integer` | — | — | `open` | — | Nepatenkintas sveikatos priežiūros poreikis per pastaruosius 12 mėn. dėl ilgų eilių | — |
| `un1b` | `integer` | — | — | `open` | — | Nepatenkintas sveikatos priežiūros poreikis per pastaruosius 12 mėn. dėl atstumo ar transporto problemų | — |
| `un2a` | `integer` | — | — | `open` | — | Per pastaruosius 12 mėn. dėl finansinių priežasčių atsisakėte gydytojo paslaugų (išskyrus odontologo) | — |
| `un2b` | `integer` | — | — | `open` | — | Per pastaruosius 12 mėn. dėl finansinių priežasčių atsisakėte odontologo paslaugų | — |
| `un2c` | `integer` | — | — | `open` | — | Per pastaruosius 12 mėn. dėl finansinių priežasčių atsisakėte gydytojo išrašytų vaistų | — |
| `un2d` | `integer` | — | — | `open` | — | Per pastaruosius 12 mėn. dėl finansinių priežasčių atsisakėte psichikos sveikatos paslaugų (pvz., teikiamų psichologo, psichoterapeuto ar psichiatro) | — |
| `bm1` | `integer` | — | — | `open` | — | Ūgis (be batų) | — |
| `bm2` | `integer` | — | — | `open` | — | Svoris (be drabužių ir batų) | — |
| `pe1` | `integer` | — | — | `open` | — | Fizinė veikla dirbant (tiek apmokamą, tiek neapmokamą darbą) | — |
| `pe2` | `integer` | — | — | `open` | — | Kiek dienų per įprastą savaitę einate pėsčiomis užtrukdamas (-a) mažiausiai 10 min. be pertraukos? | — |
| `pe3` | `integer` | — | — | `open` | — | Kiek laiko per dieną paprastai užtrunkate eidamas (-a) pėsčiomis? | — |
| `pe4` | `integer` | — | — | `open` | — | Kiek dienų per įprastą savaitę važiuojate dviračiu užtrukdamas (-a) mažiausiai 10 min. be pertraukos? | — |
| `pe5` | `integer` | — | — | `open` | — | Kiek laiko per dieną paprastai užtrunkate važiuodamas (-a) dviračiu? | — |
| `pe6` | `integer` | — | — | `open` | — | Kiek dienų per įprastą savaitę sportuojate, užsiimate kūno rengyba ar aktyvia laisvalaikio veikla mažiausiai 10 min. be pertraukos? | — |
| `pe7` | `string` | — | — | `open` | — | Kiek laiko per įprastą savaitę sportuojate, užsiimate kūno rengyba ar aktyvia laisvalaikio veikla? | — |
| `pe8` | `integer` | — | — | `open` | — | Kiek dienų per įprastą savaitę atliekate konkrečius veiksmus, skirtus sustiprinti raumenis, pvz., darote ištvermės ar jėgos pratimus? | — |
| `pe9` | `string` | — | — | `open` | — | Kiek paprastai laiko per dieną sėdite? | — |
| `dh1` | `integer` | — | — | `open` | — | Kaip dažnai valgote vaisius, įskaitant šaldytus, džiovintus, konservuotus? (Išskyrus vaisių sultis (natūralias ar iš koncentrato) | — |
| `dh2` | `integer` | — | — | `open` | — | Vaisių porcijų skaičius per dieną (išskyrus vaisių sultis) | — |
| `dh3` | `integer` | — | — | `open` | — | Kaip dažnai valgote daržoves ar salotas (įskaitant šaldytas, džiovintas, konservuotas)? (Išskyrus bulves, daržovių sultis (natūralias ar iš koncentrato), daržovių sriubas) | — |
| `dh4` | `integer` | — | — | `open` | — | Daržovių ar salotų porcijų skaičius per dieną | — |
| `dh5` | `integer` | — | — | `open` | — | Kaip dažnai geriate natūralias (100 %) vaisių ar daržovių sultis? (Išskyrus iš koncentrato pagamintas ar saldintas sultis) | — |
| `dh6` | `integer` | — | — | `open` | — | Kaip dažnai geriate gaiviuosius gėrimus, pvz., limonadą ar kolą? (Išskyrus dietinius ar dirbtiniais saldikliais saldintus gėrimus) | — |
| `sk1` | `integer` | — | — | `open` | — | Tabako rūkymas (esama padėtis) | — |
| `sk2` | `integer` | — | — | `open` | — | Vidutinis cigarečių skaičius per dieną | — |
| `sk3` | `integer` | — | — | `open` | — | Ankstesnis kasdienis tabako rūkymas | — |
| `sk4` | `integer` | — | — | `open` | — | Kiek metų rūkėte tabaką kasdien? | — |
| `sk5` | `integer` | — | — | `open` | — | Kaip dažnai tenka būti prirūkytose patalpose? | — |
| `sk6` | `integer` | — | — | `open` | — | Elektroninių cigarečių arba panašių elektroninių prietaisų naudojimas | — |
| `al1` | `integer` | — | — | `open` | — | Bet kokių alkoholinių gėrimų (alaus, vyno, sidro, stipriųjų gėrimų, kokteilių, likerių, namų gamybos alkoholinių gėrimų ir pan.) vartojimo dažnumas per pastaruosius 12 mėn. | — |
| `al2` | `integer` | — | — | `open` | — | Alkoholinių gėrimų vartojimo dažnumas pirmadieniais–ketvirtadieniais | — |
| `al3` | `integer` | — | — | `open` | — | Vidutinis standartinių alkoholio vienetų skaičius suvartojamas tą dieną, kai vartojamas alkoholis (pirmadieniais–ketvirtadieniais) | — |
| `al4` | `integer` | — | — | `open` | — | Alkoholinių gėrimų vartojimo dažnumas penktadieniais–sekmadieniais | — |
| `al5` | `integer` | — | — | `open` | — | Vidutinis standartinių alkoholio vienetų skaičius suvartojamas tą dieną, kai vartojamas alkoholis (penktadieniais–sekmadieniais) | — |
| `al6` | `integer` | — | — | `open` | — | Rizikingo alkoholio vartojimo, kai viena proga išgeriama 1,5 litro ar daugiau alaus arba 6 taures (600 ml) ar daugiau vyno arba 5 taureles (200 ml) ar daugiau degtinės, arba kitų stipriųjų alkoholinių gėrimų, dažnumas per pastaruosius 12 mėn. | — |
| `ss1` | `integer` | — | — | `open` | — | Artimų žmonių, kuriais galima pasikliauti kilus rimtai asmeninei problemai, skaičius | — |
| `ss2` | `integer` | — | — | `open` | — | Kiek artimieji (šeimos nariai, draugai ir kt.) domisi tuo, ką veikiate? | — |
| `ss3` | `integer` | — | — | `open` | — | Ar paprasta prireikus gauti praktinės kaimynų pagalbos? | — |
| `ic1` | `integer` | — | — | `open` | — | Priežiūros ar pagalbos teikimas bent kartą per savaitę vienam ar keliems asmenims, turintiems su senatve, lėtiniais sveikatos sutrikimais ar negalia susijusių problemų (išskyrus profesionalią veiklą) | — |
| `ic2` | `integer` | — | — | `open` | — | Ar šis asmuo (asmenys) yra: | — |
| `ic3` | `integer` | — | — | `open` | — | Kiek valandų per savaitę prižiūrite ar padedate šiam asmeniui (šiems asmenims)? | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `proxy` | `1` | — | — | Pats respondentas | — |
| `proxy` | `2` | — | — | Už respondentą atsakė kitas to paties namų ūkio narys | — |
| `proxy` | `3` | — | — | Už respondentą atsakė kitas jį prižiūrintis, namų ūkiui nepriklausantis, asmuo | — |
| `sex` | `1` | — | — | Vyras | — |
| `sex` | `2` | — | — | Moteris | — |
| `sex` | `1` | — | — | Taip | — |
| `sex` | `2` | — | — | Ne | — |
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
| `deg_urb` | `3` | — | — | Retai apgyvendinta vietovė | — |
| `m_k` | `1` | — | — | Miestas | — |
| `m_k` | `2` | — | — | Kaimas | — |
| `birthplace` | `10` | — | — | Lietuvos Respublika | — |
| `birthplace` | `20` | — | — | Kita šalis | — |
| `citizen` | `10` | — | — | Lietuvos Respublikos | — |
| `citizen` | `20` | — | — | Kitos šalies | — |
| `hatlevel` | `0` | — | — | Ikimokyklinis ugdymas (ISCED 0) | — |
| `hatlevel` | `1` | — | — | Pradinis išsilavinimas (ISCED 1) | — |
| `hatlevel` | `2` | — | — | Pagrindinis išsilavinimas (ISCED 2) | — |
| `hatlevel` | `3` | — | — | Vidurinis išsilavinimas (ISCED 3) | — |
| `hatlevel` | `4` | — | — | Profesinis mokymas turint vidurinį išsilavinimą (ISCED 4) | — |
| `hatlevel` | `6` | — | — | Bakalauro studijos (ISCED 6) | — |
| `hatlevel` | `7` | — | — | Magistrantūros studijos (ISCED 7) | — |
| `hatlevel` | `8` | — | — | Doktorantūra (ISCED 8) | — |
| `mainstat` | `10` | — | — | Užimtas asmuo | — |
| `mainstat` | `20` | — | — | Bedarbis (-ė) | — |
| `mainstat` | `30` | — | — | Nedirbantis (-i) senatvės pensininkas (-ė) | — |
| `mainstat` | `40` | — | — | Dėl negalios nedirbantis asmuo | — |
| `mainstat` | `50` | — | — | Mokinys (-ė), nedirbantis (-i) studentas (-ė) | — |
| `mainstat` | `60` | — | — | Namų šeimininkas (-ė) | — |
| `mainstat` | `70` | — | — | Atliekantis privalomąją karo ar alternatyviąją tarnybą | — |
| `mainstat` | `80` | — | — | Kitas neaktyvus asmuo | — |
| `ft_pt` | `1` | — | — | Visą | — |
| `ft_pt` | `2` | — | — | Ne visą | — |
| `ft_pt` | `-2` | — | — | Netaikoma | — |
| `jobstat` | `11` | — | — | Savarankiškai dirbantis asmuo, turintis samdomųjų darbuotojų | — |
| `jobstat` | `12` | — | — | Savarankiškai dirbantis asmuo, neturintis samdomųjų darbuotojų | — |
| `jobstat` | `20` | — | — | Samdomasis darbuotojas | — |
| `jobstat` | `30` | — | — | Padedantis ūkyje ar šeimos versle ir atlyginimo negaunantis šeimos narys | — |
| `jobstat` | `-2` | — | — | Netaikoma | — |
| `marstalegal` | `1` | — | — | Niekada nebuvote vedęs (ištekėjusi) | — |
| `marstalegal` | `2` | — | — | Vedęs (ištekėjusi) | — |
| `marstalegal` | `3` | — | — | Našlys (-ė) | — |
| `marstalegal` | `4` | — | — | Išsituokęs (-usi) | — |
| `hhtype` | `10` | — | — | Vieno asmens namų ūkis | — |
| `hhtype` | `21` | — | — | Viena motina ar vienas tėvas su vaiku (-ais) iki 25 metų amžiaus | — |
| `hhtype` | `22` | — | — | Viena motina ar vienas tėvas, su vaikais 25 metų amžiaus ir vyresniais | — |
| `hhtype` | `31` | — | — | Pora be vaikų | — |
| `hhtype` | `32` | — | — | Pora su bent vienu vaiku iki 25 metų amžiaus | — |
| `hhtype` | `33` | — | — | Pora, kurios visi vaikai 25 metų amžiaus ir vyresni | — |
| `hhtype` | `40` | — | — | Kita | — |
| `hhincome` | `1` | — | — | Pirmoji pajamų kvintilinė grupė | — |
| `hhincome` | `2` | — | — | Antroji pajamų kvintilinė grupė | — |
| `hhincome` | `3` | — | — | Trečioji pajamų kvintilinė grupė | — |
| `hhincome` | `4` | — | — | Ketvirtoji pajamų kvintilinė grupė | — |
| `hhincome` | `5` | — | — | Penktoji pajamų kvintilinė grupė | — |
| `hhincome` | `-1` | — | — | Nenurodyta | — |
| `hs1` | `1` | — | — | Labai gera | — |
| `hs1` | `2` | — | — | Gera | — |
| `hs1` | `3` | — | — | Vidutiniška | — |
| `hs1` | `4` | — | — | Bloga | — |
| `hs1` | `5` | — | — | Labai bloga | — |
| `hs1` | `-1` | — | — | Nenurodyta | — |
| `hs1` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `hs3` | `1` | — | — | Labai apribota | — |
| `hs3` | `2` | — | — | Šiek tiek apribota | — |
| `hs3` | `3` | — | — | Visiškai neapribota | — |
| `cd2` | `1` | — | — | Labai gera | — |
| `cd2` | `2` | — | — | Gera | — |
| `cd2` | `3` | — | — | Vidutiniška | — |
| `cd2` | `4` | — | — | Bloga | — |
| `cd2` | `5` | — | — | Labai bloga | — |
| `cd2` | `-1` | — | — | Nenurodyta | — |
| `cd2` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `ac2` | `1` | — | — | Buvote paguldytas (-a) į ligoninę ar kitą sveikatos priežiūros įstaigą | — |
| `ac2` | `2` | — | — | Buvo suteikta gydytojo ar slaugytojo ambulatorinė pagalba | — |
| `ac2` | `3` | — | — | Sveikatos priežiūros specialisto pagalbos neprireikė | — |
| `ac2` | `-2` | — | — | Netaikoma | — |
| `aw1` | `1` | — | — | Taip | — |
| `aw1` | `2` | — | — | Ne | — |
| `aw1` | `-2` | — | — | Netaikoma | — |
| `aw2` | `-2` | — | — | Netaikoma | — |
| `aw2` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `pl1` | `1` | — | — | Taip | — |
| `pl1` | `2` | — | — | Ne | — |
| `pl1` | `3` | — | — | Visai nematote | — |
| `pl2` | `1` | — | — | Matote gerai | — |
| `pl2` | `2` | — | — | Šiek tiek prastai | — |
| `pl2` | `3` | — | — | Labai prastai | — |
| `pl2` | `4` | — | — | Visai nematote | — |
| `pl2` | `-2` | — | — | Netaikoma | — |
| `pl3` | `1` | — | — | Taip | — |
| `pl3` | `2` | — | — | Ne | — |
| `pl3` | `3` | — | — | Visai negirdite | — |
| `pl4` | `1` | — | — | Girdite gerai | — |
| `pl4` | `2` | — | — | Šiek tiek prastai | — |
| `pl4` | `3` | — | — | Labai prastai | — |
| `pl4` | `4` | — | — | Visai negirdite | — |
| `pl4` | `-2` | — | — | Netaikoma | — |
| `pl5` | `1` | — | — | Girdite gerai | — |
| `pl5` | `2` | — | — | Šiek tiek prastai | — |
| `pl5` | `3` | — | — | Labai prastai | — |
| `pl5` | `4` | — | — | Visai negirdite | — |
| `pl5` | `-2` | — | — | Netaikoma | — |
| `pl6` | `1` | — | — | Nesunku | — |
| `pl6` | `2` | — | — | Šiek tiek sunku | — |
| `pl6` | `3` | — | — | Labai sunku | — |
| `pl6` | `4` | — | — | Visai negalite to padaryti | — |
| `pl7` | `1` | — | — | Nesunku | — |
| `pl7` | `2` | — | — | Šiek tiek sunku | — |
| `pl7` | `3` | — | — | Labai sunku | — |
| `pl7` | `4` | — | — | Visai negalite to padaryti | — |
| `pl8` | `1` | — | — | Nesunku | — |
| `pl8` | `2` | — | — | Šiek tiek sunku | — |
| `pl8` | `3` | — | — | Labai sunku | — |
| `pl8` | `4` | — | — | Visai negalite to padaryti | — |
| `pl9` | `1` | — | — | Nesunku | — |
| `pl9` | `2` | — | — | Šiek tiek sunku | — |
| `pl9` | `3` | — | — | Labai sunku | — |
| `pl9` | `4` | — | — | Visai negalite to padaryti | — |
| `pl9` | `-2` | — | — | Netaikoma (Klausimas skirtas 55 metų ir vyresniems asmenims) | — |
| `pc1a` | `1` | — | — | Nesunku | — |
| `pc1a` | `2` | — | — | Šiek tiek sunku | — |
| `pc1a` | `3` | — | — | Labai sunku | — |
| `pc1a` | `4` | — | — | Visai negalite atlikti šio veiksmo | — |
| `pc1a` | `-2` | — | — | Netaikoma | — |
| `pc1b` | `1` | — | — | Nesunku | — |
| `pc1b` | `2` | — | — | Šiek tiek sunku | — |
| `pc1b` | `3` | — | — | Labai sunku | — |
| `pc1b` | `4` | — | — | Visai negalite atlikti šio veiksmo | — |
| `pc1b` | `-2` | — | — | Netaikoma | — |
| `pc1c` | `1` | — | — | Nesunku | — |
| `pc1c` | `2` | — | — | Šiek tiek sunku | — |
| `pc1c` | `3` | — | — | Labai sunku | — |
| `pc1c` | `4` | — | — | Visai negalite atlikti šio veiksmo | — |
| `pc1c` | `-2` | — | — | Netaikoma | — |
| `pc1d` | `1` | — | — | Nesunku | — |
| `pc1d` | `2` | — | — | Šiek tiek sunku | — |
| `pc1d` | `3` | — | — | Labai sunku | — |
| `pc1d` | `4` | — | — | Visai negalite atlikti šio veiksmo | — |
| `pc1d` | `-2` | — | — | Netaikoma | — |
| `pc1e` | `1` | — | — | Nesunku | — |
| `pc1e` | `2` | — | — | Šiek tiek sunku | — |
| `pc1e` | `3` | — | — | Labai sunku | — |
| `pc1e` | `4` | — | — | Visai negalite atlikti šio veiksmo | — |
| `pc1e` | `-2` | — | — | Netaikoma | — |
| `pc2` | `1` | — | — | Taip, bent vieną iš šių veiksmų | — |
| `pc2` | `2` | — | — | Ne | — |
| `pc2` | `-2` | — | — | Netaikoma | — |
| `pc3` | `1` | — | — | Taip, bent vienam iš šių veiksmų | — |
| `pc3` | `2` | — | — | Ne | — |
| `pc3` | `-1` | — | — | Nenurodyta | — |
| `pc3` | `-2` | — | — | Netaikoma | — |
| `pc3` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `ha1a` | `1` | — | — | Nesunku | — |
| `ha1a` | `2` | — | — | Šiek tiek sunku | — |
| `ha1a` | `3` | — | — | Labai sunku | — |
| `ha1a` | `4` | — | — | Visai negalite to padaryti | — |
| `ha1a` | `5` | — | — | Netaikytina (niekada nebandėte ar nėra būtinybės) | — |
| `ha1a` | `-2` | — | — | Netaikoma | — |
| `ha1b` | `1` | — | — | Nesunku | — |
| `ha1b` | `2` | — | — | Šiek tiek sunku | — |
| `ha1b` | `3` | — | — | Labai sunku | — |
| `ha1b` | `4` | — | — | Visai negalite to padaryti | — |
| `ha1b` | `5` | — | — | Netaikytina (niekada nebandėte ar nėra būtinybės) | — |
| `ha1b` | `-2` | — | — | Netaikoma | — |
| `ha1c` | `1` | — | — | Nesunku | — |
| `ha1c` | `2` | — | — | Šiek tiek sunku | — |
| `ha1c` | `3` | — | — | Labai sunku | — |
| `ha1c` | `4` | — | — | Visai negalite to padaryti | — |
| `ha1c` | `5` | — | — | Netaikytina (niekada nebandėte ar nėra būtinybės) | — |
| `ha1c` | `-2` | — | — | Netaikoma | — |
| `ha1d` | `1` | — | — | Nesunku | — |
| `ha1d` | `2` | — | — | Šiek tiek sunku | — |
| `ha1d` | `3` | — | — | Labai sunku | — |
| `ha1d` | `4` | — | — | Visai negalite to padaryti | — |
| `ha1d` | `5` | — | — | Netaikytina (niekada nebandėte ar nėra būtinybės) | — |
| `ha1d` | `-2` | — | — | Netaikoma | — |
| `ha1e` | `1` | — | — | Nesunku | — |
| `ha1e` | `2` | — | — | Šiek tiek sunku | — |
| `ha1e` | `3` | — | — | Labai sunku | — |
| `ha1e` | `4` | — | — | Visai negalite to padaryti | — |
| `ha1e` | `5` | — | — | Netaikytina (niekada nebandėte ar nėra būtinybės) | — |
| `ha1e` | `-2` | — | — | Netaikoma | — |
| `ha1f` | `1` | — | — | Nesunku | — |
| `ha1f` | `2` | — | — | Šiek tiek sunku | — |
| `ha1f` | `3` | — | — | Labai sunku | — |
| `ha1f` | `4` | — | — | Visai negalite to padaryti | — |
| `ha1f` | `5` | — | — | Netaikytina (niekada nebandėte ar nėra būtinybės) | — |
| `ha1f` | `-2` | — | — | Netaikoma | — |
| `ha1g` | `1` | — | — | Nesunku | — |
| `ha1g` | `2` | — | — | Šiek tiek sunku | — |
| `ha1g` | `3` | — | — | Labai sunku | — |
| `ha1g` | `4` | — | — | Visai negalite to padaryti | — |
| `ha1g` | `5` | — | — | Netaikytina (niekada nebandėte ar nėra būtinybės) | — |
| `ha1g` | `-2` | — | — | Netaikoma | — |
| `ha2` | `1` | — | — | Taip, bent vieną iš šių darbų | — |
| `ha2` | `2` | — | — | Ne | — |
| `ha2` | `-2` | — | — | Netaikoma | — |
| `ha3` | `1` | — | — | Taip, bent vienam iš šių darbų | — |
| `ha3` | `2` | — | — | Ne | — |
| `ha3` | `-1` | — | — | Nenurodyta | — |
| `ha3` | `-2` | — | — | Netaikoma | — |
| `ha3` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `pn1` | `1` | — | — | Jokio | — |
| `pn1` | `2` | — | — | Labai silpnas | — |
| `pn1` | `3` | — | — | Silpnas | — |
| `pn1` | `4` | — | — | Vidutinis | — |
| `pn1` | `5` | — | — | Stiprus | — |
| `pn1` | `6` | — | — | Labai stiprus | — |
| `pn1` | `-1` | — | — | Nenurodyta | — |
| `pn1` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `pn2` | `1` | — | — | Tokių atvejų nebuvo | — |
| `pn2` | `2` | — | — | Šiek tiek trukdė | — |
| `pn2` | `3` | — | — | Vidutiniškai trukdė | — |
| `pn2` | `4` | — | — | Ganėtinai trukdė | — |
| `pn2` | `5` | — | — | Labai trukdė | — |
| `pn2` | `-1` | — | — | Nenurodyta | — |
| `pn2` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `mh1a` | `1` | — | — | Tokių atvejų nebuvo | — |
| `mh1a` | `2` | — | — | Keletą dienų | — |
| `mh1a` | `3` | — | — | Daugiau kaip savaitę | — |
| `mh1a` | `4` | — | — | Beveik kasdien | — |
| `mh1a` | `-1` | — | — | Nenurodyta | — |
| `mh1a` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `mh1b` | `1` | — | — | Tokių atvejų nebuvo | — |
| `mh1b` | `2` | — | — | Keletą dienų | — |
| `mh1b` | `3` | — | — | Daugiau kaip savaitę | — |
| `mh1b` | `4` | — | — | Beveik kasdien | — |
| `mh1b` | `-1` | — | — | Nenurodyta | — |
| `mh1b` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `mh1c` | `1` | — | — | Tokių atvejų nebuvo | — |
| `mh1c` | `2` | — | — | Keletą dienų | — |
| `mh1c` | `3` | — | — | Daugiau kaip savaitę | — |
| `mh1c` | `4` | — | — | Beveik kasdien | — |
| `mh1c` | `-1` | — | — | Nenurodyta | — |
| `mh1c` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `mh1d` | `1` | — | — | Tokių atvejų nebuvo | — |
| `mh1d` | `2` | — | — | Keletą dienų | — |
| `mh1d` | `3` | — | — | Daugiau kaip savaitę | — |
| `mh1d` | `4` | — | — | Beveik kasdien | — |
| `mh1d` | `-1` | — | — | Nenurodyta | — |
| `mh1d` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `mh1e` | `1` | — | — | Tokių atvejų nebuvo | — |
| `mh1e` | `2` | — | — | Keletą dienų | — |
| `mh1e` | `3` | — | — | Daugiau kaip savaitę | — |
| `mh1e` | `4` | — | — | Beveik kasdien | — |
| `mh1e` | `-1` | — | — | Nenurodyta | — |
| `mh1e` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `mh1f` | `1` | — | — | Tokių atvejų nebuvo | — |
| `mh1f` | `2` | — | — | Keletą dienų | — |
| `mh1f` | `3` | — | — | Daugiau kaip savaitę | — |
| `mh1f` | `4` | — | — | Beveik kasdien | — |
| `mh1f` | `-1` | — | — | Nenurodyta | — |
| `mh1f` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `mh1g` | `1` | — | — | Tokių atvejų nebuvo | — |
| `mh1g` | `2` | — | — | Keletą dienų | — |
| `mh1g` | `3` | — | — | Daugiau kaip savaitę | — |
| `mh1g` | `4` | — | — | Beveik kasdien | — |
| `mh1g` | `-1` | — | — | Nenurodyta | — |
| `mh1g` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `mh1h` | `1` | — | — | Tokių atvejų nebuvo | — |
| `mh1h` | `2` | — | — | Keletą dienų | — |
| `mh1h` | `3` | — | — | Daugiau kaip savaitę | — |
| `mh1h` | `4` | — | — | Beveik kasdien | — |
| `mh1h` | `-1` | — | — | Nenurodyta | — |
| `mh1h` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
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
| `md1` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `md2` | `1` | — | — | Taip | — |
| `md2` | `2` | — | — | Ne | — |
| `md2` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `pa1` | `1` | — | — | Seniai (daugiau nei prieš metus) | — |
| `pa1` | `2` | — | — | Niekada | — |
| `pa2` | `1` | — | — | Per pastaruosius 12 mėn. | — |
| `pa2` | `2` | — | — | Prieš 1–3 metus | — |
| `pa2` | `3` | — | — | Prieš 3–5 metus | — |
| `pa2` | `4` | — | — | Prieš 5 m. ir daugiau | — |
| `pa2` | `5` | — | — | Niekada | — |
| `pa2` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `pa3` | `1` | — | — | Per pastaruosius 12 mėn. | — |
| `pa3` | `2` | — | — | Prieš 1–3 metus | — |
| `pa3` | `3` | — | — | Prieš 3–5 metus | — |
| `pa3` | `4` | — | — | Prieš 5 m. ir daugiau | — |
| `pa3` | `5` | — | — | Niekada | — |
| `pa3` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `pa4` | `1` | — | — | Per pastaruosius 12 mėn. | — |
| `pa4` | `2` | — | — | Prieš 1–3 metus | — |
| `pa4` | `3` | — | — | Prieš 3–5 metus | — |
| `pa4` | `4` | — | — | Prieš 5 m. ir daugiau | — |
| `pa4` | `5` | — | — | Niekada | — |
| `pa4` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `pa5` | `1` | — | — | Per pastaruosius 12 mėn. | — |
| `pa5` | `2` | — | — | Prieš 1–2 metus | — |
| `pa5` | `3` | — | — | Prieš 2–3 metus | — |
| `pa5` | `4` | — | — | Prieš 3 m. ir daugiau | — |
| `pa5` | `5` | — | — | Niekada | — |
| `pa5` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `pa6` | `1` | — | — | Per pastaruosius 12 mėn. | — |
| `pa6` | `2` | — | — | Prieš 1–5 metus | — |
| `pa6` | `3` | — | — | Prieš 5–10 metų | — |
| `pa6` | `4` | — | — | Prieš 10 m. ir daugiau | — |
| `pa6` | `5` | — | — | Niekada | — |
| `pa6` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `pa7` | `1` | — | — | Per pastaruosius 12 mėn. | — |
| `pa7` | `2` | — | — | Prieš 1–2 metus | — |
| `pa7` | `3` | — | — | Priesš 2–3 metus | — |
| `pa7` | `4` | — | — | Prieš 3 m. ir daugiau | — |
| `pa7` | `5` | — | — | Niekada | — |
| `pa7` | `-2` | — | — | Netaikoma | — |
| `pa7` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `pa8` | `1` | — | — | Per pastaruosius 12 mėn. | — |
| `pa8` | `2` | — | — | Prieš 1–2 metus | — |
| `pa8` | `3` | — | — | Priesš 2–3 metus | — |
| `pa8` | `4` | — | — | Prieš 3 m. ir daugiau | — |
| `pa8` | `5` | — | — | Niekada | — |
| `pa8` | `-2` | — | — | Netaikoma | — |
| `pa8` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `un1a` | `1` | — | — | Taip | — |
| `un1a` | `2` | — | — | Ne | — |
| `un1a` | `3` | — | — | Nereikėjo sveikatos priežiūros paslaugų | — |
| `un1a` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `un1b` | `1` | — | — | Taip | — |
| `un1b` | `2` | — | — | Ne | — |
| `un1b` | `3` | — | — | Nereikėjo sveikatos priežiūros paslaugų | — |
| `un1b` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `un2a` | `1` | — | — | Taip | — |
| `un2a` | `2` | — | — | Ne | — |
| `un2a` | `3` | — | — | Nereikėjo teikiamų paslaugų | — |
| `un2a` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `un2b` | `1` | — | — | Taip | — |
| `un2b` | `2` | — | — | Ne | — |
| `un2b` | `3` | — | — | Nereikėjo teikiamų paslaugų | — |
| `un2b` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `un2c` | `1` | — | — | Taip | — |
| `un2c` | `2` | — | — | Ne | — |
| `un2c` | `3` | — | — | Nereikėjo teikiamų paslaugų | — |
| `un2c` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `un2d` | `1` | — | — | Taip | — |
| `un2d` | `2` | — | — | Ne | — |
| `un2d` | `3` | — | — | Nereikėjo teikiamų paslaugų | — |
| `un2d` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `pe1` | `1` | — | — | Daugiausia sėdima ar stovima | — |
| `pe1` | `2` | — | — | Daugiausia vaikštoma arba atliekamas vidutinių fizinių pastangų reikalaujantis darbas | — |
| `pe1` | `3` | — | — | Daugiausia dirbamas sunkus fizinis darbas | — |
| `pe1` | `4` | — | — | Neatliekama jokių darbinių užduočių | — |
| `pe1` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `pe3` | `1` | — | — | 10 – 29 min. | — |
| `pe3` | `2` | — | — | 30 – 59 min. | — |
| `pe3` | `3` | — | — | Nuo 1 val. iki 2 val. | — |
| `pe3` | `4` | — | — | Nuo 2 val. iki 3 val. | — |
| `pe3` | `5` | — | — | 3 val. ar daugiau | — |
| `pe3` | `-2` | — | — | Netaikoma | — |
| `pe3` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `pe5` | `1` | — | — | 10 – 29 min. | — |
| `pe5` | `2` | — | — | 30 – 59 min. | — |
| `pe5` | `3` | — | — | Nuo 1 val. iki 2 val. | — |
| `pe5` | `4` | — | — | Nuo 2 val. iki 3 val. | — |
| `pe5` | `5` | — | — | 3 val. ar daugiau | — |
| `pe5` | `-2` | — | — | Netaikoma | — |
| `pe5` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `dh1` | `1` | — | — | Vieną ar daugiau kartų per dieną | — |
| `dh1` | `2` | — | — | 4 – 6 kartus per savaitę | — |
| `dh1` | `3` | — | — | 1 – 3 kartus per savaitę | — |
| `dh1` | `4` | — | — | Rečiau nei kartą per savaitę | — |
| `dh1` | `5` | — | — | Niekada | — |
| `dh1` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `dh3` | `1` | — | — | Vieną ar daugiau kartų per dieną | — |
| `dh3` | `2` | — | — | 4 – 6 kartus per savaitę | — |
| `dh3` | `3` | — | — | 1 – 3 kartus per savaitę | — |
| `dh3` | `4` | — | — | Rečiau nei kartą per savaitę | — |
| `dh3` | `5` | — | — | Niekada | — |
| `dh3` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `dh5` | `1` | — | — | Vieną ar daugiau kartų per dieną | — |
| `dh5` | `2` | — | — | 4 – 6 kartus per savaitę | — |
| `dh5` | `3` | — | — | 1 – 3 kartus per savaitę | — |
| `dh5` | `4` | — | — | Rečiau nei kartą per savaitę | — |
| `dh5` | `5` | — | — | Niekada | — |
| `dh5` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `dh6` | `1` | — | — | Vieną ar daugiau kartų per dieną | — |
| `dh6` | `2` | — | — | 4 – 6 kartus per savaitę | — |
| `dh6` | `3` | — | — | 1 – 3 kartus per savaitę | — |
| `dh6` | `4` | — | — | Rečiau nei kartą per savaitę | — |
| `dh6` | `5` | — | — | Niekada | — |
| `dh6` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `sk1` | `1` | — | — | Rūko kasdien | — |
| `sk1` | `2` | — | — | Rūko kartais | — |
| `sk1` | `3` | — | — | Nerūko | — |
| `sk3` | `1` | — | — | Taip | — |
| `sk3` | `2` | — | — | Ne | — |
| `sk3` | `-2` | — | — | Netaikoma | — |
| `sk5` | `1` | — | — | Kasdien, 1 valandą per dieną ar ilgiau | — |
| `sk5` | `2` | — | — | Kasdien, trumpiau nei 1 val. per dieną | — |
| `sk5` | `3` | — | — | Mažiausiai kartą per savaitę (bet ne kasdien) | — |
| `sk5` | `4` | — | — | Rečiau nei kartą per savaitę | — |
| `sk5` | `5` | — | — | Niekada arba beveik niekada | — |
| `sk5` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `sk6` | `1` | — | — | Kasdien | — |
| `sk6` | `2` | — | — | Kartais | — |
| `sk6` | `3` | — | — | Anksčiau naudodavo | — |
| `sk6` | `4` | — | — | Niekada nėra naudojęs (-usi) | — |
| `sk6` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `al1` | `1` | — | — | Kasdien arba beveik kasdien | — |
| `al1` | `2` | — | — | 5 – 6 dienas per savaitę | — |
| `al1` | `3` | — | — | 3 – 4 dienas per savaitę | — |
| `al1` | `4` | — | — | 1 – 2 dienas per savaitę | — |
| `al1` | `5` | — | — | 2 – 3 dienas per mėnesį | — |
| `al1` | `6` | — | — | Kartą per mėnesį | — |
| `al1` | `7` | — | — | Rečiau nei kartą per mėnesį | — |
| `al1` | `8` | — | — | Nevartojote per pastaruosius 12 mėn., nes atsisakėte alkoholio | — |
| `al1` | `9` | — | — | Niekada arba ragavote tik keletą kartų gyvenime | — |
| `al1` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `al2` | `1` | — | — | Visas 4 dienas | — |
| `al2` | `2` | — | — | 3-is iš 4 dienų | — |
| `al2` | `3` | — | — | 2-i iš 4 dienų | — |
| `al2` | `4` | — | — | 1-ą iš 4 dienų | — |
| `al2` | `5` | — | — | Nei vieną iš 4 dienų | — |
| `al2` | `-2` | — | — | Netaikoma | — |
| `al2` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `al3` | `1` | — | — | 16 arba daugiau standartinių alkoholio vienetų (1 SAV laikoma 10 g gryno etilo alkoholio) per dieną | — |
| `al3` | `2` | — | — | 10 - 15 SAV per dieną | — |
| `al3` | `3` | — | — | 6 - 9 SAV per dieną | — |
| `al3` | `4` | — | — | 4 - 5 SAV per dieną | — |
| `al3` | `5` | — | — | 3 SAV per dieną | — |
| `al3` | `6` | — | — | 2 SAV per dieną | — |
| `al3` | `7` | — | — | 1 SAV per dieną | — |
| `al3` | `8` | — | — | 0 SAV per dieną | — |
| `al3` | `-2` | — | — | Netaikoma | — |
| `al3` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `al4` | `1` | — | — | Visas 3 dienas | — |
| `al4` | `2` | — | — | 2-i iš 3 dienų | — |
| `al4` | `3` | — | — | 1-ą iš 3 dienų | — |
| `al4` | `4` | — | — | Nei vieną iš trijų dienų | — |
| `al4` | `-2` | — | — | Netaikoma | — |
| `al4` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `al5` | `1` | — | — | 16 arba daugiau standartinių alkoholio vienetų (1 SAV laikoma 10 g gryno etilo alkoholio) per dieną | — |
| `al5` | `2` | — | — | 10 - 15 SAV per dieną | — |
| `al5` | `3` | — | — | 6 - 9 SAV per dieną | — |
| `al5` | `4` | — | — | 4 - 5 SAV per dieną | — |
| `al5` | `5` | — | — | 3 SAV per dieną | — |
| `al5` | `6` | — | — | 2 SAV per dieną | — |
| `al5` | `7` | — | — | 1 SAV per dieną | — |
| `al5` | `8` | — | — | 0 SAV per dieną | — |
| `al5` | `-2` | — | — | Netaikoma | — |
| `al5` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `al6` | `1` | — | — | Kasdien ar beveik kasdien | — |
| `al6` | `2` | — | — | 5 – 6 dienas per savaitę | — |
| `al6` | `3` | — | — | 3 – 4 dienas per savaitę | — |
| `al6` | `4` | — | — | 1 – 2 dienas per savaitę | — |
| `al6` | `5` | — | — | 2 – 3 dienas per mėnesį | — |
| `al6` | `6` | — | — | Kartą per mėnesį | — |
| `al6` | `7` | — | — | Rečiau nei kartą per mėnesį | — |
| `al6` | `8` | — | — | Nei karto per pastaruosius 12 mėn. | — |
| `al6` | `9` | — | — | Niekada | — |
| `al6` | `-2` | — | — | Netaikoma | — |
| `al6` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `ss1` | `1` | — | — | Nei vieno | — |
| `ss1` | `2` | — | — | 1 ar 2 asmenis | — |
| `ss1` | `3` | — | — | 3 – 5 asmenis | — |
| `ss1` | `4` | — | — | 6 ir daugiau asmenų | — |
| `ss1` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `ss2` | `1` | — | — | Labai | — |
| `ss2` | `2` | — | — | Šiek tiek | — |
| `ss2` | `3` | — | — | Vidutiniškai | — |
| `ss2` | `4` | — | — | Mažai | — |
| `ss2` | `5` | — | — | Nesidomi | — |
| `ss2` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `ss3` | `1` | — | — | Labai lengva | — |
| `ss3` | `2` | — | — | Lengva | — |
| `ss3` | `3` | — | — | Nei sunku, nei lengva | — |
| `ss3` | `4` | — | — | Sunku | — |
| `ss3` | `5` | — | — | Labai sunku | — |
| `ss3` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `ic1` | `1` | — | — | Taip | — |
| `ic1` | `2` | — | — | Ne | — |
| `ic1` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `ic2` | `1` | — | — | Šeimos narys (-iai) | — |
| `ic2` | `2` | — | — | Ne šeimos narys (-iai) | — |
| `ic2` | `-2` | — | — | Netaikoma | — |
| `ic2` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |
| `ic3` | `1` | — | — | Mažiau nei 10 val. per savaitę | — |
| `ic3` | `2` | — | — | Nuo 10 val. iki 20 val. per savaitę | — |
| `ic3` | `3` | — | — | 20 ar daugiau val. per savaitę | — |
| `ic3` | `-2` | — | — | Netaikoma | — |
| `ic3` | `-3` | — | — | Neįtraukiama į skaičiavimus (Proxy = 2 arba 3) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata.csv
