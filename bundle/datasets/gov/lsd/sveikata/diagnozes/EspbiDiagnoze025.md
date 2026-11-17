---
type: Table
title: "EspbiDiagnoze025 — Diagnozių dažnis pagal E025 formos duomenis"
description: "\"Diagnozių TLK-10-AM kodų, nurodytų ESPBI IS E025 dokumente (“Ambulatorinio apsilankymo aprašymas”), dažnis pagal apsilankymo metus, lytį ir savivaldybę sveikatos priežiūros įstaigos (SPĮ), kurioje nustatyta diagnozė."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/diagnozes/EspbiDiagnoze025"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# EspbiDiagnoze025 — Diagnozių dažnis pagal E025 formos duomenis

"Diagnozių TLK-10-AM kodų, nurodytų ESPBI IS E025 dokumente (“Ambulatorinio apsilankymo aprašymas”), dažnis pagal apsilankymo metus, lytį ir savivaldybę sveikatos priežiūros įstaigos (SPĮ), kurioje nustatyta diagnozė. Nurodytas skaičius unikalių asmenų, kuriems per ataskaitinius metus E025 dokumente diagnozės laukelyje buvo bent kartą įrašytas konkretus TLK "kodas, ir šių asmenų amžiaus vidurkis apsilankymų SPĮ metu.

- **Model:** `datasets/gov/lsd/sveikata/diagnozes/EspbiDiagnoze025`[^manifest]
- **Dataset:** [Diagnozių dažnis](../diagnozes.md) (`datasets/gov/lsd/sveikata/diagnozes`)
- **Manifest CSV:** [datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/diagnozes/EspbiDiagnoze025`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus kodas | — |
| `diagnozes_kodas` | `string` | — | `4` | `open` | — | Diagnozės TLK-10-AM kodas | — |
| `savivaldybes_pavadinimas` | `string` | — | `4` | `open` | — | Įstaigos, kurioje nustatyta diagnozė, savivaldybės pavadinimas | — |
| `diagnozes_metai` | `integer` | — | `2` | `open` | — | Metai, kada diagnozė buvo bent kartą nustatyta | Jeigu asmeniui tais metais diagnozė nustatyta kelis kartus, skaičiuojamas, kaip vienas atvejis |
| `lytis` | `string` | — | `4` | `open` | — | Asmenų grupės lytis | — |
| `atveju_kiekis` | `integer` | `U` | `4` | `open` | — | Asmenų, kuriems nustatyta diagnozė, skaičius pagal savivaldybę, metus ir lytį | — |
| `amziaus_vidurkis` | `number` | — | `4` | `open` | — | Asmenų, kuriems nustatyta diagnozė, amžiaus vidurkis | Konfidencialumo užtikrinimo tikslais, kai nustatytas tik vienas atvejis, amžiaus vidurkis paslėptas |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `diagnozes_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv
