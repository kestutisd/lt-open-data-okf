---
type: Dataset
title: "Vilniaus atliekų sistemos administratoriaus atliekų tvarkymas"
description: "Rinkinys sudarytas iš SĮ „Vilniaus atliekų sistemos administratorius“ (VASA) atliekų tvarkymo informacinių sistemų „ASMLIS“ ir „SAVITARNA“ duomenų."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas"
tags: [gov, vilniaus_m_sav, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Vilniaus atliekų sistemos administratoriaus atliekų tvarkymas

Rinkinys sudarytas iš SĮ „Vilniaus atliekų sistemos administratorius“ (VASA) atliekų tvarkymo informacinių sistemų „ASMLIS“ ir „SAVITARNA“ duomenų. Rinkinį sudaro lentelės, kuriose pateikiama išsami informacija apie atliekų surinkimo infrastruktūrą, planuojamus išvežimus ir istorinius surinkimo duomenis.

Išvežimų tvarkaraščių lentelėje pateikiama informacija apie atliekų surinkimo taškus ir jų aptarnavimo tvarkaraščius. Viena eilutė atitinka artimiausią konteinerio išvežimo informaciją: konteinerio identifikacinius duomenis, jo charakteristikas, aptarnavimo informaciją ir geografinius duomenis.

Konteinerių išvežimų lentelėje pateikiamas faktinių atliekų surinkimo operacijų žurnalas. Viena eilutė atitinka vieną konteinerio aptarnavimo operaciją. Lentelėje galima rasti konteinerių informaciją, surinktų atliekų kiekius, operacijų detales, geografines operacijų vietas.

Išvežimų tvarkaraščių ir konteinerių išvežimų lentelių duomenys pateikiami nuo 2023 m. sausio mėnesio pradžios. Šias dvi lenteles tarpusavyje galima jungti per „inventorinis_nr“ raktą.

Didelių gabaritų atliekų lentelėje pateikiami individualių atliekų paėmimų užsakymai nuo 2023 m. spalio mėnesio pabaigos. Vienas užsakymas gali apimti kelias skirtingas daiktų grupes, todėl jie išdėstyti atskirose lentelės eilutėse.

Duomenų teikėjas – SĮ „Vilniaus atliekų sistemos administratorius“.

- **Namespace:** `datasets/gov/vilniaus_m_sav/atlieku_tvarkymas`[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [KonteinerioIsvezimas](atlieku_tvarkymas/KonteinerioIsvezimas.md) | — | `4` | `pickup_history_id` | — | 12 | — |
| [IsvezimoTvarkarastis](atlieku_tvarkymas/IsvezimoTvarkarastis.md) | Konteinerių išvežimo tvarkaraštis | `4` | `waste_object_id` | — | 12 | Informacija apie atliekų surinkimo taškus ir jų aptarnavimo tvarkaraščius. |
| [DideliuGabarituAtlieka](atlieku_tvarkymas/DideliuGabarituAtlieka.md) | Didelių gabaritų atliekos | — | `vda_id` | — | 11 | Rinkinio lentelėje pateikiami SĮ „Vilniaus atliekų sistemos administratoriaus“ (VASA) gaunami užsakymai išvežti didelių gabaritų atliekas Vilniaus miesto... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv
