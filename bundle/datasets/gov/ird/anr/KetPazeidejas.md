---
type: Table
title: "KetPazeidejas — Kelių eismo taisyklių pažeidimai ir pažeidėjai"
description: "Administracinių nusižengimų registro (ANR) duomenų neagreguota lentelė (mikroduomenys), kurioje įtraukti tik tie nusižengimai kurių sudėtį nustatantys Administracinių nusižengimų kodekso (ANK) straipsniai yra susiję su Kelių eismo..."
resource: "https://get.data.gov.lt/datasets/gov/ird/anr/KetPazeidejas"
tags: [gov, ird, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ird/anr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/anr.csv#L19"
    last_modified: "2026-11-11T14:39:20Z"
---

# KetPazeidejas — Kelių eismo taisyklių pažeidimai ir pažeidėjai

Administracinių nusižengimų registro (ANR) duomenų neagreguota lentelė (mikroduomenys), kurioje įtraukti tik tie nusižengimai kurių sudėtį nustatantys Administracinių nusižengimų kodekso (ANK) straipsniai yra susiję su Kelių eismo taisyklių (KET) pažeidimais (straipsniai 414-433, 439-441, 463). Viena eilutė yra vieno administracinio nusižengimo vieno straipsnio viena dalis, tad vienas nusižengimas gali kartotis daugelyje eilučių. Kievienam nusižengimui yra priskirtas pažeidėjas (tačiau būna nemažai atvejų, kuomet pažeidėjo duomenų nėra). Pažeidėjo duomenys nėra laikytini griežtai patikimais.

- **Model:** `datasets/gov/ird/anr/KetPazeidejas`[^manifest]
- **Dataset:** [Administracinių nusižengimų registras](../anr.md) (`datasets/gov/ird/anr`)
- **Manifest CSV:** [datasets/gov/ird/anr.csv#L19](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/anr.csv#L19)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/anr/KetPazeidejas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Identifikatorius | Eilutes identifikatorius |
| `anr_id` | `string` | — | `4` | `open` | — | Administracinio nusižengimo unikalus identifikatorius | Skirtas jungimui su kitom lentelėm taip pat konkretaus nusižengimo sudėties (straipsnių) radimui keliose eilutėse Administracinio nusižengimo unikalus identifikatorius, skirtas jungimui su kitom lentelėm, taip pat konkretaus nusižengimo sudėties (straipsnių) radimui keliose eilutėse |
| `anr_uzregistruota` | `date` | `M` | `4` | `open` | — | Administracinio nusižengimo registravimo registre data | — |
| `amzius` | `integer` | `yr` | `4` | `open` | — | Pažeidėjo amžius | Asmens amžius nusižengimo registravimo metu. Gali būti nežinomas. |
| `lytis` | `string` | — | `3` | `open` | — | Pažeidėjo lytis | Gali būti nežinoma |
| `pilietybe` | `string` | — | `4` | `open` | — | Pažeidėjo pilietybė | Gali būti nežinoma, gali būti dviguba ir pan. |
| `ank_straipsnis` | `string` | — | `4` | `open` | — | Pagrindinis ANK straipsnis | — |
| `ank_straipsnio_dalis` | `string` | — | `4` | `open` | — | Pagrindinio ANK straipsnio dalis | — |
| `ank_straipsnis_pav` | `string` | — | `4` | `open` | — | Pagrindinio ANK straipsnio pavadinimas | — |
| `ank_straipsnio_dalis_pav` | `string` | — | `4` | `open` | — | Pagrindinio ANK straipsnio dalies pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/anr.csv
