---
type: Table
title: "KelionesAtvykBeNakv2021 — Atvykusių turistų kelionės be nakvynės 2021 m."
description: "Spinta table datasets/gov/lsd/turizmas/atvyksta/KelionesAtvykBeNakv2021 (32 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/turizmas/atvyksta/KelionesAtvykBeNakv2021"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/turizmas/atvyksta.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/turizmas/atvyksta.csv#L119"
    last_modified: "2026-11-11T14:39:20Z"
---

# KelionesAtvykBeNakv2021 — Atvykusių turistų kelionės be nakvynės 2021 m.

- **Model:** `datasets/gov/lsd/turizmas/atvyksta/KelionesAtvykBeNakv2021`[^manifest]
- **Dataset:** [Atvykstamojo turizmo statistiniai tyrimai](../atvyksta.md) (`datasets/gov/lsd/turizmas/atvyksta`)
- **Manifest CSV:** [datasets/gov/lsd/turizmas/atvyksta.csv#L119](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/turizmas/atvyksta.csv#L119)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/turizmas/atvyksta/KelionesAtvykBeNakv2021`
- **Primary Key (`ref`):** `id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Respondento ID kodas | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | Respondento lytis |
| `amzius` | `string` | — | `4` | `open` | — | Amžiaus grupė | Respondento amžiaus grupė |
| `gyv_salis` | `string` | — | `3` | `open` | — | Gyvenamoji šalis | Respondento nuolatinė gyvenamoji šalis arba jų grupė |
| `gyv_salies_kodas` | `string` | — | `2` | `open` | — | Gyvenamosios šalies kodas | Respondento nuolatinė gyvenamoji šalis (dviraidis kodas) arba jų grupė (tuščia) |
| `apkl_vieta` | `string` | — | `3` | `open` | — | Apklausos atlikimo vieta | — |
| `ketvirtis` | `string` | — | `3` | `open` | — | Metų ketvirtis | — |
| `tikslas` | `string` | — | `4` | `open` | — | Kelionės tikslas | — |
| `transporto_priemone` | `string` | — | `4` | `open` | — | Transporto priemonė | Pagrindinė transporto priemonė, kuria keliavo |
| `trukme` | `integer` | `h` | `4` | `open` | — | Kiek valandų praleido Lietuvoje | — |
| `pirmakart` | `integer` | `bool` | `4` | `open` | — | Ar pirmąkart lankėsi Lietuvoje | — |
| `islaid_pries` | `integer` | — | `2` | `open` | — | Išlaidos prieš kelionę | Visos išlaidos čia pateiktos vienam asmeniui (respondento nurodytos išlaidos padalintos iš asmenų skaičiaus); apima paslaugų paketą, vizą ir kitas išlaidas prieš kelionę |
| `zmoniu_sk_pries` | `integer` | `U` | `4` | `open` | — | Žmonių skaičius, kuriam nurodytos išlaidos prieš kelionę | — |
| `islaid_paketui` | `integer` | — | `2` | `open` | — | Išlaidos paslaugų paketui | Nurodyta vidutinė kaina vienai šaliai, jei paslaugų paketas apima kelias šalis |
| `islaid_vizai` | `integer` | — | `2` | `open` | — | Išlaidos vizai ir kitiems kelionės dokumentams | — |
| `islaid_ktpries` | `integer` | — | `2` | `open` | — | Kitos išlaidos prieš kelionę | Apima bilietus į renginius ir kt., išskyrus kelionės bilietus |
| `saliu_pakete` | `integer` | `U` | `4` | `open` | — | Kiek šalių apėmė paslaugų paketas | — |
| `islaid_lt` | `integer` | — | `2` | `open` | — | Išlaidos Lietuvoje | Visos išlaidos čia pateiktos vienam asmeniui (respondento nurodytos išlaidos padalintos iš asmenų skaičiaus) |
| `zmoniu_sk` | `integer` | `U` | `4` | `open` | — | Žmonių skaičius, kuriam nurodytos išlaidos Lietuvoje | — |
| `islaid_maistui` | `integer` | — | `2` | `open` | — | Išlaidos maistui | Išlaidos maistui, įskaitant maistą restoranuose ir parduotuvėse |
| `islaid_restoranuose` | `integer` | — | `2` | `open` | — | Išlaidos maistui restoranuose | Įskaitant kavines, barus ir kt. |
| `islaid_parduotuvese` | `integer` | — | `2` | `open` | — | Išlaidos maistui parduotuvėse | — |
| `islaid_transportui` | `integer` | — | `2` | `open` | — | Išlaidos transportui Lietuvoje | Išlaidos apima degalus, transporto nuomą, remontą, viešąjį transportą, bet ne degalus, pirktus parduoti |
| `islaid_degalams` | `integer` | — | `2` | `open` | — | Išlaidos degalams | — |
| `islaid_trnuomai` | `integer` | — | `2` | `open` | — | Išlaidos transporto nuomai | — |
| `islaid_trremontui` | `integer` | — | `2` | `open` | — | Išlaidos transporto remontui | — |
| `islaid_viesajamtr` | `integer` | — | `2` | `open` | — | Išlaidos viešajam transportui ir taksi | — |
| `islaid_laisvalaikiui` | `integer` | — | `2` | `open` | — | Išlaidos laisvalaikiui ir kultūrai | — |
| `islaid_pirkiniams` | `integer` | — | `2` | `open` | — | Išlaidos pirkiniams | — |
| `islaid_pirkmasinai` | `integer` | — | `2` | `open` | — | Išlaidos pirktam automobiliui | Išlaidos neįtraukia automobilių, pirktų perparduoti |
| `islaid_kt` | `integer` | — | `2` | `open` | — | Kitos išlaidos | — |
| `islaid_viso` | `integer` | — | `2` | `open` | — | Viso išlaidų | Visos išlaidos čia pateiktos vienam asmeniui (respondento nurodytos išlaidos padalintos iš asmenų skaičiaus) |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"1"` | — | — | Vyras | — |
| `lytis` | `"2"` | — | — | Moteris | — |
| `amzius` | `"1"` | — | — | 15-24 | — |
| `amzius` | `"2"` | — | — | 25-34 | — |
| `amzius` | `"3"` | — | — | 35-44 | — |
| `amzius` | `"4"` | — | — | 45-54 | — |
| `amzius` | `"5"` | — | — | 55-64 | — |
| `amzius` | `"6"` | — | — | 65+ | — |
| `tikslas` | `"1"` | — | — | Laisvalaikis | — |
| `tikslas` | `"26"` | — | — | Verslas | — |
| `tikslas` | `"3"` | — | — | Draugų ir giminių lankymas | — |
| `tikslas` | `"4"` | — | — | Sveikatinimo tikslai | — |
| `tikslas` | `"5"` | — | — | Pirkiniai | — |
| `tikslas` | `"7"` | — | — | Kita | — |
| `transporto_priemone` | `"1"` | — | — | Lengvasis automobilis | — |
| `transporto_priemone` | `"2"` | — | — | Maršrutinis autobusas | — |
| `transporto_priemone` | `"3"` | — | — | Nereguliarių reisų autobusas | — |
| `transporto_priemone` | `"4"` | — | — | Traukinys | — |
| `transporto_priemone` | `"5"` | — | — | Lėktuvas | — |
| `transporto_priemone` | `"6"` | — | — | Laivas, keltas | — |
| `transporto_priemone` | `"78"` | — | — | Kita | — |
| `pirmakart` | `1` | — | — | Taip | — |
| `pirmakart` | `0` | — | — | Ne | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `islaid_pries` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_paketui` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_vizai` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_ktpries` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_lt` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_maistui` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_restoranuose` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_parduotuvese` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_transportui` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_degalams` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_trnuomai` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_trremontui` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_viesajamtr` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_laisvalaikiui` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_pirkiniams` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_pirkmasinai` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_kt` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_viso` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/turizmas/atvyksta.csv
