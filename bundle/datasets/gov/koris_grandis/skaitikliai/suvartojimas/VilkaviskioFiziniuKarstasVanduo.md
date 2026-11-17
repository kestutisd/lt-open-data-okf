---
type: Table
title: "VilkaviskioFiziniuKarstasVanduo — UAB „Vilkaviškio šilumos tinklų“ karšto vandens suvartojimas, už kurį moka fiziniai asmenys"
description: "Spinta table datasets/gov/koris_grandis/skaitikliai/suvartojimas/VilkaviskioFiziniuKarstasVanduo (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/koris_grandis/skaitikliai/suvartojimas/VilkaviskioFiziniuKarstasVanduo"
tags: [gov, koris_grandis, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/koris_grandis/skaitikliai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/koris_grandis/skaitikliai.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# VilkaviskioFiziniuKarstasVanduo — UAB „Vilkaviškio šilumos tinklų“ karšto vandens suvartojimas, už kurį moka fiziniai asmenys

- **Model:** `datasets/gov/koris_grandis/skaitikliai/suvartojimas/VilkaviskioFiziniuKarstasVanduo`[^manifest]
- **Dataset:** [Suvartojimas](../suvartojimas.md) (`datasets/gov/koris_grandis/skaitikliai/suvartojimas`)
- **Manifest CSV:** [datasets/gov/koris_grandis/skaitikliai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/koris_grandis/skaitikliai.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/koris_grandis/skaitikliai/suvartojimas/VilkaviskioFiziniuKarstasVanduo`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo unikalus identifikatorius | — |
| `pastato_id` | `string` | — | `4` | `open` | — | Namo, daugiabučio ar kito pastato identifikatorius | — |
| `pastato_ar_dalies_id` | `string` | — | `4` | `open` | — | Namo, buto arba kitos pastato dalies identifikatorius | — |
| `apskaitos_tasko_id` | `string` | — | `4` | `open` | — | Apskaitos taško (skaitiklio vietos) identifikatorius | — |
| `moketojo_asmens_kodas` | `string` | — | `4` | `open` | — | Sąskaitos mokėtojo asmens kodas | — |
| `moketojo_asmens_kodo_tinkamumas` | `string` | — | `4` | `open` | — | Sąskaitos mokėtojo asmens kodo tinkamumas | — |
| `apskaitos_menuo` | `date` | `M` | `4` | `open` | — | Apskaitos laikotarpio mėnuo | — |
| `deklaravimo_data` | `date` | `D` | `4` | `open` | — | Skaitiklio rodmenų deklaravimo data | — |
| `deklaruotas_suvartojimas_m3` | `number` | — | `4` | `open` | — | Deklaruotas skaitiklio rodmenų skirtumas nuo praėjusio apskaitos laikotarpio, m3 | — |
| `pateikimo_budas` | `string` | — | `4` | `open` | — | Skaitiklio rodmenų pateikimo būdas | — |
| `gyvenanciu_zmoniu_skaicius` | `number` | — | `4` | `open` | — | Name, bute ar kitoje pastato dalyje gyvenančių žmonių skaičius | — |
| `busena` | `string` | — | `4` | `open` | — | Būsena (Nedalyvauja – nesudalyvavo periodo uždaryme; Dalyvauja – sudalyvavo periodo uždaryme; Ištrintas) | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `moketojo_asmens_kodo_tinkamumas` | `"Tinkamas"` | — | — | Tinkamas | — |
| `moketojo_asmens_kodo_tinkamumas` | `"Tuščia reikšmė"` | — | — | Tuščia reikšmė | — |
| `moketojo_asmens_kodo_tinkamumas` | `"Netinkamas ilgis"` | — | — | Netinkamas ilgis | — |
| `moketojo_asmens_kodo_tinkamumas` | `"Yra ne skaitmenų"` | — | — | Yra ne skaitmenų | — |
| `moketojo_asmens_kodo_tinkamumas` | `"Netinkama gimimo data"` | — | — | Netinkama gimimo data | — |
| `moketojo_asmens_kodo_tinkamumas` | `"Netinkamas kontrolinis skaitmuo"` | — | — | Netinkamas kontrolinis skaitmuo | — |
| `moketojo_asmens_kodo_tinkamumas` | `"Netinkamas pirmas skaitmuo"` | — | — | Netinkamas pirmas skaitmuo | — |
| `pateikimo_budas` | `"Importuota"` | — | — | Importuota | — |
| `pateikimo_budas` | `"Įvesta"` | — | — | Įvesta | — |
| `pateikimo_budas` | `"Neįvesta"` | — | — | Neįvesta | — |
| `busena` | `"Nedalyvauja"` | — | — | Nedalyvauja | — |
| `busena` | `"Dalyvauja"` | — | — | Dalyvauja | — |
| `busena` | `"Ištrintas"` | — | — | Ištrintas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/koris_grandis/skaitikliai.csv
