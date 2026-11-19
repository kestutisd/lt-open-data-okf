---
type: Table
title: "TechKlausimynas — Sveikatos technologijų kompetencijų klausimyno duomenys su atsakymais"
description: "Rinkinyje pateikiami anoniminės apklausos duomenys, gauti atsakius į sveikatos technologijų kompetencijų klausimyną."
resource: "https://get.data.gov.lt/datasets/gov/sam/sveikatos_tech_klausimynas/TechKlausimynas"
tags: [gov, sam, techklausimynas, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sam/sveikatos_tech_klausimynas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/sam/sveikatos_tech_klausimynas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4152/"
    title: "data.gov.lt DCAT-AP — datasets/gov/sam/sveikatos_tech_klausimynas"
    author: "team:vda"
    last_modified: "2026-02-19T00:00:00Z"
---

# TechKlausimynas — Sveikatos technologijų kompetencijų klausimyno duomenys su atsakymais

Rinkinyje pateikiami anoniminės apklausos duomenys, gauti atsakius į sveikatos technologijų kompetencijų klausimyną. Apklausą parengė Health Tech Akseleratoriaus darbo grupė, siekianti sukurti sveikatos technologijų kompetencijų modelį ir pasiūlyti efektyviausius įgūdžių tobulinimo metodus. Klausimynas skirtas įvairių sveikatos priežiūros įstaigų darbuotojų skaitmeninių kompetencijų įsivertinimui, siekiant įvertinti pasirengimą naudotis sveikatos technologijomis. Sveikatos technologijų kompetencijų klausimynas apima klausimus apie skaitmeninį raštingumą, sveikatos informacinę sistemą ir elektroninius įrašus, duomenų valdymą, privatumą ir kibernetinį saugumą, IT standartus, duomenų analizę ir dirbtinį intelektą, nuotolinę sveikatos priežiūrą, skaitmeninį raštingumą, skaitmeninių įrankių naudojimą, inovacijas ir verslumą sveikatos technologijose, lyderystę ir pokyčių valdymą, nuolatinį mokymąsi ir profesinį tobulėjimą. Galimi atsakymai – visiškai nesutinku, nesutinku, nei sutinku, nei nesutinku, sutinku arba visiškai sutinku. Duomenų šaltinis – Sveikatos apsaugos ministerija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt[^manifest]

- **Model:** `datasets/gov/sam/sveikatos_tech_klausimynas/TechKlausimynas`[^manifest]
- **Dataset:** [Sveikatos technologijų kompetencijų klausimyno duomenų rinkinys](../sveikatos_tech_klausimynas.md) (`datasets/gov/sam/sveikatos_tech_klausimynas`)[^manifest]
- **Manifest CSV:** [datasets/gov/sam/sveikatos_tech_klausimynas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sam/sveikatos_tech_klausimynas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sam/sveikatos_tech_klausimynas/TechKlausimynas` (`deployed`)[^manifest]
- **Provider:** `sam` — Lietuvos Respublikos sveikatos apsaugos ministerija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-02-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus įrašo identifikatorius | — |
| `vda_respondento_id` | `string` | — | `4` | `open` | — | Unikalus respondento identifikatorius | — |
| `data` | `datetime` | `D` | `4` | `open` | — | Apklausos atsakymo pateikimo data. | — |
| `sveikatos_istaiga` | `string` | — | `4` | `open` | — | Respondento nurodyta sveikatos priežiūros įstaiga arba jos tipas. | — |
| `pareigos` | `string` | — | `4` | `open` | — | Respondento pareigos sveikatos priežiūros įstaigoje. | — |
| `klausimo_sritis` | `string` | — | `4` | `open` | — | Teminė klausimo sritis, kuriai priskiriamas klausimas. | — |
| `klausimas` | `string` | — | `4` | `open` | — | Pilnas apklausos klausimo tekstas. | — |
| `atsakymas` | `string` | — | `4` | `open` | — | Respondento pateiktas atsakymas į konkretų klausimą. | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sam/sveikatos_tech_klausimynas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sam/sveikatos_tech_klausimynas.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/sam/sveikatos_tech_klausimynas (https://data.gov.lt/datasets/4152/)
