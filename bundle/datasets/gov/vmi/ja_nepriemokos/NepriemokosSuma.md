---
type: Table
title: "NepriemokosSuma — Juridinių asmenų nepriemokos sumos"
description: "Spinta table datasets/gov/vmi/ja_nepriemokos/NepriemokosSuma (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/ja_nepriemokos/NepriemokosSuma"
tags: [gov, vmi, nepriemokossuma, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/ja_nepriemokos.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vmi/ja_nepriemokos.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1202/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/ja_nepriemokos"
    author: "team:vda"
    last_modified: "2026-03-03T00:00:00Z"
---

# NepriemokosSuma — Juridinių asmenų nepriemokos sumos

- **Model:** `datasets/gov/vmi/ja_nepriemokos/NepriemokosSuma`[^manifest]
- **Dataset:** [Juridinių asmenų mokestinė nepriemoka](../ja_nepriemokos.md) (`datasets/gov/vmi/ja_nepriemokos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/ja_nepriemokos.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/ja_nepriemokos.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/ja_nepriemokos/NepriemokosSuma` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-03-03`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus įrašo ID | — |
| `sukurta` | `date` | `D` | `4` | `open` | — | Įrašo sukūrimo data | — |
| `atnaujinta` | `date` | `D` | `4` | `open` | — | Įrašo atnaujinimo data | — |
| `ja_kodas` | `string` | — | `2` | `open` | — | Juridinio asmens (toliau – JA) kodas | — |
| `ja_pavadinimas` | `string` | — | `2` | `open` | — | JA pavadinimas | — |
| `sav_kodas` | `ref` | [Savivaldybe](../../rc/ar/savivaldybe/Savivaldybe.md) (`level=3`: `sav_kodas.sav_kodas`) | `3` | `open` | — | Savivaldybės, kurioje registruotas JA, kodas | — |
| `nepriemoka` | `number` | — | `2` | `open` | — | JA mokestinės nepriemokos suma iš viso | — |
| `pradelsta_nepriemoka` | `number` | — | `2` | `open` | — | JA pradelsta mokestinės nepriemokos suma | — |
| `atideta_nepriemoka` | `number` | — | `2` | `open` | — | JA pagal mokestinės paskolos sutartį, susitarimą dėl pagalbos, restruktūrizavimo planą, mokumo atkūrimo planą, taikos sutartį atidėtos nepriemokos likutis. | — |
| `atideta_pradelsta` | `number` | — | `2` | `open` | — | JA pagal mokestinės paskolos sutartį, susitarimą dėl pagalbos, restruktūrizavimo planą, mokumo atkūrimo planą, taikos sutartį, pradelsta suma. | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nepriemoka` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `pradelsta_nepriemoka` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `atideta_nepriemoka` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `atideta_pradelsta` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/ja_nepriemokos.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/ja_nepriemokos.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/ja_nepriemokos (https://data.gov.lt/datasets/1202/)
