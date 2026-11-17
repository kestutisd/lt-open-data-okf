---
type: Dataset
title: "Lobistinės veiklos statistiniai duomenys"
description: "Rinkinyje pateikiami Vyriausiosios tarnybinės etikos komisijos (VTEK) Lobistinės veiklos duomenų tvarkymo informacinės sistemos agreguoti duomenys apie registruotus lobistus, lobistų pateiktas skaidrumo deklaracijas ir asmenų, patyrusių..."
resource: "https://get.data.gov.lt/datasets/gov/vtek/ataskaita"
tags: [gov, vtek, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vtek/ataskaitos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/ataskaitos.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Lobistinės veiklos statistiniai duomenys

Rinkinyje pateikiami Vyriausiosios tarnybinės etikos komisijos (VTEK) Lobistinės veiklos duomenų tvarkymo informacinės sistemos agreguoti duomenys apie registruotus lobistus, lobistų pateiktas skaidrumo deklaracijas ir asmenų, patyrusių lobistinę įtaką, pateiktas deklaracijas pamėnesiui. Duomenys pateikiami nuo 2021 m. Pažymėtina, jog lobistais laikomi fiziniai arba juridiniai asmenys, vykdantys lobistinę veiklą. Kaip numatyta Lietuvos Respublikos lobistinės veiklos įstatyme, prisistatydami asmeniui, kuriam siekiama daryti įtaką, lobistai privalo pateikti VTEK išduotą lobisto pažymėjimą, nurodyti lobistinės veiklos užsakovą, naudos gavėją, diskutuojamą teisės akto projektą ir per septynias dienas pateikti skaidrių teisėkūros procesų deklaraciją. Asmenys, kuriems lobistine veikla siekiama daryti įtaką, taip pat privalo per septynias dienas deklaruoti patirtą įtaką dėl kiekvieno teisės akto projekto.

Duomenų teikėjas – Vyriausioji tarnybinės etikos komisija.

- **Namespace:** `datasets/gov/vtek/ataskaita`[^manifest]
- **Manifest CSV:** [datasets/gov/vtek/ataskaitos.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/ataskaitos.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vtek/ataskaita`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Lobistas](ataskaita/Lobistas.md) | Lobistų skaičius pagal asmens tipą | `4` | `vda_id` | — | 5 | Pateikiamos aktyviai veikiančių fizinių ir juridinių asmenų suvestinės. |
| [SkaidrumoDeklaracija](ataskaita/SkaidrumoDeklaracija.md) | Pateiktų lobistų skaidrumo deklaracijų skaičius | `4` | `vda_id` | — | 4 | Pateikiama per mėnesį registruotų lobistų skaidrumo deklaracijų statistika. |
| [ItakosDeklaracija](ataskaita/ItakosDeklaracija.md) | Asmenų, patyrusių lobistinę įtaką, pateiktų deklaracijų skaičius | `4` | `vda_id` | — | 3 | Pateikiama mėnesinė patirtos lobistinės įtakos deklaracijų statistika. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vtek/ataskaitos.csv
