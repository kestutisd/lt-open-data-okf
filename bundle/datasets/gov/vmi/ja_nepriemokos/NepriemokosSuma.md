---
type: Table
title: "NepriemokosSuma — Juridinių asmenų nepriemokos sumos"
description: "Spinta table datasets/gov/vmi/ja_nepriemokos/NepriemokosSuma (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/ja_nepriemokos/NepriemokosSuma"
tags: [gov, vmi, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmi/ja_nepriemokos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/ja_nepriemokos.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# NepriemokosSuma — Juridinių asmenų nepriemokos sumos

- **Model:** `datasets/gov/vmi/ja_nepriemokos/NepriemokosSuma`[^manifest]
- **Dataset:** [datasets/gov/vmi/ja_nepriemokos](../ja_nepriemokos.md) (`datasets/gov/vmi/ja_nepriemokos`)
- **Manifest CSV:** [datasets/gov/vmi/ja_nepriemokos.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/ja_nepriemokos.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/ja_nepriemokos/NepriemokosSuma`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus įrašo ID | — |
| `sukurta` | `date` | `D` | `4` | `open` | — | Įrašo sukūrimo data | — |
| `atnaujinta` | `date` | `D` | `4` | `open` | — | Įrašo atnaujinimo data | — |
| `ja_kodas` | `string` | — | `2` | `open` | — | Juridinio asmens (toliau – JA) kodas | — |
| `ja_pavadinimas` | `string` | — | `2` | `open` | — | JA pavadinimas | — |
| `sav_kodas` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) | `3` | `open` | — | Savivaldybės, kurioje registruotas JA, kodas | — |
| `nepriemoka` | `number` | — | `2` | `open` | — | JA mokestinės nepriemokos suma iš viso | — |
| `pradelsta_nepriemoka` | `number` | — | `2` | `open` | — | JA pradelsta mokestinės nepriemokos suma | — |
| `atideta_nepriemoka` | `number` | — | `2` | `open` | — | JA pagal mokestinės paskolos sutartį, susitarimą dėl pagalbos, restruktūrizavimo planą, mokumo atkūrimo planą, taikos sutartį atidėtos nepriemokos likutis. | — |
| `atideta_pradelsta` | `number` | — | `2` | `open` | — | JA pagal mokestinės paskolos sutartį, susitarimą dėl pagalbos, restruktūrizavimo planą, mokumo atkūrimo planą, taikos sutartį, pradelsta suma. | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nepriemoka` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `pradelsta_nepriemoka` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `atideta_nepriemoka` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `atideta_pradelsta` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/ja_nepriemokos.csv
