---
type: Table
title: "ZemesGelmiuIstekliuRusis — Žemės gelmių išteklių rūšys (klasifikatorius)"
description: "Spinta table datasets/gov/lgt/zemes_gelmiu_istekliu_rusys/ZemesGelmiuIstekliuRusis (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/zemes_gelmiu_istekliu_rusys/ZemesGelmiuIstekliuRusis"
tags: [gov, lgt, zemesgelmiuistekliurusis, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geologija_zemes_istekliai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/lgt/geologija_zemes_istekliai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1341/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lgt/zemes_gelmiu_istekliu_rusys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# ZemesGelmiuIstekliuRusis — Žemės gelmių išteklių rūšys (klasifikatorius)

- **Model:** `datasets/gov/lgt/zemes_gelmiu_istekliu_rusys/ZemesGelmiuIstekliuRusis`[^manifest]
- **Dataset:** [Žemės gelmių išteklių rūšys](../zemes_gelmiu_istekliu_rusys.md) (`datasets/gov/lgt/zemes_gelmiu_istekliu_rusys`)[^manifest]
- **Manifest CSV:** [datasets/gov/lgt/geologija_zemes_istekliai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geologija_zemes_istekliai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/zemes_gelmiu_istekliu_rusys/ZemesGelmiuIstekliuRusis` (`deployed`)[^manifest]
- **Provider:** `lgt` — Lietuvos geologijos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `integer` | — | `4` | `open` | — | Kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `pavadinimas_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai | — |
| `galiojimas` | `date` | `D` | `4` | `open` | — | Galioja iki | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/geologija_zemes_istekliai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/geologija_zemes_istekliai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lgt/zemes_gelmiu_istekliu_rusys (https://data.gov.lt/datasets/1341/)
