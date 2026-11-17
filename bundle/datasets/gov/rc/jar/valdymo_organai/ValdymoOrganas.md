---
type: Table
title: "ValdymoOrganas — Juridinių asmenų valdymo organai"
description: "Spinta table datasets/gov/rc/jar/valdymo_organai/ValdymoOrganas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/valdymo_organai/ValdymoOrganas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/valdymo_organai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/valdymo_organai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# ValdymoOrganas — Juridinių asmenų valdymo organai

- **Model:** `datasets/gov/rc/jar/valdymo_organai/ValdymoOrganas`[^manifest]
- **Dataset:** [Juridinių asmenų registre įregistruotų juridinių asmenų valdymo organai, jų formos (raw data)](../valdymo_organai.md) (`datasets/gov/rc/jar/valdymo_organai`)
- **Manifest CSV:** [datasets/gov/rc/jar/valdymo_organai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/valdymo_organai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/valdymo_organai/ValdymoOrganas`
- **Primary Key (`ref`):** `juridinis_asmuo`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../iregistruoti/JuridinisAsmuo.md) | `4` | — | — | Juridinio asmens pavadinimas iš juridinių asmenų registro | — |
| `vadovas` | `integer` | — | `4` | `open` | — | Juridinio asmens vienasmenis valdymo organas – vadovas | — |
| `vad_org_nuo` | `date` | `D` | `4` | `open` | — | Juridinio asmens vienasmenio valdymo organo - vadovo įregistravimo juridinių asmenų registre data | — |
| `vad_lytis` | `string` | — | `4` | `open` | — | Vadovo lytis: V - vyras, M - moteris, ND - nėra duomenų apie vadovo lytį | — |
| `valdyba` | `integer` | — | `4` | `open` | — | Juridinio asmens daugiaasmenis valdymo organas – valdyba | — |
| `vald_org_nuo` | `date` | `D` | `4` | `open` | — | Juridinio asmens daugiaasmenio valdymo organo - valdybos įregistravimo juridinių asmenų registre data | — |
| `taryba` | `integer` | — | `4` | `open` | — | Juridinio asmens daugiaasmenis valdymo organas – taryba | — |
| `tar_org_nuo` | `date` | `D` | `4` | `open` | — | Juridinio asmens daugiaasmenio valdymo organo – tarybos įregistravimo juridinių asmenų registre data | — |
| `kiti_valdymo_organai` | `integer` | — | `4` | `open` | — | Kiti juridinio asmens valdymo organai | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vadovas` | `1` | — | — | Vadovas yra | — |
| `vadovas` | `0` | — | — | Vadovo nėra | — |
| `valdyba` | `1` | — | — | Valdyba yra | — |
| `valdyba` | `0` | — | — | Valdybos nėra | — |
| `taryba` | `1` | — | — | Taryba yra | — |
| `taryba` | `0` | — | — | Tarybos nėra | — |
| `kiti_valdymo_organai` | `1` | — | — | Kiti juridinio asmens valdymo organai yra | — |
| `kiti_valdymo_organai` | `0` | — | — | Kitų juridinio asmens valdymo organų nėra | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/valdymo_organai.csv
