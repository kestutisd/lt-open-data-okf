---
type: Table
title: "IsregistruotasParamosGavejas — Juridinių asmenų registre įregistruoti paramos gavėjai"
description: "Duomenys apie Lietuvos Respublikos juridinių asmenų registre įregistruotus juridinius asmenis, turinčius išregistruotą žymą „PARAMOS GAVĖJAI“ (kodas, pavadinimas, žymos įregistravimo data)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/isregistruoti_paramos_gavejai/IsregistruotasParamosGavejas"
tags: [gov, rc, isregistruotasparamosgavejas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/isregistruoti_paramos_gavejai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/isregistruoti_paramos_gavejai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1569/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/isregistruoti_paramos_gavejai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# IsregistruotasParamosGavejas — Juridinių asmenų registre įregistruoti paramos gavėjai

**Dataset Context:** Duomenys apie Lietuvos Respublikos juridinių asmenų registre įregistruotus juridinius asmenis, turinčius išregistruotą žymą „PARAMOS GAVĖJAI“ (kodas, pavadinimas, žymos įregistravimo data). Individualių įmonių, komanditinių ūkinių bendrijų, tikrųjų ūkinių bendrijų pavadinimai nuasmeninti.[^manifest]

- **Model:** `datasets/gov/rc/jar/isregistruoti_paramos_gavejai/IsregistruotasParamosGavejas`[^manifest]
- **Dataset:** [Juridinių asmenų registre įregistruoti paramos gavėjai (pagal išregistruotą statusą „PARAMOS...](../isregistruoti_paramos_gavejai.md) (`datasets/gov/rc/jar/isregistruoti_paramos_gavejai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/isregistruoti_paramos_gavejai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/isregistruoti_paramos_gavejai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/isregistruoti_paramos_gavejai/IsregistruotasParamosGavejas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `juridinis_asmuo`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [JuridinisAsmuo](../iregistruoti/JuridinisAsmuo.md) (`level=4 UUID`: `juridinis_asmuo._id`) | `4` | `open` | — | Juridinio asmens pavadinimas Juridinių asmenų registre | — |
| `paramos_gav_nuo` | `date` | `D` | `4` | `open` | — | Paramos gavėjo statuso įregistravimo data | — |
| `paramos_gav_iki` | `date` | `D` | `4` | `open` | — | Paramos gavėjo statuso išregistravimo data | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/isregistruoti_paramos_gavejai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/isregistruoti_paramos_gavejai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/isregistruoti_paramos_gavejai (https://data.gov.lt/datasets/1569/)
