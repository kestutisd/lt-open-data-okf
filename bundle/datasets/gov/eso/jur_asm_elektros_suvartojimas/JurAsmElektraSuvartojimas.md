---
type: Table
title: "JurAsmElektraSuvartojimas — Juridinių asmenų elektros energijos suvartojimo duomenys"
description: "Lentelėje pateikti Energijos skirstymo operatoriaus (ESO) juridinių asmenų elektros suvartojimo duomenys."
resource: "https://get.data.gov.lt/datasets/gov/eso/jur_asm_elektros_suvartojimas/JurAsmElektraSuvartojimas"
tags: [gov, eso, jurasmelektrasuvartojimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eso/jur_asm_elektros_suvartojimas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/eso/jur_asm_elektros_suvartojimas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2742/"
    title: "data.gov.lt DCAT-AP — datasets/gov/eso/jur_asm_elektros_suvartojimas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# JurAsmElektraSuvartojimas — Juridinių asmenų elektros energijos suvartojimo duomenys

Lentelėje pateikti Energijos skirstymo operatoriaus (ESO) juridinių asmenų elektros suvartojimo duomenys. Adresai pateikiami 10 kilometrų dydžio stačiakampėmis gardelėmis Lietuvos koordinačių sistemoje (LKS-94). Elektros suvartojimo duomenys pateikiami mėnesio tikslumu. Realus suvartotas elektros kiekis gali skirtis nuo pateikiamų duomenų, tokiu atveju, kai vartotojas neteisingai deklaruoja suvartotą elektros kiekį arba turi įsirengęs saulės elektrinę. Duomenų laiko aprėptis - nuo 2019 m. sausio 1d.[^manifest]

- **Model:** `datasets/gov/eso/jur_asm_elektros_suvartojimas/JurAsmElektraSuvartojimas`[^manifest]
- **Dataset:** [Juridinių asmenų elektros energijos suvartojimo duomenys](../jur_asm_elektros_suvartojimas.md) (`datasets/gov/eso/jur_asm_elektros_suvartojimas`)[^manifest]
- **Manifest CSV:** [datasets/gov/eso/jur_asm_elektros_suvartojimas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eso/jur_asm_elektros_suvartojimas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/eso/jur_asm_elektros_suvartojimas/JurAsmElektraSuvartojimas` (`deployed`)[^manifest]
- **Provider:** `eso` — Energijos skirstymo operatorius *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `kliento_id` | `string` | — | `4` | `open` | — | Kliento identifikatorius | — |
| `objekto_id` | `string` | — | `4` | `open` | — | Objekto identifikatorius | — |
| `objekto_savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė, kurioje yra objektas | — |
| `obj_adreso_gardele` | `ref` | [Grid10KmSq](../../lsd/grid/Grid10KmSq.md) (`level=4 UUID`: `obj_adreso_gardele._id`) | `4` | `open` | — | Objekto adreso stačiakampė 10km gardelė | — |
| `imones_kodas` | `string` | — | `4` | `open` | — | Įmonės kodas | — |
| `evrk_2_red` | `string` | — | `4` | `open` | — | Ekonominės veiklos rūšies klasifikatorius 2 red. | — |
| `obj_galioja_nuo` | `date` | `D` | `4` | `open` | — | Objektas galioja nuo | — |
| `obj_galioja_iki` | `date` | `D` | `4` | `open` | — | Objektas galioja iki | — |
| `apskaitos_men` | `date` | `M` | `4` | `open` | — | Apskaitos mėnesis | — |
| `atgauta_kwh` | `number` | — | `4` | `open` | — | Atgautas kilovatvalandžių skaičius | — |
| `suvartota_kwh` | `number` | — | `4` | `open` | — | Suvartotas kilovatvalandžių skaičius | — |
| `bendras_suvartojimas_kwh` | `number` | — | `4` | `open` | — | Bendras suvartojimas kilovatvalandėmis | — |
| `duomenis_pateike` | `string` | — | `4` | `open` | — | Duomenų pateikėjas (inžinierius/klientas) | — |
| `im_adreso_gardele` | `ref` | [Grid10KmSq](../../lsd/grid/Grid10KmSq.md) (`level=4 UUID`: `im_adreso_gardele._id`) | `4` | `open` | — | Įmonės registruoto adreso stačiakampė 10km gardelė | — |
| `nutoles_gv` | `boolean` | — | `4` | `open` | — | Nutolęs gaminantis vartotojas | — |
| `automatizuota_apskaita` | `string` | — | `4` | `open` | — | Automatizuota apskaita | — |
| `el_pasto_adresas` | `string` | — | `4` | `open` | — | Elektroninio pašto adresas | — |
| `telefono_nr` | `string` | — | `4` | `open` | — | Telefono numeris | — |
| `obj_itampos_lygis` | `string` | — | `4` | `open` | — | Objekto įtampos lygis | — |
| `obj_itampa_kv` | `number` | `kV` | `4` | `open` | — | Objekto įtampa, kilovoltais | — |
| `leistina_galia_kw` | `number` | `kW` | `4` | `open` | — | Leistina galia, kilovatvalandėmis | — |
| `leistina_gen_galia_kw` | `number` | `kW` | `4` | `open` | — | Leistina generuoti galia | — |
| `instal_gen_galia_kw` | `number` | `kW` | `4` | `open` | — | Instaliuota generuoti galia | — |
| `objekto_gamintojo_tipas` | `string` | — | `4` | `open` | — | Objekto gamintojo tipas | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/eso/jur_asm_elektros_suvartojimas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eso/jur_asm_elektros_suvartojimas.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/eso/jur_asm_elektros_suvartojimas (https://data.gov.lt/datasets/2742/)
