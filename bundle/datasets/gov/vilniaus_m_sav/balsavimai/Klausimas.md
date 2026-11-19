---
type: Table
title: "Klausimas — Vilniaus miesto tarybos posėdžių duomenys ir apibendrinti rezultatai"
description: "Rinkinyje pateikiama informacija apie Vilniaus miesto tarybos posėdžiuose svarstytus klausimus ir balsavimus."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/balsavimai/Klausimas"
tags: [gov, vilniaus_m_sav, klausimas, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/balsavimai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/balsavimai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3849/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/balsavimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Klausimas — Vilniaus miesto tarybos posėdžių duomenys ir apibendrinti rezultatai

**Dataset Context:** Rinkinyje pateikiama informacija apie Vilniaus miesto tarybos posėdžiuose svarstytus klausimus ir balsavimus. Rinkinį sudaro dvi pagrindinės lentelės: viena reprezentuoja posėdžių ir klausimų informaciją su apibendrintais balsavimo duomenimis, kita – detalius kiekvieno tarybos nario balsus dėl individualaus klausimo. Rinkinyje pateikiami duomenys apie įvykusį posėdį (laiko žyma, posėdžio pirmininkas ir sekretorius), balsavimus (iškeltas klausimas, svarstymo tvarka, balsavimo rezultatai) ir priimtus sprendimus. Pažymėtina, jog abi rinkinio lentelės siejasi tarpusavyje per lauką "balsavimo_id".[^manifest]

- **Model:** `datasets/gov/vilniaus_m_sav/balsavimai/Klausimas`[^manifest]
- **Dataset:** [Vilniaus miesto tarybos balsavimai](../balsavimai.md) (`datasets/gov/vilniaus_m_sav/balsavimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/balsavimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/balsavimai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/balsavimai/Klausimas` (`deployed`)[^manifest]
- **Provider:** `vilniaus_m_sav` — Vilniaus miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `posedis` | `string` | — | `4` | `open` | — | Tarybos posėdžio pavadinimas | — |
| `posedzio_statusas` | `string` | — | `4` | `open` | — | Posėdžio statusas | — |
| `pirmininkas` | `string` | — | `4` | `open` | — | Posėdžio pirmininkas | — |
| `sekretorius` | `string` | — | `4` | `open` | — | Posėdžio sekretorius | — |
| `prasidejo` | `datetime` | `S` | `4` | `open` | — | Posėdžio pradžios laiko žyma | — |
| `baigesi` | `datetime` | `S` | `4` | `open` | — | Posėdžio pabaigos laiko žyma | — |
| `klausimo_id` | `string` | — | `4` | `open` | — | Svarstyto klausimo identifikacinis numeris | — |
| `klausimas_lt` | `string` | — | `2` | `open` | — | Svarstytas klausimas | — |
| `svarstymas` | `string` | — | `4` | `open` | — | Svarstymas | — |
| `svarstymo_tvarka` | `string` | — | `4` | `open` | — | Klausimo svarstymo tvarka | — |
| `balsavimo_id` | `string` | — | `4` | `open` | — | Balsavimo identifikacinis numeris | — |
| `balsavo` | `integer` | `U` | `4` | `open` | — | Bendras Tarybos narių, dalyvavusių balsavime, skaičius | — |
| `nebalsavo` | `integer` | `U` | `4` | `open` | — | Bendras Tarybos narių, nedalyvavusių balsavime, skaičius | — |
| `dalyvavo` | `integer` | `U` | `4` | `open` | — | Bendras Tarybos narių, dalyvavusių posėdyje, skaičius | — |
| `reikia_daugumai` | `integer` | `U` | `4` | `open` | — | Minimalus kriterijus kvorumui pasiekti (50% dalyvavusių posėdyje) | — |
| `sprendimas` | `string` | — | `4` | `open` | — | Balsavime priimtas sprendimas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `posedzio_statusas` | `"Baigta"` | — | — | — | — |
| `posedzio_statusas` | `"Vyksta"` | — | — | — | — |
| `posedzio_statusas` | `"Parengta"` | — | — | — | — |
| `posedzio_statusas` | `"Įvykęs"` | — | — | — | — |
| `posedzio_statusas` | `"Užbaigta/Tvarkoma"` | — | — | — | — |
| `svarstymo_tvarka` | `"Bendra tvarka"` | — | — | — | — |
| `svarstymo_tvarka` | `"Skubos tvarka"` | — | — | — | — |
| `svarstymo_tvarka` | `"Viena stadija"` | — | — | — | — |
| `svarstymo_tvarka` | `"Skubos tvarka arba ne"` | — | — | — | — |
| `svarstymo_tvarka` | `"Skubos tvarka, jei bus komiteto pritarimas"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `klausimas_lt` | `update(property: "klausimas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/balsavimai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/balsavimai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/balsavimai (https://data.gov.lt/datasets/3849/)
