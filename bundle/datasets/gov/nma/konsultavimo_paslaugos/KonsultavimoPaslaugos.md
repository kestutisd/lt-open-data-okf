---
type: Table
title: "KonsultavimoPaslaugos — Strateginio plano Kaimo plėtros programos priemonė \"Konsultavimo paslaugos\". Bendra informacija."
description: "Konsultavimo paslaugos (25PK1)."
resource: "https://get.data.gov.lt/datasets/gov/nma/konsultavimo_paslaugos/KonsultavimoPaslaugos"
tags: [gov, nma, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nma/konsultavimo_paslaugos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/konsultavimo_paslaugos.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# KonsultavimoPaslaugos — Strateginio plano Kaimo plėtros programos priemonė "Konsultavimo paslaugos". Bendra informacija.

Konsultavimo paslaugos (25PK1). Bendra informacija

- **Model:** `datasets/gov/nma/konsultavimo_paslaugos/KonsultavimoPaslaugos`[^manifest]
- **Dataset:** [datasets/gov/nma/konsultavimo_paslaugos](../konsultavimo_paslaugos.md) (`datasets/gov/nma/konsultavimo_paslaugos`)
- **Manifest CSV:** [datasets/gov/nma/konsultavimo_paslaugos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/konsultavimo_paslaugos.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nma/konsultavimo_paslaugos/KonsultavimoPaslaugos`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Projekto įgyvendinimo vieta (savivaldybės lygiu) | — |
| `priemones_pavadinimas` | `string` | — | `3` | `open` | — | Priemonės pavadinimas | — |
| `pareiskejo_lytis` | `string` | — | `4` | `open` | — | Pareiškėjo lytis | — |
| `pareiskejo_tipas` | `string` | — | `4` | `open` | — | Pareiškėjo tipas | — |
| `sprendimo_data` | `date` | `D` | — | `open` | — | Sprendimo skirti paramą data | — |
| `bylos_etapas` | `string` | — | `3` | `open` | — | Bylos etapas | — |
| `paraiskos_nutraukimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos nutraukimo data | — |
| `paraiskos_gavimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos gavimo data | — |
| `es_paramos_dalis` | `number` | — | — | `open` | — | Paramos sumos ES dalis, Eur | — |
| `lt_paramos_dalis` | `number` | — | — | `open` | — | Paramos sumos LT dalis, Eur | — |
| `konsultacijos_data` | `date` | `D` | `4` | `open` | — | Pareiškėjo konsultacijos data | — |
| `kvietimo_pradzios_data` | `date` | `D` | `4` | `open` | — | Kvietimo pabaiga | — |
| `kvietimo_pabaigos_data` | `date` | `D` | `4` | `open` | — | Kvietimo pradžia | — |
| `skirta_suma` | `number` | — | — | `open` | — | Skirta paramos suma, Eur | — |
| `prasoma_suma` | `number` | — | — | `open` | — | Prašoma paramos suma, Eur | — |
| `veiklos_sritis` | `string` | — | — | `open` | — | Veiklos sritis | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pareiskejo_lytis` | `'V'` | — | — | Vyras | — |
| `pareiskejo_lytis` | `'M'` | — | — | Moteris | — |
| `pareiskejo_tipas` | `'Fizinis'` | — | — | Fizinis asmuo | — |
| `pareiskejo_tipas` | `'Juridinis'` | — | — | Juridinis asmuo | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nma/konsultavimo_paslaugos.csv
