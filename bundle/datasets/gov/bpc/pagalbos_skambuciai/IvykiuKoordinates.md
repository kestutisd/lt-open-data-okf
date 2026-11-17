---
type: Table
title: "IvykiuKoordinates — BPC įvykių koordinatės"
description: "Bendrojo pagalbos centro (BPC) registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, pilnas sąrašas."
resource: "https://get.data.gov.lt/datasets/gov/bpc/pagalbos_skambuciai/IvykiuKoordinates"
tags: [gov, bpc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/bpc/pagalbos_skambuciai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_skambuciai.csv#L11"
    last_modified: "2026-11-11T14:39:20Z"
---

# IvykiuKoordinates — BPC įvykių koordinatės

Bendrojo pagalbos centro (BPC) registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, pilnas sąrašas. Tai yra neagreguota lentelė, kurioje viena eilutė yra vienas įvykis. To paties ar skirtingų asmenų pranešimai apie tą patį įvykį yra sujungti į vieną įvykį. Lentelė skirta dažniams, dinamikai ir geografiniam pasiskirstymui stebėti. Dėl konfidencialumo nepateikiama tiksli įvykio data, o skelbiamos koordinatės yra "triukšmintos" (paslenkant tikrąsias kooridates atsitiktine kryptimi 0–5000 metrų, priklausomai nuo gyventojų tankio; mažesnis tankis – didesnis tikėtinasis poslinkis). BPC koordinates nustato pagal pranešėjo pateiktą įvykio adresą ir Registrų centro adresų duomenis; jeigu konkretus adresas nepateikiamas arba jo nėra, nurodomos gyvenvietės centro koordinatės; koordinatės taip pat gali būti patikslinamos pagal pagalbos prašančiojo asmens vietos nustatymo duomenis, jeigu nepavyksta nustatyti adreso ar gyvenvietės. Praneštų įvykių skaičiai nebūtinai turi sutapti su Administracinių nusižengimų registro duomenimis (pranešimai gali būti melagingi arba nepasiekti administracinių nusižengimų bylos stadijos).

- **Model:** `datasets/gov/bpc/pagalbos_skambuciai/IvykiuKoordinates`[^manifest]
- **Dataset:** [Bendrojo pagalbos centro 112 skambučių duomenų rinkinys](../pagalbos_skambuciai.md) (`datasets/gov/bpc/pagalbos_skambuciai`)
- **Manifest CSV:** [datasets/gov/bpc/pagalbos_skambuciai.csv#L11](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_skambuciai.csv#L11)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/bpc/pagalbos_skambuciai/IvykiuKoordinates`
- **Primary Key (`ref`):** `ivykio_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ivykio_id` | `string` | — | `4` | `open` | — | Unikalus šifruotas įvykio ID | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai, kuriais įvyko įvykis | — |
| `menuo` | `integer` | — | `2` | `open` | — | Mėnuo, kuomet įvyko įvykis | — |
| `ivykio_tipo_kodas` | `ref` | [IvykiuKlasifikatorius](IvykiuKlasifikatorius.md) | `4` | `open` | — | Įvykio tipo kodas | — |
| `koordinate` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Triukšminta LKS-94 įvykio koordinatė | Triukšminta X koordinatė (rytai–vakarai) ir triukšminta Y koordinatė (šiaurė–pietūs) LKS-94 koordinačių sistemoje. |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `menuo` | `1` | — | — | Sausis | — |
| `menuo` | `2` | — | — | Vasaris | — |
| `menuo` | `3` | — | — | Kovas | — |
| `menuo` | `4` | — | — | Balandis | — |
| `menuo` | `5` | — | — | Gegužė | — |
| `menuo` | `6` | — | — | Birželis | — |
| `menuo` | `7` | — | — | Liepa | — |
| `menuo` | `8` | — | — | Rugpjūtis | — |
| `menuo` | `9` | — | — | Rugsėjis | — |
| `menuo` | `10` | — | — | Spalis | — |
| `menuo` | `11` | — | — | Lapkritis | — |
| `menuo` | `12` | — | — | Gruodis | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/bpc/pagalbos_skambuciai.csv
