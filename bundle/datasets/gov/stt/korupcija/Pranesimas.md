---
type: Table
title: "Pranesimas — Gauti pranešimai apie korupciją"
description: "Gauti pranešimai apie korupciją,\"Duomenų rinkinyje pateikiami Specialiųjų tyrimų tarnybai pateikti pranešimai apie korupcinio pobūdžio nusikalstamas veikas nuo 2024m. Rinkinio objektas - gautas pranešimas, pateiktas vienu iš galimų..."
resource: "https://get.data.gov.lt/datasets/gov/stt/korupcija/Pranesimas"
tags: [gov, stt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/stt/korupcija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/stt/korupcija.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pranesimas — Gauti pranešimai apie korupciją

Gauti pranešimai apie korupciją,"Duomenų rinkinyje pateikiami Specialiųjų tyrimų tarnybai pateikti pranešimai apie korupcinio pobūdžio nusikalstamas veikas nuo 2024m. Rinkinio objektas - gautas pranešimas, pateiktas vienu iš galimų būdų: el. paštu, paštu, per e. pristatymo sistemą, mobiliąja programėle, STT tinklalapyje ar atvykus į STT padalinį. Rinkinyje nurodoma informacija apie pranešimą (gavimo data, pateikimo būdas, priskiriama sritis ir sektorius), jį teikusį pranešėją (kategorija, tipas, požymis, ar pranešimas susijęs su pranešėjo darboviete) bei nagrinėjimą (nagrinėjimo tvarka, rezultatai ir galutinis sprendimas).

- **Model:** `datasets/gov/stt/korupcija/Pranesimas`[^manifest]
- **Dataset:** [Gauti pranešimai apie korupciją](../korupcija.md) (`datasets/gov/stt/korupcija`)
- **Manifest CSV:** [datasets/gov/stt/korupcija.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/stt/korupcija.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/stt/korupcija/Pranesimas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `gavimas` | `date` | `D` | `4` | `open` | — | Pranešimo gavimo data | — |
| `gavimo_budas` | `string` | — | `4` | `open` | — | Pranešimo gavimo būdas | — |
| `sritis` | `string` | — | `4` | `open` | — | Pranešimo sritis | — |
| `sektorius` | `string` | — | `4` | `open` | — | Pranešimo sektorius | — |
| `ar_vykdomas_istatymas` | `boolean` | — | `4` | `open` | — | Lietuvos Respublikos korupcijos prevencijos įstatymo 9 str. „Pranešimas apie korupcinio pobūdžio nusikalstamas veikas“ vykdymas | — |
| `pranesejo_kategorija` | `string` | — | `4` | `open` | — | Pranešėjo kategorija | — |
| `ar_darboviete` | `boolean` | — | `4` | `open` | — | Požymis, ar pranešimas yra apie darbovietę | — |
| `pranesejo_tipas` | `string` | — | `4` | `open` | — | Pranešėjo tipas (fizinis asmuo (grupė)/ juridinis asmuo) | — |
| `nagrinejimo_tvarka` | `string` | — | `4` | `open` | — | Pranešimo nagrinėjimo tvarka | — |
| `nagrinejimo_rezultatai` | `string` | — | `4` | `open` | — | Pranešimo nagrinėjimo rezultatai | — |
| `sprendimas` | `string` | — | `4` | `open` | — | Sprendimas, priimtas išnagrinėjus pranešimą vadovaujantis 2018-05-21 LRSTT direktoriaus aktualios redakcijos įsakymu Nr. 2-86 arba išnagrinėjus pranešimą baudžiamojo proceso kodekso tvarka | Žiūrėti stulpelį nagrinejimo_tvarka |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pranesejo_kategorija` | `"Valstybės sektoriuje dirbantis (veikiantis)asmuo"` | — | — | — | — |
| `pranesejo_kategorija` | `"Mišriame sektoriuje dirbantis (veikiantis) asmuo)"` | — | — | — | — |
| `pranesejo_tipas` | `"Fizinis asmuo (grupė)"` | — | — | — | — |
| `pranesejo_tipas` | `"Juridinis asmuo"` | — | — | — | — |
| `nagrinejimo_tvarka` | `"Baudžiamojo proceso kodeksas"` | — | — | — | — |
| `nagrinejimo_tvarka` | `"Pranešimų nagrinėjimo skyriaus tvarka"` | — | — | — | — |
| `nagrinejimo_rezultatai` | `"Pažeidimų nenustatyta"` | — | — | — | — |
| `nagrinejimo_rezultatai` | `"Nustatyti tarnybinio (darbo drausmės) nusižengimo požymiai"` | — | — | — | — |
| `nagrinejimo_rezultatai` | `"Kita"` | — | — | — | — |
| `nagrinejimo_rezultatai` | `"Nustatyti nusikalstamos veikos požymiai"` | — | — | — | — |
| `nagrinejimo_rezultatai` | `"Nustatytos korupcinio pobūdžio rizikos"` | — | — | — | — |
| `sprendimas` | `"Atsisakyti pradėti ikiteisminį tyrimą"` | — | — | — | — |
| `sprendimas` | `"Baigti procedūras"` | — | — | — | — |
| `sprendimas` | `"Pradėti ikiteisminį tyrimą"` | — | — | — | — |
| `sprendimas` | `"Priimti sprendimą pagal baudžiamojo proceso kodeksą"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/stt/korupcija.csv
