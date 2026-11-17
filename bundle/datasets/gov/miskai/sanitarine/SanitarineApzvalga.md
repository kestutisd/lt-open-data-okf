---
type: Table
title: "SanitarineApzvalga"
description: "Spinta table datasets/gov/miskai/sanitarine/SanitarineApzvalga (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/sanitarine/SanitarineApzvalga"
tags: [gov, miskai, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/miskai/sanitarine.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sanitarine.csv#L47"
    last_modified: "2026-11-11T14:39:20Z"
---

# SanitarineApzvalga

- **Model:** `datasets/gov/miskai/sanitarine/SanitarineApzvalga`[^manifest]
- **Dataset:** [datasets/gov/miskai/sanitarine](../sanitarine.md) (`datasets/gov/miskai/sanitarine`)
- **Manifest CSV:** [datasets/gov/miskai/sanitarine.csv#L47](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/sanitarine.csv#L47)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/sanitarine/SanitarineApzvalga`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vyk_data` | `datetime` | `T` | `4` | `open` | — | Įrašo sukūrimo data ir laikas | — |
| `vieta` | `ref` | [Vieta](Vieta.md) | `4` | `open` | — | Naudotojo pasirinkta vieta (medelynas arba miškas) | — |
| `tipas` | `ref` | [Tipas](Tipas.md) | `4` | `open` | — | Pasirinktas pildymo tipas (židinių registravimas arba profilaktinių priemonių registravimas) | — |
| `plotas` | `number` | `ha` | `4` | `open` | — | — | Suminis sklypų plotas |
| `kenkejas` | `ref` | [Kenkejas](Kenkejas.md) | `4` | `open` | — | — | Kenkėjas |
| `pazeidimo_kiekis_proc` | `number` | `%` | `4` | `open` | — | — | Pažeidimo kiekis procentais |
| `pazeidimo_kiekis` | `number` | — | `3` | `open` | — | — | Pažeidimo kiekis |
| `pazeidimo_laipsnis` | `number` | `%` | `4` | `open` | — | — | Pažeidimo laipsnis |
| `priemones` | `ref` | [Priemone](Priemone.md) | `4` | `open` | — | — | Naudota priemonė |
| `priemones_kiekis` | `number` | — | `3` | `open` | — | — | Priemonės kiekis |
| `priemones_plotas` | `number` | `ha` | `4` | `open` | — | — | Plotas, kuriame panaudota priemonė |
| `preparatas` | `ref` | [Preparatas](Preparatas.md) | `4` | `open` | — | — | Preparatas |
| `sunaudotas_preparatas` | `number` | — | `3` | `open` | — | — | Kiek preparato sunaudota |
| `savininkas` | `ref` | [Savininkas](Savininkas.md) | `4` | `open` | — | — | Miško savininkas/naudotojas |
| `atnaujinta` | `datetime` | `T` | `4` | `open` | — | — | Atnaujinimo data |
| `kadastrinis_nr` | `string` | — | `3` | `open` | — | — | Kadastro numeris |
| `vietove_pav` | `string` | — | `2` | `open` | — | — | Regioninis padalinys / girininkija / kvartalas / sklypo nr. ir jo dalis (jei yra) |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/sanitarine.csv
