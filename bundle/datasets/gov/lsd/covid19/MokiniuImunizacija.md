---
type: Table
title: "MokiniuImunizacija — Mokinių vakcinacija ir imunizacija"
description: "12–19 metų amžiaus moksleivių skiepijimas ir imunizacija (nuo SARS-CoV-2) Lietuvos mokyklose pagal amžių Kasdien atnaujinami mokinių imunizacijos nuo SARS-CoV-2 duomenys Lietuvos mokyklose pagal amžių"
resource: "https://get.data.gov.lt/datasets/gov/lsd/covid19/MokiniuImunizacija"
tags: [gov, lsd, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/covid19.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L189"
    last_modified: "2026-11-11T14:39:20Z"
---

# MokiniuImunizacija — Mokinių vakcinacija ir imunizacija

12–19 metų amžiaus moksleivių skiepijimas ir imunizacija (nuo SARS-CoV-2) Lietuvos mokyklose pagal amžių Kasdien atnaujinami mokinių imunizacijos nuo SARS-CoV-2 duomenys Lietuvos mokyklose pagal amžių

- **Model:** `datasets/gov/lsd/covid19/MokiniuImunizacija`[^manifest]
- **Dataset:** [datasets/gov/lsd/covid19](../covid19.md) (`datasets/gov/lsd/covid19`)
- **Manifest CSV:** [datasets/gov/lsd/covid19.csv#L189](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L189)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/covid19/MokiniuImunizacija`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `school` | `string` | — | `2` | `open` | — | Mokyklos pavadinimas (arba laisvasis mokytojas) | — |
| `municipality` | `string` | — | `2` | `open` | — | Savivaldybė, kurioje yra mokykla | — |
| `age_at_2021sep1` | `integer` | `yr` | `4` | `open` | — | Amžiaus grupė, mokinio amžius 2021 m. rugsėjo 1 d. | — |
| `n_all` | `integer` | `U` | `4` | `open` | — | Visi šioje mokykloje šiuo metu besimokantys šios amžiaus grupės mokiniai. Įtraukti ir moksleiviai be lietuviško asmens kodo. | — |
| `n_lt` | `integer` | `U` | `4` | `open` | — | Visi šioje mokykloje besimokantys mokiniai | Visi šios amžiaus grupės mokiniai, kurie turi lietuvišką asmens kodą ir gali būti randami medicininiuose registruose. Šis skaičius naudojamas kaip vardiklis kituose procentiniuose stulpeliuose. |
| `n_vac` | `number` | `U` | `4` | `open` | — | Bent viena doze vakcinuotų besimokančių mokinių skaičius. Tik turintieji lietuvišką asmens kodą. | — |
| `n_vac_imm` | `number` | `U` | `4` | `open` | — | Abiem vakcinos dozėmis paskiepyti mokiniai | T.y. mokiniai, kurie oficialiai jau turi imunitetą (praėjo 14 d. nuo paskiepijimo abiem vakcinos dozėmis datos), skaičius. Tik turintieji lietuvišką asmens kodą. |
| `n_any_imm` | `number` | `U` | `4` | `open` | — | Besimokančių mokinių, kurie galimai turi imunitetą | Mokinių skaičius, kurie turi arba neseniai gavo (per 180 d. laikotarpį) teigiamą diagnostinio tyrimo atsakymą, arba paskiepyti abiem vakcinos dozėmis ir praėjo 14 d. nuo antros vakcinos dozės datos. Tik turintieji lietuvišką asmens kodą. |
| `p_vac` | `number` | `%` | `4` | `open` | — | Procentas bent viena doze vakcinuotų mokinių (n_vac / n_lt * 100%) | — |
| `p_vac_imm` | `number` | `%` | `4` | `open` | — | Procentas turinčių oficialų imunitetą po vakcinacijos (n_vac_imm / n_lt * 100%) | — |
| `p_any_imm` | `number` | `%` | `4` | `open` | — | Procentas turinčių oficialų imunitetą po vakcinacijos arba užsikrėtimo (n_any_imm / n_lt * 100%) | — |
| `c_vac` | `number` | — | `3` | `open` | — | Procentilis, parodantis, kaip aukštai ši mokykla yra kitų mokyklų kontekste pagal konkrečiai šios amžiaus grupės mokinių vakcinaciją (p_vac rodiklį) | 100 – viena iš labiausiai paskiepytų mokyklų, 50 – pačiame viduryje, 0 – viena iš prasčiausiai paskiepytų mokyklų. Procentiliai skaičiuojami tik tų mokyklų, kurios toje amžiaus grupėje turi bent 25 mokinius, kontekste. |
| `c_vac_imm` | `number` | — | `3` | `open` | — | Procentilis, parodantis, kaip aukštai ši mokykla yra kitų mokyklų kontekste pagal konkrečiai šios amžiaus grupės mokinių neišnykusį skiepų suteiktą specifinį imunitetą (p_vac_imm rodiklį) | Procentiliai skaičiuojami tik tų mokyklų kontekste, kurios toje amžiaus grupėje turi bent 25 mokinius. |
| `c_any_imm` | `number` | — | `3` | `open` | — | Procentilis, parodantis, kaip aukštai ši mokykla yra kitų mokyklų kontekste pagal konkrečiai šios amžiaus grupės mokinių turimą oficialų bet kokios kilmės imunitetą (p_any_imm rodiklį) | Procentiliai skaičiuojami tik tų mokyklų kontekste, kurios toje amžiaus grupėje turi bent 25 mokinius. |
| `confidentiality` | `string` | — | `2` | `open` | — | Konfidencialumo taisyklė | Ar buvo pritaikyta konfidencialumo taisyklė, modifikuojanti absoliučius ir procentinius skaičius, kad nebūtų įmanoma sužinoti, kas konkrečiai yra vakcinuotas ir kas ne. Taisyklė: mažiausiame pogrupyje negali būti mažiau nei 5 asmenys. Jei yra – tokiu atveju laikoma, kad tame pogrupyje yra 5 asmenys, ir procentai skaičiuojami atitinkamai. |
| `data_freshness` | `date` | `D` | `4` | `open` | — | Duomenų "šviežumas" | Mažiausia iš dviejų datų: paskutinės įtrauktos vakcinacijos datos ir paskutinio įtraukto teigiamo testo datos. |
| `reference_data` | `date` | `D` | `4` | `open` | — | Ataskaitinė para. | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/covid19.csv
