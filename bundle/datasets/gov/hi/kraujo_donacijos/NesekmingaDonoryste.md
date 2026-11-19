---
type: Table
title: "NesekmingaDonoryste — Nesėkmingi kraujo donacijos vizitai"
description: "\"Nesėkmingų kraujo donacijos vizitų duomenys iš Higienos instituto Kraujo donorų registro informacinės sistemos."
resource: "https://get.data.gov.lt/datasets/gov/hi/kraujo_donacijos/NesekmingaDonoryste"
tags: [gov, hi, nesekmingadonoryste, deployed, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/kraujo_donacijos.csv#L53"
    title: "atviriduomenys/manifest — datasets/gov/hi/kraujo_donacijos.csv#L53"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3889/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/kraujo_donacijos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# NesekmingaDonoryste — Nesėkmingi kraujo donacijos vizitai

"Nesėkmingų kraujo donacijos vizitų duomenys iš Higienos instituto Kraujo donorų registro informacinės sistemos. Viena eilutė yra vienas unikalus ir nesėkmingas kraujo donavimo vizitas. Vizitas laikomas nesėkmingu, kai kraują donuojančiam asmeniui nepavyksta praeiti medicininės atrankos (pvz., dėl mažo hemoglobino kiekio kraujyje), procedūra nutraukiama arba kai donuotame kraujyje aptinkama patogenų. Eilutėje nurodomas vizito identifikacinis numeris, vizito metai, donuojančio asmens gimimo metai, lytis, gydytojo sprendimas leisti donuoti kraują, donacijos statusas, įvairių testų metu kraujyje nustatyti patogenai, kraujo grupė, hemoglobino kiekis vizito metu, bei nesėkmingos kraujo donacijos sustabdymo kriterijus."[^manifest]

- **Model:** `datasets/gov/hi/kraujo_donacijos/NesekmingaDonoryste`[^manifest]
- **Dataset:** [Kraujo donacijos](../kraujo_donacijos.md) (`datasets/gov/hi/kraujo_donacijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/hi/kraujo_donacijos.csv#L53](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/kraujo_donacijos.csv#L53)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/kraujo_donacijos/NesekmingaDonoryste` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vizito_id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vizito_id` | `string` | — | `4` | `open` | — | Vizito ID | Apsilankymo duoti kraujo identifikacinis numeris |
| `vizito_metai` | `date` | `Y` | `4` | `open` | — | Vizito metai | Apsilankymo duoti kraujo metai |
| `gim_metai` | `date` | `Y` | `4` | `open` | — | Gimimo metai | Donoro gimimo metai. 40 % asmenų gimimo metai yra padidinti arba sumažinti vieneriais metais |
| `lytis` | `string` | — | `4` | `open` | — | Donoro lytis | — |
| `sprendimo_tipas` | `string` | — | `4` | `open` | — | Sprendimo tipas | Gydytojo sprendimas leisti donuoti kraują |
| `donacijos_statusas` | `string` | — | `4` | `open` | — | Kraujo donavimo statusas | — |
| `kraujo_grupe` | `string` | — | `4` | `open` | — | Donoro kraujo grupė | — |
| `hemoglobino_kiekis` | `integer` | `g/l` | `4` | `open` | — | Hemoglobino kiekis | "Donoro hemoglobino kiekis kurajo donorystės vizito metu, matuojama g/L" |
| `nustatyti_patogenai` | `string` | — | `4` | `open` | — | Nustatyti patogenai | Patogenai nustatyti kraujyje atrankinio arba patvirtinamojo kraujo tyrimo metu |
| `sustabdymo_krit` | `string` | — | `4` | `open` | — | Sustabdymo kriterijus | "Kriterijus, nurodantis priežastį dėl ko kraujo donorystė buvo nesėkminga" |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"M"` | — | — | Moteris | — |
| `lytis` | `"V"` | — | — | Vyras | — |
| `sprendimo_tipas` | `"Laikinai atidėta"` | — | — | Laikinai atidėta | — |
| `sprendimo_tipas` | `"Leista"` | — | — | Leista | — |
| `sprendimo_tipas` | `"Uždrausta visam laikui"` | — | — | Uždrausta visam laikui | — |
| `donacijos_statusas` | `"Atranka nesėkminga"` | — | — | Atranka nesėkminga | "Apsilankymo būsena priskiriama, kai KDĮ perduoda gydytojo sprendimą, priimtą atrankos metu, uždrausti arba laikinai sustabdyti donaciją/donorystę" |
| `donacijos_statusas` | `"Donacija nesėkminga"` | — | — | Donacija nesėkminga | "Apsilankymo būsena priskiriama, kai po atrankinių/patvirtinamųjų kraujo tyrimų rezultatų gavimo yra gydytojo sprendimas uždrausti arba laikinai sustabdyti donorystę. Esant šiai būsenai skaitoma, kad donoras davė kraujo ar jo komponentų – donacija atlikta" |
| `donacijos_statusas` | `"Donacija nutraukta"` | — | — | Donacija nutraukta | "Apsilankymo būsena priskiriama, kai, KDĮ perdavus donacijos numerį ir registre jai automatiškai suteikus donacijos identifikavimo kodą, donacija dėl tam tikrų priežasčių nebuvo atlikta. Esant šiai būsenai skaitoma, kad donacija neatlikta, t.y. donoras nedavė kraujo ar jo komponentų" |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/kraujo_donacijos.csv#L53 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/kraujo_donacijos.csv#L53)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/kraujo_donacijos (https://data.gov.lt/datasets/3889/)
