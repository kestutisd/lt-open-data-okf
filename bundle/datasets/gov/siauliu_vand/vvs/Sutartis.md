---
type: Table
title: "Sutartis — UAB „Šiaulių vandenys“ sutarčių duomenys"
description: "UAB „Šiaulių vandenys“ naudojamoje Verslo valdymo sistemoje (VVS) nuo 2017 m. kaupiami suteiktų paslaugų sąskaitų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/siauliu_vand/vvs/Sutartis"
tags: [gov, siauliu_vand, sutartis, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_vand/vvs.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/siauliu_vand/vvs.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2899/"
    title: "data.gov.lt DCAT-AP — datasets/gov/siauliu_vand/vvs"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Sutartis — UAB „Šiaulių vandenys“ sutarčių duomenys

UAB „Šiaulių vandenys“ naudojamoje Verslo valdymo sistemoje (VVS) nuo 2017 m. kaupiami suteiktų paslaugų sąskaitų duomenys. Duomenų rinkinyje kaupiami sutarčių su klientais duomenys. Rinkinio duomenų aprėptis laike – nuo 1991 m. Duomenų rinkinį sudaro: sutarties identifikatorius, kliento juridinio asmens pavadinimas arba fizinio asmens anonimizuotas vardas ir pavardė, juridinio arba fizinio asmens kodas, asmens rūšis (fizinis / juridinis), sutarties sudarymo, galiojimo pradžios ir pabaigos data, nurodyta, ar tai vandens, ar nuotekų paslaugų sutartis. Vienas įrašas atitinka vieną sutartį. Nors, anot turimų duomenų, VVS duomenys kaupiami nuo 2017 m., rinkiniui sudaryti panaudotuose duomenyse yra datų nuo 1753 m. iki 2122 m. Pirmasis metų skaičius dėl dažnumo laikytas nesančių duomenų atitikmeniu, todėl tų metų datos pakeistos į „null“ reikšmes. Likusios datos apribotos nuo 1991 m. iki šiandienos datos. Duomenų rinkinys sudarytas iš vienkartinio naudojimo duomenų, todėl nėra atnaujinamas. Duomenų teikėjas – UAB „Šiaulių vandenys“. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/siauliu_vand/vvs/Sutartis`[^manifest]
- **Dataset:** [UAB „Šiaulių vandenys“ sutarčių duomenys](../vvs.md) (`datasets/gov/siauliu_vand/vvs`)[^manifest]
- **Manifest CSV:** [datasets/gov/siauliu_vand/vvs.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_vand/vvs.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/siauliu_vand/vvs/Sutartis` (`deployed`)[^manifest]
- **Provider:** `siauliu_vand` — UAB „Šiaulių vandenys“ *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Kliento juridinio asmens pavadinimas arba fizinio asmens anonimizuoti vardas ir pavardė | — |
| `kodas` | `string` | — | `4` | `open` | — | Kliento juridinio arba fizinio asmens kodas | — |
| `kliento_asm_rusis` | `string` | — | `4` | `open` | — | Kliento asmens rūšis | — |
| `sutarties_sudarymo_data` | `date` | `D` | `4` | `open` | — | Sutarties sudarymo data | — |
| `sutartis_galioja_nuo` | `date` | `D` | `4` | `open` | — | Nuo kada galioja sutartis | — |
| `sutartis_galioja_iki` | `date` | `D` | `4` | `open` | — | Iki kada galioja sutartis | — |
| `ar_vandens_sutartis` | `string` | — | `4` | `open` | — | Ar sutartis yra vandens paslaugų sutartis | — |
| `ar_nuoteku_sutartis` | `string` | — | `4` | `open` | — | Ar sutartis yra nuotekų paslaugų sutartis | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `kliento_asm_rusis` | `"Fizinis"` | — | — | Fizinis | — |
| `kliento_asm_rusis` | `"Nežinoma"` | — | — | Nežinoma | — |
| `kliento_asm_rusis` | `"Juridinis"` | — | — | Juridinis | — |
| `ar_vandens_sutartis` | `"Taip"` | — | — | Taip | — |
| `ar_vandens_sutartis` | `"Ne"` | — | — | Ne | — |
| `ar_nuoteku_sutartis` | `"Taip"` | — | — | Taip | — |
| `ar_nuoteku_sutartis` | `"Ne"` | — | — | Ne | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/siauliu_vand/vvs.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_vand/vvs.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/siauliu_vand/vvs (https://data.gov.lt/datasets/2899/)
