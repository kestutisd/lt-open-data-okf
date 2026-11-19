---
type: Table
title: "LeistinasAtributas — Juridinių asmenų registro leistinų atributų klasifikatorius pagal teisines formas"
description: "Lietuvos Respublikos juridinių asmenų registro atributų klasifikatoriai (duomenų rinkinių grupė, viso 4 vnt.) (JAR atributų klasifikatorius; JAR kokybinių atributų klasifikatorius; JAR leistinų atributų klasifikatorius; JAR tekstinių atributų klasifikatorius)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/atributai/LeistinasAtributas"
tags: [gov, rc, leistinasatributas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/atributai.csv#L16"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/atributai.csv#L16"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1627/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/atributai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# LeistinasAtributas — Juridinių asmenų registro leistinų atributų klasifikatorius pagal teisines formas

**Dataset Context:** Lietuvos Respublikos juridinių asmenų registro atributų klasifikatoriai (duomenų rinkinių grupė, viso 4 vnt.) (JAR atributų klasifikatorius; JAR kokybinių atributų klasifikatorius; JAR leistinų atributų klasifikatorius; JAR tekstinių atributų klasifikatorius).[^manifest]

- **Model:** `datasets/gov/rc/jar/atributai/LeistinasAtributas`[^manifest]
- **Dataset:** [Juridinių asmenų registro atributų klasifikatoriai](../atributai.md) (`datasets/gov/rc/jar/atributai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/atributai.csv#L16](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/atributai.csv#L16)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/atributai/LeistinasAtributas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `forma,atributas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `forma` | `ref` | [Forma](../formos_statusai/Forma.md) (`level=4 UUID`: `forma._id`) | `4` | `open` | — | Juridinių asmenų registro leistina forma | — |
| `atributas` | `ref` | [Atributas](Atributas.md) (`level=4 UUID`: `atributas._id`) | `4` | `open` | — | Juridinių asmenų registro leistino atributo kodas | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/atributai.csv#L16 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/atributai.csv#L16)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/atributai (https://data.gov.lt/datasets/1627/)
