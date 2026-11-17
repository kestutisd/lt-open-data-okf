---
type: Table
title: "Uzsakymas — Kraujo produktų užsakymai pacientams"
description: "Duomenų rinkinyje pateikiami nuo 2016 m. informacinėje sistemoje „LabDataLIMS“ kaupiami ir iki šiol atnaujinami Respublikinės Šiaulių ligoninės atliktų kraujo perpylimo procedūrų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/rsl/labdatalims/Uzsakymas"
tags: [gov, rsl, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rsl/labdatalims.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsl/labdatalims.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Uzsakymas — Kraujo produktų užsakymai pacientams

Duomenų rinkinyje pateikiami nuo 2016 m. informacinėje sistemoje „LabDataLIMS“ kaupiami ir iki šiol atnaujinami Respublikinės Šiaulių ligoninės atliktų kraujo perpylimo procedūrų duomenys. Vienas įrašas atitinka vieną išdavimo įvykio ir išduoto produkto kombinaciją. Duomenų rinkinį sudaro: išdavimo identifikatorius, numeris, užsakymo ir išdavimo datos, recipiento identifikatorius, asmens kodas, lytis bei gimimo metai iš atitinkamų stulpelių bei galiojančių asmens kodų, kraujo grupė, kraujo produkto identifikatorius, grupė, fenotipas, Kelo kodas, komponento kodas bei pavadinimas, minėto produkto tūris, davimo bei galiojimo pabaigos datos ir tiekėjas. Dalyje įrašų kraujo produkto išdavimo data yra ankstesnė už užsakymo, kadangi skubiais atvejais užsakymas fiksuojamas po išdavimo. Pavieniais atvejais to paties kodo kraujo produktų galiojimo laikas ženkliai skiriasi nuo didžiosios dalies atitinkamo kodo produkto, veikiausiai, dėl klaidingai įvestų duomenų. Duomenų teikėjas – VšĮ Respublikinė Šiaulių ligoninė.

- **Model:** `datasets/gov/rsl/labdatalims/Uzsakymas`[^manifest]
- **Dataset:** [datasets/gov/rsl/labdatalims](../labdatalims.md) (`datasets/gov/rsl/labdatalims`)
- **Manifest CSV:** [datasets/gov/rsl/labdatalims.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsl/labdatalims.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rsl/labdatalims/Uzsakymas`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus indentifikatorius | — |
| `isdavimo_id` | `string` | — | `4` | `open` | — | Šifruotas išdavimo identifikatorius | — |
| `isdavimo_numeris` | `string` | — | `4` | `open` | — | Šifruotas išdavimo numeris | — |
| `uzsakymo_data` | `datetime` | `S` | `4` | `open` | — | Produkto užsakymo data su laiku | — |
| `isdavimo_data` | `datetime` | `S` | `4` | `open` | — | Produkto išdavimo data su laiku | — |
| `recipiento_id` | `string` | — | `4` | `open` | — | Šifruotas produkto recipiento identifikatorius | — |
| `recipiento_asmens_kodas` | `string` | — | `4` | `open` | — | Šifruotas produkto recipiento asmens kodas | — |
| `recipiento_asmens_kodo_validacija` | `string` | — | `4` | `open` | — | Produkto recipiento asmens kodo validacija | — |
| `recipiento_lytis` | `string` | — | `4` | `open` | — | Produkto recipiento lytis | — |
| `vda_recipiento_lytis` | `string` | — | `4` | `open` | — | Produkto recipiento lytis iš asmens kodo | — |
| `recipiento_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Produkto recipiento gimimo metai | — |
| `vda_recipiento_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Produkto recipiento gimimo metai iš asmens kodo | — |
| `recipiento_kraujo_grupe` | `string` | — | `4` | `open` | — | Produkto recipiento kraujo grupė | — |
| `produkto_id` | `string` | — | `4` | `open` | — | Produkto šifruotas identifikatorius | — |
| `produkto_kraujo_grupe` | `string` | — | `4` | `open` | — | Produkto kraujo grupė | — |
| `produkto_kraujo_fenotipas` | `string` | — | `4` | `open` | — | Produkto kraujo fenotipas | — |
| `produkto_kelo_kodas` | `string` | — | `4` | `open` | — | Produkto kraujo Kelo kodas | — |
| `produkto_komponento_kodas` | `string` | — | `4` | `open` | — | Produkto komponento kodas | — |
| `produkto_komponentas` | `string` | — | `4` | `open` | — | Produkto komponento pavadinimas | — |
| `produkto_turis_ml` | `integer` | `ml` | `4` | `open` | — | Produkto tūris | — |
| `kraujo_davimo_data` | `date` | — | `4` | `open` | — | Produkto kraujo davimo data | — |
| `produkto_nebegaliojimo_data` | `date` | — | `4` | `open` | — | Produkto galiojimo pabaigos data | — |
| `tiekejas` | `string` | — | `4` | `open` | — | Produkto tiekėjas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `recipiento_asmens_kodo_validacija` | `"Tinkamas"` | — | — | Tinkamas | — |
| `recipiento_lytis` | `"M"` | — | — | Moteris | — |
| `recipiento_lytis` | `"V"` | — | — | Vyras | — |
| `recipiento_lytis` | `"N"` | — | — | Nežinoma | — |
| `vda_recipiento_lytis` | `"M"` | — | — | Moteris | — |
| `vda_recipiento_lytis` | `"V"` | — | — | Vyras | — |
| `recipiento_kraujo_grupe` | `"A+"` | — | — | A teigiama | — |
| `recipiento_kraujo_grupe` | `"O+"` | — | — | O teigiama | — |
| `recipiento_kraujo_grupe` | `"B+"` | — | — | B teigiama | — |
| `recipiento_kraujo_grupe` | `"O-"` | — | — | O neigiama | — |
| `recipiento_kraujo_grupe` | `"A-"` | — | — | A neigiama | — |
| `recipiento_kraujo_grupe` | `"AB+"` | — | — | AB teigiama | — |
| `recipiento_kraujo_grupe` | `"B-"` | — | — | B neigiama | — |
| `recipiento_kraujo_grupe` | `"AB-"` | — | — | AB neigiama | — |
| `produkto_kraujo_grupe` | `"O+"` | — | — | O teigiama | — |
| `produkto_kraujo_grupe` | `"A+"` | — | — | A teigiama | — |
| `produkto_kraujo_grupe` | `"B+"` | — | — | B teigiama | — |
| `produkto_kraujo_grupe` | `"O-"` | — | — | O neigiama | — |
| `produkto_kraujo_grupe` | `"A-"` | — | — | A neigiama | — |
| `produkto_kraujo_grupe` | `"AB+"` | — | — | AB teigiama | — |
| `produkto_kraujo_grupe` | `"B-"` | — | — | B neigiama | — |
| `produkto_kraujo_grupe` | `"AB-"` | — | — | AB neigiama | — |
| `produkto_kelo_kodas` | `"K Neg"` | — | — | K neigiamas | — |
| `produkto_kelo_kodas` | `"K Pos"` | — | — | K teigiamas | — |
| `produkto_komponento_kodas` | `"E5303V00"` | — | — | E5303V00 | — |
| `produkto_komponento_kodas` | `"E3874V00"` | — | — | E3874V00 | — |
| `produkto_komponento_kodas` | `"E6258V00"` | — | — | E6258V00 | — |
| `produkto_komponento_kodas` | `"E5358V00"` | — | — | E5358V00 | — |
| `produkto_komponento_kodas` | `"E4636V00"` | — | — | E4636V00 | — |
| `produkto_komponento_kodas` | `"E4637V00"` | — | — | E4637V00 | — |
| `produkto_komponento_kodas` | `"A0001V00"` | — | — | A0001V00 | — |
| `produkto_komponento_kodas` | `"A0403V00"` | — | — | A0403V00 | — |
| `produkto_komponentas` | `"Eritrocitai be leukocitų pridėtiniame tirpale"` | — | — | Eritrocitai be leukocitų pridėtiniame tirpale | — |
| `produkto_komponentas` | `"Šviežiai užšaldyta plazma"` | — | — | Šviežiai užšaldyta plazma | — |
| `produkto_komponentas` | `"Sukautieji trombocitai iš 4 vnt."` | — | — | Sukautieji trombocitai iš 4 vnt. | — |
| `produkto_komponentas` | `"Krioprecipitatas"` | — | — | Krioprecipitatas | — |
| `produkto_komponentas` | `"Afreziniai Trombocitai"` | — | — | Afreziniai Trombocitai | — |
| `produkto_komponentas` | `"Sukauptieji trombocitai iš 5 vnt."` | — | — | Sukauptieji trombocitai iš 5 vnt. | — |
| `produkto_komponentas` | `"Sukauptieji trombocitai"` | — | — | Sukauptieji trombocitai | — |
| `tiekejas` | `"VšĮ NKC Panevėžio skyrius"` | — | — | VšĮ NKC Panevėžio skyrius | — |
| `tiekejas` | `"VšĮ Nacionalinis kraujo centras"` | — | — | VšĮ Nacionalinis kraujo centras | — |
| `tiekejas` | `"VšĮ VU ligoninė Santaros klinika Kraujo centras"` | — | — | VšĮ VU ligoninė Santaros klinika Kraujo centras | — |
| `tiekejas` | `"Kauno klinikų Kraujo centras"` | — | — | Kauno klinikų Kraujo centras | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rsl/labdatalims.csv
