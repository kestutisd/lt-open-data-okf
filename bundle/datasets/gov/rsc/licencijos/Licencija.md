---
type: Table
title: "Licencija — Licencijos"
description: "Spinta table datasets/gov/rsc/licencijos/Licencija (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rsc/licencijos/Licencija"
tags: [gov, rsc, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rsc/licencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsc/licencijos.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Licencija — Licencijos

- **Model:** `datasets/gov/rsc/licencijos/Licencija`[^manifest]
- **Dataset:** [datasets/gov/rsc/licencijos](../licencijos.md) (`datasets/gov/rsc/licencijos`)
- **Manifest CSV:** [datasets/gov/rsc/licencijos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsc/licencijos.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rsc/licencijos/Licencija`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `lic_nr` | `string` | — | `4` | `open` | — | Licencijos numeris | — |
| `isduota` | `date` | `D` | `4` | `open` | — | Licencijos išdavimo data | — |
| `busena` | `string` | — | `4` | `open` | — | Licencijos būsenos pavadinimas | — |
| `tipas` | `string` | — | `4` | `open` | — | Licencijų tipai | — |
| `ja_kodas` | `string` | — | `2` | `open` | — | Juridinio asmens kodas | — |
| `org_pav` | `string` | — | `1` | `open` | — | Juridinio asmens pavadinimas | — |
| `adresas` | `string` | — | `2` | `open` | — | Pilnas adresas | — |
| `uzs_adresas` | `string` | — | `1` | `open` | — | Adresas užsienio šalyse | — |
| `miesto_pozymis` | `boolean` | — | `4` | `open` | — | Požymis ar miestas | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybės pavadinimas | — |
| `salis` | `string` | — | `4` | `open` | — | Valstybės pavadinimas | — |
| `koord` | `geometry(point, 3346)` | — | `3` | `open` | — | Licenciją gaunančio juridinio asmens koordinatės | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `busena` | `"Panaikinta"` | — | — | Panaikinta | — |
| `busena` | `"Išduota"` | — | — | Išduota | — |
| `busena` | `"Sustabdytas galiojimas"` | — | — | Sustabdytas galiojimas | — |
| `tipas` | `"1"` | — | — | Licencija gaminti, naudoti, saugoti, prižiureti, remontuoti, perdirbti jonizuojanciosios spinduliuotes šaltinius ir (ar) tvarkyti (atlikti pradini radioaktyviuju atlieku apdorojima (rinkti, rušiuoti, dezaktyvuoti), atlikti pagrindini radioaktyviuju atlieku apdorojima, saugoti) radioaktyviasias atliekas | — |
| `tipas` | `"2"` | — | — | Licencija montuoti jonizuojančiosios spinduliuotės šaltinius | Nebegelioja |
| `tipas` | `"3"` | — | — | Licencija prekiauti jonizuojančiosios spinduliuotės šaltiniais | Nebegalioja |
| `tipas` | `"4"` | — | — | Licencija vežti radioaktyviąsias medžiagas ir (ar) radioaktyviąsias atliekas | — |
| `tipas` | `"6"` | — | — | Licencija vykdyti veiklą jonizuojančiosios spinduliuotės aplinkoje pas kitą asmenį, turintį licenciją | — |
| `tipas` | `"7"` | — | — | Licencija gaminti, naudoti (taip pat pakartotinai naudoti), saugoti, perdirbti jonizuojančiosios spinduliuotės šaltinius ir (ar) tvarkyti (atlikti pradinį radioaktyviųjų atliekų apdorojimą, atlikti pagrindinį radioaktyviųjų atliekų apdorojimą, saugoti) radioaktyviąsias atliekas | — |
| `tipas` | `"8"` | — | — | Licencija prekiauti, montuoti, prižiūrėti ir remontuoti jonizuojančiosios spinduliuotės šaltinius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ja_kodas` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `base` | `4` | `open` | — | — | — |
| `ja_kodas` | `update(type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rsc/licencijos.csv
