---
type: Table
title: "Dokumentas — Vilniaus miesto savivaldybės teisės aktai"
description: "Rinkinyje skelbiami Vilniaus miesto savivaldybės mero, tarybos, administracijos ir seniūnų paskelbti teisės aktų objektai: įsakymai, sprendimai, potvarkiai, projektai ir įsakai."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/aktai/Dokumentas"
tags: [gov, vilniaus_m_sav, dokumentas, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/aktai.csv#L10"
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/aktai.csv#L10"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3857/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/aktai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Dokumentas — Vilniaus miesto savivaldybės teisės aktai

**Dataset Context:** Rinkinyje skelbiami Vilniaus miesto savivaldybės mero, tarybos, administracijos ir seniūnų paskelbti teisės aktų objektai: įsakymai, sprendimai, potvarkiai, projektai ir įsakai. Duomenys apima laikotarpį nuo 1990 m. Rinkinio objektas – vienas dokumentas. Rinkinyje kaupiami istoriniai duomenys, todėl įtraukti ir nustoję galioti teisės aktai. Skelbiami šie teisės aktų požymiai: pavadinimas, paskelbimo data, potvarkio numeris, aktą paskelbęs savivaldybės subjektas ir akto statusas. Vartotojai taip pat gali analizuoti paskelbtų teisės aktų tarpusavio ryšius – kurie dokumentai susiję, keičia ar yra priedai kitiems teisės aktams (žr. modelį Jungimas). Duomenų teikėjas – Vilniaus miesto savivaldybės administracija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/vilniaus_m_sav/aktai/Dokumentas`[^manifest]
- **Dataset:** [Vilniaus miesto savivaldybės teisės aktų registras](../aktai.md) (`datasets/gov/vilniaus_m_sav/aktai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/aktai.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/aktai.csv#L10)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/aktai/Dokumentas` (`deployed`)[^manifest]
- **Provider:** `vilniaus_m_sav` — Vilniaus miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `dokumento_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dokumento_id` | `string` | — | `4` | `open` | — | Dokumento identifikacinis numeris | — |
| `paskelbimas` | `date` | `D` | `4` | `open` | — | Dokumento pasirašymo data | — |
| `potvarkio_nr` | `string` | — | `4` | `open` | — | Dokumento registracijos numeris | — |
| `rusis` | `string` | — | `4` | `open` | — | Dokumento rūšis | — |
| `url` | `string` | — | `4` | `open` | — | Suformuota nuoroda į dokumentą | — |
| `pavadinimas_lt` | `string` | — | `4` | `open` | — | Dokumento pavadinimas | — |
| `padalinys` | `string` | — | `4` | `open` | — | Savivaldybės padalinys, parengęs dokumentą | — |
| `statusas` | `string` | — | `4` | `open` | — | Dokumento statusas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/aktai.csv#L10 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/aktai.csv#L10)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/aktai (https://data.gov.lt/datasets/3857/)
