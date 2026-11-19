---
type: Table
title: "MenesioAtaskaita — Mėnesinė kraujo donavimo vizitų statistika"
description: "\"Mėnesinė kraujo donavimo vizitų statistika iš Higienos instituto Kraujo donorų registro informacinės sistemos."
resource: "https://get.data.gov.lt/datasets/gov/hi/kraujo_donacijos/MenesioAtaskaita"
tags: [gov, hi, menesioataskaita, deployed, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/kraujo_donacijos.csv#L73"
    title: "atviriduomenys/manifest — datasets/gov/hi/kraujo_donacijos.csv#L73"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3889/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/kraujo_donacijos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# MenesioAtaskaita — Mėnesinė kraujo donavimo vizitų statistika

"Mėnesinė kraujo donavimo vizitų statistika iš Higienos instituto Kraujo donorų registro informacinės sistemos. Viena eilutė yra vizitų skaičius atitinkamam donacijos statusui ir datai. Eilutėje nurodomas unikalios eilutės identifikacinis numeris, datos stulpelis, sudarytas iš metų ir mėnesio, donacijos statusas, tipas ir šiems rodikliams paskaičiuotas įvykusių vizitų skaičius."[^manifest]

- **Model:** `datasets/gov/hi/kraujo_donacijos/MenesioAtaskaita`[^manifest]
- **Dataset:** [Kraujo donacijos](../kraujo_donacijos.md) (`datasets/gov/hi/kraujo_donacijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/hi/kraujo_donacijos.csv#L73](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/kraujo_donacijos.csv#L73)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/kraujo_donacijos/MenesioAtaskaita` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA pirminis raktas | "Valstybės duomenų agentūros sugeneruotas unikalios eilutės identifikatorius sudarytas iš stulpelių data, donacijos_statusas, donacijos_tipas" |
| `data` | `date` | `M` | `4` | `open` | — | Data | "Metai ir mėnesis, kuriam skaičiuojamas vizitų skaičius" |
| `donacijos_statusas` | `string` | — | `4` | `open` | — | Donacijos statusas | — |
| `donacijos_tipas` | `string` | — | `4` | `open` | — | Kraujo donavimo tipas | — |
| `vizitu_skaicius` | `integer` | — | `4` | `open` | — | Vizitų skaičius | "Įvykusių vizitų skaičius atitinkamam donacijos statusui ir nurodytam metų mėnesiui" |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `donacijos_statusas` | `"Donacija sėkminga"` | — | — | Donacija sėkminga | "Apsilankymo būsena priskiriama, kai po atrankinių/patvirtinamųjų kraujo tyrimų rezultatų gavimo yra gydytojo sprendimas leisti donorystę. Esant šiai būsenai skaitoma, kad donoras davė kraujo ar jo komponentų – donacija atlikta" |
| `donacijos_statusas` | `"Donacija nutraukta"` | — | — | Donacija nutraukta | "Apsilankymo būsena priskiriama, kai, KDĮ perdavus donacijos numerį ir registre jai automatiškai suteikus donacijos identifikavimo kodą, donacija dėl tam tikrų priežasčių nebuvo atlikta. Esant šiai būsenai skaitoma, kad donacija neatlikta, t.y. donoras nedavė kraujo ar jo komponentų" |
| `donacijos_statusas` | `"Donacija nesėkminga"` | — | — | Donacija nesėkminga | "Apsilankymo būsena priskiriama, kai po atrankinių/patvirtinamųjų kraujo tyrimų rezultatų gavimo yra gydytojo sprendimas uždrausti arba laikinai sustabdyti donorystę. Esant šiai būsenai skaitoma, kad donoras davė kraujo ar jo komponentų – donacija atlikta" |
| `donacijos_statusas` | `"Atranka nesėkminga"` | — | — | Atranka nesėkminga | "Apsilankymo būsena priskiriama, kai KDĮ perduoda gydytojo sprendimą, priimtą atrankos metu, uždrausti arba laikinai sustabdyti donaciją/donorystę" |
| `donacijos_statusas` | `"Donacija pradėta"` | — | — | Donacija pradėta | "Apsilankymo būsena priskiriama, kai KDĮ perduoda registrui savo suteiktą KDĮ donacijos numerį, o registras jai automatiškai suteikia donacijos identifikavimo kodą. Esant šiai būsenai skaitoma, kad donacija atlikta, tačiau ji gali būti nutraukta. Ši būsena rodoma tol, kol registrui neperduotas KDĮ gydytojo sprendimas dėl tolesnės donorystės, kuris priimamas po atrankinių/patvirtinamųjų kraujo tyrimų rezultatų gavimo" |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/kraujo_donacijos.csv#L73 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/kraujo_donacijos.csv#L73)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/kraujo_donacijos (https://data.gov.lt/datasets/3889/)
