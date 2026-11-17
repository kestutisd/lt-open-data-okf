---
type: Table
title: "Ataskaita — Alkoholio ir tabako ataskaitų duomenys"
description: "Narkotikų, tabako ir alkoholio kontrolės departamento (NTAKD) naudojamoje alkoholio produktų ir tabako gaminių ataskaitų teikimo sistemoje kaupiamos juridinių bei fizinių asmenų pateiktos alkoholio ir tabako gaminių ataskaitos."
resource: "https://get.data.gov.lt/datasets/gov/ntakd/ataskaitos/Ataskaita"
tags: [gov, ntakd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ntakd/alkoholis_tabakas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/alkoholis_tabakas.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Ataskaita — Alkoholio ir tabako ataskaitų duomenys

Narkotikų, tabako ir alkoholio kontrolės departamento (NTAKD) naudojamoje alkoholio produktų ir tabako gaminių ataskaitų teikimo sistemoje kaupiamos juridinių bei fizinių asmenų pateiktos alkoholio ir tabako gaminių ataskaitos. Duomenys sistemoje kaupiami nuo 2020 m. ir atnaujinami iki šiol. Duomenų rinkinys sudarytas iš: ataskaitą pateikusio fizinio arba juridinio asmens pseudonimizuoto kodo, ataskaitos teikėjo asmens rūšies, alkoholio arba tabako gaminio pavadinimo, gaminio KN kodo, licencijos, skaičiaus, kiek atitinkamo gaminio pagaminta arba nupirkta bei parduota arba panaudota atitinkamu ataskaitos periodu, mato vieneto bei ataskaitos periodo metų, numerio ir dažnio. Vienas įrašas atitinka vieną ataskaitos teikėjo, gaminio, ataskaitos metų ir periodo numerio kombinaciją.

- **Model:** `datasets/gov/ntakd/ataskaitos/Ataskaita`[^manifest]
- **Dataset:** [Alkoholio ir tabako ataskaitų duomenys](../ataskaitos.md) (`datasets/gov/ntakd/ataskaitos`)
- **Manifest CSV:** [datasets/gov/ntakd/alkoholis_tabakas.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/alkoholis_tabakas.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ntakd/ataskaitos/Ataskaita`
- **Primary Key (`ref`):** `medziagos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `medziagos_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `ataskaitos_teikejo_kodas` | `string` | — | `4` | `open` | — | Ataskaitą pateikusio asmens pseudonimizuotas kodas | — |
| `ataskaitos_teikejo_asmens_rusis` | `string` | — | `4` | `open` | — | Ataskaitą pateikusio asmens rūšis | — |
| `gaminys` | `string` | — | `4` | `open` | — | Ataskaitoje nurodytas gaminys | — |
| `gaminio_kn_kodas` | `string` | — | `4` | `open` | — | Ataskaitoje nurodyto gaminio KN kodas | — |
| `licencija_leidimas` | `string` | — | `4` | `open` | — | Gaminiui priskirta licencija arba leidimas | — |
| `pagamintas_ar_pirktas_kiekis` | `number` | — | `4` | `open` | — | Skaičius, kiek buvo pagaminta arba nupirkta gaminio | — |
| `parduotas_ar_panaudotas_kiekis` | `number` | — | `4` | `open` | — | Skaičius, kiek buvo parduota arba panaudota gaminio | — |
| `mato_vienetas` | `string` | — | `4` | `open` | — | Gaminio matavimo vienetas | — |
| `ataskaitinio_periodo_metai` | `integer` | — | `4` | `open` | — | Ataskaitos periodo metai | — |
| `ataskaitinio_periodo_nr` | `integer` | — | `4` | `open` | — | Ataskaitos periodo numeris tam tikrais metais | — |
| `ataskaitinio_periodo_daznis` | `string` | — | `4` | `open` | — | Ataskaitos periodo dažnis | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ataskaitos_teikejo_asmens_rusis` | `"Juridinis"` | — | — | LR juridinis asmuo | — |
| `ataskaitos_teikejo_asmens_rusis` | `"Fizinis"` | — | — | LR fizinis asmuo | — |
| `ataskaitos_teikejo_asmens_rusis` | `"Nežinoma"` | — | — | Nei LR juridinis, nei LR fizinis asmuo | — |
| `mato_vienetas` | `"lpa"` | — | — | Litrai gryno alkoholio (angl. litres of pure alcohol) | — |
| `mato_vienetas` | `"vnt"` | — | — | Vienetai | — |
| `mato_vienetas` | `"kg"` | — | — | Kilogramai | — |
| `mato_vienetas` | `"l"` | — | — | Litrai | — |
| `ataskaitinio_periodo_daznis` | `"MONTHLY"` | — | — | Kas mėnesį | — |
| `ataskaitinio_periodo_daznis` | `"QUARTERLY"` | — | — | Kas metų ketvirtį | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ntakd/alkoholis_tabakas.csv
