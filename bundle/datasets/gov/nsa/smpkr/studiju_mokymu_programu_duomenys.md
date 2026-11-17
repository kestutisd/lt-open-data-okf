---
type: Dataset
title: "Studijų ir mokymų programų duomenys"
description: "Rinkinyje pateikiami studijų ir mokymų programų duomenys – programų sąrašai, akreditacijos informacija, studentų skaičiai – iš Nacionalinės švietimo agentūros (NŠA) Studijų, mokymo programų ir kvalifikacijų registro (SMPKR) bei Studentų..."
resource: "https://get.data.gov.lt/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys"
tags: [gov, nsa, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Studijų ir mokymų programų duomenys

Rinkinyje pateikiami studijų ir mokymų programų duomenys – programų sąrašai, akreditacijos informacija, studentų skaičiai – iš Nacionalinės švietimo agentūros (NŠA) Studijų, mokymo programų ir kvalifikacijų registro (SMPKR) bei Studentų registro (SR), taip pat stojimų į konkrečias studijų programas duomenys iš LAMA BPO sistemos.

- **Namespace:** `datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys`[^manifest]
- **Manifest CSV:** [datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [StudijuPrograma](studiju_mokymu_programu_duomenys/StudijuPrograma.md) | Studijų ir mokymų programos | `4` | `vda_prime_key` | — | 29 | Lentelėje pateiktos studijų ir mokymų programos iš Nacionalinės švietimo agentūros (NŠA) Studijų, mokymo programų ir kvalifikacijų registro (SMPKR). |
| [ProgramosAkreditacija](studiju_mokymu_programu_duomenys/ProgramosAkreditacija.md) | Studijų ir mokymų programų akreditacijos | `4` | `vda_prime_key` | — | 12 | Lentelėje pateikti studijų ir mokymų programų akreditacijų duomenys iš Nacionalinės švietimo agentūros (NŠA) Studijų, mokymo programų ir kvalifikacijų... |
| [ProgramosStojimas](studiju_mokymu_programu_duomenys/ProgramosStojimas.md) | Stojimų į aukštojo mokslo programas duomenys | `4` | `vda_prime_key` | — | 16 | Lentelėje pateikiami apibendrinti kasmetinių stojimų į aukštojo mokslo programas duomenys iš LAMA BPO sistemos. |
| [ProgramosStudentas](studiju_mokymu_programu_duomenys/ProgramosStudentas.md) | Studentai studijų programose | `4` | `vda_prime_key` | — | 6 | Lentelėje pateikiami studentų, bent šiek tiek studijavusių ir baigusių tam tikrą programą konkrečiais metais, skaičiai iš Nacionalinės švietimo agentūros... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv
