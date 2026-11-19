---
type: Table
title: "Sutartis — Vilniaus miesto savivaldybės patalpų nuomų sutartys"
description: "Rinkinyje skelbiami Vilniaus miesto savivaldybės nuomojamų patalpų duomenys iš „Active Vilnius“ nuomos sistemos."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/patalpos/Sutartis"
tags: [gov, vilniaus_m_sav, sutartis, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/patalpos.csv#L32"
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/patalpos.csv#L32"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3859/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/patalpos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Sutartis — Vilniaus miesto savivaldybės patalpų nuomų sutartys

**Dataset Context:** Rinkinyje skelbiami Vilniaus miesto savivaldybės nuomojamų patalpų duomenys iš „Active Vilnius“ nuomos sistemos. Platformoje kaupiama informacija apie nuomojamus aktyvaus laisvalaikio objektus: sporto ir aktų sales, kabinetus, žaidimo ir sporto aikšteles bei kita. Šias laisvalaikio zonas nuomoti gali fiziniai bei juridiniai asmenys. Rinkinyje pateikiami duomenys apie nuomojamas patalpas, nuomotojus, esamus ir buvusius nuomininkus bei išrašytas sąskaitas-faktūras už naudojimąsi paslaugomis. Nuomos įkainiai ir mokėtinos sumos sąskaitose už suteiktas paslaugas nėra skelbiami, tačiau viešinamas reitingas, kur mokėtinos sumos išrikiuojamos eilės tvarka nuo didžiausios iki mažiausios. Sutarčių ir sąskaitų duomenys skelbiami nuo 2020m. liepos mėnesio iki šių dienų. Duomenų teikėjas: Vilniaus miesto savivaldybės administracija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/vilniaus_m_sav/patalpos/Sutartis`[^manifest]
- **Dataset:** [Vilniaus miesto savivaldybės nuomojamų patalpų sutarčių duomenys](../patalpos.md) (`datasets/gov/vilniaus_m_sav/patalpos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/patalpos.csv#L32](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/patalpos.csv#L32)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/patalpos/Sutartis` (`deployed`)[^manifest]
- **Provider:** `vilniaus_m_sav` — Vilniaus miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `sutarties_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sutarties_id` | `string` | — | `4` | `open` | — | Sutarties identifikacinis numeris | — |
| `patalpos_id` | `string` | — | `4` | `open` | — | Patalpos identifikacinis numeris | — |
| `sutarties_nr` | `string` | — | `4` | `open` | — | Sutarties numeris | — |
| `aprasymas_lt` | `string` | — | `2` | `open` | — | Veiklos aprašymas | — |
| `sutarties_tipas` | `string` | — | `4` | `open` | — | Pasirašytos sutarties tipas | — |
| `statusas` | `string` | — | `4` | `open` | — | Sutarties statusas | — |
| `sudarymas` | `date` | `D` | `4` | `open` | — | Sutarties sudarymo data | — |
| `naudotoju_sk` | `integer` | `U` | `4` | `open` | — | Veikloje dalyvaujančių asmenų skaičius | — |
| `antroji_salis` | `string` | — | `4` | `open` | — | Sutarties antrosios šalies pavadinimas | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Antrosios šalies JAR kodas | — |
| `jar_kodas_validus` | `boolean` | — | `4` | `open` | — | JAR kodo validacijos požymis | — |
| `nuomos_valandu_sk` | `number` | `h` | `4` | `open` | — | Sutartyje nurodytas patalpų nuomos valandų skaičius | — |
| `nutraukimas` | `date` | `D` | `4` | `open` | — | Jei sutartis buvo nutraukta, nurodoma nutraukimo data | — |
| `kaina_reitingas` | `integer` | — | `4` | `open` | — | Sutartyje nurodyta patalpų kaina neatvaizduojama, tačiau ji išreitinguojama pagal visų rinkinyje nurodytų sutarčių sumas | — |
| `duomenu_atnaujinimas` | `date` | `D` | `4` | `open` | — | Sutarties duomenų atnaujinimo data | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `sutarties_tipas` | `"Konkursinė sutartis"` | — | — | — | — |
| `sutarties_tipas` | `"Nuomos sutartis"` | — | — | — | — |
| `sutarties_tipas` | `"Aukcionas"` | — | — | — | — |
| `sutarties_tipas` | `"Panaudos sutartis"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `aprasymas_lt` | `update(property: "aprasymas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/patalpos.csv#L32 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/patalpos.csv#L32)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/patalpos (https://data.gov.lt/datasets/3859/)
