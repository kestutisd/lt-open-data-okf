---
type: Table
title: "PasipriesinimoDalyvis — Pasipriešinimo okupacijoms dalyviai"
description: "Rinkinyje pateikiami duomenys apie asmenis, kuriems buvo suteiktas pasipriešinimo okupaciniams režimams dalyvio statusas pagal Lietuvos Respublikos Lietuvos gyventojų genocido ir rezistencijos tyrimo centro įstatymo 5 straipsnio 3, 5 ir 20 punktus."
resource: "https://get.data.gov.lt/datasets/gov/lggrtc/pasipriesinimo_okupacijoms_dalyviai/PasipriesinimoDalyvis"
tags: [gov, lggrtc, pasipriesinimodalyvis, deployed, level-4, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lggrtc/pasipriesinimo_okupacijoms_dalyviai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lggrtc/pasipriesinimo_okupacijoms_dalyviai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3873/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lggrtc/pasipriesinimo_okupacijoms_dalyviai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PasipriesinimoDalyvis — Pasipriešinimo okupacijoms dalyviai

Rinkinyje pateikiami duomenys apie asmenis, kuriems buvo suteiktas pasipriešinimo okupaciniams režimams dalyvio statusas pagal Lietuvos Respublikos Lietuvos gyventojų genocido ir rezistencijos tyrimo centro įstatymo 5 straipsnio 3, 5 ir 20 punktus. Taip pat pateikiama informacija apie valstybės apdovanojimus, suteiktus šiems asmenims vadovaujantis Lietuvos Respublikos pasipriešinimo 1940–1990 metų okupacijoms dalyvių teisinio statuso pripažinimo ir karių savanorių karinių laipsnių bei apdovanojimų prilyginimo įstatymo 4 straipsniu. Rinkinį sudaro duomenys apie asmens gimimo metus, duomenų pateikėjo savivaldybę, asmeniui suteiktą teisinį statusą, jo kodą, pavadinimą ir aprašymą, taip pat įsakymo datą, kurią buvo suteiktas šis statusas, ir išduoto pažymėjimo numerį. Ši informacija leidžia nustatyti, kokiu pagrindu ir kada asmeniui buvo suteiktas pasipriešinimo okupaciniams režimams dalyvio statusas, bei kokiu dokumentu tai patvirtinta. Duomenų teikėjas – Lietuvos gyventojų genocido ir rezistencijos tyrimo centras. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/lggrtc/pasipriesinimo_okupacijoms_dalyviai/PasipriesinimoDalyvis`[^manifest]
- **Dataset:** [Pasipriešinimo okupacijoms dalyviai](../pasipriesinimo_okupacijoms_dalyviai.md) (`datasets/gov/lggrtc/pasipriesinimo_okupacijoms_dalyviai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lggrtc/pasipriesinimo_okupacijoms_dalyviai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lggrtc/pasipriesinimo_okupacijoms_dalyviai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lggrtc/pasipriesinimo_okupacijoms_dalyviai/PasipriesinimoDalyvis` (`deployed`)[^manifest]
- **Provider:** `lggrtc` — Lietuvos gyventojų genocido ir rezistencijos tyrimo centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_2`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Asmens gimimo metai | — |
| `pateikejo_savivaldybe` | `string` | — | `4` | `open` | — | Duomenų pateikėjo savivaldybė | — |
| `suteiktas_statusas` | `string` | — | `4` | `open` | — | Asmeniui suteiktas teisinis statusas | — |
| `teisinis_statusas_kodas` | `string` | — | `4` | `open` | — | Teisinio statuso kodas | — |
| `teisinis_statusas_pavadinimas` | `string` | — | `4` | `open` | — | Teisinio statuso pavadinimas | — |
| `teisinis_statusas_aprasymas` | `string` | — | `4` | `open` | — | Teisinio statuso aprašymas | — |
| `isakymo_data` | `date` | `D` | `4` | `open` | — | Įsakymo data | — |
| `pazymejimo_numeris` | `string` | — | `4` | `open` | — | Pažymėjimo numeris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lggrtc/pasipriesinimo_okupacijoms_dalyviai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lggrtc/pasipriesinimo_okupacijoms_dalyviai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lggrtc/pasipriesinimo_okupacijoms_dalyviai (https://data.gov.lt/datasets/3873/)
