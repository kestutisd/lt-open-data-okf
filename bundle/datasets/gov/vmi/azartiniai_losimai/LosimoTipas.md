---
type: Table
title: "LosimoTipas — Azartinių lošimų verslo loterijų ir lošimų mokesčio deklaracijų lošimo tipai"
description: "Spinta table datasets/gov/vmi/azartiniai_losimai/LosimoTipas (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/azartiniai_losimai/LosimoTipas"
tags: [gov, vmi, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmi/azartiniai_losimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/azartiniai_losimai.csv#L34"
    last_modified: "2026-11-11T14:39:20Z"
---

# LosimoTipas — Azartinių lošimų verslo loterijų ir lošimų mokesčio deklaracijų lošimo tipai

- **Model:** `datasets/gov/vmi/azartiniai_losimai/LosimoTipas`[^manifest]
- **Dataset:** [Azartinių lošimų verslo loterijų ir lošimo mokesčio deklaracijų (forma FR0584) duomenys](../azartiniai_losimai.md) (`datasets/gov/vmi/azartiniai_losimai`)
- **Manifest CSV:** [datasets/gov/vmi/azartiniai_losimai.csv#L34](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/azartiniai_losimai.csv#L34)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/azartiniai_losimai/LosimoTipas`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Mokestinio laikotarpio, už kurį teikiama deklaracija, metai | — |
| `ketvirtis` | `integer` | — | `2` | `open` | — | Mokestinio laikotarpio, už kurį teikiama deklaracija, ketvirtis | — |
| `tipas` | `integer` | — | `4` | `open` | — | Lošimo tipas | — |
| `moketoju_sk` | `integer` | `U` | `4` | `open` | — | Mokesčių mokėtojų skaičius | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `1` | — | — | Bingo | — |
| `tipas` | `2` | — | — | Totalizatorius | — |
| `tipas` | `3` | — | — | Lažybos | — |
| `tipas` | `4` | — | — | Nuotoliniai lošimai | — |
| `tipas` | `5` | — | — | A kategorijos lošimų automatai | — |
| `tipas` | `6` | — | — | B kategorijos lošimų automatai | — |
| `tipas` | `7` | — | — | Ruletė | — |
| `tipas` | `8` | — | — | Kortų stalai | — |
| `tipas` | `9` | — | — | Kauliukų stalai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/azartiniai_losimai.csv
