---
type: Table
title: "BendrasNtMokestis — NT mokesčio mokėtojo ir NT bendri duomenys"
description: "Nekilnojamojo turto (toliau - NT) mokesčio mokėtojo ir NT bendri duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vmi/nt/BendrasNtMokestis"
tags: [gov, vmi, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmi/nt.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/nt.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# BendrasNtMokestis — NT mokesčio mokėtojo ir NT bendri duomenys

Nekilnojamojo turto (toliau - NT) mokesčio mokėtojo ir NT bendri duomenys

- **Model:** `datasets/gov/vmi/nt/BendrasNtMokestis`[^manifest]
- **Dataset:** [Nekilnojamo turto mokesčio duomenų rinkinys](../nt.md) (`datasets/gov/vmi/nt`)
- **Manifest CSV:** [datasets/gov/vmi/nt.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/nt.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/nt/BendrasNtMokestis`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Eilutės numeris | — |
| `moketojo_tipas` | `integer` | — | `4` | `open` | — | Požymis, ar fizinio asmens, ar juridinio asmens deklaracija | — |
| `metai` | `integer` | — | `2` | `open` | — | Deklaracijoje nurodyto mokestinio laikotarpio arba jo pradžios metai | NTM deklaracijoje nurodyto mokestinio laikotarpio arba jo pradžios metai |
| `apskaiciuota_suma` | `number` | — | `2` | `open` | — | Apskaičiuota mokesčio suma (KIT711S priedo visų lapų S15 laukelių suma) | Apskaičiuota mokesčio suma (bendra mokesčio suma už visose savivaldybėse turimą NT dar neįvertinus gautų lengvatų), t. y. NTM deklaracijos KIT711S priedo visų lapų S15 laukelių suma |
| `lengvata` | `number` | — | `2` | `open` | — | Savivaldybės (-ių) suteikta mokesčio lengvata (priedo KIT711S lapų S16 laukelių suma) | Bendra savivaldybės (-ių) suteikta mokesčio lengvata (visose savivaldybėse gautų lengvatų suma), t. y. NTM deklaracijos KIT711S priedo visų lapų S16 laukelių suma |
| `bendra_suma` | `number` | — | `2` | `open` | — | Bendra mokesčio per mokestinį laikotarpį suma (grąžintina suma su minuso (-) ženklu) (12) | Bendra mokesčio per mokestinį laikotarpį suma, t. y. bendra mokesčio suma, kurią turi sumokėti mokėtojas už visose savivaldybėse deklaruotą turimą NT |
| `neapmok_turto_verte` | `number` | — | `2` | `open` | — | Mokestinio laikotarpio paskutinę dieną turimo nuosavo ir/ar perimto iš fizinių asmenų turto, neapmokestinamo pagal NTMĮ 7 str. 2 d. nuostatas, vertė (pildo tik juridiniai asmenys) | — |
| `veiklos_pabaiga` | `date` | `D` | `4` | `open` | — | Veiklos pabaigos data | Veiklos pabaigos data (nurodytą mokestinį laikotarpį baigia veiklą ir teikia paskutinio mokestinio laikotarpio deklaraciją, pildo tik juridiniai asmenys) |
| `proceduros_pradzia` | `date` | `D` | `4` | `open` | — | Procedūros pradžios data | Procedūros pradžios data (nurodytą mokestinį laikotarpį pradeda bankroto ar restruktūrizavimo procedūras, pildo tik juridiniai asmenys) |
| `avansinio_mokescio_metai` | `integer` | — | `2` | `open` | — | Avansinio mokesčio metai | — |
| `avansinio_mok_suma_1k_agr` | `number` | — | `2` | `open` | — | Avansinio mokesčio suma už 1 ketvirtį | Bendra avansinio mokesčio suma už 1 ketvirtį (bendra NT avansinio mokesčio suma, kurią turi sumokėti mokėtojas už visose savivaldybėse deklaruotą avansinį mokestį sausio–kovo mėn.) |
| `avansinio_mok_suma_2k_agr` | `number` | — | `2` | `open` | — | Avansinio mokesčio suma už 2 ketvirtį | Bendra avansinio mokesčio suma už 2 ketvirtį (bendra NT avansinio mokesčio suma, kurią turi sumokėti mokėtojas už visose savivaldybėse deklaruotą avansinį mokestį balandžio–birželio mėn.) |
| `avansinio_mok_suma_3k_agr` | `number` | — | `2` | `open` | — | Avansinio mokesčio suma už 3 ketvirtį | Bendra avansinio mokesčio suma už 3 ketvirtį (bendra NT avansinio mokesčio suma, kurią turi sumokėti mokėtojas už visose savivaldybėse deklaruotą avansinį mokestį liepos–rugsėjo mėn.) |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `moketojo_tipas` | `1` | — | — | Fizinis asmuo | — |
| `moketojo_tipas` | `2` | — | — | Juridinis asmuo | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(ref: "id")` | `ref` | `4` | `open` | — | — | — |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `apskaiciuota_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `lengvata` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `bendra_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `neapmok_turto_verte` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `avansinio_mokescio_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `avansinio_mok_suma_1k_agr` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `avansinio_mok_suma_2k_agr` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `avansinio_mok_suma_3k_agr` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/nt.csv
