---
type: Table
title: "NeJuridinisAsmuo — Juridinių asmenų registro ne juridinių asmenų (valstybės, savivaldybių, valstybės ir savivaldybių atstovaujamųjų ir vykdomųjų institucijų, kurios neregistruojamos juridinių asmenų registre) klasifikatorius"
description: "Lietuvos Respublikos juridinių asmenų registro ne juridinių asmenų (valstybės, savivaldybių, valstybės ir savivaldybių atstovaujamųjų ir vykdomųjų institucijų, kurios neregistruojamos JAR) klasifikatorius"
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/ne_juridiniai_asmenys/NeJuridinisAsmuo"
tags: [gov, rc, nejuridinisasmuo, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/ne_juridiniai_asmenys.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/ne_juridiniai_asmenys.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1633/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/ne_juridiniai_asmenys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NeJuridinisAsmuo — Juridinių asmenų registro ne juridinių asmenų (valstybės, savivaldybių, valstybės ir savivaldybių atstovaujamųjų ir...

**Dataset Context:** Lietuvos Respublikos juridinių asmenų registro ne juridinių asmenų (valstybės, savivaldybių, valstybės ir savivaldybių atstovaujamųjų ir vykdomųjų institucijų, kurios neregistruojamos JAR) klasifikatorius[^manifest]

- **Model:** `datasets/gov/rc/jar/ne_juridiniai_asmenys/NeJuridinisAsmuo`[^manifest]
- **Dataset:** [Juridinių asmenų registro ne juridinių asmenų (valstybės, savivaldybių, valstybės ir...](../ne_juridiniai_asmenys.md) (`datasets/gov/rc/jar/ne_juridiniai_asmenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/ne_juridiniai_asmenys.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/ne_juridiniai_asmenys.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/ne_juridiniai_asmenys/NeJuridinisAsmuo` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `grupes_kodas` | `integer` | — | `3` | `open` | — | Ne juridinio asmens grupės kodas | — |
| `kodas` | `string` | — | `4` | `open` | — | Ne juridinio asmens kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Ne juridinio asmens pavadinimas | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/ne_juridiniai_asmenys.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/ne_juridiniai_asmenys.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/ne_juridiniai_asmenys (https://data.gov.lt/datasets/1633/)
