---
type: Table
title: "Projektas — Organizacijų bei socialinių projektų duomenys"
description: "Spinta table datasets/gov/sppd/socialiniu_projektu_duomenys/Projektas (26 columns)."
resource: "https://get.data.gov.lt/datasets/gov/sppd/socialiniu_projektu_duomenys/Projektas"
tags: [gov, sppd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/sppd/socialiniu_projektu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Projektas — Organizacijų bei socialinių projektų duomenys

- **Model:** `datasets/gov/sppd/socialiniu_projektu_duomenys/Projektas`[^manifest]
- **Dataset:** [Socialinių projektu duomenys](../socialiniu_projektu_duomenys.md) (`datasets/gov/sppd/socialiniu_projektu_duomenys`)
- **Manifest CSV:** [datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sppd/socialiniu_projektu_duomenys/Projektas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus eilutės identifikatorius | — |
| `projekto_id` | `string` | — | `4` | `open` | — | Unikalus projekto identifikatorius | Projektui priskirta id reikšmė kuri unikaliai identifikuoja eilutę lentelėje. |
| `priemones_id` | `string` | — | `4` | `open` | — | Priemonės identifikatorius | Išorinis raktas į priemonės lentelę |
| `projekto_kodas` | `string` | — | `4` | `open` | — | Projekto kodas | Projekto kodas sudarytas iš priemonės trumpinio bei skaičiaus atitinkančio projektų eilės tvarką |
| `pareiskejas` | `string` | — | `4` | `open` | — | Organizacijos pavadinimas | Pareiškėjo įmonės, viešosios įstaigos, ar kitos organizacijos pavadinimas |
| `pareiskejo_tinklapis` | `string` | — | `4` | `open` | — | Tinklapio adresas | Pareiškėjo URL nuoroda į pareiškėjo internetinę svetainę |
| `pareiskejo_adresas` | `string` | — | `4` | `open` | — | Fizinis adresas | Pareiškėjo nurodytas organizacijos adresas |
| `pareiskejo_pasto_kodas` | `string` | — | `4` | `open` | — | Pašto kodas | Nurodyto adreso pašto kodas |
| `pasto_kodas` | `string` | — | `4` | `open` | — | Koordinačių pašto kodas | Pašto kodas išimtas iš nurodytų koordinačių |
| `gatve` | `string` | — | `4` | `open` | — | Koordinačių gatvės pavadinimas | Gatvės pavadinimas išimta iš nurodytų koordinačių |
| `savivaldybe` | `string` | — | `4` | `open` | — | Koordinačių savivaldybė | Savivaldybė išimta iš nurodytų koordinačių |
| `miestas` | `string` | — | `4` | `open` | — | Koordinačių miestas | Miestas išimtas iš nurodytų koordinačių |
| `lokacijos_tipas` | `string` | — | `4` | `open` | — | Koordinačių lokacijos tipas | Nurodo kokia yra koordinačių taško reikšmė |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | Koordinačių taškas | Organizacijos nurodyto adreso taško žemėlapyje, pagal WGS84 koordinačių formatą, WKT reikšmės representaciją |
| `geometrijos_balai` | `number` | — | `4` | `open` | — | Koordinačių teisingumo įvertinimas | Nurodyta reikšmė žymi koordinačių teisingumo procentą |
| `pareiskejo_veiklos_teritorija` | `string` | — | `4` | `open` | — | Pareiškėjo veiklos teritorija | Reikšmė nurodo vietą kurioje vykdo veiklą pareiškėjo organizacija |
| `pareiskejo_jar` | `string` | — | `4` | `open` | — | Juridinio asmens kodas | Organizacijos kodas pateiktas kodas kuris atitinka juridinio asmens kodą |
| `pareiskos_teikimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos teikimo data | Data kada buvo sukurtas įrašas SOPAS sistemoje |
| `vykdymo_pradzios_data` | `date` | `D` | `4` | `open` | — | Projekto pradžios data | Data kada buvo/bus pradėtas vykdyti projektas |
| `vykdymo_pabaigos_data` | `date` | `D` | `4` | `open` | — | Projekto pabaigos data | Data kada yra numatoma projekto pabaiga |
| `projekto_tikslas` | `string` | — | `4` | `open` | — | Projekto tikslas | Projekto metu siekiamas įgyvendinti uždavinys |
| `projekto_aprasymas` | `string` | — | `4` | `open` | — | Projekto aprašymas | Trumpas projekto aprašymas pateiktas projektui vykdyti pretenduojančios organizacijos |
| `projekto_busena` | `string` | — | `4` | `open` | — | Projekto būsena | — |
| `gauta_suma` | `number` | — | `4` | `open` | — | Gauta suma | Gauta suma projektui įgyvendinti |
| `isleista_suma` | `number` | — | `4` | `open` | — | Išleista suma | Viso projekto eigos metu išleista suma |
| `paskutinio_mokejimo_data` | `date` | `D` | `4` | `open` | — | Paskutinio mokėjimo data | Data kuomet buvo atliktas paskutinis mokėjimas |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `projekto_busena` | `"Tikrinimas"` | — | — | Tikrinimas | Projekto paraiška pateikta tikrinimui |
| `projekto_busena` | `"Nefinansuojamas "` | — | — | Nefinansuojamas | Projektas nebus finansuojamas dėl įvairių priežasčių |
| `projekto_busena` | `"Vertinimas"` | — | — | Vertinimas | Projekto anketa yra užpildyta ir duomenys yra vertinami |
| `projekto_busena` | `"Paraiškos dokumentų tikslinimas"` | — | — | Paraiškos dokumentų tikslinimas | — |
| `projekto_busena` | `"Paraiškos tikslinimas ekspertams"` | — | — | Paraiškos tikslinimas ekspertams | — |
| `projekto_busena` | `"Laukiantis rezerve"` | — | — | Laukiantis rezerve | Projekto anketa neperduota vykdymui, tačiau nėra atmesta |
| `projekto_busena` | `"Sąmatos pildymas"` | — | — | Sąmatos pildymas | Būsimų projekto išlaidų pildymas |
| `projekto_busena` | `"Sutarties ruošimas"` | — | — | Sutarties ruošimas | Projekto sutarties ruošimas |
| `projekto_busena` | `"Sąmatos tikslinimas"` | — | — | Sąmatos tikslinimas | Būsimų projekto išlaidų tikslinimas |
| `projekto_busena` | `"Pasirašymas"` | — | — | Pasirašymas | Projekto sutarties pasirašymas |
| `projekto_busena` | `"Vykdymas"` | — | — | Vykdymas | Projekto vykdymas |
| `projekto_busena` | `"Tvirtinimas"` | — | — | Tvirtinimas | Projekto pabaigimo būsenos tvirtinimas |
| `projekto_busena` | `"Sustabdytas"` | — | — | Sustabdytas | Projekto vykdymas yra sustabdytas |
| `projekto_busena` | `"Nutrauktas"` | — | — | Nutrauktas | Projekto vykdymas yra nutrauktas |
| `projekto_busena` | `"Pabaigtas"` | — | — | Pabaigtas | Projekto vykdymas yra pabaigtas |
| `projekto_busena` | `"Archyvas"` | — | — | Archyvas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gauta_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `isleista_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sppd/socialiniu_projektu_duomenys.csv
