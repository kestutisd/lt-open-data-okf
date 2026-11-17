---
type: Table
title: "SekmingaDonoryste — Sėkmingi kraujo donacijos vizitai"
description: "Lentelėje pateikiami sėkmingų kraujo donacijos vizitų duomenys iš Higienos instituto Kraujo donorų registro informacinės sistemos."
resource: "https://get.data.gov.lt/datasets/gov/hi/kraujo_donacijos/SekmingaDonoryste"
tags: [gov, hi, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/hi/kraujo_donacijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/kraujo_donacijos.csv#L38"
    last_modified: "2026-11-11T14:39:20Z"
---

# SekmingaDonoryste — Sėkmingi kraujo donacijos vizitai

Lentelėje pateikiami sėkmingų kraujo donacijos vizitų duomenys iš Higienos instituto Kraujo donorų registro informacinės sistemos. Viena eilutė yra vienas unikalus ir sėkmingas kraujo donacijos vizitas. Kraujo donacijos vizitas laikomas sėkmingu, kai kraują donuojantis asmuo sėkmingai praeina medicininę atranką, o jo donuotame kraujyje nėra aptinkama patogenų (t. y. testai, kurie atliekami po kraujo donacijos ir identifikuojantys infekcinių ligų žymenis, yra neigiami). Eilutėje nurodomas unikalaus vizito identifikacinis numeris, donoro identifikacinis numeris, vizito data, donacijos tipas ir hemoglobino kiekis donoro kraujyje vizito metu, požymiai, nurodantys ar kraujas yra duodamas pirmą kartą, ar kraujas sudarytas iš kelių komponentų, ar donorystė yra atlygintina, ar donacija atliekama mobiliajame punkte, taip pat nurodomas vizitą administruojantis kraujo donorystės centras ir savivaldybė, kurioje atliekama donacija. Paskutiniuose dviejuose stulpeliuose nurodomi įrašo sukūrimo ir atnaujinimo data bei laikas duomenų bazėje.

- **Model:** `datasets/gov/hi/kraujo_donacijos/SekmingaDonoryste`[^manifest]
- **Dataset:** [Kraujo donacijos](../kraujo_donacijos.md) (`datasets/gov/hi/kraujo_donacijos`)
- **Manifest CSV:** [datasets/gov/hi/kraujo_donacijos.csv#L38](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/kraujo_donacijos.csv#L38)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/kraujo_donacijos/SekmingaDonoryste`
- **Primary Key (`ref`):** `vizito_id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vizito_id` | `string` | — | `4` | `open` | — | Vizito ID | Apsilankymo duoti kraujo identifikacinis numeris |
| `donoro_id` | `string` | — | `4` | `open` | — | Donoro ID | Donoro (kraujo davėjo) identifikacinis numeris |
| `vizito_data` | `date` | `D` | `4` | `open` | — | Vizito data | Apsilankymo duoti kraujo data |
| `donancijos_tipas` | `string` | — | `4` | `open` | — | Kraujo davimo tipas | — |
| `pirmas_kartas` | `boolean` | — | `4` | `open` | — | Pirmas kartas | Požymis, nurodantis, ar krauajs yra duodamas pirmą kartą |
| `is_keliu_komp` | `boolean` | — | `4` | `open` | — | Iš kelių komponentų | Požymis, nurodantis, ar kraujo donorą sudaro keletas kraujo komponentų |
| `donorystes_centras` | `string` | — | `4` | `open` | — | Donorystės centras | Kraujo donorystės centras administruojantis vizitą |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė | Savivaldybė, kurioje buvo duotas kraujas |
| `mobilusis_punktas` | `boolean` | — | `4` | `open` | — | Mobilusis punktas | Požymis, nurodantis ar kraujo buvo duota mobiliajame punkte |
| `atlyginta_donoryste` | `boolean` | — | `4` | `open` | — | Atlyginta donorystė | Požymis, nurodantis ar kraujas buvo duodamas už piniginį atlygį |
| `hemoglobino_kiekis` | `integer` | `g/l` | `4` | `open` | — | Hemoglobino kiekis | Asmens hemoglobino kiekis kurajo donorystės vizito metu, matuojama g/L |
| `irasas_sukurtas` | `datetime` | `S` | `4` | `open` | — | Įrašo sukūrimo data ir laikas duomenų bazėje | — |
| `irasas_atnaujintas` | `datetime` | `S` | `4` | `open` | — | Įrašo atnaujinimo data ir laikas duomenų bazėje | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/kraujo_donacijos.csv
