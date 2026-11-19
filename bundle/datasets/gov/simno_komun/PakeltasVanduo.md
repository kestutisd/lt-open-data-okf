---
type: Table
title: "PakeltasVanduo — Iš gręžinių išgautas (pakeltas) vanduo"
description: "Rinkinyje pateikiamas Alytaus rajono savivaldybės įmonės „Simno komunalininkas“ vedamoje vandens gavybos apskaitoje stebimas iš gręžinių išgauto (pakelto) vandens kiekis ir jo teikimas gyventojams bei įmonėms."
resource: "https://get.data.gov.lt/datasets/gov/simno_komun/PakeltasVanduo"
tags: [gov, simno_komun, pakeltasvanduo, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/pakeltas_vanduo.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/simno_komun/pakeltas_vanduo.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2774/"
    title: "data.gov.lt DCAT-AP — datasets/gov/simno_komun"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PakeltasVanduo — Iš gręžinių išgautas (pakeltas) vanduo

Rinkinyje pateikiamas Alytaus rajono savivaldybės įmonės „Simno komunalininkas“ vedamoje vandens gavybos apskaitoje stebimas iš gręžinių išgauto (pakelto) vandens kiekis ir jo teikimas gyventojams bei įmonėms. Taip pat fiksuojamas technologinio vandens, skirto įrenginiams plauti, kiekis. Viena eilutė atitinka atitinkamo gręžinio tam tikro periodo ir parametro reikšmę. Duomenys kaupiami nuo 2018 metų. ir iki dabar. PASITEIRAVIMUI: Valstybės duomenų valdysenos atvėrimo komanda: atverimas@stat.gov.lt[^manifest]

- **Model:** `datasets/gov/simno_komun/PakeltasVanduo`[^manifest]
- **Dataset:** [Alytaus rajono savivaldybės įmonė „Simno komunalininkas“](../simno_komun.md) (`datasets/gov/simno_komun`)[^manifest]
- **Manifest CSV:** [datasets/gov/simno_komun/pakeltas_vanduo.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/pakeltas_vanduo.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/simno_komun/PakeltasVanduo` (`deployed`)[^manifest]
- **Provider:** `simno_komun` — Alytaus rajono savivaldybės įmonė „Simno komunalininkas“ *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `vandenvietes_pavadinimas` | `string` | — | `4` | `open` | — | Vandenvietės pavadinimas, iš kurios išgaunamas vanduo | — |
| `metai` | `date` | `D` | `4` | `open` | — | Metai | — |
| `periodas` | `string` | — | `4` | `open` | — | Periodas (mėn, ketv, metinis dienos vidurkis) | — |
| `rodiklis` | `string` | — | `4` | `open` | — | Rodiklis | — |
| `reiksme` | `number` | — | `4` | `open` | — | Skaitinė reikšmė | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `rodiklis` | `"išgautas vanduo"` | — | — | atitinkamą mėnesį išgautas vanduo | — |
| `rodiklis` | `"įmonėms tiekiamas vanduo"` | — | — | įmonėms tiekiamas vanduo | — |
| `rodiklis` | `"gyventojams tiekiamas vanduo"` | — | — | gyventojams tiekiamas vanduo | — |
| `rodiklis` | `"filtrų plovimo vanduo"` | — | — | vanduo skirtas filtrų technologiniam praplovimui | — |
| `rodiklis` | `"proc. filtrų plovimui"` | — | — | Procentinė vidutinė dienos išraiška kiek reikia vandens filtrų plovimui | — |
| `rodiklis` | `"m3/d. pakelto vandens"` | — | — | Vidutinis pakelto vandens kieks per dieną m3/d. | — |
| `rodiklis` | `"m3/d. į gyventojų ir įmonių tinklus"` | — | — | Vidutinis pakelto vandens kieks per dieną teikiamas į gyventojų ir į įmonių tinklus m3/d. | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/simno_komun/pakeltas_vanduo.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/simno_komun/pakeltas_vanduo.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/simno_komun (https://data.gov.lt/datasets/2774/)
