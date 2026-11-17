---
type: Dataset
title: "datasets/gov/vat/tikrinimo_vietos"
description: "Pateikiama informacija apie prekių saugojimo ir muitinio tikrinimo vietas, pripažintas tinkamomis augalams, augaliniams produktams ir kitiems susijusiems objektams laikyti (pažymėjimo numeris; pažymėjimo išdavimo data; ūkio subjekto..."
resource: "https://get.data.gov.lt/datasets/gov/vat/tikrinimo_vietos"
tags: [gov, vat, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/tikrinimo_vietos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/tikrinimo_vietos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/vat/tikrinimo_vietos

Pateikiama informacija apie prekių saugojimo ir muitinio tikrinimo vietas, pripažintas tinkamomis augalams, augaliniams produktams ir kitiems susijusiems objektams laikyti (pažymėjimo numeris; pažymėjimo išdavimo data; ūkio subjekto pavadinimas; sandėlio / terminalo tipas ir numeris; sandėlio / terminalo adresas) Pateikiama informacija apie Patikrinimo vietas, pripažintas tinkamomis atlikti fitosanitarinį tikrinimą įvežamiems į Lietuvos Respubliką ir Europos Sąjungą augalams, augaliniams produktams ir kitiems objektams laikyti (pažymėjimo numeris; pažymėjimo išdavimo data; ūkio subjekto pavadinimas; sandėlio / terminalo adresas)

- **Namespace:** `datasets/gov/vat/tikrinimo_vietos`[^manifest]
- **Manifest CSV:** [datasets/gov/vat/tikrinimo_vietos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/tikrinimo_vietos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/tikrinimo_vietos`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Muitine](tikrinimo_vietos/Muitine.md) | Prekių saugojimo ir muitinio tikrinimo vietos, pripažintos tinkamomis augalams, augaliniams produktams ir kitiems susijusiems objektams laikyti | `4` | `eil_nr` | `open` | 6 | — |
| [FitosanitarineVieta](tikrinimo_vietos/FitosanitarineVieta.md) | Patikrinimo vietos, pripažintos tinkamomis atlikti fitosanitarinį tikrinimą įvežamiems į Lietuvos Respubliką ir Europos Sąjungą augalams, augaliniams produktams ir kitiems objektams laikyti | — | `eil_nr` | — | 5 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/tikrinimo_vietos.csv
