---
type: Table
title: "Profilis — Priėmimo prašymus į profesinio mokymo įstaigas teikusių asmenų profilis"
description: "Lentelėje pateikiami demografiniai duomenys apie asmenis, teikusius priėmimo prašymus į profesinio mokymo įstaigas."
resource: "https://get.data.gov.lt/datasets/gov/lamabpo/profesines_mokyklos/Profilis"
tags: [gov, lamabpo, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lamabpo/profesiniu_prasymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/profesiniu_prasymai.csv#L61"
    last_modified: "2026-11-11T14:39:20Z"
---

# Profilis — Priėmimo prašymus į profesinio mokymo įstaigas teikusių asmenų profilis

Lentelėje pateikiami demografiniai duomenys apie asmenis, teikusius priėmimo prašymus į profesinio mokymo įstaigas. Lentelės eilutės objektas – asmuo, teikęs priėmimo prašymą. Pažymėtina, jog priėmimo prašymus gali teikti ne tik Lietuvos Respublikos piliečiai, bet ir užsieniečiai. Nurodomi asmens gimimo metai, lytis, požymis, ar galimai yra užsienietis. Prie lentelės taip pat prijungti duomenys iš Lietuvos Respublikos gyventojų registro ir Nacionalinės švietimo agentūros informacinių sistemų apie asmens gyvenamąją vietą (savivaldybę ir gyvenvietės tipą) prašymo teikimo metu ir instituciją, kurioje įgijo pagrindinį arba vidurinį išsilavinimą.

- **Model:** `datasets/gov/lamabpo/profesines_mokyklos/Profilis`[^manifest]
- **Dataset:** [Priėmimo į profesinio mokymo įstaigas prašymų duomenys](../profesines_mokyklos.md) (`datasets/gov/lamabpo/profesines_mokyklos`)
- **Manifest CSV:** [datasets/gov/lamabpo/profesiniu_prasymai.csv#L61](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/profesiniu_prasymai.csv#L61)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lamabpo/profesines_mokyklos/Profilis`
- **Primary Key (`ref`):** `asmens_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `asmens_id` | `string` | — | `4` | `open` | — | Asmens identifikacinis numeris | — |
| `ar_galimai_uzsienietis` | `boolean` | — | `4` | `open` | — | Požymis, ar asmuo galimai yra užsienietis. Jeigu asmens priėmimo prašyme nepateiktas asmens kodas, tuomet daroma išvada, jog yra užsienietis. Tačiau šis požymis neapima užsieniečių asmenų, turinčių lietuvišką asmens kodą. | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Asmens gimimo metai | — |
| `lytis` | `string` | — | `4` | `open` | — | Asmens lytis | — |
| `issilavinim_inst_jar` | `string` | — | `4` | `open` | — | Švietimo įstaigos (mokyklos) kodas Juridinių asmenų registre. | — |
| `issilavinimo_institucija` | `string` | — | `4` | `open` | — | Švietimo institucija, kurioje asmuo įgijo brandos atestatą | — |
| `issilavinimo_sav_kodas` | `string` | — | `4` | `open` | — | Švietimo įstaigos savivaldybė | — |
| `issilavinimo_sav` | `string` | — | `4` | `open` | — | Švietimo įstaigos savivaldybės pavadinimas | — |
| `asm_gyv_sav` | `string` | — | `4` | `open` | — | Asmens gyvenamosios savivaldybės pavadinimas | — |
| `asm_gyv_tipas` | `string` | — | `4` | `open` | — | Gyvenvietės tipas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"vyras"` | — | — | — | — |
| `lytis` | `"moteris"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lamabpo/profesiniu_prasymai.csv
