---
type: Table
title: "PatyciuPrevencija — Smurto ir patyčių prevencijos programų vykdymas švietimo įstaigose."
description: "Viena eilutė atitinka faktą ar programa buvo įvykdyta švietimo įstaigoje atitinkamais mokslo metais."
resource: "https://get.data.gov.lt/datasets/gov/nsa/svis/prevencines_programos/PatyciuPrevencija"
tags: [gov, nsa, patyciuprevencija, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/svis/prevencines_programos.csv#L28"
    title: "atviriduomenys/manifest — datasets/gov/nsa/svis/prevencines_programos.csv#L28"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3890/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nsa/svis/prevencines_programos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PatyciuPrevencija — Smurto ir patyčių prevencijos programų vykdymas švietimo įstaigose.

Viena eilutė atitinka faktą ar programa buvo įvykdyta švietimo įstaigoje atitinkamais mokslo metais.[^manifest]

- **Model:** `datasets/gov/nsa/svis/prevencines_programos/PatyciuPrevencija`[^manifest]
- **Dataset:** [Prevencinių programų vykdymas švietimo įstaigose](../prevencines_programos.md) (`datasets/gov/nsa/svis/prevencines_programos`)[^manifest]
- **Manifest CSV:** [datasets/gov/nsa/svis/prevencines_programos.csv#L28](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/svis/prevencines_programos.csv#L28)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/svis/prevencines_programos/PatyciuPrevencija` (`deployed`)[^manifest]
- **Provider:** `nsa` — Nacionalinė švietimo agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus pirminis raktas | — |
| `mokslo_metai` | `string` | — | `4` | `open` | — | Mokslo metai | — |
| `padalinio_grupe` | `string` | — | `4` | `open` | — | Padalinio grupė | — |
| `padalinio_priklausomybe` | `string` | — | `4` | `open` | — | Padalinio priklausomybė | — |
| `padalinio_savivaldybe` | `string` | — | `4` | `open` | — | Padalinio savivaldybė | — |
| `padalinio_pavadinimas` | `string` | — | `4` | `open` | — | Padalinio pavadinimas | — |
| `padalinio_kodas` | `string` | — | `4` | `open` | — | Padalinio kodas | — |
| `programos_kodas` | `string` | — | `4` | `open` | — | Programos kodas | — |
| `programos_pavadinimas` | `string` | — | `4` | `open` | — | Prevencinė programa | — |
| `ar_igyvendinama` | `string` | — | `4` | `open` | — | Ar programa buvo įgyvendinama Jūsų mokykloje | — |
| `parengtu_mokytoju` | `integer` | — | `4` | `open` | — | Pagal programą parengtų dirbti mokytojų skaičius | — |
| `parengtu_sp_specialistu` | `integer` | — | `4` | `open` | — | Pagal programą parengtų dirbti švietimo pagalbos specialistų skaičius | — |
| `vykdziusiu_mokytoju` | `integer` | — | `4` | `open` | — | Programą vykdžiusių mokytojų skaičius | — |
| `vykdziusiu_sp_specialistu` | `integer` | — | `4` | `open` | — | Programą vykdžiusių švietimo pagalbos specialistų skaičius | — |
| `dalyvavusiu_mokiniu` | `integer` | — | `4` | `open` | — | Programoje dalyvavusių mokinių skaičius | — |
| `priezastys` | `boolean` | — | `4` | `open` | — | Ar šią prevencinę programą mokykloje paskatino įsidiegti pastebėtos situacijos ar iššūkiai įgyvendinant Gyvenimo įgūdžių bendrųjų programų | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `padalinio_priklausomybe` | `"Savivaldybės"` | — | — | Savivaldybės | — |
| `padalinio_priklausomybe` | `"Nevalstybinė"` | — | — | Nevalstybinė | — |
| `padalinio_priklausomybe` | `"Valstybinė"` | — | — | Valstybinė | — |
| `ar_igyvendinama` | `"Taip"` | — | — | Taip | — |
| `ar_igyvendinama` | `"Ne"` | — | — | Ne | — |
| `ar_igyvendinama` | `"Vykdė OPKUS (Galioja iki 2024-2025)"` | — | — | Vykdė OPKUS (Galioja iki 2024-2025) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/svis/prevencines_programos.csv#L28 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/svis/prevencines_programos.csv#L28)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nsa/svis/prevencines_programos (https://data.gov.lt/datasets/3890/)
