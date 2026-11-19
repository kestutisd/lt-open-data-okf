---
type: Table
title: "JurAsmDujuSuvartojimas — Juridinių asmenų dujų suvartojimo duomenys"
description: "Lentelėje pateikti Energijos skirstymo operatoriaus (ESO) juridinių asmenų dujų suvartojimo duomenys."
resource: "https://get.data.gov.lt/datasets/gov/eso/jur_asm_duju_suvartojimas/JurAsmDujuSuvartojimas"
tags: [gov, eso, jurasmdujusuvartojimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eso/jur_asm_duju_suvartojimas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/eso/jur_asm_duju_suvartojimas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2621/"
    title: "data.gov.lt DCAT-AP — datasets/gov/eso/jur_asm_duju_suvartojimas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# JurAsmDujuSuvartojimas — Juridinių asmenų dujų suvartojimo duomenys

Lentelėje pateikti Energijos skirstymo operatoriaus (ESO) juridinių asmenų dujų suvartojimo duomenys. Adresai pateikiami 10 kilometrų dydžio stačiakampėmis gardelėmis Lietuvos koordinačių sistemoje (LKS-94). Gardelės, kuriose yra 5 arba mažiau vartotojų nerodomos. Duomenų laiko aprėptis - nuo 2019 m. sausio 1d.[^manifest]

- **Model:** `datasets/gov/eso/jur_asm_duju_suvartojimas/JurAsmDujuSuvartojimas`[^manifest]
- **Dataset:** [Juridinių asmenų dujų suvartojimas](../jur_asm_duju_suvartojimas.md) (`datasets/gov/eso/jur_asm_duju_suvartojimas`)[^manifest]
- **Manifest CSV:** [datasets/gov/eso/jur_asm_duju_suvartojimas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eso/jur_asm_duju_suvartojimas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/eso/jur_asm_duju_suvartojimas/JurAsmDujuSuvartojimas` (`deployed`)[^manifest]
- **Provider:** `eso` — Energijos skirstymo operatorius *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `vartotojo_kodas` | `string` | — | `4` | `open` | — | Dujų vartotojo kodas | — |
| `imones_kodas` | `string` | — | `4` | `open` | — | Įmonės kodas | — |
| `evrk_2_red` | `string` | — | `4` | `open` | — | Ekonominės veiklos rūšies klasifikatorius 2 red. | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybė | — |
| `vrt_adreso_gardele` | `ref` | [Grid10KmSq](../../lsd/grid/Grid10KmSq.md) (`level=4 UUID`: `vrt_adreso_gardele._id`) | `4` | `open` | — | Vartotojo adreso 10km gardelė | — |
| `rgob_adreso_gardele` | `ref` | [Grid10KmSq](../../lsd/grid/Grid10KmSq.md) (`level=4 UUID`: `rgob_adreso_gardele._id`) | `4` | `open` | — | Registruoto objekto 10km gardelė | — |
| `rgob_numeris` | `string` | — | `4` | `open` | — | Registruoto objekto numeris | — |
| `apskaita_nuo` | `date` | `M` | `4` | `open` | — | Apskaitos laikotarpio pradžia | — |
| `apskaita_iki` | `date` | `M` | `4` | `open` | — | Apskaitos laikotarpio pabaiga | — |
| `suvartojimas` | `number` | `m^3` | `4` | `open` | — | Suvartotas dujų kiekis, m3 | — |
| `automatizuota_apskaita` | `string` | — | `4` | `open` | — | Automatizuota apskaita | — |
| `duomenis_pateike` | `string` | — | `4` | `open` | — | Nurodoma kas deklaravo dujų rodmenis už apskaitos laikotarpį | — |
| `vartotojo_statusas` | `string` | — | `4` | `open` | — | Vartotojo statusas | — |
| `objekto_statusas` | `string` | — | `4` | `open` | — | Objekto statusas | — |
| `pajungimo_data` | `date` | `D` | `4` | `open` | — | Dujų pajungimo data | — |
| `pajungimo_tipas` | `string` | — | `4` | `open` | — | Dujų pajungimo tipas | — |
| `atjungimo_data` | `date` | `D` | `4` | `open` | — | Dujų atjungimo data | — |
| `atjungimo_tipas` | `string` | — | `4` | `open` | — | Dujų atjungimo tipas | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/eso/jur_asm_duju_suvartojimas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eso/jur_asm_duju_suvartojimas.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/eso/jur_asm_duju_suvartojimas (https://data.gov.lt/datasets/2621/)
