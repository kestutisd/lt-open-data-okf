---
type: Table
title: "NVRusysPPS21 — Lietuvos kaimo plėtros programos 2014-2020 priemonė \"Parama Nykstančių Lietuvos senųjų veislių gyvulių ir naminių paukščių išsaugojimui\" gyvulių rūšis"
description: "Spinta table datasets/gov/nma/nv_rusys/NVRusysPPS21 (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nma/nv_rusys/NVRusysPPS21"
tags: [gov, nma, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nma/nv_rusys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/nv_rusys.csv#L20"
    last_modified: "2026-11-11T14:39:20Z"
---

# NVRusysPPS21 — Lietuvos kaimo plėtros programos 2014-2020 priemonė "Parama Nykstančių Lietuvos senųjų veislių gyvulių ir naminių paukščių išsaugojimui" gyvulių rūšis

- **Model:** `datasets/gov/nma/nv_rusys/NVRusysPPS21`[^manifest]
- **Dataset:** [datasets/gov/nma/nv_rusys](../nv_rusys.md) (`datasets/gov/nma/nv_rusys`)
- **Manifest CSV:** [datasets/gov/nma/nv_rusys.csv#L20](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/nv_rusys.csv#L20)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nma/nv_rusys/NVRusysPPS21`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pareiskejo_tipas` | `string` | — | `4` | `open` | — | Pareiškėjo tipas | — |
| `pareiskejo_lytis` | `string` | — | `4` | `open` | — | Pareiškėjo lytis | — |
| `paraiskos_pateikimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos pateikimo data | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybės ŽŪS | — |
| `programa` | `string` | — | `3` | `open` | — | Programa | — |
| `remiama_grupe` | `string` | — | `3` | `open` | — | Remiama grupė | — |
| `gyvuliu_kiekis` | `number` | `U` | `4` | `open` | — | Deklaruotas gyvulių kiekis | — |
| `valdos_numeris` | `string` | — | `4` | `open` | — | Valda | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pareiskejo_tipas` | `"Fizinis"` | — | — | Fizinis asmuo | — |
| `pareiskejo_tipas` | `"Juridinis"` | — | — | Juridinis asmuo | — |
| `pareiskejo_lytis` | `"V"` | — | — | Vyras | — |
| `pareiskejo_lytis` | `"M"` | — | — | Moteris | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `update(type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nma/nv_rusys.csv
