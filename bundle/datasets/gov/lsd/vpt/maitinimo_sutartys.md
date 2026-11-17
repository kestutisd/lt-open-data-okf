---
type: Dataset
title: "Ugdymo įstaigų maitinimo sutarčių duomenys"
description: "Rinkinyje pateikiami Viešųjų pirkimų tarnybos (VPT) Viešųjų pirkimų monitoringo informacinės sistemos Lietuvos bendrojo ugdymo įstaigų maitinimo sutarčių, viešinamų Viešųjų pirkimų portale, duomenys nuo 2008 m. Nurodomi išsamūs..."
resource: "https://get.data.gov.lt/datasets/gov/lsd/vpt/maitinimo_sutartys"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/vpt/maitinimo_sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/maitinimo_sutartys.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Ugdymo įstaigų maitinimo sutarčių duomenys

Rinkinyje pateikiami Viešųjų pirkimų tarnybos (VPT) Viešųjų pirkimų monitoringo informacinės sistemos Lietuvos bendrojo ugdymo įstaigų maitinimo sutarčių, viešinamų Viešųjų pirkimų portale, duomenys nuo 2008 m. Nurodomi išsamūs maitinimo sutarčių duomenys (galiojimo laikotarpis, sutarties vertė, duomenys apie perkančiąją organizaciją ir konkursą laimėjusį tiekėją). Pažymėtina, kad maitinimo paslaugų konkursą gali organizuoti ne tik mokykla, bet ir mokyklos savininkė – savivaldybės administracija. Tokiu atveju prie perkančiosios organizacijos nurodomas maitinimo konkursą organizavusios savivaldybės administracijos pavadinimas.

2025 m. pabaigoje bendro Viešųjų pirkimų tarnybos ir Valstybės duomenų agentūros projekto metu, pasitelkiant dirbtinio intelekto (DI) modelį, buvo analizuojamos galiojančios ugdymo įstaigų maitinimo sutartys. DI modelis identifikavo duomenis apie maitinimo organizavimą (ar tiekiamas ekologiškas maistas, ar už maistą galima atsiskaityti elektroninėje maitinimo užsakymų ir atsiskaitymo sistemoje (EMUAS), ar maitinimas valgyklose organizuojamas savitarnos principu) ir sutartyse nurodytus patiekalus bei jų požymius (kaina, maitinimo laikas, moksleivių amžiaus grupė, kuriai skirtas patiekalas). Atkreipiame dėmesį, jog DI modelio identifikuotų duomenų tikslumas nėra garantuojamas. Šie duomenys atnaujinami nebus.

Duomenų teikėjas – Viešųjų pirkimų tarnyba

- **Namespace:** `datasets/gov/lsd/vpt/maitinimo_sutartys`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/vpt/maitinimo_sutartys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/maitinimo_sutartys.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/vpt/maitinimo_sutartys`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Sutartis](maitinimo_sutartys/Sutartis.md) | Bendrojo ugdymo įstaigų maitinimo paslaugų viešųjų pirkimų sutarčių duomenys | `4` | `sutarties_id` | `open` | 25 | — |
| [Kaina](maitinimo_sutartys/Kaina.md) | Ugdymo įstaigų maitinimo sutartyse nurodytų patiekalų kainoraštis | `4` | `vda_id` | `open` | 25 | Pateikiami ugdymo įstaigų maitinimo sutarčių kainos ir kiti maitinimo požymiai, dirbtinio intelekto (DI) modelio pagalba surinktos iš sutarčių tekstų |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/vpt/maitinimo_sutartys.csv
