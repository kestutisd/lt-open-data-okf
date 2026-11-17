---
type: Table
title: "ValstPerduotasTurtas"
description: "Spinta table datasets/gov/vmi/turto_realizavimas/ValstPerduotasTurtas (18 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/turto_realizavimas/ValstPerduotasTurtas"
tags: [gov, vmi, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmi/turto_realizavimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/turto_realizavimas.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# ValstPerduotasTurtas

- **Model:** `datasets/gov/vmi/turto_realizavimas/ValstPerduotasTurtas`[^manifest]
- **Dataset:** [datasets/gov/vmi/turto_realizavimas](../turto_realizavimas.md) (`datasets/gov/vmi/turto_realizavimas`)
- **Manifest CSV:** [datasets/gov/vmi/turto_realizavimas.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/turto_realizavimas.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/turto_realizavimas/ValstPerduotasTurtas`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `bylos_nr` | `string` | — | `2` | `open` | — | Atsargų kodas (bylos Nr.) | — |
| `turto_pav` | `string` | — | `1` | `open` | — | Turto pavadinimas | — |
| `apskritis` | `string` | — | `2` | `open` | — | Apskritis | — |
| `vpt_grupe` | `string` | — | `3` | `open` | — | VPT grupė | — |
| `vpt_kategorija` | `string` | — | `3` | `open` | — | VPT kategorija | — |
| `bylos_tipas` | `string` | — | `3` | `open` | — | Bylos tipas | — |
| `realizuota` | `date` | `D` | `4` | `open` | — | Realizavimo veiksmo data | — |
| `realiz_budas` | `string` | — | `3` | `open` | — | Realizavimo veiksmo tipas | — |
| `realizuotojas` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_pavadinimas]](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `2` | `open` | — | Realizuotojo pavadinimas | — |
| `mato_vnt` | `string` | — | `3` | `open` | — | Mato vienetas | — |
| `realiz_turto_verte` | `number` | — | `2` | `open` | — | Realizuoto turto vertė | — |
| `realiz_turto_kiekis` | `integer` | `U` | `4` | `open` | — | Realizuoto turto kiekis | — |
| `suma` | `number` | — | `2` | `open` | — | Realizuoto turto suma | — |
| `turtas_apskaitytas` | `date` | `D` | `4` | `open` | — | Turto apskaitymo data | — |
| `apsk_turto_verte` | `number` | — | `2` | `open` | — | Apskaityto turto vertė | — |
| `apsk_turto_kiekis` | `integer` | `U` | `4` | `open` | — | Apskaityto turto kiekis | — |
| `apsk_turto_suma` | `number` | — | `2` | `open` | — | Apskaityto turto suma | — |
| `pajamuota` | `date` | `D` | `4` | `open` | — | Pajamavimo veiksmo data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `realiz_turto_verte` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `apsk_turto_verte` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `apsk_turto_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/turto_realizavimas.csv
