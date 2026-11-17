---
type: Table
title: "Sutartis — SR archyviniai duomenys apie sutartis pagal rūšis"
description: "Spinta table datasets/gov/rc/sr/sutartys/Sutartis (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/sr/sutartys/Sutartis"
tags: [gov, rc, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/sr/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/sr/sutartys.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sutartis — SR archyviniai duomenys apie sutartis pagal rūšis

- **Model:** `datasets/gov/rc/sr/sutartys/Sutartis`[^manifest]
- **Dataset:** [Reorganizuoto Sutarčių registro (SR) archyviniai duomenys](../sutartys.md) (`datasets/gov/rc/sr/sutartys`)
- **Manifest CSV:** [datasets/gov/rc/sr/sutartys.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/sr/sutartys.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/sr/sutartys/Sutartis`
- **Primary Key (`ref`):** `dok_nr, turto_tipas`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dok_nr` | `integer` | — | `3` | `open` | — | Sutarties dirbtinis identifikatorius šiame duomenų rinkinyje | — |
| `ireg_data` | `date` | `D` | `4` | `open` | — | Sutarties įregistravimo data | — |
| `sutarties_tipas` | `ref` | [/datasets/gov/rc/sr/klasifikatoriai/SutartiesTipas](../klasifikatoriai/SutartiesTipas.md) | `4` | `open` | — | Sutarties tipo aprašymas | — |
| `sut_data` | `date` | `D` | `4` | `open` | — | Sutarties data | — |
| `atsis_term` | `date` | `D` | `4` | `open` | — | Galutinis atsiskaitymo terminas (metai) | — |
| `turto_tipas` | `ref` | [/datasets/gov/rc/sr/klasifikatoriai/TurtoTipas](../klasifikatoriai/TurtoTipas.md) | `4` | `open` | — | Turto tipas | — |
| `dav_asmens_tipas` | `string` | — | `2` | `open` | — | Davėjo asmens tipas | — |
| `dav_valstybe` | `string` | — | `2` | `open` | — | Davėjo valstybė | — |
| `dav_valstybes_kodas` | `string` | — | `2` | `open` | — | Davėjo valstybės kodas | — |
| `gav_asmens_tipas` | `string` | — | `2` | `open` | — | Gavėjo asmens tipas | — |
| `gav_valstybe` | `string` | — | `2` | `open` | — | Gavėjo valstybė | — |
| `gav_valstybes_kodas` | `string` | — | `2` | `open` | — | Gavėjo valstybės kodas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `dav_asmens_tipas` | `"FA"` | — | — | Fizinis asmuo | — |
| `dav_asmens_tipas` | `"JA"` | — | — | Juridinis asmuo | — |
| `dav_valstybe` | `"LT"` | — | — | Lietuva | — |
| `dav_valstybe` | `"UZS"` | — | — | Užsienio valstybė | — |
| `gav_asmens_tipas` | `"FA"` | — | — | Fizinis asmuo | — |
| `gav_asmens_tipas` | `"JA"` | — | — | Juridinis asmuo | — |
| `gav_valstybe` | `"LT"` | — | — | Lietuva | — |
| `gav_valstybe` | `"UZS"` | — | — | Užsienio valstybė | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dav_asmens_tipas` | `create(property: "davejas", type: "ref", ref: "Davejas")` | `property` | `4` | `open` | — | — | — |
| `dav_asmens_tipas` | `update(property: "davejas.asmens_tipas", type: "")` | `property` | `4` | `open` | — | — | — |
| `dav_valstybe` | `update(property: "davejas.valstybe", type: "")` | `property` | `4` | `open` | — | — | — |
| `dav_valstybes_kodas` | `update(property: "davejas.valstybes_kodas", type: "")` | `property` | `4` | `open` | — | — | — |
| `gav_asmens_tipas` | `create(property: "gavejas", type: "ref", ref: "Gavejas")` | `property` | `4` | `open` | — | — | — |
| `gav_asmens_tipas` | `update(property: "gavejas.asmens_tipas", type: "")` | `property` | `4` | `open` | — | — | — |
| `gav_valstybe` | `update(property: "gavejas.valstybe", type: "")` | `property` | `4` | `open` | — | — | — |
| `gav_valstybes_kodas` | `update(property: "gavejas.valstybes_kodas", type: "")` | `property` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/sr/sutartys.csv
