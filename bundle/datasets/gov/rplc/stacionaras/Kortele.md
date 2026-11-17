---
type: Table
title: "Kortele — Pateikiami Respublikinio Priklausomybės Ligų Centro Vilniaus filialo stacionaro skyriuose gydytų pacientų duomenys nuo 2016m. Duomenys apima pacientų demografinę (gyvenamoji vieta..."
description: "Spinta table datasets/gov/rplc/stacionaras/Kortele (16 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rplc/stacionaras/Kortele"
tags: [gov, rplc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rplc/stacionaro_apsilankymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rplc/stacionaro_apsilankymai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Kortele — Pateikiami Respublikinio Priklausomybės Ligų Centro Vilniaus filialo stacionaro skyriuose gydytų pacientų duomenys nuo 2016m. Duomenys apima pacientų demografinę (gyvenamoji vieta...

- **Model:** `datasets/gov/rplc/stacionaras/Kortele`[^manifest]
- **Dataset:** [datasets/gov/rplc/stacionaras](../stacionaras.md) (`datasets/gov/rplc/stacionaras`)
- **Manifest CSV:** [datasets/gov/rplc/stacionaro_apsilankymai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rplc/stacionaro_apsilankymai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rplc/stacionaras/Kortele`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `skyrius` | `string` | — | `4` | `open` | — | Vilniaus Filialo (VF) skyrius iš kurio pateikti duomenys: VF SPRS – Stacionarinės psichosocialininės reabilitacijos skyrius (Motyvacinės terapijos); VF AAGS – Alkoholinės abstinencijos gydymo skyrius; VF NAGS – Narkotinės abstinencijos gydymo skyrius; VF PGS – Psichosocialinio gydymo skyrius (Minesota); VF VJRS – Vaikų ir jaunimo reabilitacijos skyrius. | — |
| `ataskaitiniai_metai` | `date` | `D` | `4` | `open` | — | Metai, už kuriuos pateikta ataskaita. | — |
| `pacientas` | `string` | — | `4` | `open` | — | Paciento žyma | — |
| `lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `gimimo_metai_gr` | `string` | — | `4` | `open` | — | Paciento gimimo metų grupė. | — |
| `amzius_gr` | `string` | — | `4` | `open` | — | Paciento amžiaus grupė. | — |
| `gyvenamoji_vieta` | `string` | — | `4` | `open` | — | Paciento gyvenamoji vieta. Jei pacientas kilęs ne iš Vilniaus miesto, nurodoma jo gyvenamosios vietos apskritis. Jei pacientas gyvena ne Lietuvoje - nurodoma užsienis. | — |
| `issilavinimas` | `string` | — | `4` | `open` | — | Paciento išsilavinimas | — |
| `sveikatos_draudimas` | `boolean` | — | `4` | `open` | — | Nuoroda, ar pacientas turi sveikatos draudimą | — |
| `uzimtumas` | `string` | — | `4` | `open` | — | Paciento užimtumo statusas | — |
| `sutrikimas` | `string` | — | `4` | `open` | — | Sutrikimai, klasifikuojami pagal TLK sisteminį ligų sąrašą | — |
| `vizitas` | `string` | — | `4` | `open` | — | Paciento vizito tipas | — |
| `taikytas_gydymas` | `string` | — | `4` | `open` | — | Pacientui taikytas gydymo tipas | — |
| `israsytas` | `string` | — | `4` | `open` | — | Informacija apie paciento išrašymą po taikyto gydymo. | — |
| `israsyto_paciento_bukle` | `string` | — | `4` | `open` | — | Paciento būklė po išrašymo | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `skyrius` | `"Alkoholinės abstinencijos gydymo skyrius"` | — | — | — | — |
| `skyrius` | `"Psichosocialinio gydymo skyrius (Minesota)"` | — | — | — | — |
| `skyrius` | `"Narkotinės abstinencijos gydymo skyrius"` | — | — | — | — |
| `skyrius` | `"Stacionarinės psichosocialininės reabilitacijos skyrius (Motyvacinės terapijos)"` | — | — | — | — |
| `skyrius` | `"Vaikų ir jaunimo reabilitacijos skyrius"` | — | — | — | — |
| `lytis` | `"vyras"` | — | — | — | — |
| `lytis` | `"moteris"` | — | — | — | — |
| `gyvenamoji_vieta` | `"Vilniaus miestas"` | — | — | — | — |
| `gyvenamoji_vieta` | `"Vilniaus apskritis"` | — | — | — | — |
| `gyvenamoji_vieta` | `"Utenos apskritis"` | — | — | — | — |
| `gyvenamoji_vieta` | `"Alytaus apskritis"` | — | — | — | — |
| `gyvenamoji_vieta` | `"Kauno apskritis"` | — | — | — | — |
| `gyvenamoji_vieta` | `"Panevėžio apskritis"` | — | — | — | — |
| `gyvenamoji_vieta` | `"Šiaulių apskritis"` | — | — | — | — |
| `gyvenamoji_vieta` | `"Marijampolės apskritis"` | — | — | — | — |
| `gyvenamoji_vieta` | `"Klaipėdos apskritis"` | — | — | — | — |
| `gyvenamoji_vieta` | `"Tauragės apskritis"` | — | — | — | — |
| `gyvenamoji_vieta` | `"Telšių apskritis"` | — | — | — | — |
| `gyvenamoji_vieta` | `"užsienis"` | — | — | — | — |
| `vizitas` | `"pirminis"` | — | — | — | — |
| `vizitas` | `"pakartotinis"` | — | — | — | — |
| `taikytas_gydymas` | `"medikamentinis abstinencijos gydymas"` | — | — | — | — |
| `taikytas_gydymas` | `"nemedikamentinis gydymas"` | — | — | — | — |
| `taikytas_gydymas` | `"kita"` | — | — | — | — |
| `taikytas_gydymas` | `"atkryčio gydymas"` | — | — | — | — |
| `israsytas` | `"perkeltas į psichosocialinio profilio stacionarinius skyrius RPLC"` | — | — | — | Pacientas perkeltas į Psichosocialinio gydymo (Minesotos) ar Psichosocialinės reabilitacijos skyrių |
| `israsytas` | `"iškeltas į kitas stacionarines asmens sveikatos priežiūros, reabilitacijos įstaigas"` | — | — | — | Pacientas perkeltas į kitas reabilitacines įstaigas |
| `israsyto_paciento_bukle` | `"sėkmingai baigė gydymą"` | — | — | — | Pacientas baigė gydymo kursą arba būklė pagerėjo esant neryškiems abstinencijos reiškiniams |
| `israsyto_paciento_bukle` | `"nesėkmingai baigė gydymą"` | — | — | — | Pacientas išrašytas be pakitimų (nutraukė gydymą) arba išrašytas už režimo pažeidimus. |

[^manifest]: atviriduomenys/manifest — datasets/gov/rplc/stacionaro_apsilankymai.csv
