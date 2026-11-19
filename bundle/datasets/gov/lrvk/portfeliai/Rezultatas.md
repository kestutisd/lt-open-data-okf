---
type: Table
title: "Rezultatas — Lietuvos Respublikos Vyriausybės strateginio projektų portfelio rezultatai"
description: "Lentelės objektas - projekto rezultatas."
resource: "https://get.data.gov.lt/datasets/gov/lrvk/portfeliai/Rezultatas"
tags: [gov, lrvk, rezultatas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrvk/portfeliai.csv#L43"
    title: "atviriduomenys/manifest — datasets/gov/lrvk/portfeliai.csv#L43"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1550/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lrvk/portfeliai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Rezultatas — Lietuvos Respublikos Vyriausybės strateginio projektų portfelio rezultatai

Lentelės objektas - projekto rezultatas. Per lauką "projekto_id" jungiasi su kitomis rinkinio lentelėmis.[^manifest]

- **Model:** `datasets/gov/lrvk/portfeliai/Rezultatas`[^manifest]
- **Dataset:** [Lietuvos Respublikos Vyriausybės strateginio projektų portfelio valdymo duomenys](../portfeliai.md) (`datasets/gov/lrvk/portfeliai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lrvk/portfeliai.csv#L43](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrvk/portfeliai.csv#L43)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrvk/portfeliai/Rezultatas` (`deployed`)[^manifest]
- **Provider:** `lrvk` — Lietuvos Respublikos Vyriausybės Kanceliarija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `projekto_id` | `string` | — | `4` | `open` | — | Projekto identifikacinis numeris | — |
| `projekto_pavadinimas` | `string` | — | `4` | `open` | — | Projekto pavadinimas | — |
| `institucija` | `string` | — | `4` | `open` | — | Projektą vykdanti institucija | — |
| `rezultatas` | `string` | — | `4` | `open` | — | Projekto rezultatas | — |
| `reikalavimai_rezultatui` | `string` | — | `4` | `open` | — | Reikalavimai projekto rezultatui | — |
| `matavimo_vnt` | `string` | — | `4` | `open` | — | Rezultato (gairės) matavimo vienetas | — |
| `planuojamas_rezultato_rodiklis` | `string` | — | `4` | `open` | — | Siekiama projekto rezultato (gairės) rodiklio reikšme | — |
| `faktinis_rezultato_rodiklis` | `number` | — | `4` | `open` | — | Faktinė rezultato (gairės) rodiklio reikšmė | — |
| `planuojama_pasiekimo_data` | `date` | `D` | `4` | `open` | — | Planuojama projekto rodiklio pasiekimo data | — |
| `faktine_pasiekimo_data` | `date` | `D` | `4` | `open` | — | Faktinė projekto rodiklio pasiekimo data | — |
| `pasiektas_rezultatas` | `string` | — | `4` | `open` | — | Pasiekto rezultato (gairės) aprašymas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrvk/portfeliai.csv#L43 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrvk/portfeliai.csv#L43)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lrvk/portfeliai (https://data.gov.lt/datasets/1550/)
