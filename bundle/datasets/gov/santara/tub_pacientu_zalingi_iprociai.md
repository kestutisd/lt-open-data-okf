---
type: Dataset
title: "Pacientų, kuriems diagnozuota tuberkuliozė, žalingi įpročiai."
description: "Lentelėje pateikti Tuberkuliozės valstybės informacinės sistemos (TVIS) duomenys apie tuberkuliozės liga diagnozuotus pacientus, jų žalingus įpročius, diagnozes ir mirtis."
resource: "https://get.data.gov.lt/datasets/gov/santara/tub_pacientu_zalingi_iprociai"
tags: [gov, santara, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/santara/tub_pacientu_zalingi_iprociai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/santara/tub_pacientu_zalingi_iprociai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pacientų, kuriems diagnozuota tuberkuliozė, žalingi įpročiai.

Lentelėje pateikti Tuberkuliozės valstybės informacinės sistemos (TVIS) duomenys apie tuberkuliozės liga diagnozuotus pacientus, jų žalingus įpročius, diagnozes ir mirtis. Duomenų valdytojas - Nacionalinio visuomenės sveikatos centro prie Sveikatos apsaugos ministerijos (NVSC). Duomenų tvarkytojas - Vilniaus universiteto ligoninė Santaros klinikos (VULSK). Viena duomenų rinkinio eilutė atspindi vieną pacientą kuriam buvo diagnozuota tuberkuliozės liga. Duomenys apima visos Lietuvos tuberkuliozės liga sirgusius bei sergančius asmenis ir informacinėje sistemoje yra kaupiami nuo 2013 m. Atkreipiame dėmesį, kad paciento identifikacinis kodas nebūtinai reiškia unikalų paciento įrašą - vienas pacientas gali turėti kelis identifikacinius kodus, dėl gyvenamosios vietos pasikeitimo, dėl šios priežasties unikalius pacientų įrašus rekomenduojama nustatyti pagal paciento vardo, pavardės, gimimo datos, asmens kodo ir asmens kodo validacijos stulpelius. Taip pat pažymime kad paciento diagnozė gali kisti, paciento gydymo metu ar atliekant papildomus tyrimus. Be to, Pasaulio sveikatos organizacijos (PSO) tuberkuliozės duomenų kaupimo rekomendacijos keitėsi 1996, 1998, 2000, 2014 metais ir galėjo paveikti duomenų surinkimo metodikas bei surinktų duomenų kokybę.

- **Namespace:** `datasets/gov/santara/tub_pacientu_zalingi_iprociai`[^manifest]
- **Manifest CSV:** [datasets/gov/santara/tub_pacientu_zalingi_iprociai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/santara/tub_pacientu_zalingi_iprociai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/santara/tub_pacientu_zalingi_iprociai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [TubPacientoZalingasIprotis](tub_pacientu_zalingi_iprociai/TubPacientoZalingasIprotis.md) | Pacientų, kuriems diagnozuota tuberkuliozė, žalingi įpročiai. | `4` | `paciento_id` | — | 20 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/santara/tub_pacientu_zalingi_iprociai.csv
