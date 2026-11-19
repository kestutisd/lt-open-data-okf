---
type: Table
title: "KraujoDonoras — \"Asmenų, pageidaujančių duoti kraujo arba kraujo komponentus, duomenys\""
description: "\"Lentelėje pateikiami duomenys apie asmenis, kurie pageidauja duoti kraujo arba kraujo komponentų, surinkti Higienos instituto Kraujo donorų registro informacinėje sistemoje."
resource: "https://get.data.gov.lt/datasets/gov/hi/kraujo_donacijos/KraujoDonoras"
tags: [gov, hi, kraujodonoras, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/kraujo_donacijos.csv#L15"
    title: "atviriduomenys/manifest — datasets/gov/hi/kraujo_donacijos.csv#L15"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3889/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/kraujo_donacijos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# KraujoDonoras — "Asmenų, pageidaujančių duoti kraujo arba kraujo komponentus, duomenys"

"Lentelėje pateikiami duomenys apie asmenis, kurie pageidauja duoti kraujo arba kraujo komponentų, surinkti Higienos instituto Kraujo donorų registro informacinėje sistemoje. Viena eilutė yra vienas asmuo su jam priskirtu donoro identifikaciniu numeriu (pasitaiko atvejų, kai žmogus turi kelis donoro identifikacinius numerius, todėl vieno donoro identifikacinio numerio negalime prilyginti vienam unikaliam asmeniui). Eilutėje nurodomas šifruotas donoro identifikacinis numeris, asmens kodas, asmens kodo validacijos įvertis, donuojančio asmens gimimo metai, lytis, pirmoji valstybė ir savivaldybė (jeigu Lietuvoje), kurioje asmuo registravo savo gyvenamąją vietą, kraujo grupė, eritrocitų antigenai Rh ir Kell bei asmens mirties metai. Paskutiniuose dviejuose stulpeliai nurodoma, kada įrašas buvo sukurtas ir atnaujintas duomenų bazėje. Asmenys, kurių asmens kodas nenurodytas, yra užsienio šalių gyventojai."[^manifest]

- **Model:** `datasets/gov/hi/kraujo_donacijos/KraujoDonoras`[^manifest]
- **Dataset:** [Kraujo donacijos](../kraujo_donacijos.md) (`datasets/gov/hi/kraujo_donacijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/hi/kraujo_donacijos.csv#L15](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/kraujo_donacijos.csv#L15)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/kraujo_donacijos/KraujoDonoras` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `donoro_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `donoro_id` | `string` | — | `4` | `open` | — | Kraujo donoro identifikacinis numeris | — |
| `asmens_id` | `string` | — | `4` | `open` | — | Asmens identifikacininis numeris | — |
| `ak_validacija` | `string` | — | `4` | `open` | — | Asmens kodo validacija | Valstybės duomenų agentūros sugeneruotas stulpelis validuojantis asmens kodą |
| `gim_metai` | `date` | `Y` | `4` | `open` | — | Gimimo metai | "Asmens gimimo metai. Kuomet asmens kodas yra validus metai yra išraukiami iš asmens kodo, kitu atveju paliekami sistemoje įvesti gimimo metai" |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | "Asmens lytis. Kuomet asmens kodas yra validus lytis yra ištraukiama iš asmens kodo, kitu atveju paliekama sistemoje įvesta lytis" |
| `pirm_gyv_vlst` | `string` | — | `4` | `open` | — | Pirma gyvenamoji valstybė | "Valstybė, kurioje asmuo oficialiai įregistravo savo gyvenamąją vietą pirmąjį kartą" |
| `pirm_gyv_sav` | `string` | — | `4` | `open` | — | Pirma gyvenamoji savivaldybė | "Savivaldybė, kurioje asmuo oficialiai įregistravo savo gyvenamąją vietą pirmąjį kartą" |
| `kraujo_grupe` | `string` | — | `4` | `open` | — | Asmens kraujo grupė | — |
| `rezus_faktorius` | `string` | — | `4` | `open` | — | Rezus faktorius | "Požymis, nurodantis ar rezus (Rh) antigenas aptinkamas ant raudonųjų kraujo kūnelių (eritrocitų) paviršiaus" |
| `kell_antigen` | `string` | — | `4` | `open` | — | Kell antigenas | "Požymis, nurodantis ar kell antigenas yra aptinkamas ant raudonųjų kraujo kūnelių (eritrocitų) paviršiaus" |
| `mirties_data` | `date` | `Y` | `4` | `open` | — | Asmens mirties data | — |
| `irasas_sukurtas` | `datetime` | `S` | `4` | `open` | — | Įrašo sukūrimo data ir laikas duomenų bazėje | — |
| `irasas_atnaujintas` | `datetime` | `S` | `4` | `open` | — | Įrašo atnaujinimo data ir laikas duomenų bazėje | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"M"` | — | — | Moteris | — |
| `lytis` | `"V"` | — | — | Vyras | — |
| `rezus_faktorius` | `"Rh D teigiamas"` | — | — | Rh D teigiamas | — |
| `rezus_faktorius` | `"Rh D neigiamas"` | — | — | Rh D neigiamas | — |
| `rezus_faktorius` | `"Nėra duomenų"` | — | — | Nėra duomenų | — |
| `kell_antigen` | `"Kell-"` | — | — | Kell- | — |
| `kell_antigen` | `"Kell+"` | — | — | Kell+ | — |
| `kell_antigen` | `"Nėra duomenų"` | — | — | Nėra duomenų | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/kraujo_donacijos.csv#L15 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/kraujo_donacijos.csv#L15)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/kraujo_donacijos (https://data.gov.lt/datasets/3889/)
