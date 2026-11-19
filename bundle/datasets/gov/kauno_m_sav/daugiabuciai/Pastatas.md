---
type: Table
title: "Pastatas — Duomenys apie Kauno miesto daugiabučius"
description: "Pateikiami Kauno miesto savivaldybės duomenys apie Kauno mieste stovinčius daugiabučius pastatus."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/daugiabuciai/Pastatas"
tags: [gov, kauno_m_sav, pastatas, deployed, level-4, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/daugiabuciai.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/daugiabuciai.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2744/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/daugiabuciai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pastatas — Duomenys apie Kauno miesto daugiabučius

Pateikiami Kauno miesto savivaldybės duomenys apie Kauno mieste stovinčius daugiabučius pastatus. Rinkinio objektas - daugiabutis pastatas. Rinkinį sudaro informacija apie daugiabučio pastatymo laikotarpį, namo ir aplink jį esančios žemės plotus, namo pastatymo metus, valdymo formą ir esamą valdytoją, renovacijos būklę bei renovacijos metu atliktus darbus. Taip pat nurodytas namo adresas bei jo koordinatės. Pasiteiravimui kreiptis į Valstybės duomenų valdysenos komandą: vdv@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/kauno_m_sav/daugiabuciai/Pastatas`[^manifest]
- **Dataset:** [Duomenys apie Kauno miesto daugiabučius](../daugiabuciai.md) (`datasets/gov/kauno_m_sav/daugiabuciai`)[^manifest]
- **Manifest CSV:** [datasets/gov/kauno_m_sav/daugiabuciai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/daugiabuciai.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/daugiabuciai/Pastatas` (`deployed`)[^manifest]
- **Provider:** `kauno_m_sav` — Kauno miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_2`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/daugiabuciai.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/daugiabuciai.csv#L8)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/daugiabuciai (https://data.gov.lt/datasets/2744/)
