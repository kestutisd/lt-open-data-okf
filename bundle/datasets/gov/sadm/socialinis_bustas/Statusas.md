---
type: Table
title: "Statusas — Socialinio ir savivaldybės būsto nuomos duomenys"
description: "Lentelėje pateikiami socialinio ir savivaldybės būsto nuomos Lietuvos savivaldybėse istorijos duomenys nuo 20 a."
resource: "https://get.data.gov.lt/datasets/gov/sadm/socialinis_bustas/Statusas"
tags: [gov, sadm, statusas, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/soc_bustas.csv#L73"
    title: "atviriduomenys/manifest — datasets/gov/sadm/soc_bustas.csv#L73"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Statusas — Socialinio ir savivaldybės būsto nuomos duomenys

Lentelėje pateikiami socialinio ir savivaldybės būsto nuomos Lietuvos savivaldybėse istorijos duomenys nuo 20 a. pabaigos. Lentelės objektas – vieno socialinio arba savivaldybės būsto statusas (nuomojamas, laisvas, rezervuotas, parduotas ir kt.) tam tikru laikotarpiu. Lentelėje pateikiami būsto statuso duomenys (būsena, būsenos pradžia ir pabaiga, būsto charakteristikos, vietovė) ir nuomos informacija (sutarties dėl nuomos pasirašymo metai, būsto nuomos kainos savivaldybėje ataskaitiniais metais, 25 %, 50 % ir 75 % kvantiliai bei požymis, nurodantis, ar būste gyvena asmuo iš socialinio būsto eilės sąrašo; duomenų naudotojams primename, jog kvantilis nurodo reikšmę, už kurią x dalis duomenų yra mažesni arba lygūs). Duomenys jungiami su lentele „Socialinio būsto fondas“ pagal lauką „busto_id“.[^manifest]

- **Model:** `datasets/gov/sadm/socialinis_bustas/Statusas`[^manifest]
- **Dataset:** [Socialinio būsto duomenys](../socialinis_bustas.md) (`datasets/gov/sadm/socialinis_bustas`)[^manifest]
- **Manifest CSV:** [datasets/gov/sadm/soc_bustas.csv#L73](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/soc_bustas.csv#L73)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sadm/socialinis_bustas/Statusas` (`deployed`)[^manifest]
- **Provider:** `sadm` — Lietuvos Respublikos socialinės apsaugos ir darbo ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `ivykio_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ivykio_id` | `string` | — | `4` | `open` | — | Būsto įvykio identifikacinis numeris | — |
| `busto_id` | `string` | — | `4` | `open` | — | Būsto identifikacinis numeris | — |
| `data_nuo` | `date` | `D` | `4` | `open` | — | Statuso pradžios data | — |
| `data_iki` | `date` | `D` | `4` | `open` | — | Statuso pabaigos data | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Būsto savivaldybės pavadinimas | — |
| `busto_tipas` | `string` | — | `4` | `open` | — | Būsto tipas | — |
| `busto_busena` | `string` | — | `4` | `open` | — | Būsto būsenos pavadinimas | — |
| `naudojimo_budas` | `string` | — | `4` | `open` | — | Būsto naudojimo būdo pavadinimas | — |
| `busto_plotas_kv_m` | `number` | `m²` | `4` | `open` | — | Būsto plotas, išreikštas kvadratiniais metrais | — |
| `kambariu_sk` | `integer` | — | `4` | `open` | — | Kambarių skaičius būste | — |
| `nuoma_eur_kvantilis_25` | `number` | — | `4` | `open` | — | Socialinio būsto nuomos kainų savivaldybėje pagal sutarties metus 25% kvantilis, išreikštas eurais | Kvantilis nurodo reikšmę, už kurią x dalis duomenų yra mažesni arba lygūs. |
| `nuoma_eur_mediana` | `number` | — | `4` | `open` | — | Socialinio būsto nuomos kainų savivaldybėje pagal sutarties metus mediana (50% kvantilis), išreikštas eurais | Kvantilis nurodo reikšmę, už kurią x dalis duomenų yra mažesni arba lygūs. |
| `nuomos_eur_kvantilis_75` | `number` | — | `4` | `open` | — | Socialinio būsto nuomos kainų savivaldybėje pagal sutarties metus 75% kvantilis, išreikštas eurais | Kvantilis nurodo reikšmę, už kurią x dalis duomenų yra mažesni arba lygūs. |
| `asmuo_is_eiles` | `boolean` | — | `4` | `open` | — | Požymis, ar būste gyvena asmuo iš socialinio būsto eilės | — |
| `sutarties_metai` | `integer` | — | `4` | `open` | — | Sutarties dėl socialinio būsto nuomos pasirašymo metai | — |
| `duomenu_atnaujinimas` | `datetime` | `S` | `4` | `open` | — | Duomenų atnaujinimo laikas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `busto_tipas` | `"Savivaldybės būstas"` | — | — | — | — |
| `busto_tipas` | `"Socialinis būstas"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sadm/soc_bustas.csv#L73 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/soc_bustas.csv#L73)
