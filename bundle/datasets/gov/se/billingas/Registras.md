---
type: Table
title: "Registras — Tiekiamų paslaugų registras"
description: "Šiaulių energijos teikiamų paslaugų ir suvartotų kiekių registras."
resource: "https://get.data.gov.lt/datasets/gov/se/billingas/Registras"
tags: [gov, se, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/se/registras.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/se/registras.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Registras — Tiekiamų paslaugų registras

Šiaulių energijos teikiamų paslaugų ir suvartotų kiekių registras. Rinkinys apima Šiaulių energijos teikiamų paslaugų teritoriją, duomenys nuo 2017 metų iki dabar. Rinkinyje pateikiama paslaugos pavadinimas ir kategorija, kiekis ir matavimo vienetas, periodo mėnuo ir patalpos ID (referuoja į lentelę Patalpos).

- **Model:** `datasets/gov/se/billingas/Registras`[^manifest]
- **Dataset:** [Sistema skirta AB Šiaulių energija klientų duomenų valdymui, karšto vandens bei šildymo tiekimo paslaugų apskaičiavimui, sąskaitų leidimui ir skolų valdymui.](../billingas.md) (`datasets/gov/se/billingas`)
- **Manifest CSV:** [datasets/gov/se/registras.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/se/registras.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/se/billingas/Registras`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identitfikatorius | — |
| `patalpos_id` | `string` | — | `4` | `open` | — | Patalpos unikalus identifikatorius | — |
| `periodo_menuo` | `date` | `M` | `4` | `open` | — | Suteiktų paslaugų laikotarpio mėnuo | — |
| `kiekis` | `number` | — | `4` | `open` | — | Suteiktų paslaugų kiekis | — |
| `matavimo_vnt` | `string` | — | `4` | `open` | — | Suteiktų paslaugų kiekio matavimo vienetas | — |
| `pirkejo_kodas` | `string` | — | `4` | `open` | — | Pirkėjo kodas | — |
| `juridinis` | `string` | — | `4` | `open` | — | Požymis ar juridinis pirkėjas | — |
| `paslaugos_pavadinimas` | `string` | — | `4` | `open` | — | Paslaugos pavadinimas | — |
| `paslaugos_kategorija` | `string` | — | `4` | `open` | — | Paslaugos kategorija | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/se/registras.csv
