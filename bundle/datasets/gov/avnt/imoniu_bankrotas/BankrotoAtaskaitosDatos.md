---
type: Table
title: "BankrotoAtaskaitosDatos — Įmonių bankroto ataskaitų duomenys"
description: "Spinta table datasets/gov/avnt/imoniu_bankrotas/BankrotoAtaskaitosDatos (23 columns)."
resource: "https://get.data.gov.lt/datasets/gov/avnt/imoniu_bankrotas/BankrotoAtaskaitosDatos"
tags: [gov, avnt, bankrotoataskaitosdatos, deployed, level-2, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/imoniu_bankrotas.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/avnt/imoniu_bankrotas.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1979/"
    title: "data.gov.lt DCAT-AP — datasets/gov/avnt/imoniu_bankrotas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# BankrotoAtaskaitosDatos — Įmonių bankroto ataskaitų duomenys

- **Model:** `datasets/gov/avnt/imoniu_bankrotas/BankrotoAtaskaitosDatos`[^manifest]
- **Dataset:** [Įmonių bankroto ataskaitų duomenys](../imoniu_bankrotas.md) (`datasets/gov/avnt/imoniu_bankrotas`)[^manifest]
- **Manifest CSV:** [datasets/gov/avnt/imoniu_bankrotas.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/imoniu_bankrotas.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/avnt/imoniu_bankrotas/BankrotoAtaskaitosDatos` (`deployed`)[^manifest]
- **Provider:** `avnt` — Audito, apskaitos, turto vertinimo ir nemokumo valdymo tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `imones_kodas` | `string` | — | `2` | `open` | — | Įmonės JAR kodas | — |
| `imones_pavadinimas` | `string` | — | `2` | `open` | — | Įmonės pavadinimas | — |
| `teritorijos_kodas` | `string` | — | `2` | `open` | — | Teritorijos kodas | — |
| `teritorijos_pavadinimas` | `string` | — | `2` | `open` | — | Teritorijos pavadinimas | — |
| `apskrities_kodas` | `string` | — | `2` | `open` | — | Apskrities kodas | — |
| `apskrities_pavadinimas` | `string` | — | `2` | `open` | — | Apskrities pavadinimas | — |
| `teisine_forma` | `string` | — | `2` | `open` | — | Rūšis (teisinė forma) | — |
| `veiklos_kodas` | `string` | — | `2` | `open` | — | Veiklos kodas | — |
| `veikla` | `string` | — | `2` | `open` | — | Veiklos pavadinimas | — |
| `veiklos_sekcija` | `string` | — | `2` | `open` | — | Veiklos sekcijos pavadinimas | — |
| `bankroto_iniciatorius` | `string` | — | `2` | `open` | — | Bankroto proceso iniciatorius | — |
| `bankroto_data` | `date` | `D` | `4` | `open` | — | Bankroto bylos iškėlimo data | — |
| `apygardos_teismas` | `string` | — | `2` | `open` | — | Apygardos teismo pavadinimas | — |
| `ne_teismo_tvarka` | `date` | `D` | `4` | `open` | — | Bankroto proceso ne teismo tvarka data | — |
| `nutraukimo_data` | `date` | `D` | `4` | `open` | — | Bankroto proceso nutraukimo data | — |
| `nutraukimo_priezastis` | `string` | — | `2` | `open` | — | Bankroto proceso nutraukimo priežastis | — |
| `likvidavimo_data` | `date` | `D` | `4` | `open` | — | Likvidavimo data | — |
| `supaprastintas_bankrotas` | `date` | `D` | `4` | `open` | — | Taikyti supaprastintą bankroto procesą data | — |
| `nutrauktas_supaprastintas` | `date` | `D` | `4` | `open` | — | Nutraukti supaprastintą bankroto procesą data | — |
| `tycinis_bankrotas` | `date` | `D` | `4` | `open` | — | Pripažinti bankrotą tyčiniu data | — |
| `tycinio_bankroto_nutraukimas` | `date` | `D` | `4` | `open` | — | Tyčinio bankroto nutraukimo data | — |
| `sprendimas_del_pabaigos` | `date` | `D` | `4` | `open` | — | Sprendimo dėl pabaigos data | — |
| `isregistravimo_data` | `date` | `D` | `4` | `open` | — | Išregistravimo data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `base` | `3` | `open` | — | — | — |
| `(model)` | `update(model: "JuridinisAsmuo")` | `model` | `3` | `open` | — | — | — |
| `(model)` | `update(ref: "imones_kodas")` | `ref` | `4` | `open` | — | — | — |
| `imones_kodas` | `update(property: "ja_kodas", type: "")` | `type` | `4` | `open` | — | — | — |
| `imones_pavadinimas` | `update(property: "ja_pavadinimas", type: "")` | `type` | `4` | `open` | — | — | — |
| `teritorijos_kodas` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `teritorijos_kodas` | `update(property: "savivaldybe.sav_kodas", type: "")` | `type` | `4` | `open` | — | — | — |
| `teritorijos_pavadinimas` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `4` | `open` | — | — | — |
| `apskrities_kodas` | `update(property: "savivaldybe.apskritis.adm_kodas", type: "")` | `type` | `4` | `open` | — | — | — |
| `apskrities_pavadinimas` | `update(property: "savivaldybe.apskritis.pavadinimas", type: "")` | `type` | `4` | `open` | — | — | — |
| `teisine_forma` | `update(property: "form_pavadinimas", type: "")` | `type` | `4` | `open` | — | — | — |
| `veiklos_kodas` | `create(property: "veikla", type: "ref", ref: "datasets/gov/lsd/cl/evrk/EkonominesVeiklosRusis")` | `type` | `4` | `open` | — | — | — |
| `veiklos_kodas` | `update(property: "veikla.kodas", type: "")` | `type` | `4` | `open` | — | — | — |
| `veikla` | `update(property: "veikla.pavadinimas_lt", type: "")` | `type` | `4` | `open` | — | — | — |
| `veiklos_sekcija` | `update(property: "veikla.bendresne_veiklos_rusis.pavadinimas_lt", type: "")` | `type` | `4` | `open` | — | — | — |
| `bankroto_iniciatorius` | `update(type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |
| `apygardos_teismas` | `create(property: "apygardos_teismas", type: "ref", ref: "datasets/gov/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |
| `apygardos_teismas` | `update(property: "apygardos_teismas.kodas", type: "")` | `type` | `4` | `open` | — | — | — |
| `nutraukimo_priezastis` | `update(property: "nutraukimo_priezastis@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/avnt/imoniu_bankrotas.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/imoniu_bankrotas.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/avnt/imoniu_bankrotas (https://data.gov.lt/datasets/1979/)
