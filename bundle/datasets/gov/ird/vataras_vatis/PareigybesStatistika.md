---
type: Table
title: "PareigybesStatistika — Nestatutinių valstybės tarnautojų pareigybių statistika"
description: "Aktuali nestatutinių valstybės tarnautojų pareigybių statistika pagal Valstybės ir savivaldybių institucijas bei įstaigas."
resource: "https://get.data.gov.lt/datasets/gov/ird/vataras_vatis/PareigybesStatistika"
tags: [gov, ird, pareigybesstatistika, deployed, level-3, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/vataras_vatis.csv#L25"
    title: "atviriduomenys/manifest — datasets/gov/ird/vataras_vatis.csv#L25"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1240/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ird/vataras_vatis"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# PareigybesStatistika — Nestatutinių valstybės tarnautojų pareigybių statistika

Aktuali nestatutinių valstybės tarnautojų pareigybių statistika pagal Valstybės ir savivaldybių institucijas bei įstaigas. Pareigybių statistika skaičiuojama kaip įsteigtų pareigybių suma (sumuojant etatus, nes pareigybė gali sudaryti ir ne pilną etatą). Pareigybės - tai įstaigos turimos ar suplanuotos, bet nebūtinai užpildytos įvairių tipų darbo pozicijos; įsteigtų pareigybių skaičius gali skirtis nuo užimtų pareigybių skaičiaus ar šiuo metu aktyviai dirbančių asmenų skaičiaus. Nestatutiniai valstybės tarnautojai - tai, pvz., įstaigų vadovai, patarėjai, padėjėjai, specialistai; dažniausiai tai nėra visi įstaigoje dirbantys darbuotojai. Duomenų šaltinis - VATIS ir VATARAS. Rodomos tik šiuo metu egzistuojančios įstaigos, turinčios bent vieną tokio tipo pareigybę. Dėl techninių klausimų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/ird/vataras_vatis/PareigybesStatistika`[^manifest]
- **Dataset:** [Valstybės tarnautojų registras, Valstybės tarnybos valdymo informacinė sistema](../vataras_vatis.md) (`datasets/gov/ird/vataras_vatis`)[^manifest]
- **Manifest CSV:** [datasets/gov/ird/vataras_vatis.csv#L25](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/vataras_vatis.csv#L25)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/vataras_vatis/PareigybesStatistika` (`deployed`)[^manifest]
- **Provider:** `ird` — Informatikos ir ryšių departamentas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `jar_kodas`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `jar_kodas` | `string` | — | `2` | `open` | — | Institucijos ar įstaigos Juridinių asmenų registro (JAR) kodas | — |
| `pk_1` | `number` | `U` | `2` | `open` | — | Įsteigtų etatų suma pareigybių kategorijoje 1: "Politinio (asmeninio) pasitikėjimo" | — |
| `pk_2` | `number` | `U` | `2` | `open` | — | Įsteigtų etatų suma pareigybių kategorijoje 2: "Karjeros valstybės tarnautojas" | — |
| `pk_3` | `number` | `U` | `2` | `open` | — | Įsteigtų etatų suma pareigybių kategorijoje 3: "Įstaigos vadovas" | — |
| `pk_1_2_3` | `number` | `U` | `2` | `open` | — | Įsteigtų etatų suma pareigybių kategorijose 1-3 | — |
| `atnaujinimas` | `date` | `D` | `4` | `open` | — | Naujausio įrašo arba modifikacijos data gaunamuose duomenyse | Paruošiamas imant naujausio įrašo originaliuose duomenyse datą |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/vataras_vatis.csv#L25 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/vataras_vatis.csv#L25)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ird/vataras_vatis (https://data.gov.lt/datasets/1240/)
