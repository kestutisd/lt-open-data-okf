---
type: Table
title: "Biobankas — Biobanko atveriami duomenys"
description: "Spinta table datasets/gov/nvi/biobankas/Biobankas (15 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nvi/biobankas/Biobankas"
tags: [gov, nvi, biobankas, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvi/biobankas.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/nvi/biobankas.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Biobankas — Biobanko atveriami duomenys

- **Model:** `datasets/gov/nvi/biobankas/Biobankas`[^manifest]
- **Dataset:** [datasets/gov/nvi/biobankas](../biobankas.md) (`datasets/gov/nvi/biobankas`)[^manifest]
- **Manifest CSV:** [datasets/gov/nvi/biobankas.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvi/biobankas.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nvi/biobankas/Biobankas` (`deployed`)[^manifest]
- **Provider:** `nvi` — Nacionalinis vėžio institutas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `meg_nr, meg_pavad`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `amzgr` | `string` | — | `4` | `open` | — | Paciento amžiaus grupė | — |
| `diagnoze` | `ref` | [Tlk10am](../../vlk/tlk10am/Tlk10am.md) (`level=4 UUID` via `Tlk10am[name]`: `diagnoze._id`) | `4` | `open` | — | Diagnozė pagal TLK-10 | — |
| `lok_kodas` | `string` | — | `4` | `open` | — | Lokalizacijos kodas | — |
| `ind_pavad` | `string` | — | `4` | `open` | — | Indelio pavadinimas | — |
| `kiekis` | `number` | — | `3` | `open` | — | Medžiagos kiekis | — |
| `lokalizacija` | `string` | — | `3` | `open` | — | Medžiaga / naviko lokalizacija, iš kurios buvo paimta medžiaga | — |
| `lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `meg_men` | `integer` | — | `2` | `open` | — | Mėginio paėmimo mėnuo | — |
| `meg_metai` | `integer` | — | `2` | `open` | — | Mėginio paėmimo metai | — |
| `meg_nr` | `string` | — | `4` | `open` | — | Mėginio Nr. | — |
| `meg_pavad` | `string` | — | `4` | `open` | — | Mėginio pavadinimas | — |
| `pm` | `string` | — | `4` | `open` | — | pTNM M dalis | — |
| `pn` | `string` | — | `4` | `open` | — | pTNM N dalis | — |
| `pt` | `string` | — | `4` | `open` | — | pTNM T dalis | — |
| `vnt` | `string` | — | `4` | `open` | — | Mato vienetas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ind_pavad` | `"Cryo mėg."` | — | — | Cryo mėg. | — |
| `ind_pavad` | `"Mėgintuvėlis"` | — | — | Megintuvėlis | — |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |
| `meg_pavad` | `"Kraujas"` | — | — | Kraujas | — |
| `meg_pavad` | `"Navikas"` | — | — | Navikas | — |
| `meg_pavad` | `"Plazma"` | — | — | Plazma | — |
| `meg_pavad` | `"Plazmos ląstelės"` | — | — | Plazmos ląstelės | — |
| `meg_pavad` | `"Serumas"` | — | — | Serumas | — |
| `meg_pavad` | `"Sveikas audinys"` | — | — | Sveikas audinys | — |
| `meg_pavad` | `"Šlapimas"` | — | — | Šlapimas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `meg_metai` | `update(type: "date", ref: "Y")` | `type` | `2` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nvi/biobankas.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvi/biobankas.csv#L5)
