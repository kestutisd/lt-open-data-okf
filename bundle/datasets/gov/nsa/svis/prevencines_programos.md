---
type: Dataset
title: "Prevencinių programų vykdymas švietimo įstaigose"
description: "Spinta dataset datasets/gov/nsa/svis/prevencines_programos (2 tables)."
resource: "https://get.data.gov.lt/datasets/gov/nsa/svis/prevencines_programos"
tags: [gov, nsa, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nsa/svis/prevencines_programos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/svis/prevencines_programos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Prevencinių programų vykdymas švietimo įstaigose

- **Namespace:** `datasets/gov/nsa/svis/prevencines_programos`[^manifest]
- **Manifest CSV:** [datasets/gov/nsa/svis/prevencines_programos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/svis/prevencines_programos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/svis/prevencines_programos`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SveikatingumoUgdymas](prevencines_programos/SveikatingumoUgdymas.md) | Sveikatos, lytiškumo ugdymo ir rengimo šeimai bendrosios programos bei kenksmingų ir psichiką veikiančių medžiagų prevencijos programos vykdymas švietimo įstaigose | `4` | `vda_prime_key` | — | 16 | Viena eilutė atitinka programos įvykdymą švietimo įstaigoje atitinkamais mokslo metais. |
| [PatyciuPrevencija](prevencines_programos/PatyciuPrevencija.md) | Smurto ir patyčių prevencijos programų vykdymas švietimo įstaigose. | `4` | `vda_prime_key` | — | 16 | Viena eilutė atitinka faktą ar programa buvo įvykdyta švietimo įstaigoje atitinkamais mokslo metais. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/svis/prevencines_programos.csv
