---
type: Table
title: "Deklaracija — Prašymai pervesti pajamų mokesčio dalį duomenys"
description: "Prašymų pervesti pajamų mokesčio dalį vienetams, turintiems teisę gauti paramą, ir (arba) politinėms partijoms duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vmi/paramos/Deklaracija"
tags: [gov, vmi, deklaracija, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/parama.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vmi/parama.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1299/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/paramos"
    author: "team:vda"
    last_modified: "2026-03-09T00:00:00Z"
---

# Deklaracija — Prašymai pervesti pajamų mokesčio dalį duomenys

Prašymų pervesti pajamų mokesčio dalį vienetams, turintiems teisę gauti paramą, ir (arba) politinėms partijoms duomenys[^manifest]

- **Model:** `datasets/gov/vmi/paramos/Deklaracija`[^manifest]
- **Dataset:** [Parama](../paramos.md) (`datasets/gov/vmi/paramos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/parama.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/parama.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/paramos/Deklaracija` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-03-09`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eiles_nr` | `string` | — | `4` | `open` | — | Įrašo identifikatorius | — |
| `remejo_kodas` | `string` | — | `4` | `open` | — | Rėmėjo kodas | — |
| `metai` | `integer` | — | `4` | `open` | — | Mokestinis laikotarpis | — |
| `gavejo_kodas` | `string` | — | `4` | `open` | — | Gavėjo kodas | — |
| `gavejo_pavadinimas` | `string` | — | `4` | `open` | — | Gavėjo pavadinimas | — |
| `gavejo_sav_kodas` | `string` | — | `4` | `open` | — | Gavėjo savivaldybės kodas | — |
| `gavejo_savivaldybe` | `string` | — | `4` | `open` | — | Gavėjo savivaldybė | — |
| `gavejo_tipas` | `string` | — | `4` | `open` | — | Gavėjo tipas | — |
| `gavejo_imones_rusis` | `string` | — | `4` | `open` | — | Gavėjo įmonės rūšis | — |
| `mokescio_dalis_proc` | `number` | `%` | `4` | `open` | — | Mokesčio dalis | Procentais |
| `suma` | `number` | — | `4` | `open` | — | Apskaičiuota paramos suma | Eurais |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/parama.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/parama.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/paramos (https://data.gov.lt/datasets/1299/)
