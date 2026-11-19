---
type: Table
title: "Dokumentas — Saugiųjų dokumentų ir saugiųjų dokumentų blankų aprašomieji duomenys"
description: "Valstybės saugiųjų dokumentų ir saugiųjų dokumentų blankų, tokių kaip tokių kaip pasai, asmens tapatybės kortelės, kelionės dokumentai, vairuotojo pažymėjimai, akcizais apmokestinamų prekių banderolės, aukštojo mokslo diplomai ir kt., registro aprašomieji duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vdtat/saugiuju_dokumentu_registras/Dokumentas"
tags: [gov, vdtat, dokumentas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2781/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vdtat/saugiuju_dokumentu_registras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Dokumentas — Saugiųjų dokumentų ir saugiųjų dokumentų blankų aprašomieji duomenys

Valstybės saugiųjų dokumentų ir saugiųjų dokumentų blankų, tokių kaip tokių kaip pasai, asmens tapatybės kortelės, kelionės dokumentai, vairuotojo pažymėjimai, akcizais apmokestinamų prekių banderolės, aukštojo mokslo diplomai ir kt., registro aprašomieji duomenys[^manifest]

- **Model:** `datasets/gov/vdtat/saugiuju_dokumentu_registras/Dokumentas`[^manifest]
- **Dataset:** [Saugiųjų dokumentų ir saugiųjų dokumentų blankų registro duomenys](../saugiuju_dokumentu_registras.md) (`datasets/gov/vdtat/saugiuju_dokumentu_registras`)[^manifest]
- **Manifest CSV:** [datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vdtat/saugiuju_dokumentu_registras/Dokumentas` (`deployed`)[^manifest]
- **Provider:** `vdtat` — Valstybės dokumentų technologinės apsaugos tarnyba prie FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Eilutės identifikatorius | — |
| `dokumento_ar_blanko_id` | `string` | — | `4` | `open` | — | Dokumento ar blanko identifikatorius | — |
| `blanko_identifikacinis_kodas` | `string` | — | `4` | `open` | — | Dokumento ar blanko identifikacinis kodas | — |
| `dokumento_pavadinimas` | `string` | — | `4` | `open` | — | Dokumento ar blanko pavadinimas | — |
| `tvirtinanti_istaiga` | `string` | — | `4` | `open` | — | Tvirtinanti įstaiga | — |
| `istaigos_isleidziancios_dokumenta_pavadinimas` | `string` | — | `4` | `open` | — | Įstaigos išleidžiančios dokumentą ar blanką pavadinimas | — |
| `teises_aktas_tvirtinantis_dokumenta_lt` | `string` | — | `4` | `open` | — | Teisės aktas tvirtinantis dokumentą ar blanką | — |
| `dokumento_pastabos` | `string` | — | `4` | `open` | — | Pastabos apie dokumentą | — |
| `iregistravimo_data` | `date` | `D` | `4` | `open` | — | Dokumento ar blanko įregistravimo registre data | — |
| `pastabos_apie_galiojima` | `string` | — | `4` | `open` | — | Pastabos apie dokumento galiojimą | — |
| `dokumento_statusas` | `string` | — | `4` | `open` | — | Dokumento ar blanko statusas | — |
| `archyvinis` | `boolean` | — | `4` | `open` | — | Požymis ar dokumentas arba blankas archyvinis | — |
| `archyvavimo_data` | `date` | `D` | `4` | `open` | — | Dokumento ar blanko archyvavimo data | — |
| `isregistruojanti_istaiga` | `string` | — | `4` | `open` | — | Dokumentą ar blanką išregistruojanti įstaiga | — |
| `isregistravimo_data` | `date` | `D` | `4` | `open` | — | Dokumento ar blanko įšregistravimo data | — |
| `istaiga_kuruojanti_sriti` | `string` | — | `4` | `open` | — | Įstaiga kuruojanti dokumento ar blanko sritį | — |
| `paskelbta_viesai_lt` | `string` | — | `4` | `open` | — | Vieta apie paskelbimą viešai | — |
| `dokumento_privalomosios_formos_kodas` | `string` | — | `4` | `open` | — | Dokumento ar blanko privalomosios formos kodas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `dokumento_statusas` | `"Patvirtintas"` | — | — | — | — |
| `dokumento_statusas` | `"Panaikintas su įgaliojimu"` | — | — | — | — |
| `dokumento_statusas` | `"Panaikintas be įgaliojimo"` | — | — | — | — |
| `isregistruojanti_istaiga` | `"Valstybės dokumentų technologinės apsaugos tarnyba prie Finansų ministerijos"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `teises_aktas_tvirtinantis_dokumenta_lt` | `update(property: "teises_aktas_tvirtinantis_dokumenta_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |
| `paskelbta_viesai_lt` | `update(property: "paskelbta_viesai_lt@lt", type: "text")` | — | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vdtat/saugiuju_dokumentu_registras.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vdtat/saugiuju_dokumentu_registras (https://data.gov.lt/datasets/2781/)
