---
type: Dataset
title: "Atliekų tvarkytojų valstybės registro duomenys"
description: "Atliekų tvarkytojų valstybės registro duomenys - tvarkytojų leidžiami tvarkyti atliekų kiekiai, tvarkytojų registruotos tvarkomos atliekos, tvarkytojai turintys teises išrašyti atliekų sutvarkymą įrodančius dokumentus, komunalinių..."
resource: "https://get.data.gov.lt/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras"
tags: [gov, aaa, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Atliekų tvarkytojų valstybės registro duomenys

Atliekų tvarkytojų valstybės registro duomenys - tvarkytojų leidžiami tvarkyti atliekų kiekiai, tvarkytojų registruotos tvarkomos atliekos, tvarkytojai turintys teises išrašyti atliekų sutvarkymą įrodančius dokumentus, komunalinių atliekų tvarkymos sutartys, organizacijoms išduodamos licencijos ir atliekų kalsifikatorius

- **Namespace:** `datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras`[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [LeidziamaReiksme](atlieku_tvarkytoju_valstybes_registras/LeidziamaReiksme.md) | Leidžiamų tvarkyti atliekų kiekiai | `4` | `reiksmes_id` | — | 24 | Atliekų tvarkymo vietai TIPK/taršos leidime nustatyti leidžiamų tvarkyti atliekų kiekiai |
| [PatvirtintaAtlieka](atlieku_tvarkytoju_valstybes_registras/PatvirtintaAtlieka.md) | Registruotos tvarkomos atliekos | `4` | `patvirtintu_atlieku_id` | — | 24 | Atliekų tvarkytojų patvirtintos registruotos tvarkomos atliekos |
| [Teise](atlieku_tvarkytoju_valstybes_registras/Teise.md) | Teises išrašyti gaminių, pakuočių atliekų sutvarkymą įrodančius dokumentus turintys atliekų tvarkytojai | `4` | `teises_id` | — | 25 | Teisės išrašyti atliekų sutvarkymą įrodančius dokumentus |
| [Sutartis](atlieku_tvarkytoju_valstybes_registras/Sutartis.md) | Komunalinių atliekų tvarkymo sutartys | `4` | `sutarties_id` | — | 17 | Informacija apie komunalinių atliekų tvarkymo sutartys |
| [Atlieka](atlieku_tvarkytoju_valstybes_registras/Atlieka.md) | Atliekų klasifikatorius | `4` | `atliekos_id` | — | 12 | Atliekų klasifikatorius |
| [Licencija](atlieku_tvarkytoju_valstybes_registras/Licencija.md) | Informacija apie organizacijoms išduodamas licencijas | `4` | `licencijos_id` | — | 12 | Organizacijoms išduodamos licencijos |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv
