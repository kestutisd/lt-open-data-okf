---
type: Dataset
title: "Elektroninis archyvas"
description: "Lietuvos vyriausiojo archyvaro tarnybos (LVAT) Elektroninio archyvo informacinėje sistemoje (EAIS) centralizuotai valdomi su Nacionaliniu dokumentų fondu (NDF) susiję dokumentai ir duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lvat/elektroninis_archyvas"
tags: [gov, lvat, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lvat/elektroninis_archyvas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lvat/elektroninis_archyvas.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Elektroninis archyvas

Lietuvos vyriausiojo archyvaro tarnybos (LVAT) Elektroninio archyvo informacinėje sistemoje (EAIS) centralizuotai valdomi su Nacionaliniu dokumentų fondu (NDF) susiję dokumentai ir duomenys. NDF sudaro valstybės ir savivaldybių institucijų, įstaigų ir įmonių, valstybės įgaliotų asmenų veiklos dokumentai, Lietuvoje įvairiais istorijos laikotarpiais veikusių valstybinių įstaigų ir įmonių veiklos dokumentai, taip pat valstybės archyvuose saugomi dokumentai ir valstybės dokumentiniam paveldui reikšmingi valstybės registrų, žinybinių registrų ir valstybės informacinių sistemų duomenys. Šiame rinkinyje pateikiama tik dalis LVAT EAIS duomenų – fondai ir juose esančių bylų apyrašai. Šie duomenys atitinka NDF aprašus, randamus per LVAT EAIS skaitmeninės skaityklos paiešką adresu <https://eais.archyvai.lt/repo-ext/search>, kur pagal bylos apyrašą galima rasti jam priskirtus apskaitos vienetus (bylas); apskaitos vienetas apima vieną ar kelis dokumentus, kurių dalį galima pasiekti minėtoje LVAT EAIS skaitmeninėje skaitykloje. Seniausi dokumentai siekia XIII a. Rinkinį planuojama atnaujinti kas mėnesį. Duomenų teikėjas – Lietuvos vyriausiojo archyvaro tarnyba.

- **Namespace:** `datasets/gov/lvat/elektroninis_archyvas`[^manifest]
- **Manifest CSV:** [datasets/gov/lvat/elektroninis_archyvas.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lvat/elektroninis_archyvas.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lvat/elektroninis_archyvas`
- **Parent Namespace (`ns`):** Lietuvos vyriausiojo archyvaro tarnyba (`datasets/gov/lvat`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Fondas](elektroninis_archyvas/Fondas.md) | Fondai | `4` | `fondo_id` | — | 15 | Šioje rinkinio lentelėje vienos eilutės objektas yra fondas – hierarchiškai aukščiausia numeruojama archyvinių dokumentų struktūra. |
| [Apyrasas](elektroninis_archyvas/Apyrasas.md) | Apyrašai | `4` | `apyraso_id` | — | 11 | Šioje rinkinio lentelėje vienos eilutės objektas yra bylos apyrašas – hierarchiškai žemesnė numeruojama archyvinių dokumentų struktūra nei fondas, bet... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lvat/elektroninis_archyvas.csv
