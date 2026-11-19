---
type: Table
title: "Procedura — Prašomos įforminti procedūros aprašymai pagal kodus"
description: "Prašomos įforminti procedūros aprašymų klasifikatorius pagal kodus, naudojamas muitinės deklaracijų duomenyse nurodytoms procedūroms aprašyti"
resource: "https://get.data.gov.lt/datasets/gov/muitine/deklaraciju_apdorojimo_sistema/Procedura"
tags: [gov, muitine, procedura, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L30"
    title: "atviriduomenys/manifest — datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L30"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3996/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/deklaraciju_apdorojimo_sistema"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Procedura — Prašomos įforminti procedūros aprašymai pagal kodus

Prašomos įforminti procedūros aprašymų klasifikatorius pagal kodus, naudojamas muitinės deklaracijų duomenyse nurodytoms procedūroms aprašyti[^manifest]

- **Model:** `datasets/gov/muitine/deklaraciju_apdorojimo_sistema/Procedura`[^manifest]
- **Dataset:** [Muitinės importo ir eksporto deklaracijų duomenys ir deklaracijų prašomų įforminti procedūrų...](../deklaraciju_apdorojimo_sistema.md) (`datasets/gov/muitine/deklaraciju_apdorojimo_sistema`)[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L30](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L30)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/deklaraciju_apdorojimo_sistema/Procedura` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pip_aprasymo_kalba` | `"LT"` | — | — | — | — |
| `pip_aprasymo_kalba` | `"EN"` | — | — | — | — |
| `novis_saraso_kodas` | `"446COM"` | — | — | — | — |
| `novis_saraso_kodas` | `"593COM"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L30 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/deklaraciju_apdorojimo_sistema.csv#L30)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/deklaraciju_apdorojimo_sistema (https://data.gov.lt/datasets/3996/)
