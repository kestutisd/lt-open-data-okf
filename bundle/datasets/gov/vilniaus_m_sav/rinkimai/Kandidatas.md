---
type: Table
title: "Kandidatas — Vilniaus miesto savivaldybės seniūnaičių rinkimų rezultatai"
description: "Rinkinyje pateikiami Vilniaus mieste savivaldybėje vykusių seniūnaičių rinkimų duomenys nuo 2019m."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/rinkimai/Kandidatas"
tags: [gov, vilniaus_m_sav, kandidatas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/seniunaiciai.csv#L12"
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/seniunaiciai.csv#L12"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3847/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/rinkimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Kandidatas — Vilniaus miesto savivaldybės seniūnaičių rinkimų rezultatai

Rinkinyje pateikiami Vilniaus mieste savivaldybėje vykusių seniūnaičių rinkimų duomenys nuo 2019m. Vilniaus miesto teritorija yra padalinta į seniūnijas, o seniūnijos savo ruožtu yra skirstomos į mažesnius administracinius vienetus – seniūnaitijas. Seniūnaitis – tai visuomeniniais pagrindais dirbantis gyvenamosios vietovės ar bendruomenės išrinktas atstovas, vykdantis įstatymo nustatytas teises ir pareigas. Vilniaus miesto tarybos sprendimu seniūnaičiui skiriama 30 eurų mėnesio išmoka, skirta su seniūnaičio veikla susijusioms išlaidos apmokėti. Daugiau informacijos apie seniūnaičių teises ir pareigas: https://vilnius.lt/savivaldybe/seniunijos-ir-bendruomenes/seniunaiciai Rinkinio objektas – rinkimuose dalyvavusio kandidato rezultatai. Duomenyse nurodyti duomenys apie seniūnaičių rinkimus (rinkimų data, balsavimo pradžios ir pabaigos datos, turas) ir kandidatus į seniūnaičius (seniūnija, seniūnaitija, kandidato (-ės) vardas ir pavardė, rinkiminės programos tikslai, surinktų balsų skaičius ir požymis, ar buvo išrinktas(-a)). Duomenų teikėjas – Vilniaus miesto savivaldybės administracija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/vilniaus_m_sav/rinkimai/Kandidatas`[^manifest]
- **Dataset:** [Vilniaus miesto savivaldybės seniūnaičių rinkimų rezultatai](../rinkimai.md) (`datasets/gov/vilniaus_m_sav/rinkimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/seniunaiciai.csv#L12](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/seniunaiciai.csv#L12)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/rinkimai/Kandidatas` (`deployed`)[^manifest]
- **Provider:** `vilniaus_m_sav` — Vilniaus miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `rinkimai` | `string` | — | `4` | `open` | — | Rinkimų pavadinimas | — |
| `rinkimu_turas` | `string` | — | `4` | `open` | — | Rinkimų turo numeris | — |
| `balsavimo_pradzia` | `date` | `D` | `4` | `open` | — | Balsavimo pradžios data | — |
| `balsavimo_pabaiga` | `date` | `D` | `4` | `open` | — | Balsavimo pabaigos data | — |
| `seniunija` | `string` | — | `4` | `open` | — | Kandidato seniūnija | — |
| `seniunaitija` | `string` | — | `4` | `open` | — | Kandidato seniūnaitija | — |
| `kandidatas` | `string` | — | `4` | `open` | — | Kandidato vardas ir pavardė | — |
| `kandidato_rinkimai` | `integer` | — | `4` | `open` | — | Kandidatavimų eilės skaičius | — |
| `tikslai` | `string` | — | `4` | `open` | — | Kandidato rinkiminės programos tikslai | — |
| `viso_balsu` | `integer` | — | `4` | `open` | — | Rinkimuose gautų balsų skaičius | — |
| `ar_isrinko` | `boolean` | — | `4` | `open` | — | Požymis ar kandidatas buvo išrinktas į seniūnaičius | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `rinkimai` | `"Seniūnaičių rinkimai (2019 m.)"` | — | — | — | — |
| `rinkimai` | `"Seniūnaičių rinkimai (2023 m.)"` | — | — | — | — |
| `rinkimai` | `"Seniūnaičių rinkimai (2024 m.)"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/seniunaiciai.csv#L12 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/seniunaiciai.csv#L12)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/rinkimai (https://data.gov.lt/datasets/3847/)
