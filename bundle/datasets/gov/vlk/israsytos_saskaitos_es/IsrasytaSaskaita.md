---
type: Table
title: "IsrasytaSaskaita — Išrašytos sąskaitos ES šalims už tų šalių apdraustųjų sveikatos draudimu gydymą Lietuvoje"
description: "Informacija apie PSDF išlaidas kitų Europos Sąjungos, Europos ekonominės erdvės valstybių narių, Šveicarijos Konfederacijos ir Jungtinės Karalystės apdraustiesiems Lietuvos gydymo įstaigose suteiktoms asmens sveikatos priežiūros paslaugoms bei vaistinėse išduotiems..."
resource: "https://get.data.gov.lt/datasets/gov/vlk/israsytos_saskaitos_es/IsrasytaSaskaita"
tags: [gov, vlk, israsytasaskaita, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/israsytos_saskaitos_es.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/vlk/israsytos_saskaitos_es.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1805/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/israsytos_saskaitos_es"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# IsrasytaSaskaita — Išrašytos sąskaitos ES šalims už tų šalių apdraustųjų sveikatos draudimu gydymą Lietuvoje

Informacija apie PSDF išlaidas kitų Europos Sąjungos, Europos ekonominės erdvės valstybių narių, Šveicarijos Konfederacijos ir Jungtinės Karalystės apdraustiesiems Lietuvos gydymo įstaigose suteiktoms asmens sveikatos priežiūros paslaugoms bei vaistinėse išduotiems kompensuojamiesiems vaistams ir MPP apmokėti[^manifest]

- **Model:** `datasets/gov/vlk/israsytos_saskaitos_es/IsrasytaSaskaita`[^manifest]
- **Dataset:** [Išrašytos sąskaitos ES šalims už tų šalių apdraustųjų sveikatos draudimu gydymą Lietuvoje](../israsytos_saskaitos_es.md) (`datasets/gov/vlk/israsytos_saskaitos_es`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/israsytos_saskaitos_es.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/israsytos_saskaitos_es.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/israsytos_saskaitos_es/IsrasytaSaskaita` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/israsytos_saskaitos_es.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/israsytos_saskaitos_es.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/israsytos_saskaitos_es (https://data.gov.lt/datasets/1805/)
