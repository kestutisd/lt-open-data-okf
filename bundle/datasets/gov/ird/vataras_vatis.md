---
type: Dataset
title: "Valstybės tarnautojų registras, Valstybės tarnybos valdymo informacinė sistema"
description: "Šių informacinių sistemų tikslas – vykdyti žmogiškųjų išteklių valdymo viešajame administravime, valstybės tarnybos valdymo sprendimų planavimo, Valstybės tarnybos įstatymo ir su juo susijusių teisės aktų įgyvendinimo kontrolės procedūras."
resource: "https://get.data.gov.lt/datasets/gov/ird/vataras_vatis"
tags: [gov, ird, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ird/vataras_vatis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/vataras_vatis.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Valstybės tarnautojų registras, Valstybės tarnybos valdymo informacinė sistema

Šių informacinių sistemų tikslas – vykdyti žmogiškųjų išteklių valdymo viešajame administravime, valstybės tarnybos valdymo sprendimų planavimo, Valstybės tarnybos įstatymo ir su juo susijusių teisės aktų įgyvendinimo kontrolės procedūras. Šios esybės (VATARAS ir VATIS) praktikoje yra laikomi viena sistema.

- **Namespace:** `datasets/gov/ird/vataras_vatis`[^manifest]
- **Manifest CSV:** [datasets/gov/ird/vataras_vatis.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/vataras_vatis.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/vataras_vatis`
- **Parent Namespace (`ns`):** Informatikos ir ryšių departamentas (`datasets/gov/ird`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [DarboSkelbimas](vataras_vatis/DarboSkelbimas.md) | Aktualūs darbo skelbimai viešajame sektoriuje | `4` | `id` | — | 16 | Valstybės tarnybos portale viešinami konkursai bei atrankos į valstybės ir savivaldybių institucijų bei įstaigų laisvas darbo pozicijas. |
| [PareigybesStatistika](vataras_vatis/PareigybesStatistika.md) | Nestatutinių valstybės tarnautojų pareigybių statistika | `3` | `jar_kodas` | — | 6 | Aktuali nestatutinių valstybės tarnautojų pareigybių statistika pagal Valstybės ir savivaldybių institucijas bei įstaigas. |
| [ValstybineIstaiga](vataras_vatis/ValstybineIstaiga.md) | Valstybės ir savivaldybių institucijos bei įstaigos, jų pavaldumas | `4` | `id` | — | 11 | Aktualus ir išsamus valstybės ir savivaldybių institucijų bei įstaigų sąrašas, šių įstaigų pavaldumas viena kitai. |

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/vataras_vatis.csv
