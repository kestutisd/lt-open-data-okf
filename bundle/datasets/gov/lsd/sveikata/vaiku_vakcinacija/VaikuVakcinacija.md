---
type: Table
title: "VaikuVakcinacija — Prie įstaigos prisirašiusių nepilnamečių asmenų skaičius ir paskiepijimas nuo 2021 metų"
description: "\"Prie pirminės ambulatorinės asmens sveikatos priežiūros įstaigų prisirašiusių ir bent kartą paskiepytų nepilnamečių skaičius nuo 2021 metų."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/vaiku_vakcinacija/VaikuVakcinacija"
tags: [gov, lsd, vaikuvakcinacija, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/vaiku_vakcinacija.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/vaiku_vakcinacija.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3861/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/vaiku_vakcinacija"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# VaikuVakcinacija — Prie įstaigos prisirašiusių nepilnamečių asmenų skaičius ir paskiepijimas nuo 2021 metų

"Prie pirminės ambulatorinės asmens sveikatos priežiūros įstaigų prisirašiusių ir bent kartą paskiepytų nepilnamečių skaičius nuo 2021 metų. Duomenys parengti naudojantis SVEIDRA bei ESPBI IS informacija."[^manifest]

- **Model:** `datasets/gov/lsd/sveikata/vaiku_vakcinacija/VaikuVakcinacija`[^manifest]
- **Dataset:** [Prie įstaigos prisirašiusių nepilnamečių asmenų skaičius ir paskiepijimas nuo 2021 metų](../vaiku_vakcinacija.md) (`datasets/gov/lsd/sveikata/vaiku_vakcinacija`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/vaiku_vakcinacija.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/vaiku_vakcinacija.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/vaiku_vakcinacija/VaikuVakcinacija` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus kodas | — |
| `metai` | `integer` | — | `2` | `open` | — | "Metai, už kuriuos skaičiuojami prisirašę ir paskiepyti asmenys konkrečioje įstaigoje" | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Juridinio asmens kodas | — |
| `name` | `string` | — | `4` | `open` | — | Įstaigos pavadinimas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Įstaigos savivaldybės pavadinimas | — |
| `gyvenviete` | `string` | — | `4` | `open` | — | Įstaigos miestas/gyvenamoji vietovė | — |
| `adresas` | `string` | — | `4` | `open` | — | Įstaigos veiklos adresas | — |
| `aob_kodas` | `string` | — | `4` | `open` | — | Įstaigos veiklos vieneto veiklos/registracijos adreso kodas | — |
| `sveidra_id` | `string` | — | `4` | `open` | — | Įstaigos veiklos vieneto kodas SVEIDRA | — |
| `vidutiniskai_prisirasiusiuju` | `integer` | — | `4` | `open` | — | "Vidutinis tais metais įstaigoje prisirašiusių vaikų skaičius (bendrų prisirašymo dienų visiems įstaigoje prisirašiusiems nepilnamečiams, t.y. person-days, skaičius, padalintas iš metų trukmės)" | — |
| `prisirase_bent1d` | `integer` | — | `4` | `open` | — | Prie įstaigos prisirašiusių bent vieną dieną tais metais nepilnamečių skaičius | — |
| `paskiepyta_vaiku` | `integer` | — | `4` | `open` | — | "Įstaigoje paskiepytų unikalių nepilnamečių skaičius tais metais, neatsižvelgiant į jų prisirašymo vietą" | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type:"date", ref:"Y")` | `type` | `4` | — | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/vaiku_vakcinacija.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/vaiku_vakcinacija.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/vaiku_vakcinacija (https://data.gov.lt/datasets/3861/)
