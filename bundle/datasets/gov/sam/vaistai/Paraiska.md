---
type: Table
title: "Paraiska — Paraiškų dėl vaistinių preparatų ar medicinos pagalbos priemonių įrašymo į kompensavimo sąrašus svarstymo duomenys"
description: "Lietuvos Respublikos sveikatos apsaugos ministerija (LR SAM) renka ir skelbia duomenis apie svarstomas paraiškas dėl vaistinių preparatų ir medicinos pagalbos priemonių (MPP) įtraukimo į kompensuojamųjų sąrašus."
resource: "https://get.data.gov.lt/datasets/gov/sam/vaistai/Paraiska"
tags: [gov, sam, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/sam/vaistai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sam/vaistai.csv#L9"
    last_modified: "2026-11-11T14:39:20Z"
---

# Paraiska — Paraiškų dėl vaistinių preparatų ar medicinos pagalbos priemonių įrašymo į kompensavimo sąrašus svarstymo duomenys

Lietuvos Respublikos sveikatos apsaugos ministerija (LR SAM) renka ir skelbia duomenis apie svarstomas paraiškas dėl vaistinių preparatų ir medicinos pagalbos priemonių (MPP) įtraukimo į kompensuojamųjų sąrašus. Šie duomenys suteikia galimybę stebėti sveikatos technologijų vertinimo (STV) procesą ir priimamus sprendimus dėl kompensavimo.

STV paraiškų duomenis teikia Valstybinė vaistų kontrolės tarnyba (VVKT). MPP duomenys gaunami iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos (VASPVT) duomenų bazių.

Šio rinkinio duomenis galima praturtinti jungiant su VVKT atvertu rinkiniu (duomenys jungiami per stulpelį „paraiskos_numeris“): https://data.gov.lt/datasets/2897/.

- **Model:** `datasets/gov/sam/vaistai/Paraiska`[^manifest]
- **Dataset:** [Paraiškų dėl vaistinių preparatų ar medicinos pagalbos priemonių įrašymo į kompensavimo sąrašus svarstymo duomenys](../vaistai.md) (`datasets/gov/sam/vaistai`)
- **Manifest CSV:** [datasets/gov/sam/vaistai.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sam/vaistai.csv#L9)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sam/vaistai/Paraiska`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `paraiskos_numeris` | `string` | — | `4` | `open` | — | Sveikatos technologijų vertinimo (STV) paraiškų įrašyti vaistinį preparatą į kompensavimo sąrašus numeris | — |
| `bendrinis_preparato_pav` | `string` | — | `4` | `open` | — | Bendrinis vaistinio preparato ar medicinos pagalbos priemonės (MPP) pavadinimas | — |
| `prekinis_preparato_pav` | `string` | — | `4` | `open` | — | Prekinis vaistinio preparato ar medicinos pagalbos priemonės (MPP) pavadinimas | — |
| `pareiskejas` | `string` | — | `4` | `open` | — | Pareiškėjo pavadinimas | — |
| `paraiskos_gavimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos gavimo data | — |
| `tlk_kodas` | `string` | — | `4` | `open` | — | Ligų kodai pagal TLK-AM-10 (Tarptautinė statistinė ligų ir sveikatos sutrikimų klasifikacija, dešimtasis pataisytas ir papildytas leidimas, Australijos modifikacija) | — |
| `rekomendacijos_data` | `date` | `D` | `4` | `open` | — | Rekomendacijos gavimo data iš Valstybinės vaistų kontrolės tarnybos (VVKT) ar Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos (VASPVT) | — |
| `posedzio_data` | `date` | `D` | `4` | `open` | — | Komisijos posėdžio data(-os) dėl vaistinių preparatų ar medicinos pagalbos priemonių (MPP) įrašymo į kompensavimo sąrašus | — |
| `spredimo_data` | `date` | `D` | `4` | `open` | — | Komisijos sprendimo priėmimo data dėl vaistinių preparatų ar medicinos pagalbos priemonių (MPP) įrašymo į kompensavimo sąrašus | — |
| `sprendimas` | `string` | — | `4` | `open` | — | Priimtas komisijos sprendimas | — |
| `isakymo_data` | `date` | `D` | `4` | `open` | — | Įsakymo data | — |
| `isakymo_numeris` | `string` | — | `4` | `open` | — | Įsakymo numeris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sam/vaistai.csv
