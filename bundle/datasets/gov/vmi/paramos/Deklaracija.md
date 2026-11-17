---
type: Table
title: "Deklaracija — Prašymai pervesti pajamų mokesčio dalį duomenys"
description: "Prašymų pervesti pajamų mokesčio dalį vienetams, turintiems teisę gauti paramą, ir (arba) politinėms partijoms duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vmi/paramos/Deklaracija"
tags: [gov, vmi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmi/parama.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/parama.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Deklaracija — Prašymai pervesti pajamų mokesčio dalį duomenys

Prašymų pervesti pajamų mokesčio dalį vienetams, turintiems teisę gauti paramą, ir (arba) politinėms partijoms duomenys

- **Model:** `datasets/gov/vmi/paramos/Deklaracija`[^manifest]
- **Dataset:** [datasets/gov/vmi/paramos](../paramos.md) (`datasets/gov/vmi/paramos`)
- **Manifest CSV:** [datasets/gov/vmi/parama.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/parama.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/paramos/Deklaracija`
- **Level:** `4`

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/parama.csv
