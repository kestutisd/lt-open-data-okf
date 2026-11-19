---
type: Table
title: "Reklama"
description: "Spinta table datasets/gov/vrk/reklama/Reklama (46 columns)."
tags: [gov, vrk, reklama, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/reklama.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/vrk/reklama.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Reklama

- **Model:** `datasets/gov/vrk/reklama/Reklama`[^manifest]
- **Dataset:** [datasets/gov/vrk/reklama](../reklama.md) (`datasets/gov/vrk/reklama`)[^manifest]
- **Manifest CSV:** [datasets/gov/vrk/reklama.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/reklama.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `vrk` — Vyriausioji rinkimų komisija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `reklamos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `reklamos_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `rinkimu_id` | `integer` | — | `2` | `open` | — | Rinkimų identifikatorius | Rinkimų identifikatorius |
| `rinkimu_pavad` | `string` | — | `2` | `open` | — | Rinkimų pavadinimas | — |
| `rink_apyg_id` | `integer` | — | `2` | `open` | — | Rinkimų apygardos identifikatorius | — |
| `apyg_id` | `integer` | — | `2` | `open` | — | Apygardos identifikatorius | — |
| `apyg_nr` | `integer` | — | `2` | `open` | — | Apygardos numeris | — |
| `apyg_pavad` | `string` | — | `2` | `open` | — | Apygardos pavadinimas | — |
| `p_kamp_rusis` | `string` | — | `2` | `open` | — | Politinės kampanijos rūšis | Nurodoma politinė kampanijos rūšis (Seimo rinkimai / Savivaldybių tarybų rinkimai / Respublikos Prezidento rinkimai / rinkimai į Europos Parlamentą / Referendumas) |
| `p_kamp_id` | `integer` | — | `2` | `open` | — | Politinės kampanijos identifikatorius | — |
| `p_kamp_pavad` | `string` | — | `2` | `open` | — | Politinės kampanijos pavadinimas | Politinės kampanijos pavadinimas |
| `p_kamp_dal_id` | `integer` | — | `2` | `open` | — | Politinės kampanijos dalyvio identifikatorius | — |
| `p_kamp_dal_pavad` | `string` | — | `2` | `open` | — | Politinės kampanijos dalyvio pavardė/pavadinimas | — |
| `p_kamp_dal_vardas` | `string` | — | `2` | `open` | — | Politinės kampanijos dalyvio vardas | — |
| `dal_tipo_kodas` | `string` | — | `2` | `open` | — | Politinės kampanijos dalyvio tipo kodas | Politinės kampanijos dalyvio tipo kodas (KS, FA, RO) |
| `dal_tipas` | `string` | — | `2` | `open` | — | Politinės kampanijos dalyvio tipas | Politinė partija / Politinės partijos keltas kandidatų sąrašas / Visuomeninis rinkimų komitetas/ Išsikėlęs kandidatas |
| `dal_reg_busena` | `string` | — | `2` | `open` | — | Politinės kampanijos dalyvio registravimo būsena | Panaikintas/Registruotas/ Šablonas/Atsisakyta/Anuliuotas |
| `virs_ja_kodas` | `string` | — | `2` | `open` | — | Viešosios informacijos rengėjo/ skleidėjo (VIRS) juridinio asmens kodas Juridinių asmenų registre | susiejimui su RC duomenimis |
| `virs_pavad` | `string` | — | `2` | `open` | — | Viešosios informacijos rengėjo/ skleidėjo (VIRS) pavadinimas | — |
| `virs_tipo_kodas` | `integer` | — | `2` | `open` | — | VIRS tipo kodas | Kodų intervalas 1-8 |
| `virs_tipo_pavad` | `string` | — | `2` | `open` | — | VIRS tipo aprašymas (pavadinimas) | Agentūra / Spauda / Radijas / Televizija / Internetas / Lauko reklama / VIRS grupė / Kita / Visos (išskyrus agentūras) |
| `reklamos_data_nuo` | `date` | `D` | `4` | `open` | — | Politinės reklamos data nuo | — |
| `reklamos_data_iki` | `date` | `D` | `4` | `open` | — | Politinės reklamos data iki | — |
| `leidinio_nr` | `string` | — | `4` | `open` | — | Periodinio spaudos leidinio numeris | — |
| `reklamos_pavad` | `string` | — | `4` | `open` | — | Politinės reklamos pavadinimas | — |
| `uzsakymo_nr` | `string` | — | `4` | `open` | — | Užsakymo numeris | — |
| `reklamos_formos_kodas` | `string` | — | `4` | `open` | — | Politinės reklamos formos kodas | KIT, REL, INP, REP, PAD, LAN, INS, SCI, STD, VZE, RKP, GRE, TIE, AGL, SKD, STR, SVE, SKE, DIS, VAI, SIU, AGS, TNT, KAL, ISS, DIL, BEE, PLA, INT |
| `reklamos_forma` | `string` | — | `4` | `open` | — | Politinės reklamos formos pavadinimas | Agitacinis siužetas / Lankstinukas / Plakatas / Skydelis / Straipsnis / Agitacinė laida / Reklaminis leidinys / Siužetas / Skelbimas / Stendas / Vaizdo įrašas / Diskusija / Diskusijų laida / Kalendoriukas / Reklaminis puslapis / Sveikinimas / Tentas / Interneto svetainė / Interviu / Tiesioginė transliacija / Vaizdo ekranas / Bėganti eilutė / Garso reklama / Informacinis pranešimas / Iššokantis langas / Reportažas / Straipsnių ciklas / Padėka / Kita |
| `reklamos_apimtis` | `string` | — | `4` | `open` | — | Politinės reklamos apimtis | Politinės reklamos dydis/trukmė pagal reklamos formą (h/min/s arba kv.m/kv.cm) |
| `reklamos_kiekis` | `integer` | — | `4` | `open` | — | Politinės reklamos kiekis | Politinės reklamos kiekis (vnt.) |
| `islaidu_paskirties_kodas` | `string` | — | `2` | `open` | — | Išlaidų paskirties kodas | RT, RR, RS, RI, RIN, RK, NPK |
| `islaidu_paskirtis` | `string` | — | `2` | `open` | — | Išlaidų paskirties aprašymas (pavadinimas) | RT - Politinė reklama televizijoje. RR - Politinė reklama radijuje. RS - Politinė reklama spaudoje. RI - Išorinė politinė reklama. RIN - Reklama internete. RK - Kitomis priemonėmis skleidžiama reklama. NPK - Ne politinės kampanijos laikotarpiu turėtos išlaidos, jeigu įsigyti daiktai ir kitas turtas yra skirti politinei kampanijai ar jeigu paslaugos yra gautos politinės kampanijos laikotarpiu. Žiniaraštyje registruota išlaidų paskirtis (nuo 2016 m.) |
| `reklamos_kaina` | `number` | — | `4` | `open` | — | Paskelbtos politinės reklamos kaina, Eur | — |
| `apmok_is_p_kamp` | `number` | — | `4` | `open` | — | Apmokėta iš politinės kampanijos sąskaitos, Eur | — |
| `neapmok_reklama` | `number` | — | `4` | `open` | — | Neapmokėta politinė reklama, Eur | — |
| `apmok_rengejo` | `number` | — | `4` | `open` | — | Politinė reklama apmokėta rengėjo ar skleidėjo lėšomis, Eur | — |
| `apmok_kito_salt` | `number` | — | `4` | `open` | — | Politinė reklama apmokėta kito šaltinio lėšomis, Eur | — |
| `pasl_teikejo_tipas` | `string` | — | `4` | `open` | — | Paslaugų teikėjo tipas (FA/JA) | Paslaugų teikėjo tipas (Fizinis asmuo/ Juridinis asmuo) arba (FA/JA) |
| `kito_salt_ja_kodas` | `string` | — | `2` | `open` | — | Kito šaltinio juridinio asmens kodas Juridinių asmenų registre | Tik juridinių asmenų |
| `kito_salt_pavad` | `string` | — | `2` | `open` | — | Kito šaltinio pavadinimas | Jei fizinis asmuo ir jis kampanijos dalyvis (savarankiškas arba jo atstovaujamas atstovaujamasis, vardas pavardė. Kitais atvejais naudojamas HASH kodas. |
| `org_pavad` | `string` | — | `2` | `open` | — | Politinės kampanijos dalyvį iškėlusios organizacijos pavadinimas | — |
| `sask_f_nr` | `string` | — | `2` | `open` | — | Sąskaitos faktūros numeris | — |
| `sask_f_israse` | `string` | — | `2` | `open` | — | Sąskaitą faktūrą išrašęs asmuo | — |
| `sask_f_ja_kodas` | `string` | — | `2` | `open` | — | Sąskaitą faktūrą išrašiusio juridinio asmens kodas Juridinių asmenų registre | Sąskaitą faktūrą išrašiusio juridinio asmens kodas Juridinių asmenų registre (nuo 2016 m.) |
| `sutarties_nr` | `string` | — | `4` | `open` | — | Sutarties numeris | Sutarties numeris (nuo 2016 m.) |
| `vrk_spr_nr` | `string` | — | `4` | `open` | — | VRK sprendimo numeris | VRK sprendimo, kuriuo papildytas politinės kampanijos dalyvio finansavimo apskaitos žiniaraštis, numeris (nuo 2016 m.) |
| `vrk_spr_data` | `date` | `D` | `4` | `open` | — | VRK sprendimo data | VRK sprendimo, kuriuo papildytas politinės kampanijos dalyvio finansavimo apskaitos žiniaraštis, data (nuo 2016 m.) |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `p_kamp_rusis` | `"EP"` | — | — | Rinkimai į Europos Parlamentą | — |
| `p_kamp_rusis` | `"PRE"` | — | — | Prezidento rinkimai | — |
| `p_kamp_rusis` | `"REF"` | — | — | Referendumas | — |
| `p_kamp_rusis` | `"SAV"` | — | — | Savivaldybių tarybų rinkimai | — |
| `p_kamp_rusis` | `"SEI"` | — | — | Seimo rinkimai | — |
| `dal_tipo_kodas` | `"K"` | — | — | Kandidatas | — |
| `dal_tipo_kodas` | `"KS"` | — | — | Kandidatų sąrašas | — |
| `dal_tipo_kodas` | `"P"` | — | — | Pretendentas | — |
| `dal_tipo_kodas` | `"PP"` | — | — | Politinė partija | — |
| `dal_tipo_kodas` | `"RI"` | — | — | Referendumo iniciatorius | — |
| `dal_tipo_kodas` | `"V"` | — | — | Politinis komitetas | — |
| `dal_tipas` | `"Kandidatas"` | — | — | Kandidatas | — |
| `dal_tipas` | `"Kandidatų sąrašas"` | — | — | Kandidatų sąrašas | — |
| `dal_tipas` | `"Pretendentas"` | — | — | Pretendentas | — |
| `dal_tipas` | `"Politinė partija"` | — | — | Politinė partija | — |
| `dal_tipas` | `"Referendumo iniciatorius"` | — | — | Referendumo iniciatorius | — |
| `dal_tipas` | `"Politinis komitetas"` | — | — | Politinis komitetas | — |
| `dal_reg_busena` | `"Registruotas"` | — | — | Registruotas | — |
| `dal_reg_busena` | `"Panaikintas"` | — | — | Panaikintas/Praradęs statusą | — |
| `virs_tipo_kodas` | `1` | — | — | Spauda | — |
| `virs_tipo_kodas` | `2` | — | — | Radijas | — |
| `virs_tipo_kodas` | `3` | — | — | Televizija | — |
| `virs_tipo_kodas` | `4` | — | — | Internetas | — |
| `virs_tipo_kodas` | `5` | — | — | Lauko reklama | — |
| `virs_tipo_kodas` | `6` | — | — | Kita | — |
| `virs_tipo_kodas` | `7` | — | — | Agentūra | — |
| `virs_tipo_kodas` | `8` | — | — | VIRS grupė | — |
| `virs_tipo_pavad` | `"Spauda"` | — | — | Spauda | — |
| `virs_tipo_pavad` | `"Radijas"` | — | — | Radijas | — |
| `virs_tipo_pavad` | `"Televizija"` | — | — | Televizija | — |
| `virs_tipo_pavad` | `"Internetas"` | — | — | Internetas | — |
| `virs_tipo_pavad` | `"Lauko reklama"` | — | — | Lauko reklama | — |
| `virs_tipo_pavad` | `"Kita"` | — | — | Kita | — |
| `virs_tipo_pavad` | `"Agentūra"` | — | — | Agentūra | — |
| `virs_tipo_pavad` | `"VIRS grupė"` | — | — | VIRS grupė | — |
| `islaidu_paskirties_kodas` | `"KI"` | — | — | KI - Kitos išlaidos | — |
| `islaidu_paskirties_kodas` | `"KI; RS"` | — | — | KI - Kitos išlaidos; RS - Politinė reklama spaudoje | — |
| `islaidu_paskirties_kodas` | `"NPK"` | — | — | NPK - Ne politinės kampanijos laikotarpiu turėtos išlaidos, jeigu įsigyti daiktai ir kitas turtas yra skirti politinei kampanijai ar jeigu paslaugos yra gautos politinės kampanijos laikotarpiu | — |
| `islaidu_paskirties_kodas` | `"NPK; RI"` | — | — | NPK - Ne politinės kampanijos laikotarpiu turėtos išlaidos, jeigu įsigyti daiktai ir kitas turtas yra skirti politinei kampanijai ar jeigu paslaugos yra gautos politinės kampanijos laikotarpiu; RI - Išorinė politinė reklama | — |
| `islaidu_paskirties_kodas` | `"RI"` | — | — | RI - Išorinė politinė reklama | — |
| `islaidu_paskirties_kodas` | `"RI; RK"` | — | — | RI - Išorinė politinė reklama; RK - Kitomis priemonėmis skleidžiama politinė reklama | — |
| `islaidu_paskirties_kodas` | `"RI; RS"` | — | — | RI - Išorinė politinė reklama; RS - Politinė reklama spaudoje | — |
| `islaidu_paskirties_kodas` | `"RIN"` | — | — | RIN - Politinė reklama internete | — |
| `islaidu_paskirties_kodas` | `"RK"` | — | — | RK - Kitomis priemonėmis skleidžiama politinė reklama | — |
| `islaidu_paskirties_kodas` | `"RK; RR"` | — | — | RK - Kitomis priemonėmis skleidžiama politinė reklama; RR - Politinė reklama radijuje | — |
| `islaidu_paskirties_kodas` | `"RK; RT"` | — | — | RK - Kitomis priemonėmis skleidžiama politinė reklama; RT - Politinė reklama televizijoje | — |
| `islaidu_paskirties_kodas` | `"RR"` | — | — | RR - Politinė reklama radijuje | — |
| `islaidu_paskirties_kodas` | `"RS"` | — | — | RS - Politinė reklama spaudoje | — |
| `islaidu_paskirties_kodas` | `"RS; RT"` | — | — | RS - Politinė reklama spaudoje; RT - Politinė reklama televizijoje | — |
| `islaidu_paskirties_kodas` | `"RT"` | — | — | RT - Politinė reklama televizijoje | — |
| `islaidu_paskirtis` | `"Kitos išlaidos"` | — | — | Kitos išlaidos | — |
| `islaidu_paskirtis` | `"Ne politinės kampanijos laikotarpiu turėtos išlaidos, jeigu įsigyti daiktai ir kitas turtas yra skirti politinei kampanijai ar jeigu paslaugos yra gautos politinės kampanijos laikotarpiu"` | — | — | Ne politinės kampanijos laikotarpiu turėtos išlaidos, jeigu įsigyti daiktai ir kitas turtas yra skirti politinei kampanijai ar jeigu paslaugos yra gautos politinės kampanijos laikotarpiu | — |
| `islaidu_paskirtis` | `"Išorinė politinė reklama"` | — | — | Išorinė politinė reklama | — |
| `islaidu_paskirtis` | `"Kitomis priemonėmis skleidžiama politinė reklama"` | — | — | Kitomis priemonėmis skleidžiama politinė reklama | — |
| `islaidu_paskirtis` | `"Politinė reklama internete"` | — | — | Politinė reklama radijuje | — |
| `islaidu_paskirtis` | `"Politinė reklama spaudoje"` | — | — | Politinė reklama spaudoje | — |
| `islaidu_paskirtis` | `"Politinė reklama televizijoje"` | — | — | Politinė reklama televizijoje | — |
| `pasl_teikejo_tipas` | `"J"` | — | — | Juridinis asmuo | — |
| `pasl_teikejo_tipas` | `"F"` | — | — | Fizinis asmuo | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/reklama.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/reklama.csv#L4)
