---
type: Table
title: "Vietovardis — Vietovardžių duomenys"
description: "Valstybinės lietuvių kalbos komisijos (VLKK) pasvetainė „Pasaulio vietovardžiai“ kaupia sulietuvintus pasaulio objektų vietovardžius."
resource: "https://get.data.gov.lt/datasets/gov/vlkk/pv/Vietovardis"
tags: [gov, vlkk, vietovardis, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlkk/pv.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vlkk/pv.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2703/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlkk/pv"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Vietovardis — Vietovardžių duomenys

Valstybinės lietuvių kalbos komisijos (VLKK) pasvetainė „Pasaulio vietovardžiai“ kaupia sulietuvintus pasaulio objektų vietovardžius. Duomenų pagrindas sudarytas iš Mokslo ir enciklopedijų leidybos centro (MELC) parengto ir išleisto žodyno. Duomenys kaupiami nuo 2014 m. ir yra atnaujinami iki šiol. Duomenys apima objekto identifikatorių, apjungiantį jo pavadinimus originalo ir lietuvių kalbomis, pavadinimus su ir be kirčio ženklų, požymį, ar pavadinimas sulietuvintas, objekto rūšį, šalį, žemyną, lokalizaciją, skirtą nurodyti objekto vietovę bei paieškų skaičių, anksčiausią ir vėliausią datas.[^manifest]

- **Model:** `datasets/gov/vlkk/pv/Vietovardis`[^manifest]
- **Dataset:** [Vietovardžių duomenys](../pv.md) (`datasets/gov/vlkk/pv`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlkk/pv.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlkk/pv.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlkk/pv/Vietovardis` (`deployed`)[^manifest]
- **Provider:** `vlkk` — Valstybinė lietuvių kalbos komisija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `objekto_id` | `string` | — | `4` | `open` | — | Objekto identifikatorius apjungti pavadinimus skirtingomis kalbomis | — |
| `objekto_pavadinimas` | `string` | — | `4` | `open` | — | Objekto pavadinimas originalo arba lietuvių kalba | — |
| `objekto_pavadinimas_be_kirciu` | `string` | — | `4` | `open` | — | Lietuviškas objekto pavadinimas be kirčio ženklų | — |
| `sulietuvinta` | `boolean` | — | `4` | `open` | — | Ar pavadinimas sulietuvintas | — |
| `objekto_rusis` | `string` | — | `4` | `open` | — | Objekto rūšis | — |
| `objekto_salis` | `string` | — | `4` | `open` | — | Šalis, kuriai priklauso objektas | — |
| `objekto_lokalizacija` | `string` | — | `1` | `open` | — | Objekto vietovės duomenys | — |
| `objekto_zemynas` | `string` | — | `4` | `open` | — | Objekto žemynas | — |
| `paiesku_sk` | `integer` | `U` | `4` | `open` | — | Kiek kartų buvo ieškota šio objekto VLKK pasvetainėje | — |
| `anksciausia_paieskos_data` | `datetime` | `S` | `4` | `open` | — | Anksčiausia objekto paieškos data | — |
| `veliausia_paieskos_data` | `datetime` | `S` | `4` | `open` | — | Vėliausia objekto paieškos data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlkk/pv.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlkk/pv.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlkk/pv (https://data.gov.lt/datasets/2703/)
