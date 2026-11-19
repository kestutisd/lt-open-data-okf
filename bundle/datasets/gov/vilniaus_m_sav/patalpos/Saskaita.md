---
type: Table
title: "Saskaita — Vilniaus miesto savivaldybės sąskaitos patalpų nuomininkams už suteiktas paslaugas"
description: "Rinkinyje skelbiami Vilniaus miesto savivaldybės nuomojamų patalpų duomenys iš „Active Vilnius“ nuomos sistemos."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/patalpos/Saskaita"
tags: [gov, vilniaus_m_sav, saskaita, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/patalpos.csv#L54"
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/patalpos.csv#L54"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3859/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/patalpos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Saskaita — Vilniaus miesto savivaldybės sąskaitos patalpų nuomininkams už suteiktas paslaugas

**Dataset Context:** Rinkinyje skelbiami Vilniaus miesto savivaldybės nuomojamų patalpų duomenys iš „Active Vilnius“ nuomos sistemos. Platformoje kaupiama informacija apie nuomojamus aktyvaus laisvalaikio objektus: sporto ir aktų sales, kabinetus, žaidimo ir sporto aikšteles bei kita. Šias laisvalaikio zonas nuomoti gali fiziniai bei juridiniai asmenys. Rinkinyje pateikiami duomenys apie nuomojamas patalpas, nuomotojus, esamus ir buvusius nuomininkus bei išrašytas sąskaitas-faktūras už naudojimąsi paslaugomis. Nuomos įkainiai ir mokėtinos sumos sąskaitose už suteiktas paslaugas nėra skelbiami, tačiau viešinamas reitingas, kur mokėtinos sumos išrikiuojamos eilės tvarka nuo didžiausios iki mažiausios. Sutarčių ir sąskaitų duomenys skelbiami nuo 2020m. liepos mėnesio iki šių dienų. Duomenų teikėjas: Vilniaus miesto savivaldybės administracija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/vilniaus_m_sav/patalpos/Saskaita`[^manifest]
- **Dataset:** [Vilniaus miesto savivaldybės nuomojamų patalpų sutarčių duomenys](../patalpos.md) (`datasets/gov/vilniaus_m_sav/patalpos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/patalpos.csv#L54](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/patalpos.csv#L54)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/patalpos/Saskaita` (`deployed`)[^manifest]
- **Provider:** `vilniaus_m_sav` — Vilniaus miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `saskaitos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `saskaitos_id` | `string` | — | `4` | `open` | — | Sąskaitos identifikacinis numeris | — |
| `sutarties_id` | `string` | — | `4` | `open` | — | Sutarties identifikacinis numeris | — |
| `saskaitos_nr` | `string` | — | `4` | `open` | — | Sąskaitos numeris | — |
| `periodo_pradzia` | `date` | `D` | `4` | `open` | — | Periodo, už kurį išrašyta sąskaita faktūra, pradžia | — |
| `periodo_pabaiga` | `date` | `D` | `4` | `open` | — | Periodo, už kurį išrašyta sąskaita faktūra, pabaiga | — |
| `israsymo_data` | `date` | `D` | `4` | `open` | — | Sąskaitos apmokėjimo data | — |
| `apmokejimas` | `date` | `D` | `4` | `open` | — | Sąskaitos faktūros išrašymo data | — |
| `nuomos_val` | `number` | `h` | `4` | `open` | — | Nuomos valandų skaičius | — |
| `suma_reitingas` | `integer` | — | `4` | `open` | — | Sąskaitoje faktūroje nurodyta bendra suma apmokėjimui, kurios dydis išreitinguotas pagal visas kitas sąskaitas, išrašytas per tą patį laikotarpį | — |
| `duomenu_atnaujinimas` | `date` | `D` | `4` | `open` | — | Sąskaitos duomenų atnaujinimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/patalpos.csv#L54 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/patalpos.csv#L54)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/patalpos (https://data.gov.lt/datasets/3859/)
