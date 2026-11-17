---
type: Table
title: "Patikrinimas — Nemaisto produktų planinių tikrinimų duomenys"
description: "Pateikiama informacija apie Valstybinės vartotojų teisių apsaugos tarnybos (VVTAT) vykdytus gamintojų, įgaliotųjų atstovų, importuotojų, platintojų ir paslaugos teikėjų planinius ne maisto gaminių ir paslaugų tikrinimus."
resource: "https://get.data.gov.lt/datasets/gov/vvtat/planiniai_patikrinimai/Patikrinimas"
tags: [gov, vvtat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvtat/planiniai_patikrinimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/planiniai_patikrinimai.csv#L9"
    last_modified: "2026-11-11T14:39:20Z"
---

# Patikrinimas — Nemaisto produktų planinių tikrinimų duomenys

Pateikiama informacija apie Valstybinės vartotojų teisių apsaugos tarnybos (VVTAT) vykdytus gamintojų, įgaliotųjų atstovų, importuotojų, platintojų ir paslaugos teikėjų planinius ne maisto gaminių ir paslaugų tikrinimus. Šių tikrinimų tikslas - padidinti vartotojų ekonominę gerovę ne maisto produktų srityje, apsaugoti gyventojų sveikatą ir ūkinės veiklos laisvę vartotojams, teikiamą ne maisto gaminių ir paslaugų srityje bei teisės aktų reikalavimų užtikrinimą šiose srityse. Patikrinimus atlieka VVTAT valstybės tarnautojai ar darbuotojai, dirbantys pagal darbo sutartis. Duomenys apima laikotarpį nuo 2004m. iki šių dienų. Ekonominės veiklos vykdytojų veiklos patikrinimai gali būti planiniai ir neplaniniai. Planiniai patikrinimai atliekami vadovaujantis VVTAT direktoriaus įsakymu patvirtintomis Tarnybos rinkos priežiūros planų rengimo ir jų vykdymo kontrolės taisyklėmis. Šių patikrinimų metu Tarnybos darbuotojai stebi ekonominės veiklos vykdytojų veiką, ją analizuoja ir vertina, konsultuoja ir teikia metodinę pagalbą, siekiant nustatyti ir pašalinti trūkumus ne maisto produktų saugos bei ženklinimo srityse.

Rinkinyje nurodomos tikrinimo pradžios, pabaigos ir tikrinimo akto surašymo datos, tikrinamo objekto tipas, objekto JAR kodas ir pavadinimas, patikrinimą inicijavusios institucijos pavadinimas, tikrinime dalyvavusių darbuotojų iš įmonės pusės skaičius bei patikrintų produktų skaičius.

- **Model:** `datasets/gov/vvtat/planiniai_patikrinimai/Patikrinimas`[^manifest]
- **Dataset:** [Nemaisto produktų planinių tikrinimų duomenys](../planiniai_patikrinimai.md) (`datasets/gov/vvtat/planiniai_patikrinimai`)
- **Manifest CSV:** [datasets/gov/vvtat/planiniai_patikrinimai.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/planiniai_patikrinimai.csv#L9)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvtat/planiniai_patikrinimai/Patikrinimas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo unikalus identifikatorius | — |
| `patikrinimo_id` | `string` | — | `4` | `open` | — | Patikrinimo identifikacinis numeris | — |
| `objekto_tikrinimo_id` | `string` | — | `4` | `open` | — | Objekto tikrinimo identifikacinis numeris | — |
| `patikrinimo_pradzia` | `date` | `D` | `4` | `open` | — | Patikrinimo pradžios laikas | — |
| `patikrinimo_pabaiga` | `date` | `D` | `4` | `open` | — | Patikrinimo pabaigos laikas | — |
| `akto_data` | `date` | `D` | `4` | `open` | — | Patikrinimo akto data | — |
| `objekto_tipas` | `string` | — | `4` | `open` | — | Tikrinamo objekto tipas | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | Įmonės juridinio asmens kodas | — |
| `imone_lt` | `string` | — | `1` | `open` | — | Tikrinamos įmonės pavadinimas | — |
| `pat_inic_institucija` | `string` | — | `4` | `open` | — | Institucijos pavadinimas | — |
| `vyk_inspektorius` | `string` | — | `2` | `open` | — | Patikrinimą vykdęs inspektorius (pseudonimizuota informacija) | — |
| `patikrinta_produktu` | `integer` | `U` | `4` | `open` | — | Tikrinimo metu patikrintų produktų skaičius | — |
| `dalyvavo_darbuotoju` | `integer` | `U` | `4` | `open` | — | Tikrinime dalyvavusių įmonės darbuotojų skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `imone_lt` | `update(property: "imone_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `vyk_inspektorius` | `"update(property: ""vyk_inspektorius[]"", type: ""array"", source: ""Vyk_inspektorius"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvtat/planiniai_patikrinimai.csv
