---
type: Table
title: "KetPazeidejas — Kelių eismo taisyklių pažeidimai ir pažeidėjai"
description: "Administracinių nusižengimų registro (ANR) duomenų neagreguota lentelė (mikroduomenys), kurioje įtraukti tik tie nusižengimai kurių sudėtį nustatantys Administracinių nusižengimų kodekso (ANK) straipsniai yra susiję su Kelių eismo taisyklių (KET) pažeidimais (straipsniai..."
resource: "https://get.data.gov.lt/datasets/gov/ird/anr/KetPazeidejas"
tags: [gov, ird, ketpazeidejas, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/anr.csv#L19"
    title: "atviriduomenys/manifest — datasets/gov/ird/anr.csv#L19"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2558/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ird/anr"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# KetPazeidejas — Kelių eismo taisyklių pažeidimai ir pažeidėjai

Administracinių nusižengimų registro (ANR) duomenų neagreguota lentelė (mikroduomenys), kurioje įtraukti tik tie nusižengimai kurių sudėtį nustatantys Administracinių nusižengimų kodekso (ANK) straipsniai yra susiję su Kelių eismo taisyklių (KET) pažeidimais (straipsniai 414-433, 439-441, 463). Viena eilutė yra vieno administracinio nusižengimo vieno straipsnio viena dalis, tad vienas nusižengimas gali kartotis daugelyje eilučių. Kievienam nusižengimui yra priskirtas pažeidėjas (tačiau būna nemažai atvejų, kuomet pažeidėjo duomenų nėra). Pažeidėjo duomenys nėra laikytini griežtai patikimais. Dėl techninių klausimų kreiptis į atverimas@stat.gov.lt[^manifest]

- **Model:** `datasets/gov/ird/anr/KetPazeidejas`[^manifest]
- **Dataset:** [Administracinių nusižengimų registras](../anr.md) (`datasets/gov/ird/anr`)[^manifest]
- **Manifest CSV:** [datasets/gov/ird/anr.csv#L19](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/anr.csv#L19)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/anr/KetPazeidejas` (`deployed`)[^manifest]
- **Provider:** `ird` — Informatikos ir ryšių departamentas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/anr.csv#L19 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/anr.csv#L19)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ird/anr (https://data.gov.lt/datasets/2558/)
