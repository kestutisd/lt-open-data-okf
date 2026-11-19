---
type: Table
title: "IstaigosAtaskaituDuomenys — Istaigų Ataskaitų Duomenys"
description: "Spinta table datasets/gov/vaspvt/priemones/IstaigosAtaskaituDuomenys (72 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/priemones/IstaigosAtaskaituDuomenys"
tags: [gov, vaspvt, istaigosataskaituduomenys, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_iranga.csv#L58"
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/medicinos_iranga.csv#L58"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2310/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vaspvt/priemones"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# IstaigosAtaskaituDuomenys — Istaigų Ataskaitų Duomenys

- **Model:** `datasets/gov/vaspvt/priemones/IstaigosAtaskaituDuomenys`[^manifest]
- **Dataset:** [Sveikatos priežiūros technologijų, susijusių su medicinos prietaisais, vertinimo ir valdymo duomenys](../priemones.md) (`datasets/gov/vaspvt/priemones`)[^manifest]
- **Manifest CSV:** [datasets/gov/vaspvt/medicinos_iranga.csv#L58](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_iranga.csv#L58)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/priemones/IstaigosAtaskaituDuomenys` (`deployed`)[^manifest]
- **Provider:** `vaspvt` — Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA identifikatorius | — |
| `ja_kodas` | `string` | — | `2` | `open` | — | Juridinio Asmens Kodas | — |
| `istaiga` | `string` | — | `4` | `open` | — | Įstaigos Pavadinimas | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybė | — |
| `apskritis` | `string` | — | `2` | `open` | — | Apskritis | — |
| `rusis` | `string` | — | `4` | `open` | — | Ataskaitos Rūšis | — |
| `numeris` | `string` | — | `2` | `open` | — | Ataskaitos Numeris | — |
| `busena` | `string` | — | `4` | `open` | — | Ataskaitos Būsena | — |
| `filialas` | `string` | — | `2` | `open` | — | Filialo Pavadinimas | — |
| `data` | `date` | `D` | `4` | `open` | — | Ataskaitos Pateikimo Data | — |
| `ataskaitinis_laikotarpis_metai` | `string` | — | `2` | `open` | — | Ataskaitinis Laikotarpis(Metai) | — |
| `ataskaitinis_laikotarpis_pusmetis` | `string` | — | `4` | `open` | — | Ataskaitinis Laikotarpis(Pusmetis) | — |
| `ataskaitinis_laikotarpis_ketvirtis` | `string` | — | `4` | `open` | — | Ataskaitinis Laikotarpis(Ketvirtis) | — |
| `vieta` | `string` | — | `4` | `open` | — | Ataskaitos Sudarymo Vieta | — |
| `priemones_rusis` | `string` | — | `4` | `open` | — | Priemonės Rūšis | — |
| `priemones_numeris` | `string` | — | `4` | `open` | — | Priemonės Numeris | — |
| `modelis` | `string` | — | `4` | `open` | — | Priemonės Tipas/Modelis | — |
| `nr` | `string` | — | `4` | `open` | — | Priemonės Serijos/Partijos Nr. | — |
| `priemone` | `string` | — | `2` | `open` | — | Priemonės Pavadinimas | — |
| `naudojimo_skyrius` | `string` | — | `4` | `open` | — | Priemonės Naudojimo Vieta (Skyrius) | — |
| `naudojimo_kabinetas` | `string` | — | `4` | `open` | — | Priemonės Naudojimo Vieta (Kabinetas) | — |
| `gamintojas` | `string` | — | `4` | `open` | — | Priemonės Gamintojo Pavadinimas | — |
| `gamintojo_salis` | `string` | — | `2` | `open` | — | Priemonės Gamintojo Šalies Kodas | — |
| `pagaminimo_data` | `date` | `D` | `4` | `open` | — | Priemonės Pagaminimo Data | — |
| `isigijimo_data` | `date` | `D` | `4` | `open` | — | Priemonės Įsigijimo Data | — |
| `naudojimo_pradzia` | `date` | `D` | `4` | `open` | — | Priemonės Naudojimo Pradžios Data | — |
| `naudojimo_pabaiga` | `date` | `D` | `4` | `open` | — | Priemonės Naudojimo Pabaigos Data | — |
| `priemones_busena` | `string` | — | `4` | `open` | — | Priemonės Būsena | — |
| `busenos_data` | `date` | `D` | `4` | `open` | — | Būsenos Data | — |
| `aprobavimo_dokumento_nr` | `string` | — | `4` | `open` | — | Aprobavimo Dokumento Nr. | — |
| `ce_numeris` | `string` | — | `4` | `open` | — | Ce Numeris | — |
| `istaigos_nr` | `string` | — | `4` | `open` | — | Paskelbtosios Įstaigos Nr. | — |
| `darbo_val_ketv` | `number` | `U` | `4` | `open` | — | St-Mp Naudojimo (Darbo) Valandų Skaičius Per I Mėnesį | — |
| `proc_kiekis_ketv` | `number` | `U` | `4` | `open` | — | St-Mp Atliekamų Procedūrų/Tyrimų Skaičius Per I Mėnesį | — |
| `kaina_su_priedais` | `number` | — | `2` | `open` | — | Priemonės Įsigijimo Kaina Su Priedais | — |
| `kaina_be_priedu` | `number` | — | `2` | `open` | — | Priemonės Įsigijimo Kaina Be Priedų | — |
| `paskutines_technines_bukles_tikrinimas` | `date` | `D` | `4` | `open` | — | Paskutinės Techninės Būklės Tikrinimo Data | — |
| `planuojamos_technines_bukles_tikrinimas` | `date` | `D` | `4` | `open` | — | Planuojamos Techninės Būklės Tikrinimo Data | — |
| `pastabos` | `string` | — | `4` | `open` | — | Pastabos | — |
| `instaliavimo_kaina` | `number` | — | `4` | `open` | — | Priemonės Instaliavimo Kaina | — |
| `naudojimo_vidutines_menesio_islaidos` | `number` | — | `4` | `open` | — | Priemonės Naudojimo Vidutinės Mėnesio Išlaidos | — |
| `personalo_mokymai_kaina` | `number` | — | `4` | `open` | — | Priemonės Personalo Mokymai | — |
| `nusidevejimas` | `number` | — | `4` | `open` | — | Priemonės Sukauptas Nusidėvėjimas | — |
| `likutine_verte` | `number` | — | `4` | `open` | — | Priemonės Likutinė Vertė | — |
| `atsiperkamoji_verte` | `number` | — | `4` | `open` | — | Priemonės Atsiperkamoji Vertė | — |
| `gedimai` | `number` | `U` | `4` | `open` | — | St-Mp Prastovų Dėl Gedimo Skaičius Dienomis | — |
| `esminio_pagerinimo_pavadinimas` | `string` | — | `4` | `open` | — | Esminio Pagerinimo Pavadinimas | — |
| `esminio_pagerinimo_serijos_nr` | `string` | — | `4` | `open` | — | Esminio Pagerinimo Serijos Nr. | — |
| `esminio_pagerinimo_isigijimas` | `date` | `D` | `4` | `open` | — | Esminio Pagerinimo Įsigijimo Data | — |
| `pagerinimo_verte` | `number` | — | `4` | `open` | — | Esminio Pagerinimo Vertė | — |
| `ang_tipas` | `string` | — | `4` | `open` | — | Techninė Charakteristika (Ang): Tipas | — |
| `ang_injektoriaus_tipas` | `string` | — | `4` | `open` | — | Techninė Charakteristika (Ang): Injektoriaus Tipas | — |
| `ang_naudojimo_sritys` | `string` | — | `4` | `open` | — | Techninė Charakteristika (Ang): Naudojimo Sritys | — |
| `rentgeno_tipas` | `string` | — | `2` | `open` | — | Techninė Charakteristika (Rtg): Tipas (1) | — |
| `ultragarso_tipas` | `string` | — | `2` | `open` | — | Techninė Charakteristika (Ug): Tipas(1) | — |
| `ug_vaizdo_rezimas` | `string` | — | `2` | `open` | — | Techninė Charakteristika (Ug): Vaizdo Režimas | — |
| `ug_doplerio_rezimas` | `string` | — | `4` | `open` | — | Techninė Charakteristika (Ug): Doplerio Režimas | — |
| `gama_kameros_tipas` | `string` | — | `4` | `open` | — | Techninė Charakteristika (Gk): Tipas | — |
| `gk_detektoriu_sk` | `string` | — | `4` | `open` | — | Detektorių Skaičius | — |
| `kompiuterinio_tomografo_tipas` | `string` | — | `4` | `open` | — | Techninė Charakteristika (Kt): Tipas | — |
| `kt_sluoksniu_skaicius` | `integer` | `U` | `4` | `open` | — | Techninė Charakteristika (Kt): Sluoksnių Skaičius | — |
| `kt_injektoriaus_tipas` | `string` | — | `4` | `open` | — | Techninė Charakteristika (Kt): Injektoriaus Tipas | — |
| `linijinis_greitintuvas` | `integer` | `eV` | `4` | `open` | — | Linijinis greitintuvas Kinetinė Energija (Elektronvoltai) | — |
| `mr_tomografo_tipas` | `string` | — | `2` | `open` | — | Magnetinio rezonanso tomografo tipas | — |
| `mrt_lauko_stiprumas` | `number` | — | `2` | `open` | — | Techninė Charakteristika (Mrt): Magnetinio Lauko Stiprumas | — |
| `mrt_injektoriaus_tipas` | `string` | — | `4` | `open` | — | Techninė Charakteristika (Mrt): Injektoriaus Tipas | — |
| `momografo_tipas` | `string` | — | `2` | `open` | — | Techninė Charakteristika (Mmg): Tipas(1) | — |
| `pet_tipas` | `string` | — | `2` | `open` | — | Techninė Charakteristika (Pet): Tipas | — |
| `pet_kt_sluoksniu_skaicius` | `integer` | — | `2` | `open` | — | Techninė Charakteristika (Pet): Kt Sluoksnių Skaičius | — |
| `pet_injektoriu_tipas` | `string` | — | `2` | `open` | — | Techninė Charakteristika (Pet): Injektoriaus Tipas | — |
| `pet_kt_tipas` | `string` | — | `2` | `open` | — | Techninė Charakteristika (Pet): Kt Tipas | — |
| `pet_mrt_mag_lauko_stiprumas` | `string` | — | `2` | `open` | — | Techninė Charakteristika (Pet): Mrt Magnetinio Lauko Stiprumas (Tesla) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `rusis` | `"1"` | — | — | Darbo su medicinos priemonėmis ataskaita | — |
| `rusis` | `"2"` | — | — | Medicinos priemonių naudojimo išlaidų ataskaita | — |
| `busena` | `"1"` | — | — | Rengiama | — |
| `busena` | `"2"` | — | — | Pateikta | — |
| `busena` | `"3"` | — | — | Tikslinama | — |
| `busena` | `"4"` | — | — | Panaikinta | — |
| `ataskaitinis_laikotarpis_pusmetis` | `"I"` | — | — | Pirmasis Pusmetis | — |
| `ataskaitinis_laikotarpis_pusmetis` | `"II"` | — | — | Antrasis Pusmetis | — |
| `ataskaitinis_laikotarpis_ketvirtis` | `"I"` | — | — | Pirmasis Ketvirtis | — |
| `ataskaitinis_laikotarpis_ketvirtis` | `"II"` | — | — | Antrasis Ketvirtis | — |
| `ataskaitinis_laikotarpis_ketvirtis` | `"III"` | — | — | Trečiasis Ketvirtis | — |
| `ataskaitinis_laikotarpis_ketvirtis` | `"IV"` | — | — | Ketvirtasis Ketvirtis | — |
| `priemones_rusis` | `"1"` | — | — | Diagnostinis Ultragarsinis Prietaisas | — |
| `priemones_rusis` | `"2"` | — | — | Diagnostinė Rentgeno Įranga | — |
| `priemones_rusis` | `"3"` | — | — | Kompiuterinis Tomografas | — |
| `priemones_rusis` | `"4"` | — | — | Mamografas | — |
| `priemones_rusis` | `"5"` | — | — | Magnetinio Rezonanso Tomografas | — |
| `priemones_rusis` | `"6"` | — | — | Angiografas | — |
| `priemones_rusis` | `"7"` | — | — | Linijinis Greitintuvas | — |
| `priemones_rusis` | `"8"` | — | — | Gama Kamera | — |
| `priemones_rusis` | `"9"` | — | — | Pozitronų Emisijos Tomografas | — |
| `priemones_busena` | `"Naudojamas"` | — | — | Naudojamas | — |
| `priemones_busena` | `"Nurašytas"` | — | — | Nurašytas | — |
| `priemones_busena` | `"Laikinai nenaudojamas"` | — | — | Laikinai Nenaudojamas | — |
| `priemones_busena` | `"Panaikinta"` | — | — | Panaikinta | — |
| `ce_numeris` | `"TAIP"` | — | — | Numeris Yra | — |
| `ce_numeris` | `"NE"` | — | — | Numenio Nėra | — |
| `ang_tipas` | `"Stacionarus"` | — | — | Stacionarus | — |
| `ang_tipas` | `"Mobilus"` | — | — | Mobilus | — |
| `ang_injektoriaus_tipas` | `"Automatinis"` | — | — | Automatinis | — |
| `ang_injektoriaus_tipas` | `"Be injektoriaus"` | — | — | Be Injektoriaus | — |
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
| `kt_injektoriaus_tipas` | `"3"` | — | — | Su Injektoriumi | — |
| `kt_injektoriaus_tipas` | `"4"` | — | — | Dviejų Židinių | Besisukančio Anodo Rentgeno Vamzdis,Sukonstruotas Optimaliam Aušinimui, Taikoma Daugiapjūvio Ir Skenavimo Atvejais |
| `kt_injektoriaus_tipas` | `"5"` | — | — | Neautomatinis | — |
| `mr_tomografo_tipas` | `"1"` | — | — | Stacionarus / Uzdaras | — |
| `mr_tomografo_tipas` | `"2"` | — | — | Stacionarus / Atviras | — |
| `mr_tomografo_tipas` | `"3"` | — | — | Mobilus / Uzdaras | — |
| `mr_tomografo_tipas` | `"4"` | — | — | Stacionarus / Be injektoriaus | — |
| `mrt_injektoriaus_tipas` | `"Automatinis"` | — | — | Automatinis | — |
| `mrt_injektoriaus_tipas` | `"Be injektoriaus"` | — | — | Be Injektoriaus | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo", ref: "ja_kodas")` | `base` | `4` | `open` | — | — | — |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `apskritis` | `create(property: "apskritis", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Apskritis")` | `type` | `4` | `open` | — | — | — |
| `kaina_su_priedais` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `kaina_be_priedu` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/medicinos_iranga.csv#L58 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_iranga.csv#L58)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vaspvt/priemones (https://data.gov.lt/datasets/2310/)
