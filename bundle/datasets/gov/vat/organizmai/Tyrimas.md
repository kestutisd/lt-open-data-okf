---
type: Table
title: "Tyrimas — Pateikiama informacija apie kenksmingųjų organizmų tyrimų rezultatus per tam tikrą laikotarpį."
description: "Spinta table datasets/gov/vat/organizmai/Tyrimas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/organizmai/Tyrimas"
tags: [gov, vat, tyrimas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r6_kenksmingi_organizmai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/r6_kenksmingi_organizmai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1862/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/organizmai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Tyrimas — Pateikiama informacija apie kenksmingųjų organizmų tyrimų rezultatus per tam tikrą laikotarpį.

- **Model:** `datasets/gov/vat/organizmai/Tyrimas`[^manifest]
- **Dataset:** [Kenksmingųjų organizmų tyrimai](../organizmai.md) (`datasets/gov/vat/organizmai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r6_kenksmingi_organizmai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r6_kenksmingi_organizmai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/organizmai/Tyrimas` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Įrašo identifikatorius | — |
| `padalinys` | `string` | — | `4` | `open` | — | Patikrinimą atlikęs teritorinis padalinys | — |
| `buvo_tirta` | `string` | — | `4` | `open` | — | Tyrimo objektas | — |
| `rajonas` | `string` | — | `4` | `open` | — | Rajonas (pagal tikrinimo vietą) | — |
| `tikrinimas` | `date` | `D` | `4` | `open` | — | Patikrinimo akto data | — |
| `vieta` | `string` | — | `3` | `open` | — | Tikrinimo vietos pavadinimas | — |
| `objektas` | `string` | — | `1` | `open` | — | Tikrinimo vietos pavadinimas | — |
| `kiekis` | `number` | — | `4` | `open` | — | Tikrinamo objekto bendras kiekis | — |
| `matavimo_vnt` | `string` | — | `4` | `open` | — | Tikrinamo objekto kiekio matavimo vienetai | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `padalinys` | `"Kauno oro uosto pasienio kontrolės punkto fitosanitarijos postas (skyrius)"` | — | — | — | — |
| `padalinys` | `"Klaipėdos regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Vilniaus regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Kauno regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Panevėžio regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Alytaus regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Telšių regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Marijampolės regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Šiaulių regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Utenos regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Tauragės regioninis skyrius"` | — | — | — | — |
| `padalinys` | `"Klaipėdos jūrų uosto pasienio kontrolės punkto fitosanitarijos postas (skyrius)"` | — | — | — | — |
| `padalinys` | `"Fitosanitarijos skyrius"` | — | — | — | — |
| `buvo_tirta` | `"Bakterijos"` | — | — | — | — |
| `buvo_tirta` | `"Nematodai"` | — | — | — | — |
| `buvo_tirta` | `"Grybai"` | — | — | — | — |
| `buvo_tirta` | `"Vabzdžiai"` | — | — | — | — |
| `buvo_tirta` | `"Piktžolių sėklos"` | — | — | — | — |
| `buvo_tirta` | `"Virusai"` | — | — | — | — |
| `buvo_tirta` | `"Erkės"` | — | — | — | — |
| `buvo_tirta` | `"Piktžolės"` | — | — | — | — |
| `buvo_tirta` | `"Fitoplazmos"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r6_kenksmingi_organizmai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r6_kenksmingi_organizmai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/organizmai (https://data.gov.lt/datasets/1862/)
