---
type: Table
title: "TuristoRinkliava — Turisto rinkliavos deklaravimo duomenys"
description: "Rinkinyje pateikiami Klaipėdos miesto savivaldybės vietinės rinkliavos už suteiktą nakvynę (vadinamąjį turisto rinkliavos mokestį) deklaracijų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/turisto_rinkliava/TuristoRinkliava"
tags: [gov, klaipedos_m_sav, turistorinkliava, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/turisto_rinkliava.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/turisto_rinkliava.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3972/"
    title: "data.gov.lt DCAT-AP — datasets/gov/klaipedos_m_sav/turisto_rinkliava"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# TuristoRinkliava — Turisto rinkliavos deklaravimo duomenys

Rinkinyje pateikiami Klaipėdos miesto savivaldybės vietinės rinkliavos už suteiktą nakvynę (vadinamąjį turisto rinkliavos mokestį) deklaracijų duomenys. Vietinė rinkliava Klaipėdoje yra 1 euras už vienam asmeniui suteiktą nakvynę. Deklaracijas teikia fiziniai ir juridiniai asmenys, teikiantys apgyvendinimo paslaugas Klaipėdos mieste – nepriklausomai nuo to, ar veikla vykdoma pagal verslo liudijimą, individualios veiklos pažymą ar kitą apgyvendinimo paslaugų teikimo formą. Rinkinio objektas – viena turisto rinkliavos deklaracija, pateikta konkretaus apgyvendinimo paslaugų teikėjo už atitinkamus atskaitinius metus ir mėnesį ar ketvirtį. Rinkinyje pateikiami duomenys nurodo deklaraciją pateikusio subjekto tipą (fizinis ar juridinis asmuo), jo veiklą pagal Ekonominės veiklos rūšių klasifikatorių (EVRK 2.1), bei deklaracijos pateikimo laikotarpį. Šiame rinkinyje pateikiami duomenys neapima konkrečių nakvynių skaičiaus ar mokėtinų rinkliavos sumų, o atspindi faktą, jog deklaracija už tam tikrą laikotarpį buvo pateikta. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt[^manifest]

- **Model:** `datasets/gov/klaipedos_m_sav/turisto_rinkliava/TuristoRinkliava`[^manifest]
- **Dataset:** [Turisto rinkliavos deklaravimo duomenų rinkinys](../turisto_rinkliava.md) (`datasets/gov/klaipedos_m_sav/turisto_rinkliava`)[^manifest]
- **Manifest CSV:** [datasets/gov/klaipedos_m_sav/turisto_rinkliava.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/turisto_rinkliava.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/turisto_rinkliava/TuristoRinkliava` (`deployed`)[^manifest]
- **Provider:** `klaipedos_m_sav` — Klaipėdos miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Įrašo unikalus identifikatorius | — |
| `kodas` | `string` | — | `4` | `open` | — | Juridinio arba šifruotas fizinio asmens identifikatorius | — |
| `asmens_tipas` | `string` | — | `4` | `open` | — | Reikšmė nurodanti asmens tipą - fizinis arba juridinis asmuo | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Juridinis pavadinimas arba fizinio asmens vardas ir pavardė | — |
| `evrk_kodas` | `string` | — | `4` | `open` | — | Ekonominės veiklos rūšies kodas pagal EVRK 2.1 redakciją. | — |
| `evrk_aprasymas` | `string` | — | `4` | `open` | — | Ekonominės veiklos aprašymas pagal EVRK 2.1 kodą. | — |
| `metai` | `integer` | — | `4` | `open` | — | Deklaracijos pateikimo metai | — |
| `menuo` | `integer` | — | `4` | `open` | — | Reikšmė nurodo kalendorinį mėnesį (1–12), jei deklaruojama kas mėnesį, arba ketvirtį (1–4), jei deklaruojama kas ketvirtį. | — |

# Related References

- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/turisto_rinkliava.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/turisto_rinkliava.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/klaipedos_m_sav/turisto_rinkliava (https://data.gov.lt/datasets/3972/)
