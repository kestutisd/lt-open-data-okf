---
type: Table
title: "MiskoKirtimoLeidimas — Kertamų miško plotų atstumai iki Lietuvos Respublikos sienos"
description: "Lentelėje pateikiami duomenys apie miško kirtimų leidimus ir kertamų miško plotų atstumus iki Lietuvos Respublikos (LR) sienos."
resource: "https://get.data.gov.lt/datasets/gov/lsd/aplinkosauga/kertamu_plotu_leidimai/MiskoKirtimoLeidimas"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/aplinkosauga/kertamu_plotu_leidimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/aplinkosauga/kertamu_plotu_leidimai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# MiskoKirtimoLeidimas — Kertamų miško plotų atstumai iki Lietuvos Respublikos sienos

Lentelėje pateikiami duomenys apie miško kirtimų leidimus ir kertamų miško plotų atstumus iki Lietuvos Respublikos (LR) sienos. Viena lentelės eilutė atitinka vieną unikalų išduotą leidimą kirsti miško plotą. Lentelę sudaro: unikalios eilutės identifikatorius, kertamo miško ploto tipas, vyraujanti medžių rūšis, kirtimo rūšis, atkūrimo būdas, kertamo ploto dydis hektarais, mažiausias atstumas iki LR sienos, artimiausia kertamo ploto kaimyninės valstybės siena, leidimo kirsti mišką galiojimo pradžia ir pabaiga, valstybinės miškų urėdijos padalinio pavadinimas, girininkijos pavadinimas, kertamo miško ploto nuosavybės forma, kvartalas, sklypas, kadastrinis numeris ir kertamo miško ploto geometrija keliais formatais.

Duomenys apie leidimus kirsti miškus gaunami iš Aplinkosaugos leidimų informacinės sistemos Leidimų kirsti mišką posistemio atvirų duomenų nuorodos: https://lkmp.alisas.lt/static/lkmp-data.geojson.zip.

- **Model:** `datasets/gov/lsd/aplinkosauga/kertamu_plotu_leidimai/MiskoKirtimoLeidimas`[^manifest]
- **Dataset:** [Kertamų miško plotų leidimai ir atstumai iki LR sienos](../kertamu_plotu_leidimai.md) (`datasets/gov/lsd/aplinkosauga/kertamu_plotu_leidimai`)
- **Manifest CSV:** [datasets/gov/lsd/aplinkosauga/kertamu_plotu_leidimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/aplinkosauga/kertamu_plotu_leidimai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/aplinkosauga/kertamu_plotu_leidimai/MiskoKirtimoLeidimas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA unikalus identifikatorius | Valstybės duomenų agentūros sugeneruotas unikalios eilutės identifikatorius |
| `id` | `string` | — | `4` | `open` | — | ALIS LKMP ID | Aplinkos ministerijos Aplinkosaugos leidimų informacinės sistemos (ALIS), Leidimų kirsti mišką posistemio (LKMP) sugeneruotas įrašo identifikacinis numeris |
| `ploto_tipas` | `string` | — | `4` | `open` | — | Kertamo miško ploto tipas | — |
| `vyraujantys_medziai` | `string` | — | `4` | `open` | — | Vyraujančių medžių rūšies pavadinimas kertamame plote | — |
| `kirtimo_rusis` | `string` | — | `4` | `open` | — | Kirtimo rūšis | — |
| `atkurimo_budas` | `string` | — | `4` | `open` | — | Kertamo miško ploto atkūrimo būdas | — |
| `kertamas_plotas_ha` | `number` | — | `4` | `open` | — | Kertamo miško ploto dydis hektarais | — |
| `atstumas_iki_lr_sienos_km` | `number` | — | `4` | `open` | — | Atstumas iki LR sienos | Mažiausias atstumas tarp kertamo miško ploto geometrijos ir Lietuvos Respublikos sienos |
| `artmiausias_kaimynas` | `string` | — | `4` | `open` | — | Artimiausias kaimynas | Artimiausia kertamo ploto kaimyninės valstybės siena |
| `galioja_nuo` | `date` | `D` | `4` | `open` | — | Leidimo kirsti plotą galiojimo pradžios data | — |
| `galioja_iki` | `date` | `D` | `4` | `open` | — | Leidimo kirsti plotą galiojimo pabaigos data | — |
| `padalinys` | `string` | — | `4` | `open` | — | Valstybinės miškų urėdijos padalinio pavadinimas | — |
| `girininkija` | `string` | — | `4` | `open` | — | Girininkijos pavadinimas | — |
| `nuosavybes_forma` | `string` | — | `4` | `open` | — | Kertamo miško ploto nuosavybės forma | — |
| `kvartalas` | `string` | — | `4` | `open` | — | Kvartalo numeris(-iai) | — |
| `sklypas` | `string` | — | `4` | `open` | — | Sklypo numeris(-iai) | — |
| `kadastrinis_nr` | `string` | — | `4` | `open` | — | Kadastrinis numeris(-iai) | — |
| `geometrija_wgs_wkt` | `geometry(4326)` | — | `4` | `open` | — | Kertamo ploto WGS-84 geometrijos koordinatės WKT formatu | — |
| `geometrija_wgs_geojson` | `string` | — | `4` | `open` | — | Kertamo ploto WGS-84 geometrijos koordinatės GeoJSON formatu | — |
| `geometrija_lks_geojson` | `string` | — | `4` | `open` | — | Kertamo ploto LKS-94 geometrijos koordinatės GeoJSON formatu | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ploto_tipas` | `"biržė"` | — | — | Biržė | — |
| `ploto_tipas` | `"sklypas"` | — | — | Sklypas | — |
| `atkurimo_budas` | `"Miško žėlimas"` | — | — | Miško žėlimas | — |
| `atkurimo_budas` | `"Miško želdinimas"` | — | — | Miško želdinimas | — |
| `atkurimo_budas` | `"Neatkuriamas"` | — | — | Neatkuriamas | — |
| `atkurimo_budas` | `"Mišrus atkūrimo būdas (želdinimo ir žėlimo būdų derinys)"` | — | — | Mišrus atkūrimo būdas (želdinimo ir žėlimo būdų derinys) | — |
| `artmiausias_kaimynas` | `"Latvijos Respublika"` | — | — | Latvijos Respublika | — |
| `artmiausias_kaimynas` | `"Baltarusijos Respublika"` | — | — | Baltarusijos Respublika | — |
| `artmiausias_kaimynas` | `"Rusijos Federacija"` | — | — | Rusijos Federacija | — |
| `artmiausias_kaimynas` | `"Lenkijos Respublika"` | — | — | Lenkijos Respublika | — |
| `nuosavybes_forma` | `"valstybinė"` | — | — | Valstybinė | — |
| `nuosavybes_forma` | `"privati"` | — | — | Privati | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/aplinkosauga/kertamu_plotu_leidimai.csv
