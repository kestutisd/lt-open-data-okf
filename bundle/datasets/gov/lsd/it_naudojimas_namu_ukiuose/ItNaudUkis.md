---
type: Table
title: "ItNaudUkis — Informacinių technologijų naudojimas namų ūkiuose"
description: "Spinta table datasets/gov/lsd/it_naudojimas_namu_ukiuose/ItNaudUkis (46 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/it_naudojimas_namu_ukiuose/ItNaudUkis"
tags: [gov, lsd, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/it_naudojimas_namu_ukiuose.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/it_naudojimas_namu_ukiuose.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# ItNaudUkis — Informacinių technologijų naudojimas namų ūkiuose

- **Model:** `datasets/gov/lsd/it_naudojimas_namu_ukiuose/ItNaudUkis`[^manifest]
- **Dataset:** [Informacinių technologijų naudojimas namų ūkiuose](../it_naudojimas_namu_ukiuose.md) (`datasets/gov/lsd/it_naudojimas_namu_ukiuose`)
- **Manifest CSV:** [datasets/gov/lsd/it_naudojimas_namu_ukiuose.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/it_naudojimas_namu_ukiuose.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/it_naudojimas_namu_ukiuose/ItNaudUkis`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `comp` | `string` | — | `4` | `open` | — | Ar Jūsų namų ūkis namuose naudojasi kompiuteriu (stacionariu, nešiojamuoju, planšetiniu)? | — |
| `iacc` | `string` | — | `4` | `open` | — | Ar namų ūkis namuose naudojasi internetu jungdamasis per kompiuterį, telefoną ar kitą įrenginį? | — |
| `dsl` | `string` | — | `4` | `open` | — | Prisijungimo prie interneto būdas: DSL (ADSL, SDSL, VDSL) (interneto ryšys, teikiamas per skaitmeninę abonentinę liniją) | — |
| `bbwfx` | `string` | — | `4` | `open` | — | Prisijungimo prie interneto būdas: kabelinės, šviesolaidinės ryšio linijos | — |
| `bbfwl` | `string` | — | `4` | `open` | — | Prisijungimo prie interneto būdas: fiksuotas belaidis ryšys (palydovinis ryšys, WiFi, WiMax , pvz., Erdvės, Mezon) | — |
| `bbmobh` | `string` | — | `4` | `open` | — | Prisijungimo prie interneto būdas: trečiosios ar aukštesnės kartos mobilusis ryšys (UMTS), jungiantis per telefoną | — |
| `bbmobm` | `string` | — | `4` | `open` | — | Prisijungimo prie interneto būdas: trečiosios ar aukštesnės kartos mobilusis ryšys (UMTS), naudojantis USB modemu ar ryšio kortele per nešiojamą kompiuterį | — |
| `dialup1` | `string` | — | `4` | `open` | — | Prisijungimo prie interneto būdas: komutuojamoji telefono linija (angl. dial-up) | — |
| `mphnar1` | `string` | — | `4` | `open` | — | Prisijungimo prie interneto būdas: Mobilusis ryšys (GPRS ir kt. žemesnis nei 3G kartos mobilusis ryšys) naudojantis USB modemu ar SIM kortele per nešiojamąjį kompiuterį ar jungiantis per telefoną | — |
| `xelse` | `string` | — | `4` | `open` | — | Dėl kokių priežasčių namų ūkis neturi interneto namuose: naudojasi internetu kitur | — |
| `xneed` | `string` | — | `4` | `open` | — | Dėl kokių priežasčių namų ūkis neturi interneto namuose: internetas nereikalingas, nes nedomina | — |
| `xequ` | `string` | — | `4` | `open` | — | Dėl kokių priežasčių namų ūkis neturi interneto namuose: brangi įranga | — |
| `xacc` | `string` | — | `4` | `open` | — | Dėl kokių priežasčių namų ūkis neturi interneto namuose: brangus ryšys | — |
| `xskl` | `string` | — | `4` | `open` | — | Dėl kokių priežasčių namų ūkis neturi interneto namuose: neturi reikiamų žinių | — |
| `xsec` | `string` | — | `4` | `open` | — | Dėl kokių priežasčių namų ūkis neturi interneto namuose: dėl privatumo, saugumo | — |
| `xbbna` | `string` | — | `4` | `open` | — | Dėl kokių priežasčių namų ūkis neturi interneto namuose: plačiajuostis internetas nepasiekiamas namų ūkio gyvenamojoje vietovėje | — |
| `xdis` | `string` | — | `4` | `open` | — | Dėl kokių priežasčių namų ūkis neturi interneto namuose: dėl fizinės ar jutiminės negalios | — |
| `xoth` | `string` | — | `4` | `open` | — | Dėl kokių priežasčių namų ūkis neturi interneto namuose: kita (-os) | — |
| `geo_nuts2` | `string` | — | `4` | `open` | — | REGIONAS − NUTS 2 | — |
| `geo_nuts3` | `string` | — | `4` | `open` | — | REGIONAS − NUTS 3 | — |
| `geo_dens` | `string` | — | `4` | `open` | — | Gyventojų tankumas | — |
| `deg_urba` | `string` | — | `4` | `open` | — | Gyventojų tankumas | — |
| `hh_pop` | `integer` | — | `4` | `open` | — | Namų ūkio narių skaičius (įskaitant vaikus) | — |
| `hh_pop_16_24` | `integer` | — | `4` | `open` | — | 16 - 24 metų amžiaus asmenų skaičius namų ūkyje | — |
| `hh_pop_16_24s` | `integer` | — | `4` | `open` | — | 16 - 24 metų amžiaus studentų skaičius namų ūkyje | — |
| `hh_pop_25_64` | `integer` | — | `4` | `open` | — | 25 - 64 metų amžiaus asmenų skaičius namų ūkyje | — |
| `hh_pop_65_max` | `integer` | — | `4` | `open` | — | 65 metų ir vyresnių asmenų skaičius namų ūkyje | — |
| `hh_child` | `integer` | — | `4` | `open` | — | Vaikų skaičius namų ūkyje | — |
| `hh_child_14_15` | `integer` | — | `4` | `open` | — | 14 - 15 metų amžiaus vaikų skaičius namų ūkyje | — |
| `hh_child_5_13` | `integer` | — | `4` | `open` | — | 5 - 13 metų amžiaus vaikų skaičius namų ūkyje | — |
| `hh_child_le_4` | `integer` | — | `4` | `open` | — | 4 metų ir jaunesnių vaikų skaičius namų ūkyje | — |
| `hh_wght` | `number` | — | `3` | `open` | — | Namų ūkio populiacijos svoris | — |
| `hh_iq` | `string` | — | `4` | `open` | — | Namų ūkio pajamų kvartiliai | — |
| `hh_id` | `string` | — | `4` | `open` | — | Namų ūkio ID | — |
| `bb` | `string` | — | `4` | `open` | — | Prisijungimo prie interneto būdas: plačiajuostis ryšys (pvz., DSL, kabelinis, šviesolaidinis, palydovinis, 3G ar aukštesnės kartos mobilusis ryšys (UMTS)) | — |
| `idkpc` | `string` | — | `4` | `open` | — | Kokį prietaisą naudojate naršyti internete: stalinį kompiuterį | — |
| `iport` | `string` | — | `4` | `open` | — | Kokį prietaisą naudojate naršyti internete: nešiojamąjį ar planšetinį kompiuterį | — |
| `iothdv` | `string` | — | `4` | `open` | — | Kokį prietaisą naudojate naršyti internete: kitą mobilųjį įrenginį (mobilųjį ar išmanųjį telefoną, medijos ar žaidimų leistuvą, el. knygų skaityklę) | — |
| `itv2` | `string` | — | `4` | `open` | — | Kokį prietaisą naudojate naršyti internete: televizorių (įskaitant išmanųjį televizorių) | — |
| `igame` | `string` | — | `4` | `open` | — | Kokį prietaisą naudojate naršyti internete: žaidimų kompiuterį (angl. Console) | — |
| `idevz` | `string` | — | `4` | `open` | — | Nežino (kokį prietaisą naudoja naršyti internete) | — |
| `bbfix` | `string` | — | `4` | `open` | — | Prisijungimo prie interneto būdas: plačiajuostis laidinis ar belaidis fiksuotas ryšys (DSL, kabelinis, šviesolaidinis, palydovinis ryšys, WiFi, WiMax, pvz., Erdvės, Mezon) | — |
| `bbmob` | `string` | — | `4` | `open` | — | Prisijungimo prie interneto būdas: plačiajuostis ryšys jungiantis per mobiliojo ryšio tinklus (3G ar aukštesnės kartos mobilusis ryšys (UMTS), naudojantis USB modemu ar SIM kortele per nešiojamąjį kompiuterį ar jungiantis per telefoną | — |
| `geo_dev` | `string` | — | `4` | `open` | — | Geografinė padėtis | — |
| `hh_iq5` | `string` | — | `4` | `open` | — | Namų ūkio ekvivalentinių pajamų kvintiliai | — |
| `metai` | `date` | `Y` | `4` | `open` | — | Atlikto statistinio tyrimo metai | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `comp` | `"1"` | — | — | Taip | — |
| `comp` | `"0"` | — | — | Ne | — |
| `iacc` | `"1"` | — | — | Taip | — |
| `iacc` | `"0"` | — | — | Ne | — |
| `iacc` | `"8"` | — | — | Nežinau | — |
| `dsl` | `"1"` | — | — | Taip | — |
| `dsl` | `"0"` | — | — | Ne | — |
| `dsl` | `"9"` | — | — | Nežinau | — |
| `bbwfx` | `"1"` | — | — | Taip | — |
| `bbwfx` | `"0"` | — | — | Ne | — |
| `bbwfx` | `"9"` | — | — | Nežinau | — |
| `bbfwl` | `"1"` | — | — | Taip | — |
| `bbfwl` | `"0"` | — | — | Ne | — |
| `bbfwl` | `"9"` | — | — | Nežinau | — |
| `bbmobh` | `"1"` | — | — | Taip | — |
| `bbmobh` | `"0"` | — | — | Ne | — |
| `bbmobh` | `"9"` | — | — | Nežinau | — |
| `bbmobm` | `"1"` | — | — | Taip | — |
| `bbmobm` | `"0"` | — | — | Ne | — |
| `bbmobm` | `"9"` | — | — | Nežinau | — |
| `dialup1` | `"1"` | — | — | Taip | — |
| `dialup1` | `"0"` | — | — | Ne | — |
| `dialup1` | `"9"` | — | — | Nežinau | — |
| `mphnar1` | `"1"` | — | — | Taip | — |
| `mphnar1` | `"0"` | — | — | Ne | — |
| `mphnar1` | `"9"` | — | — | Nežinau | — |
| `xelse` | `"1"` | — | — | Taip | — |
| `xelse` | `"0"` | — | — | Ne | — |
| `xelse` | `"9"` | — | — | Nežinau | — |
| `xneed` | `"1"` | — | — | Taip | — |
| `xneed` | `"0"` | — | — | Ne | — |
| `xneed` | `"9"` | — | — | Nežinau | — |
| `xequ` | `"1"` | — | — | Taip | — |
| `xequ` | `"0"` | — | — | Ne | — |
| `xequ` | `"9"` | — | — | Nežinau | — |
| `xacc` | `"1"` | — | — | Taip | — |
| `xacc` | `"0"` | — | — | Ne | — |
| `xacc` | `"9"` | — | — | Nežinau | — |
| `xskl` | `"1"` | — | — | Taip | — |
| `xskl` | `"0"` | — | — | Ne | — |
| `xskl` | `"9"` | — | — | Nežinau | — |
| `xsec` | `"1"` | — | — | Taip | — |
| `xsec` | `"0"` | — | — | Ne | — |
| `xsec` | `"9"` | — | — | Nežinau | — |
| `xbbna` | `"1"` | — | — | Taip | — |
| `xbbna` | `"0"` | — | — | Ne | — |
| `xbbna` | `"9"` | — | — | Nežinau | — |
| `xdis` | `"1"` | — | — | Taip | — |
| `xdis` | `"0"` | — | — | Ne | — |
| `xdis` | `"9"` | — | — | Netaikoma | — |
| `xoth` | `"1"` | — | — | Taip | — |
| `xoth` | `"0"` | — | — | Ne | — |
| `xoth` | `"9"` | — | — | Nežinau | — |
| `geo_nuts2` | `"LT01"` | — | — | Sostinės regionas | — |
| `geo_nuts2` | `"LT02"` | — | — | Vidurio ir vakarų Lietuvos regionas | — |
| `geo_nuts3` | `"LT00A"` | — | — | Vilniaus apskritis | — |
| `geo_nuts3` | `"LT001"` | — | — | Alytaus apskritis | — |
| `geo_nuts3` | `"LT002"` | — | — | Kauno apskritis | — |
| `geo_nuts3` | `"LT003"` | — | — | Klaipėdos apskritis | — |
| `geo_nuts3` | `"LT004"` | — | — | Marijampolės apskritis | — |
| `geo_nuts3` | `"LT005"` | — | — | Panevėžio apskritis | — |
| `geo_nuts3` | `"LT006"` | — | — | Šiaulių apskritis | — |
| `geo_nuts3` | `"LT007"` | — | — | Tauragės apskritis | — |
| `geo_nuts3` | `"LT008"` | — | — | Telšių apskritis | — |
| `geo_nuts3` | `"LT009"` | — | — | Utenos apskritis | — |
| `geo_dens` | `"1"` | — | — | Tankiai apgyvendinta vietovė | — |
| `geo_dens` | `"3"` | — | — | Retai apgyvendinta vietovė | — |
| `deg_urba` | `"1"` | — | — | Iš esmės miesto vietovė | — |
| `deg_urba` | `"2"` | — | — | Tarpinė vietovė | — |
| `deg_urba` | `"3"` | — | — | Iš esmės kaimo vietovė | — |
| `hh_iq` | `"1"` | — | — | Pirmasis kvartilis | — |
| `hh_iq` | `"2"` | — | — | Antrasis kvartilis | — |
| `hh_iq` | `"3"` | — | — | Trečiasis kvartilis | — |
| `hh_iq` | `"4"` | — | — | Ketvirtasis kvartilis | — |
| `bb` | `"1"` | — | — | Taip | — |
| `bb` | `"0"` | — | — | Ne | — |
| `bb` | `"9"` | — | — | Nežinau | — |
| `idkpc` | `"1"` | — | — | Taip | — |
| `idkpc` | `"0"` | — | — | Ne | — |
| `idkpc` | `"9"` | — | — | Nežinau | — |
| `iport` | `"1"` | — | — | Taip | — |
| `iport` | `"0"` | — | — | Ne | — |
| `iport` | `"9"` | — | — | Nežinau | — |
| `iothdv` | `"1"` | — | — | Taip | — |
| `iothdv` | `"0"` | — | — | Ne | — |
| `iothdv` | `"9"` | — | — | Nežinau | — |
| `itv2` | `"1"` | — | — | Taip | — |
| `itv2` | `"0"` | — | — | Ne | — |
| `itv2` | `"9"` | — | — | Nežinau | — |
| `igame` | `"1"` | — | — | Taip | — |
| `igame` | `"0"` | — | — | Ne | — |
| `igame` | `"9"` | — | — | Nežinau | — |
| `idevz` | `"1"` | — | — | Taip | — |
| `idevz` | `"0"` | — | — | Ne | — |
| `idevz` | `"9"` | — | — | Nežinau | — |
| `bbfix` | `"1"` | — | — | Taip | — |
| `bbfix` | `"0"` | — | — | Ne | — |
| `bbfix` | `"9"` | — | — | Nežinau | — |
| `bbmob` | `"1"` | — | — | Taip | — |
| `bbmob` | `"0"` | — | — | Ne | — |
| `bbmob` | `"9"` | — | — | Nežinau | — |
| `geo_dev` | `"1"` | — | — | Mažiau išvysytame regione | — |
| `geo_dev` | `"2"` | — | — | Tarpiniame regione | — |
| `geo_dev` | `"3"` | — | — | Labiau išvysytame regione | — |
| `hh_iq5` | `"1"` | — | — | Pirmasis (žemiausias) kvintilis | — |
| `hh_iq5` | `"2"` | — | — | Antrasis (žemiausias) kvintilis | — |
| `hh_iq5` | `"3"` | — | — | Trečiasis (vidurinis) kvintilis | — |
| `hh_iq5` | `"4"` | — | — | Ketvirtasis (antrasis aukščiausias) kvintilis | — |
| `hh_iq5` | `"5"` | — | — | Penktasis (aukščiausias) kvintilis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/it_naudojimas_namu_ukiuose.csv
