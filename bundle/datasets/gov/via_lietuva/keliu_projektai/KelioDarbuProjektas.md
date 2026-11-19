---
type: Table
title: "KelioDarbuProjektas — „Kelių projektų darbai“"
description: "\"Duomenys apie valstybinės reikšmės keliuose vykstančius kelio darbų projektus."
resource: "https://get.data.gov.lt/datasets/gov/via_lietuva/keliu_projektai/KelioDarbuProjektas"
tags: [gov, via_lietuva, keliodarbuprojektas, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/keliu_projektai.csv#L15"
    title: "atviriduomenys/manifest — datasets/gov/via_lietuva/keliu_projektai.csv#L15"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3844/"
    title: "data.gov.lt DCAT-AP — datasets/gov/via_lietuva/keliu_projektai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# KelioDarbuProjektas — „Kelių projektų darbai“

"Duomenys apie valstybinės reikšmės keliuose vykstančius kelio darbų projektus. Vienoje eilutėje pateikiami vieno kelio projekto darbų sutarties eigos duomenys: kelio atkarpos, kurioje vyksta darbai, identifikacinis numeris, objekto pavadinimas, objekte vykdomų darbų pradžios ir pabaigos data, sutarties pavadinimas, identifikacinis numeris ir sutartyje nurodytas darbų pabaigos terminas, rangovo identifikacinis numeris, savivaldybė (-s), kurioje (-se) atliekami darbai, požymiai, nusakantys ar tai yra pagrindinis objektas, žvyrkelis ar tiltas. Paskutinis stulpelis nurodo kada eilutės informacija buvo atnaujinta paskutinį kartą."[^manifest]

- **Model:** `datasets/gov/via_lietuva/keliu_projektai/KelioDarbuProjektas`[^manifest]
- **Dataset:** [Duomenys apie valstybinės reikšmės kelių projektus](../keliu_projektai.md) (`datasets/gov/via_lietuva/keliu_projektai`)[^manifest]
- **Manifest CSV:** [datasets/gov/via_lietuva/keliu_projektai.csv#L15](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/keliu_projektai.csv#L15)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/via_lietuva/keliu_projektai/KelioDarbuProjektas` (`deployed`)[^manifest]
- **Provider:** `via_lietuva` — AB „Via Lietuva“ (buv. LAKD) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA identifikatorius | Valstybės duomenų agentūros sugeneruotas unikalios eilutės identifikatorius |
| `atkarpos_id` | `string` | — | `4` | `open` | — | Kelio atkarpos identifikatorius | Kelio darbų atkarpos identifikacinis numeris |
| `obj_pav` | `string` | — | `4` | `open` | — | Objekto pavadinimas | Objekto darbų pavadinimas |
| `obj_darbai_nuo` | `date` | `D` | `4` | `open` | — | Darbų pradžia | Kelio objekto atliekamų darbų pradžios data |
| `obj_darbai_iki` | `date` | `D` | `4` | `open` | — | Darbų pabaiga | Kelio objekto atliekamų darbų pabaigos data |
| `sutartis_id` | `string` | — | `4` | `open` | — | Sutarties identifikacinis numeris | — |
| `sutarties_pav` | `string` | — | `4` | `open` | — | Sutarties pavadinimas | — |
| `sutart_darbai_nuo` | `date` | `D` | `4` | `open` | — | Sutarties darbų pradžia | Pagal sutartį atliekamų darbų pradžios data |
| `sutart_darbai_iki` | `date` | `D` | `4` | `open` | — | Sutarties darbų pabaiga | Pagal sutartį atliekamų darbų pabaigos data |
| `rangovas_id` | `string` | — | `4` | `open` | — | Rangovo identifikacinis numeris | — |
| `obj_savivaldybes` | `string` | — | `4` | `open` | — | Objekto savivaldybė | "Savivaldybės, kuriose atliekami kelio objekto darbai" |
| `obj_ivykd` | `boolean` | — | `4` | `open` | — | Objektas įvykdytas | "Požymis, nurodantis, ar darbai objekte yra įvykdyti" |
| `sutartis_ivykd` | `boolean` | — | `4` | `open` | — | Sutartis įvykdyta | "Požymis, nurodantis, ar darbai pagal sutartį yra įvykdyti" |
| `garantijos_pabaiga` | `date` | `D` | `4` | `open` | — | Garantijos pabaiga | Data iki kurios yra suteikiama darbų garantija objektui |
| `garantija_men` | `integer` | `mo` | `4` | `open` | — | Garantijos laikotarpis | "Darbų garantijos mėnesių skaičius, nurodantis kiek laiko garantija suteikiama darbams po jų užbaigimo" |
| `pagrindinis_obj` | `boolean` | — | `4` | `open` | — | Pagrindinio objekto požymis | "Požymis, nurodantis, ar tai su pagrindiniu objektu susiję darbai" |
| `zvyrkelis` | `boolean` | — | `4` | `open` | — | Žvyrkelio požymis | "Požymis, nurodantis, ar tai yra žvyrinė kelio danga" |
| `tiltas` | `boolean` | — | `4` | `open` | — | Tilto požymis | "Požymis, nurodantis, ar objektas yra tiltas" |
| `irasas_atnaujintas` | `datetime` | `U` | `4` | `open` | — | Įrašas atnaujintas | "Laiko žyma, nurodanti eilutės įrašo atnaujinimo laiką" |

[^manifest]: atviriduomenys/manifest — datasets/gov/via_lietuva/keliu_projektai.csv#L15 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/keliu_projektai.csv#L15)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/via_lietuva/keliu_projektai (https://data.gov.lt/datasets/3844/)
