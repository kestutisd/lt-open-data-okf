---
type: Table
title: "Procedura — Prašomos įforminti procedūros aprašymai pagal kodus"
description: "Prašomos įforminti procedūros aprašymų klasifikatorius pagal kodus, naudojamas muitinės deklaracijų duomenyse nurodytoms procedūroms aprašyti"
resource: "https://get.data.gov.lt/datasets/gov/muitine/deklaraciju_apdorojimo_sistema/Procedura"
tags: [gov, muitine, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L30"
    last_modified: "2026-11-11T14:39:20Z"
---

# Procedura — Prašomos įforminti procedūros aprašymai pagal kodus

Prašomos įforminti procedūros aprašymų klasifikatorius pagal kodus, naudojamas muitinės deklaracijų duomenyse nurodytoms procedūroms aprašyti

- **Model:** `datasets/gov/muitine/deklaraciju_apdorojimo_sistema/Procedura`[^manifest]
- **Dataset:** [Muitinės importo ir eksporto deklaracijų duomenys ir deklaracijų prašomų įforminti procedūrų klasifikatorius](../deklaraciju_apdorojimo_sistema.md) (`datasets/gov/muitine/deklaraciju_apdorojimo_sistema`)
- **Manifest CSV:** [datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L30](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L30)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/deklaraciju_apdorojimo_sistema/Procedura`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA pirminis raktas | — |
| `pip_kodas` | `string` | — | `4` | `open` | — | Prašomos įforminti procedūros kodas | — |
| `pip_aprasymas` | `string` | — | `4` | `open` | — | Prašomos įforminti procedūros aprašymas | — |
| `pip_aprasymo_kalba` | `string` | — | `4` | `open` | — | Prašomos įforminti procedūros aprašymo kalba | — |
| `novis_saraso_kodas` | `string` | — | `4` | `open` | — | Sarašo kodas NOVIS sistemoje | — |
| `ar_pip_kodas_galioja` | `boolean` | — | `4` | `open` | — | Ar procedūros kodas rinkinio atnaujinimo metu galioja | — |
| `pip_kodo_galiojimo_pradzia` | `date` | `D` | `4` | `open` | — | Procedūros kodo galiojimo pradžia | — |
| `pip_kodo_galiojimo_pabaiga` | `date` | `D` | `4` | `open` | — | Procedūros kodo galiojimo pabaiga | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pip_aprasymo_kalba` | `"LT"` | — | — | — | — |
| `pip_aprasymo_kalba` | `"EN"` | — | — | — | — |
| `novis_saraso_kodas` | `"446COM"` | — | — | — | — |
| `novis_saraso_kodas` | `"593COM"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv
