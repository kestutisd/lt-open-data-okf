---
type: Table
title: "Srove — Klaipėdos valstybinio jūrų uosto vandens srovių matavimo duomenys"
description: "AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami geografiniai jūrų uosto duomenys."
resource: "https://get.data.gov.lt/datasets/gov/kvjud/sroviu_matavimai/Srove"
tags: [gov, kvjud, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kvjud/sroviu_matavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/sroviu_matavimai.csv#L9"
    last_modified: "2026-11-11T14:39:20Z"
---

# Srove — Klaipėdos valstybinio jūrų uosto vandens srovių matavimo duomenys

AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami geografiniai jūrų uosto duomenys. Rinkinyje pateikiami nuo 2016 m. gegužės mėnesio kaupiami vertikaliu arba horizontaliu davikliu atliekamų vandens srovių matavimų duomenys. Šių matavimų metu nustatomas srovių greitis ir kryptis. Vienas įrašas atitinka vienu daviklių atliktą matavimą.

Duomenų teikėjas – AB Klaipėdos valstybinio jūrų uosto direkcija.

- **Model:** `datasets/gov/kvjud/sroviu_matavimai/Srove`[^manifest]
- **Dataset:** [Klaipėdos valstybinio jūrų uosto vandens srovių matavimo duomenys](../sroviu_matavimai.md) (`datasets/gov/kvjud/sroviu_matavimai`)
- **Manifest CSV:** [datasets/gov/kvjud/sroviu_matavimai.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/sroviu_matavimai.csv#L9)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kvjud/sroviu_matavimai/Srove`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `daviklio_id` | `string` | — | `4` | `open` | — | Daviklio identifikacinis numeris | — |
| `matavimo_paketo_nr` | `string` | — | `4` | `open` | — | Paketo numeris | — |
| `matavimo_laikas` | `datetime` | `S` | `4` | `open` | — | Laikas | — |
| `dav_gylis` | `number` | `cm` | `4` | `open` | — | Daviklio gylis | — |
| `dav_kryptis` | `number` | — | `4` | `open` | — | Daviklio kryptis | Daviklių magnetinio kompaso rodmenys, naudojama kalibravimui, matuojama laipsniais, tik skaičių formatas be kablelio. |
| `sroves_kampas` | `number` | — | `4` | `open` | — | Srovės kampas | Išvestinis dydis iš duomenų bazės duomenų |
| `sroves_greitis` | `number` | — | `4` | `open` | — | Srovės greitis | Išvestinis dydis iš duomenų bazės duomenų |

[^manifest]: atviriduomenys/manifest — datasets/gov/kvjud/sroviu_matavimai.csv
