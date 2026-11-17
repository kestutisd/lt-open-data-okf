---
type: Table
title: "NtrZemesSklypas"
description: "Spinta table datasets/gov/rc/ntr/ntr_zemes_sklypai/NtrZemesSklypas (22 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_zemes_sklypai/NtrZemesSklypas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_zemes_sklypai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_zemes_sklypai.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# NtrZemesSklypas

- **Model:** `datasets/gov/rc/ntr/ntr_zemes_sklypai/NtrZemesSklypas`[^manifest]
- **Dataset:** [Nekilnojamojo turto registre įregistruotų žemės sklypų duomenys pagal savivaldybes](../ntr_zemes_sklypai.md) (`datasets/gov/rc/ntr/ntr_zemes_sklypai`)
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_zemes_sklypai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_zemes_sklypai.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_zemes_sklypai/NtrZemesSklypas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Objekto identifikatorius | Dirbtinis nekinojamojo turto objekto identifikatorius |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybė | Savivaldybės pavadinimas |
| `seniunija` | `ref` | [/datasets/gov/rc/ar/seniunija/Seniunija](../../ar/seniunija/Seniunija.md) | `4` | `open` | — | Seniūnija | Savivaldybėje esančios seniūnijos pavadinimas |
| `pask_tipas` | `ref` | [/datasets/gov/rc/ntr/ntr_paskirtys/NtrPaskirtiesTipas](../ntr_paskirtys/NtrPaskirtiesTipas.md) | `4` | `open` | — | Paskirties tipas | Pagrindinė žemės sklypo naudojimo paskirtis |
| `naub_budas[]` | `ref` | [/datasets/gov/rc/ntr/ntr_naudojimo_budai/NtrNaudojimoBudas](../ntr_naudojimo_budai/NtrNaudojimoBudas.md) | `4` | `open` | — | Naudojimo būdas | Žemės naudojimo būdas |
| `sklypo_pl` | `number` | — | `3` | `open` | — | Žemės sklypo plotas | Žemės sklypo plotas |
| `naudmenu_pl` | `number` | — | `3` | `open` | — | Naudmenų plotas | Bendras žemės sklype esančių žemės ūkio naudmenų žemės plotas |
| `ariamas_pl` | `number` | — | `3` | `open` | — | Ariamos žemės plotas | Žemės sklype esančios ariamos žemės naudmenos žemės plotas |
| `sodu_pl` | `number` | — | `3` | `open` | — | Sodu plotas | Žemės sklype esančios sodų naudmenos žemės plotas |
| `pievu_pl` | `number` | — | `3` | `open` | — | Pievų plotas | Žemės sklype esančios pievų naudmenos žemės plotas |
| `misko_pl` | `number` | — | `3` | `open` | — | Miško plotas | Žemės sklype esančios miško naudmenos žemės plotas |
| `keliu_pl` | `number` | — | `3` | `open` | — | Kelių plotas | Žemės sklype esančios kelių naudmenos žemės plotas |
| `uzstatytas_pl` | `number` | — | `3` | `open` | — | Užstatyta teritorija | Žemės sklype esančios užstatytos žemės plotas |
| `vandens_pl` | `number` | — | `3` | `open` | — | Vandens telkinių plotas | Žemės sklype esančios vandens telkinių naudmenos žemės plotas |
| `kitos_z_pl` | `number` | — | `3` | `open` | — | Kitos žemės plotas | Žemės sklype esančios kitos žemės naudmenos žemės plotas |
| `zeldiniu_pl` | `number` | — | `3` | `open` | — | Želdinių plotas | Žemės sklype esančios želdinių naudmenos žemės plotas |
| `pelkiu_pl` | `number` | — | `3` | `open` | — | Pelkių plotas | Žemės sklype esančios pelkių naudmenos žemės plotas |
| `pazeistos_z_pl` | `number` | — | `3` | `open` | — | Pažeistos žemės plotas | Žemės sklype esančios pažeistos žemės naudmenos žemės plotas |
| `nenaudojamos_z_pl` | `number` | — | `3` | `open` | — | Nenaudojamos žemės plotas | Žemės sklype esančios nenaudojamos žemės naudmenos žemės plotas |
| `nusausintos_z_pl` | `number` | — | `3` | `open` | — | Nusausintos žemės plotas | Žemės sklype esančios nusausintos žemės plotas |
| `drekinamos_z_pl` | `number` | — | `3` | `open` | — | Drėkinamos žemės plotas | Žemės sklype esančios drėkinamos žemės plotas |
| `nasumo_balas` | `integer` | — | `3` | `open` | — | Naudmenų našumo balas | Žemės sklypo žemės naudmenų našumo balas |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_zemes_sklypai.csv
