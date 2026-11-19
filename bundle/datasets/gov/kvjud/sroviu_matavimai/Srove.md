---
type: Table
title: "Srove — Klaipėdos valstybinio jūrų uosto vandens srovių matavimo duomenys"
description: "AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami geografiniai jūrų uosto duomenys."
resource: "https://get.data.gov.lt/datasets/gov/kvjud/sroviu_matavimai/Srove"
tags: [gov, kvjud, srove, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/sroviu_matavimai.csv#L9"
    title: "atviriduomenys/manifest — datasets/gov/kvjud/sroviu_matavimai.csv#L9"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2860/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kvjud/sroviu_matavimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Srove — Klaipėdos valstybinio jūrų uosto vandens srovių matavimo duomenys

AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami geografiniai jūrų uosto duomenys. Rinkinyje pateikiami nuo 2016 m. gegužės mėnesio kaupiami vertikaliu arba horizontaliu davikliu atliekamų vandens srovių matavimų duomenys. Šių matavimų metu nustatomas srovių greitis ir kryptis. Vienas įrašas atitinka vienu daviklių atliktą matavimą. Duomenų teikėjas – AB Klaipėdos valstybinio jūrų uosto direkcija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/kvjud/sroviu_matavimai/Srove`[^manifest]
- **Dataset:** [Klaipėdos valstybinio jūrų uosto vandens srovių matavimo duomenys](../sroviu_matavimai.md) (`datasets/gov/kvjud/sroviu_matavimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/kvjud/sroviu_matavimai.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/sroviu_matavimai.csv#L9)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kvjud/sroviu_matavimai/Srove` (`deployed`)[^manifest]
- **Provider:** `kvjud` — AB Klaipėdos valstybinio jūrų uosto direkcija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/kvjud/sroviu_matavimai.csv#L9 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/sroviu_matavimai.csv#L9)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kvjud/sroviu_matavimai (https://data.gov.lt/datasets/2860/)
