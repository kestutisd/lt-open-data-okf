---
type: Dataset
title: "Privačių interesų registro ataskaitos"
description: "Rinkinyje pateikiamos Vyriausiosios tarnybinės etikos komisijos privačių interesų registro veiklos ataskaitos: 1."
resource: "https://get.data.gov.lt/datasets/gov/vtek/pinreg_ataskaitos"
tags: [gov, vtek, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vtek/pinreg_ataskaitos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/pinreg_ataskaitos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Privačių interesų registro ataskaitos

Rinkinyje pateikiamos Vyriausiosios tarnybinės etikos komisijos privačių interesų registro veiklos ataskaitos:

1. Vyriausiosios tarnybinės etikos komisijos (VTEK) priimtų sprendimų statistika. Tirdama pranešimus, skundus ir prašymus dėl deklaruojančių asmenų veiklos atitikimo Viešųjų ir privačių interesų derinimo įstatymui, VTEK nusprendžia pripažinti pažeidimą, pripažinti pažeidimo nebuvimą arba nutraukti tyrimą. Ataskaitoje pateikiami nuo 2006 m. kaupiami šių sprendimų duomenys.

2. Privačių interesų deklaracijų statistika pagal pareigybės pobūdį. Į ataskaitą įtrauktos tik standartinio tipo pareigybės arba ekspertų ataskaitose nurodytų pareigybių pobūdis, kai asmuo teikia deklaraciją dėl einamųjų pareigų ir dėl dalyvavimo viešuosiuose pirkimuose bei turi deklaruoti pareigas. Be to, jei asmuo užima vienodo pobūdžio pareigybes keliose darbovietėse, į statistiką įtraukiamos tik unikalios pobūdžių reikšmės. Ataskaitoje pateikiami nuo 2020 m. kaupiami duomenys.

3. Privačių interesų deklaracijų statistika pagal pateiktas deklaracijas ir deklaruojančius asmenis. Ataskaitoje nurodomi duomenys apie per ataskaitinį laikotarpį pateiktas deklaracijas ir jas teikusius asmenis. Ataskaitoje pateikiami nuo 2012 m. kaupiami duomenys.

Agreguoti duomenys pateikiami kiekvieno mėnesio paskutinę dieną.

Duomenų teikėjas – Vyriausioji tarnybinės etikos komisija.

- **Namespace:** `datasets/gov/vtek/pinreg_ataskaitos`[^manifest]
- **Manifest CSV:** [datasets/gov/vtek/pinreg_ataskaitos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/pinreg_ataskaitos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vtek/pinreg_ataskaitos`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [AsmuoDeklaracija](pinreg_ataskaitos/AsmuoDeklaracija.md) | Privačių interesų deklaracijų statistika pagal pateiktas deklaracijas ir deklaruojančius asmenis | `4` | `vda_id` | — | 4 | Ataskaitoje nurodomi duomenys apie per ataskaitinį laikotarpį pateiktas deklaracijas ir jas teikusius asmenis. |
| [PareigybeDeklaracija](pinreg_ataskaitos/PareigybeDeklaracija.md) | Privačių interesų deklaracijų statistika pagal pareigybės pobūdį | `4` | `vda_id` | — | 4 | Į ataskaitą įtrauktos tik standartinio tipo pareigybės arba ekspertų ataskaitose nurodytų pareigybių pobūdis, kai asmuo teikia deklaraciją dėl einamųjų... |
| [Sprendimas](pinreg_ataskaitos/Sprendimas.md) | Vyriausiosios tarnybinės etikos komisijos (VTEK) priimtų sprendimų statistika | `4` | `vda_id` | — | 6 | Tirdama pranešimus, skundus ir prašymus dėl deklaruojančių asmenų veiklos atitikimo Viešųjų ir privačių interesų derinimo įstatymui, VTEK nusprendžia... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vtek/pinreg_ataskaitos.csv
