---
type: Table
title: "Prasymas — Socialinio būsto prašymų duomenys"
description: "Lentelėje pateikiami prašymų gauti socialinį būstą arba būsto nuomos mokesčio dalies kompensaciją nuo 20 a."
resource: "https://get.data.gov.lt/datasets/gov/sadm/socialinis_bustas/Prasymas"
tags: [gov, sadm, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/sadm/soc_bustas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/soc_bustas.csv#L93"
    last_modified: "2026-11-11T14:39:20Z"
---

# Prasymas — Socialinio būsto prašymų duomenys

Lentelėje pateikiami prašymų gauti socialinį būstą arba būsto nuomos mokesčio dalies kompensaciją nuo 20 a. pabaigos duomenys:

prašymo dėl paramos būstui išsinuomoti BP-3 forma (dėl įrašymo į asmenų ir šeimų, turinčių teisę į socialinio būsto nuomą, sąrašą),

prašymo dėl paramos būstui išsinuomoti BP-5 forma (neįrašytiems į turinčių teisę sąrašus),

prašymo dėl paramos būstui išsinuomoti BP-4 forma (būsto nuomos mokesčio dalies kompensacijai gauti).

Lentelės objektas – vienas prašymas. Pateikiami duomenys apie prašymą (pateikimo laikas, kaip nurodyta socialinio būsto įstatyme, prašymo būsena duomenų atnaujinimo metu, pagal įstatymą apibrėžta būsto grupė, į kurią pretenduoja prašymą pateikęs asmuo, bei prašymo pagerinti būstą priežastis) ir jį teikusį asmenį (gyvenamoji savivaldybė ir duomenys apie turimą būstą). Lentelė jungiasi su kita rinkinio lentele „Sprendimai suteikti socialinį būstą“ pagal lauką „prasymo_id“.

- **Model:** `datasets/gov/sadm/socialinis_bustas/Prasymas`[^manifest]
- **Dataset:** [Socialinio būsto duomenys](../socialinis_bustas.md) (`datasets/gov/sadm/socialinis_bustas`)
- **Manifest CSV:** [datasets/gov/sadm/soc_bustas.csv#L93](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/soc_bustas.csv#L93)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sadm/socialinis_bustas/Prasymas`
- **Primary Key (`ref`):** `prasymo_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `prasymo_id` | `string` | — | `4` | `open` | — | Prašymo identifikacinis numeris | — |
| `prasymo_tipas` | `string` | — | `4` | `open` | — | Teikto prašymo gauti socialinį būstą tipas | — |
| `prasymo_laikas` | `datetime` | `S` | `4` | `open` | — | Prašymo teikimo laikas | — |
| `busena` | `string` | — | `4` | `open` | — | Prašymo būsena | — |
| `busenos_laikas` | `datetime` | `S` | `4` | `open` | — | Prašymo būsenos laikas | — |
| `busto_grupe` | `string` | — | `4` | `open` | — | Būsto grupė, į kurią pretenduoja prašymą dėl socialinio būsto teikęs asmuo ar šeima | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybės, kurioje teiktas prašymas, pavadinimas | — |
| `turimas_bustas` | `string` | — | `4` | `open` | — | Asmens ar šeimos, teikusios prašymą, turimo būsto požymis | — |
| `turimo_busto_ivert` | `string` | — | `4` | `open` | — | Turimo būsto švertinimas | — |
| `pagerinimo_priezastis` | `string` | — | `4` | `open` | — | Prašymo pagerinti būstą priežastis | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `prasymo_tipas` | `"Parama būstui išsinuomoti (dėl įrašymo Asmenų ir šeimų, turinčių teisę į socialinio būsto nuomą, sąrašą)"` | — | — | — | — |
| `prasymo_tipas` | `"Parama būstui išsinuomoti (būsto nuomos mokesčio dalies kompensacijai gauti)"` | — | — | — | — |
| `prasymo_tipas` | `"Parama būstui išsinuomoti (neįrašytiems į turinčių teisę sąrašus)"` | — | — | — | — |
| `busto_grupe` | `"Bendrasis"` | — | — | — | — |
| `busto_grupe` | `"Jaunų šeimų"` | — | — | — | — |
| `busto_grupe` | `"Neįgaliųjų, asmenų, sergančių lėtinių ligų sunkiomis formomis, ir šeimų, kuriose yra tokių asmenų"` | — | — | — | — |
| `busto_grupe` | `"Šeimų, auginančių tris ar daugiau vaikų ir (ar) vaikų, kuriems nustatyta nuolatinė globa"` | — | — | — | — |
| `busto_grupe` | `"Likusių be tėvų globos asmenų ir jų šeimų"` | — | — | — | — |
| `busto_grupe` | `"Socialinio būsto nuomininkų, turinčių teisę į socialinio būsto sąlygų pagerinimą"` | — | — | — | — |
| `turimas_bustas` | `"neturi būsto"` | — | — | — | — |
| `turimas_bustas` | `"nuosavybės teise turimas būstas"` | — | — | — | — |
| `turimas_bustas` | `"socialinis būstas"` | — | — | — | — |
| `turimas_bustas` | `"tarnybinis būstas arba bendrabutis"` | — | — | — | — |
| `turimo_busto_ivert` | `"Mažesnis kaip 10 kv. m vienam asmeniui ar šeimos nariui"` | — | — | — | — |
| `turimo_busto_ivert` | `"Nusidėvėjęs daugiau kaip 60 proc."` | — | — | — | — |
| `turimo_busto_ivert` | `"Mažesnis kaip 14 kv. m vienam asmeniui ar šeimos nariui (jei yra neįgalusis arba asmuo, sergantis sunkia lėtinės ligos forma)"` | — | — | — | — |
| `turimo_busto_ivert` | `"Nepritaikytas neįgaliųjų poreikiams"` | — | — | — | — |
| `pagerinimo_priezastis` | `"padidėjo šeimos narių skaičius"` | — | — | — | — |
| `pagerinimo_priezastis` | `"šeimoje yra skirtingų lyčių vyresnių kaip 9 metai vaikų, kurie turi turėti atskirus kambarius"` | — | — | — | — |
| `pagerinimo_priezastis` | `"šeimoje yra neįgaliųjų, kurie turi turėti atskirus kambarius"` | — | — | — | — |
| `pagerinimo_priezastis` | `"įgijo teisę į neįgaliųjų poreikiams pritaikytą socialinį būstą"` | — | — | — | — |
| `pagerinimo_priezastis` | `"šeimoje yra sergančių lėtine liga sunkia forma, kurie turi turėti atskirus kambarius"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sadm/soc_bustas.csv
