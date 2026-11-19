---
type: Table
title: "VeiklosRodiklis — Lovos veiklos rodikliai"
description: "Pagal asmens sveikatos priežiūros įstaigą, lovų specialybės grupes, savivaldybes"
resource: "https://get.data.gov.lt/datasets/gov/hi/lovos/VeiklosRodiklis"
tags: [gov, hi, veiklosrodiklis, deployed, level-3, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/lovos.csv#L18"
    title: "atviriduomenys/manifest — datasets/gov/hi/lovos.csv#L18"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1230/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/lovos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# VeiklosRodiklis — Lovos veiklos rodikliai

**Dataset Context:** Pagal asmens sveikatos priežiūros įstaigą, lovų specialybės grupes, savivaldybes[^manifest]

- **Model:** `datasets/gov/hi/lovos/VeiklosRodiklis`[^manifest]
- **Dataset:** [Stacionaro lovų skaičius ir jų veiklos rodikliai](../lovos.md) (`datasets/gov/hi/lovos`)[^manifest]
- **Manifest CSV:** [datasets/gov/hi/lovos.csv#L18](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/lovos.csv#L18)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/lovos/VeiklosRodiklis` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | `yr` | `2` | `open` | — | Duomenų vedimo metai | — |
| `sav_kodas` | `ref` | [Savivaldybe](Savivaldybe.md) (`level=4 UUID` via `Savivaldybe[sav_kodas]`: `sav_kodas._id`) | `4` | `open` | — | Savivaldybės kodas | — |
| `istg_id` | `ref` | [Istaiga](Istaiga.md) (`level=4 UUID`: `istg_id._id`) | `4` | `open` | — | Įstaigos ID | — |
| `tev_ist_id` | `ref` | [Istaiga](Istaiga.md) (`level=4 UUID`: `tev_ist_id._id`) | `4` | `open` | — | Tėvinės įstaigos ID | — |
| `prof_kod` | `string` | — | `4` | `open` | — | Lovos profilis | — |
| `grupes_kodas` | `string` | — | `4` | `open` | — | Lovų profilių grupė | — |
| `lov` | `integer` | `U` | `4` | `open` | — | Lovų skaičius metų gale | Stacionaro lovų skaičius metų pabaigoje |
| `vid_lov` | `number` | `U` | `4` | `open` | — | Vidutinis metinis lovų skaičius | Nustatomas vidutinę mėnesinę lovų skaičiaus sumą dalijant iš 12 arba metų kiekvienos dienos lovų skaičiaus sumą dalinant iš metų dienų skaičiaus (365 arba 366). Šis rodiklis parodo stacionaro lovų vidutinį skaičių per kalendorinius metus |
| `hosp` | `integer` | `U` | `4` | `open` | — | Hospitalizuotų ligonių skaičius | Pacientų, paguldytų į stacionarinio gydymo įstaigą (skyrių,)skaičius |
| `hosp_vaik` | `integer` | `U` | `4` | `open` | — | Iš hospitalizuotų 0-17 m. vaikai | 0-17 m. vaikų, paguldytų į stacionarinio gydymo įstaigą (skyrių), skaičius |
| `isr` | `integer` | `U` | `4` | `open` | — | Išrašyta ir perkelta ligonių | Pacientai, išvykę iš stacionaro į namus arba perkelti į kitą gydymo įstaigą |
| `mire` | `integer` | `U` | `4` | `open` | — | Mirę ligoniai | — |
| `lovadieniai` | `integer` | `d` | `4` | `open` | — | Lovadieniai | Kalendorinių dienų skaičius nuo paciento atvykimo į ligoninę iki jo išrašymo. Atvykimo ir išrašymo diena skaičiuojama kaip viena. Jei ligonis atvyko ir išsirašė tą pačią dieną, skaičiuojamas 1 lovadienis |
| `funk` | `number` | `d` | `4` | `open` | — | Lovos funkcionavimas (užimtumas), dienomis | Parodo, kiek dienų per metus stacionaro lova buvo užimta, dienomis |
| `funk_proc` | `number` | `%` | `4` | `open` | — | Lovos funkcionavimas (užimtumas), procentais | Parodo, kokią dalį (procentais) dienų per metus stacionaro lova buvo užimta |
| `vgl` | `number` | `d` | `4` | `open` | — | Vidutinis gulėjimo laikas | Vidutinė vieno gulėjimo stacionare trukmė |
| `apyv` | `number` | `U` | `4` | `open` | — | Lovos apyvarta | Parodo, kiek vidutiniškai vienoje stacionaro lovoje gulėjo ligonių per metus |
| `letal` | `number` | `%` | `4` | `open` | — | Letališkumas | Mirusių stacionaro ligonių dalis (proc.) |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/lovos.csv#L18 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/lovos.csv#L18)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/lovos (https://data.gov.lt/datasets/1230/)
