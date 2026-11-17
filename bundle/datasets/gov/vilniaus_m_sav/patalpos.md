---
type: Dataset
title: "Vilniaus miesto savivaldybės nuomojamų patalpų sutarčių duomenys"
description: "Rinkinyje skelbiami Vilniaus miesto savivaldybės nuomojamų patalpų duomenys iš „Active Vilnius“ nuomos sistemos."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/patalpos"
tags: [gov, vilniaus_m_sav, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/patalpos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/patalpos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Vilniaus miesto savivaldybės nuomojamų patalpų sutarčių duomenys

Rinkinyje skelbiami Vilniaus miesto savivaldybės nuomojamų patalpų duomenys iš „Active Vilnius“ nuomos sistemos. Platformoje kaupiama informacija apie nuomojamus aktyvaus laisvalaikio objektus: sporto ir aktų sales, kabinetus, žaidimo ir sporto aikšteles bei kita. Šias laisvalaikio zonas nuomoti gali fiziniai bei juridiniai asmenys. Rinkinyje pateikiami duomenys apie nuomojamas patalpas, nuomotojus, esamus ir buvusius nuomininkus bei išrašytas sąskaitas-faktūras už naudojimąsi paslaugomis. Nuomos įkainiai ir mokėtinos sumos sąskaitose už suteiktas paslaugas nėra skelbiami, tačiau viešinamas reitingas, kur mokėtinos sumos išrikiuojamos eilės tvarka nuo didžiausios iki mažiausios. Sutarčių ir sąskaitų duomenys skelbiami nuo 2020m. liepos mėnesio iki šių dienų.

Duomenų teikėjas: Vilniaus miesto savivaldybės administracija.

- **Namespace:** `datasets/gov/vilniaus_m_sav/patalpos`[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/patalpos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/patalpos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/patalpos`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Patalpa](patalpos/Patalpa.md) | Vilniaus miesto savivaldybės nuomojamos patalpos | `4` | `patalpos_id` | — | 17 | — |
| [Sutartis](patalpos/Sutartis.md) | Vilniaus miesto savivaldybės patalpų nuomų sutartys | `4` | `sutarties_id` | — | 15 | — |
| [Saskaita](patalpos/Saskaita.md) | Vilniaus miesto savivaldybės sąskaitos patalpų nuomininkams už suteiktas paslaugas | `4` | `saskaitos_id` | — | 10 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/patalpos.csv
