---
type: Table
title: "Dokumentas — Juridinių asmenų registre įregistruotų juridinių asmenų steigimo dokumentai"
description: "Duomenys apie Lietuvos Respublikos juridinių asmenų registre įregistruotų juridinių asmenų registro tvarkytojui pateiktus dokumentus (kodas, pavadinimas, dokumentų rūšis, dokumentų data, įregistravimo data)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/dokumentai/Dokumentas"
tags: [gov, rc, dokumentas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/dokumentai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/dokumentai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1565/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/dokumentai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Dokumentas — Juridinių asmenų registre įregistruotų juridinių asmenų steigimo dokumentai

**Dataset Context:** Duomenys apie Lietuvos Respublikos juridinių asmenų registre įregistruotų juridinių asmenų registro tvarkytojui pateiktus dokumentus (kodas, pavadinimas, dokumentų rūšis, dokumentų data, įregistravimo data). Individualių įmonių, komanditinių ūkinių bendrijų, tikrųjų ūkinių bendrijų pavadinimai nuasmeninti.[^manifest]

- **Model:** `datasets/gov/rc/jar/dokumentai/Dokumentas`[^manifest]
- **Dataset:** [Juridinių asmenų registre įregistruotų juridinių asmenų steigimo dokumentų, pateiktų registro...](../dokumentai.md) (`datasets/gov/rc/jar/dokumentai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/dokumentai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/dokumentai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/dokumentai/Dokumentas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `juridinis_asmuo`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [JuridinisAsmuo](../iregistruoti/JuridinisAsmuo.md) (`level=4 UUID`: `juridinis_asmuo._id`) | `4` | `open` | — | Juridinio asmens kodas iš juridinių asmenų registro | — |
| `dokumento_tipas` | `ref` | [DokumentoTipas](../dokumentu_tipai_potipiai/DokumentoTipas.md) (`level=4 UUID`: `dokumento_tipas._id`) | `4` | `open` | — | Juridinių asmenų registrui juridinio asmens pateikto dokumento tipas iš jar dokumentų tipų klasifikatoriaus | — |
| `dokumento_potipis` | `ref` | [DokumentoPotipis](../dokumentu_tipai_potipiai/DokumentoPotipis.md) (`level=4 UUID`: `dokumento_potipis._id`) | `4` | `open` | — | Juridinių asmenų registrui juridinio asmens pateikto dokumento potipio pavadinimas | — |
| `dok_data` | `date` | `D` | `4` | `open` | — | Juridinių asmenų registrui juridinio asmens pateikto dokumento data | — |
| `dok_reg_data` | `date` | `D` | `4` | `open` | — | Juridinių asmenų registrui juridinio asmens pateikto dokumento įregistravimo juridinių asmenų registre data | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/dokumentai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/dokumentai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/dokumentai (https://data.gov.lt/datasets/1565/)
