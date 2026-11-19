---
type: Table
title: "Pajamos"
description: "Spinta table datasets/gov/vrk/pajamos/Pajamos (30 columns)."
tags: [gov, vrk, pajamos, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/pajamos.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/vrk/pajamos.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pajamos

- **Model:** `datasets/gov/vrk/pajamos/Pajamos`[^manifest]
- **Dataset:** [datasets/gov/vrk/pajamos](../pajamos.md) (`datasets/gov/vrk/pajamos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vrk/pajamos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/pajamos.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `vrk` — Vyriausioji rinkimų komisija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `pajamu_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pajamu_id` | `integer` | — | `4` | `open` | — | Unikalus raktas | — |
| `rinkimu_id` | `integer` | — | `4` | `open` | — | Rinkimų identifikatorius | — |
| `rink_pavad` | `string` | — | `4` | `open` | — | Rinkimų pavadinimas | — |
| `rink_apyg_id` | `integer` | — | `4` | `open` | — | Rinkimų apygardos identifikatorius | — |
| `apyg_id` | `integer` | — | `4` | `open` | — | Apygardos identifikatorius | — |
| `apyg_nr` | `integer` | — | `4` | `open` | — | Apygardos numeris | — |
| `apyg_pavad` | `string` | — | `4` | `open` | — | Apygardos pavadinimas | — |
| `p_kamp_rusis` | `string` | — | `4` | `open` | — | Politinės kampanijos rūšis | Nurodoma politinė kampanijos rūšis (Seimo rinkimai / Savivaldybių tarybų rinkimai / Respublikos Prezidento rinkimai / rinkimai į Europos Parlamentą / Referendumas) |
| `p_kamp_id` | `integer` | — | `4` | `open` | — | Politinės kampanijos identifikatorius | — |
| `p_kamp_pavad` | `string` | — | `4` | `open` | — | Politinės kampanijos pavadinimas | — |
| `p_kamp_dal_pavad` | `string` | — | `4` | `open` | — | Politinės kampanijos pavadinimas | — |
| `p_kamp_dal_id` | `integer` | — | `4` | `open` | — | Politinės kampanijos dalyvio identifikatorius | — |
| `auk_tipas` | `string` | — | `4` | `open` | — | Aukotojo tipas (FA/JA) | Aukotojo tipas (Fizinis asmuo/ Juridinis asmuo) arba (FA/JA) |
| `suma` | `number` | — | `4` | `open` | — | Pajamų suma | Politinės kampanijos dalyvio gautų pajamų suma |
| `auk_ja_kodas` | `string` | — | `4` | `open` | — | Aukotojo juridinio asmens kodas Juridinių asmenų registre | — |
| `auk_ja_pavad` | `string` | — | `4` | `open` | — | Aukotojo juridinio asmens pavadinimas | — |
| `aukotojo_kodas` | `string` | — | `4` | `open` | — | Atsitiktinai sugeneruotas aukotojo fizinio asmens kodas | — |
| `lytis` | `string` | — | `4` | `open` | — | Aukotojo lytis | — |
| `amziaus_grupe` | `string` | — | `4` | `open` | — | Aukotojo amžiaus grupė (aukos mokėjimo dieną) | Aukotojo amžiaus grupė aukojimo dieną intervalais (nuo - iki), kas 5 metai Amžiaus grupės: 18-24; 25-29; 30-34; 35-39; ....; 75-79; 80 +; |
| `lesu_saltinio_kodas` | `string` | — | `4` | `open` | — | Lėšų šaltinio paskirties kodas | Lėšų šaltinio paskirties kodas (FAA, MA, KL, PL, VBA, JAA, BP, DLL, NA) |
| `lesu_saltinis` | `string` | — | `4` | `open` | — | Lėšų šaltinio aprašymas (pavadinimas) | — |
| `paj_dok_data` | `date` | `D` | `4` | `open` | — | Pajamų dokumento data | pavyzdžiui - mokėjimo nurodymo data |
| `paj_dok_nr` | `string` | — | `4` | `open` | — | Pajamų dokumento numeris | — |
| `lesu_formos_kodas` | `string` | — | `4` | `open` | — | Lėšų formos kodas | Lėšų formos kodas: P, G, N |
| `lesu_forma` | `string` | — | `4` | `open` | — | Lėšų forma | Lėšų forma (Piniginės lėšos / Nepiniginės lėšos / Lėšos grynaisiais). |
| `dal_tipo_kodas` | `string` | — | `4` | `open` | — | Politinės kampanijos dalyvio tipo kodas | Politinės kampanijos dalyvio tipo kodas (KS, FA, RO) |
| `dal_tipas` | `string` | — | `4` | `open` | — | Politinės kampanijos dalyvio tipas | Politinės kampanijos dalyvio tipas (Politinė partija / Politinės partijos keltas kandidatų sąrašas / Visuomeninis rinkimų komitetas/ Išsikėlęs kandidatas) |
| `dal_reg_busena` | `string` | — | `4` | `open` | — | Politinės kampanijos dalyvio registravimo būsena | — |
| `vrk_spr_nr` | `string` | — | `4` | `open` | — | VRK sprendimo numeris | VRK sprendimo, kuriuo papildytas politinės kampanijos dalyvio finansavimo apskaitos žiniaraštis, numeris |
| `vrk_spr_data` | `date` | `D` | `4` | `open` | — | VRK sprendimo data | VRK sprendimo, kuriuo papildytas politinės kampanijos dalyvio finansavimo apskaitos žiniaraštis, data |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `p_kamp_rusis` | `"EP"` | — | — | Rinkimai į Europos Parlamentą | — |
| `p_kamp_rusis` | `"PRE"` | — | — | Prezidento rinkimai | — |
| `p_kamp_rusis` | `"REF"` | — | — | Referendumas | — |
| `p_kamp_rusis` | `"SAV"` | — | — | Savivaldybių tarybų rinkimai | — |
| `p_kamp_rusis` | `"SEI"` | — | — | Seimo rinkimai | — |
| `auk_tipas` | `"F"` | — | — | Fizinis asmuo | — |
| `auk_tipas` | `"J"` | — | — | Juridinis asmuo | — |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |
| `amziaus_grupe` | `"18-24"` | — | — | Amžiaus grupė nuo 18 iki 24 metų | — |
| `amziaus_grupe` | `"25-29"` | — | — | Amžiaus grupė nuo 25 iki 29 metų | — |
| `amziaus_grupe` | `"30-34"` | — | — | Amžiaus grupė nuo 30 iki 34 metų | — |
| `amziaus_grupe` | `"35-39"` | — | — | Amžiaus grupė nuo 35 iki 39 metų | — |
| `amziaus_grupe` | `"40-44"` | — | — | Amžiaus grupė nuo 40 iki 44 metų | — |
| `amziaus_grupe` | `"45-49"` | — | — | Amžiaus grupė nuo 45 iki 49 metų | — |
| `amziaus_grupe` | `"50-54"` | — | — | Amžiaus grupė nuo 50 iki 54 metų | — |
| `amziaus_grupe` | `"55-59"` | — | — | Amžiaus grupė nuo 55 iki 59 metų | — |
| `amziaus_grupe` | `"60-64"` | — | — | Amžiaus grupė nuo 60 iki 64 metų | — |
| `amziaus_grupe` | `"65-69"` | — | — | Amžiaus grupė nuo 65 iki 69 metų | — |
| `amziaus_grupe` | `"70-74"` | — | — | Amžiaus grupė nuo 70 iki 74 metų | — |
| `amziaus_grupe` | `"75-79"` | — | — | Amžiaus grupė nuo 75 iki 79 metų | — |
| `amziaus_grupe` | `"80+"` | — | — | Amžiaus grupė nuo 80 metų | — |
| `lesu_saltinio_kodas` | `"AMA"` | — | — | AMA - Fizinių asmenų mažos aukos, registruojamos neišskiriant aukotojų | — |
| `lesu_saltinio_kodas` | `"B"` | — | — | B - Nepriimtina auka pervesta į valstybės biudžetą | — |
| `lesu_saltinio_kodas` | `"BP"` | — | — | BP - Palūkanos už politinės kampanijos sąskaitoje esančias lėšas | — |
| `lesu_saltinio_kodas` | `"DLL"` | — | — | DLL - Politinės kampanijos dalyvio lėšos perduotos juridiniam asmeniui, galinčiam teikti labdarą | — |
| `lesu_saltinio_kodas` | `"FAA"` | — | — | FAA - Fizinio asmens auka | — |
| `lesu_saltinio_kodas` | `"G"` | — | — | G - Nepriimtina auka grąžinta aukotojui | — |
| `lesu_saltinio_kodas` | `"JAA"` | — | — | JAA - Juridinio asmens auka | — |
| `lesu_saltinio_kodas` | `"KL"` | — | — | KL - Kandidato nuosavos (asmeninės) lėšos, paaukotos politinei kampanijai | — |
| `lesu_saltinio_kodas` | `"MA"` | — | — | MA - Fizinio asmens maža auka | — |
| `lesu_saltinio_kodas` | `"N"` | — | — | N - Fizinių asmenų paaukojusių iki 100 Lt vertės auką ir nesutinkančių, kad jų asmens duomenys būtų paviešinti, aukos | — |
| `lesu_saltinio_kodas` | `"NA"` | — | — | NA - Gauta nepriimtina auka | — |
| `lesu_saltinio_kodas` | `"P"` | — | — | P - Nepriimtinos aukos perduotos juridiniam asmeniui galinčiam teikti labdarą | — |
| `lesu_saltinio_kodas` | `"PL"` | — | — | PL - Nuosavos politinės partijos lėšos, skirtos politinei kampanijai | — |
| `lesu_saltinio_kodas` | `"VBA"` | — | — | VBA - Politines partijos gauti valstybės biudžeto asignavimai, panaudoti politinei kampanijai finansuoti | — |
| `lesu_saltinis` | `"Fizinių asmenų mažos aukos, registruojamos neišskiriant aukotojų"` | — | — | Fizinių asmenų mažos aukos, registruojamos neišskiriant aukotojų | — |
| `lesu_saltinis` | `"Nepriimtina auka pervesta į valstybės biudžetą"` | — | — | Nepriimtina auka pervesta į valstybės biudžetą | — |
| `lesu_saltinis` | `"Palūkanos už politinės kampanijos sąskaitoje esančias lėšas"` | — | — | Palūkanos už politinės kampanijos sąskaitoje esančias lėšas | — |
| `lesu_saltinis` | `"Politinės kampanijos dalyvio lėšos perduotos juridiniam asmeniui, galinčiam teikti labdarą"` | — | — | Politinės kampanijos dalyvio lėšos perduotos juridiniam asmeniui, galinčiam teikti labdarą | — |
| `lesu_saltinis` | `"Fizinio asmens auka"` | — | — | Fizinio asmens auka | — |
| `lesu_saltinis` | `"Nepriimtina auka grąžinta aukotojui"` | — | — | Nepriimtina auka grąžinta aukotojui | — |
| `lesu_saltinis` | `"Juridinio asmens auka"` | — | — | Juridinio asmens auka | — |
| `lesu_saltinis` | `"Kandidato nuosavos (asmeninės) lėšos, paaukotos politinei kampanijai"` | — | — | Kandidato nuosavos (asmeninės) lėšos, paaukotos politinei kampanijai | — |
| `lesu_saltinis` | `"Fizinio asmens maža auka"` | — | — | Fizinio asmens maža auka | — |
| `lesu_saltinis` | `"Fizinių asmenų paaukojusių iki 100 Lt vertės auką ir nesutinkančių, kad jų asmens duomenys būtų paviešinti, aukos"` | — | — | Fizinių asmenų paaukojusių iki 100 Lt vertės auką ir nesutinkančių, kad jų asmens duomenys būtų paviešinti, aukos | — |
| `lesu_saltinis` | `"Gauta nepriimtina auka"` | — | — | Gauta nepriimtina auka | — |
| `lesu_saltinis` | `"Nepriimtinos aukos perduotos juridiniam asmeniui galinčiam teikti labdarą"` | — | — | Nepriimtinos aukos perduotos juridiniam asmeniui galinčiam teikti labdarą | — |
| `lesu_saltinis` | `"Nuosavos politinės partijos lėšos, skirtos politinei kampanijai"` | — | — | Nuosavos politinės partijos lėšos, skirtos politinei kampanijai | — |
| `lesu_saltinis` | `"Politines partijos gauti valstybės biudžeto asignavimai, panaudoti politinei kampanijai finansuoti"` | — | — | Politines partijos gauti valstybės biudžeto asignavimai, panaudoti politinei kampanijai finansuoti | — |
| `lesu_formos_kodas` | `"P"` | — | — | P – Piniginės lėšos | — |
| `lesu_formos_kodas` | `"G"` | — | — | G – Lėšos grynaisiais | — |
| `lesu_formos_kodas` | `"N"` | — | — | N – Nepiniginės lėšos | — |
| `lesu_forma` | `"Piniginės lėšos"` | — | — | Piniginės lėšos | — |
| `lesu_forma` | `"Lėšos grynaisiais"` | — | — | Lėšos grynaisiais | — |
| `lesu_forma` | `"Nepiniginės lėšos"` | — | — | Nepiniginės lėšos | — |
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
| `dal_reg_busena` | `"Panaikintas"` | — | — | Panaikintas | — |
| `dal_reg_busena` | `"Praradęs PKD statusą"` | — | — | Praradęs PKD statusą | — |
| `dal_reg_busena` | `"Registruotas"` | — | — | Registruotas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/pajamos.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/pajamos.csv#L4)
