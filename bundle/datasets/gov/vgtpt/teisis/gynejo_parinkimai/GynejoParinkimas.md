---
type: Table
title: "GynejoParinkimas — Gynėjo parinkimų duomenys baudžiamosiose bylose, kai gynėjo dalyvavimas pripažintas būtinu"
description: "Valstybės garantuojamos teisinės pagalbos tarnybos duomenų, kaupiamų Teisinės pagalbos paslaugų informacinėje sistemoje (TEISIS),duomenys apie gynėjo parinkimą baudžiamosiose bylose, kai gynėjo dalyvavimas pripažintas būtinu."
resource: "https://get.data.gov.lt/datasets/gov/vgtpt/teisis/gynejo_parinkimai/GynejoParinkimas"
tags: [gov, vgtpt, gynejoparinkimas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/gynejo_parinkimai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/vgtpt/teisis/gynejo_parinkimai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1759/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vgtpt/teisis/gynejo_parinkimai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# GynejoParinkimas — Gynėjo parinkimų duomenys baudžiamosiose bylose, kai gynėjo dalyvavimas pripažintas būtinu

**Dataset Context:** Valstybės garantuojamos teisinės pagalbos tarnybos duomenų, kaupiamų Teisinės pagalbos paslaugų informacinėje sistemoje (TEISIS),duomenys apie gynėjo parinkimą baudžiamosiose bylose, kai gynėjo dalyvavimas pripažintas būtinu. Duomenų geografinė imtis — visa šalies teritorija. Brandos lygis — III. Atnaujinimo dažnumas — kas 1 mėn. Duomenų formatas — CSV. Licencija — CC BY 4.0. Atvėrimo data —2023-04-03.[^manifest]

- **Model:** `datasets/gov/vgtpt/teisis/gynejo_parinkimai/GynejoParinkimas`[^manifest]
- **Dataset:** [Gynėjo parinkimų duomenys baudžiamosiose bylose, kai gynėjo dalyvavimas pripažintas būtinu](../gynejo_parinkimai.md) (`datasets/gov/vgtpt/teisis/gynejo_parinkimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vgtpt/teisis/gynejo_parinkimai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/gynejo_parinkimai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vgtpt/teisis/gynejo_parinkimai/GynejoParinkimas` (`deployed`)[^manifest]
- **Provider:** `vgtpt` — Valstybės garantuojamos teisinės pagalbos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `parinkimo_metai` | `integer` | — | `2` | `open` | — | Metai, kada nustatytas gynėjo parinkimo pagrindas | — |
| `parinkimo_ketvirtis` | `integer` | — | `2` | `open` | — | Ketvirtis, kada nustatytas gynėjo parinkimo pagrindas | — |
| `teritorijos_kodas` | `ref` | [Teritorija](../klasifikatoriai/Teritorija.md) (`level=4 UUID`: `teritorijos_kodas._id`) | `4` | `open` | — | Antrinę teisinę pagalbą gaunančio asmens gyvenamosios vietos teritorijos kodas | Iš TEISIS teritorijos klasifikatoriaus |
| `parinkimo_pagrindo_kodas` | `ref` | [ParinkimoPagrindas](../klasifikatoriai/ParinkimoPagrindas.md) (`level=4 UUID`: `parinkimo_pagrindo_kodas._id`) | `4` | `open` | — | Gynėjo parinkimų duomenys baudžiamosiose bylose | Kai gynėjo dalyvavimas pripažintas būtinu, teisinis pagrindas —Baudžiamojo proceso kodekso straipsnio kodas iš TEISIS pagalbos teikimo pagrindų klasifikatoriaus |
| `parinkimu_skaicius` | `integer` | `U` | `4` | `open` | — | Gynėjo parinkimų pagal gautus prašymus skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `parinkimo_metai` | `update(type: "date", ref: "Q")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vgtpt/teisis/gynejo_parinkimai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/gynejo_parinkimai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vgtpt/teisis/gynejo_parinkimai (https://data.gov.lt/datasets/1759/)
