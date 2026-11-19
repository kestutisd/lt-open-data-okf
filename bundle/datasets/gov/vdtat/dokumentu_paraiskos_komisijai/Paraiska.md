---
type: Table
title: "Paraiska — Pateiktos paraiškos VDTAT Komisijai dėl dokumentų ar blankų priskyrimo prie saugiųjų dokumentų ar blankų"
description: "Pateiktos paraiškos VDTAT Komisijai dėl Vyriausybės vertybinių popierių, banderolių, keleivinio transporto bilietų, oficialiųjų žymėjimo ženklų, dokumentų blankų vertinimo ir priskyrimo prie saugiųjų dokumentų ar saugiųjų dokumentų blankų"
resource: "https://get.data.gov.lt/datasets/gov/vdtat/dokumentu_paraiskos_komisijai/Paraiska"
tags: [gov, vdtat, paraiska, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vdtat/dokumentu_paraiskos_komisijai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vdtat/dokumentu_paraiskos_komisijai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2780/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vdtat/dokumentu_paraiskos_komisijai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Paraiska — Pateiktos paraiškos VDTAT Komisijai dėl dokumentų ar blankų priskyrimo prie saugiųjų dokumentų ar blankų

Pateiktos paraiškos VDTAT Komisijai dėl Vyriausybės vertybinių popierių, banderolių, keleivinio transporto bilietų, oficialiųjų žymėjimo ženklų, dokumentų blankų vertinimo ir priskyrimo prie saugiųjų dokumentų ar saugiųjų dokumentų blankų[^manifest]

- **Model:** `datasets/gov/vdtat/dokumentu_paraiskos_komisijai/Paraiska`[^manifest]
- **Dataset:** [Pateiktos paraiškos VDTAT Komisijai dėl dokumentų ar blankų priskyrimo prie saugiųjų dokumentų...](../dokumentu_paraiskos_komisijai.md) (`datasets/gov/vdtat/dokumentu_paraiskos_komisijai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vdtat/dokumentu_paraiskos_komisijai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vdtat/dokumentu_paraiskos_komisijai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vdtat/dokumentu_paraiskos_komisijai/Paraiska` (`deployed`)[^manifest]
- **Provider:** `vdtat` — Valstybės dokumentų technologinės apsaugos tarnyba prie FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `paraiskos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `technologines_apsaugos_lygis` | `"Aukščiausias"` | — | — | — | — |
| `technologines_apsaugos_lygis` | `"Aukštesnysis"` | — | — | — | — |
| `technologines_apsaugos_lygis` | `"Vidutinis"` | — | — | — | — |
| `technologines_apsaugos_lygis` | `"Žemiausias"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `teises_aktas_tvirtinantis_dokumenta_lt` | `update(property: "teises_aktas_tvirtinantis_dokumenta_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vdtat/dokumentu_paraiskos_komisijai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vdtat/dokumentu_paraiskos_komisijai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vdtat/dokumentu_paraiskos_komisijai (https://data.gov.lt/datasets/2780/)
