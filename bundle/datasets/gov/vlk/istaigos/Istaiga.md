---
type: Table
title: "Istaiga — Gydymo įstaigų, vaistinių ir kitų įmonių sąrašas"
description: "Informacija apie gydymo įstaigas, vaistines ir kitas įmones."
resource: "https://get.data.gov.lt/datasets/gov/vlk/istaigos/Istaiga"
tags: [gov, vlk, istaiga, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/vlk_istg.csv#L9"
    title: "atviriduomenys/manifest — datasets/gov/vlk/vlk_istg.csv#L9"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1386/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/istaigos"
    author: "team:vda"
    last_modified: "2026-06-10T00:00:00Z"
---

# Istaiga — Gydymo įstaigų, vaistinių ir kitų įmonių sąrašas

Informacija apie gydymo įstaigas, vaistines ir kitas įmones.[^manifest]

- **Model:** `datasets/gov/vlk/istaigos/Istaiga`[^manifest]
- **Dataset:** [Gydymo įstaigų, vaistinių ir kitų įmonių sąrašas](../istaigos.md) (`datasets/gov/vlk/istaigos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/vlk_istg.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/vlk_istg.csv#L9)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/istaigos/Istaiga` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-06-10`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `integer` | — | `4` | `open` | — | Įstaigos (ASPĮ, vaistinės ir kt.) ID | Įstaigos (ASPĮ, vaistinės ir kt.) unikalus identifikavimo kodas (ID), pagal kurį įstaiga identifikuojama informacinėje sistemoje Sveidra. Šis ID suteikiamas kiekvienai įstaigos veiklos vietai (filialui) skirtingas |
| `jar` | `integer` | — | `2` | `open` | — | Įstaigos JAR | Įstaigos (ASPĮ, vaistinės ir kt.) Juridinių asmenų registre nurodytas juridinio asmens kodas |
| `pavadinimas` | `string` | — | `2` | `open` | — | Įstaigos pavadinimas | Įstaigos (ASPĮ, vaistinės ir kt.) pavadinimas |
| `pagrindines_kodas` | `integer` | — | `2` | `open` | — | Įstaigos (pagrindinės) ID | Pagrindinės įstaigos (ASPĮ, vaistinės ir kt.) unikalus identifikavimo kodas (ID). Šis ID suteikiamas įstaigos veiklos vietai, kurioje registruota įstaigos buveinė |
| `pagrindines_pavadinimas` | `string` | — | `2` | `open` | — | Įstaigos (pagrindinės) pavadinimas | Pagrindinės įstaigos (ASPĮ, vaistinės ir kt.) pavadinimas |
| `optika` | `string` | `enum: bool` | `4` | `open` | — | Požymis ar įstaiga yra optika | — |
| `nenurodyta` | `string` | `enum: bool` | `4` | `open` | — | Požymis ar įstaigos tipas yra nenurodytas | — |
| `gydymo` | `string` | `enum: bool` | `4` | `open` | — | Požymis ar įstaiga yra gydymo įstaiga | — |
| `farmacijos` | `string` | `enum: bool` | `4` | `open` | — | Požymis ar įstaiga yra vaistinė | — |
| `ortopedijos_gamybos` | `string` | `enum: bool` | `4` | `open` | — | Požymis ar įstaiga yra ortopedijos gamybos įstaiga | — |
| `odontologines_prieziuros` | `string` | `enum: bool` | `4` | `open` | — | Požymis ar įstaiga yra odontologinės priežiūros įstaiga | — |
| `skyrius` | `string` | `enum: bool` | `4` | `open` | — | Požymis ar įstaiga yra licencijuojamos įstaigos skyrius | — |
| `sav_kodas` | `string` | — | `2` | `open` | — | Nuoroda į savivaldybių klasifikatorių | — |
| `tlk` | `string` | — | `4` | `open` | — | Teritorinė ligonių kasa (TLK) | TLK pavadinimas |
| `sutarties_pradzia` | `date` | `D` | `4` | `open` | — | Sutarties galiojimo pradžios data | Įstaigos (ASPĮ, vaistinės ir kt.) sutarties galiojimo pradžios data |
| `sutarties_pabaiga` | `date` | `D` | `4` | `open` | — | Sutarties galiojimo pabaigos data | Įstaigos (ASPĮ, vaistinės ir kt.) sutarties galiojimo pabaigos data |
| `nuo` | `date` | `D` | `4` | `open` | — | Galiojimo pradžios data | Įstaigos (ASPĮ, vaistinės ir kt.) galiojimo pradžios data |
| `iki` | `date` | `D` | `4` | `open` | — | Galiojimo pabaigos data | Įstaigos (ASPĮ, vaistinės ir kt.) galiojimo pabaigos data |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `optika` | `"Ne"` | — | — | Ne | — |
| `optika` | `"Taip"` | — | — | Taip | — |
| `nenurodyta` | `"Ne"` | — | — | Ne | — |
| `nenurodyta` | `"Taip"` | — | — | Taip | — |
| `gydymo` | `"Ne"` | — | — | Ne | — |
| `gydymo` | `"Taip"` | — | — | Taip | — |
| `farmacijos` | `"Ne"` | — | — | Ne | — |
| `farmacijos` | `"Taip"` | — | — | Taip | — |
| `ortopedijos_gamybos` | `"Ne"` | — | — | Ne | — |
| `ortopedijos_gamybos` | `"Taip"` | — | — | Taip | — |
| `odontologines_prieziuros` | `"Ne"` | — | — | Ne | — |
| `odontologines_prieziuros` | `"Taip"` | — | — | Taip | — |
| `skyrius` | `"Ne"` | — | — | Ne | — |
| `skyrius` | `"Taip"` | — | — | Taip | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `jar` | `update(type: "ref", ref: "JuridinisAsmuo")` | `type` | `4` | — | — | — | — |
| `jar` | `update(property: "jar.ja_kodas", type: "")` | `property` | `4` | — | — | — | — |
| `pavadinimas` | `update(property: "jar.ja_pavadinimas", type: "")` | `property` | `4` | — | — | — | — |
| `pagrindines_kodas` | `create(property: "pagrindine", type: "ref", ref: "Pagrindine")` | `type` | `4` | — | — | — | — |
| `pagrindines_kodas` | `update(property: "pagrindine.kodas", type: "")` | `property` | `4` | — | — | — | — |
| `pagrindines_pavadinimas` | `update(property: "pagrindine.pavadinimas", type: "")` | `property` | `4` | — | — | — | — |
| `sav_kodas` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `sav_kodas` | `update(property: "savivaldybe.sav_kodas", type: "")` | `property` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/vlk_istg.csv#L9 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/vlk_istg.csv#L9)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/istaigos (https://data.gov.lt/datasets/1386/)
