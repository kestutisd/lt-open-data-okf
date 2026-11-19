---
type: Table
title: "GyvunasTyrimas — Valstybinės maisto ir veterinarijos tarnybos gyvūnų tyrimai"
description: "Rinkinyje pateikiami nuo 2008 m. Valstybinės maisto ir veterinarijos tarnybos kaupiami duomenys apie gyvūnams atliktus tyrimus."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/gyvunu_tyrimai/GyvunasTyrimas"
tags: [gov, vmvt, gyvunastyrimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/gyvunu_tyrimai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vmvt/gyvunu_tyrimai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3819/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmvt/gyvunu_tyrimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# GyvunasTyrimas — Valstybinės maisto ir veterinarijos tarnybos gyvūnų tyrimai

Rinkinyje pateikiami nuo 2008 m. Valstybinės maisto ir veterinarijos tarnybos kaupiami duomenys apie gyvūnams atliktus tyrimus. Rinkinyje pateikiama informacija apie atliktus tyrimus ir jų rezultatus, gyvūnų amžių, laikymo vietą seniūnijos tikslumu. Viena eilutė atitinka vieno gyvūno vieno tyrimo statusą. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/vmvt/gyvunu_tyrimai/GyvunasTyrimas`[^manifest]
- **Dataset:** [Valstybinės maisto ir veterinarijos tarnybos gyvūnų tyrimai](../gyvunu_tyrimai.md) (`datasets/gov/vmvt/gyvunu_tyrimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmvt/gyvunu_tyrimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/gyvunu_tyrimai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/gyvunu_tyrimai/GyvunasTyrimas` (`deployed`)[^manifest]
- **Provider:** `vmvt` — Valstybinė maisto ir veterinarijos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikacinis kodas | — |
| `gyvuno_id` | `string` | — | `4` | `open` | — | Gyvūno identifikatorius | — |
| `meginio_id` | `string` | — | `4` | `open` | — | Mėginio identifikatorius | — |
| `laboratorijos_uzsakymo_nr` | `string` | — | `4` | `open` | — | Laboratorijos užsakymo numeris | — |
| `gyvuno_amzius_nuo` | `integer` | — | `4` | `open` | — | Gyvūno amžius nuo | — |
| `gyvuno_amzius_iki` | `integer` | — | `4` | `open` | — | Gyvūno amžius iki | — |
| `tiriama_liga` | `string` | — | `4` | `open` | — | Tiriama liga | — |
| `tyrimo_rez_reiksme` | `string` | — | `4` | `open` | — | Tyrimo rezultato reikšmė | — |
| `gautas_tyr_rezultatas` | `string` | — | `4` | `open` | — | Tyrimo rezultatas | — |
| `normalus_tyr_rezultatas` | `string` | — | `4` | `open` | — | Rezultato reikšmė, kai gyvūnas yra sveikas | — |
| `tyrimo_rez_vienetai` | `string` | — | `4` | `open` | — | Tyrimo rezultato vienetai | — |
| `paskutine_tyrimo_busena` | `string` | — | `4` | `open` | — | Paskutinė tyrimo būsena | — |
| `paskutines_tyr_busen_data` | `date` | `D` | `4` | `open` | — | Paskutinės tyrimo būsenos data | — |
| `tyrimo_tikslas` | `string` | — | `4` | `open` | — | Tyrimo tikslas | — |
| `tyrimo_tipas` | `string` | — | `4` | `open` | — | Tyrimo tipas | — |
| `tyrimo_tipo_aprasymas` | `string` | — | `4` | `open` | — | Tyrimo tipo aprašymas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė, kurioje yra gyvūnas | — |
| `seniunija` | `string` | — | `4` | `open` | — | Seniūnija, kurioje yra gyvūnas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/gyvunu_tyrimai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/gyvunu_tyrimai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmvt/gyvunu_tyrimai (https://data.gov.lt/datasets/3819/)
