---
type: Table
title: "Sprendimas — Sprendimai suteikti socialinį būstą"
description: "Lentelėje nurodomi sprendimai skirti socialinį būstą asmenims, pateikusiems prašymą, ir duomenys apie sprendimą – data ir sprendimą priėmusi savivaldybė."
resource: "https://get.data.gov.lt/datasets/gov/sadm/socialinis_bustas/Sprendimas"
tags: [gov, sadm, sprendimas, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/soc_bustas.csv#L135"
    title: "atviriduomenys/manifest — datasets/gov/sadm/soc_bustas.csv#L135"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sprendimas — Sprendimai suteikti socialinį būstą

Lentelėje nurodomi sprendimai skirti socialinį būstą asmenims, pateikusiems prašymą, ir duomenys apie sprendimą – data ir sprendimą priėmusi savivaldybė. Jeigu asmuo arba šeima, kaip numatyta socialinio būsto įstatyme, netenka teisės į socialinį būstą, tuomet nurodoma sprendimo priėmimo išbraukti asmenį iš sąrašo data, priežastis ir išbraukimo data. Taip pat pateikiamas asmens, įrašyto į būsto laukiančiųjų sąrašą, eilės numeris duomenų atnaujinimo metu, nurodomas jo eilės numeris tuo metu, kai jam buvo paskirtas socialinis būstas, ir fiksuojama įsikraustymo į pirmąjį socialinį būstą data. Lentelės naudotojai, sujungę duomenis su prašymų lentele pagal lauką „prasymo_id“, gali apskaičiuoti skirtumą tarp prašymo teikimo, sprendimo priėmimo ir pirmo įsikraustymo į suteiktą socialinį būstą datų.[^manifest]

- **Model:** `datasets/gov/sadm/socialinis_bustas/Sprendimas`[^manifest]
- **Dataset:** [Socialinio būsto duomenys](../socialinis_bustas.md) (`datasets/gov/sadm/socialinis_bustas`)[^manifest]
- **Manifest CSV:** [datasets/gov/sadm/soc_bustas.csv#L135](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/soc_bustas.csv#L135)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sadm/socialinis_bustas/Sprendimas` (`deployed`)[^manifest]
- **Provider:** `sadm` — Lietuvos Respublikos socialinės apsaugos ir darbo ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `sprendimo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sprendimo_id` | `string` | — | `4` | `open` | — | Sprendimo identifikacinis numeris | — |
| `prasymo_id` | `string` | — | `4` | `open` | — | Prašymo identifikacinis numeris | Jungiasi su prašymų lenta |
| `sprendimo_data` | `date` | `D` | `4` | `open` | — | Sprendimo priėmimo data | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybės administracijos, kurioje priimtas sprendimas, pavadinimas | — |
| `eil_nr_skyrimo_metu` | `integer` | — | `4` | `open` | — | Eilės numeris sprendimo dėl socialinio būsto skyrimo metu | — |
| `eil_nr` | `integer` | — | `4` | `open` | — | Eilės numeris duomenų atnaujinimo laiku | — |
| `duomenu_atnaujinimas` | `datetime` | `S` | `4` | `open` | — | Duomenų atnaujinimas | — |
| `pirmas_isikraustymas` | `date` | `D` | `4` | `open` | — | Pirmo įsikraustymo į socialinį būstą tada pagal priimtą sprendimą | — |
| `sprendimas_isbraukti` | `date` | `D` | `4` | `open` | — | Sprendimo išbraukti asmenį arba šeimą iš Asmenų ir šeimų, turinčių teisę į socialinio būsto nuomą, sąrašo data | — |
| `isbraukimo_data` | `date` | `D` | `4` | `open` | — | Asmens arba šeimos išbraukimo iš Asmenų ir šeimų, turinčių teisę į socialinio būsto nuomą, sąrašo data | — |
| `isbraukimo_priezastis` | `string` | — | `4` | `open` | — | Išbraukimo iš Asmenų ir šeimų, turinčių teisę į socialinio būsto nuomą, sąrašo priežastis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sadm/soc_bustas.csv#L135 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/soc_bustas.csv#L135)
