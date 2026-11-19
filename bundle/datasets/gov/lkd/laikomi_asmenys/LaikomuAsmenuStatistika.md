---
type: Table
title: "LaikomuAsmenuStatistika — Kalinimo įstaigose laikomų asmenų statistika"
description: "Lietuvos kalėjimų departamentas (LKD) kaupia kalinimo įstaigose laikomų asmenų statistinius duomenis nuo 2021 m., atnaujinamus kas menėsį, gaunamus iš kalinimo įstaigų."
resource: "https://get.data.gov.lt/datasets/gov/lkd/laikomi_asmenys/LaikomuAsmenuStatistika"
tags: [gov, lkd, laikomuasmenustatistika, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lkd/laikomi_asmenys.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lkd/laikomi_asmenys.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2665/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lkd/laikomi_asmenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# LaikomuAsmenuStatistika — Kalinimo įstaigose laikomų asmenų statistika

Lietuvos kalėjimų departamentas (LKD) kaupia kalinimo įstaigose laikomų asmenų statistinius duomenis nuo 2021 m., atnaujinamus kas menėsį, gaunamus iš kalinimo įstaigų. Rinkinys apima momentinį laikotarpį, kuriam aktualūs pateikti skaičiai, kalinimo įstaigos pavadinimą, bendrą laisvės atėmimo vietose laikomų asmenų skaičių, suimtųjų skaičių, bendrą nuteisimų laisvės atėmimu skaičių, nuteistųjų atviro tipo bausme be Pusiaukelės namų skaičių, nuteistųjų pusiau atviro tipo bausmės atlikimo vietoje skaičių, nuteistųjų uždaro tipo bausmės atlikimo vietoje skaičių, nuteistųjų Pusiaukelės namuose skaičių, suėmimo vykdymo vietoje laikomų nuteistųjų skaičių, nuteistųjų arešto bausme skaičių, moterų skaičių, nepilnamečių skaičių, bendrą užsienio šalių piliečių skaičių, suimtų užsienio šalių piliečių skaičių ir nuteistų užsienio šalių piliečių skaičių.[^manifest]

- **Model:** `datasets/gov/lkd/laikomi_asmenys/LaikomuAsmenuStatistika`[^manifest]
- **Dataset:** [Kalinimo įstaigose laikomų asmenų statistika](../laikomi_asmenys.md) (`datasets/gov/lkd/laikomi_asmenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/lkd/laikomi_asmenys.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lkd/laikomi_asmenys.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lkd/laikomi_asmenys/LaikomuAsmenuStatistika` (`deployed`)[^manifest]
- **Provider:** `lkd` — Lietuvos kalėjimų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros unikalus identifikatorius | — |
| `laikotarpis` | `date` | `M` | `4` | `open` | — | Laikotarpis mėnesio tikslumu, kada aktualūs įrašo duomenys | — |
| `ist_pav` | `string` | — | `4` | `open` | — | Kalinimo įstaigos pavadinimas | — |
| `asm_sk` | `integer` | `U` | `4` | `open` | — | Įstaigoje kalinamų asmenų skaičius | — |
| `suimtieji_sk` | `integer` | `U` | `4` | `open` | — | Suimtųjų skaičius | — |
| `nut_laisves_atemimu_sk` | `integer` | `U` | `4` | `open` | — | Nuteistųjų laisvės atėmimu skaičius | — |
| `nut_atv_bausm_be_pn_sk` | `integer` | `U` | `4` | `open` | — | Nuteistųjų atviro tipo bausme bausmės atlikimo vietoje be pusiaukelės namų skaičius | — |
| `nut_pus_atv_bausm_sk` | `integer` | `U` | `4` | `open` | — | Nuteistųjų pusiau atviro tipo bausme bausmės atlikimo vietoje skaičius | — |
| `nut_uzd_bausm_sk` | `integer` | `U` | `4` | `open` | — | Nuteistųjų uždaro tipo bausmės atlikimo vietoje | — |
| `nut_pn_sk` | `integer` | `U` | `4` | `open` | — | Nuteistųjų pusiaukelės namuose | — |
| `suem_vt_kt_asm_sk` | `integer` | `U` | `4` | `open` | — | Suėmimo vietoje laikomų nuteistųjų asmenų skaičius | — |
| `nut_arestu_sk` | `integer` | `U` | `4` | `open` | — | Arešto bausme nuteistųjų skaičius | — |
| `moteru_sk` | `integer` | `U` | `4` | `open` | — | Kalinamų moterų skaičius | — |
| `nepilnameciu_sk` | `integer` | `U` | `4` | `open` | — | Kalinamų nepilnamečių skaičius | — |
| `uzs_pil_sk` | `integer` | `U` | `4` | `open` | — | Kalinamų užsienio šalių piliečių skaičius | — |
| `suim_uzs_pil_sk` | `integer` | `U` | `4` | `open` | — | Suimtų užsienio šalių piliečių skaičius | — |
| `nut_uzs_pil_sk` | `integer` | `U` | `4` | `open` | — | Nuteistų užsienio šalių piliečių skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lkd/laikomi_asmenys.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lkd/laikomi_asmenys.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lkd/laikomi_asmenys (https://data.gov.lt/datasets/2665/)
