---
type: Table
title: "IsrasytaSaskaita — Išrašytos sąskaitos ES šalims už tų šalių apdraustųjų sveikatos draudimu gydymą Lietuvoje"
description: "Informacija apie PSDF išlaidas kitų Europos Sąjungos, Europos ekonominės erdvės valstybių narių, Šveicarijos Konfederacijos ir Jungtinės Karalystės apdraustiesiems Lietuvos gydymo įstaigose suteiktoms asmens sveikatos priežiūros..."
resource: "https://get.data.gov.lt/datasets/gov/vlk/israsytos_saskaitos_es/IsrasytaSaskaita"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/israsytos_saskaitos_es.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/israsytos_saskaitos_es.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# IsrasytaSaskaita — Išrašytos sąskaitos ES šalims už tų šalių apdraustųjų sveikatos draudimu gydymą Lietuvoje

Informacija apie PSDF išlaidas kitų Europos Sąjungos, Europos ekonominės erdvės valstybių narių, Šveicarijos Konfederacijos ir Jungtinės Karalystės apdraustiesiems Lietuvos gydymo įstaigose suteiktoms asmens sveikatos priežiūros paslaugoms bei vaistinėse išduotiems kompensuojamiesiems vaistams ir MPP apmokėti

- **Model:** `datasets/gov/vlk/israsytos_saskaitos_es/IsrasytaSaskaita`[^manifest]
- **Dataset:** [datasets/gov/vlk/israsytos_saskaitos_es](../israsytos_saskaitos_es.md) (`datasets/gov/vlk/israsytos_saskaitos_es`)
- **Manifest CSV:** [datasets/gov/vlk/israsytos_saskaitos_es.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/israsytos_saskaitos_es.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/israsytos_saskaitos_es/IsrasytaSaskaita`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `salies_kodas` | `string` | — | `4` | `open` | — | Šalies kodas | ES šalies kodas pagal ISO 3166-1 A2 |
| `israsyta` | `number` | — | `2` | `open` | — | Išrašyta suma | Atitinkamos ES šalies susižinojimo tarnybai už tos ES šalies apdraustiesiems Lietuvoje suteiktas medicinos paslaugas išsiųstose sąskaitose nurodyta mokėtina suma eurais |
| `apmoketa` | `number` | — | `2` | `open` | — | Apmokėta suma | Atitinkamos ES šalies susižinojimo tarnybos už tos ES šalies apdraustiesiems Lietuvoje suteiktas medicinos paslaugas apmokėta suma eurais |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date, ref: "Y")` | `type` | `4` | `open` | — | — | — |
| `israsyta` | `update(type: "money, ref: "EUR")"` | `type` | `4` | `open` | — | — | — |
| `apmoketa` | `update(type: "money, ref: "EUR")"` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/israsytos_saskaitos_es.csv
