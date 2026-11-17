---
type: Dataset
title: "Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba"
description: "Valstybinės akreditavimo sveikatos priežiūrai veiklos tarnybos duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos"
tags: [gov, vaspvt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba

Valstybinės akreditavimo sveikatos priežiūrai veiklos tarnybos duomenys

- **Namespace:** `datasets/gov/vaspvt/licencijos`[^manifest]
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Isakymas](licencijos/Isakymas.md) | Įsakymai | `4` | `id` | — | 3 | — |
| [Istaiga](licencijos/Istaiga.md) | Sveikatos priežiūros įstaigos | `2` | `spi_id` | — | 8 | — |
| [LicencijosVeiksmas](licencijos/LicencijosVeiksmas.md) | Atlikti veiksmai su licencija | `3` | `id` | — | 5 | — |
| [Licencija](licencijos/Licencija.md) | Licencijos | `4` | `licencijos_id` | — | 12 | — |
| [Filialas](licencijos/Filialas.md) | Sveikatos priežiūros įstaigų filialai | `4` | `vda_prime_key` | — | 7 | — |
| [IstaigosVeiklosAdresas](licencijos/IstaigosVeiklosAdresas.md) | Sveikatos priežiūros įstaigų veiklos adresai | `4` | `spi_veiklos_adreso_id` | — | 5 | — |
| [IstaigosPaslauga](licencijos/IstaigosPaslauga.md) | Sveikatos priežiūros įstaigų paslaugos | `4` | `istaigos_paslaugos_id` | — | 7 | — |
| [IstaigosPaslauguOrganas](licencijos/IstaigosPaslauguOrganas.md) | Sveikatos priežiūros įstaigų paslaugų organai | `3` | `id` | — | 2 | — |
| [IstaigosPaslauguProfilis](licencijos/IstaigosPaslauguProfilis.md) | Sveikatos priežiūros įstaigų paslaugų profiliai | `4` | `id` | — | 3 | — |
| [LaboratorinisTyrimas](licencijos/LaboratorinisTyrimas.md) | Laboratoriniai tyrimai | `3` | `labor_tyrimo_id` | — | 5 | — |
| [VeiklosAdresoPaslauga](licencijos/VeiklosAdresoPaslauga.md) | Veiklos adresų paslaugos | `3` | `veiklos_adreso_paslaugos_id` | — | 5 | — |
| [IstaigosPaslaugosProfilioEtapas](licencijos/IstaigosPaslaugosProfilioEtapas.md) | Sveikatos priežiūros įstaigų paslaugų profilių etapai | `3` | `id` | — | 4 | — |
| [TeisineForma](licencijos/TeisineForma.md) | — | `1` | `teisines_formos_id` | — | 2 | — |
| [PaslauguNustatymas](licencijos/PaslauguNustatymas.md) | — | `3` | `paslaugos_nustatymo_id` | — | 6 | — |
| [PaslauguProfilis](licencijos/PaslauguProfilis.md) | — | `4` | `id` | — | 3 | — |
| [Eminys](licencijos/Eminys.md) | — | `4` | `eminio_id` | — | 2 | — |
| [Analite](licencijos/Analite.md) | — | `4` | `analites_id` | — | 2 | — |
| [Tyrimas](licencijos/Tyrimas.md) | — | `4` | `tyrimo_id` | — | 2 | — |
| [Paslauga](licencijos/Paslauga.md) | — | `4` | `paslaugos_id` | — | 2 | — |
| [PaslauguLygis](licencijos/PaslauguLygis.md) | — | `4` | `paslaugu_lygio_id` | — | 2 | — |
| [PaslauguGrupe](licencijos/PaslauguGrupe.md) | — | `4` | `paslaugu_grupes_id` | — | 2 | — |
| [PaslauguProfiliuEtapas](licencijos/PaslauguProfiliuEtapas.md) | — | `4` | `id` | — | 3 | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv
