---
type: Table
title: "Persalimas — Kvėpavimo takų infekcijų dažnis dienos tikslumu"
description: "\"Kvėpavimo takų infekcijų diagnozių dinamika: TLK-10-AM kodų, nurodytų ESPBI IS E025 dokumente (“Ambulatorinio apsilankymo aprašymas”), dažnis pagal apsilankymo dieną, lytį ir paciento gyvenamosios vietos savivaldybę."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/diagnozes/Persalimas"
tags: [gov, lsd, persalimas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L31"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L31"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2843/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/diagnozes"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Persalimas — Kvėpavimo takų infekcijų dažnis dienos tikslumu

"Kvėpavimo takų infekcijų diagnozių dinamika: TLK-10-AM kodų, nurodytų ESPBI IS E025 dokumente (“Ambulatorinio apsilankymo aprašymas”), dažnis pagal apsilankymo dieną, lytį ir paciento gyvenamosios vietos savivaldybę. Pateikti tik kodai, susiję su kvėpavimo takų infekcijomis (tam tikri J ir U blokai). Nurodytas skaičius unikalių asmenų, kuriems ataskaitinę dieną "E025 dokumente diagnozės laukelyje buvo bent kartą įrašytas nurodytos diagnozių grupės TLK kodas, ir skaičius asmenų, kuriems ši diagnozė "nauja" (t.y. nebuvo įrašyta per 30 praėjusių dienų).[^manifest]

- **Model:** `datasets/gov/lsd/sveikata/diagnozes/Persalimas`[^manifest]
- **Dataset:** [Diagnozių dažnis](../diagnozes.md) (`datasets/gov/lsd/sveikata/diagnozes`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L31](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L31)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/diagnozes/Persalimas` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus kodas | — |
| `data` | `date` | `D` | `4` | `open` | — | Diagnozės data | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | "Savivaldybė, kurioje asmuo deklaravęs gyvenamąją vietą kai nustatyta diagnozė" | "Apie 20 tūkst. atvejų, kurių savivaldybė nenurodyta, sudaro užsienyje nuolat gyvenantys arba išvykę" |
| `diagnoze` | `string` | — | `4` | `open` | — | Diagnozių grupė | — |
| `bendras_diagnoziu_kiekis` | `integer` | `U` | `4` | `open` | — | "Unikalių asmenų skaičius, kuriems nustatyta diagnozė" | "Jeigu asmeniui tą pačią dieną kelis kartus nustatoma ta pati diagnozė, nėra skaičiuojamas kaip atskiras atvejis" |
| `naujai_nustatytos_diagnozes` | `integer` | `U` | `4` | `open` | — | "Unikalių asmenų skaičius, kuriems nustatyta diagnozė pirmą kartą per praėjusias 30 d." | "Kiekvieną dieną skaičiuojama suma asmenų, kuriems nebuvo tos diagnozės per praėjusias 30 dienų" |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `diagnoze` | `"ŪVKTI"` | — | — | "TLK kodai - J00, J01, J02, J03, J04, J05, J06" | — |
| `diagnoze` | `"COVID-19"` | — | — | "TLK kodai - U07.1, U07.2" | — |
| `diagnoze` | `"Gripas ir pneumonija"` | — | — | "TLK kodai - J09, J10, J11, J12, J13, J14, J14, J15, J16, J17, J18" | — |
| `diagnoze` | `"Bronchitas ir kitos infekcijos"` | — | — | "TLK kodai - J20, J21, J22" | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L31 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L31)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/diagnozes (https://data.gov.lt/datasets/2843/)
