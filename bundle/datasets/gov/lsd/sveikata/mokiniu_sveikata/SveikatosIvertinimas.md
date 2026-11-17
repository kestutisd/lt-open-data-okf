---
type: Table
title: "SveikatosIvertinimas — Sveikatos būklės įvertinimas"
description: "E027-1 formos pirmos dalies duomenys"
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/mokiniu_sveikata/SveikatosIvertinimas"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/mokiniu_sveikata.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/mokiniu_sveikata.csv#L26"
    last_modified: "2026-11-11T14:39:20Z"
---

# SveikatosIvertinimas — Sveikatos būklės įvertinimas

E027-1 formos pirmos dalies duomenys

- **Model:** `datasets/gov/lsd/sveikata/mokiniu_sveikata/SveikatosIvertinimas`[^manifest]
- **Dataset:** [Kasmetinės vaikų sveikatos patikros duomenys](../mokiniu_sveikata.md) (`datasets/gov/lsd/sveikata/mokiniu_sveikata`)
- **Manifest CSV:** [datasets/gov/lsd/sveikata/mokiniu_sveikata.csv#L26](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/mokiniu_sveikata.csv#L26)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/mokiniu_sveikata/SveikatosIvertinimas`
- **Primary Key (`ref`):** `tikrinimo_id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tikrinimo_id` | `string` | — | `4` | `open` | — | Sveikatos tikrinimo vizito identifikatorius | — |
| `istaigos_espbi_id` | `string` | — | `4` | `open` | — | Asmens sveikatos priežiūros įstaigos (ASPĮ), kurioje buvo atliktas sveikatos tikrinimas, identifikatorius Elektroninėje sveikatos paslaugų ir bendradarbiavimo sistemoje (ESPBI) | Esant mažiau nei 10 mokinių, gimusių tais pačiais metais, ir tikrinimo metais atlikusių sveikatos tikrinimą, ASPĮ ESPBI identifikatorius nurodomas "kita". Pažymėtina, jog ASPĮ, kurioje buvo tikrinta mokinio sveikata, nebūtinai yra mokinio pirminės ambulatorinės asmens sveikatos priežiūros įstaiga (PAASPĮ) |
| `jar_kodas` | `string` | — | `4` | `open` | — | Asmens sveikatos priežiūros įstaigos (ASPĮ), kurioje buvo atliktas sveikatos tikrinimas, juridinio asmens kodas | Esant mažiau nei 10 mokinių, gimusių tais pačiais metais, ir tikrinimo metais atlikusių sveikatos tikrinimą, ASPĮ JAR nurodomas "kita". Pažymėtina, jog ASPĮ, kurioje buvo tikrinta mokinio sveikata, nebūtinai yra mokinio pirminės ambulatorinės asmens sveikatos priežiūros įstaiga (PAASPĮ) |
| `istaigos_pavadinimas` | `string` | — | `4` | `open` | — | Asmens sveikatos priežiūros įstaigos (ASPĮ), kurioje buvo atliktas sveikatos tikrinimas, pavadinimas | Esant mažiau nei 10 mokinių, gimusių tais pačiais metais, ir tikrinimo metais atlikusių sveikatos tikrinimą, ASPĮpavadinimas nurodomas "kita". Pažymėtina, jog ASPĮ, kurioje buvo tikrinta mokinio sveikata, nebūtinai yra mokinio pirminės ambulatorinės asmens sveikatos priežiūros įstaiga (PAASPĮ) |
| `istaigos_savivaldybe` | `string` | — | `4` | `open` | — | Asmens sveikatos priežiūros įstaigos (ASPĮ), kurioje buvo atliktas sveikatos tikrinimas, veiklos savivaldybė | — |
| `geometrija_adp` | `geometry(point, 3346)` | — | `4` | `open` | — | Asmens sveikatos priežiūros įstaigos (ASPĮ) koordinatės | — |
| `asmens_id` | `string` | — | `4` | `open` | — | Mokinio asmens identifikatorius | — |
| `gimimo_metai` | `date` | `D` | `4` | `open` | — | Mokinio gimimo metai | — |
| `lytis` | `string` | — | `4` | `open` | — | Mokinio lytis | — |
| `iraso_laikas` | `datetime` | `S` | `4` | `open` | — | Įrašo įvedimo laiko žyma, suapvalinta iki artimiausios valandos | — |
| `duomenu_atnaujinimas` | `datetime` | `S` | `4` | `open` | — | Įrašo duomenų atnaujinimo laiko žyma, suapvalinta iki artimiausios valandos | — |
| `ugis_cm` | `number` | `cm` | `4` | `open` | — | Mokinio ūgis, pateiktas centimetrais | — |
| `svoris_kg` | `number` | `kg` | `4` | `open` | — | Mokinio svoris, pateiktas kilogramais | — |
| `fiz_ugdymo_grupe` | `string` | — | `4` | `open` | — | Sveikatos priežiūros specialisto nustatyta mokinio fizinio ugdymo grupė | — |
| `vertinimo_isvada` | `string` | — | `4` | `open` | — | Sveikatos priežiūros specialisto vertinimo išvada | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |
| `fiz_ugdymo_grupe` | `"Pagrindinė"` | — | — | — | — |
| `fiz_ugdymo_grupe` | `"Parengiamoji"` | — | — | — | — |
| `fiz_ugdymo_grupe` | `"Specialioji"` | — | — | — | — |
| `vertinimo_isvada` | `"Mokinys gali dalyvauti ugdymo veikloje be apribojimų"` | — | — | — | — |
| `vertinimo_isvada` | `"Vaikas gali dalyvauti mokykloje vykdomoje ugdymo veikloje, įskaitant kūno kultūros ugdymą, be jokių apribojimų"` | — | — | — | — |
| `vertinimo_isvada` | `"Mokinys gali dalyvauti ugdymo veikloje laikydamasis rekomendacijų"` | — | — | — | — |
| `vertinimo_isvada` | `"Vaikas gali dalyvauti mokykloje vykdomoje ugdymo veikloje, laikydamasis šių rekomendacijų"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/mokiniu_sveikata.csv
