---
type: Table
title: "Uzsakymas — Atliekų tvarkymo užsakymų duomenys"
description: "Atliekų surinkimo, monitoringo ir logistikos informacinė sistemos (ASMLIS, MOKESTA) naudojamos atliekų tvarkymo organizavimui ir atsiskaitymui už komunalinių atliekų surinkimo ir išvežimo paslaugas."
resource: "https://get.data.gov.lt/datasets/gov/asmlis/uzsakymai/Uzsakymas"
tags: [gov, asmlis, uzsakymas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/uzsakymai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/asmlis/uzsakymai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2763/"
    title: "data.gov.lt DCAT-AP — datasets/gov/asmlis/uzsakymai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Uzsakymas — Atliekų tvarkymo užsakymų duomenys

Atliekų surinkimo, monitoringo ir logistikos informacinė sistemos (ASMLIS, MOKESTA) naudojamos atliekų tvarkymo organizavimui ir atsiskaitymui už komunalinių atliekų surinkimo ir išvežimo paslaugas. Priklausomai nuo naudojančios įstaigos duomenų aprėptis gali skirtis, tačiau duomenys numatyti būti atnaujinami kasdien. Duomenų rinkinį sudaro: pateikto paslaugos užsakymo identifikatorius, adresas, data, užsakytos paslaugos veiksmas, atliekų kodas, rūšis ir nurodytos vietovės apibūdinimas. Vienas įrašas atitinka vieną pateiktą užsakymą. Turint klausimų apie duomenų rinkinį, prašome kreiptis į Valstybės duomenų valdysenos atvėrimo komandą elektroniniu paštu atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/asmlis/uzsakymai/Uzsakymas`[^manifest]
- **Dataset:** [Atliekų tvarkymo užsakymų duomenys](../uzsakymai.md) (`datasets/gov/asmlis/uzsakymai`)[^manifest]
- **Manifest CSV:** [datasets/gov/asmlis/uzsakymai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/uzsakymai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/asmlis/uzsakymai/Uzsakymas` (`deployed`)[^manifest]
- **Provider:** `asmlis` — MOKESTA ir ASMLIS sistemos *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `uzsakymo_id` | `string` | — | `4` | `open` | — | Užsakymo identifikatorius | — |
| `uzsakymo_adresas` | `string` | — | `4` | `open` | — | Užsakymo vykdymo vietos adresas | — |
| `sav_kodas` | `string` | — | `4` | `open` | — | Savivaldybės kodas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | X koordinatė LKS94 koordinačių sistemoje | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Y koordinatė LKS94 koordinačių sistemoje | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Platumos koordinatė WGS84 koordinačių sistemoje | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Ilgumos koordinatė WGS84 koordinačių sistemoje | — |
| `koord_patik_proc` | `number` | — | `4` | `open` | — | Koordinačių patikimumas procentais | — |
| `adreso_tipas` | `string` | — | `4` | `open` | — | Adreso tipas | Adresas (aktualus) - reiškia, kad koordinatė atitinka adresą |
| `uzsakytas_veiksmas` | `string` | — | `3` | `open` | — | Užsakytos paslaugos veiksmas | — |
| `uzsakymo_data` | `date` | `D` | `4` | `open` | — | Užsakymo gavimo data | — |
| `atlieku_kodas` | `string` | — | `4` | `open` | — | Pilnas tvarkytų atliekų kodas | — |
| `atlieku_rusis` | `string` | — | `4` | `open` | — | Tvarkytų atliekų rūšis | — |
| `uzsakymo_vietos_rusis` | `string` | — | `4` | `open` | — | Užsakymo vykdymo vietos apibūdinimas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `uzsakytas_veiksmas` | `"Pakeisti"` | `Pakeisti` | — | Pakeisti nurodytą objektą | — |
| `uzsakytas_veiksmas` | `"Pastatyti"` | `Pastatyti` | — | Pastatyti naują objektą | — |
| `uzsakytas_veiksmas` | `"Ištuštinti"` | `Ištuštinti` | — | Ištuštinti nurodytą objektą | — |
| `uzsakytas_veiksmas` | `"Nuimti"` | `Nuimti` | — | Nuimti nurodytą objektą | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/asmlis/uzsakymai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/uzsakymai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/asmlis/uzsakymai (https://data.gov.lt/datasets/2763/)
