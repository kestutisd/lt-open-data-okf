---
type: Table
title: "Skelbimas — Vilniaus miesto savivaldybės darbo skelbimai"
description: "Rinkinyje pateikiamos Vilniaus miesto savivaldybės administracijos skelbiamos laisvos darbo vietos savivaldybės ugdymo, gydymo bei kitose biudžetinėse įstaigose Vilniaus mieste."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/laisvos_darbo_vietos/Skelbimas"
tags: [gov, vilniaus_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/darbo_vietos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/darbo_vietos.csv#L11"
    last_modified: "2026-11-11T14:39:20Z"
---

# Skelbimas — Vilniaus miesto savivaldybės darbo skelbimai

Rinkinyje pateikiamos Vilniaus miesto savivaldybės administracijos skelbiamos laisvos darbo vietos savivaldybės ugdymo, gydymo bei kitose biudžetinėse įstaigose Vilniaus mieste. Duomenys apima laikotarpį nuo 2021m. iki dabar. Rinkinio objektas - vienos darbo vietos skelbimas. Pateikiami duomenys apie darbovietę (adresas, koordinatės, įstaigos tipas) ir siūlomą darbo vietą (pareigos, darbo vietos aprašymas, reikalavimai, atlyginimas, kontaktai pasiteiravimui).

Duomenų teikėjas: Vilniaus miesto savivaldybės administracija

Vilniaus miesto savivaldybės administracija

- **Model:** `datasets/gov/vilniaus_m_sav/laisvos_darbo_vietos/Skelbimas`[^manifest]
- **Dataset:** [Vilniaus miesto savivaldybės darbo skelbimai](../laisvos_darbo_vietos.md) (`datasets/gov/vilniaus_m_sav/laisvos_darbo_vietos`)
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/darbo_vietos.csv#L11](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/darbo_vietos.csv#L11)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/laisvos_darbo_vietos/Skelbimas`
- **Primary Key (`ref`):** `skelbimo_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `skelbimo_id` | `string` | — | `4` | `open` | — | Skelbimo identifikacinis numeris | — |
| `publikavimas` | `datetime` | `S` | `4` | `open` | — | Skelbimo publikavimo data | — |
| `galiojimo_pabaiga` | `date` | `D` | `4` | `open` | — | Skelbimo galiojimo pabaiga | — |
| `istaiga` | `string` | — | `4` | `open` | — | Darbo vietos įstaiga | — |
| `istaigos_tipas` | `string` | — | `4` | `open` | — | Įstaigos tipas | — |
| `adresas` | `string` | — | `4` | `open` | — | Darbo vietos adresas | — |
| `adp_geometrija` | `geometry(point, 3346)` | — | `4` | `open` | — | Adreso koordinatės | — |
| `pareigos_lt` | `string` | — | `4` | `open` | — | Pareigų pavadinimas | — |
| `pareigu_statusas` | `string` | — | `4` | `open` | — | Pareigų tipas | — |
| `etatas_lt` | `string` | — | `4` | `open` | — | Etato dydis | — |
| `atlyginimas_lt` | `string` | — | `4` | `open` | — | Siūlomas atlyginimas | — |
| `skelbimas_lt` | `string` | — | `4` | `open` | — | Skelbimo tekstas | — |
| `aprasymas_lt` | `string` | — | `4` | `open` | — | Darbo vietos aprašymas | — |
| `reikalavimas_lt` | `string` | — | `4` | `open` | — | Reikalavimai kandidatui | — |
| `naudos_lt` | `string` | — | `4` | `open` | — | Darbovietės siūlomos naudos | — |
| `kontaktas_lt` | `string` | — | `4` | `open` | — | Darbo vietos kontaktinė informacija | — |
| `skelbimo_url_lt` | `string` | — | `4` | `open` | — | Nuoroda į darbo skelbimą (veikia, kol skelbimo galiojimas nepasibaigęs) | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `istaigos_tipas` | `"Švietimo įstaigos"` | — | — | — | — |
| `istaigos_tipas` | `"Kitos įstaigos"` | — | — | — | — |
| `istaigos_tipas` | `"Vilniaus miesto savivaldybės administracija"` | — | — | — | — |
| `istaigos_tipas` | `"Įstaigų vadovai"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pareigos_lt` | `update(property: "pareigos_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `etatas_lt` | `update(property: "etatas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `atlyginimas_lt` | `update(property: "atlyginimas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `skelbimas_lt` | `update(property: "skelbimas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `aprasymas_lt` | `update(property: "aprasymas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `reikalavimas_lt` | `update(property: "reikalavimas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `naudos_lt` | `update(property: "naudos_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `kontaktas_lt` | `update(property: "kontaktas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `skelbimo_url_lt` | `update(property: "skelbimo_url_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/darbo_vietos.csv
