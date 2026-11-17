---
type: Table
title: "Patalpa — Vilniaus miesto savivaldybės nuomojamos patalpos"
description: "Spinta table datasets/gov/vilniaus_m_sav/patalpos/Patalpa (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/patalpos/Patalpa"
tags: [gov, vilniaus_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/patalpos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/patalpos.csv#L10"
    last_modified: "2026-11-11T14:39:20Z"
---

# Patalpa — Vilniaus miesto savivaldybės nuomojamos patalpos

- **Model:** `datasets/gov/vilniaus_m_sav/patalpos/Patalpa`[^manifest]
- **Dataset:** [Vilniaus miesto savivaldybės nuomojamų patalpų sutarčių duomenys](../patalpos.md) (`datasets/gov/vilniaus_m_sav/patalpos`)
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/patalpos.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/patalpos.csv#L10)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/patalpos/Patalpa`
- **Primary Key (`ref`):** `patalpos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `patalpos_id` | `string` | — | `4` | `open` | — | Patalpos identifikacinis numeris | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Patalpos pavadinimas | — |
| `aprasymas_lt` | `string` | — | `2` | `open` | — | Patalpos aprašymas | — |
| `vietos_tipas` | `string` | — | `4` | `open` | — | Patalpos vietos tipas | — |
| `patalpos_tipas` | `string` | — | `4` | `open` | — | Patalpos tipas | — |
| `adresas` | `string` | — | `4` | `open` | — | Patalpos adresas | — |
| `seniunija` | `string` | — | `4` | `open` | — | Seniūnijos pavadinimas | — |
| `geometrija_adp` | `geometry(point, 3346)` | — | `4` | `open` | — | Patalpos adreso koordinatės (LKS) | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | Patalpos adreso ilgumos koordinatė | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Patalpos adreso platumos koordinatė | — |
| `istaiga_savininke` | `string` | — | `4` | `open` | — | Patalpų savininkas | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Patalpų savininko JAR kodas | — |
| `jar_kodas_validus` | `boolean` | — | `4` | `open` | — | JAR kodo validacijos požymis | — |
| `plotas_kv_m` | `number` | `m²` | `4` | `open` | — | Patalpų plotas, nurodytas kvadratiniais metrais | — |
| `statybos_data` | `date` | `D` | `4` | `open` | — | Pastato statybos data | — |
| `talpina_zmoniu` | `integer` | `U` | `4` | `open` | — | Nurodomas patalpoje telpančių asmenų skaičius | — |
| `duomenu_atnaujinimas` | `date` | `D` | `4` | `open` | — | Patalpos duomenų atnaujinimo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vietos_tipas` | `"Vidaus patalpa"` | — | — | — | — |
| `vietos_tipas` | `"Lauko erdve"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `aprasymas_lt` | `update(property: "aprasymas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/patalpos.csv
