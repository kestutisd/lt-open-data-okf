---
type: Table
title: "Gavejas — Socialinio būsto gavėjų charakteristikos"
description: "Lentelėje pateikiamos socialinį būstą gaunančių asmenų ar šeimų bendrosios charakteristikos nuo 2000 metų."
resource: "https://get.data.gov.lt/datasets/gov/sadm/socialinis_bustas/Gavejas"
tags: [gov, sadm, gavejas, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/soc_bustas.csv#L61"
    title: "atviriduomenys/manifest — datasets/gov/sadm/soc_bustas.csv#L61"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Gavejas — Socialinio būsto gavėjų charakteristikos

Lentelėje pateikiamos socialinį būstą gaunančių asmenų ar šeimų bendrosios charakteristikos nuo 2000 metų. Įrašas lentelėje nurodo vieną asmenį ar šeimą, tais metais pasirašiusius socialinio būsto nuomos sutartį. Nurodomos būsto gavėjo charakteristikos (požymiai, ar yra bedarbių, ar asmuo patenka į socialinės rizikos įskaitą, įtraukimo į įskaitą priežastis, namų ūkį sudarančių asmenų skaičius ir šeimos tipas) ir gyvenamosios vietos duomenys savivaldybės arba apskrities lygmeniu.[^manifest]

- **Model:** `datasets/gov/sadm/socialinis_bustas/Gavejas`[^manifest]
- **Dataset:** [Socialinio būsto duomenys](../socialinis_bustas.md) (`datasets/gov/sadm/socialinis_bustas`)[^manifest]
- **Manifest CSV:** [datasets/gov/sadm/soc_bustas.csv#L61](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/soc_bustas.csv#L61)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sadm/socialinis_bustas/Gavejas` (`deployed`)[^manifest]
- **Provider:** `sadm` — Lietuvos Respublikos socialinės apsaugos ir darbo ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `statuso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `statuso_id` | `string` | — | `4` | `open` | — | Statuso identifikacinis numeris | — |
| `sutarties_metai` | `integer` | — | `4` | `open` | — | Socialinio būsto sutarties pasirašymo metai | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Šeimos ar asmens, gaunančio socialinį būstą, savivaldybę. | — |
| `apskritis` | `string` | — | `4` | `open` | — | Šeimos ar asmens, gaunančio socialinį būstą, apskritis | — |
| `ar_bedarbis` | `boolean` | — | `4` | `open` | — | Požymis, ar socialinį būstą gavusioje šeimoje yra bedarbių | — |
| `soc_rizika` | `boolean` | — | `4` | `open` | — | Požymis, ar socialinį būstą gavęs asmuo ar šeima patenka į socialinę riziką | — |
| `seim_tipas` | `string` | — | `4` | `open` | — | Socialinį būstą gaunančio asmens ar šeimos tipas | — |
| `itr_iskait_priezastis` | `string` | — | `4` | `open` | — | Asmens ar šeimos, gaunančios socialinį būstą, įtraukimo į socialinės rizikos šeimų įskaitą priežastis | — |
| `seim_nariai` | `integer` | — | `4` | `open` | — | Socialinį būstą gaunančios šeimos narių skaičius | — |
| `seim_duomenu_atnaujinimas` | `datetime` | `S` | `4` | `open` | — | Duomenų atnaujinimo laikas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sadm/soc_bustas.csv#L61 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/soc_bustas.csv#L61)
