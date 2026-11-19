---
type: Table
title: "Operacija — Pacientų gydymo operacijomis duomenys"
description: "Vilniaus universiteto ligoninės Žalgirio klinikos ŽKIS sistema kaupia pacientų odontologinių sutrikimų gydymo operacijomis duomenis."
resource: "https://get.data.gov.lt/datasets/gov/vulzk/zkis/Operacija"
tags: [gov, vulzk, operacija, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vulzk/zkis.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vulzk/zkis.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2660/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vulzk/zkis"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Operacija — Pacientų gydymo operacijomis duomenys

Vilniaus universiteto ligoninės Žalgirio klinikos ŽKIS sistema kaupia pacientų odontologinių sutrikimų gydymo operacijomis duomenis. Duomenų laikotarpis yra nuo 2015 m. iki 2024 m. Duomenų rinkinys apima vykdytos operacijos protokolo identifikatorių, šifruotą paciento asmens kodą, gimimo metus, ligos TLK-10-AM kodą bei žodinį pavadinimą, operacijos pradžios, pabaigos laikus, taikytos anestezės rūšies, rizikos kodus bei jos pradžios ir pabaigos laikus. Papildomai, saugomi paciento draudiko pavadinimas, JAR kodas ir draudimo rūšis, numatyta būti imama iš Sveidros.[^manifest]

- **Model:** `datasets/gov/vulzk/zkis/Operacija`[^manifest]
- **Dataset:** [Pacientų gydymo operacijomis duomenys](../zkis.md) (`datasets/gov/vulzk/zkis`)[^manifest]
- **Manifest CSV:** [datasets/gov/vulzk/zkis.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vulzk/zkis.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vulzk/zkis/Operacija` (`deployed`)[^manifest]
- **Provider:** `vulzk` — VšĮ Vilniaus universiteto ligoninės Žalgirio klinika *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `operacijos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `operacijos_id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `paciento_asmens_kodas` | `string` | — | `4` | `open` | — | Šifruotas paciento asmens kodas | — |
| `paciento_lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `paciento_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `diagnozes_kodas_tlk_10_am` | `string` | — | `4` | `open` | — | Paciento diagnozės TLK-10-AM kodas | — |
| `diagnozes_pavadinimas_lt` | `string` | — | `4` | `open` | — | Paciento diagnozės pavadinimas | — |
| `paguldymo_ligonineje_data` | `datetime` | `T` | `4` | `open` | — | Paciento paguldymo ligoninėje data | — |
| `operacijos_pradzios_laikas` | `datetime` | `T` | `4` | `open` | — | Pacientui vykdytos operacijos pradžios data ir laikas minutės tikslumu | — |
| `operacijos_pabaigos_laikas` | `datetime` | `T` | `4` | `open` | — | Pacientui vykdytos operacijos pabaigos data ir laikas minutės tikslumu | — |
| `anestezes_rusies_kodas` | `string` | — | `4` | `open` | — | Pacientui vykdytos anestezės rūšies kodas | — |
| `anestezes_rizikos_kodas` | `string` | — | `4` | `open` | — | Pacientui vykdytos anestezės rizikos kodas | — |
| `anestezes_pradzios_laikas` | `datetime` | `T` | `4` | `open` | — | Pacientui vykdytos anestezės pradžios data ir laikas minutės tikslumu | — |
| `anestezes_pabaigos_laikas` | `datetime` | `T` | `4` | `open` | — | Pacientui vykdytos anestezės pabaigos data ir laikas minutės tikslumu | — |
| `paciento_draudiko_pav` | `string` | — | `4` | `open` | — | Pacientą apdraudžiusios įstaigos pavadinimas | — |
| `paciento_draudiko_jar_kodas` | `string` | — | `4` | `open` | — | Pacientą apdraudžiusios įstaigos juridinio asmens kodas | — |
| `draudimo_rusis` | `string` | — | `4` | `open` | — | Paciento draudimo rūšis | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paciento_lytis` | `"Vyras"` | `V` | — | Vyras | — |
| `paciento_lytis` | `"Moteris"` | `M` | — | Moteris | — |
| `anestezes_rusies_kodas` | `"Bendra nejautra"` | `ANEST_NEJAUTRA` | — | Bendra nejautra | — |
| `anestezes_rusies_kodas` | `"Sedacija"` | `ANEST_SEDAC` | — | Sedacija | — |
| `anestezes_rusies_kodas` | `"Regioninė nejautra"` | `ANEST_REGNEJAUTR` | — | Regioninė nejautra | — |
| `anestezes_rizikos_kodas` | `"Sveikas pacientas"` | `ASA1` | — | Sveikas pacientas | — |
| `anestezes_rizikos_kodas` | `"Lengva sistemine liga sergantis pacientas"` | `ASA2` | — | Lengva sistemine liga sergantis pacientas | — |
| `anestezes_rizikos_kodas` | `"Sunkia, ribojančia aktyvumą, sistemine liga sergantis pacientas"` | `ASA3` | — | Sunkia, ribojančia aktyvumą, sistemine liga sergantis pacientas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `diagnozes_pavadinimas_lt` | `update(property: "diagnozes_pavadinimas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vulzk/zkis.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vulzk/zkis.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vulzk/zkis (https://data.gov.lt/datasets/2660/)
