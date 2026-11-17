---
type: Dataset
title: "Lietuvos muitinei pateikiamų dokumentų sąrašo duomenys"
description: "Lietuvos muitinei pateikiamų dokumentų sąrašas tvarkomas Lietuvos Respublikos integruoto tarifo (LITAR) sistemoje (https://litarweb.lrmuitine.lt/taric/web/certsearchform_LT)."
resource: "https://get.data.gov.lt/datasets/gov/muitine/dokumentu_sarasas"
tags: [gov, muitine, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/dokumentu_sarasas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/dokumentu_sarasas.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Lietuvos muitinei pateikiamų dokumentų sąrašo duomenys

Lietuvos muitinei pateikiamų dokumentų sąrašas tvarkomas Lietuvos Respublikos integruoto tarifo (LITAR) sistemoje (https://litarweb.lrmuitine.lt/taric/web/certsearchform_LT).

Sąraše pateikiama informacija apie Lietuvos muitinei pateikiamus dokumentus (dokumentų rūšis), kurių duomenys nurodomi muitinės deklaracijose. Vienoje eilutėje pateikiama tam tikru laikotarpiu galiojančio vieno dokumento informacija: dokumento rūšis, rūšies galiojimo pradžios ir pabaigos data, rūšies pavadinimas, rūšies kodas (dokumento rūšis ir 3 simolių kodas), dokumento kodo galiojimo pradžios ir pabaigos data, kodo pavadinimas, bei dokumento pavadinimo įsigaliojimo data. Paskutiniame stulpelyje nurodomas dokumento šaltinis (Taric arba National).

Duomenų laikotarpis: nuo 2004 m. gegužės 1 d. Lietuvos Respublikoje galiojantys Europos Bendrijos integruoto tarifo (TARIC) duomenys apie dokumentus, papildyti nuo 2004 m. gegužės 1 d. galiojančiais nacionalinių dokumentų duomenimis.

Duomenų teikėjas – Muitinės departamentas prie Lietuvos Respublikos finansų ministerijos.

- **Namespace:** `datasets/gov/muitine/dokumentu_sarasas`[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/dokumentu_sarasas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/dokumentu_sarasas.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/dokumentu_sarasas`
- **Parent Namespace (`ns`):** Muitinės departamentas prie LR FM (`datasets/gov/muitine`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Dokumentas](dokumentu_sarasas/Dokumentas.md) | Lietuvos muitinei pateikiamų dokumentų sąrašo duomenys | `4` | `vda_prime_key` | — | 11 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spint` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/dokumentu_sarasas.csv
