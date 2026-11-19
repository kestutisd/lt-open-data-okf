---
type: Table
title: "EspbiDiagnoze003 — Diagnozių dažnis pagal E003 formos duomenis"
description: "\"Diagnozių TLK-10-AM kodų, nurodytų ESPBI IS E003 dokumente (“Stacionaro epikrizė”), dažnis pagal apsilankymo metus, lytį ir savivaldybę sveikatos priežiūros įstaigos (SPĮ), kurioje nustatyta diagnozė."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/diagnozes/EspbiDiagnoze003"
tags: [gov, lsd, espbidiagnoze003, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L19"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L19"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2843/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/diagnozes"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# EspbiDiagnoze003 — Diagnozių dažnis pagal E003 formos duomenis

"Diagnozių TLK-10-AM kodų, nurodytų ESPBI IS E003 dokumente (“Stacionaro epikrizė”), dažnis pagal apsilankymo metus, lytį ir savivaldybę sveikatos priežiūros įstaigos (SPĮ), kurioje nustatyta diagnozė. Nurodytas skaičius unikalių asmenų, kuriems per ataskaitinius metus E003 dokumente diagnozės laukelyje buvo bent kartą įrašytas konkretus TLK kodas, ir šių asmenų "amžiaus vidurkis apsilankymų SPĮ metu.[^manifest]

- **Model:** `datasets/gov/lsd/sveikata/diagnozes/EspbiDiagnoze003`[^manifest]
- **Dataset:** [Diagnozių dažnis](../diagnozes.md) (`datasets/gov/lsd/sveikata/diagnozes`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L19](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L19)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/diagnozes/EspbiDiagnoze003` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus kodas | — |
| `diagnozes_kodas` | `string` | — | `4` | `open` | — | Diagnozės TLK kodas | — |
| `savivaldybes_pavadinimas` | `string` | — | `4` | `open` | — | "Įstaigos, kurioje nustatyta diagnozė, savivaldybės pavadinimas" | — |
| `diagnozes_metai` | `integer` | — | `2` | `open` | — | "Metai, kada diagnozė buvo bent kartą nustatyta" | "Nustatomi pagal vizito pradžios laiką. Jeigu asmeniui tais metais diagnozė nustatyta kelis kartus, skaičiuojamas, kaip vienas atvejis" |
| `lytis` | `string` | — | `4` | `open` | — | Asmenų grupės lytis | — |
| `atveju_kiekis` | `integer` | `U` | `4` | `open` | — | "Nustatytų diagnozių kiekis pagal savivaldybę, metus ir lytį" | — |
| `amziaus_vidurkis` | `number` | — | `4` | `open` | — | "Asmenų, kuriems nustatyta diagnozė, amžiaus vidurkis" | "Nustatomas pagal vizito pradžios laiką. Konfidencialumo užtikrinimo tikslais, kai nustatytas tik vienas atvejis, amžiaus vidurkis paslėptas" |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `diagnozes_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L19 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L19)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/diagnozes (https://data.gov.lt/datasets/2843/)
