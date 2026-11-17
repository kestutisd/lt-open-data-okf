---
type: Table
title: "Isvyka — Namuose balsuojančiųjų rinkėjų balsų rinkimo išvykos"
description: "Vyriausiosios rinkimų komisijos Rinkimų organizavimo posistemėje nuo 2011-12-29 kaupiami ir iki šiol atnaujinami balsų skaičiavimo išvykų i rinkėjų namus duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vrk/balsu_skaiciavimo_isvykos/Isvyka"
tags: [gov, vrk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vrk/balsu_skaiciavimo_isvykos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/balsu_skaiciavimo_isvykos.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Isvyka — Namuose balsuojančiųjų rinkėjų balsų rinkimo išvykos

Vyriausiosios rinkimų komisijos Rinkimų organizavimo posistemėje nuo 2011-12-29 kaupiami ir iki šiol atnaujinami balsų skaičiavimo išvykų i rinkėjų namus duomenys. Duomenų rinkinys apima vykdomų rinkimų identifikatorių bei pavadinimą, vykdomų rinkimų turo identifikatorių ir numerį, išvykos identifikatorių, komisijos nario identifikatorių, pareigas, organizaciją, apygardų ir apylinkių, kuriose dirba ir kuriose skaičiavo balsus, identifikatorius ir pavadinimus. Rinkinyje taip pat yra duomenų apie numatytą aplankyti rinkėjų skaičių, grafiko būseną, grafiko bei planuotos išvykos datas. Vienas rinkinio įrašas atitinka vieno nario išvyką atitinkamų rinkimų metu. Komisijos narių darbo apygardos ir apylinkės nurodytos ne visur, siekiant parodyti, ar atitinkamas narys priklauso centrinei komisijai, kuri neturi nei apygardos, nei apylinkės, ar jis yra apygardos darbuotojas, kai nurodyta tik apygarda, arba apylinkės darbuotojas, kai nurodyta tik apylinkė.

- **Model:** `datasets/gov/vrk/balsu_skaiciavimo_isvykos/Isvyka`[^manifest]
- **Dataset:** [Namuose balsuojančiųjų rinkėjų balsų rinkimo išvykos](../balsu_skaiciavimo_isvykos.md) (`datasets/gov/vrk/balsu_skaiciavimo_isvykos`)
- **Manifest CSV:** [datasets/gov/vrk/balsu_skaiciavimo_isvykos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/balsu_skaiciavimo_isvykos.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vrk/balsu_skaiciavimo_isvykos/Isvyka`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `vr_id` | `string` | — | `4` | `open` | — | Vykdomų rinkimų identifikatorius | — |
| `vr_pav` | `string` | — | `4` | `open` | — | Vykdomų rinkimų pavadinimas | — |
| `vrt_id` | `string` | — | `4` | `open` | — | Vykdomų rinkimų turo identifikatorius | — |
| `vrt_nr` | `integer` | — | `4` | `open` | — | Vykdomų rinkimų turo numeris | — |
| `isvykos_id` | `string` | — | `4` | `open` | — | Išvykos identifikatorius | — |
| `komisijos_nario_id` | `string` | — | `4` | `open` | — | Komisijos nario identifikatorius | — |
| `komisijos_nario_pareigos` | `string` | — | `4` | `open` | — | Komisijos nario pareigos | — |
| `komisijos_nario_rinkimu_org` | `string` | — | `4` | `open` | — | Komisijos nario rinkiminė organizacija | — |
| `komisijos_nario_apygardos_id` | `string` | — | `4` | `open` | — | Komisijos nario apygardos, kurioje dirba, identifikatorius | — |
| `komisijos_nario_apygardos_pav` | `string` | — | `4` | `open` | — | Komisijos nario apygardos, kurioje dirba, pavadinimas | — |
| `komisijos_nario_apylinkes_id` | `string` | — | `4` | `open` | — | Komisijos nario apylinkės, kurioje dirba, identifikatorius | — |
| `komisijos_nario_apylinkes_pav` | `string` | — | `4` | `open` | — | Komisijos nario apylinkės, kurioje dirba, pavadinimas | — |
| `isvykimo_apygardos_id` | `string` | — | `4` | `open` | — | Apygardos, kurioje komisijos narys skaičiavo balsus, identifikatorius | — |
| `isvykimo_apygardos_pav` | `string` | — | `4` | `open` | — | Apygardos, kurioje komisijos narys skaičiavo balsus, pavadinimas | — |
| `isvykimo_apylinkes_id` | `string` | — | `4` | `open` | — | Apylinkės, kurioje komisijos narys skaičiavo balsus, identifikatorius | — |
| `isvykimo_apylinkes_pav` | `string` | — | `4` | `open` | — | Apylinkės, kurioje komisijos narys skaičiavo balsus, pavadinimas | — |
| `numatyta_aplankyti_rinkeju_sk` | `integer` | — | `4` | `open` | — | Numatytas išvykos metu aplankyti rinkėjų skaičius | — |
| `grafiko_data` | `date` | `D` | `4` | `open` | — | Grafiko data | — |
| `planuojama_isvykimo_data` | `date` | `D` | `4` | `open` | — | Planuotos išvykos data | — |
| `grafiko_busena` | `string` | — | `4` | `open` | — | Grafiko naujausia būsena | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `grafiko_busena` | `"Patvirtinta"` | — | — | Patvirtinta | — |
| `grafiko_busena` | `"Pildoma"` | — | — | Pildoma | — |
| `grafiko_busena` | `"Laukiama patvirtinimo"` | — | — | Laukiama patvirtinimo | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/balsu_skaiciavimo_isvykos.csv
