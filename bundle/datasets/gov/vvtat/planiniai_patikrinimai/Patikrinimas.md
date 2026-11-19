---
type: Table
title: "Patikrinimas — Nemaisto produktų planinių tikrinimų duomenys"
description: "Pateikiama informacija apie Valstybinės vartotojų teisių apsaugos tarnybos (VVTAT) vykdytus gamintojų, įgaliotųjų atstovų, importuotojų, platintojų ir paslaugos teikėjų planinius ne maisto gaminių ir paslaugų tikrinimus."
resource: "https://get.data.gov.lt/datasets/gov/vvtat/planiniai_patikrinimai/Patikrinimas"
tags: [gov, vvtat, patikrinimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/planiniai_patikrinimai.csv#L9"
    title: "atviriduomenys/manifest — datasets/gov/vvtat/planiniai_patikrinimai.csv#L9"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2683/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vvtat/planiniai_patikrinimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Patikrinimas — Nemaisto produktų planinių tikrinimų duomenys

Pateikiama informacija apie Valstybinės vartotojų teisių apsaugos tarnybos (VVTAT) vykdytus gamintojų, įgaliotųjų atstovų, importuotojų, platintojų ir paslaugos teikėjų planinius ne maisto gaminių ir paslaugų tikrinimus. Šių tikrinimų tikslas - padidinti vartotojų ekonominę gerovę ne maisto produktų srityje, apsaugoti gyventojų sveikatą ir ūkinės veiklos laisvę vartotojams, teikiamą ne maisto gaminių ir paslaugų srityje bei teisės aktų reikalavimų užtikrinimą šiose srityse. Patikrinimus atlieka VVTAT valstybės tarnautojai ar darbuotojai, dirbantys pagal darbo sutartis. Duomenys apima laikotarpį nuo 2004m. iki šių dienų. Ekonominės veiklos vykdytojų veiklos patikrinimai gali būti planiniai ir neplaniniai. Planiniai patikrinimai atliekami vadovaujantis VVTAT direktoriaus įsakymu patvirtintomis Tarnybos rinkos priežiūros planų rengimo ir jų vykdymo kontrolės taisyklėmis. Šių patikrinimų metu Tarnybos darbuotojai stebi ekonominės veiklos vykdytojų veiką, ją analizuoja ir vertina, konsultuoja ir teikia metodinę pagalbą, siekiant nustatyti ir pašalinti trūkumus ne maisto produktų saugos bei ženklinimo srityse. Rinkinyje nurodomos tikrinimo pradžios, pabaigos ir tikrinimo akto surašymo datos, tikrinamo objekto tipas, objekto JAR kodas ir pavadinimas, patikrinimą inicijavusios institucijos pavadinimas, tikrinime dalyvavusių darbuotojų iš įmonės pusės skaičius bei patikrintų produktų skaičius.[^manifest]

- **Model:** `datasets/gov/vvtat/planiniai_patikrinimai/Patikrinimas`[^manifest]
- **Dataset:** [Nemaisto produktų planinių tikrinimų duomenys](../planiniai_patikrinimai.md) (`datasets/gov/vvtat/planiniai_patikrinimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vvtat/planiniai_patikrinimai.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/planiniai_patikrinimai.csv#L9)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvtat/planiniai_patikrinimai/Patikrinimas` (`deployed`)[^manifest]
- **Provider:** `vvtat` — Valstybinė vartotojų teisių apsaugos tarnyba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/vvtat/planiniai_patikrinimai.csv#L9 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/planiniai_patikrinimai.csv#L9)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vvtat/planiniai_patikrinimai (https://data.gov.lt/datasets/2683/)
