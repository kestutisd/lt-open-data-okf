---
type: Table
title: "VaizdoGarsoIrasas — Tautosakos vaizdo ir garso įrašų duomenys"
description: "Duomenų rinkinyje pateikiama informacija apie 1905–2007 m. Lietuvos tautosakos archyvinius garso įrašus ir fotografijas."
resource: "https://get.data.gov.lt/datasets/gov/llti/tautosakos_vaizdo_garso_irasai/VaizdoGarsoIrasas"
tags: [gov, llti, vaizdogarsoirasas, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/tautosakos_vaizdo_garso_irasu_duomenys.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/llti/tautosakos_vaizdo_garso_irasu_duomenys.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2790/"
    title: "data.gov.lt DCAT-AP — datasets/gov/llti/tautosakos_vaizdo_garso_irasai"
    author: "team:vda"
    last_modified: "2026-10-14T00:00:00Z"
---

# VaizdoGarsoIrasas — Tautosakos vaizdo ir garso įrašų duomenys

Duomenų rinkinyje pateikiama informacija apie 1905–2007 m. Lietuvos tautosakos archyvinius garso įrašus ir fotografijas. Rinkinyje pateikiamos ir nuorodos į įrašus, pateiktus Lietuvos literatūros ir tautosakos instituto svetainėje. Viena duomenų rinkinio eilutė nurodo įrašą ir informaciją apie pateikėją. Kai įrašo pateikėjų yra daugiau nei vienas, informacija apie įrašą pateikiama per kelias eilutes. Adresuose pateikiamos šios santrumpos: r. – rajonas, k. – kaimas, mstl. – miestelis, mst. – miestas, apyl. – apylinkė, apskr. – apskritis, gub. – gubernija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/llti/tautosakos_vaizdo_garso_irasai/VaizdoGarsoIrasas`[^manifest]
- **Dataset:** [Tautosakos vaizdo ir garso įrašų duomenys](../tautosakos_vaizdo_garso_irasai.md) (`datasets/gov/llti/tautosakos_vaizdo_garso_irasai`)[^manifest]
- **Manifest CSV:** [datasets/gov/llti/tautosakos_vaizdo_garso_irasu_duomenys.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/tautosakos_vaizdo_garso_irasu_duomenys.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/llti/tautosakos_vaizdo_garso_irasai/VaizdoGarsoIrasas` (`deployed`)[^manifest]
- **Provider:** `llti` — Lietuvių literatūros ir tautosakos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-10-14`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `iraso_id` | `string` | — | `4` | `open` | — | Įrašo identifikatorius | — |
| `laikmenos_nr` | `string` | — | `4` | `open` | — | Laikmenos numeris | — |
| `vnt_nr` | `string` | — | `4` | `open` | — | Vieneto numeris | — |
| `fondas` | `string` | — | `4` | `open` | — | Fondas | — |
| `ekspedicija` | `string` | — | `4` | `open` | — | Ekspedicija | — |
| `zanro_pavadinimas` | `string` | — | `4` | `open` | — | Žanras | — |
| `atlikimo_budas` | `string` | — | `4` | `open` | — | Atlikimo būdas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Įrašo pavadinimas | — |
| `laikmenos_tipas_orig` | `string` | — | `4` | `open` | — | Originalios laikmenos tipas | — |
| `orig_sifras` | `string` | — | `4` | `open` | — | Originalios laikmenos šifras | — |
| `vda_trukme_sek` | `integer` | `s` | `4` | `open` | — | Trukmė (sekundės) | — |
| `melodiju_rinkinio_nr` | `string` | — | `4` | `open` | — | Melodijų rinkinio numeris | — |
| `melodijos_eiles_nr` | `string` | — | `4` | `open` | — | Melodijos eilės numeris | — |
| `fotografijos_nr` | `string` | — | `4` | `open` | — | Fotografijos numeris | — |
| `fotografijos_sifras` | `string` | — | `4` | `open` | — | Fotografijos šifras | — |
| `uzrasymo_data` | `string` | — | `4` | `open` | — | Užrašymo data | — |
| `uzrasymo_vieta` | `string` | — | `4` | `open` | — | Užrašymo vieta | — |
| `tekstu_rinkinio_nr` | `string` | — | `4` | `open` | — | Tekstų rinkinio numeris | — |
| `teksto_eiles_nr` | `string` | — | `4` | `open` | — | Teksto eilės numeris | — |
| `pateikejas` | `string` | — | `4` | `open` | — | Pateikėjas | — |
| `pat_gimimo_data` | `string` | — | `4` | `open` | — | Pateikėjo gimimo data | — |
| `pat_gyv_vieta` | `string` | — | `4` | `open` | — | Pateikėjo gyvenamoji vieta | — |
| `pat_gyv_vieta_pastab` | `string` | — | `4` | `open` | — | Pastabos apie pateikėjo gyvenamąją vietą | — |
| `pat_kilmes_vieta` | `string` | — | `4` | `open` | — | Pateikėjo kilmės vieta | — |
| `pat_klm_vieta_pastab` | `string` | — | `4` | `open` | — | Pastabos apie pateikėjo kilmės vietą | — |
| `iraso_kokybe` | `string` | — | `4` | `open` | — | Įrašo kokybė | — |
| `laikmenos_bukle` | `string` | — | `4` | `open` | — | Laikmenos būklė | — |
| `perrasymo_greitis_aps_min` | `string` | — | `4` | `open` | — | Perrašymo greitis (apsukomis per minutę) | — |
| `pastabos` | `string` | — | `4` | `open` | — | Pastabos | — |
| `kopija_archyvuose` | `string` | — | `4` | `open` | — | Kopija archyvuose | — |
| `skelbta` | `string` | — | `4` | `open` | — | Kur įrašas buvo skelbtas | — |
| `paskelbta` | `string` | — | `4` | `open` | — | Kur įrašas buvo paskelbtas | — |
| `uzrasytojai` | `string` | — | `4` | `open` | — | Užrašytojai | — |
| `nuoroda_i_irasa` | `url` | — | `4` | `open` | — | Nuoroda į įrašą internete | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `fondas` | `"LTR"` | — | — | Lietuvių tautosakos archyvo rankraštinių rinkinių fondas | — |
| `fondas` | `"LMD II"` | — | — | Lietuvos mokslo draugijos II fondas | — |
| `fondas` | `"LMD III"` | — | — | Lietuvos mokslo draugijos III fondas | — |
| `fondas` | `"VPUTR"` | — | — | Vilniaus Pedagoginio universiteto tautosakos rankraštyno rinkinių fondas | — |
| `ekspedicija` | `"Lietuvių kalbos ir literatūros instituto tautosakinė ekspedicija"` | — | — | Lietuvių kalbos ir literatūros instituto tautosakinė ekspedicija | — |
| `ekspedicija` | `"Lietuvių kalbos ir literatūros instituto dialektologinė-tautosakinė ekspedicija"` | — | — | Lietuvių kalbos ir literatūros instituto dialektologinė-tautosakinė ekspedicija | — |
| `ekspedicija` | `"Paminklų apsaugos ir kraštotyros draugijos Vilniaus skyriaus kompleksinė ekspedicija"` | — | — | Paminklų apsaugos ir kraštotyros draugijos Vilniaus skyriaus kompleksinė ekspedicija | — |
| `ekspedicija` | `"Vilniaus valstybinio universiteto kraštotyros klubo kompleksinė"` | — | — | Vilniaus valstybinio universiteto kraštotyros klubo kompleksinė ekspedicija | — |
| `ekspedicija` | `"Mokslų Akademijos ir Lietuvių kalbos ir literatūros instituto kompleksinė ekspedicija"` | — | — | — | — |
| `ekspedicija` | `"Vilniaus valstybinio universiteto tautosakinė ekspedicija"` | — | — | Vilniaus valstybinio universiteto tautosakinė ekspedicija | — |
| `ekspedicija` | `"Lietuvių literatūros ir tautosakos instituto tautosakinė ekspedicija"` | — | — | Lietuvių literatūros ir tautosakos instituto tautosakinė ekspedicija | — |
| `ekspedicija` | `"Kraštotyros draugijos Kėdainių skyriaus kompleksinė ekspedicija"` | — | — | Kraštotyros draugijos Kėdainių skyriaus kompleksinė ekspedicija | — |
| `ekspedicija` | `"Kraštotyros draugijos Ukmergės skyriaus kompleksinė ekspedicija"` | — | — | Kraštotyros draugijos Ukmergės skyriaus kompleksinė ekspedicija | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/llti/tautosakos_vaizdo_garso_irasu_duomenys.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/tautosakos_vaizdo_garso_irasu_duomenys.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/llti/tautosakos_vaizdo_garso_irasai (https://data.gov.lt/datasets/2790/)
