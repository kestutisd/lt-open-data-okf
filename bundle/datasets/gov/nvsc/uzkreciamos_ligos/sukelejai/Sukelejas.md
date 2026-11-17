---
type: Table
title: "Sukelejas — Užkrečiamųjų ligų sukelėjai"
description: "Spinta table datasets/gov/nvsc/uzkreciamos_ligos/sukelejai/Sukelejas (61 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nvsc/uzkreciamos_ligos/sukelejai/Sukelejas"
tags: [gov, nvsc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nvsc/uzkreciamos_ligos/sukelejai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvsc/uzkreciamos_ligos/sukelejai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sukelejas — Užkrečiamųjų ligų sukelėjai

- **Model:** `datasets/gov/nvsc/uzkreciamos_ligos/sukelejai/Sukelejas`[^manifest]
- **Dataset:** [Nacionalinio visuomenės sveikatos centro užkrečiamų ligų sukelėjų duomenys](../sukelejai.md) (`datasets/gov/nvsc/uzkreciamos_ligos/sukelejai`)
- **Manifest CSV:** [datasets/gov/nvsc/uzkreciamos_ligos/sukelejai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvsc/uzkreciamos_ligos/sukelejai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nvsc/uzkreciamos_ligos/sukelejai/Sukelejas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `centras` | `string` | — | `2` | `open` | — | NVSC departamenas | — |
| `tlk` | `ref` | [/datasets/gov/vlk/tlk10am/Tlk10am[code]](../../../vlk/tlk10am/Tlk10am.md) | `4` | `open` | — | Diagnozės kodas | — |
| `diagnoze` | `string` | — | `4` | `open` | — | Diagnozės pavadinimas | — |
| `suk_seima_gentis` | `string` | — | `2` | `open` | — | Sukelėjo šeima, gentis | — |
| `suk_pavadinimas` | `string` | — | `2` | `open` | — | Sukelėjo pavadinimas | — |
| `suk_porusis` | `string` | — | `2` | `open` | — | Sukelėjo porūšis | — |
| `suk_serogrupe` | `string` | — | `2` | `open` | — | Sukelėjo serogrupė | — |
| `suk_serotipas` | `string` | — | `2` | `open` | — | Sukelėjo serotipas | — |
| `suk_kalicinotipas` | `string` | — | `2` | `open` | — | Sukelėjo kalcinotipas | — |
| `suk_biotipas` | `string` | — | `2` | `open` | — | Sukelėjo biotipas | — |
| `suk_fagotipas` | `string` | — | `2` | `open` | — | Sugelėjo fagotipas | — |
| `suk_toksino_tipas` | `string` | — | `2` | `open` | — | Sukelėjo toksino tipas | — |
| `suk_anti_o` | `string` | — | `2` | `open` | — | Sukelėjo antigenas O | — |
| `suk_anti_h` | `string` | — | `2` | `open` | — | Sukelėjo antigenas H | — |
| `suk_v_genas` | `string` | — | `2` | `open` | — | Sukelėjo virulentiškumo genas | — |
| `gydymas` | `string` | — | `4` | `open` | — | Paciento gydymas | Požymis, ar pacientas gydomas ambulatoriškai ar stacionariai |
| `paciento_tyrimo_priezastis` | `string` | — | `4` | `open` | — | Paciento tyrimo priežastis | Požymis, ar pacientas tiriamas pagal epidemiologinę būtinybę, dėl sąlyčio su sergančiu asmeniu, ar dėl kitų priežasčių |
| `meginio_tyrimo_priezastis` | `string` | — | `2` | `open` | — | Mėginio tyrimo priežastis | Požymis nurodantis, ar mėginys tirtas vykdant kontrolę, stebėseną, dėl kitų priežasčių |
| `pgr` | `boolean` | — | `4` | `open` | — | PGR tyrimas | Požymis, ar atliktas PGR tyrimas |
| `tif` | `boolean` | — | `4` | `open` | — | Tiesioginės imunoflorescencijos tyrimas | Požymis, ar atliktas tiesioginės imunofluorescencijos tyrimas |
| `ifa_elisa` | `boolean` | — | `4` | `open` | — | Imunofermentinė analizė | Požymis, nurodantis, ar buvo atlikti imunofermentinės analizės tyrimai |
| `imunoblotas` | `boolean` | — | `4` | `open` | — | Imunoblotas | Požymis, nurodantis, ar buvo atliktas imunobloto tyrimas |
| `mikroskopija` | `boolean` | — | `4` | `open` | — | Mikroskopiniai tyrimai | Požymis, ar buvo atlikti mikroskopiniai tyrimai |
| `nif` | `boolean` | — | `4` | `open` | — | Netiesioginės imunoflorescencijos tyrimas | Požymis, ar buvo atliktas netiesioginės imunofluorescencijos tyrimas |
| `netiesiogine_hemogliutinacija` | `boolean` | — | `4` | `open` | — | Hemagliutinacijos tyrimas | Požymis, ar buvo atliktas netiesioginės hemagliutinacijos tyrimas |
| `kiti` | `boolean` | — | `4` | `open` | — | Kiti tyrimai | Požymis, ar buvo atlikti kiti nei anksčiau paminėti tyrimai |
| `isaugintas_is_klinikinio_ban` | `boolean` | — | `4` | `open` | — | Klinikinis bandinys | Požymis, ar sukelėjo kultūra išauginta iš klinikinio bandinio |
| `meginys_kraujas` | `boolean` | — | `4` | `open` | — | Klinikinis bandinys - kraujas | Požymis nurodantis ar sukelėjo kultūra išauginta iš kraujo mėginio |
| `meginys_likvoras` | `boolean` | — | `4` | `open` | — | Klinikinis bandinys - smegenų skystis | Požymis nurodantis ar sukelėjo kultūra išauginta iš smegenų skysčio mėginio |
| `meginys_skranzio_turinys` | `boolean` | — | `4` | `open` | — | Klinikinis bandinys - skrandžio turinys | Požymis nurodantis ar sukelėjo kultūra išauginta iš skrandžio turinio mėginio |
| `meginys_fekalijos` | `boolean` | — | `4` | `open` | — | Klinikinis bandinys - fekalijos | Požymis nurodantis ar sukelėjo kultūra išauginta iš fekalijų mėginio |
| `meginys_slapimas` | `boolean` | — | `4` | `open` | — | Klinikinis bandinys - šlapimas | Požymis nurodantis ar sukelėjo kultūra išauginta iš šlapimo mėginio |
| `meginys_zaizda` | `boolean` | — | `4` | `open` | — | Klinikinis bandinys - žaizda | Požymis nurodantis ar sukelėjo kultūra išauginta iš žaizdos mėginio |
| `meginys_ausu_isskyros` | `boolean` | — | `4` | `open` | — | Klinikinis bandinys - ausų išskyros | Požymis nurodantis ar sukelėjo kultūra išauginta iš ausų išskyrų mėginio |
| `meginys_akiu_isskyros` | `boolean` | — | `4` | `open` | — | Klinikinis bandinys - akių išskyros | Požymis nurodantis ar sukelėjo kultūra išauginta iš akių išskyrų mėginio |
| `meginys_patanatomine_med` | `boolean` | — | `4` | `open` | — | Klinikinis bandinys - patanatominis | Požymis nurodantis ar sukelėjo kultūra patanatominio mėginio |
| `meginys_sinusu_punktas` | `boolean` | — | `4` | `open` | — | Klinikinis bandinys - sinusai | Požymis nurodantis ar sukelėjo kultūra išauginta iš sinusų mėginio |
| `meginys_virs_kv_tak` | `boolean` | — | `4` | `open` | — | Klinikinis bandinys - viršutiniai kvėpavimo takai | Požymis nurodantis ar sukelėjo kultūra išauginta iš viršutinių kvėpavimo takų mėginio |
| `meginys_apat_kv_tak` | `boolean` | — | `4` | `open` | — | Klinikinis bandinys - apatiniai kvėpavimo takai | Požymis nurodantis ar sukelėjo kultūra išauginta iš apatinių kvėpavimo takų mėginio |
| `meginys_lyties_organai` | `boolean` | — | `4` | `open` | — | Klinikinis bandinys - lytiniai organai | Požymis nurodantis ar sukelėjo kultūra išauginta iš lytinių organų mėginio |
| `meginys_kiti` | `boolean` | — | `4` | `open` | — | Klinikinis bandinys - kiti | Požymis nurodantis ar sukelėjo kultūra išauginta iš kitų klinikinių mėginių |
| `isaugintas_is_aplinkos_ban` | `boolean` | — | `4` | `open` | — | Aplinkos bandinys | Požymis, ar sukelėjo kultūra išauginta iš aplinkos bandinio |
| `meginys_zalia_mesa` | `boolean` | — | `4` | `open` | — | Aplinkos bandinys - žalia mėsa | Požymis nurodantis ar sukelėjo kultūra išauginta iš žalios mėsos mėginio |
| `meginys_pieno_produktai` | `boolean` | — | `4` | `open` | — | Aplinkos bandinys - pieno produktai | Požymis nurodantis ar sukelėjo kultūra išauginta iš pieno produktų mėginio |
| `meginys_kulinarijos_gaminiai` | `boolean` | — | `4` | `open` | — | Aplinkos bandinys - kulinarijos produktai | Požymis nurodantis ar sukelėjo kultūra išauginta iš kulinarijos produktų mėginio |
| `meginys_maist_pr_vaikams` | `boolean` | — | `4` | `open` | — | Aplinkos bandinys - maisto produktai vaikams | Požymis nurodantis ar sukelėjo kultūra išauginta iš maisto produktų vaikams mėginio |
| `meginys_kreminiai_gaminiai` | `boolean` | — | `4` | `open` | — | Aplinkos bandinys - kreminiai gaminiai | Požymis nurodantis ar sukelėjo kultūra išauginta iš kreminių gaminių mėginio |
| `meginys_kaiusiniu_gaminiai` | `boolean` | — | `4` | `open` | — | Aplinkos bandinys - kiaušinių gaminiai | Požymis nurodantis ar sukelėjo kultūra išauginta iš kiaušinių gaminių mėginio |
| `meginys_geriamas_vanduo` | `boolean` | — | `4` | `open` | — | Aplinkos bandinys - geriamasis vanduo | Požymis nurodantis ar sukelėjo kultūra išauginta iš geriamojo vandens mėginio |
| `meginys_atviras_vandens_telk` | `boolean` | — | `4` | `open` | — | Aplinkos bandinys - atviras vandens telkinys | Požymis nurodantis ar sukelėjo kultūra išauginta iš atviro vandens telkinio mėginio |
| `meginys_baseinas` | `boolean` | — | `4` | `open` | — | Aplinkos bandinys - baseino vanduo | Požymis nurodantis ar sukelėjo kultūra išauginta iš baseino mėginio |
| `meginys_plovinys` | `boolean` | — | `4` | `open` | — | Aplinkos bandinys - ploviniai | Požymis nurodantis ar sukelėjo kultūra išauginta iš plovinių mėginio |
| `meginys_nuotekos` | `boolean` | — | `4` | `open` | — | Aplinkos bandinys - nuotekos | Požymis nurodantis ar sukelėjo kultūra išauginta iš nuotekų mėginio |
| `meginys_kiti_produktai` | `boolean` | — | `4` | `open` | — | Aplinkos bandinys - kiti | Požymis nurodantis ar sukelėjo kultūra išauginta iš kitų aplinkos mėginių |
| `jautrumas_antibiotikams` | `boolean` | — | `4` | `open` | — | Jautrumas antibiotikams | Požymis, ar nustatytas sukelėjo jautrumas antibiotikams |
| `antibiotics_jautrus` | `string` | — | `2` | `open` | — | Jautrūs antibiotikai | Antibiotiko tarptautinis nepatentuojamas pavadinimas, kuriam sukelėjas yra jautrus |
| `antibiotics_mjautrus` | `string` | — | `2` | `open` | — | Mažai jautrūs antibiotikai | Antibiotiko tarptautinis nepatentuojamas pavadinimas, kuriam sukelėjas yra mažai jautrus |
| `antibiotics_atsparus` | `string` | — | `2` | `open` | — | Atsparūs antibiotikai | Antibiotiko tarptautinis nepatentuojamas pavadinimas, kuriam sukelėjas yra atsparus |
| `eminio_paemimas` | `date` | `M` | `4` | `open` | — | Mėginio paėmimo data | — |
| `atvejai` | `integer` | `U` | `4` | `open` | — | Atvejų skaičius | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `gydymas` | `"Stacionarinis"` | — | — | Pacientas gydomas stacionare | — |
| `gydymas` | `"Ambulatorinis"` | — | — | Pacientas gydomas ambulatoriškai | — |
| `paciento_tyrimo_priezastis` | `"Tiriamas dėl kitų priežasčių"` | — | — | Pacientas tiriamas dėl kitų priežasčių | — |
| `paciento_tyrimo_priezastis` | `"Tiriamas dėl sąlyčio"` | — | — | Pacientas tiriamas dėl sąlyčio | — |
| `paciento_tyrimo_priezastis` | `"Tiriamas pagal būtinybę"` | — | — | Pacientas tiriamas pagal būtinybę | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nvsc/uzkreciamos_ligos/sukelejai.csv
