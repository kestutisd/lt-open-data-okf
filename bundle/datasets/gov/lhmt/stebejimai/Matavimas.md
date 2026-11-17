---
type: Table
title: "Matavimas — Rinkinyje pateikiami Lietuvos meteorologijos stočių meteorologinių stebėjimų duomenys."
description: "Duomenų rinkinį sudaro stoties pavadinimas ir kodas, stoties lokacijos koordinatės, stebėjimo laikas, reali ir juntamoji oro temperatūra stebėjimo metu, vėjo greitis, vėjo gūsis, vėjo kryptis, debesuotumas, slėgis jūros lygmenyje..."
resource: "https://get.data.gov.lt/datasets/gov/lhmt/stebejimai/Matavimas"
tags: [gov, lhmt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lhmt/stebejimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/stebejimai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Matavimas — Rinkinyje pateikiami Lietuvos meteorologijos stočių meteorologinių stebėjimų duomenys.

Duomenų rinkinį sudaro stoties pavadinimas ir kodas, stoties lokacijos koordinatės, stebėjimo laikas, reali ir juntamoji oro temperatūra stebėjimo metu, vėjo greitis, vėjo gūsis, vėjo kryptis, debesuotumas, slėgis jūros lygmenyje, santykinė oro drėgmė, kritulių kiekis ir oro sąlygos.

- **Model:** `datasets/gov/lhmt/stebejimai/Matavimas`[^manifest]
- **Dataset:** [Rinkinyje pateikiami Lietuvos meteorologijos stočių meteorologinių stebėjimų duomenys.](../stebejimai.md) (`datasets/gov/lhmt/stebejimai`)
- **Manifest CSV:** [datasets/gov/lhmt/stebejimai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/stebejimai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lhmt/stebejimai/Matavimas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Pirminis raktas | — |
| `stoties_pavadinimas` | `string` | — | `4` | `open` | — | Meteorologinės stoties pavadinimas | — |
| `stoties_kodas` | `string` | — | `4` | `open` | — | Meteorologinės stoties kodas | — |
| `ilguma` | `number` | — | `4` | `open` | — | Stoties ilgumos koordinatė | — |
| `platuma` | `number` | — | `4` | `open` | — | Stoties platumos koordinatė | — |
| `stebejimo_laikas` | `datetime` | `L` | `4` | `open` | — | Stebėjimo laikas | — |
| `oro_temp` | `number` | — | `4` | `open` | — | Reali oro temperatūra | — |
| `juntamoji_temp` | `number` | — | `4` | `open` | — | Juntamoji oro temperatūra | — |
| `vejo_greitis` | `number` | — | `4` | `open` | — | Vėjo greitis | — |
| `vejo_gusis` | `number` | — | `4` | `open` | — | Vėjo gūsis | — |
| `vejo_kryptis` | `integer` | — | `4` | `open` | — | Vėjo kryptis | — |
| `debesuotumas` | `integer` | — | `4` | `open` | — | Debesuotumas | — |
| `slegis_juros_lyg` | `number` | — | `4` | `open` | — | Slėgis jūros lygmenyje | — |
| `santyk_oro_dregme` | `integer` | — | `4` | `open` | — | Santykinė oro drėgmė | — |
| `kritutliu_kiekis` | `number` | — | `4` | `open` | — | Kritulių kiekis | — |
| `oro_salygos` | `string` | — | `4` | `open` | — | Oro sąlygos | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lhmt/stebejimai.csv
