---
type: Table
title: "AudiosensorinisIrasas — Bibliografiniai įrašai"
description: "Elektroninių leidinių valdymo informacinės sistemos (ELVIS) bibliografinių įrašų sąrašas."
resource: "https://get.data.gov.lt/datasets/gov/lab/bibliografiniai_irasai/AudiosensorinisIrasas"
tags: [gov, lab, audiosensorinisirasas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab/bibliografiniai_irasai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lab/bibliografiniai_irasai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3841/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lab/bibliografiniai_irasai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# AudiosensorinisIrasas — Bibliografiniai įrašai

Elektroninių leidinių valdymo informacinės sistemos (ELVIS) bibliografinių įrašų sąrašas.[^manifest]

- **Model:** `datasets/gov/lab/bibliografiniai_irasai/AudiosensorinisIrasas`[^manifest]
- **Dataset:** [Bibliografiniai įrašai](../bibliografiniai_irasai.md) (`datasets/gov/lab/bibliografiniai_irasai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lab/bibliografiniai_irasai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab/bibliografiniai_irasai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lab/bibliografiniai_irasai/AudiosensorinisIrasas` (`deployed`)[^manifest]
- **Provider:** `lab` — Lietuvos audiosensorinė biblioteka *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

# Related References

- [ISO 639 Language Codes Reference](../../../../references/iso-639-kalbu-kodai.md) — ISO 639-1 / 639-2 / EU NAL codes and special markers `zxx`, `und`, `mul`, `mis`.

[^manifest]: atviriduomenys/manifest — datasets/gov/lab/bibliografiniai_irasai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab/bibliografiniai_irasai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lab/bibliografiniai_irasai (https://data.gov.lt/datasets/3841/)
