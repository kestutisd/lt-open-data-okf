---
type: Table
title: "VilkaviskioPastatas — UAB „Vilkaviškio šilumos tinklų“ aptarnaujami pastatai"
description: "Pastatų nekintanti informacija"
resource: "https://get.data.gov.lt/datasets/gov/koris_grandis/skaitikliai/pastatai/VilkaviskioPastatas"
tags: [gov, koris_grandis, vilkaviskiopastatas, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/koris_grandis/skaitikliai.csv#L103"
    title: "atviriduomenys/manifest — datasets/gov/koris_grandis/skaitikliai.csv#L103"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3969/"
    title: "data.gov.lt DCAT-AP — datasets/gov/koris_grandis/skaitikliai/pastatai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# VilkaviskioPastatas — UAB „Vilkaviškio šilumos tinklų“ aptarnaujami pastatai

**Dataset Context:** Pastatų nekintanti informacija[^manifest]

- **Model:** `datasets/gov/koris_grandis/skaitikliai/pastatai/VilkaviskioPastatas`[^manifest]
- **Dataset:** [Pastatai](../pastatai.md) (`datasets/gov/koris_grandis/skaitikliai/pastatai`)[^manifest]
- **Manifest CSV:** [datasets/gov/koris_grandis/skaitikliai.csv#L103](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/koris_grandis/skaitikliai.csv#L103)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/koris_grandis/skaitikliai/pastatai/VilkaviskioPastatas` (`deployed`)[^manifest]
- **Provider:** `koris_grandis` — Komunaliniai suvartojimo įrašai sistemoje „GRANDIS“ *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `pastato_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pastato_id` | `string` | — | `4` | `open` | — | Namo, daugiabučio ar kito pastato identifikatorius | — |
| `pastato_tipas` | `string` | — | `4` | `open` | — | Pastato tipo pavadinimas | — |
| `apskaitos_tasku_daug` | `boolean` | — | `4` | `open` | — | Požymis, nurodantis, ar apskaitos taškų pastate yra bent 4 (TRUE – taip, FALSE – ne). Jei pastate yra mažiausiai 4 apskaitos taškai, pastato koordinatės paliekamos tikslios, o jei apskaitos taškų yra mažiau nei 4, tuomet pastato koordinatės paslenkamos iki 1 km nuo tikrosios padėties. | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Pastato vietos platuma pagal pasaulinės geodezinės sistemos (WGS-84) koordinačių sistemą. Jei apskaitos taškų 3 arba mažiau, koordinatės gali būti pastumtos iki maždaug 1 km. | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Pastato vietos ilguma pagal pasaulinės geodezinės sistemos (WGS-84) koordinačių sistemą. Jei apskaitos taškų 3 arba mažiau, koordinatės gali būti pastumtos iki maždaug 1 km. | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | Pastato vietos X koordinatė pagal Lietuvos koordinačių sistemą (LKS-94). Jei apskaitos taškų 3 arba mažiau, koordinatės gali būti pastumtos iki maždaug 1 km. | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Pastato vietos Y koordinatė pagal Lietuvos koordinačių sistemą (LKS-94). Jei apskaitos taškų 3 arba mažiau, koordinatės gali būti pastumtos iki maždaug 1 km. | — |
| `geometrija` | `geometry(point, 3346)` | — | `4` | `open` | — | Pastato vietos X ir Y koordinatės pagal Lietuvos koordinačių sistemą (LKS-94) WKT formatu. Jei apskaitos taškų 3 arba mažiau, koordinatės gali būti pastumtos iki maždaug 1 km. | — |
| `pastatymo_metai` | `date` | `Y` | `4` | `open` | — | Pastato pastatymo metai, paskutinį metų skaičių pakeičiant 0 | — |
| `busena` | `string` | — | `4` | `open` | — | Būsena (Dalyvauja – sudalyvavo periodo uždaryme; Ištrintas) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pastato_tipas` | `"BŪ namas"` | — | — | BŪ namas | — |
| `pastato_tipas` | `"Negyvenamos patalpos"` | — | — | Negyvenamos patalpos | — |
| `pastato_tipas` | `"Privatus namas"` | — | — | Privatus namas | — |
| `pastato_tipas` | `"Bendrija"` | — | — | Bendrija | — |
| `pastato_tipas` | `"Bendrabutis"` | — | — | Bendrabutis | — |
| `busena` | `"Dalyvauja"` | — | — | Dalyvauja | — |
| `busena` | `"Ištrintas"` | — | — | Ištrintas | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/koris_grandis/skaitikliai.csv#L103 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/koris_grandis/skaitikliai.csv#L103)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/koris_grandis/skaitikliai/pastatai (https://data.gov.lt/datasets/3969/)
