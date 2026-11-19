---
type: Table
title: "Doze — Apšvitą patiriančių darbuotojų gautos metinės apšvitos dozės"
description: "Spinta table datasets/gov/rsc/apsvitos_dozes/Doze (13 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rsc/apsvitos_dozes/Doze"
tags: [gov, rsc, doze, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsc/apsvitos_dozes.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rsc/apsvitos_dozes.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2188/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rsc/apsvitos_dozes"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Doze — Apšvitą patiriančių darbuotojų gautos metinės apšvitos dozės

- **Model:** `datasets/gov/rsc/apsvitos_dozes/Doze`[^manifest]
- **Dataset:** [Apšvitą patiriančių darbuotojų gautos metinės apšvitos dozės](../apsvitos_dozes.md) (`datasets/gov/rsc/apsvitos_dozes`)[^manifest]
- **Manifest CSV:** [datasets/gov/rsc/apsvitos_dozes.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsc/apsvitos_dozes.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rsc/apsvitos_dozes/Doze` (`deployed`)[^manifest]
- **Provider:** `rsc` — Radiacinės saugos centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `matavimo_metai` | `integer` | — | `4` | `open` | — | Apšvitos dozės matavimo metai | — |
| `idarbinimo_pradzia` | `integer` | — | `4` | `open` | — | Metai, kuriais pradėta dirbti atitinkamoje darbovietėje | — |
| `idarbinimo_pabaiga` | `integer` | — | `4` | `open` | — | Metai, kuriais baigta dirbti atitinkamoje darbovietėje | — |
| `darbuotojo_id` | `string` | — | `4` | `open` | — | Darbuotojo identifikatorius | — |
| `darbovietes_id` | `string` | — | `4` | `open` | — | Darbovietės identifikatorius | — |
| `lytis` | `string` | — | `4` | `open` | — | Darbuotojo lytis | — |
| `gimimo_metai` | `integer` | — | `4` | `open` | — | Darbuotojo gimimo metai | — |
| `bendra_doze` | `number` | `mSv` | `4` | `open` | — | Bendra darbuotojo apšvitos dozė atitinkamoje darbovietėje | Norint gauti darbuotojo bendrą metinę dozę reikia susumuoti visas bendras dozes gautas skirtingose darbovietėse. |
| `akiu_doze` | `number` | `mSv` | `4` | `open` | — | Darbuotojo akių apšvitos dozė atitinkamoje darbovietėje | Null reikšmės - gauta akių apšvitos dozė nebuvo matuota |
| `galuniu_doze` | `number` | `mSv` | `4` | `open` | — | Darbuotojo galūnių apšvitos dozė atitinkamoje darbovietėje | Null reikšmės - gauta galūnių apšvitos dozė nebuvo matuota |
| `pareigu_gr` | `string` | — | `4` | `open` | — | Pareigų grupės pavadinimas | — |
| `sritis` | `string` | — | `4` | `open` | — | Darbuotojo padalinio veiklos srities pavadinimas | — |
| `salis` | `string` | — | `4` | `open` | — | Juridinio asmens šalis | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"1"` | — | — | Vyras | — |
| `lytis` | `"2"` | — | — | Moteris | — |
| `pareigu_gr` | `"Gydytojai"` | — | — | Gydytojai | — |
| `pareigu_gr` | `"Slaugytojai"` | — | — | Slaugytojai | — |
| `pareigu_gr` | `"Technologai"` | — | — | Technologai | — |
| `pareigu_gr` | `"Kitas medicinos personalas"` | — | — | Kitas medicinos personalas | — |
| `pareigu_gr` | `"Pagalbinis medicinos personalas"` | — | — | Pagalbinis medicinos personalas | — |
| `pareigu_gr` | `"Techninis medicinos personalas"` | — | — | Techninis medicinos personalas | — |
| `pareigu_gr` | `"Specialistai"` | — | — | Specialistai | — |
| `pareigu_gr` | `"Darbininkai"` | — | — | Darbininkai | — |
| `pareigu_gr` | `"Vadovai"` | — | — | Vadovai | — |
| `pareigu_gr` | `"Kiti"` | — | — | Kiti | — |
| `pareigu_gr` | `"Jaunesnieji specialistai"` | — | — | Jaunesnieji specialistai | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `matavimo_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `idarbinimo_pradzia` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `idarbinimo_pabaiga` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rsc/apsvitos_dozes.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsc/apsvitos_dozes.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rsc/apsvitos_dozes (https://data.gov.lt/datasets/2188/)
