---
type: Table
title: "SanitarineApzvalga"
description: "Spinta table datasets/gov/miskai/sanitarine/SanitarineApzvalga (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/sanitarine/SanitarineApzvalga"
tags: [gov, miskai, sanitarineapzvalga, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sanitarine.csv#L47"
    title: "atviriduomenys/manifest — datasets/gov/miskai/sanitarine.csv#L47"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/827/"
    title: "data.gov.lt DCAT-AP — datasets/gov/miskai/sanitarine"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# SanitarineApzvalga

- **Model:** `datasets/gov/miskai/sanitarine/SanitarineApzvalga`[^manifest]
- **Dataset:** [Miškų sanitarinė būklė](../sanitarine.md) (`datasets/gov/miskai/sanitarine`)[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/sanitarine.csv#L47](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sanitarine.csv#L47)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/sanitarine/SanitarineApzvalga` (`deployed`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vyk_data` | `datetime` | `T` | `4` | `open` | — | Įrašo sukūrimo data ir laikas | — |
| `vieta` | `ref` | [Vieta](Vieta.md) (`level=4 UUID`: `vieta._id`) | `4` | `open` | — | Naudotojo pasirinkta vieta (medelynas arba miškas) | — |
| `tipas` | `ref` | [Tipas](Tipas.md) (`level=4 UUID`: `tipas._id`) | `4` | `open` | — | Pasirinktas pildymo tipas (židinių registravimas arba profilaktinių priemonių registravimas) | — |
| `plotas` | `number` | `ha` | `4` | `open` | — | — | Suminis sklypų plotas |
| `kenkejas` | `ref` | [Kenkejas](Kenkejas.md) (`level=4 UUID`: `kenkejas._id`) | `4` | `open` | — | — | Kenkėjas |
| `pazeidimo_kiekis_proc` | `number` | `%` | `4` | `open` | — | — | Pažeidimo kiekis procentais |
| `pazeidimo_kiekis` | `number` | — | `3` | `open` | — | — | Pažeidimo kiekis |
| `pazeidimo_laipsnis` | `number` | `%` | `4` | `open` | — | — | Pažeidimo laipsnis |
| `priemones` | `ref` | [Priemone](Priemone.md) (`level=4 UUID`: `priemones._id`) | `4` | `open` | — | — | Naudota priemonė |
| `priemones_kiekis` | `number` | — | `3` | `open` | — | — | Priemonės kiekis |
| `priemones_plotas` | `number` | `ha` | `4` | `open` | — | — | Plotas, kuriame panaudota priemonė |
| `preparatas` | `ref` | [Preparatas](Preparatas.md) (`level=4 UUID`: `preparatas._id`) | `4` | `open` | — | — | Preparatas |
| `sunaudotas_preparatas` | `number` | — | `3` | `open` | — | — | Kiek preparato sunaudota |
| `savininkas` | `ref` | [Savininkas](Savininkas.md) (`level=4 UUID`: `savininkas._id`) | `4` | `open` | — | — | Miško savininkas/naudotojas |
| `atnaujinta` | `datetime` | `T` | `4` | `open` | — | — | Atnaujinimo data |
| `kadastrinis_nr` | `string` | — | `3` | `open` | — | — | Kadastro numeris |
| `vietove_pav` | `string` | — | `2` | `open` | — | — | Regioninis padalinys / girininkija / kvartalas / sklypo nr. ir jo dalis (jei yra) |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/sanitarine.csv#L47 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sanitarine.csv#L47)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/miskai/sanitarine (https://data.gov.lt/datasets/827/)
