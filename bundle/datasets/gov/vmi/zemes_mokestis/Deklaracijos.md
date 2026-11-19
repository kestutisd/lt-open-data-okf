---
type: Table
title: "Deklaracijos — Žemės mokečio deklaracijų duomenys"
description: "Spinta table datasets/gov/vmi/zemes_mokestis/Deklaracijos (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/zemes_mokestis/Deklaracijos"
tags: [gov, vmi, deklaracijos, deployed, level-3, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/zemes_mokestis.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vmi/zemes_mokestis.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1125/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/zemes_mokestis"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Deklaracijos — Žemės mokečio deklaracijų duomenys

- **Model:** `datasets/gov/vmi/zemes_mokestis/Deklaracijos`[^manifest]
- **Dataset:** [Žemės mokesčio deklaracijų duomenys](../zemes_mokestis.md) (`datasets/gov/vmi/zemes_mokestis`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/zemes_mokestis.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/zemes_mokestis.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/zemes_mokestis/Deklaracijos` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eilutės numeris | — |
| `mm_sav_kodas` | `integer` | — | `2` | `open` | — | Mokesčių mokėtojo savivaldybės kodas | — |
| `metai_id` | `integer` | — | `2` | `open` | — | Įrašo identifikacinis numeris informacinėje sistemoje (Mokestinis laikotarpis) | — |
| `tvirtinimo_data` | `datetime` | — | `3` | `open` | — | Deklaracijos tvirtinimo data (Suformavimo data deklaracijoje) | — |
| `apsk_suma` | `number` | — | `2` | `open` | — | Apskaičiuota žemės mokesčio suma | — |
| `sumoketi_mokesti` | `string` | — | `2` | `open` | — | Žemės mokestį sumokėti iki (data) | — |
| `tipas` | `string` | — | `4` | `open` | — | Deklaracijos tipas | — |
| `imokos_kodas` | `integer` | — | `3` | `open` | — | Įmokos kodas | — |
| `sst_kodas` | `string` | — | `4` | `open` | — | Žemės mokesčio mokėtojo tipas | — |
| `sklyp_plotas` | `number` | `ha` | `4` | `open` | — | Apmokestinamų žemės sklypų plotas (Priedo 5 stulp.suma) | — |
| `sklyp_verte` | `number` | — | `2` | `open` | — | Apmokestinamų žemės sklypų vertė (Priedo 6 stulp. suma) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Pirminė"` | `1` | — | Pirminė | — |
| `tipas` | `"Patikslinta"` | `2` | — | Patikslinta | — |
| `sst_kodas` | `"Fizinis asmuo"` | `1` | — | Fizinis asmuo | — |
| `sst_kodas` | `"Juridinis asmuo"` | `2` | — | Juridinis asmuo | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(ref: "eil_nr")` | `ref` | `4` | `open` | — | — | — |
| `mm_sav_kodas` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `mm_sav_kodas` | `update(property: "savivaldybe.sav_kodas", type: "")` | `type` | `4` | — | — | — | — |
| `metai_id` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `metai_id` | `update(property: "metai")` | `property` | `4` | `open` | — | — | — |
| `tvirtinimo_data` | `update(type: "datetime", ref: "D")` | `type` | `4` | — | — | — | — |
| `apsk_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `sumoketi_mokesti` | `update(type: "datetime", ref: "D")` | `type` | `4` | — | — | — | — |
| `sklyp_verte` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/zemes_mokestis.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/zemes_mokestis.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/zemes_mokestis (https://data.gov.lt/datasets/1125/)
