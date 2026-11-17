---
type: Table
title: "LicencijuojamaVeikla — Policijos licencijuojamų veiklų duomenys"
description: "Lentelėje pateikiami Policijos departamento prie LR vidaus reikalų ministerijos išduotų ir galiojančių licencijų vykdyti tam tikrą veiklą duomenys iš Policijos licencijuojamos veiklos informacinės sistemos (PLVIS)."
resource: "https://get.data.gov.lt/datasets/gov/pd/policijos_licencijuojamos_veiklos/LicencijuojamaVeikla"
tags: [gov, pd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pd/policijos_licencijuojamos_veiklos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/policijos_licencijuojamos_veiklos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# LicencijuojamaVeikla — Policijos licencijuojamų veiklų duomenys

Lentelėje pateikiami Policijos departamento prie LR vidaus reikalų ministerijos išduotų ir galiojančių licencijų vykdyti tam tikrą veiklą duomenys iš Policijos licencijuojamos veiklos informacinės sistemos (PLVIS).

- **Model:** `datasets/gov/pd/policijos_licencijuojamos_veiklos/LicencijuojamaVeikla`[^manifest]
- **Dataset:** [Policijos licencijuojamų veiklų duomenys](../policijos_licencijuojamos_veiklos.md) (`datasets/gov/pd/policijos_licencijuojamos_veiklos`)
- **Manifest CSV:** [datasets/gov/pd/policijos_licencijuojamos_veiklos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/policijos_licencijuojamos_veiklos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pd/policijos_licencijuojamos_veiklos/LicencijuojamaVeikla`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `licencijos_dok_numeris` | `string` | — | `4` | `open` | — | Licencijos numeris | — |
| `licencijos_rusies_pav` | `string` | — | `4` | `open` | — | Licencijos rūšies pavadinimas | — |
| `veiklos_pavadinimas` | `string` | — | `4` | `open` | — | Licencijuojamos veiklos pavadinimas | — |
| `inst_kodas` | `string` | — | `4` | `open` | — | Licenciją gavusios institucijos juridinio asmens kodas | — |
| `inst_pavadinimas` | `string` | — | `4` | `open` | — | Licenciją gavusios institucijos pavadinimas arba licenciją gavusio fizinio asmens vardas ir pavardė | — |
| `galioja_nuo` | `date` | `D` | `4` | `open` | — | Licencijos galiojimo pradžios data | — |
| `kas_isdave` | `string` | — | `4` | `open` | — | Institucijos, išdavusios licenciją, pavadinimas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `inst_kodas` | `create(property: "ja_kodas", type: "ref", ref: "datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pd/policijos_licencijuojamos_veiklos.csv
