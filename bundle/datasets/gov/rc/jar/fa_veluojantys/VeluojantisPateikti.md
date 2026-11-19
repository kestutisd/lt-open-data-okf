---
type: Table
title: "VeluojantisPateikti — Juridinių asmenų registre įregistruoto juridinio asmens kodas"
description: "Duomenys apie finansinės atskaitomybės dokumentus už praėjusius finansinius metus daugiau nei 60 d."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/fa_veluojantys/VeluojantisPateikti"
tags: [gov, rc, veluojantispateikti, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/fa_veluojantys.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/fa_veluojantys.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1572/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/fa_veluojantys"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# VeluojantisPateikti — Juridinių asmenų registre įregistruoto juridinio asmens kodas

**Dataset Context:** Duomenys apie finansinės atskaitomybės dokumentus už praėjusius finansinius metus daugiau nei 60 d. vėluojančius pateikti juridinius asmenis[^manifest]

- **Model:** `datasets/gov/rc/jar/fa_veluojantys/VeluojantisPateikti`[^manifest]
- **Dataset:** [Jurdiniai asmenys vėluojantys pateikti finansinės atskaitomybės dokumentus už praėjusius...](../fa_veluojantys.md) (`datasets/gov/rc/jar/fa_veluojantys`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/fa_veluojantys.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/fa_veluojantys.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/fa_veluojantys/VeluojantisPateikti` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `juridinis_asmuo`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [JuridinisAsmuo](../iregistruoti/JuridinisAsmuo.md) (`level=4 UUID`: `juridinis_asmuo._id`) | `4` | `open` | — | Juridinis asmuo juridinių asmenų registre | — |
| `ja_reg_data` | `date` | `D` | `4` | `open` | — | Juridinio asmens įregistravimo juridinių asmenų registre data | — |
| `forma` | `ref` | [Forma](../formos_statusai/Forma.md) (`level=4 UUID`: `forma._id`) | `4` | `open` | — | Juridinio asmens formos kodas | — |
| `statusas` | `ref` | [Statusas](../formos_statusai/Statusas.md) (`level=4 UUID`: `statusas._id`) | `4` | `open` | — | Juridinio asmens teisinio statuso kodas | — |
| `veluojantis_iki` | `date` | `D` | `4` | `open` | — | Metai, už kuriuos juridinio asmens pateikta paskutinė finansinė ataskaita | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/fa_veluojantys.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/fa_veluojantys.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/fa_veluojantys (https://data.gov.lt/datasets/1572/)
