---
type: Table
title: "Paraiska — Pateiktos paraiškos VDTAT Komisijai dėl dokumentų ar blankų priskyrimo prie saugiųjų dokumentų ar blankų"
description: "Pateiktos paraiškos VDTAT Komisijai dėl Vyriausybės vertybinių popierių, banderolių, keleivinio transporto bilietų, oficialiųjų žymėjimo ženklų, dokumentų blankų vertinimo ir priskyrimo prie saugiųjų dokumentų ar saugiųjų dokumentų blankų"
resource: "https://get.data.gov.lt/datasets/gov/vdtat/dokumentu_paraiskos_komisijai/Paraiska"
tags: [gov, vdtat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vdtat/dokumentu_paraiskos_komisijai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vdtat/dokumentu_paraiskos_komisijai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Paraiska — Pateiktos paraiškos VDTAT Komisijai dėl dokumentų ar blankų priskyrimo prie saugiųjų dokumentų ar blankų

Pateiktos paraiškos VDTAT Komisijai dėl Vyriausybės vertybinių popierių, banderolių, keleivinio transporto bilietų, oficialiųjų žymėjimo ženklų, dokumentų blankų vertinimo ir priskyrimo prie saugiųjų dokumentų ar saugiųjų dokumentų blankų

- **Model:** `datasets/gov/vdtat/dokumentu_paraiskos_komisijai/Paraiska`[^manifest]
- **Dataset:** [Pateiktos paraiškos VDTAT Komisijai dėl dokumentų ar blankų priskyrimo prie saugiųjų dokumentų ar blankų](../dokumentu_paraiskos_komisijai.md) (`datasets/gov/vdtat/dokumentu_paraiskos_komisijai`)
- **Manifest CSV:** [datasets/gov/vdtat/dokumentu_paraiskos_komisijai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vdtat/dokumentu_paraiskos_komisijai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vdtat/dokumentu_paraiskos_komisijai/Paraiska`
- **Primary Key (`ref`):** `paraiskos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paraiskos_id` | `string` | — | `4` | `open` | — | Paraiškos identifikatorius | — |
| `dokumento_ar_blanko_pavadinimas` | `string` | — | `4` | `open` | — | Dokumento ar blanko pavadinimas | — |
| `besikreipiancios_istaigos_pavadinimas` | `string` | — | `4` | `open` | — | Besikreipiančios įstaigos pavadinimas | — |
| `besikreipiancios_istaigos_tipas` | `string` | — | `4` | `open` | — | Besikreipiančios įstaigos tipas | — |
| `besikreipiancios_istaigos_savivaldybe` | `string` | — | `4` | `open` | — | Besikreipiančios įstaigos savivaldybė | — |
| `privalomosios_formos_kodas` | `string` | — | `4` | `open` | — | Privalomosios formos kodas | — |
| `teises_aktas_tvirtinantis_dokumenta_lt` | `string` | — | `4` | `open` | — | Teisės aktas tvirtinantis dokumentą | — |
| `akto_data` | `date` | `D` | `4` | `open` | — | Akto data | — |
| `paraiskos_gavimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos gavimo data | — |
| `technologines_apsaugos_lygis` | `string` | — | `4` | `open` | — | Technologinės apsaugos lygis | — |
| `technologines_apsaugos_polygis` | `string` | — | `4` | `open` | — | Technologinės apsaugos polygis | — |
| `iregistravimo_registre_data` | `date` | `D` | `4` | `open` | — | Įregistravimo registre data | — |
| `dokumento_tipas` | `string` | — | `4` | `open` | — | Dokumento tipas | — |
| `komisijos_sprendimo_nuoroda` | `string` | — | `4` | `open` | — | Komisijos sprendimo nuoroda | — |
| `paskelbta_viesai` | `string` | — | `4` | `open` | — | Paskelbtas viešai | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `technologines_apsaugos_lygis` | `"Aukščiausias"` | — | — | — | — |
| `technologines_apsaugos_lygis` | `"Aukštesnysis"` | — | — | — | — |
| `technologines_apsaugos_lygis` | `"Vidutinis"` | — | — | — | — |
| `technologines_apsaugos_lygis` | `"Žemiausias"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `teises_aktas_tvirtinantis_dokumenta_lt` | `update(property: "teises_aktas_tvirtinantis_dokumenta_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vdtat/dokumentu_paraiskos_komisijai.csv
