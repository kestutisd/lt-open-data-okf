---
type: Dataset
title: "Nacionalinės miškų inventorizacijos matavimų duomenys"
description: "Rinkinyje pateikiami Valstybinės miškų tarnybos vykdomos Lietuvos nacionalinės miškų inventorizacijos (NMI) duomenys nuo 1998 m. iki dabar."
resource: "https://get.data.gov.lt/datasets/gov/vmt/inventorizacija"
tags: [gov, vmt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmt/inventorizacija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmt/inventorizacija.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Nacionalinės miškų inventorizacijos matavimų duomenys

Rinkinyje pateikiami Valstybinės miškų tarnybos vykdomos Lietuvos nacionalinės miškų inventorizacijos (NMI) duomenys nuo 1998 m. iki dabar. Nacionalinė miškų inventorizacija Miškų įstatyme apibrėžiama kaip valstybinė miškų inventorizacija atrankos metodu (https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/TAIS.417889?jfwid=zzkff5ewj). Inventorizacija suteikia galimybę stebėti miškų būklę ir jų kaitos rodiklius šalies ir administracinių vienetų ar jų junginių (apskričių, rajonų grupių) lygmeniu. Ši visų Lietuvos miškų inventorizacija vykdoma pagal statistiniais metodais pagrįstą atrankos schemą, naudojant apskaitos barelių tinklą. Ši inventorizacija leidžia sekti miškų būklę ir jų kaitos rodiklius šalies ir administracinių vienetų ar jų junginių (apskričių, rajonų grupių) lygmenyje. Lietuvos Respublikos teritorijoje yra išskirti 16 349 nuolatiniai apskaitos bareliai, kurie kas penkerius metus permatuojami. Barelis – miško apskaitos vienetas, apimantis 500 m², arba 400 ha miško plotą.

Daugiau informacijos apie miškų inventorizaciją – https://amvmt.lrv.lt/lt/veiklos-sritys/nacionaline-misku-inventorizacija/.

Duomenų teikėjas – Valstybinė miškų tarnyba.

- **Namespace:** `datasets/gov/vmt/inventorizacija`[^manifest]
- **Manifest CSV:** [datasets/gov/vmt/inventorizacija.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmt/inventorizacija.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmt/inventorizacija`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [BarelioMatavimas](inventorizacija/BarelioMatavimas.md) | Barelių matavimai | `4` | `vda_id` | — | 8 | Lentelėje skelbiami barelių matavimų duomenys. |
| [MedzioMatavimas](inventorizacija/MedzioMatavimas.md) | Medžių matavimai | `4` | `matavimo_id` | — | 38 | Lentelėje skelbiami medžių matavimų duomenys. |
| [PomiskioMatavimas](inventorizacija/PomiskioMatavimas.md) | Pomiškių matavimai | `4` | `matavimo_id` | — | 21 | Lentelėje skelbiami pomiškių matavimų duomenys. |
| [TrakoMatavimas](inventorizacija/TrakoMatavimas.md) | Trakų matavimai | `4` | `matavimo_id` | — | 13 | Lentelėje skelbiami trakų matavimų duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmt/inventorizacija.csv
