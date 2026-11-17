---
type: Table
title: "Programa — Neformaliojo vaikų švietimo programos"
description: "Viena eilutė atitinka vieną neformaliojo vaikų švietimo programą"
resource: "https://get.data.gov.lt/datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos/Programa"
tags: [gov, nsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Programa — Neformaliojo vaikų švietimo programos

Viena eilutė atitinka vieną neformaliojo vaikų švietimo programą

- **Model:** `datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos/Programa`[^manifest]
- **Dataset:** [Neformaliojo vaikų švietimo programos](../neformaliojo_vaiku_svietimo_programos.md) (`datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos`)
- **Manifest CSV:** [datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos/Programa`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus lentelės raktas | — |
| `programos_id` | `string` | — | `4` | `open` | — | Programos identifikatorius | — |
| `prg_kodas` | `string` | — | `4` | `open` | — | Neformaliojo švietimo programos kodas | — |
| `prg_pavad_lt` | `string` | — | `4` | `open` | — | Neformaliojo švietimo programos pavadinimas lietuvių kalba | — |
| `prg_pavad_en` | `string` | — | `4` | `open` | — | Neformaliojo švietimo programos pavadinimas anglų kalba | — |
| `prg_ireg_data` | `date` | `D` | `4` | `open` | — | Neformaliojo švietimo programos įregistravimo į neformaliojo švietimo programų registrą data | — |
| `prg_isreg_data` | `date` | `D` | `4` | `open` | — | Neformaliojo švietimo programos išregistravimo iš neformaliojo švietimo programų registro data | — |
| `prg_isreg_priezast_lt` | `string` | — | `4` | `open` | — | Neformaliojo švietimo programos išregistravimo iš neformaliojo švietimo programų registro priežastis anglų kalba | — |
| `prg_isreg_priezast_en` | `string` | — | `4` | `open` | — | Neformaliojo švietimo programos išregistravimo iš neformaliojo švietimo programų registro priežastis lietuvių kalba | — |
| `prg_paskirtis_lt` | `string` | — | `4` | `open` | — | Neformaliojo švietimo programos paskirtis lietuvių kalba | — |
| `prg_paskirtis_en` | `string` | — | `4` | `open` | — | Neformaliojo švietimo programos paskirtis anglų kalba | — |
| `prg_kryptis_lt` | `string` | — | `4` | `open` | — | Neformaliojo švietimo programos kryptis lietuvių kalba | — |
| `prg_kryptis_en` | `string` | — | `4` | `open` | — | Neformaliojo švietimo programos kryptis anglų kalba | — |
| `prg_pakraipa_lt` | `string` | — | `4` | `open` | — | Neformaliojo švietimo programos pskraipa lietuvių kalba | — |
| `prg_pakraipa_en` | `string` | — | `4` | `open` | — | Neformaliojo švietimo programos pakraipa anglų kalba | — |
| `prg_reikalavimai` | `string` | — | `4` | `open` | — | Reikalavimai kuriuos privalo atitikti mokinys norintis lankyti atitinkamą neformaliojo švietimo programą | — |
| `prg_teikejas_lt` | `string` | — | `4` | `open` | — | Neformaliojo švietimo programos tiekėjo pavadinimas lietuvių kalba | — |
| `prg_teikejas_en` | `string` | — | `4` | `open` | — | Neformaliojo švietimo programos tiekėjo pavadinimas anglų kalba | — |
| `prg_teikejo_kodas` | `string` | — | `4` | `open` | — | Neformaliojo švietimo programos tiekėjo kodas | — |
| `prg_teikejo_kodo_tipas` | `string` | — | `4` | `open` | — | Neformaliojo švietimo programos tiekėjo kodo tipas | — |
| `prg_teikejo_kodo_strukt` | `string` | — | `4` | `open` | — | Neformaliojo švietimo programos tiekėjo kodo struktūra | — |
| `prg_teikejo_tipas` | `string` | — | `4` | `open` | — | Neformaliojo švietimo programos tiekėjo tipas | — |
| `prg_teikejo_adresas` | `string` | — | `4` | `open` | — | Neformaliojo švietimo programos tiekėjo adresas | — |
| `prg_paskut_kitimas` | `date` | `D` | `4` | `open` | — | Paskutinio neformaliojo švietimo programos koregavimo data | — |
| `duom_paskut_redagav` | `datetime` | `L` | `4` | `open` | — | Paskutinio įrašo redagavimo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `prg_isreg_priezast_lt` | `"Programos teikėjo prašymu"` | — | — | Programos teikėjo prašymu | — |
| `prg_isreg_priezast_lt` | `"Nevykdant daugiau kaip dvejus metus"` | — | — | Nevykdant daugiau kaip dvejus metus | — |
| `prg_isreg_priezast_lt` | `"Registro tvarkytojo sprendimu"` | — | — | Registro tvarkytojo sprendimu | — |
| `prg_isreg_priezast_lt` | `"Prijungiant prie kitos programos"` | — | — | Prijungiant prie kitos programos | — |
| `prg_isreg_priezast_en` | `"According to the program developer's request"` | — | — | According to the program developer's request | — |
| `prg_isreg_priezast_en` | `"Do not take place more than two years"` | — | — | Do not take place more than two years | — |
| `prg_isreg_priezast_en` | `"By Decision of the Register Manager"` | — | — | By Decision of the Register Manager | — |
| `prg_isreg_priezast_en` | `"Connected to the other program"` | — | — | Connected to the other program | — |
| `prg_teikejo_kodo_tipas` | `"LT JAR kodas"` | — | — | LT JAR kodas | — |
| `prg_teikejo_kodo_tipas` | `"LT asmens kodas"` | — | — | LT asmens kodas | — |
| `prg_teikejo_kodo_tipas` | `"Kitas kodas"` | — | — | Kitas kodas | — |
| `prg_teikejo_kodo_tipas` | `"Senas LT JAR kodas"` | — | — | Senas LT JAR kodas | — |
| `prg_teikejo_kodo_tipas` | `"Institucijos padalinio kodas"` | — | — | Institucijos padalinio kodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos.csv
