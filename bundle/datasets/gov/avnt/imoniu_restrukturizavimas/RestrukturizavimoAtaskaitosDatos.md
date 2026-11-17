---
type: Table
title: "RestrukturizavimoAtaskaitosDatos — Įmonių restruktūrizavimo ataskaitų duomenys"
description: "Spinta table datasets/gov/avnt/imoniu_restrukturizavimas/RestrukturizavimoAtaskaitosDatos (16 columns)."
resource: "https://get.data.gov.lt/datasets/gov/avnt/imoniu_restrukturizavimas/RestrukturizavimoAtaskaitosDatos"
tags: [gov, avnt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/avnt/imoniu_restrukturizavimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/imoniu_restrukturizavimas.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# RestrukturizavimoAtaskaitosDatos — Įmonių restruktūrizavimo ataskaitų duomenys

- **Model:** `datasets/gov/avnt/imoniu_restrukturizavimas/RestrukturizavimoAtaskaitosDatos`[^manifest]
- **Dataset:** [Įmonių restruktūrizavimo ataskaitų duomenys](../imoniu_restrukturizavimas.md) (`datasets/gov/avnt/imoniu_restrukturizavimas`)
- **Manifest CSV:** [datasets/gov/avnt/imoniu_restrukturizavimas.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/imoniu_restrukturizavimas.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/avnt/imoniu_restrukturizavimas/RestrukturizavimoAtaskaitosDatos`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `imones_kodas` | `string` | — | `4` | `open` | — | Įmonės JAR kodas | — |
| `imones_pavadinimas` | `string` | — | `4` | `open` | — | Įmonės pavadinimas | — |
| `teritorijos_kodas` | `string` | — | `4` | `open` | — | Teritorijos kodas | — |
| `teritorijos_pavadinimas` | `string` | — | `4` | `open` | — | Teritorijos pavadinimas | — |
| `apskrities_kodas` | `string` | — | `4` | `open` | — | Apskrities kodas | — |
| `apskrities_pavadinimas` | `string` | — | `4` | `open` | — | Apskrities pavadinimas | — |
| `teisine_forma` | `string` | — | `4` | `open` | — | Rūšis (teisinė forma) | — |
| `veiklos_kodas` | `string` | — | `4` | `open` | — | Veiklos kodas | — |
| `veikla` | `string` | — | `4` | `open` | — | Veiklos pavadinimas | — |
| `veiklos_sekcija` | `string` | — | `4` | `open` | — | Veiklos sekcijos pavadinimas | — |
| `restrukturizavimo_data` | `date` | `D` | `4` | `open` | — | Restruktūrizavimo bylos iškėlimo data | — |
| `apygardos_teismas` | `string` | — | `4` | `open` | — | Apygardos teismo pavadinimas | — |
| `plano_patvirtinimas` | `date` | `D` | `4` | `open` | — | Restruktūrizavimo plano patvirtinimo data | — |
| `nutraukimo_data` | `date` | `D` | `4` | `open` | — | Restruktūrizavimo proceso nutraukimo data | — |
| `nutraukimo_priezastis` | `string` | — | `4` | `open` | — | Restruktūrizavimo proceso nutraukimo priežastis | — |
| `restrukturizavimo_pabaiga` | `date` | `D` | `4` | `open` | — | Restruktūrizavimo proceso baigimo data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `base` | `4` | `open` | — | — | — |
| `(model)` | `update(base: "/datasets/gov/avnt/imoniu_bankrotas/BankrotoAtaskaitosDatos")` | `base` | `4` | `open` | — | — | — |
| `(model)` | `update(model: "JuridinisAsmuo")` | `model` | `4` | `open` | — | — | — |
| `(model)` | `update(ref: "imones_kodas")` | `ref` | `4` | `open` | — | — | — |
| `imones_kodas` | `update(property: "ja_kodas", type: "")` | `type` | `4` | `open` | — | — | — |
| `imones_pavadinimas` | `update(property: "ja_pavadinimas", type: "")` | `type` | `4` | `open` | — | — | — |
| `teritorijos_kodas` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `teritorijos_kodas` | `update(property: "savivaldybe.sav_kodas", type: "")` | `type` | `4` | `open` | — | — | — |
| `teritorijos_pavadinimas` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `4` | `open` | — | — | — |
| `apskrities_kodas` | `update(property: "savivaldybe.apskritis.adm_kodas", type: "")` | `type` | `4` | `open` | — | — | — |
| `apskrities_pavadinimas` | `update(property: "savivaldybe.apskritis.pavadinimas", type: "")` | `type` | `4` | `open` | — | — | — |
| `teisine_forma` | `update(property: "form_pavadinimas", type: "")` | `type` | `4` | `open` | — | — | — |
| `veiklos_kodas` | `create(property: "veikla", type: "ref", ref: "/datasets/gov/lsd/cl/evrk/EkonominesVeiklosRusis")` | `type` | `4` | `open` | — | — | — |
| `veiklos_kodas` | `update(property: "veikla.kodas", type: "")` | `type` | `4` | `open` | — | — | — |
| `veikla` | `update(property: "veikla.pavadinimas_lt", type: "")` | `type` | `4` | `open` | — | — | — |
| `veiklos_sekcija` | `update(property: "veikla.bendresne_veiklos_rusis.pavadinimas_lt", type: "")` | `type` | `4` | `open` | — | — | — |
| `apygardos_teismas` | `create(property: "apygardos_teismas", type: "ref", ref: "/datasets/gov/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |
| `apygardos_teismas` | `update(property: "apygardos_teismas.ja_pavadinimas", type: "")` | `type` | `4` | `open` | — | — | — |
| `nutraukimo_priezastis` | `update(property: "nutraukimo_priezastis@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/avnt/imoniu_restrukturizavimas.csv
