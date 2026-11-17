---
type: Table
title: "Elementas — Lentelėje pateikti valstybės strategijų, programų elementų hierarchijos duomenys iš Lietuvos Respublikos finansų ministerijos Stebėsenos informacinė sistema (SIS)."
description: "Spinta table datasets/gov/finmin/sis/Elementas (16 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sis/Elementas"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sis/finmin.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sis/finmin.csv#L18"
    last_modified: "2026-11-11T14:39:20Z"
---

# Elementas — Lentelėje pateikti valstybės strategijų, programų elementų hierarchijos duomenys iš Lietuvos Respublikos finansų ministerijos Stebėsenos informacinė sistema (SIS).

- **Model:** `datasets/gov/finmin/sis/Elementas`[^manifest]
- **Dataset:** [datasets/gov/finmin/sis](../sis.md) (`datasets/gov/finmin/sis`)
- **Manifest CSV:** [datasets/gov/finmin/sis/finmin.csv#L18](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sis/finmin.csv#L18)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sis/Elementas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `doc_id` | `string` | — | `4` | `open` | — | Dokumento kodas, atvaizduojamas ataskaitose. | — |
| `obj_id` | `string` | — | `4` | `open` | — | Žemesnio lygmens objektas (objektas-vaikas). Nuoroda į OBJECTS. OBJ_ID. | — |
| `tevinis_obj_id` | `string` | — | `4` | `open` | — | Aukštesnio lygmens objektas (objektas-tėvas). NULL pirmame hierarchijos objektų lygyje. Nuoroda į OBJECTS. OBJ_ID. | — |
| `obj_code` | `string` | — | `4` | `open` | — | Objekto kodas, identifikuojantis įrašą. | — |
| `tipas` | `string` | — | `4` | `open` | — | Elemento tipo pavadinimas vienaskaita. | — |
| `klase` | `string` | — | `4` | `open` | — | Požymis, nusakantis objekto klasę: Element - įprasti elementai, Criterion - kriterijai, Risk - rizikos, Job - darbai, Real estate - NT objektai, Folder - dokumento elementų aplankas, Indicator - rodikliai, Folder for indicators - rodiklių grupė (aplankas), Scope - rodiklių analizės sritis. | — |
| `eil_nr` | `number` | — | `4` | `open` | — | Eilės numeris (objekto prioritetas, objekto atvaizdavimo hierarchijoje pozicija). | — |
| `kodas` | `string` | — | `4` | `open` | — | Objekto kodas, atvaizduojamas ataskaitose. Kodas generuojamas automatiškai, atsižvelgiant į kodo generavimo taisykles. | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Objekto pavadinimas (vystomos versijos). | — |
| `aprasymas` | `string` | — | `4` | `open` | — | Vertinimo kriterijaus skaičiavimo specifikacija. Paaiškinama, kas vertinimo kriterijumi vertinama, jeigu tai nėra akivaizdu iš kriterijaus formuluotės. Pateikiami vertinimo kriterijaus formuluotės specifinių terminų apibrėžimai. | — |
| `elemento_pradzia` | `date` | `D` | `4` | `open` | — | Dokumento elemento pradžios data | — |
| `elemento_pabaiga` | `date` | `D` | `4` | `open` | — | Dokumento elemento pabaigos data | — |
| `periodas` | `string` | — | `4` | `open` | — | Periodiškumo pavadinimas. | — |
| `pozymis` | `string` | — | `4` | `open` | — | Kriterijaus faktinių/siektinų reikšmių pateikimo kontekstas (vystomos versijos). Galimos reikšmės: COUNTRY - reikšmės pateikiamos šalies lygyje, ORGANIZATION - reikšmės pateikia elemento vykdytojai, DOCUMENT_OWNER - reikšmės pateikia dokumento savininkas. | — |
| `matavimo_vnt` | `string` | — | `4` | `open` | — | Matavimo vieneto pavadinimas. | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sis/finmin.csv
