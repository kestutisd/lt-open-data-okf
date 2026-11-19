---
type: Table
title: "LisPazymejimas — Licencijų informacinės sistemos duomenys apie valstybės institucijų ūkio subjektams išduotus pažymėjimus"
description: "Spinta table datasets/gov/rc/lis/lis_pazymejimai/LisPazymejimas (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/lis/lis_pazymejimai/LisPazymejimas"
tags: [gov, rc, lispazymejimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_pazymejimai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/lis/lis_pazymejimai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1707/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/lis/lis_pazymejimai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# LisPazymejimas — Licencijų informacinės sistemos duomenys apie valstybės institucijų ūkio subjektams išduotus pažymėjimus

- **Model:** `datasets/gov/rc/lis/lis_pazymejimai/LisPazymejimas`[^manifest]
- **Dataset:** [Valstybės institucijų ūkio subjektams išduoti PAŽYMĖJIMAI](../lis_pazymejimai.md) (`datasets/gov/rc/lis/lis_pazymejimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/lis/lis_pazymejimai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_pazymejimai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/lis/lis_pazymejimai/LisPazymejimas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `numeris` | `string` | — | `4` | `open` | — | Registracijos numeris | — |
| `isdavimo_data` | `date` | `D` | `4` | `open` | — | Išdavimo data | — |
| `galioja_nuo` | `date` | `D` | `4` | `open` | — | Galiojimo data nuo | — |
| `galioja_iki` | `date` | `D` | `4` | `open` | — | Galiojimo data iki | — |
| `juridinis_asmuo` | `ref` | [JuridinisAsmuo](../../jar/iregistruoti/JuridinisAsmuo.md) (`level=4 UUID`: `juridinis_asmuo._id`) | `4` | `open` | — | Licenciją išduodanti institucija | — |
| `gavejo_pavadinimas` | `string` | — | `3` | `open` | — | Gavėjo pavadinimas (fizinio asmens atveju tik įrašas „fizinis asmuo“) | — |
| `gavejo_kodas` | `string` | — | `3` | `open` | — | Gavėjo kodas (fizinio asmens atveju tik įrašas „fizinis asmuo“) | — |
| `lic_tipas` | `ref` | [LisTipas](../lis_rusys_tipai/LisTipas.md) (`level=4 UUID`: `lic_tipas._id`) | `4` | `open` | — | Tipo kodas | — |
| `lic_rusis` | `ref` | [LisRusis](../lis_rusys_tipai/LisRusis.md) (`level=4 UUID`: `lic_rusis._id`) | `4` | `open` | — | Rūšies kodas | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/lis/lis_pazymejimai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_pazymejimai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/lis/lis_pazymejimai (https://data.gov.lt/datasets/1707/)
