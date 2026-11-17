---
type: Dataset
title: "Georeferencinio pagrindo kadastro erdviniai duomenys"
description: "Specifikacija - https://e-tar.lt/portal/lt/legalAct/c53d28609d7811eea5a28c81c82193a8"
resource: "https://get.data.gov.lt/datasets/gov/giscentras/grpk"
tags: [gov, giscentras, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/giscentras/grpk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/giscentras/grpk.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Georeferencinio pagrindo kadastro erdviniai duomenys

Specifikacija - https://e-tar.lt/portal/lt/legalAct/c53d28609d7811eea5a28c81c82193a8

- **Namespace:** `datasets/gov/giscentras/grpk`[^manifest]
- **Manifest CSV:** [datasets/gov/giscentras/grpk.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/giscentras/grpk.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/giscentras/grpk`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Kelias](grpk/Kelias.md) | Sluoksnyje saugoma informacija apie kelių ir gatvių ašines linijas | `4` | `top_id` | — | 18 | — |
| [Gelezinkelis](grpk/Gelezinkelis.md) | Sluoksnyje saugoma informacija apie geležinkelio vėžės ašines linijas | `4` | `top_id` | — | 13 | — |
| [HidrografijaLinija](grpk/HidrografijaLinija.md) | Sluoksnyje saugoma informacija apie upių, upelių, kanalų ir melioracijos griovių ašines linijas | `4` | `top_id` | — | 15 | — |
| [Plotas](grpk/Plotas.md) | Sluoksnyje saugoma informacija apie vandens telkinių dengiamas teritorijas | `4` | `top_id` | — | 13 | — |
| [PlotasRiba](grpk/PlotasRiba.md) | Sluoksnyje saugoma informacija apie žemės naudmenų ir vandens telkinių dengiamų teritorijų ribas | `4` | `top_id` | — | 11 | — |
| [Pastatas](grpk/Pastatas.md) | Sluoksnyje saugoma informacija apie aiškiai atpažįstamų pastatų ir statinių dengiamą teritoriją | `4` | `top_id` | — | 11 | — |
| [Bokstas](grpk/Bokstas.md) | Sluoksnyje saugoma informacija apie atskirai stovinčius bokštus ir kaminus, kurie negali būti išreikšti plotu | `4` | `top_id` | — | 8 | — |
| [Aukstis](grpk/Aukstis.md) | Sluoksnyje saugoma informacija apie žemės paviršiaus taškus | `4` | `top_id` | — | 9 | — |
| [Lapas](grpk/Lapas.md) | Sluoksnyje saugoma informacija apie žemėlapio M1:10000 nomenklatūrinio skaitymo lapus LKS-94 koordinačių sistemoje | `4` | `top_id` | — | 13 | — |
| [Riba](grpk/Riba.md) | Sluoksnyje saugoma informacija apie administracines ribas | `4` | `top_id` | — | 10 | — |
| [VietovardisTaskas](grpk/VietovardisTaskas.md) | Sluoksnyje saugoma informacija apie pagrindinius ir pakartotinius vietovių ir kraštovaizdžio objektų pavadinimus ir jų vietas, kai nėra nustatoma konkreti objekto vieta | `4` | `top_id` | — | 13 | — |
| [VietovardisPlotas](grpk/VietovardisPlotas.md) | Sluoksnyje saugoma informacija apie pagrindinius vietovių ir kraštovaizdžio objektų pavadinimus ir jų vietas, kai yra nustatoma objekto teritorija | `4` | `top_id` | — | 11 | — |
| [MiskasRiba](grpk/MiskasRiba.md) | Sluoksnyje saugoma informacija apie miškų kvartalinių linijų ir proskynų ašines linijas, taip pat medžių juostas | `4` | `top_id` | — | 9 | — |
| [PaveldasTaskas](grpk/PaveldasTaskas.md) | Sluoksnyje saugoma informacija apie taškais vaizduojamus išskirtinę kultūrinę vertę turinčius nekilnojamojo kultūros paveldo objektus, kurių sąrašai patvirtinti Lietuvos Respublikos Vyriausybės 2007 m. vasario 7 L. nutarimu Nr. 193 „Dėl Išskirtinę kultūrinę vertę turinčių nekilnojamojo kultūros paveldo objektų ir pastatų ir patalpų, skirtų saugoti ir eksponuoti kilnojamąsias kultūros vertybes, sąrašų patvirtinimo“ | `4` | `top_id` | — | 13 | — |
| [PaveldasPlotas](grpk/PaveldasPlotas.md) | Sluoksnyje saugoma informacija apie plotais vaizduojamus išskirtinę kultūrinę vertę turinčius nekilnojamojo kultūros paveldo objektus, kurių sąrašai patvirtinti Lietuvos Respublikos Vyriausybės 2007 m. vasario 7 L. nutarimu Nr. 193 „Dėl Išskirtinę kultūrinę vertę turinčių nekilnojamojo kultūros paveldo objektų ir pastatų ir patalpų, skirtų saugoti ir eksponuoti kilnojamąsias kultūros vertybes, sąrašų patvirtinimo“ | `4` | `top_id` | — | 15 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/giscentras/grpk.csv
