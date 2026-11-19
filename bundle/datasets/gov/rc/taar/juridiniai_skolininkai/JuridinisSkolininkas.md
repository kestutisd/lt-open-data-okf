---
type: Table
title: "JuridinisSkolininkas"
description: "Turto arešto aktų registro nuasmeninti duomenys (RAW DATA) apie skolininkus, kai skolininkai juridiniai asmenys, jų teisinę formą ir kilmės šalį, turto arešto aktų jų statusus, įregistravimo / išregistravimo datas, areštuojančių institucijų."
resource: "https://get.data.gov.lt/datasets/gov/rc/taar/juridiniai_skolininkai/JuridinisSkolininkas"
tags: [gov, rc, juridinisskolininkas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/juridiniai_skolininkai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/taar/juridiniai_skolininkai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2233/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/taar/juridiniai_skolininkai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# JuridinisSkolininkas

**Dataset Context:** Turto arešto aktų registro nuasmeninti duomenys (RAW DATA) apie skolininkus, kai skolininkai juridiniai asmenys, jų teisinę formą ir kilmės šalį, turto arešto aktų jų statusus, įregistravimo / išregistravimo datas, areštuojančių institucijų.[^manifest]

- **Model:** `datasets/gov/rc/taar/juridiniai_skolininkai/JuridinisSkolininkas`[^manifest]
- **Dataset:** [TAAR pirminiai duomenys (raw data) apie skolininkus (skolininkai juridiniai asmenys)](../juridiniai_skolininkai.md) (`datasets/gov/rc/taar/juridiniai_skolininkai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/taar/juridiniai_skolininkai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/juridiniai_skolininkai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/taar/juridiniai_skolininkai/JuridinisSkolininkas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Turto arešto akto dirbtinis identifikavimo kodas šiame rinkinyje | — |
| `dokumento_statusas` | `ref` | [DokumentoStatusas](../klasifikatoriai/DokumentoStatusas.md) (`level=4 UUID`: `dokumento_statusas._id`) | `4` | `open` | — | Turto arešto akto statusas iš TAAR dokumentų statusų klasifikatoriaus | — |
| `ai_tipas` | `ref` | [AI](../klasifikatoriai/AI.md) (`level=4 UUID`: `ai_tipas._id`) | `4` | `open` | — | Areštuojančios institucijos tipas iš TAAR areštuojančių institucijų klasifikatoriaus | — |
| `skolininkoid` | `integer` | — | `4` | `open` | — | Juridinio asmens dirbtinis identifikavimo kodas šiame rinkinyje | — |
| `jar_teisine_forma` | `ref` | [Forma](../../jar/formos_statusai/Forma.md) (`level=4 UUID`: `jar_teisine_forma._id`) | `4` | `open` | — | Juridinio asmens teisinė forma iš JAR teisinių formų klasifikatoriaus | — |
| `ar_uzsienietis` | `integer` | — | `4` | `open` | — | Požymis, ar Juridinis asmuo įregistruotas Juridinių asmenų registre | — |
| `taa_iregistravimo_metai` | `integer` | — | `2` | `open` | — | Turto arešto akto įregistravimo metai | — |
| `taa_iregistravimo_menuo` | `integer` | — | `2` | `open` | — | Turto arešto akto įregistravimo mėnuo | — |
| `taa_isregistravimo_metai` | `integer` | — | `2` | `open` | — | Turto arešto akto išregistravimo metai | — |
| `taa_isregistravimo_menuo` | `integer` | — | `2` | `open` | — | Turto arešto akto išregistravimo mėnuo | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ar_uzsienietis` | `1` | — | — | Taip | — |
| `ar_uzsienietis` | `0` | — | — | Ne | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/taar/juridiniai_skolininkai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/juridiniai_skolininkai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/taar/juridiniai_skolininkai (https://data.gov.lt/datasets/2233/)
