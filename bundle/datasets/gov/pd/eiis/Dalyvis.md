---
type: Table
title: "Dalyvis"
description: "Spinta table datasets/gov/pd/eiis/Dalyvis (29 columns)."
tags: [gov, pd, dalyvis, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/eiis.csv#L108"
    title: "atviriduomenys/manifest — datasets/gov/pd/eiis.csv#L108"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Dalyvis

- **Model:** `datasets/gov/pd/eiis/Dalyvis`[^manifest]
- **Dataset:** [datasets/gov/pd/eiis](../eiis.md) (`datasets/gov/pd/eiis`)[^manifest]
- **Manifest CSV:** [datasets/gov/pd/eiis.csv#L108](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/eiis.csv#L108)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `pd` — Policijos departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `dalyvis_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eismo_ivykis` | `ref` | [EismoIvykis](EismoIvykis.md) (`level=4 UUID`: `eismo_ivykis._id`) | `4` | — | — | — | — |
| `dalyvis_id` | `integer` | — | `4` | `open` | — | Dalyvio ID | — |
| `kategorija` | `string` | — | `3` | `open` | — | Kategorija | — |
| `dalyvio_tipas` | `string` | — | `4` | `open` | — | Dalyvio tipas | — |
| `pasisalino` | `string` | — | `4` | `open` | — | Pasišalino | — |
| `asmuo_nezinomas` | `string` | — | `4` | `open` | — | Asmuo nežinomas | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `pilietybe` | `string` | — | `3` | `open` | — | Pilietybė | — |
| `amzius` | `integer` | — | `3` | `open` | — | Amžius | — |
| `neigalumas` | `string` | — | `4` | `open` | — | Neigalumas | — |
| `saugos_dirzas` | `string` | — | `4` | `open` | — | Saugos diržas | — |
| `vaiko_kedes_naudojimas` | `number` | — | `3` | `open` | — | Vaiko kėdutė | — |
| `saugos_salmo_naudojimas` | `number` | — | `3` | `open` | — | Saugos šalmas | — |
| `oro_pagalves` | `string` | — | `4` | `open` | — | Oro pagalvės | — |
| `bukle` | `string` | — | `4` | `open` | — | Buklė | — |
| `detali_bukle` | `string` | — | `4` | `open` | — | Detali buklė | — |
| `suzalojimo_mastas` | `string` | — | `4` | `open` | — | Sužalojimo mastas | — |
| `vairuotojo_kvalifikacija` | `string` | — | `4` | `open` | — | Vairuotojo klasifikacija | — |
| `vairavimo_stazas` | `integer` | — | `3` | `open` | — | Vairavimo stažas | — |
| `busena` | `string` | — | `4` | `open` | — | Būsena | — |
| `detali_busena` | `string` | — | `4` | `open` | — | Detali būsena | — |
| `pap_busena` | `string` | — | `4` | `open` | — | Papildoma būsena | — |
| `det_pap_busena` | `string` | — | `3` | `open` | — | Detali papildoma būsena | — |
| `kaltininkas` | `string` | — | `4` | `open` | — | Kaltininkas | — |
| `girtumas_promilemis` | `number` | — | `3` | `open` | — | Girtumas (promilėmis) | — |
| `dalyvio_busena` | `string` | — | `4` | `open` | — | Dalyvio būsena | — |
| `teisenos_stadija_busena` | `string` | — | `4` | `open` | — | Teisenos stadijos būsena | — |
| `dalyvio_ket_pazeidimai[]` | `string` | — | `3` | `open` | — | Dalyvio KET pažeidimai | — |
| `transporto_priemone_id` | `integer` | — | `4` | `open` | — | Dalyvio tansporto priemonės ID | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `dalyvio_tipas` | `"Fizinis asmuo"` | — | — | Fizinis asmuo | — |
| `dalyvio_tipas` | `"Vairuotojas"` | — | — | Vairuotojas | — |
| `dalyvio_tipas` | `"Kitas asmuo"` | — | — | Kitas asmuo | — |
| `dalyvio_tipas` | `"Valstybės tarnautojas"` | — | — | Valstybės tarnautojas | — |
| `pasisalino` | `"Ne"` | — | — | Ne | — |
| `pasisalino` | `"Taip"` | — | — | Taip | — |
| `pasisalino` | `"Pasišalino"` | — | — | Pasišalino | — |
| `asmuo_nezinomas` | `"Ne"` | — | — | Ne | — |
| `asmuo_nezinomas` | `"Taip"` | — | — | Taip | — |
| `lytis` | `"Vyras"` | — | — | Vyras | — |
| `lytis` | `"Moteris"` | — | — | Moteris | — |
| `neigalumas` | `"Ne"` | — | — | Ne | — |
| `neigalumas` | `"Taip"` | — | — | Taip | — |
| `saugos_dirzas` | `"Užsegtas"` | — | — | Užsegtas | — |
| `saugos_dirzas` | `"Neužsegtas"` | — | — | Neužsegtas | — |
| `oro_pagalves` | `"Neįrengta"` | — | — | Neįrengta | — |
| `oro_pagalves` | `"Nesuveikė"` | — | — | Nesuvekė | — |
| `oro_pagalves` | `"Suveikė"` | — | — | Suveikė | — |
| `bukle` | `"Sužeistas"` | — | — | Sužeistas | — |
| `bukle` | `"Nenukentėjo"` | — | — | Nenukentėjo | — |
| `bukle` | `"Mirė nuo sužalojimų"` | — | — | Mirė nuo sužalojimų | — |
| `bukle` | `"Žuvo"` | — | — | Žuvo | — |
| `detali_bukle` | `"Gydomas stacionare"` | — | — | Gydomas stacionare | — |
| `detali_bukle` | `"Gydomas ambulatoriškai"` | — | — | Gydomas ambulatoriškai | — |
| `suzalojimo_mastas` | `"Atsisakyta nustatyti sveikatos sutrikdymo mastą"` | — | — | Atsisakyta nustatyti sveikatos sutrikdymo mastą | — |
| `suzalojimo_mastas` | `"Nežymus sveikatos sutrikdymas"` | — | — | Nežymus sveikatos sutrikdymas | — |
| `suzalojimo_mastas` | `"Nesunkus sveikatos sutrikdymas"` | — | — | Nesunkus sveikatos sutrikdymas | — |
| `suzalojimo_mastas` | `"Sunkus sveikatos sutrikdymas"` | — | — | Sunkus sveikatos sutrikdymas | — |
| `suzalojimo_mastas` | `"Sužalojimų nekonstatuota"` | — | — | Sužalojimų nekonstatuota | — |
| `vairuotojo_kvalifikacija` | `"Atitinka"` | — | — | Atitinka | — |
| `vairuotojo_kvalifikacija` | `"Neturi teisės vairuoti"` | — | — | Neturi teisės vairuoti | — |
| `busena` | `"Blaivus"` | — | — | Blaivus | — |
| `busena` | `"Neblaivus"` | — | — | Neblaivus | — |
| `detali_busena` | `"Atsisakė būti patikrintas"` | — | — | Atsisakė būti patikrintas | — |
| `detali_busena` | `"Lengvas neblaivumo (girtumo) laipsnis"` | — | — | Lengvas neblaivumo (girtumo) laipsnis | — |
| `detali_busena` | `"Neblaivus"` | — | — | Neblaivus | — |
| `detali_busena` | `"Nežymus neblaivumo (girtumo) laipsnis"` | — | — | Nežymus neblaivumo (girtumo) laipsnis | — |
| `detali_busena` | `"Sunkus neblaivumo (girtumo) laipsnis"` | — | — | Sunkus neblaivumo (girtumo) laipsnis | — |
| `detali_busena` | `"Vidutinis neblaivumo (girtumo) laipsnis"` | — | — | Vidutinis neblaivumo (girtumo) laipsnis | — |
| `pap_busena` | `"Neapsvaigęs"` | — | — | Neapsvaigęs | — |
| `pap_busena` | `"Neblaivus ir apsvaigęs"` | — | — | Neblaivus ir apsvaigęs | — |
| `kaltininkas` | `"Ne"` | — | — | Ne | — |
| `kaltininkas` | `"Taip"` | — | — | Taip | — |
| `dalyvio_busena` | `"KALTININKAS"` | — | — | Kaltininkas | — |
| `dalyvio_busena` | `"NEPAZEIDE"` | — | — | Nepažeidė | — |
| `dalyvio_busena` | `"GALIMAS KALTININKAS"` | — | — | Galimas kaltininkas | — |
| `teisenos_stadija_busena` | `"IKITEISMINIS"` | — | — | Ikitesminis | — |
| `teisenos_stadija_busena` | `"ADMINISTRACINIS"` | — | — | Administracinis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pd/eiis.csv#L108 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/eiis.csv#L108)
