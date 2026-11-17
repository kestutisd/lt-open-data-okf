---
type: Table
title: "AudiosensorinisIrasas — Bibliografiniai įrašai"
description: "Elektroninių leidinių valdymo informacinės sistemos (ELVIS) bibliografinių įrašų sąrašas."
resource: "https://get.data.gov.lt/datasets/gov/lab/bibliografiniai_irasai/AudiosensorinisIrasas"
tags: [gov, lab, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lab/bibliografiniai_irasai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab/bibliografiniai_irasai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# AudiosensorinisIrasas — Bibliografiniai įrašai

Elektroninių leidinių valdymo informacinės sistemos (ELVIS) bibliografinių įrašų sąrašas.

- **Model:** `datasets/gov/lab/bibliografiniai_irasai/AudiosensorinisIrasas`[^manifest]
- **Dataset:** [Bibliografiniai įrašai](../bibliografiniai_irasai.md) (`datasets/gov/lab/bibliografiniai_irasai`)
- **Manifest CSV:** [datasets/gov/lab/bibliografiniai_irasai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab/bibliografiniai_irasai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lab/bibliografiniai_irasai/AudiosensorinisIrasas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus ID | — |
| `leidinio_id` | `string` | — | `4` | `open` | — | Leidinio ID | — |
| `isbn_issn_ismn_numeris` | `string` | — | `4` | `open` | — | ISBN, ISSN arba ISMN identifikacinis numeris | — |
| `leidejas` | `string` | — | `4` | `open` | — | Leidinio leidėjas | — |
| `leidejo_salis` | `string` | — | `4` | `open` | — | Leidinio išleidimo šalis | — |
| `isleidimo_metai` | `integer` | — | `4` | `open` | — | Leidinio išleidimo metai | — |
| `leidinio_tipas` | `string` | — | `4` | `open` | — | Leidinio tipas | — |
| `kalba` | `string` | — | `4` | `open` | — | Leidinio kalba | — |
| `grupe` | `string` | — | `4` | `open` | — | Kopijos naudotojo grupė | — |
| `zanras` | `string` | — | `4` | `open` | — | Leidinio žanras | — |
| `autoriaus_id` | `string` | — | `4` | `open` | — | Leidinio autoriaus ID | — |
| `autorius` | `string` | — | `4` | `open` | — | Leidinio autorius | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Leidinio pavadinimas | — |
| `paantraste` | `string` | — | `4` | `open` | — | Papildoma leidinio antraštė | — |
| `aprasymas` | `string` | — | `4` | `open` | — | Leidinio aprašymas | — |
| `rengejas` | `string` | — | `4` | `open` | — | Prieinamos kopijos rengėjas | — |
| `rengejo_salis` | `string` | — | `4` | `open` | — | Prieinamos kopijos išleidimo šalis | — |
| `kopijos_metai` | `integer` | — | `4` | `open` | — | Prieinamos kopijos išleidimo metai | — |
| `diktoriaus_id` | `string` | — | `4` | `open` | — | Diktoriaus ID | — |
| `diktorius` | `string` | — | `4` | `open` | — | Diktorius | — |
| `ikelimo_data` | `date` | `D` | `4` | `open` | — | Kopijos įkėlimo į biblioteką data | — |
| `formatas` | `string` | — | `4` | `open` | — | Kopijos formatas | — |
| `trukme` | `string` | — | `4` | `open` | — | Kopijos trukmė | — |
| `psl_sk` | `integer` | — | `4` | `open` | — | Kopijos puslapių skaičius | — |
| `atviras` | `boolean` | — | `4` | `open` | — | Kopijos prieinamumo būsena. „TRUE“ – leidinys prienamas visiems | — |
| `matomas` | `boolean` | — | `4` | `open` | — | Kopijos matomumo būsena. „TRUE“ – pasiekiamas leidinys | — |
| `licencijos_pradzia` | `date` | `D` | `4` | `open` | — | licencijos pradžia | — |
| `licencijos_pabaiga` | `date` | `D` | `4` | `open` | — | Licencijos pabaiga | — |
| `licenciju_kiekis` | `integer` | — | `4` | `open` | — | Licencijų skaičius | — |
| `leidinio_vertinimas` | `number` | — | `4` | `open` | — | Leidinio vidutinis vertinimas | — |
| `vertinimu_skaicius` | `integer` | — | `4` | `open` | — | Leidinį įvertinusių naudotojų skaičius | — |
| `megstamiausiu_kiekis` | `integer` | — | `4` | `open` | — | Naudotojų, pažymėjusių leidinį kaip mėgstamiausią, skaičius | — |
| `apskaiciuoto_vertinimo_data` | `date` | `D` | `4` | `open` | — | Data, kurią apskaičiuotas vidutinis leidinio vertinimas, įvertinusių naudotojų skaičius ir į mėgstamiausių leidinių sąrašą įtraukusių naudotojų skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lab/bibliografiniai_irasai.csv
