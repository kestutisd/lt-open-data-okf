---
type: Table
title: "ValdymoOrganas — Juridinių asmenų valdymo organai"
description: "Duomenys, apibūdinantys Lietuvos Respublikos juridinių asmenų registre įregistruotų juridinių asmenų valdymo organus ir jų formas (juridinius asmenis apibūdinantys duomenys (kodas, valdymo organai)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/valdymo_organai/ValdymoOrganas"
tags: [gov, rc, valdymoorganas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/valdymo_organai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/valdymo_organai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1564/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/valdymo_organai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# ValdymoOrganas — Juridinių asmenų valdymo organai

**Dataset Context:** Duomenys, apibūdinantys Lietuvos Respublikos juridinių asmenų registre įregistruotų juridinių asmenų valdymo organus ir jų formas (juridinius asmenis apibūdinantys duomenys (kodas, valdymo organai). Individualių įmonių, komanditinių ūkinių bendrijų, tikrųjų ūkinių bendrijų pavadinimai nuasmeninti.[^manifest]

- **Model:** `datasets/gov/rc/jar/valdymo_organai/ValdymoOrganas`[^manifest]
- **Dataset:** [Juridinių asmenų registre įregistruotų juridinių asmenų valdymo organai, jų formos (raw data)](../valdymo_organai.md) (`datasets/gov/rc/jar/valdymo_organai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/valdymo_organai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/valdymo_organai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/valdymo_organai/ValdymoOrganas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `juridinis_asmuo`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [JuridinisAsmuo](../iregistruoti/JuridinisAsmuo.md) (`level=4 UUID`: `juridinis_asmuo._id`) | `4` | — | — | Juridinio asmens pavadinimas iš juridinių asmenų registro | — |
| `vadovas` | `integer` | — | `4` | `open` | — | Juridinio asmens vienasmenis valdymo organas – vadovas | — |
| `vad_org_nuo` | `date` | `D` | `4` | `open` | — | Juridinio asmens vienasmenio valdymo organo - vadovo įregistravimo juridinių asmenų registre data | — |
| `vad_lytis` | `string` | — | `4` | `open` | — | Vadovo lytis: V - vyras, M - moteris, ND - nėra duomenų apie vadovo lytį | — |
| `valdyba` | `integer` | — | `4` | `open` | — | Juridinio asmens daugiaasmenis valdymo organas – valdyba | — |
| `vald_org_nuo` | `date` | `D` | `4` | `open` | — | Juridinio asmens daugiaasmenio valdymo organo - valdybos įregistravimo juridinių asmenų registre data | — |
| `taryba` | `integer` | — | `4` | `open` | — | Juridinio asmens daugiaasmenis valdymo organas – taryba | — |
| `tar_org_nuo` | `date` | `D` | `4` | `open` | — | Juridinio asmens daugiaasmenio valdymo organo – tarybos įregistravimo juridinių asmenų registre data | — |
| `kiti_valdymo_organai` | `integer` | — | `4` | `open` | — | Kiti juridinio asmens valdymo organai | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vadovas` | `1` | — | — | Vadovas yra | — |
| `vadovas` | `0` | — | — | Vadovo nėra | — |
| `valdyba` | `1` | — | — | Valdyba yra | — |
| `valdyba` | `0` | — | — | Valdybos nėra | — |
| `taryba` | `1` | — | — | Taryba yra | — |
| `taryba` | `0` | — | — | Tarybos nėra | — |
| `kiti_valdymo_organai` | `1` | — | — | Kiti juridinio asmens valdymo organai yra | — |
| `kiti_valdymo_organai` | `0` | — | — | Kitų juridinio asmens valdymo organų nėra | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/valdymo_organai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/valdymo_organai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/valdymo_organai (https://data.gov.lt/datasets/1564/)
