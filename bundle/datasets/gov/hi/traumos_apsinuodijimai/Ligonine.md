---
type: Table
title: "Ligonine — Traumų ir apsinuodijimų atvejai dėl kurių kreiptasi į gydymo įstaigą"
description: "\"Duomenys iš Higienos instituto apie traumų ir apsinuodijimų atvejus dėl kurių buvo kreiptasi į gydymo įstaigą."
resource: "https://get.data.gov.lt/datasets/gov/hi/traumos_apsinuodijimai/Ligonine"
tags: [gov, hi, ligonine, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/traumos_apsinuodijimai.csv#L41"
    title: "atviriduomenys/manifest — datasets/gov/hi/traumos_apsinuodijimai.csv#L41"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2829/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/traumos_apsinuodijimai"
    author: "team:vda"
    last_modified: "2026-10-20T00:00:00Z"
---

# Ligonine — Traumų ir apsinuodijimų atvejai dėl kurių kreiptasi į gydymo įstaigą

"Duomenys iš Higienos instituto apie traumų ir apsinuodijimų atvejus dėl kurių buvo kreiptasi į gydymo įstaigą. Vieną eilutę sudaro vienas unikalus traumos / apsinuodjimo atvejis ir gydymo įstaiga, į kurią buvo kreiptasi. Eilutėje nurodomas gydymo įstaigos identifikacinis numeris, gydymo lapo pradžia ir pabaiga, TLK-10-AM traumos kodas, stacionaro tipas."[^manifest]

- **Model:** `datasets/gov/hi/traumos_apsinuodijimai/Ligonine`[^manifest]
- **Dataset:** ["Stacionaro ir ambulatoriniai ligoniai, gydyti nuo traumų ir apsinuodijimų"](../traumos_apsinuodijimai.md) (`datasets/gov/hi/traumos_apsinuodijimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/hi/traumos_apsinuodijimai.csv#L41](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/traumos_apsinuodijimai.csv#L41)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/traumos_apsinuodijimai/Ligonine` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_pk`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-10-20`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_pk` | `string` | — | `4` | `open` | — | VDA PK | — |
| `gist_id` | `string` | — | `4` | `open` | — | Gydymo įstaigos identifikacinis numeris | — |
| `gyd_lap_pradzia` | `datetime` | `T` | `4` | `open` | — | Gydymo lapo pradžia | — |
| `gyd_lap_pabaiga` | `datetime` | `T` | `4` | `open` | — | Gydymo lapo pabaiga | — |
| `tlk_trauma` | `string` | — | `4` | `open` | — | Traumos kodas | — |
| `gydymas` | `string` | — | `4` | `open` | — | Gydymo tipas | — |
| `stacionaro_tipas` | `string` | — | `4` | `open` | — | Stacionaro tipas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `gydymas` | `"Ambulatorinis"` | — | — | Ambulatorinis | — |
| `gydymas` | `"Stacionarinis"` | — | — | Stacionarinis | — |
| `stacionaro_tipas` | `"A"` | — | — | Aktyvus | "Paslaugos, teikiamos pacientams dėl ūmios ligos, lėtinės ligos paūmėjimo ar sužalojimo. Teikiant šias paslaugas reikalingas ištyrimas ir (ar) aktyvus medikamentinis, ir (ar) chirurginis gydymas, kuris negali būti taikomas ambulatorinėmis sąlygomis." |
| `stacionaro_tipas` | `"I"` | — | — | Ilgalaikis | "Paslaugos, teikiamos lėtinėmis ligomis sergantiems pacientams, kai reikalingas ilgai (dažniausiai ilgiau nei mėnesį) trunkantis gydymas ir (ar) slauga. Šioms paslaugoms priskiriamos slaugos ir palaikomojo gydymo, tuberkuliozės, specialiosios psichiatrijos, psichikos ligų ilgalaikio gydymo paslaugos ir pan." |
| `stacionaro_tipas` | `"R"` | — | — | Reabilitacinis | "Reabilitacijos priemonių (fizioterapijos, kineziterapijos, ergoterapijos, ortopedinių ir techninės pagalbos priemonių, psichologinės pagalbos, gydymo vaistais, pacientų ir jų artimųjų mokymo, gydymo dieta ir kt.) taikymas siekiant kuo daugiau sugrąžinti sutrikusias funkcijas arba, esant negrįžtamiems pakitimams, jas kompensuoti, arba palaikyti pasiektą funkcinio pajėgumo lygį. Susirgimai ir būklės, kada reabilitacijos paslaugos gali būti teikiamos stacionare, yra patvirtintos Sveikatos apsaugos ministro įsakymu." |
| `stacionaro_tipas` | `"T"` | — | — | Transplantacinis | "Paslaugos, kurias teikiant iš vieno asmens paimti audiniai, ląstelės ir (ar) organai persodinami kitam arba tam pačiam asmeniui gydymo tikslu. Yra atliekamos inkstų, širdies, kepenų, plaučių, širdies ir plaučių komplekso, kasos ir inksto komplekso, ragenos, kaulų čiulpų transplantacijos." |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/traumos_apsinuodijimai.csv#L41 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/traumos_apsinuodijimai.csv#L41)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/traumos_apsinuodijimai (https://data.gov.lt/datasets/2829/)
