---
type: Table
title: "Imone — Valstybės valdomų įmonių finansiniai duomenys"
description: "Valdymo koordinavimo centro (VKC) sistema „Valstybės valdomų įmonių finansiniai ir nefinansiniai duomenys“ kaupia valstybės valdomų įmonių finansinius duomenis."
resource: "https://get.data.gov.lt/datasets/gov/vkc/vvi/Imone"
tags: [gov, vkc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vkc/vvi.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkc/vvi.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Imone — Valstybės valdomų įmonių finansiniai duomenys

Valdymo koordinavimo centro (VKC) sistema „Valstybės valdomų įmonių finansiniai ir nefinansiniai duomenys“ kaupia valstybės valdomų įmonių finansinius duomenis. Duomenys kaupiami nuo 2019 m. ir yra atnaujinami. Duomenų rinkinys sudarytas iš duomenų aktualumo datos, įmonės JAR kodo, pavadinimo, sektoriaus, ar yra valstybės valdomų įmonių (VVĮ) portfelyje, teisinės formos, atstovaujančios įstaigos, valstybei priklausančios dalies, bendro pelno, veiklos pelno, pelno mokesčio, grynojo pelno, ilgalaiko turto, trumpalaiko turto, laikotarpių po einamųjų metų pajamų su sąnaudomis, bendrojo turto, įstatinio pasirašytojo kapitalo, įprastų bei perkainojimo rezervų, nepaskirstytojo pelno, įsipareigojimų einamaisiais metais, metais po einamųjų metų ir bendrų įsipareigojimų. Vienas įrašas atitinka vieną įmonę konkrečiais metais. Valstybei priklausanti dalis matuojama procentais šimtųjų tikslumu, visi kiti skaičiai matuojami tūkst. eurų. Jeigu skaičius yra neigiamas, jis reiškia matuojamo požymio priešingybę, pvz., neigiamas pelnas reiškia nuostolius. Atvertas duomenų rinkinys nebus atnaujinamas.

- **Model:** `datasets/gov/vkc/vvi/Imone`[^manifest]
- **Dataset:** [Valstybės valdomų įmonių finansiniai duomenys](../vvi.md) (`datasets/gov/vkc/vvi`)
- **Manifest CSV:** [datasets/gov/vkc/vvi.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkc/vvi.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vkc/vvi/Imone`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `metai` | `date` | `Y` | `4` | `open` | — | Duomenų aktualumo data | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Įmonės JAR kodas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Įmonės pavadinimas | — |
| `sektorius` | `string` | — | `4` | `open` | — | Įmonės sektorius | — |
| `ar_yra_vvi_portfelyje` | `string` | — | `4` | `open` | — | Ar įmonė yra valstybės valdomų įmonių portfelyje | — |
| `teisine_forma` | `string` | — | `4` | `open` | — | Įmonės teisinė forma | — |
| `atstovaujanti_istaiga` | `string` | — | `4` | `open` | — | Valstybę atstovaujanti įstaiga | — |
| `valstybes_dalis` | `number` | `%` | `4` | `open` | — | Valstybei priklausanti įmonės dalis procentais | — |
| `bendras_pelnas` | `number` | — | `4` | `open` | — | Įmonės bendras pelnas | — |
| `veiklos_pelnas` | `number` | — | `4` | `open` | — | Įmonės veiklos pelnas | — |
| `pelno_mokestis` | `number` | — | `4` | `open` | — | Įmonės sumokėtas pelno mokestis | — |
| `grynasis_pelnas` | `number` | — | `4` | `open` | — | Įmonės grynasis pelnas | — |
| `ilgalaikis_turtas` | `number` | — | `4` | `open` | — | Įmonės ilgalaikis turtas | — |
| `trumpalaikis_turtas` | `number` | — | `4` | `open` | — | Įmonės trumpalaikis turtas | — |
| `busimu_laikotarpiu_pajamos_sanaudos` | `number` | — | `4` | `open` | — | Įmonės būsimų laikotarpių pajamos ir sąnaudos | — |
| `bendras_turtas` | `number` | — | `4` | `open` | — | Įmonės bendras turtas | — |
| `istatinis_pasirasytas_kapitalas` | `number` | — | `4` | `open` | — | Duomenys apie įmonės kapitalo elemento dalį, kuris yra susijęs su įmonę įstatiniu (pasirašytuoju) kapitalu | — |
| `perkainojimo_rezervai` | `number` | — | `4` | `open` | — | Pateikiama informacija apie skirtumą tarp tam tikro turto dabartinės vertės ir jo buvusios įrašytos vertės | — |
| `rezervai` | `number` | — | `4` | `open` | — | Pateikiami duomenys apie skirtingus rezervus, kurie yra susiję su įmonės veikla | — |
| `nepaskirstytasis_pelnas` | `number` | — | `4` | `open` | — | Įmonės nepaskirstytas pelnas | — |
| `isipareigojimai_po_metu` | `number` | — | `4` | `open` | — | Įmonės įsipareigojimai, mokėtinus po vienų metų | — |
| `isipareigojimai_per_metus` | `number` | — | `4` | `open` | — | Įmonės įsipareigojimai, kuriuos įmonė turi sumokėti per artimiausius metus | — |
| `isipareigojimai` | `number` | — | `4` | `open` | — | Įmonės įsipareigojimai, kuriuos įmonė turi apmokėti ateityje | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `sektorius` | `"Kita"` | — | — | Kita | — |
| `sektorius` | `"Susisiekimas"` | — | — | Susisiekimas | — |
| `sektorius` | `"Energetika"` | — | — | Energetika | — |
| `sektorius` | `"Miškininkystė"` | — | — | Miškininkystė | — |
| `ar_yra_vvi_portfelyje` | `"Taip"` | — | — | Taip | — |
| `ar_yra_vvi_portfelyje` | `"Ne"` | — | — | Ne | — |
| `teisine_forma` | `"UAB"` | — | — | Uždara akcinė bendrovė | — |
| `teisine_forma` | `"VĮ"` | — | — | Valstybės įmonė | — |
| `teisine_forma` | `"AB"` | — | — | Akcinė bendrovė | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `bendras_pelnas` | `update(type: "money", ref: "EUR")` | `type` | — | — | — | — | — |
| `veiklos_pelnas` | `update(type: "money", ref: "EUR")` | `type` | — | — | — | — | — |
| `pelno_mokestis` | `update(type: "money", ref: "EUR")` | `type` | — | — | — | — | — |
| `grynasis_pelnas` | `update(type: "money", ref: "EUR")` | `type` | — | — | — | — | — |
| `ilgalaikis_turtas` | `update(type: "money", ref: "EUR")` | `type` | — | — | — | — | — |
| `trumpalaikis_turtas` | `update(type: "money", ref: "EUR")` | `type` | — | — | — | — | — |
| `busimu_laikotarpiu_pajamos_sanaudos` | `update(type: "money", ref: "EUR")` | `type` | — | — | — | — | — |
| `bendras_turtas` | `update(type: "money", ref: "EUR")` | `type` | — | — | — | — | — |
| `istatinis_pasirasytas_kapitalas` | `update(type: "money", ref: "EUR")` | `type` | — | — | — | — | — |
| `perkainojimo_rezervai` | `update(type: "money", ref: "EUR")` | `type` | — | — | — | — | — |
| `rezervai` | `update(type: "money", ref: "EUR")` | `type` | — | — | — | — | — |
| `nepaskirstytasis_pelnas` | `update(type: "money", ref: "EUR")` | `type` | — | — | — | — | — |
| `isipareigojimai_po_metu` | `update(type: "money", ref: "EUR")` | `type` | — | — | — | — | — |
| `isipareigojimai_per_metus` | `update(type: "money", ref: "EUR")` | `type` | — | — | — | — | — |
| `isipareigojimai` | `update(type: "money", ref: "EUR")` | `type` | — | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vkc/vvi.csv
