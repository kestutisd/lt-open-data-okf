---
type: Table
title: "VaikuVakcinacija — Prie įstaigos prisirašiusių nepilnamečių asmenų skaičius ir paskiepijimas nuo 2021 metų"
description: "Prie pirminės ambulatorinės asmens sveikatos priežiūros įstaigų prisirašiusių ir bent kartą paskiepytų nepilnamečių skaičius nuo 2021 metų."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/vaiku_vakcinacija/VaikuVakcinacija"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/vaiku_vakcinacija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/vaiku_vakcinacija.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# VaikuVakcinacija — Prie įstaigos prisirašiusių nepilnamečių asmenų skaičius ir paskiepijimas nuo 2021 metų

Prie pirminės ambulatorinės asmens sveikatos priežiūros įstaigų prisirašiusių ir bent kartą paskiepytų nepilnamečių skaičius nuo 2021 metų. Duomenys parengti naudojantis SVEIDRA bei ESPBI IS informacija.

- **Model:** `datasets/gov/lsd/sveikata/vaiku_vakcinacija/VaikuVakcinacija`[^manifest]
- **Dataset:** [Prie įstaigos prisirašiusių nepilnamečių asmenų skaičius ir paskiepijimas nuo 2021 metų](../vaiku_vakcinacija.md) (`datasets/gov/lsd/sveikata/vaiku_vakcinacija`)
- **Manifest CSV:** [datasets/gov/lsd/sveikata/vaiku_vakcinacija.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/vaiku_vakcinacija.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/vaiku_vakcinacija/VaikuVakcinacija`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus kodas | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai, už kuriuos skaičiuojami prisirašę ir paskiepyti asmenys konkrečioje įstaigoje | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Juridinio asmens kodas | — |
| `name` | `string` | — | `4` | `open` | — | Įstaigos pavadinimas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Įstaigos savivaldybės pavadinimas | — |
| `gyvenviete` | `string` | — | `4` | `open` | — | Įstaigos miestas/gyvenamoji vietovė | — |
| `adresas` | `string` | — | `4` | `open` | — | Įstaigos veiklos adresas | — |
| `aob_kodas` | `string` | — | `4` | `open` | — | Įstaigos veiklos vieneto veiklos/registracijos adreso kodas | — |
| `sveidra_id` | `string` | — | `4` | `open` | — | Įstaigos veiklos vieneto kodas SVEIDRA | — |
| `vidutiniskai_prisirasiusiuju` | `integer` | — | `4` | `open` | — | Vidutinis tais metais įstaigoje prisirašiusių vaikų skaičius (bendrų prisirašymo dienų visiems įstaigoje prisirašiusiems nepilnamečiams, t.y. person-days, skaičius, padalintas iš metų trukmės) | — |
| `prisirase_bent1d` | `integer` | — | `4` | `open` | — | Prie įstaigos prisirašiusių bent vieną dieną tais metais nepilnamečių skaičius | — |
| `paskiepyta_vaiku` | `integer` | — | `4` | `open` | — | Įstaigoje paskiepytų unikalių nepilnamečių skaičius tais metais, neatsižvelgiant į jų prisirašymo vietą | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type:"date", ref:"Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/vaiku_vakcinacija.csv
