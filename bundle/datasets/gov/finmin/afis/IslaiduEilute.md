---
type: Table
title: "IslaiduEilute — Valstybės išlaidų duomenys"
description: "Lietuvos Respublikos finansų ministerijos Atvirų finansų informacinėje sistemoje (AFIS) nuo 2015 m. kaupiami, kas 3 mėnesius atnaujinami ir atvėrimui numatyti automatiškai apdorojami viešųjų finansų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/finmin/afis/IslaiduEilute"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/afis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/afis.csv#L19"
    last_modified: "2026-11-11T14:39:20Z"
---

# IslaiduEilute — Valstybės išlaidų duomenys

Lietuvos Respublikos finansų ministerijos Atvirų finansų informacinėje sistemoje (AFIS) nuo 2015 m. kaupiami, kas 3 mėnesius atnaujinami ir atvėrimui numatyti automatiškai apdorojami viešųjų finansų duomenys. Duomenų rinkinį sudaro: juridinio asmens (subjekto), kurio veikla yra finansuojama, JAR kodas ir pavadinimas, ekonominis kodas ir išlaidų straipsnis iki 6-ojo lygio, valstybės funkcijų kodas ir grupė iki 4-ojo lygio, finansuojamų programų bei priemonių pavadinimai, finansavimo šaltinis ir grupė, pradinis išlaidų planas, patikslintas išlaidų planas ir tikrasis išlaidų kiekis pagal ataskaitinio ketvirčio paskutinės dienos informaciją.

- **Model:** `datasets/gov/finmin/afis/IslaiduEilute`[^manifest]
- **Dataset:** [Valstybės pajamų ir išlaidų duomenys](../afis.md) (`datasets/gov/finmin/afis`)
- **Manifest CSV:** [datasets/gov/finmin/afis.csv#L19](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/afis.csv#L19)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/afis/IslaiduEilute`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `ataskaitinis_periodas` | `date` | `D` | `4` | `open` | — | Paskutinė metų ketvirčio diena | — |
| `subjekto_jar_kodas` | `string` | — | `4` | `open` | — | Juridinio asmens kodas | — |
| `subjekto_pavadinimas` | `string` | — | `4` | `open` | — | Juridinio asmens pavadinimas | — |
| `ek_kodo_lygis_2` | `string` | — | `4` | `open` | — | 2-o lygio išlaidų grupės kodas | — |
| `islaidu_grupes_lygis_2` | `string` | — | `4` | `open` | — | 2-o lygio išlaidų grupės pavadinimas | — |
| `ek_kodo_lygis_3` | `string` | — | `4` | `open` | — | 3-io lygio išlaidų grupės kodas | — |
| `islaidu_grupes_lygis_3` | `string` | — | `4` | `open` | — | 3-io lygio išlaidų grupės pavadinimas | — |
| `ek_kodo_lygis_4` | `string` | — | `4` | `open` | — | 4-o lygio išlaidų grupės kodas | — |
| `islaidu_straipsnio_lygis_4` | `string` | — | `4` | `open` | — | 4-o lygio išlaidų straipsnis | — |
| `ek_kodo_lygis_6` | `string` | — | `4` | `open` | — | 6-o lygio ekonominis kodas | — |
| `islaidu_straipsnio_lygis_6` | `string` | — | `4` | `open` | — | 6-o lygio išlaidų straipsnis | — |
| `vlst_funkc_kodo_lygis_1` | `string` | — | `4` | `open` | — | 1-o lygio valstybės funkcijų kodas | — |
| `vlst_funkc_grupes_lygis_1` | `string` | — | `4` | `open` | — | 1-o lygio valstybės funkcijų grupės pavadinimas | — |
| `vlst_funkc_kodo_lygis_2` | `string` | — | `4` | `open` | — | 2-o lygio valstybės funkcijų kodas | — |
| `vlst_funkc_grupes_lygis_2` | `string` | — | `4` | `open` | — | 2-o lygio valstybės funkcijų grupės pavadinimas | — |
| `vlst_funkc_kodo_lygis_4` | `string` | — | `4` | `open` | — | 4-o lygio valstybės funkcijų kodas | — |
| `vlst_funkc_grupes_lygis_4` | `string` | — | `4` | `open` | — | 4-o lygio valstybės funkcijų grupės pavadinimas | — |
| `programa` | `string` | — | `4` | `open` | — | Finansuojamos programos pavadinimas | — |
| `priemone` | `string` | — | `4` | `open` | — | Finansuojamos priemonės pavadinimas | — |
| `finansavimo_saltiniu_grupe` | `string` | — | `4` | `open` | — | Finansavimo šaltinių grupė | — |
| `finansavimo_saltinis` | `string` | — | `4` | `open` | — | Finansavimo šaltinis | — |
| `pradinis_planas` | `number` | — | `4` | `open` | — | Pradinis išlaidų planas | — |
| `patikslintas_planas` | `number` | — | `4` | `open` | — | Patikslintas išlaidų planas | — |
| `vykdymas` | `number` | — | `4` | `open` | — | Išlaidų kiekis vykdant planą | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/afis.csv
