---
type: Table
title: "Istaiga — Vilniaus mieste veikiančios švietimo įstaigos"
description: "Rinkinyje skelbiamos Vilniaus mieste rinkinio atnaujinimo metu veikiančios švietimo įstaigos: lopšeliai-darželiai, pradinės mokyklos, progimnazijos, gimnazijos, jaunimo ir suaugusiųjų mokymo centrai."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/svietimas/Istaiga"
tags: [gov, vilniaus_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/svietimo_istaigos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/svietimo_istaigos.csv#L10"
    last_modified: "2026-11-11T14:39:20Z"
---

# Istaiga — Vilniaus mieste veikiančios švietimo įstaigos

Rinkinyje skelbiamos Vilniaus mieste rinkinio atnaujinimo metu veikiančios švietimo įstaigos: lopšeliai-darželiai, pradinės mokyklos, progimnazijos, gimnazijos, jaunimo ir suaugusiųjų mokymo centrai. Pateikiami įstaigų vietos (seniūnija, adresas, koordinatės) bei kontaktiniai (darbo laikas, telefono numeris, elektroninis paštas, nuoroda į įstaigos internetinį puslapį) duomenys.

- **Model:** `datasets/gov/vilniaus_m_sav/svietimas/Istaiga`[^manifest]
- **Dataset:** [Vilniaus mieste veikiančios švietimo įstaigos](../svietimas.md) (`datasets/gov/vilniaus_m_sav/svietimas`)
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/svietimo_istaigos.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/svietimo_istaigos.csv#L10)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/svietimas/Istaiga`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `seniunija` | `string` | — | `4` | `open` | — | Seniūnijos pavadinimas | — |
| `istaiga` | `string` | — | `4` | `open` | — | Švietimo įstaigos pavadinimas | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Įstaigos juridinio asmens kodas | — |
| `jar_validacija` | `boolean` | — | `4` | `open` | — | Juridinio asmens kodo validacija | — |
| `ar_veikia` | `boolean` | — | `4` | `open` | — | Požymis, ar įstaiga veikia rinkinio atnaujinimo metu | — |
| `adresas` | `string` | — | `4` | `open` | — | Įstaigos adresas | — |
| `tel_nr` | `string` | — | `2` | `open` | — | Įstaigos kontaktinis telefono numeris | — |
| `el_pastas` | `string` | — | `4` | `open` | — | Įstaigo elektroninio pašto adresas | — |
| `url` | `string` | — | `4` | `open` | — | Nuoroda į įstaigos internetinį puslapį | — |
| `darbo_laikas_lt` | `string` | — | `2` | `open` | — | Įstaigos darbo laikas | — |
| `geometrija_adp` | `geometry(3346)` | — | `4` | `open` | — | Įstaigos koordinatės (LKS) pagal pateiktą adresą | — |
| `duomenu_atnaujinimas` | `date` | `D` | `4` | `open` | — | Įstaigos duomenų atnaujinimo data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `darbo_laikas_lt` | `update(property: "darbo_laikas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/svietimo_istaigos.csv
