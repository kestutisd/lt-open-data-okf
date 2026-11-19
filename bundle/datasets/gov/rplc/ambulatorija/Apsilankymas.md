---
type: Table
title: "Apsilankymas — Pateikiami Respublikinio Priklausomybės Ligų Centro Vilniaus filialo ambulatorinių skyrių (dienos stacionaras priskiriamas prie amb. sk.) pacientų apsilankymų duomenys nuo 2016m. Duomenys apima pacientų demografinę..."
description: "Spinta table datasets/gov/rplc/ambulatorija/Apsilankymas (16 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rplc/ambulatorija/Apsilankymas"
tags: [gov, rplc, apsilankymas, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rplc/ambulatoriniai_apsilankymai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/rplc/ambulatoriniai_apsilankymai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2381/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rplc/ambulatorija"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Apsilankymas — Pateikiami Respublikinio Priklausomybės Ligų Centro Vilniaus filialo ambulatorinių skyrių (dienos stacionaras...

- **Model:** `datasets/gov/rplc/ambulatorija/Apsilankymas`[^manifest]
- **Dataset:** [Respublikinio Priklausomybės Ligų Centro Vilniaus filialo ambulatorinių skyrių pacientų...](../ambulatorija.md) (`datasets/gov/rplc/ambulatorija`)[^manifest]
- **Manifest CSV:** [datasets/gov/rplc/ambulatoriniai_apsilankymai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rplc/ambulatoriniai_apsilankymai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rplc/ambulatorija/Apsilankymas` (`deployed`)[^manifest]
- **Provider:** `rplc` — Respublikinis priklausomybės ligų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `pacientas` | `string` | — | `4` | `open` | — | Paciento žyma | — |
| `vizito_data` | `date` | `D` | `4` | `open` | — | Paciento vizito data. Jeigu nenurodyta mėnesio ir dienos tikslumu | — |
| `lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `gimimo_metai_gr` | `string` | — | `4` | `open` | — | Paciento gimimo metų grupė. | — |
| `amzius_gr` | `string` | — | `4` | `open` | — | Paciento amžiaus grupė. | — |
| `gyvenamoji_vieta` | `string` | — | `4` | `open` | — | Paciento gyvenamoji vieta | Duomenys pildomi nuo 2021m. |
| `issilavinimas` | `string` | — | `4` | `open` | — | Paciento išsilavinimas | — |
| `uzimtumas` | `string` | — | `4` | `open` | — | Paciento užimtumo statusas | — |
| `sveikatos_draudimas` | `boolean` | — | `4` | `open` | — | Nuoroda | — |
| `vizitas` | `string` | — | `4` | `open` | — | Paciento vizito tipas | — |
| `vartojimo_stazas` | `number` | — | `4` | `open` | — | Paciento vartojimo stažas. Jeigu reikšmė 100.0 - duomenų nepateikė. Atsakoma vizito metu. | — |
| `epizodai` | `integer` | `U` | `4` | `open` | — | Ambulatorinio gydymo epizodo atvejis yra ligonio lankymasis ambulatoriniame skyriuje pas gydytoją dėl konkrečios priežasties | — |
| `apsilankymai` | `integer` | `U` | `4` | `open` | — | Žymimas skaičius | — |
| `vartojimo_budas` | `string` | — | `4` | `open` | — | Jei pacientas vartoja narkotikus | — |
| `diagnoze` | `string` | — | `4` | `open` | — | Sutrikimai, klasifikuojami pagal TLK sisteminį ligų sąrašą. | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"vyras"` | — | — | — | — |
| `lytis` | `"moteris"` | — | — | — | — |
| `gyvenamoji_vieta` | `"Vilniaus apskritis"` | — | — | — | Pacientas kilęs iš Vilniaus |
| `gyvenamoji_vieta` | `"Kauno apskritis"` | — | — | — | Pacientas kilęs iš kitų Lietuvos teritorijų |
| `gyvenamoji_vieta` | `"Klaipėdos apskritis"` | — | — | — | — |
| `gyvenamoji_vieta` | `"Šiaulių apskritis"` | — | — | — | — |
| `gyvenamoji_vieta` | `"Panevėžio apskritis"` | — | — | — | — |
| `gyvenamoji_vieta` | `"Alytaus apskritis"` | — | — | — | — |
| `gyvenamoji_vieta` | `"Marijampolės apskritis"` | — | — | — | — |
| `gyvenamoji_vieta` | `"Tauragės apskritis"` | — | — | — | — |
| `gyvenamoji_vieta` | `"Telšių apskritis"` | — | — | — | — |
| `gyvenamoji_vieta` | `"Utenos apskritis"` | — | — | — | — |
| `gyvenamoji_vieta` | `"Užsienis"` | — | — | — | — |
| `vizitas` | `"pirminis"` | — | — | — | — |
| `vizitas` | `"pakartotinis"` | — | — | — | — |
| `vartojimo_budas` | `"leidžiasi"` | — | — | — | — |
| `vartojimo_budas` | `"rūko"` | — | — | — | — |
| `vartojimo_budas` | `"geria per burną"` | — | — | — | — |
| `vartojimo_budas` | `"rūko ir leidžiasi"` | — | — | — | — |
| `vartojimo_budas` | `"geria per burną ir leidžiasi"` | — | — | — | — |
| `vartojimo_budas` | `"uosto"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rplc/ambulatoriniai_apsilankymai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rplc/ambulatoriniai_apsilankymai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rplc/ambulatorija (https://data.gov.lt/datasets/2381/)
