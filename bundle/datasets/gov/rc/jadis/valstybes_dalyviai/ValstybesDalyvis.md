---
type: Table
title: "ValstybesDalyvis — Valstybės ir (ar) savivaldybių juridinių asmenų dalyvių duomenys"
description: "Juridinių asmenų dalyvių informacinės sistemos (JADIS) duomenys apie juridinius asmenis, kuriuose dalyvauja valstybė ir (ar) savivaldybės"
resource: "https://get.data.gov.lt/datasets/gov/rc/jadis/valstybes_dalyviai/ValstybesDalyvis"
tags: [gov, rc, valstybesdalyvis, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/valstybes_dalyviai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/jadis/valstybes_dalyviai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1711/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jadis/valstybes_dalyviai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# ValstybesDalyvis — Valstybės ir (ar) savivaldybių juridinių asmenų dalyvių duomenys

**Dataset Context:** Juridinių asmenų dalyvių informacinės sistemos (JADIS) duomenys apie juridinius asmenis, kuriuose dalyvauja valstybė ir (ar) savivaldybės[^manifest]

- **Model:** `datasets/gov/rc/jadis/valstybes_dalyviai/ValstybesDalyvis`[^manifest]
- **Dataset:** [Valstybės ir (ar) savivaldybių juridinių asmenų dalyvių duomenys](../valstybes_dalyviai.md) (`datasets/gov/rc/jadis/valstybes_dalyviai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jadis/valstybes_dalyviai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/valstybes_dalyviai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jadis/valstybes_dalyviai/ValstybesDalyvis` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `juridinis_asmuo`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [JuridinisAsmuo](../../jar/iregistruoti/JuridinisAsmuo.md) (`level=4 UUID`: `juridinis_asmuo._id`) | `4` | `open` | — | Juridinio asmuo iš Juridinių asmenų registro | — |
| `forma` | `ref` | [Forma](../../jar/formos_statusai/Forma.md) (`level=4 UUID`: `forma._id`) | `4` | `open` | — | Juridinio asmens teisinė forma iš Juridinių asmenų registro | — |
| `statusas` | `ref` | [Statusas](../../jar/formos_statusai/Statusas.md) (`level=4 UUID`: `statusas._id`) | `4` | `open` | — | Juridinio asmens teisinis statusas iš Juridinių asmenų registro | — |
| `ja_reg_data` | `date` | `D` | `4` | `open` | — | Juridinio asmens įregistravimo į Juridinių asmenų registrą data | — |
| `ne_juridinis_asmuo` | `ref` | [NeJuridinisAsmuo](../../jar/ne_juridiniai_asmenys/NeJuridinisAsmuo.md) (`level=4 UUID`: `ne_juridinis_asmuo._id`) | `4` | `open` | — | Juridinio asmens dalyvis ne juridinis asmuo iš Juridinių asmenų registro | — |
| `dal_dalys` | `number` | — | `3` | `open` | — | Juridiniame asmenyje dalyvaujančių dalyvių dalys juridiniame asmenyje procentais | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jadis/valstybes_dalyviai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/valstybes_dalyviai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jadis/valstybes_dalyviai (https://data.gov.lt/datasets/1711/)
