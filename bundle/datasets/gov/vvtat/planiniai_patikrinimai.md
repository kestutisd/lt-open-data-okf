---
type: Dataset
title: "Nemaisto produktų planinių tikrinimų duomenys"
description: "Pateikiama informacija apie Valstybinės vartotojų teisių apsaugos tarnybos (VVTAT) vykdytus gamintojų, įgaliotųjų atstovų, importuotojų, platintojų ir paslaugos teikėjų planinius ne maisto gaminių ir paslaugų tikrinimus."
resource: "https://get.data.gov.lt/datasets/gov/vvtat/planiniai_patikrinimai"
tags: [gov, vvtat, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvtat/planiniai_patikrinimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/planiniai_patikrinimai.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Nemaisto produktų planinių tikrinimų duomenys

Pateikiama informacija apie Valstybinės vartotojų teisių apsaugos tarnybos (VVTAT) vykdytus gamintojų, įgaliotųjų atstovų, importuotojų, platintojų ir paslaugos teikėjų planinius ne maisto gaminių ir paslaugų tikrinimus. Šių tikrinimų tikslas - padidinti vartotojų ekonominę gerovę ne maisto produktų srityje, apsaugoti gyventojų sveikatą ir ūkinės veiklos laisvę vartotojams, teikiamą ne maisto gaminių ir paslaugų srityje bei teisės aktų reikalavimų užtikrinimą šiose srityse. Patikrinimus atlieka VVTAT valstybės tarnautojai ar darbuotojai, dirbantys pagal darbo sutartis. Duomenys apima laikotarpį nuo 2004m. iki šių dienų. Ekonominės veiklos vykdytojų veiklos patikrinimai gali būti planiniai ir neplaniniai. Planiniai patikrinimai atliekami vadovaujantis VVTAT direktoriaus įsakymu patvirtintomis Tarnybos rinkos priežiūros planų rengimo ir jų vykdymo kontrolės taisyklėmis. Šių patikrinimų metu Tarnybos darbuotojai stebi ekonominės veiklos vykdytojų veiką, ją analizuoja ir vertina, konsultuoja ir teikia metodinę pagalbą, siekiant nustatyti ir pašalinti trūkumus ne maisto produktų saugos bei ženklinimo srityse.

Rinkinyje nurodomos tikrinimo pradžios, pabaigos ir tikrinimo akto surašymo datos, tikrinamo objekto tipas, objekto JAR kodas ir pavadinimas, patikrinimą inicijavusios institucijos pavadinimas, tikrinime dalyvavusių darbuotojų iš įmonės pusės skaičius bei patikrintų produktų skaičius.

- **Namespace:** `datasets/gov/vvtat/planiniai_patikrinimai`[^manifest]
- **Manifest CSV:** [datasets/gov/vvtat/planiniai_patikrinimai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/planiniai_patikrinimai.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvtat/planiniai_patikrinimai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Patikrinimas](planiniai_patikrinimai/Patikrinimas.md) | Nemaisto produktų planinių tikrinimų duomenys | `4` | `vda_id` | — | 13 | Pateikiama informacija apie Valstybinės vartotojų teisių apsaugos tarnybos (VVTAT) vykdytus gamintojų, įgaliotųjų atstovų, importuotojų, platintojų ir... |
| [Produktas](planiniai_patikrinimai/Produktas.md) | VVTAT tikrintų produktų duomenys | `4` | `vda_id` | — | 5 | Pateikiami Valstybinės vartotojų teisių apsaugos tarnybos (VVTAT) ne maisto produktų tikrinimų metu tikrinti produktai. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvtat/planiniai_patikrinimai.csv
