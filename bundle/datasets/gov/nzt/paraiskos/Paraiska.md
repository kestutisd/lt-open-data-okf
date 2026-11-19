---
type: Table
title: "Paraiska"
description: "\"Lentelėje pateikti Nacionalinės žemės tarnybos prie Aplinkos ministerijos išduotų sutikimų įsigyti žemės ir miškų ūkio paskirties sklypus duomenys."
resource: "https://get.data.gov.lt/datasets/gov/nzt/paraiskos/Paraiska"
tags: [gov, nzt, paraiska, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nzt/paraiskos.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/nzt/paraiskos.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3794/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nzt/paraiskos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Paraiska

**Dataset Context:** "Lentelėje pateikti Nacionalinės žemės tarnybos prie Aplinkos ministerijos išduotų sutikimų įsigyti žemės ir miškų ūkio paskirties sklypus duomenys. Rinkinys sudarytas Valstybės duomenų agentūros. Duomenys pateikiami nuo momento, kai paraiškos tampa aktualios tikrinimo procesui. Lentelės viena eilutė atitinka vieną paraišką. Atkreipiame dėmesį, kad duomenų eilutės yra nuolatos pildomos, o informacija jose yra tikslinama. Duomenys apima visoje Lietuvoje išsidėsčiusius juridinius bei fizinius asmenis. Duomenų laiko aprėptis – nuo 2022 m. sausio 1d. Duomenų teikėjas – Nacionalinės žemės tarnyba prie Aplinkos ministerijos. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt."[^manifest]

- **Model:** `datasets/gov/nzt/paraiskos/Paraiska`[^manifest]
- **Dataset:** [Paraiškų įsigyti privačius žemės ir miškų ūkio paskirties sklypus duomenys](../paraiskos.md) (`datasets/gov/nzt/paraiskos`)[^manifest]
- **Manifest CSV:** [datasets/gov/nzt/paraiskos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nzt/paraiskos.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nzt/paraiskos/Paraiska` (`deployed`)[^manifest]
- **Provider:** `nzt` — Nacionalinė žemės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `paraiskos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/nzt/paraiskos.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nzt/paraiskos.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nzt/paraiskos (https://data.gov.lt/datasets/3794/)
