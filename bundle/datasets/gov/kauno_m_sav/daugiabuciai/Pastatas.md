---
type: Table
title: "Pastatas — Duomenys apie Kauno miesto daugiabučius"
description: "Pateikiami Kauno miesto savivaldybės duomenys apie Kauno mieste stovinčius daugiabučius pastatus."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/daugiabuciai/Pastatas"
tags: [gov, kauno_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/daugiabuciai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/daugiabuciai.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pastatas — Duomenys apie Kauno miesto daugiabučius

Pateikiami Kauno miesto savivaldybės duomenys apie Kauno mieste stovinčius daugiabučius pastatus. Rinkinio objektas - daugiabutis pastatas. Rinkinį sudaro informacija apie daugiabučio pastatymo laikotarpį, namo ir aplink jį esančios žemės plotus, namo pastatymo metus, valdymo formą ir esamą valdytoją, renovacijos būklę bei renovacijos metu atliktus darbus. Taip pat nurodytas namo adresas bei jo koordinatės.

- **Model:** `datasets/gov/kauno_m_sav/daugiabuciai/Pastatas`[^manifest]
- **Dataset:** [Duomenys apie Kauno miesto daugiabučius](../daugiabuciai.md) (`datasets/gov/kauno_m_sav/daugiabuciai`)
- **Manifest CSV:** [datasets/gov/kauno_m_sav/daugiabuciai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/daugiabuciai.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/daugiabuciai/Pastatas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros unikalus įrašo identifikatorius | — |
| `seniunija` | `string` | — | `4` | `open` | — | Seniūnijos pavadinimas | — |
| `gatve` | `string` | — | `4` | `open` | — | Gatvės pavadinimas | — |
| `namo_nr` | `string` | — | `4` | `open` | — | Daugiabučio namo numeris | — |
| `butu_sk` | `number` | `U` | `4` | `open` | — | Butų skaičius daugiabutyje | — |
| `negyvenamu_sk` | `number` | `U` | `4` | `open` | — | Negyvenamų butų skaičius | — |
| `aukstu_sk` | `number` | `U` | `4` | `open` | — | Aukštų skaičius daugiabutyje | — |
| `namo_plotas` | `number` | `m²` | `4` | `open` | — | Namo plotas | — |
| `zemes_plotas` | `number` | `m²` | `4` | `open` | — | Daugiabučiui priklausantis žemės plotas | — |
| `statybos_metai` | `date` | `Y` | `4` | `open` | — | Pastato statybos metai | — |
| `valdymo_forma` | `string` | — | `4` | `open` | — | Valdymo formos identifikatorius | — |
| `valdytojas` | `string` | — | `3` | `open` | — | Daugiabučio valdytojo pavadinimas | — |
| `admin_pabaiga` | `date` | `D` | `4` | `open` | — | Administravimo pabaigos data | — |
| `ar_perduotas` | `boolean` | — | `4` | `open` | — | Pastato administratoriaus perdavimo vienas kitam statuso identifikatorius | — |
| `bukle` | `string` | — | `4` | `open` | — | Daugiabučio būklė: renovuotas ar nerenovuotas | — |
| `atlikti_darbai_lt` | `string` | — | `1` | `open` | — | Duomenys apie atliktus darbus | — |
| `geometrija` | `geometry(point, 4326)` | `m` | `4` | `open` | — | Daugiabučio WGS koordinatės | — |
| `duomenu_atnaujinimas` | `date` | `D` | `4` | `open` | — | Duomenų atnaujinimo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `valdymo_forma` | `"Administratorius"` | — | — | — | — |
| `valdymo_forma` | `"Bendrija"` | — | — | — | — |
| `valdymo_forma` | `"Jungtinės veiklos sutartis"` | — | — | — | — |
| `valdymo_forma` | `"Kita"` | — | — | — | — |
| `valdymo_forma` | `"KTK"` | — | — | — | — |
| `bukle` | `"Nerenovuotas"` | — | — | — | — |
| `bukle` | `"Renovuotas"` | — | — | — | — |
| `bukle` | `"Renovuojamas"` | — | — | — | — |
| `bukle` | `"Gyventojai nepritarė investicijų planui"` | — | — | — | — |
| `bukle` | `"Paveldas, fasado tvarkybos darbai"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `atlikti_darbai_lt` | `update(property: "atlikti_darbai_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/daugiabuciai.csv
