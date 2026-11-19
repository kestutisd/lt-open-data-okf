---
type: Table
title: "ApmoketaSaskaita — Apmokėtos sąskaitos už LR apdraustųjų privalomuoju sveikatos draudimu gydymą Europos Sąjungos šalyje"
description: "Informacija apie PSDF išlaidas už LR apdraustiesiems PSD kitose Europos Sąjungos, Europos ekonominės erdvės valstybėse narėse, Šveicarijos Konfederacijoje ir Jungtinėje Karalystėje (toliau – ES šalys) suteiktas asmens sveikatos priežiūros paslaugas, įgyvendinant Europos..."
resource: "https://get.data.gov.lt/datasets/gov/vlk/apmoketos_saskaitos_es/ApmoketaSaskaita"
tags: [gov, vlk, apmoketasaskaita, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/apmoketos_saskaitos_es.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vlk/apmoketos_saskaitos_es.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1804/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/apmoketos_saskaitos_es"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# ApmoketaSaskaita — Apmokėtos sąskaitos už LR apdraustųjų privalomuoju sveikatos draudimu gydymą Europos Sąjungos šalyje

Informacija apie PSDF išlaidas už LR apdraustiesiems PSD kitose Europos Sąjungos, Europos ekonominės erdvės valstybėse narėse, Šveicarijos Konfederacijoje ir Jungtinėje Karalystėje (toliau – ES šalys) suteiktas asmens sveikatos priežiūros paslaugas, įgyvendinant Europos Parlamento ir Tarybos Reglamento (EB) Nr. 883/2004 ir Reglamento (EB) Nr. 987/2009 nuostatas[^manifest]

- **Model:** `datasets/gov/vlk/apmoketos_saskaitos_es/ApmoketaSaskaita`[^manifest]
- **Dataset:** [Apmokėtos sąskaitos už LR apdraustųjų privalomuoju sveikatos draudimu gydymą Europos Sąjungos šalyje](../apmoketos_saskaitos_es.md) (`datasets/gov/vlk/apmoketos_saskaitos_es`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/apmoketos_saskaitos_es.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/apmoketos_saskaitos_es.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/apmoketos_saskaitos_es/ApmoketaSaskaita` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Metai | Kalendoriniai metai, kuriais buvo apmokėtos sąskaitos |
| `salis` | `string` | — | `3` | `open` | — | Šalies pavadinimas | Šalies, kurioje, vadovaujantis socialinės apsaugos sistemas koordinuojančių reglamentų (EB) Nr. 883/2004 ir (EB) Nr. 987/2009 nuostatomis, Lietuvos Respublikos apdraustiesiems privalomuoju sveikatos draudimu (toliau – LR apdraustieji) buvo suteiktos medicinos paslaugos, t. y. Europos Sąjungos, Europos ekonominės erdvės valstybės narės, Šveicarijos Konfederacijos arba Jungtinės Karalystės (toliau – ES šalys), pavadinimas |
| `tipas` | `string` | — | `3` | `open` | — | Sąskaitos tipas | Apdraustojo teisę į išmokas natūra (t. y. asmens sveikatos priežiūros paslaugas) patvirtinantis dokumentas, kurio pagrindu sąskaita pateikta apmokėti |
| `saskaitu_sk` | `number` | `U` | `4` | `open` | — | Sąskaitų skaičius | PSDF biudžeto lėšomis apmokėtų atitinkamos ES šalies susižinojimo tarnybos pateiktų sąskaitų už LR apdraustiesiems toje ES šalyje suteiktas medicinos paslaugas, skaičius vienetais |
| `suma` | `number` | `U` | `2` | `open` | — | Suma | PSDF biudžeto lėšų suma, pervesta ES šalies susižinojimo tarnybai už LR apdraustiesiems atitinkamoje ES šalyje suteiktas medicinos paslaugas |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date, ref: "Y")"` | `type` | `4` | `open` | — | — | — |
| `suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/apmoketos_saskaitos_es.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/apmoketos_saskaitos_es.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/apmoketos_saskaitos_es (https://data.gov.lt/datasets/1804/)
