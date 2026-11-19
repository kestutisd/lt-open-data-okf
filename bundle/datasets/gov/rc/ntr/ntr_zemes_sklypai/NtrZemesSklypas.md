---
type: Table
title: "NtrZemesSklypas"
description: "Spinta table datasets/gov/rc/ntr/ntr_zemes_sklypai/NtrZemesSklypas (22 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_zemes_sklypai/NtrZemesSklypas"
tags: [gov, rc, ntrzemessklypas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_zemes_sklypai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_zemes_sklypai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1811/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_zemes_sklypai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# NtrZemesSklypas

- **Model:** `datasets/gov/rc/ntr/ntr_zemes_sklypai/NtrZemesSklypas`[^manifest]
- **Dataset:** [Nekilnojamojo turto registre įregistruotų žemės sklypų duomenys pagal savivaldybes](../ntr_zemes_sklypai.md) (`datasets/gov/rc/ntr/ntr_zemes_sklypai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_zemes_sklypai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_zemes_sklypai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_zemes_sklypai/NtrZemesSklypas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Objekto identifikatorius | Dirbtinis nekinojamojo turto objekto identifikatorius |
| `savivaldybe` | `ref` | [Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybė | Savivaldybės pavadinimas |
| `seniunija` | `ref` | [Seniunija](../../ar/seniunija/Seniunija.md) (`level=4 UUID`: `seniunija._id`) | `4` | `open` | — | Seniūnija | Savivaldybėje esančios seniūnijos pavadinimas |
| `pask_tipas` | `ref` | [NtrPaskirtiesTipas](../ntr_paskirtys/NtrPaskirtiesTipas.md) (`level=4 UUID`: `pask_tipas._id`) | `4` | `open` | — | Paskirties tipas | Pagrindinė žemės sklypo naudojimo paskirtis |
| `naub_budas[]` | `ref` | [NtrNaudojimoBudas](../ntr_naudojimo_budai/NtrNaudojimoBudas.md) (`level=4 UUID`: `naub_budas[]._id`) | `4` | `open` | — | Naudojimo būdas | Žemės naudojimo būdas |
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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_zemes_sklypai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_zemes_sklypai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_zemes_sklypai (https://data.gov.lt/datasets/1811/)
