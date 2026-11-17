---
type: Table
title: "Gauta — Deklaracijų duomenys"
description: "Rinkinyje pateikiami Kauno miesto savivaldybės vietinių rinkliavų už naudojimąsi Kauno miesto savivaldybės viešąja turizmo ir poilsio infrastruktūra deklaracijų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/pagalve/Gauta"
tags: [gov, kauno_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/pagalve.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/pagalve.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Gauta — Deklaracijų duomenys

Rinkinyje pateikiami Kauno miesto savivaldybės vietinių rinkliavų už naudojimąsi Kauno miesto savivaldybės viešąja turizmo ir poilsio infrastruktūra deklaracijų duomenys. Deklaracijas teikia fiziniai ir juridiniai asmenys, teikiantys apgyvendinimo paslaugas Kauno mieste. Rinkinio objektas - vieno apgyvendinimo objekto deklaracija. Duomenys teikiami nuo 2017m. iki šių dienų. Nurodomas deklaraciją teikusio asmens tipas (fizinis ar juridinis), jo veikla pagal ekonominės veiklos rūšies klasifikatorių (EVRK), deklaracijos pradžios ir pabaigos datos, mokėtina suma bei duomenys apie suteiktas nakvynes. Pažymėtina, jog rinkliavos neskaičiuojamos vaikams iki 18 metų ir ugdymo įstaigoms, kai patalpos nuomojamos mokymosi tikslais. Nuo pagalvės mokesčio taip pat atleidžiami asmenys su negalia, kuriems nustatytas 0-40 proc. darbingumo lygis, taip pat asmenys, kuriems teikiamos medicininės reabilitacijos paslaugos iš privalomojo sveikatos draudimo fondo lėšų. Šių asmenų nakvynės taip pat įtrauktos į rinkinį.

- **Model:** `datasets/gov/kauno_m_sav/pagalve/Gauta`[^manifest]
- **Dataset:** [Kauno miesto pagalvės mokesčio deklaracijų duomenys](../pagalve.md) (`datasets/gov/kauno_m_sav/pagalve`)
- **Manifest CSV:** [datasets/gov/kauno_m_sav/pagalve.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/pagalve.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/pagalve/Gauta`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `tipas` | `string` | — | `4` | `open` | — | Deklaraciją pateikusio asmens tipas | — |
| `evrk_kodas` | `string` | — | `4` | `open` | — | Deklaraciją pateikusio asmens ekonominės veiklos rūšies (EVRK) kodas(-i) pagal EVRK klasifikatorių | — |
| `evrk` | `string` | — | `4` | `open` | — | Deklaraciją pateikusio asmens ekonominės veiklos rūšies (EVRK) pavadinimas(-i) pagal EVRK klasifikatorių | — |
| `periodo_pradzia` | `date` | `D` | `4` | `open` | — | Deklaracijos laikotarpio pradžia | — |
| `periodo_pabaiga` | `date` | `D` | `4` | `open` | — | Deklaracijos laikotarpio pabaiga | — |
| `naktys_be_isimciu` | `integer` | `U` | — | — | — | Suteiktų nakvynių skaičius asmenims, kuriems lengvatos netaikomos | — |
| `naktys_isimtys` | `integer` | `U` | — | — | — | Suteiktų nakvynių skaičius asmenims, kuriems taikomos lengvatos | — |
| `is_viso_naktu` | `integer` | `U` | — | — | — | Per mokestinį laikotarpį suteiktų nakvynių skaičius | — |
| `mok_suma_eur` | `number` | — | `2` | — | — | Mokėtina mokesčių suma eurais | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"juridinis"` | — | — | — | — |
| `tipas` | `"fizinis"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `evrk_kodas` | `"update(property: ""evrk_kodas[]"", type: ""array"", source: ""Evrk_kodas"")"` | `property` | `4` | — | — | — | — |
| `evrk` | `"update(property: ""evrk[]"", type: ""array"", source: ""Evrk"")"` | `property` | `4` | — | — | — | — |
| `mok_suma_eur` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/pagalve.csv
