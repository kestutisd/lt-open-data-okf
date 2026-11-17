---
type: Dataset
title: "Eismo ribojimai valstybinės reikšmės keliuose"
description: "Duomenų rinkinyje pateikiami Valstybinės reikšmės kelių eismo informacinės sistemos duomenys apie valstybinių kelių eismo ribojimus dėl renginių, remonto darbų ar kelyje atsiradusių kliūčių."
resource: "https://get.data.gov.lt/datasets/gov/via_lietuva/eismo_ribojimai"
tags: [gov, via_lietuva, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/via_lietuva/eismo_ribojimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/eismo_ribojimai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Eismo ribojimai valstybinės reikšmės keliuose

Duomenų rinkinyje pateikiami Valstybinės reikšmės kelių eismo informacinės sistemos duomenys apie valstybinių kelių eismo ribojimus dėl renginių, remonto darbų ar kelyje atsiradusių kliūčių. Duomenų rinkinį sudaro keturios lentelės:

1. „Kelių remonto darbai“ – informacija apie kelio remonto darbus valstybinės reikšmės keliuose;

2. „Kliūtys kelyje“ – informacija apie kliūtis kelyje valstybinės reikšmės keliuose;

3. „Eismo ribojimai dėl renginių“ – eismo ribojimai dėl renginių valstybinės reikšmės keliuose;

4. „Valstybinių kelių atkarpos“ – valstybinių kelių atkarpų identifikatoriai su atitinkamų atkarpų pavadinimais ir ilgiais, kurie skirti jungti su rinkinyje esančiomis lentelėmis.

Duomenų teikėjas – AB „Via Lietuva“.

Duomenys kaupiami nuo 2020 m. birželio 1 d.

- **Namespace:** `datasets/gov/via_lietuva/eismo_ribojimai`[^manifest]
- **Manifest CSV:** [datasets/gov/via_lietuva/eismo_ribojimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/eismo_ribojimai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/via_lietuva/eismo_ribojimai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Remontas](eismo_ribojimai/Remontas.md) | Kelių remonto darbai | `4` | `darbo_id` | — | 14 | Duomenys apie kelių remonto darbus valstybinės reikšmės keliuose. |
| [Kliutis](eismo_ribojimai/Kliutis.md) | Kliūtys kelyje | `4` | `kliuties_id` | — | 10 | Duomenys apie kliūtis valstybinės reikšmės keliuose. |
| [Renginys](eismo_ribojimai/Renginys.md) | Eismo ribojimai dėl renginių | `4` | `ribojimo_id` | — | 10 | Duomenys apie eismo ribojimus dėl renginių valstybinės reikšmės keliuose. |
| [KelioAtkarpa](eismo_ribojimai/KelioAtkarpa.md) | Valstybinių kelių atkarpos | `4` | `kelio_id` | — | 7 | Duomenys apie valstybinių kelių atkarpas. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/via_lietuva/eismo_ribojimai.csv
