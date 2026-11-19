---
type: Table
title: "MarijampolesRajSav"
description: "Duomenų rinkinys pateikia informaciją apie savivaldybių sudarytas sutartis dėl nekilnojamojo turto nuomos, pardavimo ar naudojimo."
resource: "https://get.data.gov.lt/datasets/gov/tvs/sutartys/MarijampolesRajSav"
tags: [gov, tvs, marijampolesrajsav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tvs/sutartys.csv#L40"
    title: "atviriduomenys/manifest — datasets/gov/tvs/sutartys.csv#L40"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# MarijampolesRajSav

**Dataset Context:** Duomenų rinkinys pateikia informaciją apie savivaldybių sudarytas sutartis dėl nekilnojamojo turto nuomos, pardavimo ar naudojimo. Įtraukiama informacija apie sutarties tipą, sudarymo ir galiojimo datas, sutarties vertę, šalis, atsakingas institucijas bei kitus reikšmingus aspektus. Duomenys atnaujinami periodiškai, laikantis teisės aktų reikalavimų dėl duomenų atvėrimo. Duomenų teikėjas: Savivaldybių administracijos. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/tvs/sutartys/MarijampolesRajSav`[^manifest]
- **Dataset:** [Duomenys apie savyvaldybės sudarytas sutartis](../sutartys.md) (`datasets/gov/tvs/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/tvs/sutartys.csv#L40](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tvs/sutartys.csv#L40)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/tvs/sutartys/MarijampolesRajSav` (`deployed`)[^manifest]
- **Provider:** `tvs` — Savivaldybių turto valdymo duomenų rinkinys *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `asm_identifikacija` | `string` | — | `4` | `open` | — | Asmens identifikacija | — |
| `ak_validacija` | `string` | — | `4` | `open` | — | Asmens kodo validacija | — |
| `jar_kodo_validacija` | `string` | — | `4` | `open` | — | JAR kodo validacija | — |
| `sutarties_salis_tipas` | `string` | — | `4` | `open` | — | Mokėtojo tipas | — |
| `sutarties_tipas` | `string` | — | `4` | `open` | — | Sutarties tipas | — |
| `vardas_pavarde` | `string` | — | `4` | `open` | — | Asmens vardas ir pavardė | — |
| `lytis_asmk` | `string` | — | `4` | `open` | — | Lytis iš asmens kodo | — |
| `gim_metai_asmk` | `date` | `Y` | `4` | `open` | — | Gimimo metai iš asmens kodo | — |
| `mirties_metai` | `date` | `D` | `4` | `open` | — | Mirties data | — |
| `istaiga` | `string` | — | `4` | `open` | — | Įstaigos pavadinimas | — |
| `bankroto_data` | `date` | `D` | `4` | `open` | — | Įstaigos bankroto data | — |
| `menesio_imokos_suma` | `number` | — | `4` | `open` | — | Mėnesio nuomos suma | — |
| `sutart_isigal_data` | `date` | `D` | `4` | `open` | — | Sutarties įsigaliojimo data | — |
| `sutart_nutrauk_data` | `date` | `D` | `4` | `open` | — | Sutarties nutraukimo data | — |
| `teisinis_pagrindas` | `string` | — | `4` | `open` | — | Teisinis sutarties pagrindas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/tvs/sutartys.csv#L40 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tvs/sutartys.csv#L40)
