---
type: Table
title: "IstaigosDuomenys — Istaigu_Duomenys"
description: "Spinta table datasets/gov/vaspvt/priemones/IstaigosDuomenys (57 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/priemones/IstaigosDuomenys"
tags: [gov, vaspvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/medicinos_iranga.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_iranga.csv#L189"
    last_modified: "2026-11-11T14:39:20Z"
---

# IstaigosDuomenys — Istaigu_Duomenys

- **Model:** `datasets/gov/vaspvt/priemones/IstaigosDuomenys`[^manifest]
- **Dataset:** [Sveikatos priežiūros technologijų, susijusių su medicinos prietaisais, vertinimo ir valdymo duomenys](../priemones.md) (`datasets/gov/vaspvt/priemones`)
- **Manifest CSV:** [datasets/gov/vaspvt/medicinos_iranga.csv#L189](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_iranga.csv#L189)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/priemones/IstaigosDuomenys`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `2` | `open` | — | Juridinio Asmens Kodas | — |
| `ja_kodas` | `string` | — | `2` | `open` | — | Juridinio Asmens Kodas | — |
| `istaigos_pavadinimas` | `string` | — | `4` | `open` | — | Įstaigos Pavadinimas | — |
| `teisine_forma` | `string` | — | `4` | `open` | — | Teisinė Forma | — |
| `adresas` | `string` | — | `2` | `open` | — | Buveinės Adresas | — |
| `tel_nr` | `string` | — | `4` | `open` | — | Telefono Nr. | — |
| `faksas` | `string` | — | `4` | `open` | — | Faksas | — |
| `tipas` | `string` | — | `4` | `open` | — | Įstaigos Tipas | — |
| `busena` | `string` | — | `4` | `open` | — | Įstaigos Būsena | — |
| `savivaldybe` | `string` | — | `3` | `open` | — | Savivaldybė | — |
| `apskritis` | `string` | — | `3` | `open` | — | Apskritis | — |
| `priemones_nr` | `string` | — | `4` | `open` | — | Priemonės Nr. | — |
| `priemones_rusis` | `string` | — | `4` | `open` | — | Priemonės Rūšis | — |
| `filialas` | `string` | — | `1` | `open` | — | Naudojimo Vieta (Filialas) | — |
| `skyrius` | `string` | — | `2` | `open` | — | Naudojimo Vieta (Skyrius) | — |
| `kabinetas` | `string` | — | `1` | `open` | — | Naudojimo Vieta (Kabinetas) | — |
| `priemones_pavadinimas` | `string` | — | `2` | `open` | — | Priemonės Pavadinimas | — |
| `modelis` | `string` | — | `4` | `open` | — | Tipas/Modelis | — |
| `serijos_nr` | `string` | — | `4` | `open` | — | Serijos/Partijos Nr. | — |
| `gamintojo_pavadinimas` | `string` | — | `4` | `open` | — | Gamintojo Pavadinimas | — |
| `gamintojo_salies_kodas` | `string` | — | `2` | `open` | — | Gamintojo Šalies Kodas | — |
| `pagaminimo_data` | `date` | `D` | `4` | `open` | — | Pagaminimo Data | — |
| `isigijimo_data` | `date` | `D` | `4` | `open` | — | Įsigijimo Data | — |
| `naudojimo_pradzios_data` | `date` | `D` | `4` | `open` | — | Naudojimo Pradžios Data | — |
| `naudojimo_pabaigos_data` | `date` | `D` | `4` | `open` | — | Naudojimo Pabaigos Data | — |
| `priemones_busena` | `string` | — | `4` | `open` | — | Priemonės Būsena | — |
| `busenos_data` | `date` | `D` | `4` | `open` | — | Būsenos Data | — |
| `aprobavimo_dokumento_nr` | `string` | — | `4` | `open` | — | Aprobavimo Dokumento Nr. | — |
| `ce_numeris` | `string` | — | `4` | `open` | — | Ce Numeris | — |
| `paskelbtosios_istaigos_nr` | `string` | — | `4` | `open` | — | Paskelbtosios Įstaigos Nr. | — |
| `kaina_su_priedais` | `number` | — | `4` | `open` | — | Priemonės Įsigijimo Kaina Su Priedais | — |
| `kaina_be_priedu` | `number` | — | `4` | `open` | — | Priemonės Įsigijimo Kaina Be Priedų | — |
| `paskutines_technines_bukles_tikrinimo_data` | `date` | `D` | `4` | `open` | — | Paskutinės Techninės Būklės Tikrinimo Data | — |
| `planuojamos_technines_bukles_tikrinimo_data` | `date` | `D` | `4` | `open` | — | Planuojamos Techninės Būklės Tikrinimo Data | — |
| `pastabos` | `string` | — | `4` | `open` | — | Pastabos | — |
| `ang_tipas` | `string` | — | `4` | `open` | — | Techninė Charakteristika (Ang): Tipas | — |
| `ang_injektoriaus_tipas` | `string` | — | `4` | `open` | — | Techninė Charakteristika (Ang): Injektoriaus Tipas | — |
| `ang_naudojimo_sritys` | `string` | — | `4` | `open` | — | Techninė Charakteristika (Ang): Naudojimo Sritys | — |
| `rentgeno_tipas` | `string` | — | `2` | `open` | — | Techninė Charakteristika (Rtg): Tipas (1) | — |
| `ultragarso_tipas` | `string` | — | `2` | `open` | — | Techninė Charakteristika (Ug): Tipas(1) | — |
| `ug_vaizdo_rezimas` | `string` | — | `2` | `open` | — | Techninė Charakteristika (Ug): Vaizdo Režimas | — |
| `ug_doplerio_rezimas` | `string` | — | — | `open` | — | Techninė Charakteristika (Ug): Doplerio Režimas | — |
| `gama_kameros_tipas` | `string` | — | `4` | `open` | — | Techninė Charakteristika (Gk): Tipas | — |
| `gk_detektoriu_sk` | `integer` | `U` | `4` | `open` | — | Techninė Charakteristika (Gk): Detektorių Skaičius | — |
| `kompiuterinio_tomografo_tipas` | `string` | — | `4` | `open` | — | Techninė Charakteristika (Kt): Tipas | — |
| `kt_sluoksniu_skaicius` | `integer` | `U` | `4` | `open` | — | Techninė Charakteristika (Kt): Sluoksnių Skaičius | — |
| `kt_injektoriaus_tipas` | `string` | — | `4` | `open` | — | Techninė Charakteristika (Kt): Injektoriaus Tipas | — |
| `linijinis_greitintuvas` | `integer` | `eV` | `4` | `open` | — | Linijinis greitintuvas Kinetinė Energija (Elektronvoltai) | — |
| `mr_tomografo_tipas` | `string` | — | `2` | `open` | — | Techninė Charakteristika (Mrt): Tipas(1) | — |
| `mrt_lauko_stiprumas` | `number` | — | `2` | `open` | — | Techninė Charakteristika (Mrt): Magnetinio Lauko Stiprumas | — |
| `mrt_injektoriaus_tipas` | `string` | — | `4` | `open` | — | Techninė Charakteristika (Mrt): Injektoriaus Tipas | — |
| `momografo_tipas` | `string` | — | `2` | `open` | — | Techninė Charakteristika (Mmg): Tipas(1) | — |
| `pet_tipas` | `string` | — | `2` | `open` | — | Techninė Charakteristika (Pet): Tipas | — |
| `pet_kt_sluoksniu_skaicius` | `integer` | — | `2` | `open` | — | Techninė Charakteristika (Pet): Kt Sluoksnių Skaičius | — |
| `pet_injektoriu_tipas` | `string` | — | `2` | `open` | — | Techninė Charakteristika (Pet): Injektoriaus Tipas | — |
| `pet_kt_tipas` | `string` | — | `2` | `open` | — | Techninė Charakteristika (Pet): Kt Tipas | — |
| `pet_mrt_mag_lauko_stiprumas` | `string` | — | `2` | `open` | — | Techninė Charakteristika (Pet): Mrt Magnetinio Lauko Stiprumas (Tesla) | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `teisine_forma` | `"1"` | — | — | Viešoji Įstaiga | — |
| `teisine_forma` | `"2"` | — | — | Uždaroji Akcinė Bendrovė | — |
| `teisine_forma` | `"3"` | — | — | Viešosios Įstaigos Filialas | — |
| `teisine_forma` | `"4"` | — | — | Individuali Įmonė | — |
| `teisine_forma` | `"5"` | — | — | Biudžetinė Įstaiga | — |
| `teisine_forma` | `"6"` | — | — | Akcinė Bendrovė | — |
| `teisine_forma` | `"7"` | — | — | Mažoji Bendrija | — |
| `teisine_forma` | `"8"` | — | — | Biudžetinės Įstaigos Filialas | — |
| `teisine_forma` | `"9"` | — | — | Uždarosios Akcinės Bendrovės Filialas | — |
| `teisine_forma` | `"10"` | — | — | Asociacija | — |
| `tipas` | `"1"` | — | — | Universitetinė Ligoninė | — |
| `tipas` | `"2"` | — | — | Poliklinika | — |
| `tipas` | `"3"` | — | — | Rajono Ligoninė | — |
| `tipas` | `"4"` | — | — | Respublikinė Ligoninė | — |
| `tipas` | `"5"` | — | — | Kitos Ligoninės | — |
| `tipas` | `"6"` | — | — | Regioninė Ligoninė | — |
| `tipas` | `"7"` | — | — | Sveikatos Priežiūros Centras | — |
| `tipas` | `"8"` | — | — | Ambulatorija | — |
| `tipas` | `"9"` | — | — | Palaikomojo Gydymo Ir/Ar Slaugos | — |
| `tipas` | `"10"` | — | — | Fizinės Medicinos Ir/Ar Reabilitacijos | — |
| `tipas` | `"11"` | — | — | Draugija | — |
| `tipas` | `"12"` | — | — | Psichikos Sveikatos Centras | — |
| `busena` | `"1"` | — | — | Teisinis Statusas Neįregistruotas | — |
| `busena` | `"2"` | — | — | Išregistruotas | — |
| `busena` | `"3"` | — | — | Pašalintas | — |
| `busena` | `"4"` | — | — | Likviduojamas | — |
| `busena` | `"5"` | — | — | Inicijuojamas Likvidavimas | — |
| `busena` | `"6"` | — | — | Dalyvaujantis Reorganizavime | — |
| `priemones_rusis` | `"1"` | — | — | Diagnostinis Ultragarsinis Prietaisas | — |
| `priemones_rusis` | `"2"` | — | — | Diagnostinė Rentgeno Įranga | — |
| `priemones_rusis` | `"3"` | — | — | Kompiuterinis Tomografas | — |
| `priemones_rusis` | `"4"` | — | — | Mamografas | — |
| `priemones_rusis` | `"5"` | — | — | Magnetinio Rezonanso Tomografas | — |
| `priemones_rusis` | `"6"` | — | — | Angiografas | — |
| `priemones_rusis` | `"7"` | — | — | Linijinis Greitintuvas | — |
| `priemones_rusis` | `"8"` | — | — | Gama Kamera | — |
| `priemones_rusis` | `"9"` | — | — | Pozitronų Emisijos Tomografas | — |
| `priemones_busena` | `"1"` | — | — | Naudojamas | — |
| `priemones_busena` | `"2"` | — | — | Panaikinta | — |
| `priemones_busena` | `"3"` | — | — | Nurašytas | — |
| `priemones_busena` | `"4"` | — | — | Laikinai Nenaudojamas | — |
| `ce_numeris` | `"1"` | — | — | Turi Ce Numerį | — |
| `ce_numeris` | `"2"` | — | — | Neturi Ce Numerio | — |
| `ang_tipas` | `"Stacionarus"` | — | — | Stacionarus | — |
| `ang_tipas` | `"Mobilus"` | — | — | Mobilus | — |
| `ang_injektoriaus_tipas` | `"Automatinis"` | — | — | Automatinis | — |
| `ang_injektoriaus_tipas` | `"Be injektoriaus"` | — | — | Be injektoriaus | — |
| `ang_naudojimo_sritys` | `"Gydymas ir diagnostika"` | — | — | Gydymas Ir Diagnostika | — |
| `ang_naudojimo_sritys` | `"Diagnostika"` | — | — | Diagnostika | — |
| `ang_naudojimo_sritys` | `"Gydymas"` | — | — | Gydymas | — |
| `ug_doplerio_rezimas` | `"Yra"` | — | — | Turi Doplerį | — |
| `ug_doplerio_rezimas` | `"Nėra"` | — | — | Neturi Doplerio | — |
| `gama_kameros_tipas` | `"1"` | — | — | Kompiuterinis tomografas (SPECT) | Vieno fotono emisijos tomografijos sistema |
| `gama_kameros_tipas` | `"2"` | — | — | Kompiuterinis tomografas (SPECT/CT) | Vieno fotono emisijos tomografijos sistema su kompiuterinės tomografijos moduliu |
| `kompiuterinio_tomografo_tipas` | `"Stacionarus"` | — | — | Stacionarus | — |
| `kompiuterinio_tomografo_tipas` | `"Mobilus"` | — | — | Mobilus | — |
| `kompiuterinio_tomografo_tipas` | `"Tūrinis"` | — | — | Tūrinis | — |
| `kt_injektoriaus_tipas` | `"1"` | — | — | Automatinis | — |
| `kt_injektoriaus_tipas` | `"2"` | — | — | Be Injektoriaus | — |
| `kt_injektoriaus_tipas` | `"3"` | — | — | Kita: Su Injektoriumi | — |
| `kt_injektoriaus_tipas` | `"4"` | — | — | Kita: Dviejų Židinių | Besisukančio Anodo Rentgeno Vamzdis,Sukonstruotas Optimaliam Aušinimui, Taikoma Daugiapjūvio Ir Skenavimo Atvejais |
| `kt_injektoriaus_tipas` | `"5"` | — | — | Neautomatinis | — |
| `mrt_injektoriaus_tipas` | `"Automatinis"` | — | — | Automatinis | — |
| `mrt_injektoriaus_tipas` | `"Be injektoriaus"` | — | — | Be Injektoriaus | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo", ref: "ja_kodas")` | `base` | `4` | `open` | — | — | — |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `apskritis` | `create(property: "apskritis", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Apskritis")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/medicinos_iranga.csv
