---
type: Table
title: "VidutinePareigineAlga — Valstybės kontrolės darbuotojų vidutinė pareiginė alga"
description: "Valstybės kontrolės darbuotojų vidutinė pareiginė alga pagal pareigybių grupes"
resource: "https://get.data.gov.lt/datasets/gov/vk/alga/VidutinePareigineAlga"
tags: [gov, vk, vidutinepareiginealga, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/alga.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/vk/alga.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1688/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vk/alga"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# VidutinePareigineAlga — Valstybės kontrolės darbuotojų vidutinė pareiginė alga

Valstybės kontrolės darbuotojų vidutinė pareiginė alga pagal pareigybių grupes[^manifest]

- **Model:** `datasets/gov/vk/alga/VidutinePareigineAlga`[^manifest]
- **Dataset:** [Valstybės kontrolės darbuotojų vidutinė pareiginė alga](../alga.md) (`datasets/gov/vk/alga`)[^manifest]
- **Manifest CSV:** [datasets/gov/vk/alga.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/alga.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vk/alga/VidutinePareigineAlga` (`deployed`)[^manifest]
- **Provider:** `vk` — Valstybės kontrolė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ataskaitiniai_metai` | `integer` | — | `2` | `open` | — | Metai | Metai |
| `ataskaitinis_ketvirtis` | `integer` | — | `3` | `open` | — | Ketvirtis | Ketvirtis |
| `grupes_pavadinimas` | `string` | — | `3` | `open` | — | Grupės pavadinimas | Darbuotojų pareigybių grupės pavadinimas |
| `skaicius` | `integer` | `U` | `4` | `open` | — | Skaičius | Darbuotojų skaičius, kuris patenka į pareigybių grupę |
| `vidutine_alga` | `number` | — | `2` | `open` | — | Vidutinė alga | Darbuotojų vidutinė pareiginė alga tam tikroje pareigybių grupėje |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ataskaitiniai_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `vidutine_alga` | `update(type: "money", ref: "EUR")` | `type,ref` | `4` | — | `spinta: 40` | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vk/alga.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/alga.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vk/alga (https://data.gov.lt/datasets/1688/)
