---
type: Table
title: "FizAsmDujuSuvartojimas — Fizinių asmenų dujų suvartojimo duomenys"
description: "Lentelėje pateikti Energijos skirstymo operatoriaus (ESO) fizinių asmenų dujų suvartojimo duomenys."
resource: "https://get.data.gov.lt/datasets/gov/eso/fiz_asm_duju_suvartojimas/FizAsmDujuSuvartojimas"
tags: [gov, eso, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/eso/fiz_asm_duju_suvartojimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eso/fiz_asm_duju_suvartojimas.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# FizAsmDujuSuvartojimas — Fizinių asmenų dujų suvartojimo duomenys

Lentelėje pateikti Energijos skirstymo operatoriaus (ESO) fizinių asmenų dujų suvartojimo duomenys. Adresai pateikiami 1 kilometro dydžio stačiakampėmis gardelėmis Lietuvos koordinačių sistemoje (LKS-94). Gardelės, kuriose yra 5 arba mažiau vartotojų nerodomos. Duomenų laiko aprėptis - nuo 2019 m. sausio 1d.

- **Model:** `datasets/gov/eso/fiz_asm_duju_suvartojimas/FizAsmDujuSuvartojimas`[^manifest]
- **Dataset:** [Fizinių asmenų dujų suvartojimas](../fiz_asm_duju_suvartojimas.md) (`datasets/gov/eso/fiz_asm_duju_suvartojimas`)
- **Manifest CSV:** [datasets/gov/eso/fiz_asm_duju_suvartojimas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eso/fiz_asm_duju_suvartojimas.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/eso/fiz_asm_duju_suvartojimas/FizAsmDujuSuvartojimas`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `vartotojo_kodas` | `string` | — | `4` | `open` | — | Vartotojo kodas | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Gimimo metai | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybė | — |
| `grid_id` | `ref` | [/datasets/gov/lsd/grid/Grid1KmSq](../../lsd/grid/Grid1KmSq.md) | `4` | `open` | — | Objekto stačiakampė 1km gardelė | — |
| `obj_nr` | `string` | — | `4` | `open` | — | Objekto numeris | — |
| `objekto_tipas` | `string` | — | `4` | `open` | — | Objekto tipas | — |
| `sildymo_tipas` | `string` | — | `4` | `open` | — | Šildymo tipas | — |
| `naudingas_plotas` | `number` | `m^2` | `4` | `open` | — | Naudingas plotas, m2 | — |
| `registruotu_asm_skaicius` | `string` | — | `4` | `open` | — | Registruotų asmenų skaičius | — |
| `energetine_klase` | `string` | — | `4` | `open` | — | Energetinė klasė | — |
| `apskaita_nuo` | `date` | `M` | `4` | `open` | — | Apskaitos laikotarpio pradžia | — |
| `apskaita_iki` | `date` | `M` | `4` | `open` | — | Apskaitos laikotarpio pabaiga | — |
| `suvartojimas` | `number` | `m^3` | `4` | `open` | — | Suvartotas dujų kiekis, m3 | — |
| `prijungimo_data` | `date` | `D` | `4` | `open` | — | Dujų prijungimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/eso/fiz_asm_duju_suvartojimas.csv
