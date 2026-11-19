---
type: Table
title: "Paslauga — Vilniaus miesto socialinių paslaugų centro suteiktos paslaugos"
description: "Spinta table datasets/gov/vmspc/suteiktos_paslaugos/Paslauga (16 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmspc/suteiktos_paslaugos/Paslauga"
tags: [gov, vmspc, paslauga, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmspc/suteiktos_paslaugos.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vmspc/suteiktos_paslaugos.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3801/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmspc/suteiktos_paslaugos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Paslauga — Vilniaus miesto socialinių paslaugų centro suteiktos paslaugos

- **Model:** `datasets/gov/vmspc/suteiktos_paslaugos/Paslauga`[^manifest]
- **Dataset:** [Vilniaus miesto socialinių paslaugų centro suteiktos paslaugos](../suteiktos_paslaugos.md) (`datasets/gov/vmspc/suteiktos_paslaugos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmspc/suteiktos_paslaugos.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmspc/suteiktos_paslaugos.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmspc/suteiktos_paslaugos/Paslauga` (`deployed`)[^manifest]
- **Provider:** `vmspc` — BĮ Vilniaus miesto socialinių paslaugų centras *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `kvito_numeris` | `string` | — | `4` | `open` | — | Numeris | — |
| `apskaitos_laikotarpis` | `date` | `D` | `4` | `open` | — | Apskaitinis laikotarpis | — |
| `vienetu_kiekis` | `integer` | — | `4` | `open` | — | Vienetų kiekis | — |
| `minuciu_kiekis` | `integer` | — | `4` | `open` | — | Suteiktų paslaugų minučių skaičius | — |
| `apskaitos_vienetai` | `string` | — | `4` | `open` | — | Apskaitos vienetai | — |
| `paslaugos_kaina` | `number` | — | `4` | `open` | — | Paslaugos kaina | — |
| `priskaiciuota` | `number` | — | `4` | `open` | — | Priskaičiuota | — |
| `paslaugos_kodas` | `string` | — | `4` | `open` | — | Paslaugos kodas | — |
| `paslaugos_pavadinimas` | `string` | — | `4` | `open` | — | Paslaugos pavadinimas | — |
| `paslaugu_grupe` | `string` | — | `4` | `open` | — | Paslaugų grupė (I – individuali, N – neindividuali, T – transporto, V – visos) | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Asmens kodas | — |
| `lytis_ak` | `string` | — | `4` | `open` | — | Asmens lytis iš asmens kodo | — |
| `gim_desimtm_ak` | `date` | `10Y` | `4` | `open` | — | Asmens gimimo metai iš asmens kodo apvalinti dešimtimis | — |
| `tinkamas_ak` | `string` | — | `4` | `open` | — | Požymis, ar asmens kodas validus | — |
| `seniunijos_pavadinimas` | `string` | — | `4` | `open` | — | Seniunijos pavadinimas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paslaugu_grupe` | `"I"` | — | — | Individuali | — |
| `paslaugu_grupe` | `"N"` | — | — | Neindividuali | — |
| `paslaugu_grupe` | `"T"` | — | — | Transporto | — |
| `paslaugu_grupe` | `"V"` | — | — | Visos | — |
| `lytis_ak` | `"Moteris"` | — | — | Moteris | — |
| `lytis_ak` | `"Vyras"` | — | — | Vyras | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmspc/suteiktos_paslaugos.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmspc/suteiktos_paslaugos.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmspc/suteiktos_paslaugos (https://data.gov.lt/datasets/3801/)
