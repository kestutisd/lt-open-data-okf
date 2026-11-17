---
type: Table
title: "ZemesGelmiuIstekliuRusis — Žemės gelmių išteklių rūšys (klasifikatorius)"
description: "Spinta table datasets/gov/lgt/zemes_gelmiu_istekliu_rusys/ZemesGelmiuIstekliuRusis (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/zemes_gelmiu_istekliu_rusys/ZemesGelmiuIstekliuRusis"
tags: [gov, lgt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lgt/geologija_zemes_istekliai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geologija_zemes_istekliai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# ZemesGelmiuIstekliuRusis — Žemės gelmių išteklių rūšys (klasifikatorius)

- **Model:** `datasets/gov/lgt/zemes_gelmiu_istekliu_rusys/ZemesGelmiuIstekliuRusis`[^manifest]
- **Dataset:** [Žemės gelmių išteklių rūšys](../zemes_gelmiu_istekliu_rusys.md) (`datasets/gov/lgt/zemes_gelmiu_istekliu_rusys`)
- **Manifest CSV:** [datasets/gov/lgt/geologija_zemes_istekliai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geologija_zemes_istekliai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/zemes_gelmiu_istekliu_rusys/ZemesGelmiuIstekliuRusis`
- **Primary Key (`ref`):** `kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `integer` | — | `4` | `open` | — | Kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `pavadinimas_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai | — |
| `galiojimas` | `date` | `D` | `4` | `open` | — | Galioja iki | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/geologija_zemes_istekliai.csv
