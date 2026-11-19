---
type: Table
title: "VaistoIsdavimas — ESPBI IS e. recepto posistemės duomenys apie išduotus vaistus pagal 2020 m. išrašytus receptus"
description: "ESPBI IS e. recepto posistemės duomenys apie skiriamus vaistus*."
resource: "https://get.data.gov.lt/datasets/gov/rc/espbiis/vaistu_isdavimai_rec_2020/VaistoIsdavimas"
tags: [gov, rc, vaistoisdavimas, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/espbiis/vaistu_isdavimai_rec_2020.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/espbiis/vaistu_isdavimai_rec_2020.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# VaistoIsdavimas — ESPBI IS e. recepto posistemės duomenys apie išduotus vaistus pagal 2020 m. išrašytus receptus

ESPBI IS e. recepto posistemės duomenys apie skiriamus vaistus*. * - vaistas - šiame duomenų rinkinyje naudojamas kaip bendrinis pavadinimas visiems su receptu skiriamiems medicininiams produktams (vaistinis preparatas; medicinos pagalbos priemonė (MPP); vardinis vaistas; ekstemporalus vaistas***; kitos priemonės); ** - TLK-10-AM - tarptautinis ligos kodas; kodų sistema; apimanti ligas ir įvairius simptomus; patologines būkles; skundus; socialines aplinkybes; išorines sužeidimų ir ligų priežastis; sudaroma Pasaulinės sveikatos organizacijos (PSO); *** - Ekstemporalus vaistas - (ekstemporalus vaistinis preparatas) - vaistinėje pavieniam pacientui pagal gydytojo receptą ir (arba) sveikatos priežiūros įstaigos užsakymą pagamintas vaistinis preparatas ar pagal vaistinio preparato aprašą pagamintas vaistinis preparatas; **** - ATC kodas ar indeksas - anatominis terapinis cheminis indeksas; suteikiamas vaistams ir medicinos priemonėms; pagal kuriuos jie klasifikuojami; patvirtintas Pasaulio sveikatos organizacijos[^manifest]

- **Model:** `datasets/gov/rc/espbiis/vaistu_isdavimai_rec_2020/VaistoIsdavimas`[^manifest]
- **Dataset:** [Elektroninės sveikatos paslaugų ir bendradarbiavimo infrastruktūros informacinės sistema](../vaistu_isdavimai_rec_2020.md) (`datasets/gov/rc/espbiis/vaistu_isdavimai_rec_2020`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/espbiis/vaistu_isdavimai_rec_2020.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/espbiis/vaistu_isdavimai_rec_2020.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/espbiis/vaistu_isdavimai_rec_2020/VaistoIsdavimas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `dirbt_isdavimo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dirbt_recepto_id` | `ref` | [Receptas](../receptai_2020/Receptas.md) (`level=4 UUID`: `dirbt_recepto_id._id`) | `4` | `open` | — | Dirbtinis išrašyto recepto identifikatorius | — |
| `dirbt_isdavimo_id` | `string` | — | `4` | `open` | — | Dirbtinis vaisto išdavimo identifikatorius | — |
| `isdavimo_metai` | `integer` | — | `2` | `open` | — | Vaisto išdavimo metai | — |
| `isdavimo_ketv` | `integer` | — | `3` | `open` | — | Vaisto išdavimo ketvirtis | — |
| `npakid` | `number` | — | `4` | `open` | — | Kiekvieno pavadinimo tos pačios grupės konkretaus nacionalinio vaistinio preparato pakuotės identifikavimo kodas (NPAKID) | — |
| `npakid7` | `number` | — | `4` | `open` | — | Nacionalinis vaistinio preparato identifikavimo kodas, vartojamas teritorinių ligonių kasų kompiuterinėse apskaitos programose — NPAKID-7 | — |
| `vaisto_bendrinis_pavadinimas` | `string` | — | `3` | `open` | — | Skiriamo vaisto* (vardinio vaisto bendrinis pavadinimas; ekstemporaliam vaistui gaminti naudojamos pagrindinės veikliosios medžiagos pavadinimas) bendrinis pavadinimas | — |
| `vaisto_prekinis_pavadinimas` | `string` | — | `3` | `open` | — | Skiriamo vaisto* ( vardinio vaisto; MPP) prekinis pavadinimas | — |
| `isduotas_vaisto_kiekis` | `number` | — | `3` | `open` | — | Išduotas vaisto kiekis | — |
| `kompensavimo_kodas` | `number` | — | `3` | `open` | — | Vaisto* pardavimo mažmeninės bazinės kainos dalies kompensacijos rūšies kodas | — |
| `kompensavimo_pavadinimas` | `string` | — | `4` | `open` | — | Vaisto* pardavimo mažmeninės bazinės kainos dalies kompensacijos rūšies pavadinimas | — |
| `kompensavimo_procentas` | `number` | — | `3` | `open` | — | Vaisto* pardavimo mažmeninės bazinės kainos dalies kompensavimo dydis procentais | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `isdavimo_metai` | `update(type: "date"; ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/espbiis/vaistu_isdavimai_rec_2020.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/espbiis/vaistu_isdavimai_rec_2020.csv#L5)
