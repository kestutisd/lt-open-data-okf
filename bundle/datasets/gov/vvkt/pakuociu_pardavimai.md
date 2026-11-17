---
type: Dataset
title: "Vaistinių preparatų pakuočių pardavimai"
description: "Duomenų rinkinyje pateikiami Valstybinės vaistų kontrolės tarnybos (VVKT) duomenys apie mėnesinius vaistinių preparatų pakuočių pardavimus vaistinėse, asmens sveikatos priežiūros įstaigose, mažmenoje ir pavieniams asmenims."
resource: "https://get.data.gov.lt/datasets/gov/vvkt/pakuociu_pardavimai"
tags: [gov, vvkt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkt/pakuociu_pardavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/pakuociu_pardavimai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Vaistinių preparatų pakuočių pardavimai

Duomenų rinkinyje pateikiami Valstybinės vaistų kontrolės tarnybos (VVKT) duomenys apie mėnesinius vaistinių preparatų pakuočių pardavimus vaistinėse, asmens sveikatos priežiūros įstaigose, mažmenoje ir pavieniams asmenims. Lentelėje pateikiami nuo 2017 m. kaupiami duomenys. Kiekviena eilutė nurodo, kiek konkrečios vaistų pakuotės vienetų buvo parduota atitinkamą mėnesį.

Taip pat nurodoma papildoma informacija apie pakuotę: bendrinis vaisto pavadinimas, stiprumas, farmacinė forma, pakuotės aprašymas, pakuotės pirminis ir antrinis dydis bei jų matavimo vienetai, vaistinio preparato pakuotės pardavimo vietos tipas ir pardavimų skaičių vienetais.

Duomenų teikėjas – Valstybinė vaistų kontrolės tarnyba.

- **Namespace:** `datasets/gov/vvkt/pakuociu_pardavimai`[^manifest]
- **Manifest CSV:** [datasets/gov/vvkt/pakuociu_pardavimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/pakuociu_pardavimai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkt/pakuociu_pardavimai`
- **Parent Namespace (`ns`):** Valstybinė vaistų kontrolės tarnyba (`datasets/gov/vvkt`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [ParduotaPakuote](pakuociu_pardavimai/ParduotaPakuote.md) | Vaistinių preparatų pakuočių pardavimai | `4` | `vda_prime_key` | — | 14 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkt/pakuociu_pardavimai.csv
