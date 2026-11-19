---
type: Table
title: "Istaiga — Sveikatos priežiūros įstaigos"
description: "Valstybinės akreditavimo sveikatos priežiūrai veiklos tarnybos duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/Istaiga"
tags: [gov, vaspvt, istaiga, deployed, level-2, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L9"
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv#L9"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1623/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vaspvt/licencijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Istaiga — Sveikatos priežiūros įstaigos

**Dataset Context:** Valstybinės akreditavimo sveikatos priežiūrai veiklos tarnybos duomenys[^manifest]

- **Model:** `datasets/gov/vaspvt/licencijos/Istaiga`[^manifest]
- **Dataset:** [Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba](../licencijos.md) (`datasets/gov/vaspvt/licencijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L9)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/Istaiga` (`deployed`)[^manifest]
- **Provider:** `vaspvt` — Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `spi_id`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `spi_id` | `string` | — | `4` | `open` | — | Sveikatos priežiūros įstaigos identifikatorius | — |
| `ja_kodas` | `string` | — | `2` | `open` | — | Sveikatos priežiūros įstaigos juridinio asmens kodas | — |
| `ja_pavadinimas` | `string` | — | `2` | `open` | — | Sveikatos priežiūros įstaigos pavadinimas | — |
| `teisine_forma` | `string` | — | `4` | `open` | — | Juridinio asmens teisinė forma | — |
| `adresas` | `string` | — | `2` | `open` | — | Juridinio asmens buveinės adresas | — |
| `licencijos_nr` | `string` | — | `4` | `open` | — | Licencijos numeris | — |
| `licencijos_isdavimo_data` | `datetime` | — | `3` | `open` | — | Licencijos išdavimo data | — |
| `asmuo_visuomene` | `string` | — | `2` | `open` | — | Žyma, ar tai asmens, ar visuomenės sveikatos priežiūros įstaigos licencija | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo", ref: "ja_kodas")` | `base` | `4` | `open` | — | — | — |
| `ja_kodas` | `update(type: "")` | `type` | `4` | `open` | — | — | — |
| `ja_pavadinimas` | `update(property: "ja_pavadinimas@lt", type: "")` | `type` | `4` | `open` | — | — | — |
| `adresas` | `update(type: "", ref: "")` | `type` | `4` | `open` | — | — | — |
| `asmuo_visuomene` | `update(ref: "enum")` | `ref` | `4` | `open` | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv#L9 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L9)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vaspvt/licencijos (https://data.gov.lt/datasets/1623/)
