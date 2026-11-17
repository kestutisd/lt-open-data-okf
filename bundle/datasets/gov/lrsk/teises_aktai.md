---
type: Dataset
title: "Teisės aktų registro duomenys"
description: "Rinkinyje pateikiami teisės aktų registro duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/teises_aktai"
tags: [gov, lrsk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lrsk/teises_aktai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/teises_aktai.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Teisės aktų registro duomenys

Rinkinyje pateikiami teisės aktų registro duomenys. Rinkinys susideda iš dviejų modelių: dokumentų ir jų suvestinių. Pateikiami duomenys apie teisės aktų objektus, juos parengusius ir priėmusius subjektus, identifikacinius kodus, objektų rūšis, pavadinimus ir jų chronologijas (teisės akto priėmimo data, registravimo Registre data, paskelbimo data, įsigaliojimo data, pakeitimo ar papildymo data, pripažinimo netekusiu galios data, galiojimo sustabdymo data, galiojimo terminas). Registro objektai yra šie teisės aktai: 1) Lietuvos Respublikos Konstitucija; 2) konstituciniai įstatymai; 3) kiti įstatymai; 4) Lietuvos Respublikos Seimo statutas; 5) Lietuvos Respublikos Seimo (toliau – Seimas) nutarimai; 6) kiti Seimo priimti teisės aktai; 7) Lietuvos Respublikos tarptautinės sutartys; 8) Respublikos Prezidento dekretai ir potvarkiai; 9) Lietuvos Respublikos Vyriausybės (toliau – Vyriausybė) nutarimai, sprendimai ir rezoliucijos; 10) Lietuvos Respublikos Konstitucinio Teismo (toliau – Konstitucinis Teismas) reglamentas; 11) ministrų, Vyriausybės įstaigų, kitų valstybės institucijų ir įstaigų vadovų bei kolegialių institucijų norminiai teisės aktai; 12) Ministro Pirmininko potvarkiai; 13) Seimo Pirmininko potvarkiai; 14) Seimo valdybos sprendimai; 15) Lietuvos banko norminiai teisės aktai; 16) savivaldybių institucijų norminiai teisės aktai, taip pat savivaldybių merų priimami teisės aktai, kuriuos skelbti Registre privaloma pagal teisės aktų reikalavimus; 17) įgaliotų atlikti viešąjį administravimą asociacijų, valstybės ar savivaldybės įmonių, viešųjų įstaigų, kurių savininkė ar dalininkė yra valstybė ar savivaldybė, valdymo organų priimti norminiai teisės aktai. Kitų asociacijų, valstybės ar savivaldybės įmonių, viešųjų įstaigų, kurių savininkė ar dalininkė yra valstybė ar savivaldybė, valdymo organų priimti teisės aktai Registro objektais yra tik tais atvejais, kai šiuos teisės aktus skelbti Registre privaloma pagal teisės aktų reikalavimus; 18) ministrų, Vyriausybės įstaigų, kitų valstybės ir savivaldybių institucijų ir įstaigų vadovų ir kolegialių institucijų, taip pat Lietuvos banko valdybos ar valdybos pirmininko, teisės aktų nustatyta tvarka įgaliotų atlikti viešąjį administravimą asociacijų, valstybės ar savivaldybės įmonių, viešųjų įstaigų, kurių savininkė ar dalininkė yra valstybė ar savivaldybė, valdymo organų priimti teisės taikymo aktai, kuriuos skelbti Registre privaloma pagal teisės aktų reikalavimus; 19) Konstitucinio Teismo nutarimai ir sprendimai dėl Konstitucinio Teismo nutarimo išaiškinimo, taip pat Konstitucinio Teismo pirmininko pranešimai dėl ginčijamo akto galiojimo sustabdymo ir dėl sustabdyto akto galiojimo atnaujinimo; 20) Lietuvos Aukščiausiojo Teismo ir Lietuvos vyriausiojo administracinio teismo sprendimai, nutartys, nutarimai, taip pat įsiteisėję administracinių teismų sprendimai dėl norminių administracinių aktų teisėtumo. Duomenų teikėjas: Lietuvos Respublikos Seimo kanceliarija. 2025-06-13: atverti teisės aktų suvestinių duomenys. Suvestinių tekstus šiuo metu galima pasiekti pagal pateiktą nuorodą. 2026-02-17: atverti teisės aktų priedų duomenys. Pateiktos nuorodos į priedų failus bei ištraukti priedų failų tekstai.

- **Namespace:** `datasets/gov/lrsk/teises_aktai`[^manifest]
- **Manifest CSV:** [datasets/gov/lrsk/teises_aktai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/teises_aktai.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/teises_aktai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Dokumentas](teises_aktai/Dokumentas.md) | Teisės aktų registro duomenys | `4` | `vda_id` | — | 33 | Pateikiami duomenys apie teisės aktų objektus, juos parengusius ir priėmusius subjektus, identifikacinius kodus, objektų rūšis, pavadinimus ir jų... |
| [Suvestine](teises_aktai/Suvestine.md) | Teisės aktų suvestinių duomenys | `4` | `vda_id` | — | 8 | Pateikiami duomenys apie teisės aktų suvestines. |
| [Priedas](teises_aktai/Priedas.md) | Teisės aktų priedų tekstai | `4` | `priedo_id` | — | 7 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/teises_aktai.csv
