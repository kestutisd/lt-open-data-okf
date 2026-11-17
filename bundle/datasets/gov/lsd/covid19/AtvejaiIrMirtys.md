---
type: Table
title: "AtvejaiIrMirtys — Agreguoti COVID-19 atvejai ir mirtys"
description: "Lentelė aprašo užsikrėtimų SARS-CoV-2 virusu (pirminių ir pakartotinių infekcijų) skaičius, taip pat COVID mirčių (\"mirtys nuo COVID\" ir \"mirtys su COVID\"), taip pat visų mirčių dėl bet kokios priežasties skaičius."
resource: "https://get.data.gov.lt/datasets/gov/lsd/covid19/AtvejaiIrMirtys"
tags: [gov, lsd, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/covid19.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# AtvejaiIrMirtys — Agreguoti COVID-19 atvejai ir mirtys

Lentelė aprašo užsikrėtimų SARS-CoV-2 virusu (pirminių ir pakartotinių infekcijų) skaičius, taip pat COVID mirčių ("mirtys nuo COVID" ir "mirtys su COVID"), taip pat visų mirčių dėl bet kokios priežasties skaičius. Viena eilutė yra vienos datos, vienos savivaldybės, vienos amžiaus grupės ir vienos lyties kombinacija. Kartais detalūs asmens duomenys yra nežinomi, taip gali nutikti, pvz., kuomet asmuo yra užsienietis. Duomenys yra papildomi kasdien, taip pat jie gali būti atnaujinti retrospektyviai (praeities datos gali pasipildyti skaičiais, pvz., jei gaunami mirties liudijimai išduoti po ilgai trukusios autopsijos)

- **Model:** `datasets/gov/lsd/covid19/AtvejaiIrMirtys`[^manifest]
- **Dataset:** [datasets/gov/lsd/covid19](../covid19.md) (`datasets/gov/lsd/covid19`)
- **Manifest CSV:** [datasets/gov/lsd/covid19.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/covid19/AtvejaiIrMirtys`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `municipality_name` | `string` | — | `2` | `open` | — | Asmens tikėtinos gyvenamosios vietos savivaldybė (60 Lietuvos savivaldybių), nebūtinai sutampa su asmens deklaruota savivaldybe | — |
| `date` | `date` | `D` | `4` | `open` | — | Paros, kurią įvyko aprašomi įvykiai, data | — |
| `sex` | `string` | — | `3` | `open` | — | Asmenų lytis | — |
| `age_gr` | `string` | — | `3` | `open` | — | Asmenų amžiaus grupė (dešimties metų pločio rėžiais) apskaičiuota šiai dienai | — |
| `incidence` | `integer` | `U` | `4` | `open` | — | Tą dieną toje asmenų grupėje nustatytų pirminių ar pakartotinių užsikrėtimų SARS-CoV-2 virusu skaičius | Tai yra keturių tolimesnių stulpelių suma |
| `infection_1` | `integer` | `U` | `4` | `open` | — | Pirminių užsikrėtimų SARS-CoV-2 virusu skaičius | — |
| `infection_2` | `integer` | `U` | `4` | `open` | — | Antrinių užsikrėtimų SARS-CoV-2 virusu skaičius | — |
| `infection_3` | `integer` | `U` | `4` | `open` | — | Tretinių užsikrėtimų SARS-CoV-2 virusu skaičius | — |
| `infection_4` | `integer` | `U` | `4` | `open` | — | Ketvirtinių užsikrėtimų SARS-CoV-2 virusu skaičius | — |
| `deaths_all` | `integer` | `U` | `4` | `open` | — | Visos mirtys Lietuvoje pagal skaitmeninius mirties liudijimus (<1% mirties liudijimų yra popieriniai, jų nėra nei čia, nei eSveikatoje) | — |
| `deaths_cov1` | `integer` | `U` | `4` | `open` | — | COVID mirtys pagal pirmąjį apibrėžimą ("nuo COVID") | Tai yra siauriausias/konservatyviausias COVID mirties apibrėžimas, darantis prielaidą, kad visi mirtiesliudijimai ir mirties priežastys buvo užpildytos pagal taisykles ir be klaidų. Mirusių asmenų, kurių pagrindine mirties priežastimi nurodyta COVID liga, skaičius |
| `deaths_cov2` | `integer` | `U` | `4` | `open` | — | COVID mirtys pagal antrą apibrėžimą | Šis apibrėžimas įtraukia ir pirmojo apibrėžimo mirtis, tačiau yra platesnis, mirties liudijime ieško su COVID susijusių raktinių žodžių. Mirusių asmenų, kurių bet kuria mirties priežastimi nurodyta COVID liga, skaičius |
| `deaths_cov3` | `integer` | `U` | `4` | `open` | — | COVID mirtys pagal trečią apibrėžimą ("su COVID") | Tai yra plačiausias/liberaliausias COVID mirties apibrėžimas, į save įtraukiantis ir du ankstesnius apibrėžimus, yra geriausiai atitinkantis perteklinio mirtingumo pandemijos metu skaičiavimus. Mirusių asmenų, kurių bet kuria priežastimi nurodyta COVID liga arba užsikrėtusiųjų ir mirusių ne dėl išorinių mirties priežasčių per 28 dienas, skaičius |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/covid19.csv
