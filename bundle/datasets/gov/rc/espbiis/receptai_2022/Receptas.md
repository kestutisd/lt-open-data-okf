---
type: Table
title: "Receptas — ESPBI IS e. recepto posistemės duomenys apie išduotus vaistus, duomenys už 2022 metus"
description: "ESPBI IS e. recepto posistemės duomenys apie išduotus vaistus*."
resource: "https://get.data.gov.lt/datasets/gov/rc/espbiis/receptai_2022/Receptas"
tags: [gov, rc, receptas, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/espbiis/receptai_2022.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/espbiis/receptai_2022.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Receptas — ESPBI IS e. recepto posistemės duomenys apie išduotus vaistus, duomenys už 2022 metus

ESPBI IS e. recepto posistemės duomenys apie išduotus vaistus*. * - vaistas - šiame duomenų rinkinyje naudojamas kaip bendrinis pavadinimas visiems su receptu skiriamiems medicininiams produktams (vaistinis preparatas, medicinos pagalbos priemonė (MPP), vardinis vaistas, ekstemporalus vaistas***, kitos priemonės); ** - TLK-10-AM - tarptautinis ligos kodas; kodų sistema, apimanti ligas ir įvairius simptomus, patologines būkles, skundus, socialines aplinkybes, išorines sužeidimų ir ligų priežastis, sudaroma Pasaulinės sveikatos organizacijos (PSO); *** - Ekstemporalus vaistas - (ekstemporalus vaistinis preparatas) - vaistinėje pavieniam pacientui pagal gydytojo receptą ir (arba) sveikatos priežiūros įstaigos užsakymą pagamintas vaistinis preparatas ar pagal vaistinio preparato aprašą pagamintas vaistinis preparatas; **** - ATC kodas ar indeksas - anatominis terapinis cheminis indeksas, suteikiamas vaistams ir medicinos priemonėms, pagal kuriuos jie klasifikuojami, patvirtintas Pasaulio sveikatos organizacijos[^manifest]

- **Model:** `datasets/gov/rc/espbiis/receptai_2022/Receptas`[^manifest]
- **Dataset:** [Elektroninės sveikatos paslaugų ir bendradarbiavimo infrastruktūros informacinės sistema](../receptai_2022.md) (`datasets/gov/rc/espbiis/receptai_2022`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/espbiis/receptai_2022.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/espbiis/receptai_2022.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/espbiis/receptai_2022/Receptas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `dirbt_recepto_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dirbt_recepto_id` | `string` | — | `4` | `open` | — | Dirbtinis išrašyto recepto identifikatorius | — |
| `recepto_metai` | `integer` | — | `2` | `open` | — | Recepto išrašymo metai | — |
| `recepto_ketv` | `integer` | — | `3` | `open` | — | Recepto išrašymo ketvirtis | — |
| `diagnoze` | `string` | — | `2` | `open` | — | Diagnozės (pagal TLK-10-AM** klasifikatorių), pagal kurią išrašytas receptas, kodas | — |
| `vaisto_tipas` | `string` | — | `4` | `open` | — | Skirto vaisto* tipas (vaistas, medicinos pagalbos priemonė (MPP), vardinis vaistas, ekstemporalus vaistas, kitos priemonės) | — |
| `vaisto_bendr_pav` | `string` | — | `3` | `open` | — | Skiriamo vaisto* (vardinio vaisto bendrinis pavadinimas; ekstemporaliam vaistui gaminti naudojamos pagrindinės veikliosios medžiagos pavadinimas) bendrinis pavadinimas | — |
| `vaisto_prek_pav` | `string` | — | `3` | `open` | — | Skiriamo vaisto* ( vardinio vaisto; MPP) prekinis pavadinimas | — |
| `atc_kodas` | `string` | — | `4` | `open` | — | Skiriamo vaisto* ATC**** kodas | — |
| `atc_pav` | `string` | — | `3` | `open` | — | Skiriamo vaisto* ATC**** pavadinimas | — |
| `vaisto_farmac_forma_id` | `number` | — | `4` | `open` | — | Skiriamo bendrinio vaisto arba gaminamos farmacinės formos identifikatorius | — |
| `vaisto_farmac_forma_pav` | `string` | — | `3` | `open` | — | Skiriamo bendrinio vaisto arba gaminamos farmacinės formos pavadinimas | — |
| `vaisto_stiprumas` | `string` | — | `3` | `open` | — | Skiriamo vaisto* stiprumas | — |
| `mpp_aprasymas` | `string` | — | `3` | `open` | — | Skiriamo MPP aprašymas | — |
| `dozuociu_sk` | `number` | — | `3` | `open` | — | Vaisto* dozuočių (MPP vienetų ar kito produkto) skiriamas kiekis | — |
| `dozuociu_sk_vnt_id` | `number` | — | `3` | `open` | — | Skiriamo vaisto* farmacinės formos dozavimui identifikatorius | — |
| `dozuociu_sk_vnt_pav` | `string` | — | `3` | `open` | — | Skiriamo vaisto* farmacinės formos dozavimui pavadinimas | — |
| `vart_budas_id` | `number` | — | `4` | `open` | — | Skiriamo vaisto* vartojimo būdo identifikatorius | — |
| `vart_budas_pav` | `string` | — | `3` | `open` | — | Skiriamo vaisto* vartojimo būdo pavadinimas | — |
| `vien_doze` | `number` | — | `3` | `open` | — | Skiriamo vaisto* vienkartinė dozė (vienu kartu vartojamas vaisto kiekis) | — |
| `vien_doze_vnt_id` | `number` | — | `4` | `open` | — | Skiriamo vaisto* vienkartinės dozės farmacinės formos dozavimui identifikatorius | — |
| `vien_doze_vnt_pav` | `string` | — | `3` | `open` | — | Skiriamo vaisto* vienkartinės dozės farmacinės formos dozavimui pavadinimas | — |
| `vart_daznumas` | `string` | — | `3` | `open` | — | Skiriamo vaisto* vartojimo dažnumas (kartais) per laiko vienetą | — |
| `vart_laikas` | `string` | — | `3` | `open` | — | Skiriamo vaisto* vartojimo laikas (po valgio, prieš miegą) | — |
| `vart_trukme_d` | `number` | — | `3` | `open` | — | Bendra skiriamo vaisto* vartojimo trukmė dienomis | — |
| `gydymui_testi_periodas_d` | `number` | — | `3` | `open` | — | Ilgalaikio gydymo atveju gydymui tęsti išduodamų vaistų* periodas dienomis (bendra skiriamo vaisto vartojimo trukmė/išdavimų skaičius) | — |
| `recepto_galiojimas_d` | `integer` | — | `3` | `open` | — | Išrašyto recepto galiojimo trukmė dienomis | — |
| `kompens_poz` | `number` | — | `3` | `open` | — | Požymis nurodantis, kad vaistas* yra kompensuojamas (0 - nekompensuojamas, 1 - kompensuojamas) | — |
| `vaisto_narkot_poz_id` | `number` | — | `3` | `open` | — | Požymio, nurodančio, ar skiriamas vaistas* yra narkotikas, ar psichotropas, ar prekusorius, ar kompensuojamas tik tęstiniam gydymui, identifikatorius | — |
| `vaisto_narkot_poz_pav` | `string` | — | `3` | `open` | — | Požymio, nurodančio, ar skiriamas vaistas* yra narkotikas, ar psichotropas, ar prekusorius, ar kompensuojamas tik tęstiniam gydymui, pavadinimas | — |
| `recepto_statusas` | `string` | — | `4` | `open` | — | Vaisto* skyrimo bei recepto būsena (completed - pagal išrašytą receptą išduotas vaistas, active - išrašytas receptas dar galioja, tačiau vaistas pagal jį neišduotas, stopped - išrašytas receptas nebegalioja ir vaistas nebuvo išduotas, on hold - vaistas pagal išrašytą receptą rezervuotas | — |
| `org_savivaldybe` | `ref` | [Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `org_savivaldybe._id`) | `4` | `open` | — | Įstaigos, kurioje buvo išrašytas receptas, savivaldybės pavadinimas (jeigu nurodyta - pateikiama pagal juridinio asmens veiklos adresą, jeigu ne - pagal registracijos adresą) | — |
| `gyd_kvalifikacijos_galioja` | `string` | — | `3` | `open` | — | Duomenų rinkinio formavimo metu galiojantį receptą išrašiusio specialisto kvalifikacija | — |
| `pac_lytis` | `string` | — | `4` | `open` | — | Paciento, kuriam išrašytas receptas, lytis (V - vyras, M - moteris) | — |
| `pac_amziaus_gr` | `string` | — | `3` | `open` | — | Paciento, kuriam išrašytas receptas, amžiaus grupę (Iki 17 m., 18-44 m., 45-64 m., Nuo 65 m.) | — |
| `pac_savivaldybe` | `ref` | [Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `pac_savivaldybe._id`) | `4` | `open` | — | Paciento, kuriam išrašytas receptas, deklaruotos gyvenamosios vietos savivaldybė (aktuali duomenų rinkinio formavimo metu) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vaisto_tipas` | `"Vaistas"` | — | — | Vaistas | — |
| `vaisto_tipas` | `"Medicininos pagalbos priemonės"` | — | — | Medicinos pagalbos priemonės | — |
| `vaisto_tipas` | `"Vardinis vaistas"` | — | — | Vardinis vaistas | — |
| `vaisto_tipas` | `"Ekstemporalus vaistas"` | — | — | Ekstemporalus vaistas | — |
| `vaisto_tipas` | `"Kitos priemonės"` | — | — | Kitos priemonės | — |
| `vaisto_tipas` | `"Neatveriama"` | — | — | Neatveriama | — |
| `recepto_statusas` | `"active"` | — | — | Aktyvus | — |
| `recepto_statusas` | `"completed"` | — | — | Pabaigtas | — |
| `recepto_statusas` | `"on hold"` | — | — | Laikomas | — |
| `recepto_statusas` | `"stopped"` | — | — | Sustabdytas | — |
| `recepto_statusas` | `"Neatveriama"` | — | — | Neatveriama | — |
| `pac_lytis` | `"V"` | — | — | Vyras | — |
| `pac_lytis` | `"M"` | — | — | Moteris | — |
| `pac_lytis` | `"Neatveriama"` | — | — | Neatveriama | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `recepto_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `diagnoze` | `update(type: "ref", ref: "/datasets/gov/vlk/tlk10amTlk10am[code]")` | — | `4` | `open` | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/espbiis/receptai_2022.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/espbiis/receptai_2022.csv#L5)
