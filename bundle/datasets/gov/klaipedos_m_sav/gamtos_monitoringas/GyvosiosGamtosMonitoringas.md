---
type: Table
title: "GyvosiosGamtosMonitoringas — Klaipėdos miesto savivaldybės gyvosios aplinkos monitoringo duomenys"
description: "Rinkinyje pateikiami Klaipėdos miesto savivaldybės gyvosios gamtos monitoringo duomenys."
resource: "https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/gamtos_monitoringas/GyvosiosGamtosMonitoringas"
tags: [gov, klaipedos_m_sav, gyvosiosgamtosmonitoringas, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/gyvosios_gamtos_monitoringas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/gyvosios_gamtos_monitoringas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2663/"
    title: "data.gov.lt DCAT-AP — datasets/gov/klaipedos_m_sav/gamtos_monitoringas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# GyvosiosGamtosMonitoringas — Klaipėdos miesto savivaldybės gyvosios aplinkos monitoringo duomenys

Rinkinyje pateikiami Klaipėdos miesto savivaldybės gyvosios gamtos monitoringo duomenys. Šiame rinkinyje pateikiami tokie duomenys: •	paviršinio vandens monitoringas •	gyvosios gamtos (paukščių) monitoringas •	gyvosios gamtos (šikšnosparnių) monitoringas •	gyvosios gamtos (augalijos) monitoringas •	gyvosios gamtos (varliagyvių) monitoringas •	gyvosios gamtos (žuvų) monitoringas Duomenys pateikiami nuo 2005 metų.[^manifest]

- **Model:** `datasets/gov/klaipedos_m_sav/gamtos_monitoringas/GyvosiosGamtosMonitoringas`[^manifest]
- **Dataset:** [Klaipėdos miesto savivaldybės gyvosios aplinkos monitoringo duomenys](../gamtos_monitoringas.md) (`datasets/gov/klaipedos_m_sav/gamtos_monitoringas`)[^manifest]
- **Manifest CSV:** [datasets/gov/klaipedos_m_sav/gyvosios_gamtos_monitoringas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/gyvosios_gamtos_monitoringas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/gamtos_monitoringas/GyvosiosGamtosMonitoringas` (`deployed`)[^manifest]
- **Provider:** `klaipedos_m_sav` — Klaipėdos miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `stebejimo_id` | `string` | — | `4` | `open` | — | Monitoringo duomenų eilės numeris. | — |
| `monitoringo_pradzia` | `date` | `D` | `4` | `open` | — | Monitoringo duomenys. Tyrimų pradžios data. | — |
| `monitoringo_pabaiga` | `date` | `D` | `4` | `open` | — | Monitoringo duomenys. Tyrimų pabaigos data. | — |
| `monitoringo_tasko_id` | `string` | — | `4` | `open` | — | Monitoringo duomenys. Monitoringo taško eilės numeris. | — |
| `monitoringo_tasko_tipas` | `string` | — | `4` | `open` | — | Monitoringo taško tipas | — |
| `monitoringo_tasko_reiksme_lt` | `string` | — | `3` | `open` | — | Monitoringo taško reikšmė | — |
| `tasko_lokacija` | `string` | — | `2` | `open` | — | Monitoringo taško adresas | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | Monitoringo taško LKS-94 koordinačių platuma. | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Monitoringo taško LKS-94 koordinačių ilguma. | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Monitoringo taško WGS-84 koordinačių platuma. | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Monitoringo taško WGS-84 koordinačių ilguma. | — |
| `rusies_pav_lt` | `string` | — | `4` | `open` | — | Rūšies lietuviškas pavadinimas. | — |
| `rusies_pav_la` | `string` | — | — | `open` | — | Rūšies lotyniškas pavadinimas. | — |
| `rusies_pav_en` | `string` | — | — | `open` | — | Rūšies angliškas pavadinimas. | — |
| `rusies_grupe` | `string` | — | `4` | `open` | — | Rūšies grupė. | — |
| `rusies_grupes_reiksme` | `string` | — | `3` | `open` | — | Rūšies grupės reikšmė | — |
| `reiksme` | `string` | — | `2` | `open` | — | Rūšių monitoringas. Reikšmė. | — |
| `parametras` | `string` | — | `4` | `open` | — | Rūšių monitoringas. Parametras. | — |
| `parametro_reiksme_lt` | `string` | — | `3` | `open` | — | Parametro reikšmė | — |
| `fitoplanktono_kiekis` | `number` | — | `4` | `open` | — | Fitoplanktono kiekis aplinkoje. | — |
| `fitoplanktono_biomase` | `number` | — | `4` | `open` | — | Fitoplanktono biomasė aplinkoje. | — |
| `zoobentoso_tankumas` | `number` | — | `4` | `open` | — | Zoobentoso tankumas aplinkoje. | — |
| `zoobentoso_biomase` | `number` | — | `4` | `open` | — | Zoobentoso biomasė aplinkoje. | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `monitoringo_tasko_tipas` | `"ggms"` | — | — | Gyvosios gamtos (šikšnosparnių) monitoringas | — |
| `monitoringo_tasko_tipas` | `"ggmp"` | — | — | Gyvosios gamtos (paukščių) monitoringas | — |
| `monitoringo_tasko_tipas` | `"ggmv"` | — | — | Gyvosios gamtos (varliagyvių) monitoringas | — |
| `monitoringo_tasko_tipas` | `"ggmz"` | — | — | Gyvosios gamtos (žuvų) monitoringas | — |
| `monitoringo_tasko_tipas` | `"ggma"` | — | — | Gyvosios gamtos (augalijos) monitoringas | — |
| `monitoringo_tasko_tipas` | `"pvm"` | — | — | Paviršinio vandens monitoringas | — |
| `rusies_grupe` | `"fpl"` | — | — | Fitoplanktonas | — |
| `rusies_grupe` | `"zpl"` | — | — | Zooplanktonas | — |
| `rusies_grupe` | `"pau"` | — | — | Paukščiai | — |
| `rusies_grupe` | `"sik"` | — | — | Šikšnosparniai | — |
| `rusies_grupe` | `"aum"` | — | — | Augalija (makrofitai) | — |
| `rusies_grupe` | `"var"` | — | — | Varliagyviai | — |
| `rusies_grupe` | `"zuv"` | — | — | Žuvis | — |
| `parametras` | `"count"` | — | — | Rūšies gausumo reikšmė, vnt. | — |
| `parametras` | `"pad"` | — | — | Rūšies gausumo reikšmė (vandens telkiniuose), balais | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `monitoringo_tasko_reiksme_lt` | `update(property: "monitoringo_tasko_reiksme_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `rusies_pav_lt` | `update(property: "rusies_pav_lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `rusies_pav_la` | `update(property: "rusies_pav_lo", type: "text")` | `type` | `4` | `open` | — | — | — |
| `rusies_pav_en` | `update(property: "rusies_pav_en", type: "text")` | `type` | `4` | `open` | — | — | — |
| `parametro_reiksme_lt` | `update(property: "parametro_reiksme_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/gyvosios_gamtos_monitoringas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/gyvosios_gamtos_monitoringas.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/klaipedos_m_sav/gamtos_monitoringas (https://data.gov.lt/datasets/2663/)
