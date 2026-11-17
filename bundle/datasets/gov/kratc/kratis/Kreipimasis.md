---
type: Table
title: "Kreipimasis — Klientų aptarnavimas vietinės rinkliavos administravimo klausimais pagal nekilnojamo turto objektų duomenis"
description: "UAB Klaipėdos regiono atliekų tvarkymo centro naudojamoje sistemoje „KRATIS“ kaupiami klientų aptarnavimo rinkliavos administracijos klausimais duomenys."
resource: "https://get.data.gov.lt/datasets/gov/kratc/kratis/Kreipimasis"
tags: [gov, kratc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kratc/kratis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kratc/kratis.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Kreipimasis — Klientų aptarnavimas vietinės rinkliavos administravimo klausimais pagal nekilnojamo turto objektų duomenis

UAB Klaipėdos regiono atliekų tvarkymo centro naudojamoje sistemoje „KRATIS“ kaupiami klientų aptarnavimo rinkliavos administracijos klausimais duomenys. Sistemoje duomenys kaupiami nuo 2008 m. rugpjūčio 1 d., duomenų rinkinyje – nuo 2013 m. balandžio 22 d. Rinkinyje kaupiami klientų aptarnavimo vietinės rinkliavos administracijos klausimais duomenys pagal nekilnojamojo turto (NT) objektus. Duomenų rinkinį sudaro: NT objekto identifikatorius ir paskirtis, kreipimosi data, būdas, tema, pagrįstumas su veiksmu ir išorinis raktas į 100x100 m geografinę gardelę. NT objektų identifikatoriai pseudoniminti, siekiant užtikrinti konfidencialumą, nes sistemos „KRATIS“ vartotojai gali matyti dalies objektų nepseudonimintus identifikatorius, panaudotus šiame rinkinyje. Tuo pačiu tikslu dalies įrašų paskirties stulpelio reikšmės paslėptos, kadangi adresas nurodytas kaip NT objekto paskirtis. Kadangi NT objektai gali užimti keletą gardelių, paprastumo dėlei parinktos toliausiai šiaurės vakarų kryptimi esančios gardelės, kad NT objektų ir gardelių įrašus pavyktų sujungti principu „vienas su vienu“. Vienas įrašas atitinka vieną aptarnavimo įvykį. Duomenų teikėjas – UAB Klaipėdos regiono atliekų tvarkymo centras.

- **Model:** `datasets/gov/kratc/kratis/Kreipimasis`[^manifest]
- **Dataset:** [Klientų aptarnavimas vietinės rinkliavos administravimo klausimais pagal nekilnojamo turto objektų duomenis](../kratis.md) (`datasets/gov/kratc/kratis`)
- **Manifest CSV:** [datasets/gov/kratc/kratis.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kratc/kratis.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kratc/kratis/Kreipimasis`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `turto_objekto_id` | `string` | — | `4` | `open` | — | Nekilnojamo turto objekto anonimizuotas identifikatorius | — |
| `turto_objekto_paskirtis` | `string` | — | `4` | `open` | — | Nekilnojamo turto objekto paskirtis | — |
| `kreipimosi_data` | `datetime` | `S` | `4` | `open` | — | Kreipimosi data su laiku | — |
| `kreipimosi_budas` | `string` | — | `4` | `open` | — | Kreipimosi būdas | — |
| `kreipimosi_tema` | `string` | — | `4` | `open` | — | Kreipimosi tema | — |
| `kreipimosi_pagristumas_veiksmai` | `string` | — | `4` | `open` | — | Kreipimosi pagrįstumas bei atitinkamas veiksmas, kurio imtasi | — |
| `turto_objekto_vietove_100m_gard` | `string` | — | `4` | `open` | — | Išorinis raktas į tolimiausią šiaurės-vakarų kryptimi esančią objekto geografinę gardelę | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `kreipimosi_budas` | `"Skambutis"` | — | — | Skambutis | — |
| `kreipimosi_budas` | `"Atėjimas"` | — | — | Atėjimas | — |
| `kreipimosi_budas` | `"Elektroniniu paštu"` | — | — | Elektroniniu paštu | — |
| `kreipimosi_budas` | `"Raštu"` | — | — | Raštu | — |
| `kreipimosi_budas` | `"Skolų administravimas"` | — | — | Skolų administravimas | — |
| `kreipimosi_budas` | `"Grįžtamoji korespondencija"` | — | — | Grįžtamoji korespondencija | — |
| `kreipimosi_budas` | `"Gauta iš kito darbuotojo"` | — | — | Gauta iš kito darbuotojo | — |
| `kreipimosi_budas` | `"Permoka"` | — | — | Permoka | — |
| `kreipimosi_pagristumas_veiksmai` | `"Perduotas atsakingam darbuotojui"` | — | — | Perduotas atsakingam darbuotojui | — |
| `kreipimosi_pagristumas_veiksmai` | `"Informacija arba nepagrįstas"` | — | — | Informacija arba nepagrįstas | — |
| `kreipimosi_pagristumas_veiksmai` | `"Pagrįstas"` | — | — | Pagrįstas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kratc/kratis.csv
