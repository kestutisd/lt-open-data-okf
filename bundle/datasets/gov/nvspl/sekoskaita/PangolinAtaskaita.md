---
type: Table
title: "PangolinAtaskaita — SARS-CoV-2 sekoskaitos Pangolin rezultatų ataskaita"
description: "Duomenys iš Nacionalinės visuomenės sveikatos priežiūros laboratorijos sekoskaitos tyrimų duomenų bazės apie SARS-CoV-2 viruso atliktos sekoskaitos rezultatus."
resource: "https://get.data.gov.lt/datasets/gov/nvspl/sekoskaita/PangolinAtaskaita"
tags: [gov, nvspl, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nvspl/sars_cov_sekoskaitos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvspl/sars_cov_sekoskaitos.csv#L130"
    last_modified: "2026-11-11T14:39:20Z"
---

# PangolinAtaskaita — SARS-CoV-2 sekoskaitos Pangolin rezultatų ataskaita

Duomenys iš Nacionalinės visuomenės sveikatos priežiūros laboratorijos sekoskaitos tyrimų duomenų bazės apie SARS-CoV-2 viruso atliktos sekoskaitos rezultatus. Viena eilutė yra vieno SARS-CoV-2 mėginio sekoskaitos rezultatas. Seskoskaitos rezultatai generuojami naudojant Pangolin programinę įrangą. Eilutės informaciją sudaro laboratorijos priskirtas mėginio identifikacinis numeris, Pango priskirta viruso linija, Scorpio priskirta mutacijų konsteliacijos grupė, kolizija, patikimumo ir kolizijos įverčiai, Scorpio ir Pangolin duomenų ir algoritmų versijos, bei papildomi pastabų laukeliai.

- **Model:** `datasets/gov/nvspl/sekoskaita/PangolinAtaskaita`[^manifest]
- **Dataset:** [SARS-CoV-2 viruso sekoskaitos duomenys](../sekoskaita.md) (`datasets/gov/nvspl/sekoskaita`)
- **Manifest CSV:** [datasets/gov/nvspl/sars_cov_sekoskaitos.csv#L130](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvspl/sars_cov_sekoskaitos.csv#L130)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nvspl/sekoskaita/PangolinAtaskaita`
- **Primary Key (`ref`):** `meg_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `meg_id` | `string` | — | `4` | `open` | — | Mėginio identifikacinis numeris | — |
| `linija` | `string` | — | `4` | `open` | — | Pango priskirta COVID viruso linija | — |
| `scorpio_konst_gr` | `string` | — | `4` | `open` | — | SCORPIO konsteliacijos grupė | SCORPIO programinės įrangos priskirta mutacijų konsteliacijos grupė |
| `pango_kolizija` | `number` | — | `4` | `open` | — | Pango kolizija | Nurodoma kiek kitų linijų gali būti priskirta pagal pangoLEARN modelį. Jei vertė 0, tuomet jokios kitos linijos neatitinka dabartinės sekos, jei didesnis nei 0, tuomet nurodoma kiek linijų atitinka nusekvenuotą seką. |
| `scorpio_patik_balas` | `number` | — | `4` | `open` | — | SCORPIO patikimumo balas | Patikimumo balas (angl. support score), kuris nurodo proporciją alternatyvių alelių genų sekoje |
| `scorpio_kolizijos_ivert` | `number` | — | `4` | `open` | — | SCORPIO kolizijos įvertis | Kolizijos įvertis (angl. confict score) yra proporcija apibrėžtų variantų, kurie turi referencinius alelius sekoje. Dviprasmiškos/kitos ne referencinės/alternatyvios bazės kiekvieno varianto pozicijoje prisideda prie šio įverčio denominatoriaus. |
| `scorpio_pastabos` | `string` | — | `4` | `open` | — | SCORPIO pastabos | SCORPIO programinės įrangos pastabų stulpelis |
| `scorpio_versija` | `string` | — | `4` | `open` | — | SCORPIO versija | — |
| `pangolin_modelio_versija` | `string` | — | `4` | `open` | — | Pangolin modelio versija | Pangolin versijos ir modeliai, kurie naudojami sekų klasifikavimui |
| `pangolin_duomenu_versija` | `string` | — | `4` | `open` | — | Pangolin duomenų versija | — |
| `konsteliacijos_versija` | `string` | — | `4` | `open` | — | Mutacijų konsteliacijos versija | — |
| `ar_linija_priskira` | `boolean` | — | `4` | `open` | — | Ar linija priskirta | Nurodoma ar atitinkama seka turi oficialiai priskirtą liniją |
| `kokybe` | `string` | — | `4` | `open` | — | — | Statusas, nurodantis, ar sekos kokybė yra tinkama |
| `kokybes_pastabos` | `string` | — | `4` | `open` | — | Kokybės kontrolės pastabos | — |
| `bendros_pastabos` | `string` | — | `4` | `open` | — | Bendros pastabos | Pastabų laukas, kuris aprašo problemas susijusias su sprendimų schemomis (angl. decision tree). Jei sekoskaitos kokybės kontrolė netinkama, šiame stulpelyje nurodoma priežastis. Jei seka atitinka VNP slenkstį, kad Scorpio nustatytų mutacijų konsteliaciją, čia bus nurodomas konkretus VNP, alternatyvių ir dviprasmiškų alelių skaičius. |

[^manifest]: atviriduomenys/manifest — datasets/gov/nvspl/sars_cov_sekoskaitos.csv
