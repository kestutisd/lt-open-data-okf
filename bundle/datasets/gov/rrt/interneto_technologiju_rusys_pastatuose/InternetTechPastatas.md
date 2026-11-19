---
type: Table
title: "InternetTechPastatas — Fiksuotojo ryšio tinklų geografinis ir technologinis Išvystymas Lietuvoje"
description: "\"Rinkinyje pateikiami Lietuvos Respublikos Ryšių reguliavimo tarnybai Viešųjų fiksuotojo ryšio tinklų teikėjų pateikti fiksuotojo ryšio tinklų geografinio ir technologinio išvystymo pastatuose duomenys."
resource: "https://get.data.gov.lt/datasets/gov/rrt/interneto_technologiju_rusys_pastatuose/InternetTechPastatas"
tags: [gov, rrt, internettechpastatas, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/interneto_technologiju_rusys_pastatuose.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/rrt/interneto_technologiju_rusys_pastatuose.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3835/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rrt/interneto_technologiju_rusys_pastatuose"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# InternetTechPastatas — Fiksuotojo ryšio tinklų geografinis ir technologinis Išvystymas Lietuvoje

"Rinkinyje pateikiami Lietuvos Respublikos Ryšių reguliavimo tarnybai Viešųjų fiksuotojo ryšio tinklų teikėjų pateikti fiksuotojo ryšio tinklų geografinio ir technologinio išvystymo pastatuose duomenys. Pastatų adresai pateikiami 1km dydžio stačiakampėmis gardelėmis. Vienoje eilutėje atvaizduojama viena interneto technologija pastate per vienerius metus. Duomenys pateikiami nuo 2023 metų ir atnaujinami kiekvienų metų balandžio mėn. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt. "[^manifest]

- **Model:** `datasets/gov/rrt/interneto_technologiju_rusys_pastatuose/InternetTechPastatas`[^manifest]
- **Dataset:** [Fiksuotojo ryšio tinklų geografinis ir technologinis Išvystymas Lietuvoje](../interneto_technologiju_rusys_pastatuose.md) (`datasets/gov/rrt/interneto_technologiju_rusys_pastatuose`)[^manifest]
- **Manifest CSV:** [datasets/gov/rrt/interneto_technologiju_rusys_pastatuose.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/interneto_technologiju_rusys_pastatuose.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rrt/interneto_technologiju_rusys_pastatuose/InternetTechPastatas` (`deployed`)[^manifest]
- **Provider:** `rrt` — Ryšių reguliavimo tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `iraso_sukurimo_data` | `date` | `D` | `4` | `open` | — | Metai, už kuriuos pateikti duomenys | — |
| `pastato_id` | `string` | — | `4` | `open` | — | Pastato identifikavimo kodas | — |
| `interneto_technologija` | `string` | — | `4` | `open` | — | Pastate esanti interneto technologija | — |
| `grid_id` | `ref` | [Grid1KmSq](../../lsd/grid/Grid1KmSq.md) (`level=4 UUID`: `grid_id._id`) | `4` | `open` | — | 1x1 km stačiakampės pastato adreso gardelės identifikatorius | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė, kurioje yra pastatas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `interneto_technologija` | `"Varinės linijos su VSDL"` | — | — | Varinės linijos su VSDL | — |
| `interneto_technologija` | `"Varinės linijos be VSDL"` | — | — | Varinės linijos be VSDL | — |
| `interneto_technologija` | `"Pasyvios šviesolaidinės linijos"` | — | — | Pasyvios šviesolaidinės linijos | — |
| `interneto_technologija` | `"Aktyvios šviesolaidinės linijos"` | — | — | Aktyvios šviesolaidinės linijos | — |
| `interneto_technologija` | `"Bendraašio kabelio linijos su DOCSIS3 ir vėlesniu"` | — | — | Bendraašio kabelio linijos su DOCSIS3 ir vėlesniu | — |
| `interneto_technologija` | `"Bendraašio kabelio linijos be DOCSIS3 ir vėlesnio"` | — | — | Bendraašio kabelio linijos be DOCSIS3 ir vėlesnio | — |
| `interneto_technologija` | `"FWA"` | — | — | FWA | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rrt/interneto_technologiju_rusys_pastatuose.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rrt/interneto_technologiju_rusys_pastatuose.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rrt/interneto_technologiju_rusys_pastatuose (https://data.gov.lt/datasets/3835/)
