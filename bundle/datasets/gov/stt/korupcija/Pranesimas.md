---
type: Table
title: "Pranesimas — Gauti pranešimai apie korupciją"
description: "Gauti pranešimai apie korupciją,\"Duomenų rinkinyje pateikiami Specialiųjų tyrimų tarnybai pateikti pranešimai apie korupcinio pobūdžio nusikalstamas veikas nuo 2024m."
resource: "https://get.data.gov.lt/datasets/gov/stt/korupcija/Pranesimas"
tags: [gov, stt, pranesimas, deployed, level-4, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/stt/korupcija.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/stt/korupcija.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2776/"
    title: "data.gov.lt DCAT-AP — datasets/gov/stt/korupcija"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pranesimas — Gauti pranešimai apie korupciją

Gauti pranešimai apie korupciją,"Duomenų rinkinyje pateikiami Specialiųjų tyrimų tarnybai pateikti pranešimai apie korupcinio pobūdžio nusikalstamas veikas nuo 2024m. Rinkinio objektas - gautas pranešimas, pateiktas vienu iš galimų būdų: el. paštu, paštu, per e. pristatymo sistemą, mobiliąja programėle, STT tinklalapyje ar atvykus į STT padalinį. Rinkinyje nurodoma informacija apie pranešimą (gavimo data, pateikimo būdas, priskiriama sritis ir sektorius), jį teikusį pranešėją (kategorija, tipas, požymis, ar pranešimas susijęs su pranešėjo darboviete) bei nagrinėjimą (nagrinėjimo tvarka, rezultatai ir galutinis sprendimas). Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/stt/korupcija/Pranesimas`[^manifest]
- **Dataset:** [Gauti pranešimai apie korupciją](../korupcija.md) (`datasets/gov/stt/korupcija`)[^manifest]
- **Manifest CSV:** [datasets/gov/stt/korupcija.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/stt/korupcija.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/stt/korupcija/Pranesimas` (`deployed`)[^manifest]
- **Provider:** `stt` — Specialiųjų tyrimų tarnyba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_2`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/stt/korupcija.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/stt/korupcija.csv#L8)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/stt/korupcija (https://data.gov.lt/datasets/2776/)
