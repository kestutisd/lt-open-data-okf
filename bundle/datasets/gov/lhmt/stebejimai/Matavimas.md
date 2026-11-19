---
type: Table
title: "Matavimas — Rinkinyje pateikiami Lietuvos meteorologijos stočių meteorologinių stebėjimų duomenys."
description: "Duomenų rinkinį sudaro stoties pavadinimas ir kodas, stoties lokacijos koordinatės, stebėjimo laikas, reali ir juntamoji oro temperatūra stebėjimo metu, vėjo greitis, vėjo gūsis, vėjo kryptis, debesuotumas, slėgis jūros lygmenyje, santykinė oro drėgmė, kritulių kiekis ir oro..."
resource: "https://get.data.gov.lt/datasets/gov/lhmt/stebejimai/Matavimas"
tags: [gov, lhmt, matavimas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/stebejimai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lhmt/stebejimai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3872/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lhmt/stebejimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Matavimas — Rinkinyje pateikiami Lietuvos meteorologijos stočių meteorologinių stebėjimų duomenys.

Duomenų rinkinį sudaro stoties pavadinimas ir kodas, stoties lokacijos koordinatės, stebėjimo laikas, reali ir juntamoji oro temperatūra stebėjimo metu, vėjo greitis, vėjo gūsis, vėjo kryptis, debesuotumas, slėgis jūros lygmenyje, santykinė oro drėgmė, kritulių kiekis ir oro sąlygos.[^manifest]

- **Model:** `datasets/gov/lhmt/stebejimai/Matavimas`[^manifest]
- **Dataset:** [Rinkinyje pateikiami Lietuvos meteorologijos stočių meteorologinių stebėjimų duomenys.](../stebejimai.md) (`datasets/gov/lhmt/stebejimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lhmt/stebejimai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/stebejimai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lhmt/stebejimai/Matavimas` (`deployed`)[^manifest]
- **Provider:** `lhmt` — Lietuvos hidrometeorologijos tarnyba (LHMT) *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lhmt/stebejimai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lhmt/stebejimai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lhmt/stebejimai (https://data.gov.lt/datasets/3872/)
