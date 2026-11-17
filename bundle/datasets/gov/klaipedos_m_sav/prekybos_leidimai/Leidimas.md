---
type: Table
title: "Leidimas — Klaipėdos miesto savivaldybės prekybos leidimai."
description: "Informacija apie Klaipėdos miesto savivaldybės išduotus leidimus prekiauti ir teikti paslaugas viešose vietose."
resource: "https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/prekybos_leidimai/Leidimas"
tags: [gov, klaipedos_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/prekybos_leidimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/prekybos_leidimai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Leidimas — Klaipėdos miesto savivaldybės prekybos leidimai.

Informacija apie Klaipėdos miesto savivaldybės išduotus leidimus prekiauti ir teikti paslaugas viešose vietose.

- **Model:** `datasets/gov/klaipedos_m_sav/prekybos_leidimai/Leidimas`[^manifest]
- **Dataset:** [Klaipėdos miesto savivaldybės prekybos leidimai.](../prekybos_leidimai.md) (`datasets/gov/klaipedos_m_sav/prekybos_leidimai`)
- **Manifest CSV:** [datasets/gov/klaipedos_m_sav/prekybos_leidimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/prekybos_leidimai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/prekybos_leidimai/Leidimas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Prekybos leidimo išduoto tam tikram laikotarpiui identifikatorius | — |
| `prekybos_leidimo_id` | `string` | — | `4` | `open` | — | Prekybos leidimo identifikatorius | — |
| `leidimas_galioja_nuo` | `date` | `D` | `4` | `open` | — | Prekybos leidimo galiojimo pradžia | — |
| `leidimas_galioja_iki` | `date` | `D` | `4` | `open` | — | Prekybos leidimo galiojimo pabaiga | — |
| `prekybos_vietos_id` | `string` | — | `4` | `open` | — | Prekybos vietos identifikatorius | — |
| `vietos_adresas` | `string` | — | `4` | `open` | — | Prekybos vietos adresas | — |
| `vietos_numeris` | `string` | — | `4` | `open` | — | Prekybos vietos numeris | — |
| `vieta_naudojama_nuo` | `date` | `D` | `4` | `open` | — | Data nuo kada vieta pradėta naudoti kaip prekybos vieta | — |
| `vietos_koordinates` | `geometry(point, 4326)` | `m` | `4` | `open` | — | Prekybos vietos koordinatės WGS sistemoje | — |
| `vieta_atsaukta` | `boolean` | — | `4` | `open` | — | Ar prekybos vieta šiuo metu atšaukta | — |
| `isduotas_leidimas_asmeniui` | `string` | — | `4` | `open` | — | Fizinis ar juridinas asmuo kuriam išduotas leidimas | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Fizinio ar juridinio asmens kodas | — |
| `leidimo_asortimentas` | `string` | — | `4` | `open` | — | Prekių asortimentas, kuriam suteiktas leidimas prekiauti | — |
| `leidimas_pasalintas` | `date` | `D` | `4` | `open` | — | Leidimo pašalinimo data, jei leidimas pašalintas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `leidimo_asortimentas` | `update(property: "leidimo_asortimentas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/prekybos_leidimai.csv
