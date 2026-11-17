---
type: Dataset
title: "Kasmetinės vaikų sveikatos patikros duomenys"
description: "Kaip numato įstatymai, pagal Lietuvos Respublikos bendrojo ugdymo programas darželiuose ir mokyklose besimokantys vaikai iki 18 metų kartą per metus turi pasitikrinti sveikatą."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/mokiniu_sveikata"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/mokiniu_sveikata.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/mokiniu_sveikata.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Kasmetinės vaikų sveikatos patikros duomenys

Kaip numato įstatymai, pagal Lietuvos Respublikos bendrojo ugdymo programas darželiuose ir mokyklose besimokantys vaikai iki 18 metų kartą per metus turi pasitikrinti sveikatą. Vaikų sveikatos patikrinimai leidžia laiku nustatyti sveikatos sutrikimus, ragina keisti gyvenimo būdą ir atsižvelgti į mokinio sveikatos poreikius ugdymo procese. Sveikatos patikra susideda iš dviejų dalių: šeimos, vidaus ligų ar vaikų ligų gydytojas arba slaugytojas įvertina vaiko sveikatą, o gydytojas odontologas, gydytojas odontologas specialistas arba burnos higienistas įvertina dantų ir burnos higienos būklę.

Rinkinyje pateikiami išsamūs Lietuvos bendrojo ugdymo darželių ir mokyklų mokinių sveikatos patikrinimo duomenys nuo 2019m. iki šių dienų. Atvėrime panaudoti duomenys iš ESPBĮ, SVEIDRA informacinių sistemų ir Gyventojų registro. Pažymima, jog rinkinio lentelių duomenys tarpusavyje nesijungia. Rinkinys susideda iš trijų lentelių:

1. Mokinio sveikatos pažymėjimas: I. Sveikatos būklės įvertinimas. Pateikiami E027-1 formos pirmos dalies duomenys. Lentelės objektas - moksleivio sveikatos patikrinimas. Pateikiami duomenys apie tikrinimą atlikusią asmens sveikatos priežiūros įstaigą (ASPĮ), prie kurios prirašytas mokinys, nuasmeninti mokinio asmens ir jo sveikatos duomenys (ūgis, svoris) bei vertinimo išvada.

2. Mokinio sveikatos pažymėjimas: II. Dantų ir žandikaulių būklės įvertinimas. Pateikiami E027-1 formos antros dalies duomenys. Lentelės objektas - moksleivio sveikatos patikrinimas. Pateikiami nuasmeninti mokinio asmens ir jo gyvenamosios vietos duomenys bei patikrinimo metu užfiksuota dantų ir žandikaulio duomenys (pieninių ir nuolatinių dantų būklė ir skaičius).

3. Mokinių sveikatos patikrinimų metu įrašytos diagnozės. Lentelėje skelbiamos sveikatos tikrinimų metu užfiksuotos diagnozės su tarptautinės ligų klasifikacijos (TLK) kodais. Lentelės objektas - tikrinimo metu įrašyta diagnozė.

Duomenų teikėjas: Registrų centras

- **Namespace:** `datasets/gov/lsd/sveikata/mokiniu_sveikata`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/mokiniu_sveikata.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/mokiniu_sveikata.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/mokiniu_sveikata`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Diagnoze](mokiniu_sveikata/Diagnoze.md) | Mokinių sveikatos patikrinimų metu nustatytos diagnozės. Lentelės objektas - mokinio sveikatos tikrinimo metu išrašyta diagnozė. | `4` | `vda_id` | — | 5 | — |
| [SveikatosIvertinimas](mokiniu_sveikata/SveikatosIvertinimas.md) | Sveikatos būklės įvertinimas | `4` | `tikrinimo_id` | `open` | 15 | E027-1 formos pirmos dalies duomenys |
| [DantuIvertinimas](mokiniu_sveikata/DantuIvertinimas.md) | Dantų ir žandikaulių būklės įvertinimas | `4` | `tikrinimo_id` | — | 16 | E027-1 formos antros dalies duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/mokiniu_sveikata.csv
