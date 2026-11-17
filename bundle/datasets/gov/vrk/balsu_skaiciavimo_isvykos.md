---
type: Dataset
title: "Namuose balsuojančiųjų rinkėjų balsų rinkimo išvykos"
description: "Vyriausiosios rinkimų komisijos Rinkimų organizavimo posistemė kaupia balsų skaičiavimo išvykų rinkėjų namuose duomenis."
resource: "https://get.data.gov.lt/datasets/gov/vrk/balsu_skaiciavimo_isvykos"
tags: [gov, vrk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vrk/balsu_skaiciavimo_isvykos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/balsu_skaiciavimo_isvykos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Namuose balsuojančiųjų rinkėjų balsų rinkimo išvykos

Vyriausiosios rinkimų komisijos Rinkimų organizavimo posistemė kaupia balsų skaičiavimo išvykų rinkėjų namuose duomenis. Duomenys kaupiami nuo 2011-12-29 ir yra atnaujinami. Duomenų rinkinys apima vykdomų rinkimų identifikatorių bei pavadinimą, vykdomų rinkimų turo identifikatorių ir numerį, išvykos identifikatorių, komisijos nario identifikatorių, pareigas, organizaciją, apygardų, apylinkių identifikatorius ir pavadinimus, kuriose dirba, ir apygardų, apylinkių, kuriose skaičiavo balsus. Rinkinyje taip pat yra duomenų apie numatytą aplankyti rinkėjų skaičių, grafiko būseną ir grafiko sukūrimo bei planuotą išvykos datas. Vienas rinkinio įrašas atitinka vieno nario išvyką atitinkamų rinkimų metu. Komisijos narių darbo apygardos bei apylinkės vietomis paliktos tuščios parodyti, ar atitinkamas narys priklauso centrinei komisijai, kuri neturi nei apygardos, nei apylinkės, ar yra apygardos darbuotojas, kai nurodyta tik apygarda, arba apylinkės darbuotojas, kai nurodyta tik apylinkė.

- **Namespace:** `datasets/gov/vrk/balsu_skaiciavimo_isvykos`[^manifest]
- **Manifest CSV:** [datasets/gov/vrk/balsu_skaiciavimo_isvykos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/balsu_skaiciavimo_isvykos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vrk/balsu_skaiciavimo_isvykos`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Isvyka](balsu_skaiciavimo_isvykos/Isvyka.md) | Namuose balsuojančiųjų rinkėjų balsų rinkimo išvykos | `4` | `vda_prime_key` | — | 21 | Vyriausiosios rinkimų komisijos Rinkimų organizavimo posistemėje nuo 2011-12-29 kaupiami ir iki šiol atnaujinami balsų skaičiavimo išvykų i rinkėjų namus... |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/balsu_skaiciavimo_isvykos.csv
