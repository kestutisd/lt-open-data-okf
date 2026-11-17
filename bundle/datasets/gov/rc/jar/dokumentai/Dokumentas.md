---
type: Table
title: "Dokumentas — Juridinių asmenų registre įregistruotų juridinių asmenų steigimo dokumentai"
description: "Spinta table datasets/gov/rc/jar/dokumentai/Dokumentas (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/dokumentai/Dokumentas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/dokumentai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/dokumentai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Dokumentas — Juridinių asmenų registre įregistruotų juridinių asmenų steigimo dokumentai

- **Model:** `datasets/gov/rc/jar/dokumentai/Dokumentas`[^manifest]
- **Dataset:** [Juridinių asmenų registre įregistruotų juridinių asmenų steigimo dokumentų, pateiktų registro tvarkytojui, duomenys (raw data)](../dokumentai.md) (`datasets/gov/rc/jar/dokumentai`)
- **Manifest CSV:** [datasets/gov/rc/jar/dokumentai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/dokumentai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/dokumentai/Dokumentas`
- **Primary Key (`ref`):** `juridinis_asmuo`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Juridinio asmens kodas iš juridinių asmenų registro | — |
| `dokumento_tipas` | `ref` | [/datasets/gov/rc/jar/dokumentu_tipai_potipiai/DokumentoTipas](../dokumentu_tipai_potipiai/DokumentoTipas.md) | `4` | `open` | — | Juridinių asmenų registrui juridinio asmens pateikto dokumento tipas iš jar dokumentų tipų klasifikatoriaus | — |
| `dokumento_potipis` | `ref` | [/datasets/gov/rc/jar/dokumentu_tipai_potipiai/DokumentoPotipis](../dokumentu_tipai_potipiai/DokumentoPotipis.md) | `4` | `open` | — | Juridinių asmenų registrui juridinio asmens pateikto dokumento potipio pavadinimas | — |
| `dok_data` | `date` | `D` | `4` | `open` | — | Juridinių asmenų registrui juridinio asmens pateikto dokumento data | — |
| `dok_reg_data` | `date` | `D` | `4` | `open` | — | Juridinių asmenų registrui juridinio asmens pateikto dokumento įregistravimo juridinių asmenų registre data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/dokumentai.csv
