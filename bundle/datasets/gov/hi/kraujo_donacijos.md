---
type: Dataset
title: "Kraujo donacijos"
description: "Rinkinyje pateikiami duomenys apie atliktas kraujo donacijas, kurie kaupiami Higienos instituto kraujo donorų registre."
resource: "https://get.data.gov.lt/datasets/gov/hi/kraujo_donacijos"
tags: [gov, hi, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/hi/kraujo_donacijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/kraujo_donacijos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Kraujo donacijos

Rinkinyje pateikiami duomenys apie atliktas kraujo donacijas, kurie kaupiami Higienos instituto kraujo donorų registre. Duomenų rinkinį sudaro trys lentelės:

1. Asmenų, pageidaujančių duoti kraujo arba kraujo komponentus, duomenys (atnaujinama kiekvieną dieną);

2. Sėkmingi kraujo donacijos vizitai (atnaujinama kiekvieną dieną);

3. Nesėkmingi kraujo donacijos vizitai (atnaujinama kiekvienų metų kovo 1 dieną);

4. Mėnesinė kraujo donavimo vizitų statistika (atnaujinama kiekvieno mėnesio 15 dieną).

Duomenų teikėjas – Higienos institutas.

Duomenys kaupiami nuo 2012 m. balandžio 1 d.

- **Namespace:** `datasets/gov/hi/kraujo_donacijos`[^manifest]
- **Manifest CSV:** [datasets/gov/hi/kraujo_donacijos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/kraujo_donacijos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/kraujo_donacijos`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [KraujoDonoras](kraujo_donacijos/KraujoDonoras.md) | Asmenų, pageidaujančių duoti kraujo arba kraujo komponentus, duomenys | `4` | `donoro_id` | — | 13 | Lentelėje pateikiami duomenys apie asmenis, kurie pageidauja duoti kraujo arba kraujo komponentų, surinkti Higienos instituto Kraujo donorų registro... |
| [SekmingaDonoryste](kraujo_donacijos/SekmingaDonoryste.md) | Sėkmingi kraujo donacijos vizitai | — | `vizito_id` | — | 13 | Lentelėje pateikiami sėkmingų kraujo donacijos vizitų duomenys iš Higienos instituto Kraujo donorų registro informacinės sistemos. |
| [NesekmingaDonoryste](kraujo_donacijos/NesekmingaDonoryste.md) | Nesėkmingi kraujo donacijos vizitai | — | `vizito_id` | — | 10 | Nesėkmingų kraujo donacijos vizitų duomenys iš Higienos instituto Kraujo donorų registro informacinės sistemos. |
| [MenesioAtaskaita](kraujo_donacijos/MenesioAtaskaita.md) | Mėnesinė kraujo donavimo vizitų statistika | — | `vda_prime_key` | — | 5 | Mėnesinė kraujo donavimo vizitų statistika iš Higienos instituto Kraujo donorų registro informacinės sistemos. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/kraujo_donacijos.csv
