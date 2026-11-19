---
type: Table
title: "KlaipedosRajonoStovykluApklausa — Klaipėdos rajono stovyklų apklausos rezultatai"
description: "Klaipėdos rajono savivaldybės tėvų atsakymai į apklausą apie vaiko stovyklą"
resource: "https://get.data.gov.lt/datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai/KlaipedosRajonoStovykluApklausa"
tags: [gov, klaipedos_r_sav, klaipedosrajonostovykluapklausa, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv#L72"
    title: "atviriduomenys/manifest — datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv#L72"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2739/"
    title: "data.gov.lt DCAT-AP — datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# KlaipedosRajonoStovykluApklausa — Klaipėdos rajono stovyklų apklausos rezultatai

Klaipėdos rajono savivaldybės tėvų atsakymai į apklausą apie vaiko stovyklą[^manifest]

- **Model:** `datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai/KlaipedosRajonoStovykluApklausa`[^manifest]
- **Dataset:** [Priėmimai į Klaipėdos rajono ikimokyklinio ir mokyklinio ugdymo įstaigas](../ugdymo_istaigu_priemimai.md) (`datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv#L72](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv#L72)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai/KlaipedosRajonoStovykluApklausa` (`deployed`)[^manifest]
- **Provider:** `klaipedos_r_sav` — Klaipėdos rajono savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `atsakymo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `atsakymo_id` | `string` | — | `4` | `open` | — | Unikalus atsakymo identifikatorius | — |
| `tiksline_grupe` | `string` | — | `4` | `open` | — | Tikslinė apklausos grupė | — |
| `kategorijos_id` | `string` | — | `4` | `open` | — | Stovyklos kategorijos identifikatorius | — |
| `stovyklos_kategorija` | `string` | — | `4` | `open` | — | Stovyklos kategorija | — |
| `tipo_id` | `string` | — | `4` | `open` | — | Klausimo tipo identifikatorius | — |
| `tipas` | `string` | — | `4` | `open` | — | Klausimo tipas | — |
| `klausimo_id` | `string` | — | `4` | `open` | — | Klausimo identifikatorius | — |
| `klausimas` | `string` | — | `4` | `open` | — | Klausimas | — |
| `tekst_atsakymas` | `string` | — | `4` | `open` | — | Cenzūruotas tekstinis atsakymas į klausimą | — |
| `tekst_ats_simboliu_sk` | `integer` | — | `4` | `open` | — | Tekstinio atsakymo simbolių skaičius | — |
| `tekst_ats_zodziu_sk` | `integer` | — | `4` | `open` | — | Tekstinio atsakymo žodžių skaičius | — |
| `tekst_ats_sak_sk` | `integer` | — | `4` | `open` | — | Tekstinio atsakymo sakinių skaičius | — |
| `pasirenkamas_atsakymas` | `string` | — | `4` | `open` | — | Pasirenkamas atsakymas į klausimą | — |
| `naudotojo_id` | `string` | — | `4` | `open` | — | Naudotojo identifikatorius | — |
| `pateikimo_laikas` | `datetime` | `S` | `4` | `open` | — | Atsakymų pateikimo laikas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv#L72 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv#L72)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai (https://data.gov.lt/datasets/2739/)
