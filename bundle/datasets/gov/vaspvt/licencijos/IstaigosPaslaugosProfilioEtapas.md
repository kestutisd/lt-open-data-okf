---
type: Table
title: "IstaigosPaslaugosProfilioEtapas — Sveikatos priežiūros įstaigų paslaugų profilių etapai"
description: "Spinta table datasets/gov/vaspvt/licencijos/IstaigosPaslaugosProfilioEtapas (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/IstaigosPaslaugosProfilioEtapas"
tags: [gov, vaspvt, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L129"
    last_modified: "2026-11-11T14:39:20Z"
---

# IstaigosPaslaugosProfilioEtapas — Sveikatos priežiūros įstaigų paslaugų profilių etapai

- **Model:** `datasets/gov/vaspvt/licencijos/IstaigosPaslaugosProfilioEtapas`[^manifest]
- **Dataset:** [Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba](../licencijos.md) (`datasets/gov/vaspvt/licencijos`)
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L129](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L129)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/IstaigosPaslaugosProfilioEtapas`
- **Primary Key (`ref`):** `id`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `profilis` | `string` | — | `4` | `open` | — | Paslaugos profilio identifikatorius | — |
| `etapas` | `string` | — | `4` | `open` | — | Etapo identifikatorius | — |
| `paslauga` | `string` | — | `4` | `open` | — | Paslaugos identifikatorius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(ref: "id")` | `ref` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv
