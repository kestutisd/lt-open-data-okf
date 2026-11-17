---
type: Table
title: "FinRodiklis — Savivaldybių valdomų įmonių finansiniai rodikliai"
description: "Lentelėje pateikti savivaldybių valdomų įmonių 2018 -2023 metų finansinių rodiklių duomenys iš VšĮ Valdymo koordinavimo centro (VKC)."
resource: "https://get.data.gov.lt/datasets/gov/vkc/svi_finansiniai_rodikliai/FinRodiklis"
tags: [gov, vkc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vkc/svi_finansiniai_rodikliai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkc/svi_finansiniai_rodikliai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# FinRodiklis — Savivaldybių valdomų įmonių finansiniai rodikliai

Lentelėje pateikti savivaldybių valdomų įmonių 2018 -2023 metų finansinių rodiklių duomenys iš VšĮ Valdymo koordinavimo centro (VKC).

- **Model:** `datasets/gov/vkc/svi_finansiniai_rodikliai/FinRodiklis`[^manifest]
- **Dataset:** [Savivaldybių valdomų įmonių finansiniai rodikliai](../svi_finansiniai_rodikliai.md) (`datasets/gov/vkc/svi_finansiniai_rodikliai`)
- **Manifest CSV:** [datasets/gov/vkc/svi_finansiniai_rodikliai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkc/svi_finansiniai_rodikliai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vkc/svi_finansiniai_rodikliai/FinRodiklis`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `nr` | `string` | — | `4` | `open` | — | Institucijos eilės numeris | — |
| `imones_pavadinimas` | `string` | — | `4` | `open` | — | Įmonės pavadinimas | — |
| `imones_kodas` | `string` | — | `4` | `open` | — | Įmonės kodas | — |
| `data` | `date` | `D` | `4` | `open` | — | Data | — |
| `sektorius` | `string` | — | `4` | `open` | — | Sektorius | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė | — |
| `teisine_forma` | `string` | — | `4` | `open` | — | Teisinė forma | — |
| `imones_isteigimo_data` | `date` | `D` | `4` | `open` | — | Įmonės įsteigimo data | — |
| `veiklos_sektorius` | `string` | — | `4` | `open` | — | Sektorius, kuriame veikia įmonė | — |
| `imones_direktorius` | `string` | — | `4` | `open` | — | Įmonės direktorius (generalinis direktorius) | — |
| `sav_dalis_proc` | `number` | `%` | `4` | `open` | — | Savivaldybėms priklausanti dalis procentais (%) | — |
| `ksav_dalis_proc` | `number` | `%` | `4` | `open` | — | Kontroliuojančiai savivaldybei priklausanti dalis procentais (%) | — |
| `patronuojancioji_imone` | `string` | — | `4` | `open` | — | Patronuojančioji įmonė | — |
| `ar_turi_imoniu` | `boolean` | — | `4` | `open` | — | Požymis, ar bendrovė turi kontroliuojamų įmonių ("true" - taip, turi; "false" - ne, neturi) | — |
| `kontroliuojamos_imones` | `string` | — | `4` | `open` | — | Kontroliuojamos įmonės | — |
| `roa_proc` | `number` | `%` | `4` | `open` | — | ROA (paskutinių 12 mėnesių) procentais (%) | — |
| `roe_proc` | `number` | `%` | `4` | `open` | — | ROE (paskutinių 12 mėnesių) procentais (%) | — |
| `d_e_proc` | `number` | `%` | `4` | `open` | — | D/E procentais (%) | — |
| `ebitda` | `number` | — | `4` | `open` | — | EBITDA | — |
| `bpelno_marza_proc` | `number` | `%` | `4` | `open` | — | Bendrojo pelno marža procentais (%) | — |
| `vpelno_marza_proc` | `number` | `%` | `4` | `open` | — | Veiklos pelno marža procentais (%) | — |
| `ebitda_marza_proc` | `number` | `%` | `4` | `open` | — | EBITDA marža procentais (%) | — |
| `ebt_marza_proc` | `number` | `%` | `4` | `open` | — | EBT marža procentais (%) | — |
| `gpelno_marza_proc` | `number` | `%` | `4` | `open` | — | Grynojo pelno marža procentais (%) | — |
| `ebit` | `number` | — | `4` | `open` | — | EBIT: pelnas (nuostoliai) prieš apmokestinimą + finansinės ir investicinės veiklos sąnaudos – finansinės ir investicinės veiklos pajamos | — |
| `bendrasis_likvidumas` | `number` | — | `4` | `open` | — | Bendrasis likvidumo koeficientas: trumpalaikis turtas / trumpalaikiai įsipareigojimai | — |
| `finrod1_proc` | `number` | `%` | `4` | `open` | — | Nuosavas kapitalas/ Visas turtas, procentais (%) | — |
| `finrod2` | `number` | — | `4` | `open` | — | Grynoji finansinė skola/ EBITDA | — |
| `pinigu_rodiklis_proc` | `number` | `%` | `4` | `open` | — | Pinigų rodiklis (procentais, %): pinigų vidurkis/ turto vidurkis. Imami vidurkiai, nes balansas – 1 dienos atvaizdavimas, būtų iškreiptas vaizdas | — |
| `pirkeju_skolu_apyvartumas` | `number` | `d` | `4` | `open` | — | Pirkėjų skolų apyvartumas: pardavimų pajamos/ debitorių vidurkis, dienomis | — |
| `tiekeju_skolu_apyvartumas` | `number` | `d` | `4` | `open` | — | Tiekėjų skolų apyvartumas: savikaina/ tiekėjų skolų vidurkis, dienomis | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `sektorius` | `"Kita"` | — | — | Kita | — |
| `sektorius` | `"Vandentvarka"` | — | — | Vandentvarka | — |
| `sektorius` | `"Šilumos tinklai"` | — | — | Šilumos tinklai | — |
| `sektorius` | `"Viešasis transportas"` | — | — | Viešasis transportas | — |
| `sektorius` | `"RATC"` | — | — | RATC | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `imones_kodas` | `update(type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |
| `ebitda` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `ebit` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vkc/svi_finansiniai_rodikliai.csv
