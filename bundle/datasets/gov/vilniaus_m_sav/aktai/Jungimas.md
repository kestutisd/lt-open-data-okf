---
type: Table
title: "Jungimas — Vilniaus miesto savivaldybės teisės aktų tarpusavio sąryšiai"
description: "Rinkinyje skelbiami Vilniaus miesto savivaldybės mero, tarybos, administracijos ir seniūnų paskelbti teisės aktų objektai: įsakymai, sprendimai, potvarkiai, projektai ir įsakai."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/aktai/Jungimas"
tags: [gov, vilniaus_m_sav, jungimas, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/aktai.csv#L20"
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/aktai.csv#L20"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3857/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/aktai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Jungimas — Vilniaus miesto savivaldybės teisės aktų tarpusavio sąryšiai

**Dataset Context:** Rinkinyje skelbiami Vilniaus miesto savivaldybės mero, tarybos, administracijos ir seniūnų paskelbti teisės aktų objektai: įsakymai, sprendimai, potvarkiai, projektai ir įsakai. Duomenys apima laikotarpį nuo 1990 m. Rinkinio objektas – vienas dokumentas. Rinkinyje kaupiami istoriniai duomenys, todėl įtraukti ir nustoję galioti teisės aktai. Skelbiami šie teisės aktų požymiai: pavadinimas, paskelbimo data, potvarkio numeris, aktą paskelbęs savivaldybės subjektas ir akto statusas. Vartotojai taip pat gali analizuoti paskelbtų teisės aktų tarpusavio ryšius – kurie dokumentai susiję, keičia ar yra priedai kitiems teisės aktams (žr. modelį Jungimas). Duomenų teikėjas – Vilniaus miesto savivaldybės administracija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/vilniaus_m_sav/aktai/Jungimas`[^manifest]
- **Dataset:** [Vilniaus miesto savivaldybės teisės aktų registras](../aktai.md) (`datasets/gov/vilniaus_m_sav/aktai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/aktai.csv#L20](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/aktai.csv#L20)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/aktai/Jungimas` (`deployed`)[^manifest]
- **Provider:** `vilniaus_m_sav` — Vilniaus miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `rysio_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `rysio_id` | `string` | — | `4` | `open` | — | Ryšio identifikacinis numeris | — |
| `rysio_pradzia` | `string` | — | `4` | `open` | — | Ryšio pradžios dokumento identifikacinis numeris. | Referuoja į modelio Dokumentas pirminį raktą (dokumento_id) |
| `rysio_pabaiga` | `string` | — | `4` | `open` | — | Ryšio pabaigos dokumento identifikacinis numeris | Referuoja į modelio Dokumentas pirminį raktą (dokumento_id) |
| `rysys` | `string` | — | `4` | `open` | — | Ryšio tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/aktai.csv#L20 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/aktai.csv#L20)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/aktai (https://data.gov.lt/datasets/3857/)
