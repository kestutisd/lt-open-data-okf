---
type: Table
title: "Paslauga — Asmens sveikatos priežiūros paslaugų sąrašas"
description: "Asmens sveikatos priežiūros paslaugų klasifikatorius, patvirtintas Valstybinės ligonių kasos prie Sveikatos apsaugos ministerijos direktoriaus 2005 m. birželio 30 d. įsakymu Nr. 1K-81 „Dėl asmens sveikatos priežiūros paslaugų ir..."
resource: "https://get.data.gov.lt/datasets/gov/vlk/paslaugos/Paslauga"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/paslaugos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/paslaugos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Paslauga — Asmens sveikatos priežiūros paslaugų sąrašas

Asmens sveikatos priežiūros paslaugų klasifikatorius, patvirtintas Valstybinės ligonių kasos prie Sveikatos apsaugos ministerijos direktoriaus 2005 m. birželio 30 d. įsakymu Nr. 1K-81 „Dėl asmens sveikatos priežiūros paslaugų ir sveikatos programose numatytų paslaugų, už kurias mokama iš Privalomojo sveikatos draudimo fondo biudžeto, klasifikatoriaus patvirtinimo“

- **Model:** `datasets/gov/vlk/paslaugos/Paslauga`[^manifest]
- **Dataset:** [datasets/gov/vlk/paslaugos](../paslaugos.md) (`datasets/gov/vlk/paslaugos`)
- **Manifest CSV:** [datasets/gov/vlk/paslaugos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/paslaugos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/paslaugos/Paslauga`
- **Primary Key (`ref`):** `ad_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `amzius` | `string` | — | `4` | `open` | — | Paciento amžiaus grupė | Paciento, kuriam gali būti teikiama paslauga, amžiaus grupė |
| `kodas` | `string` | — | `4` | `open` | — | Paslaugos kodas | Paslaugos kodas pagal VLK direktoriaus 2005 m. birželio 30 d. įsakymą Nr. 1K-81 "Dėl asmens sveikatos priežiūros paslaugų ir sveikatos programose numatytų paslaugų, už kurias mokama iš Privalomojo sveikatos draudimo fondo biudžeto, klasifikatoriaus patvirtinimo" |
| `pavadinimas` | `string` | — | `4` | `open` | — | Paslaugos pavadinimas | Paslaugos pavadinimas pagal VLK direktoriaus 2005 m. birželio 30 d. įsakymą Nr. 1K-81 "Dėl asmens sveikatos priežiūros paslaugų ir sveikatos programose numatytų paslaugų, už kurias mokama iš Privalomojo sveikatos draudimo fondo biudžeto, klasifikatoriaus patvirtinimo". Kai kurių paslaugų pavadinimai yra nepilni, kadangi IS Sveidra pavadinimo lauke simbolių skaičius yra ribotas |
| `teikimo_salygos` | `string` | — | `4` | `open` | — | Paslaugos teikimo sąlygos | Paslaugų teikimo sąlygos: ambulatorinės, stacionarinės bei dienos stacionaro sąlygos |
| `paslaugos_tipo_kodas` | `integer` | — | `2` | `open` | — | Paslaugos tipo kodas | Paslaugos tipas pagal VLK direktoriaus 2005 m. birželio 30 d. įsakymą Nr. 1K-81 "Dėl asmens sveikatos priežiūros paslaugų ir sveikatos programose numatytų paslaugų, už kurias mokama iš Privalomojo sveikatos draudimo fondo biudžeto, klasifikatoriaus patvirtinimo" |
| `paslaugos_tipo_pavadinimas` | `string` | — | `2` | `open` | — | Paslaugos tipo pavadinimas | Paslaugos tipas pagal VLK direktoriaus 2005 m. birželio 30 d. įsakymą Nr. 1K-81 "Dėl asmens sveikatos priežiūros paslaugų ir sveikatos programose numatytų paslaugų, už kurias mokama iš Privalomojo sveikatos draudimo fondo biudžeto, klasifikatoriaus patvirtinimo" |
| `lygis` | `string` | — | `4` | `open` | — | Paslaugos lygio kodas | Paslaugos lygio kodas |
| `nuo` | `date` | `D` | `4` | `open` | — | Paslauga teikiama nuo | Paslaugos galiojimo pradžios data |
| `iki` | `date` | `D` | `4` | `open` | — | Paslauga teikiama iki | Paslaugos galiojimo pabaigos data |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `amzius` | `"Vaikas"` | — | — | Vaikas | — |
| `amzius` | `"Suaugęs"` | — | — | Suaugęs | — |
| `teikimo_salygos` | `"Ambulatorinės"` | — | — | Ambulatorinės | — |
| `teikimo_salygos` | `"Dienos"` | — | — | Dienos | — |
| `teikimo_salygos` | `"Stacionarinės"` | — | — | Stacionarinės | — |
| `teikimo_salygos` | `"Ambulatorinės/stacionarinės"` | — | — | Ambulatorinės/stacionarinės | — |
| `lygis` | `"I lygis"` | — | — | Pirmas lygis | — |
| `lygis` | `"II lygis"` | — | — | Antras lygis | — |
| `lygis` | `"III lygis"` | — | — | Trečias lygis | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paslaugos_tipo_kodas` | `create(property: "tipas", type: "ref", ref: "Tipas")` | `property` | `4` | — | — | — | — |
| `paslaugos_tipo_kodas` | `update(property: "tipas.kodas", type: "")` | `property` | `4` | — | — | — | — |
| `paslaugos_tipo_pavadinimas` | `update(property: "tipas.pavadinimas", type: "")` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/paslaugos.csv
