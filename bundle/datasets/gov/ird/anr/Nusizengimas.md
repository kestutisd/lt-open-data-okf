---
type: Table
title: "Nusizengimas — Administracinių nusižengimų detali mėnesinė statistika"
description: "Administracinių nusižengimų registro (ANR) mėnesiniai statistiniai duomenys apie Administracinių nusižengimų kodekso nustatyta tvarka užfiksuotus administracinius nusižengimus."
resource: "https://get.data.gov.lt/datasets/gov/ird/anr/Nusizengimas"
tags: [gov, ird, nusizengimas, deployed, level-3, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/anr.csv#L31"
    title: "atviriduomenys/manifest — datasets/gov/ird/anr.csv#L31"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2558/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ird/anr"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Nusizengimas — Administracinių nusižengimų detali mėnesinė statistika

Administracinių nusižengimų registro (ANR) mėnesiniai statistiniai duomenys apie Administracinių nusižengimų kodekso nustatyta tvarka užfiksuotus administracinius nusižengimus. Nusižengimų skaičiai pateikiami Administracinių nusižengimų kodekso (ANK) straipsnio bei registracijos mėnesio detalumu. Vieno nusižengimo sudėtyje gali būti keli ANK straipnsniai, todėl stulpelio „count“ negalima sumuoti. Prasminga yra skaičiuoti „count“/“total“ santykį.[^manifest]

- **Model:** `datasets/gov/ird/anr/Nusizengimas`[^manifest]
- **Dataset:** [Administracinių nusižengimų registras](../anr.md) (`datasets/gov/ird/anr`)[^manifest]
- **Manifest CSV:** [datasets/gov/ird/anr.csv#L31](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/anr.csv#L31)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/anr/Nusizengimas` (`deployed`)[^manifest]
- **Provider:** `ird` — Informatikos ir ryšių departamentas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `month` | `date` | `M` | `4` | `open` | — | Mėnuo | Ataskaitinis kalendorinis mėnuo, kurio metu buvo užregistruoti administraciniai nusižengimai |
| `count` | `integer` | `U` | `4` | `open` | — | Konkrečių nusižengimų | Kiek unikalių, konkretų ANK straipsnį savo sudėtyje turinčių nusižengimų buvo užregistruota per ataskaitinį mėnesį |
| `total` | `integer` | `U` | `4` | `open` | — | Iš viso bet kokios rūšies ANK nusižengimų tą mėnesį | Kiek bet kokios rūšies ANK nusižengimų iš viso buvo užregistruota per ataskaitinį mėnesį |
| `ank_skyrius` | `string` | — | `4` | `open` | — | ANK skyrius | Administracinių nusižengimų kodekso skyrius (priskirtas automatiškai ne iš registro galimai nepatikimas) |
| `ank_straipsnis` | `string` | — | `4` | `open` | — | ANK straipsnis | Administracinių nusižengimų kodekso straipsnis |
| `ank_skyrius_pav` | `string` | — | `2` | `open` | — | ANK skyriaus pavadinimas | Administracinių nusižengimų kodekso skyriaus pavadinimas |
| `ank_straipsnis_pav` | `string` | — | `2` | `open` | — | ANK straipsnio pavadinimas | Administracinių nusižengimų kodekso straipsnio pavadinimas |

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/anr.csv#L31 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/anr.csv#L31)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ird/anr (https://data.gov.lt/datasets/2558/)
