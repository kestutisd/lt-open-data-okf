---
type: Table
title: "Koeficientai — DRG koeficientai"
description: "Giminingų diagnozių grupių paros/dienos gydymo kainų koeficientai"
resource: "https://get.data.gov.lt/datasets/gov/vlk/drg/Koeficientai"
tags: [gov, vlk, koeficientai, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg.csv#L27"
    title: "atviriduomenys/manifest — datasets/gov/vlk/drg.csv#L27"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1384/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/drg"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Koeficientai — DRG koeficientai

Giminingų diagnozių grupių paros/dienos gydymo kainų koeficientai[^manifest]

- **Model:** `datasets/gov/vlk/drg/Koeficientai`[^manifest]
- **Dataset:** [DRG sąrašas](../drg.md) (`datasets/gov/vlk/drg`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/drg.csv#L27](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg.csv#L27)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/drg/Koeficientai` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `grupe` | `ref` | [Grupe](Grupe.md) (`level=4 UUID`: `grupe._id`) | `4` | `open` | — | Nuoroda į DRG grupes | — |
| `nuo` | `date` | `D` | `4` | `open` | — | DRG koeficientai galioja nuo | Giminingų diagnozių grupių kainos koeficiento galiojimo pradžios data |
| `vienos_dienos` | `number` | — | `4` | `open` | — | Dienos DRG koeficientai | Giminingų diagnozių grupių dienos gydymo kainos koeficientas. Dienos gydymo kainos koeficientas – tai gydymo atvejo kainos koeficientas, taikomas tada, kai pacientas atvyksta į asmens sveikatos priežiūros įstaigą ir išvyksta iš jos tą pačią dieną. Taip pat šis koeficientas taikomas visais gydymo atvejais, kai teikiamos dienos chirurgijos II paslaugų grupei priskiriamos paslaugos |
| `iki` | `date` | `D` | `4` | `open` | — | DRG koeficientai galioja iki | Giminingų diagnozių grupių kainos koeficiento galiojimo pabaigos data |
| `vienos_paros` | `number` | — | `4` | `open` | — | Vienos paros DRG koeficientai | Giminingų diagnozių grupių paros gydymo kainos koeficientas. Paros gydymo kainos koeficientas – tai gydymo atvejo kainos koeficientas, taikomas tada, kai pacientas vieną dieną atvyksta į asmens sveikatos priežiūros įstaigą, o kitą dieną – išvyksta. Taip pat šis koeficientas taikomas visais gydymo atvejais, kai teikiamos dienos chirurgijos III paslaugų grupei priskiriamos paslaugos |
| `lovadienio_min` | `number` | — | `4` | `open` | — | Vieno lovadienio DRG koeficientas, kai gydymo trukmė trumpesnė nei minimali | Lovadienio kainos koeficientas – tai koeficientas, taikomas lovadienio kainai nustatyti, kai gydymo trukmė trumpesnė nei minimali |
| `vidutinio_atvejo` | `number` | — | `4` | `open` | — | Vidutinės trukmės atvejo DRG koeficientai | Gydymo atvejo (gydymo etapo) koeficientas - tai koeficientas, taikomas gydymo atvejo kainai nustatyti, kai gydymo trukmė ilgesnė arba lygi minimaliai ir trumpesnė arba lygi maksimaliai. Taip pat šis koeficientas taikomas visais gydymo atvejais, kai teikiamos dienos chirurgijos IV–VI paslaugų grupėms priskiriamos paslaugos |
| `lovadienio_max` | `number` | — | `4` | `open` | — | Vieno lovadienio DRG koeficientas, kai gydymo trukmė ilgesnė nei maksimali | Lovadienio kainos koeficientas – tai koeficientas, taikomas lovadienio kainai nustatyti, kai gydymo trukmė ilgesnė nei minimali |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/drg.csv#L27 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg.csv#L27)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/drg (https://data.gov.lt/datasets/1384/)
