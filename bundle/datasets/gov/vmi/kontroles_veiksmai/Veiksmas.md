---
type: Table
title: "Veiksmas — Atlikti kontrolės veiksmai"
description: "Spinta table datasets/gov/vmi/kontroles_veiksmai/Veiksmas (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/kontroles_veiksmai/Veiksmas"
tags: [gov, vmi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmi/kontroles_veiksmai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/kontroles_veiksmai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Veiksmas — Atlikti kontrolės veiksmai

- **Model:** `datasets/gov/vmi/kontroles_veiksmai/Veiksmas`[^manifest]
- **Dataset:** [Atlikti kontrolės veiksmai](../kontroles_veiksmai.md) (`datasets/gov/vmi/kontroles_veiksmai`)
- **Manifest CSV:** [datasets/gov/vmi/kontroles_veiksmai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/kontroles_veiksmai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/kontroles_veiksmai/Veiksmas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA identifikatorius | — |
| `evrk` | `ref` | [/datasets/gov/lsd/cl/evrk/EkonominesVeiklosRusis](../../lsd/cl/evrk/EkonominesVeiklosRusis.md) | `4` | `open` | — | Ekonominės veiklos rūšies kodas | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybės identifikavimo kodas | — |
| `mm_skaicius` | `integer` | `U` | `4` | `open` | — | Mokesčių mokėtojų skaičius | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/kontroles_veiksmai.csv
