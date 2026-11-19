---
type: Table
title: "Operacija — Operacijos"
description: "Lentelė „Operacijos“. Lentelę sudaro: sudarančios procedūros, paciento asmens kodas, operacijos rūšis, diagnozės, pagal kurią operuojama, TLK kodas ir pavadinimas, naudojamas endoprotezų modelis, operacijos planuota pradžios data ir realios pradžios bei pabaigos datos."
resource: "https://get.data.gov.lt/datasets/gov/rvul/hops/Operacija"
tags: [gov, rvul, operacija, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/rvul/hops.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3865/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rvul/hops"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Operacija — Operacijos

Lentelė „Operacijos“. Lentelę sudaro: sudarančios procedūros, paciento asmens kodas, operacijos rūšis, diagnozės, pagal kurią operuojama, TLK kodas ir pavadinimas, naudojamas endoprotezų modelis, operacijos planuota pradžios data ir realios pradžios bei pabaigos datos. Vienas lentelės įrašas atitinka vieną operacijos ir ją sudarančios procedūros kombinaciją. Tušti operacijos realios pradžios ir pabaigos datos laukai reiškia paskirtą, bet neįvykdytą operaciją. Nors dalyje įrašų dėl vidinių informacinės sistemos ypatumų yra užpildyta tik viena data iš realios pradžios arba pabaigos datų, tai irgi reiškia, jog operacija buvo paskirta, tačiau neįvykdyta.[^manifest]

- **Model:** `datasets/gov/rvul/hops/Operacija`[^manifest]
- **Dataset:** [Pacientams atliktų operacijų duomenys](../hops.md) (`datasets/gov/rvul/hops`)[^manifest]
- **Manifest CSV:** [datasets/gov/rvul/hops.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rvul/hops/Operacija` (`deployed`)[^manifest]
- **Provider:** `rvul` — VšĮ Respublikinė Vilniaus universitetinė ligoninė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `id` | `string` | — | `4` | `open` | — | Operacijos identifikatorius | — |
| `proceduros_id` | `string` | — | `4` | `open` | — | Išorinis raktas į procedūrą | — |
| `proceduros_pavadinimas` | `string` | — | `4` | `open` | — | Procedūros pavadinimas | — |
| `paciento_asm_k` | `string` | — | `4` | `open` | — | Operacijos paciento asmens kodas | — |
| `operacijos_rusis` | `string` | — | `4` | `open` | — | Operacijos rūšis | — |
| `diagnozes_tlk_kodas` | `string` | — | `4` | `open` | — | Diagnozės, pagal kurią gydoma, TLK | — |
| `diagnozes_pavadinimas` | `string` | — | `4` | `open` | — | Diagnozės, pagal kurią gydoma, pavadinimas | — |
| `endoprotezu_modelis` | `string` | — | `4` | `open` | — | Operacijoje naudojamas endoprotezų modelis | — |
| `operacijos_planuota_pradzios_data` | `datetime` | `M` | `4` | `open` | — | Planuoti operacijos data ir laikas | — |
| `operacijos_pradzios_data` | `datetime` | `S` | `4` | `open` | — | Realūs operacijos pradžios data ir laikas | — |
| `operacijos_pabaigos_data` | `datetime` | `S` | `4` | `open` | — | Realūs operacijos pabaigos data ir laikas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `operacijos_rusis` | `"Atvira"` | — | — | Atvira | — |
| `operacijos_rusis` | `"Artroskopinė"` | — | — | Artroskopinė | — |
| `operacijos_rusis` | `"Laporoskopinė"` | — | — | Laporoskopinė | — |
| `operacijos_rusis` | `"Endoskopinė"` | — | — | Endoskopinė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rvul/hops.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rvul/hops (https://data.gov.lt/datasets/3865/)
