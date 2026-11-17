---
type: Table
title: "NamuUkis — Namų ūkių pajamų ir gyvenimo sąlygų statistinio tyrimo rezultatai"
description: "Spinta table datasets/gov/lsd/pajamu_ir_gyvenimo_salygos/NamuUkis (61 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/pajamu_ir_gyvenimo_salygos/NamuUkis"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/pajamu_ir_gyvenimo_salygos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/pajamu_ir_gyvenimo_salygos.csv#L258"
    last_modified: "2026-11-11T14:39:20Z"
---

# NamuUkis — Namų ūkių pajamų ir gyvenimo sąlygų statistinio tyrimo rezultatai

- **Model:** `datasets/gov/lsd/pajamu_ir_gyvenimo_salygos/NamuUkis`[^manifest]
- **Dataset:** [Lietuvos statistikos departamento namų ūkių bei pavienių asmenų pajamų ir gyvenimo sąlygų statistinio tyrimo duomenys](../pajamu_ir_gyvenimo_salygos.md) (`datasets/gov/lsd/pajamu_ir_gyvenimo_salygos`)
- **Manifest CSV:** [datasets/gov/lsd/pajamu_ir_gyvenimo_salygos.csv#L258](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/pajamu_ir_gyvenimo_salygos.csv#L258)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/pajamu_ir_gyvenimo_salygos/NamuUkis`
- **Primary Key (`ref`):** `hb030`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `hb030` | `string` | — | `4` | `open` | — | Namų ūkio ID | Statistinio tyrimo subjekto (namų ūkio) unikalus identifikatorius |
| `hh010` | `string` | — | `4` | `open` | — | Būsto tipas | — |
| `hh021` | `string` | — | `4` | `open` | — | Būsto valdos statusas | — |
| `hh030` | `integer` | — | `4` | `open` | — | Namų ūkio užimamų kambarių skaičius | — |
| `hh031` | `date` | `Y` | `4` | `open` | — | Įsikėlimo į būstą metai | — |
| `hh040` | `string` | — | `4` | `open` | — | Varvantis stogas, drėgnos sienos (grindys, pamatai), supuvę langai arba grindys | — |
| `hh050` | `string` | — | `4` | `open` | — | Gali sau leisti pakankamai šildyti būstą | — |
| `hh060` | `number` | — | `2` | `open` | — | Būsto nuomos mokestis per mėnesį | — |
| `hh061` | `number` | — | `2` | `open` | — | Pajamos, kurios būtų gautos per mėnesį, išnuomojus savo būstą be baldų, neįskaitant komunalinių paslaugų | — |
| `hh070` | `number` | — | `2` | `open` | — | Būsto išlaikymo išlaidos (šildymas, karštas ir šaltas vanduo, elektra ir pan.) per mėnesį | — |
| `hh071` | `number` | — | `2` | `open` | — | Būsto paskolos įmoka, neįskaitant palūkanų | — |
| `hh081` | `string` | — | `4` | `open` | — | Vonia/dušas būste | — |
| `hh091` | `string` | — | `4` | `open` | — | Tualetas su nutekamuoju vandeniu būste | — |
| `hs011` | `string` | — | `4` | `open` | — | Laiku nesumokėtos būsto paskolos įmokos arba nuomos mokestis | — |
| `hs021` | `string` | — | `4` | `open` | — | Laiku nesumokėti mokesčiai už komunalines paslaugas | — |
| `hs031` | `string` | — | `4` | `open` | — | Laiku nesumokėtos kitos paskolos, kreditai, palūkanos | — |
| `hs040` | `string` | — | `4` | `open` | — | Galimybė namų ūkiui sau leisti savaitę atostogauti ne namuose | — |
| `hs050` | `string` | — | `4` | `open` | — | Galimybė namų ūkiui sau leisti kas antrą dieną valgyti mėsos, žuvies ar lygiaverčio vegetariško maisto | — |
| `hs060` | `string` | — | `4` | `open` | — | Galimybė namų ūkiui apmokėti nenumatytas išlaidas (350 EUR) iš savo lėšų | — |
| `hs070` | `string` | — | `4` | `open` | — | Telefonas (įskaitant mobilųjį) | — |
| `hs080` | `string` | — | `4` | `open` | — | Spalvotas televizorius | — |
| `hs090` | `string` | — | `4` | `open` | — | Ar namų ūkis turi kompiuterį? | — |
| `hs100` | `string` | — | `4` | `open` | — | Skalbimo mašina | — |
| `hs110` | `string` | — | `4` | `open` | — | Ar namų ūkis turi automobilį? | — |
| `hs120` | `string` | — | `4` | `open` | — | Kaip namų ūkis verčiasi (suduria galą su galu)? | — |
| `hs130` | `string` | — | `4` | `open` | — | Mažiausia reikalinga pinigų suma per mėnesį, kad namų ūkis galėtų sudurti galą su galu (EUR) | — |
| `hs140` | `string` | — | `4` | `open` | — | Ar mokėjimas už būstą yra didelė finansinė našta? | — |
| `hs150` | `string` | — | `4` | `open` | — | Ar paskolos ar kredito grąžinimas yra didelė finansinė našta? | — |
| `hs160` | `string` | — | `4` | `open` | — | Tamsus būstas, t. y. nepakanka dienos šviesos | — |
| `hs170` | `string` | — | `4` | `open` | — | Triukšmas iš kaimynų butų, laiptinės arba lauko | — |
| `hs180` | `string` | — | `4` | `open` | — | Smogas, dulkės, nemalonūs kvapai, užterštas vanduo gyvenamajame rajone | — |
| `hs190` | `string` | — | `4` | `open` | — | Gyvena nusikaltimais, smurtu, vandalizmu garsėjančiame rajone | — |
| `hy010` | `number` | — | `2` | `open` | — | Bendrosios metinės namų ūkio pajamos | — |
| `hy020` | `number` | — | `2` | `open` | — | Disponuojamosios metinės namų ūkio pajamos | — |
| `hy022` | `number` | — | `2` | `open` | — | Disponuojamosios metinės namų ūkio pajamos iki socialinių išmokų, išskyrus senatvės ir našlaičių pensijas | — |
| `hy023` | `number` | — | `2` | `open` | — | Disponuojamosios metinės namų ūkio pajamos iki socialinių išmokų | — |
| `hy040g` | `number` | — | `2` | `open` | — | Metinės pajamos iš turto ir žemės nuomos | — |
| `hy040n` | `number` | — | `2` | `open` | — | Metinės pajamos iš turto ir žemės nuomos, atskaičius mokesčius | — |
| `hy050g` | `number` | — | `2` | `open` | — | Metinės socialinės išmokos šeimai ir vaikams (įskaitant motinystės ir tėvystės išmokas) | — |
| `hy050n` | `number` | — | `2` | `open` | — | Metinės socialinės išmokos šeimai ir vaikams (įskaitant motinystės ir tėvystės išmokas), atskaičius mokesčius | — |
| `hy060g` | `number` | — | `2` | `open` | — | Metinės socialinės atskirties ir kitos socialinės išmokos | — |
| `hy070g` | `number` | — | `2` | `open` | — | Metinės kompensacijos būstui išlaikyti | — |
| `hy080g` | `number` | — | `2` | `open` | — | Metinė piniginė parama iš kitų namų ūkių | — |
| `hy081g` | `number` | — | `2` | `open` | — | Metinė alimentų suma, gauta iš kitų namų ūkių | — |
| `hy090g` | `number` | — | `2` | `open` | — | Metinės pajamos iš palūkanų, dividendų | — |
| `hy090n` | `number` | — | `2` | `open` | — | Metinės pajamos iš palūkanų, dividendų, atskaičius mokesčius | — |
| `hy100g` | `number` | — | `2` | `open` | — | Metinė būsto paskolos palūkanų suma | — |
| `hy110g` | `number` | — | `2` | `open` | — | Metinės jaunesnių nei 16 m. namų ūkio narių gautos pajamos | — |
| `hy110n` | `number` | — | `2` | `open` | — | Metinės jaunesnių nei 16 m. namų ūkio narių gautos pajamos, atskaičius mokesčius | — |
| `hy120g` | `number` | — | `2` | `open` | — | Metiniai žemės ir nekilnojamojo turto mokesčiai (išskyrus už žemės ūkio ir miško paskirties žemę) | — |
| `hy130g` | `number` | — | `2` | `open` | — | Metinė pinigų parama kitiems namų ūkiams | — |
| `hy131g` | `number` | — | `2` | `open` | — | Metinė alimentų suma, duota kitiems namų ūkiams | — |
| `hy140g` | `number` | — | `2` | `open` | — | Metinė gyventojų pajamų mokesčio ir privalomojo sveikatos draudimo įmokų suma | — |
| `hy145n` | `number` | — | `2` | `open` | — | Metinė grąžintina permokėta gyventojų pajamų mokesčio suma | — |
| `hy170g` | `number` | — | `2` | `open` | — | Metinė suvartotų produktų, gautų iš savo asmeninio ūkio, vertė | — |
| `db090` | `number` | — | `3` | `open` | — | Namų ūkio kalibruotasis svoris | — |
| `ap` | `string` | — | `4` | `open` | — | Apskritys | — |
| `sl` | `string` | — | `4` | `open` | — | Sluoksniai | — |
| `m_k` | `string` | — | `4` | `open` | — | Miestas ar kaimas | — |
| `hd080` | `string` | — | `4` | `open` | — | Ar namų ūkis keičia susidėvėjusius ar sulūžusius baldus? | — |
| `metai` | `date` | `Y` | `4` | `open` | — | Statistinio tyrimo metai | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `hh010` | `"1"` | — | — | Vieno buto namas | — |
| `hh010` | `"2"` | — | — | Butas dviejų butų name | — |
| `hh010` | `"3"` | — | — | Butas daugiabučiame name, kuriame mažiau nei 10 butų | — |
| `hh010` | `"4"` | — | — | Butas daugiabučiame name, kuriame 10 ar daugiau butų | — |
| `hh010` | `"5"` | — | — | Kita gyvenamoji patalpa | — |
| `hh021` | `"1"` | — | — | Visateisis šio būsto savininkas, neturintis išmokėti paskolos šiam būstui įsigyti | — |
| `hh021` | `"2"` | — | — | Būsto savininkas, turintis neišmokėtą paskolą šiam būstui įsigyti | — |
| `hh021` | `"3"` | — | — | Nuomininkas arba subnuomininkas, mokantis nuomą rinkos kaina | — |
| `hh021` | `"4"` | — | — | Nuomojasi šį būstą mažesne nei rinkos kaina | — |
| `hh021` | `"5"` | — | — | Gyvena nemokėdamas nuomos | — |
| `hh030` | `1` | — | — | Kambarių skaičius | — |
| `hh030` | `2` | — | — | Kambarių skaičius | — |
| `hh030` | `3` | — | — | Kambarių skaičius | — |
| `hh030` | `4` | — | — | Kambarių skaičius | — |
| `hh030` | `5` | — | — | Kambarių skaičius | — |
| `hh030` | `6` | — | — | Kambarių skaičius | — |
| `hh030` | `7` | — | — | Kambarių skaičius | — |
| `hh030` | `8` | — | — | Kambarių skaičius | — |
| `hh030` | `9` | — | — | Kambarių skaičius | — |
| `hh030` | `10` | — | — | 10 ar daugiau kambarių | — |
| `hh040` | `"1"` | — | — | Taip | — |
| `hh040` | `"2"` | — | — | Ne | — |
| `hh050` | `"1"` | — | — | Taip | — |
| `hh050` | `"2"` | — | — | Ne | — |
| `hh081` | `"1"` | — | — | Taip, naudojasi tik Jūsų namų ūkis | — |
| `hh081` | `"2"` | — | — | Taip, naudojasi Jūsų ir kitas namų ūkis | — |
| `hh081` | `"3"` | — | — | Ne | — |
| `hh091` | `"1"` | — | — | Taip, naudojasi tik Jūsų namų ūkis | — |
| `hh091` | `"2"` | — | — | Taip, naudojasi Jūsų ir kitas namų ūkis | — |
| `hh091` | `"3"` | — | — | Ne | — |
| `hs011` | `"1"` | — | — | Taip, 1 kartą | — |
| `hs011` | `"2"` | — | — | Taip, 2 ir daugiau kartų | — |
| `hs011` | `"3"` | — | — | Ne | — |
| `hs021` | `"1"` | — | — | Taip, 1 kartą | — |
| `hs021` | `"2"` | — | — | Taip, 2 ir daugiau kartų | — |
| `hs021` | `"3"` | — | — | Ne | — |
| `hs031` | `"1"` | — | — | Taip, 1 kartą | — |
| `hs031` | `"2"` | — | — | Taip, 2 ir daugiau kartų | — |
| `hs031` | `"3"` | — | — | Ne | — |
| `hs040` | `"1"` | — | — | Taip | — |
| `hs040` | `"2"` | — | — | Ne | — |
| `hs050` | `"1"` | — | — | Taip | — |
| `hs050` | `"2"` | — | — | Ne | — |
| `hs060` | `"1"` | — | — | Taip | — |
| `hs060` | `"2"` | — | — | Ne | — |
| `hs070` | `"1"` | — | — | Taip | — |
| `hs070` | `"2"` | — | — | Ne, nes negaliu sau to leisti | — |
| `hs070` | `"3"` | — | — | Ne, dėl kitos priežasties | — |
| `hs080` | `"1"` | — | — | Taip | — |
| `hs080` | `"2"` | — | — | Ne, nes negaliu sau to leisti | — |
| `hs080` | `"3"` | — | — | Ne, dėl kitos priežasties | — |
| `hs090` | `"1"` | — | — | Taip | — |
| `hs090` | `"2"` | — | — | Ne, nes negali sau to leisti | — |
| `hs090` | `"3"` | — | — | Ne, dėl kitos priežasties | — |
| `hs100` | `"1"` | — | — | Taip | — |
| `hs100` | `"2"` | — | — | Ne, nes negaliu sau to leisti | — |
| `hs100` | `"3"` | — | — | Ne, dėl kitos priežasties | — |
| `hs110` | `"1"` | — | — | Taip | — |
| `hs110` | `"2"` | — | — | Ne, nes negali sau to leisti | — |
| `hs110` | `"3"` | — | — | Ne, dėl kitos priežasties | — |
| `hs120` | `"1"` | — | — | Labai sunkiai | — |
| `hs120` | `"2"` | — | — | Sunkiai | — |
| `hs120` | `"3"` | — | — | Su kai kuriais sunkumais | — |
| `hs120` | `"4"` | — | — | Gana lengvai (nesunkiai) | — |
| `hs120` | `"5"` | — | — | Lengvai | — |
| `hs120` | `"6"` | — | — | Labai lengvai | — |
| `hs140` | `"1"` | — | — | Labai didelė našta | — |
| `hs140` | `"2"` | — | — | Šiokia tokia našta | — |
| `hs140` | `"3"` | — | — | Nėra našta | — |
| `hs150` | `"1"` | — | — | Labai didelė našta | — |
| `hs150` | `"2"` | — | — | Šiokia tokia našta | — |
| `hs150` | `"3"` | — | — | Nėra našta | — |
| `hs160` | `"1"` | — | — | Taip | — |
| `hs160` | `"2"` | — | — | Ne | — |
| `hs170` | `"1"` | — | — | Taip | — |
| `hs170` | `"2"` | — | — | Ne | — |
| `hs180` | `"1"` | — | — | Taip | — |
| `hs180` | `"2"` | — | — | Ne | — |
| `hs190` | `"1"` | — | — | Taip | — |
| `hs190` | `"2"` | — | — | Ne | — |
| `ap` | `"1"` | — | — | Alytaus apskritis | — |
| `ap` | `"2"` | — | — | Kauno apskritis | — |
| `ap` | `"3"` | — | — | Klaipėdos apskritis | — |
| `ap` | `"4"` | — | — | Marijampolės apskritis | — |
| `ap` | `"5"` | — | — | Panevėžio apskritis | — |
| `ap` | `"6"` | — | — | Šiaulių apskritis | — |
| `ap` | `"7"` | — | — | Tauragės apskritis | — |
| `ap` | `"8"` | — | — | Telšių apskritis | — |
| `ap` | `"9"` | — | — | Utenos apskritis | — |
| `ap` | `"10"` | — | — | Vilniaus apskritis | — |
| `sl` | `"1"` | — | — | Vilnius | — |
| `sl` | `"2"` | — | — | Kaunas | — |
| `sl` | `"3"` | — | — | Klaipėda | — |
| `sl` | `"4"` | — | — | Šiauliai | — |
| `sl` | `"5"` | — | — | Panevėžys | — |
| `sl` | `"6"` | — | — | Kiti miestai | — |
| `sl` | `"7"` | — | — | Kaimai | — |
| `m_k` | `"1"` | — | — | Miestas | — |
| `m_k` | `"2"` | — | — | Kaimas | — |
| `hd080` | `"1"` | — | — | Taip | — |
| `hd080` | `"2"` | — | — | Ne, nes negali sau to leisti | — |
| `hd080` | `"3"` | — | — | Ne, dėl kitos priežasties | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `hh060` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hh061` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hh070` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hh071` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy010` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy020` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy022` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy023` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy040g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy040n` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy050g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy050n` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy060g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy070g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy080g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy081g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy090g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy090n` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy100g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy110g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy110n` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy120g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy130g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy131g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy140g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy145n` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `hy170g` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `ap` | `create(property: "apskritis", type: "ref", ref: "/datasets/gov/rc/ar/apskritis/Apskritis")` | `type` | `2` | `open` | — | — | — |
| `ap` | `update(property: "apskritis.adm_kodas", type: "")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/pajamu_ir_gyvenimo_salygos.csv
