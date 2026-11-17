---
type: Table
title: "Grupe — DRG grupių sąrašas"
description: "Informacija apie giminingų diagnozių grupes."
resource: "https://get.data.gov.lt/datasets/gov/vlk/drg/Grupe"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/drg.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Grupe — DRG grupių sąrašas

Informacija apie giminingų diagnozių grupes. Kiekvieną ADRG sudaro DRGs, kurios skiriasi pagal sunaudojamus išteklius. DRGs – tai detaliausias klasifikavimo lygmuo. ADRG dažniausiai skirstoma į DRGs pagal gydymo atvejo klinikinio sudėtingumo lygmenis.

- **Model:** `datasets/gov/vlk/drg/Grupe`[^manifest]
- **Dataset:** [datasets/gov/vlk/drg](../drg.md) (`datasets/gov/vlk/drg`)
- **Manifest CSV:** [datasets/gov/vlk/drg.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/drg/Grupe`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `string` | — | `4` | `open` | — | DRG kodas | Giminingų diagnozių grupės kodas |
| `pavadinimas` | `string` | — | `4` | `open` | — | DRG pavadinimas (LT) | Giminingų diagnozių grupės pavadinimas lietuvių kalba. |
| `adrg_kodas` | `string` | — | `2` | `open` | — | ADRG kodas | Gretimų giminingų diagnozių grupės kodas |
| `adrg_pavadinimas` | `string` | — | `2` | `open` | — | ADRG pavadinimas | Gretimų giminingų diagnozių grupės pavadinimas |
| `profilis` | `string` | — | `4` | `open` | — | Profilis | Giminingų diagnozių grupės profilis |
| `pdk_id` | `integer` | — | `2` | `open` | — | — | — |
| `pdk_kodas` | `string` | — | `2` | `open` | — | PDK kodas | Pagrindinės diagnostinės kategorijos (PDK) kodas |
| `pdk_pavadinimas` | `string` | — | `2` | `open` | — | PDK pavadinimas | Pagrindinės diagnostinės kategorijos (PDK) pavadinimas. |
| `versija` | `ref` | [Versija](Versija.md) | `4` | `open` | — | Nuoroda į DRG versijas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `profilis` | `'Chirurginis'` | — | — | Chirurginis | — |
| `profilis` | `'Kitas'` | — | — | Kitas | — |
| `profilis` | `'Terapinis'` | — | — | Terapinis | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `adrg_kodas` | `create(property: "adrg", type: "ref", ref: "Adrg")` | `property` | `4` | — | — | — | — |
| `adrg_kodas` | `update(property: "adrg.kodas", type: "")` | `property` | `4` | — | — | — | — |
| `adrg_pavadinimas` | `update(property: "adrg.pavadinimas", type: "")` | `property` | `4` | — | — | — | — |
| `pdk_id` | `create(property: "pdk", type: "ref", ref: "Pdk")` | `property` | `4` | — | — | — | — |
| `pdk_id` | `update(property: "pdk.id", type: "")` | `property` | `4` | — | — | — | — |
| `pdk_kodas` | `update(property: "pdk.kodas", type: "")` | `property` | `4` | — | — | — | — |
| `pdk_pavadinimas` | `update(property: "pdk.pavadinimas", type: "")` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/drg.csv
