---
type: Table
title: "Deklaracija — Kontroliuojamų medžiagų deklaracijų duomenys"
description: "Narkotikų, tabako ir alkoholio kontrolės departamento (NTAKD) naudojama Pirmtakų teisėtos apyvartos kontrolės informacinė sistema (PTAKIS) kaupia juridinių bei fizinių asmenų narkotinių pirmtakų (prekursorių) deklaracijas."
resource: "https://get.data.gov.lt/datasets/gov/ntakd/ptakis/Deklaracija"
tags: [gov, ntakd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ntakd/prekursoriai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/prekursoriai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Deklaracija — Kontroliuojamų medžiagų deklaracijų duomenys

Narkotikų, tabako ir alkoholio kontrolės departamento (NTAKD) naudojama Pirmtakų teisėtos apyvartos kontrolės informacinė sistema (PTAKIS) kaupia juridinių bei fizinių asmenų narkotinių pirmtakų (prekursorių) deklaracijas. Duomenys kaupiami nuo 2021-04-01 ir atnaujinami iki šiol. Duomenų rinkinys sudarytas iš pseudonimizuoto deklaravusio fizinio arba juridinio asmens (deklaranto) kodo, deklaranto asmens rūšies, ataskaitos formos, deklaruotos medžiagos pavadinimo, paskirties ir kiekių deklaracijos periodo pradžioje ir pabaigoje, deklaracijos periodo metų ir deklaracijos numerio tais metais. Vienas įrašas atitinka vieną deklaranto, medžiagos, deklaracijos metų ir periodo numerio kombinaciją.

- **Model:** `datasets/gov/ntakd/ptakis/Deklaracija`[^manifest]
- **Dataset:** [Kontroliuojamų medžiagų deklaracijų duomenys](../ptakis.md) (`datasets/gov/ntakd/ptakis`)
- **Manifest CSV:** [datasets/gov/ntakd/prekursoriai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/prekursoriai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ntakd/ptakis/Deklaracija`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `deklaranto_kodas` | `string` | — | `4` | `open` | — | Deklaraciją pateikusio asmens pseudonimizuotas kodas | — |
| `deklaranto_asmens_rusis` | `string` | — | `4` | `open` | — | Deklaraciją pateikusio asmens rūšis | — |
| `medziaga` | `string` | — | `4` | `open` | — | Deklaruota medžiaga | — |
| `ataskaitos_forma` | `string` | — | `4` | `open` | — | Deklaracijos ataskaitos forma | — |
| `paskirtis` | `string` | — | `4` | `open` | — | Deklaruotos medžiagos paskirtis | — |
| `kiekis_periodo_pradzioje` | `number` | — | `4` | `open` | — | Medžiagos kiekis deklaracijos periodo pradžioje | — |
| `kiekis_periodo_pabaigoje` | `number` | — | `4` | `open` | — | Medžiagos kiekis deklaracijos periodo pabaigoje | — |
| `mato_vienetas` | `string` | — | `4` | `open` | — | Deklaruotos medžiagos matavimo vienetas | — |
| `dekl_periodo_metai` | `integer` | — | `4` | `open` | — | Deklaracijos periodo metai | — |
| `dekl_periodo_nr` | `integer` | — | `4` | `open` | — | Deklaracijos numeris esamais metais | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `deklaranto_asmens_rusis` | `"Juridinis"` | — | — | LR juridinis asmuo | — |
| `deklaranto_asmens_rusis` | `"Fizinis"` | — | — | LR fizinis asmuo | — |
| `deklaranto_asmens_rusis` | `"Nežinoma"` | — | — | Nei LR juridinis, nei LR fizinis asmuo | — |
| `mato_vienetas` | `"kg"` | — | — | Kilogramai | — |
| `mato_vienetas` | `"l"` | — | — | Litrai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ntakd/prekursoriai.csv
