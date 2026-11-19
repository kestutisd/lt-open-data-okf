---
type: Table
title: "DarboSkelbimas — Aktualūs darbo skelbimai viešajame sektoriuje"
description: "Valstybės tarnybos portale viešinami konkursai bei atrankos į valstybės ir savivaldybių institucijų bei įstaigų laisvas darbo pozicijas."
resource: "https://get.data.gov.lt/datasets/gov/ird/vataras_vatis/DarboSkelbimas"
tags: [gov, ird, darboskelbimas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/vataras_vatis.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/ird/vataras_vatis.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1240/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ird/vataras_vatis"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# DarboSkelbimas — Aktualūs darbo skelbimai viešajame sektoriuje

Valstybės tarnybos portale viešinami konkursai bei atrankos į valstybės ir savivaldybių institucijų bei įstaigų laisvas darbo pozicijas. Trys darbo skelbimų kategorijos: 1) Konkursų į karjeros valstybės tarnautojų pareigas skelbimai; 2) Atrankų į pakaitinių valstybės tarnautojų pareigas skelbimai; 3) Konkursų į darbuotojų, dirbančių pagal darbo sutartį, pareigas skelbimai. Pateikiami tik galiojantys (aktualūs) skelbimai. Lentelė atnaujinama kas dieną. Atlyginimo apskaičiavime naudojamas 2023 m. pareiginės algos bazinis dydis (nuo 2024 m. keisis skaičiavimo metodika). Detalesnę skelbimų informaciją galima surasti https://portalas.vtd.lt/, ieškant pagal skelbimo numerį. Duomenų šaltinis - VATIS ir VATARAS. Dėl techninių klausimų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/ird/vataras_vatis/DarboSkelbimas`[^manifest]
- **Dataset:** [Valstybės tarnautojų registras, Valstybės tarnybos valdymo informacinė sistema](../vataras_vatis.md) (`datasets/gov/ird/vataras_vatis`)[^manifest]
- **Manifest CSV:** [datasets/gov/ird/vataras_vatis.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/vataras_vatis.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/vataras_vatis/DarboSkelbimas` (`deployed`)[^manifest]
- **Provider:** `ird` — Informatikos ir ryšių departamentas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus skelbimo identifikatorius (techninėms reikmėms) | — |
| `galiojimo_pradzia` | `date` | `D` | `4` | `open` | — | Skelbimo galiojimo pradžia | Imtinai |
| `galiojimo_pabaiga` | `date` | `D` | `4` | `open` | — | Skelbimo galiojimo pabaiga | Imtinai. Laikinai pateikiama apytikslė galiojimo pabaigos data (pvz., neatsižvelgianti į valstybines šventines dienas) |
| `pozicijos_tipas` | `string` | — | `4` | `open` | — | Darbo pozicijos tipas | — |
| `pareigos` | `string` | — | `4` | `open` | — | Pareigų aprašymas | Nestruktūrizuotas tekstas, pateikiamas taip, kaip pateikė įstaiga |
| `pa_koeficientas` | `number` | `U` | `4` | `open` | — | Numatytas pareiginės algos koeficientas | Tik valstybės tarnautojams ir pakaitiniams valstybės tarnautojams |
| `bruto` | `number` | — | `2` | `open` | — | Apskaičiuotas atlyginimas prieš mokesčius | — |
| `miestas` | `string` | — | `2` | `open` | — | Miestas, kuriame yra darbo vieta | — |
| `istaiga` | `string` | — | `2` | `open` | — | Skelbimą inicijavusios įstaigos pavadinimas | — |
| `jar_kodas` | `string` | — | `2` | `open` | — | Skelbimą inicijavusios įstaigos juridinių asmenų registro kodas | — |
| `teisine_forma` | `string` | — | `3` | `open` | — | Skelbimą inicijavusios įstaigos teisinė forma | — |
| `organizatorius` | `string` | — | `2` | `open` | — | Organizuojančios įstaigos pavadinimas | — |
| `info_email` | `string` | — | `4` | `open` | — | El. pašto adresas pasiteiravimui dėl skelbimo | — |
| `numeris` | `string` | — | `4` | `open` | — | Unikalus skelbimo numeris (komunikacijai, paieškai) | — |
| `adresas` | `url` | — | `4` | `open` | — | Išsamaus skelbimo turinio URL adresas | Laikinai pateikiamas tik bendrasis Valstybės portalo adresas |
| `atnaujinimas` | `date` | `D` | `4` | `open` | — | Naujausio įrašo arba modifikacijos data gaunamuose duomenyse | Paruošiamas imant naujausio įrašo originaliuose duomenyse datą |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pozicijos_tipas` | `'valstybės tarnautojas'` | — | — | Valstybės tarnautojo pozicijos konkursas | — |
| `pozicijos_tipas` | `'pagal darbo sutartį'` | — | — | Skelbimas pagal darbo sutartį | — |
| `pozicijos_tipas` | `'pakaitinis valstybės tarnautojas'` | — | — | Pakaitinių valstybės tarnautojų atranka | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `bruto` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/vataras_vatis.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/vataras_vatis.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ird/vataras_vatis (https://data.gov.lt/datasets/1240/)
