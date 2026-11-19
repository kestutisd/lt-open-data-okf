---
type: Table
title: "PajungimasAtjungimas — Alytaus šilumos tinklų karšto vandens ir šildymo pajungimai, atjungimai"
description: "Rinkinyje pateikiamai UAB “Alytaus šilumos tinklai” paskyrų registro duomenys."
resource: "https://get.data.gov.lt/datasets/gov/ast/paskyru_registras/PajungimasAtjungimas"
tags: [gov, ast, pajungimasatjungimas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/paskyru_registras.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/ast/paskyru_registras.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2782/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ast/paskyru_registras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PajungimasAtjungimas — Alytaus šilumos tinklų karšto vandens ir šildymo pajungimai, atjungimai

Rinkinyje pateikiamai UAB “Alytaus šilumos tinklai” paskyrų registro duomenys. Registre registruojamos paskyros, kurios pildomos šildymo ir/arba karšto vandens paslaugų pajungimui ir atjungimui objektuose, kurie tampa klientais, atsisako paslaugų, arba – dažniausias atvejis - pajungiamas/atjungiamas šildymas (šildymo sezono metu). Viena eilutė atitinka vieną kontrolieriau vizitą į atitinkamą adresą. Duomenys kaupiami nuo 2019 metų. ir iki dabar. PASITEIRAVIMUI: Valstybės duomenų valdysenos atvėrimo komanda: atverimas@stat.gov.lt[^manifest]

- **Model:** `datasets/gov/ast/paskyru_registras/PajungimasAtjungimas`[^manifest]
- **Dataset:** [Alytaus šilumos tinklų karšto vandens ir šildymo pajungimai, atjungimai](../paskyru_registras.md) (`datasets/gov/ast/paskyru_registras`)[^manifest]
- **Manifest CSV:** [datasets/gov/ast/paskyru_registras.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/paskyru_registras.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ast/paskyru_registras/PajungimasAtjungimas` (`deployed`)[^manifest]
- **Provider:** `ast` — Alytaus šilumos tinklai *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Identifikacinos numeris | — |
| `regist_nr` | `string` | — | `4` | `open` | — | Darbo atlikimo registracijos numeris | — |
| `data` | `date` | `D` | `4` | `open` | — | Darbo atlikimo data | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Platumos koordinatė WGS84 koordinačių sistemoje | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Ilgumos koordinatė WGS84 koordinačių sistemoje | — |
| `vda_x_koord_lks` | `number` | — | `4` | `open` | — | X koordinatė LKS94 koordinačių sistemoje | — |
| `vda_y_koord_lks` | `number` | — | `4` | `open` | — | Y koordinatė LKS94 koordinačių sistemoje | — |
| `koord_patik_proc` | `number` | — | `4` | `open` | — | Koordinatės patikimumas procentais | — |
| `adreso_tipas` | `string` | — | `4` | `open` | — | Koordinatės adreso tipas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė iš koordinatės | — |
| `pajungimas` | `string` | — | `4` | `open` | — | Šilumos, karšto vandens pajungimas | — |
| `atjungimas` | `string` | — | `4` | `open` | — | Šilumos, karšto vandens atpajungimas | — |
| `pastabos_lt` | `string` | — | `2` | `open` | — | parašoma žodiais, atjungtas/ pajungtas šildymas arba pajungtas šildymas ir karštas vanduo | — |
| `kontrolierius` | `string` | — | `4` | `open` | — | darbus atlikęs asmuo | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `adreso_tipas` | `"Adresas (aktualus)"` | — | — | Adresas (aktualus) | — |
| `adreso_tipas` | `"Gatvė"` | — | — | Gatvė | — |
| `adreso_tipas` | `"Gyvenvietė"` | — | — | Gyvenvietė | — |
| `pajungimas` | `"šildymas"` | — | — | šildymas | — |
| `pajungimas` | `"karštas vanduo"` | — | — | karštas vanduo | — |
| `pajungimas` | `"karštas vanduo/šildymas"` | — | — | karštas vanduo/šildymas | — |
| `atjungimas` | `"šildymas"` | — | — | šildymas | — |
| `atjungimas` | `"karštas vanduo"` | — | — | karštas vanduo | — |
| `atjungimas` | `"karštas vanduo/šildymas"` | — | — | karštas vanduo/šildymas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pastabos_lt` | `update(property: "pastabos_lt@lt", type: "text")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ast/paskyru_registras.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/paskyru_registras.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ast/paskyru_registras (https://data.gov.lt/datasets/2782/)
