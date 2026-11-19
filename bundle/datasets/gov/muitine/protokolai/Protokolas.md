---
type: Table
title: "Protokolas — Muitinės sulaikytų prekių protokolų duomenys"
description: "Rinkinyje pateikiami Muitinės departamento prekių sulaikymo protokolų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/muitine/protokolai/Protokolas"
tags: [gov, muitine, protokolas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/protokolai.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/muitine/protokolai.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2875/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/protokolai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Protokolas — Muitinės sulaikytų prekių protokolų duomenys

Rinkinyje pateikiami Muitinės departamento prekių sulaikymo protokolų duomenys. Muitinei sulaikius prekes surašomas Prekių sulaikymo protokolas. Tai yra pirminės būsenos dokumentas, kurio duomenys vaizduojami atveriamame rinkinyje. Nustačius Lietuvos Respublikos administracinių teisės pažeidimų arba pareiškus įtarimus dėl baudžiamojo kodekso pažeidimų, atitinkamai gali būti pildomas administracinio teisės pažeidimo protokolas arba pradedamas ikiteisminis tyrimas. Kitu atveju, įsigaliojus sprendimui dėl sulaikytų prekių išdavimo arba prekių grąžinimo savininkams ar kitiems asmenims yra pildomas nutarimas prekes grąžinti. Pažymėtina, jog šie duomenys negali būti naudojami oficialiajai statistikai skaičiuoti. Rinkinyje skelbiami nuo 2008 m. iki šių dienų kaupiami duomenys, surašyti Lietuvos Respublikos kelio, geležinkelio, krovinių, pašto, oro ar mobiliųjų grupių postuose. Duomenų teikėjas – Muitinės departamentas prie Lietuvos Respublikos finansų ministerijos. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/muitine/protokolai/Protokolas`[^manifest]
- **Dataset:** [Muitinės sulaikytų prekių protokolų duomenys](../protokolai.md) (`datasets/gov/muitine/protokolai`)[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/protokolai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/protokolai.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/protokolai/Protokolas` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agenūros įrašo unikalus identifikatorius | — |
| `protokolo_id` | `string` | — | `4` | `open` | — | Protokolo identifikatorius | — |
| `protokolo_data` | `date` | `D` | `4` | `open` | — | Protokolo surašymo data | — |
| `pasienio_ruozas` | `string` | — | `4` | `open` | — | Pasienio ruožas, kuriame prekės buvo sulaikytos | — |
| `surasymo_vieta_lt` | `string` | — | `2` | `open` | — | Prekių sulaikymo protokolo surašyma vieta | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `surasymo_vieta_lt` | `update(property: "surasymo_vieta_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/protokolai.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/protokolai.csv#L8)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/protokolai (https://data.gov.lt/datasets/2875/)
