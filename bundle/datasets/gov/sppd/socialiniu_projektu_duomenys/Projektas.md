---
type: Table
title: "Projektas — Organizacijų bei socialinių projektų duomenys"
description: "Lentelėse pateikti Socialinių priežiūros paslaugų departamento projektų, priemonių projektams įgyvendinti bei projektų išlaidų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/sppd/socialiniu_projektu_duomenys/Projektas"
tags: [gov, sppd, projektas, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2908/"
    title: "data.gov.lt DCAT-AP — datasets/gov/sppd/socialiniu_projektu_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Projektas — Organizacijų bei socialinių projektų duomenys

**Dataset Context:** Lentelėse pateikti Socialinių priežiūros paslaugų departamento projektų, priemonių projektams įgyvendinti bei projektų išlaidų duomenys. Projektų duomenys pateikiami nuo momento, kai paraiškos tampa aktualios tikrinimo procesui. Projektų išlaidų duomenys yra klasifikuojami pagal Lietuvos Respublikos valstybės ir savivaldybių biudžetų pajamų ir išlaidų klasifikatorių. Rinkinys sudarytas Valstybės duomenų agentūros. Projektų lentelės viena eilutė atitinka vieną paraišką, teiktą institucijos priemonės lėšoms gauti, priemonių lentelės – tam tikrą priemonę, skirtą projektui įgyvendinti, o projektų išlaidų lentelės – pinigų išleidimo faktą, susijusį su projektu. Atkreipiame dėmesį, kad duomenų eilutės yra nuolatos pildomos, o informacija jose yra tikslinama. Taip pat pažymime, kad įstaiga išlaidų duomenis suveda kas ketvirtį, todėl paskutinio mokėjimo data gali neatitikti realios paskutinio mokėjimo datos. Duomenys apima visoje Lietuvoje išsidėsčiusias organizacijas. Duomenų laiko aprėptis – nuo 2019 m. sausio 1d. Duomenų teikėjas – Socialinių priežiūros paslaugų departamentas prie Socialinės apsaugos ir darbo ministerijos. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/sppd/socialiniu_projektu_duomenys/Projektas`[^manifest]
- **Dataset:** [Socialinių projektu duomenys](../socialiniu_projektu_duomenys.md) (`datasets/gov/sppd/socialiniu_projektu_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sppd/socialiniu_projektu_duomenys/Projektas` (`deployed`)[^manifest]
- **Provider:** `sppd` — Socialinių paslaugų priežiūros departamentas prie SADM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sppd/socialiniu_projektu_duomenys.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/sppd/socialiniu_projektu_duomenys (https://data.gov.lt/datasets/2908/)
