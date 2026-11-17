---
type: Dataset
title: "Vilniaus miesto istoriniai duomenys - Vilniaus DNR"
description: "Duomenų rinkinys apie Vilniaus istorinius objektus – žemėlapius, nuotraukas, gatves, skulptūras, atminimo lentas, asmenybes ir jų tarpusavio ryšius."
resource: "https://get.data.gov.lt/datasets/gov/id_vilnius/vilniaus_dnr"
tags: [gov, id_vilnius, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/id_vilnius/vilniaus_dnr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Vilniaus miesto istoriniai duomenys - Vilniaus DNR

Duomenų rinkinys apie Vilniaus istorinius objektus – žemėlapius, nuotraukas, gatves, skulptūras, atminimo lentas, asmenybes ir jų tarpusavio ryšius. Duomenys yra naudojami bendrovės „ID Vilnius“ portale „Vilniaus DNR“ (https://zemelapiai.vplanas.lt/vilniausdnr/lt). Duomenų rinkinį sudaro devynios lentelės:

1. Mieste įamžintos asmenybės;

2. Gatvės pavadintos asmenybių vardais;

3. Vilniuje įamžintų asmenybių tarpusavio ryšiai;

4. Skulptūros ir atminimo lentos;

5. Vilniaus gatvės ir istoriniai jų pavadinimai;

6. Vilniaus miesto žemėlapiai;

7. Vilniaus miesto žemėlapių nuorodos į istorines gatves;

8. Vilniaus miesto istoriniai įvykiai;

9. Vilniaus miesto nuotraukos.

Duomenų teikėjas – „ID Vilnius“

Duomenys kaupiami nuo 2021 sausio 1 d.

- **Namespace:** `datasets/gov/id_vilnius/vilniaus_dnr`[^manifest]
- **Manifest CSV:** [datasets/gov/id_vilnius/vilniaus_dnr.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/id_vilnius/vilniaus_dnr`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Asmenybe](vilniaus_dnr/Asmenybe.md) | Mieste įamžintos asmenybės | `4` | `asmenybes_id` | — | 26 | Duomenys iš „ID Vilnius“ apie asmenybes, kurioms Vilniaus mieste įrengtos atminimo lentos, skulptūros, paminklai ar jų vardais pavadintos gatvės. |
| [AsmenybeGatve](vilniaus_dnr/AsmenybeGatve.md) | Gatvės pavadintos asmenybių vardais | `4` | `vda_prime_key` | — | 4 | Duomenys iš „ID Vilnius“ apie gatves, kurioms suteikti asmenybių vardų pavadinimai. |
| [AsmenybeRysys](vilniaus_dnr/AsmenybeRysys.md) | Vilniuje įamžintų asmenybių tarpusavio ryšiai | `4` | `rysio_id` | — | 5 | Duomenys iš „ID Vilnius“ apie Vilniuje įamžintų asmenybių tarpusavio ryšius. |
| [AtminimoObjektas](vilniaus_dnr/AtminimoObjektas.md) | Skulptūros ir atminimo lentos | `4` | `objekto_id` | `open` | 15 | Duomenys iš „ID Vilnius“ apie Vilniaus mieste esančias atminimo lentas, skulptūras, kitus meninius ar mažosios architektūros objektus bei programos „Kuriu... |
| [Gatve](vilniaus_dnr/Gatve.md) | Vilniaus gatvės ir istoriniai jų pavadinimai | `4` | `vda_prime_key` | — | 11 | Duomenys iš „ID Vilnius“ apie Vilniaus miesto gatves ir kai kurių gatvių istorinius pavadinimus. |
| [Zemelapis](vilniaus_dnr/Zemelapis.md) | Vilniaus miesto žemėlapiai | `4` | `zemelapio_id` | — | 13 | Duomenys iš „ID Vilnius“ apie Vilniaus miesto planus, žemėlapius, ortografines nuotraukas ir kitą kartografinę medžiagą. |
| [ZemelapisRysys](vilniaus_dnr/ZemelapisRysys.md) | Vilniaus miesto žemėlapių nuorodos į istorines gatves | `4` | `vda_prime_key` | — | 3 | Duomenys iš „ID Vilnius“ apie žemėlapių ir istorinių gatvių ryšius. |
| [IstorinisIvykis](vilniaus_dnr/IstorinisIvykis.md) | Vilniaus miesto istoriniai įvykiai | `4` | `ivykio_id` | — | 7 | Duomenys iš „ID Vilnius“ apie svarbiausius Vilniaus miesto istorinius įvykius. |
| [Nuotrauka](vilniaus_dnr/Nuotrauka.md) | Vilniaus miesto nuotraukos | `4` | `nuotraukos_id` | — | 12 | Duomenys iš „ID Vilnius“ apie istorines Vilniaus miesto fotografijas ir atvirutes. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/id_vilnius/vilniaus_dnr.csv
