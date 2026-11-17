---
type: Table
title: "Paraiska"
description: "Spinta table datasets/gov/nzt/paraiskos/Paraiska (18 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nzt/paraiskos/Paraiska"
tags: [gov, nzt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nzt/paraiskos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nzt/paraiskos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Paraiska

- **Model:** `datasets/gov/nzt/paraiskos/Paraiska`[^manifest]
- **Dataset:** [Paraiškų įsigyti privačius žemės ir miškų ūkio paskirties sklypus duomenys](../paraiskos.md) (`datasets/gov/nzt/paraiskos`)
- **Manifest CSV:** [datasets/gov/nzt/paraiskos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nzt/paraiskos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nzt/paraiskos/Paraiska`
- **Primary Key (`ref`):** `paraiskos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paraiskos_id` | `string` | — | `4` | `open` | — | Paraiškos unikalus identifikatorius | — |
| `sutarties_nr` | `string` | — | `4` | `open` | — | Sutarties numeris | — |
| `pateikimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos pateikimo data | — |
| `prasymo_tipas` | `string` | — | `4` | `open` | — | Paraiškos prašymo tipas | — |
| `atstovavimas` | `string` | — | `4` | `open` | — | Paraiškos žemės ploto gavėjo atstovavimo statusas | — |
| `teikejo_vardas` | `string` | — | `4` | `open` | — | Paraiškos teikėjo pilnas vardas | — |
| `gavejo_asmens_kodas` | `string` | — | `4` | `open` | — | Žemės gavėjo asmens kodas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Sklypo savivaldybė | — |
| `prasytojo_tipas` | `string` | — | `4` | `open` | — | Žemės gavėjo tipas | — |
| `atsakingas_darbuotojas` | `string` | — | `4` | `open` | — | Darbuotojas dirbantis su paraiška | — |
| `sprendimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos būsenos keitimo data | — |
| `sprendimas` | `string` | — | `4` | `open` | — | Paraiškos būsena | — |
| `paslaugos_suma` | `number` | — | `4` | `open` | — | Paraiškos teikimo mokestis | Valstybės rinkliava kurios dydis yra nustatytas nutarimu Nr. 1458 'Dėl Konkrečių valstybės rinkliavos dydžių ir šios rinkliavos mokėjimo ir grąžinimo taisyklių patvirtinimo' |
| `operacijos_data` | `date` | `D` | `4` | `open` | — | Paraiškos teikimo mokesčio mokėjimo data | — |
| `sutartiniai_gyvuliai` | `number` | — | `4` | `open` | — | Sutartinių gyvulių (SG) skaičius | Skaičiuojamas pagal žemės ūkio ministro įsakymo Nr. 3D-246 priedą 'Dėl ūkinių gyvūnų perskaičiavimo į sutartinius gyvulius' |
| `bendras_prasytojo_valdomas_plotas` | `number` | — | `4` | `open` | — | Bendras su susijusiais asmenimis prasytojo turimas žemės plotas hektarais | — |
| `bendras_plotas_po_isigyjimo` | `number` | — | `4` | `open` | — | Bendras su susijusiais asmenimis prasytojo turimas žemės plotas po žemės įsigijimo hektarais | — |
| `isigyjamas_plotas` | `number` | — | `4` | `open` | — | Įsigyjamas plotas hektarais | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `prasymo_tipas` | `"Įsigyti miškų ūkio paskirties žemę"` | — | — | — | — |
| `prasymo_tipas` | `"Įsigyti žemės ūkio paskirties žemę"` | — | — | — | — |
| `prasytojo_tipas` | `"FA"` | — | — | Žemės gavėjas Fizinis Asmuo | — |
| `prasytojo_tipas` | `"Sutuoktiniai"` | — | — | Žemės gavėjai sutuoktiniai | — |
| `prasytojo_tipas` | `"JA"` | — | — | Žemės gavėjas juridinis Asmuo | — |
| `prasytojo_tipas` | `"SutuoktiniaiUzsienieciai"` | — | — | Žemės gavėjai sutuoktiniai užsieniečiai | — |
| `prasytojo_tipas` | `"Uzsienietis"` | — | — | Žemės gavėjas užsienietis fizinis asmuo | — |
| `sprendimas` | `"Suformuoti sutikimą"` | — | — | — | — |
| `sprendimas` | `"Atmesti prašymą"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paslaugos_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | Valstybės rinkliava kurios dydis yra nustatytas nutarimu Nr. 1458 'Dėl Konkrečių valstybės rinkliavos dydžių ir šios rinkliavos mokėjimo ir grąžinimo taisyklių patvirtinimo' |

[^manifest]: atviriduomenys/manifest — datasets/gov/nzt/paraiskos.csv
