---
type: Table
title: "LicregSpecialistas — Sveikatos priežiūros specialistų skaičius pamečiui"
description: "Sveikatos priežiūros specialistų licencijų skaičius pagal specialisto kvalifikaciją ir licencijos galiojimo metus pagal VASPVT LICREG duomenis."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/specialistai/LicregSpecialistas"
tags: [gov, lsd, licregspecialistas, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/specialistai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/specialistai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2896/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/specialistai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# LicregSpecialistas — Sveikatos priežiūros specialistų skaičius pamečiui

Sveikatos priežiūros specialistų licencijų skaičius pagal specialisto kvalifikaciją ir licencijos galiojimo metus pagal VASPVT LICREG duomenis. Nurodytas skaičius unikalių licencijų galiojusių ataskaitiniais metais, tačiau nebūtinai visus metus. Specialistų amžius apskaičiuotas ataskaitiniams metams.[^manifest]

- **Model:** `datasets/gov/lsd/sveikata/specialistai/LicregSpecialistas`[^manifest]
- **Dataset:** [Sveikatos priežiūros specialistai](../specialistai.md) (`datasets/gov/lsd/sveikata/specialistai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/specialistai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/specialistai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/specialistai/LicregSpecialistas` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus kodas | — |
| `kvalifikacijos_pavadinimas` | `string` | — | `4` | `open` | — | Sveikatos priežiūros specialisto kvalifikacija | — |
| `specialistu_skaicius` | `integer` | — | `4` | `open` | — | Galiojančių sveikatos priežiūros specialistų licencijų skaičius pagal kvalifikaciją ir metus | Skaičiuojama galiojančių unikalių licencijų suma, kurios galiojo bent dalį metų, nebūtinai visus metus. |
| `amziaus_vidurkis` | `integer` | — | `4` | `open` | — | Sveikatos priežiūros specialistų amžiaus vidurkis | Konfidencialumo tikslais, amžiaus vidurkis yra paslėptas, kai suskaičiuojamas tik vienas specialistas |
| `metai` | `integer` | — | `2` | `open` | — | Metai, už kuriuos skaičiuojamas galiojančių licencijų kiekis | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref:"Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/specialistai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/specialistai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/specialistai (https://data.gov.lt/datasets/2896/)
