---
type: Table
title: "Sarasas — Bibliotekų ir padalinių sąrašas"
description: "Spinta table datasets/gov/lnb/bibliotekos/Sarasas (22 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lnb/bibliotekos/Sarasas"
tags: [gov, lnb, sarasas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/bibliotekos.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/lnb/bibliotekos.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2626/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lnb/bibliotekos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Sarasas — Bibliotekų ir padalinių sąrašas

- **Model:** `datasets/gov/lnb/bibliotekos/Sarasas`[^manifest]
- **Dataset:** [Bibliotekų ir padalinių sąrašas](../bibliotekos.md) (`datasets/gov/lnb/bibliotekos`)[^manifest]
- **Manifest CSV:** [datasets/gov/lnb/bibliotekos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/bibliotekos.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lnb/bibliotekos/Sarasas` (`deployed`)[^manifest]
- **Provider:** `lnb` — Lietuvos nacionalinė Martyno Mažvydo biblioteka *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by-nc/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `bibliotekos_id` | `string` | — | `4` | `open` | — | Bibliotekos identifikatorius | — |
| `padalinio_id` | `string` | — | `4` | `open` | — | Bibliotekos padalinio (fondo / filialo ar skyriaus) identifikatorius | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Bibliotekos pavadinimas | — |
| `biblioteka_aktyvi` | `string` | — | `4` | `open` | — | Bibliotekos aktyvumo statusas | — |
| `padalin_pavadinimas` | `string` | — | `4` | `open` | — | Bibliotekos padalinio pavadinimas | — |
| `padalin_aktyvus` | `boolean` | — | `4` | `open` | — | Bibliotekos padalinio aktyvumo statusas | — |
| `soc_tinklai` | `string` | — | `4` | `open` | — | Bibliotekos socialinių tinklų nuoroda | — |
| `url` | `string` | — | `4` | `open` | — | Bibliotekos internetinė svetainė | — |
| `ar_edukacine` | `boolean` | — | `4` | `open` | — | Edukacinės institucijos požymis | — |
| `ar_biblioteka` | `boolean` | — | `4` | `open` | — | Bibliotekos požymis | — |
| `ar_leidejas` | `boolean` | — | `4` | `open` | — | Leidėjo požymis | — |
| `ar_skaitytojas` | `boolean` | — | `4` | `open` | — | Skaitytojo statuso požymis | — |
| `ar_duom_teikejas` | `boolean` | — | `4` | `open` | — | Duomenų teikėjo požymis | — |
| `ar_tba` | `boolean` | — | `4` | `open` | — | Tarpbibliotekinio abonemento požymis | — |
| `uzsak_atsiemimo_d` | `integer` | — | `4` | `open` | — | Dienų skaičius, per kurias galima atsiimti užsakymą | — |
| `padalin_priima_tba` | `boolean` | — | `4` | `open` | — | Požymis, ar padalinys priima užsakymus tarpbibliotekiniu abonementu | — |
| `padalin_siuncia_tba` | `boolean` | — | `4` | `open` | — | Požymis, ar padalinys siunčia užsakymus tarpbibliotekiniu abonementu | — |
| `sukurta` | `date` | `D` | `4` | `open` | — | Informacijos apie įstaigą pateikimo data | — |
| `atnaujinta` | `date` | `D` | `4` | `open` | — | Informacijos apie įstaigą atnaujinimo data | — |
| `adresas` | `string` | — | `4` | `open` | — | Padalinio adresas | — |
| `koord` | `geometry(3346)` | `m` | `4` | `open` | — | Padalinio koordinatės | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `biblioteka_aktyvi` | `"ACTIVE"` | — | — | Aktyvi | — |
| `biblioteka_aktyvi` | `"CLOSED"` | — | — | Neaktyvi | — |
| `biblioteka_aktyvi` | `"SUSPENDED"` | — | — | Suspenduota | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lnb/bibliotekos.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/bibliotekos.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lnb/bibliotekos (https://data.gov.lt/datasets/2626/)
