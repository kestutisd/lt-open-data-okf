---
type: Table
title: "KonteinerioIsvezimas"
description: "Rinkinys sudarytas iš SĮ „Vilniaus atliekų sistemos administratorius“ (VASA) atliekų tvarkymo informacinių sistemų „ASMLIS“ ir „SAVITARNA“ duomenų."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas/KonteinerioIsvezimas"
tags: [gov, vilniaus_m_sav, konteinerioisvezimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L12"
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L12"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3897/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/atlieku_tvarkymas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# KonteinerioIsvezimas

**Dataset Context:** Rinkinys sudarytas iš SĮ „Vilniaus atliekų sistemos administratorius“ (VASA) atliekų tvarkymo informacinių sistemų „ASMLIS“ ir „SAVITARNA“ duomenų. Rinkinį sudaro lentelės, kuriose pateikiama išsami informacija apie atliekų surinkimo infrastruktūrą, planuojamus išvežimus ir istorinius surinkimo duomenis. Išvežimų tvarkaraščių lentelėje pateikiama informacija apie atliekų surinkimo taškus ir jų aptarnavimo tvarkaraščius. Viena eilutė atitinka artimiausią konteinerio išvežimo informaciją: konteinerio identifikacinius duomenis, jo charakteristikas, aptarnavimo informaciją ir geografinius duomenis. Konteinerių išvežimų lentelėje pateikiamas faktinių atliekų surinkimo operacijų žurnalas. Viena eilutė atitinka vieną konteinerio aptarnavimo operaciją. Lentelėje galima rasti konteinerių informaciją, surinktų atliekų kiekius, operacijų detales, geografines operacijų vietas. Išvežimų tvarkaraščių ir konteinerių išvežimų lentelių duomenys pateikiami nuo 2023 m. sausio mėnesio pradžios. Šias dvi lenteles tarpusavyje galima jungti per „inventorinis_nr“ raktą. Didelių gabaritų atliekų lentelėje pateikiami individualių atliekų paėmimų užsakymai nuo 2023 m. spalio mėnesio pabaigos. Vienas užsakymas gali apimti kelias skirtingas daiktų grupes, todėl jie išdėstyti atskirose lentelės eilutėse. Duomenų teikėjas – SĮ „Vilniaus atliekų sistemos administratorius“. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/vilniaus_m_sav/atlieku_tvarkymas/KonteinerioIsvezimas`[^manifest]
- **Dataset:** [Vilniaus atliekų sistemos administratoriaus atliekų tvarkymas](../atlieku_tvarkymas.md) (`datasets/gov/vilniaus_m_sav/atlieku_tvarkymas`)[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L12](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L12)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas/KonteinerioIsvezimas` (`deployed`)[^manifest]
- **Provider:** `vilniaus_m_sav` — Vilniaus miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `pickup_history_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **URI:** `Faktinių atliekų surinkimo operacijų žurnalas`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pickup_history_id` | `string` | — | `4` | `open` | — | Konteinerių išvežimai | Atliekų surinkimo archyvinis identifikatorius |
| `dumpster_id` | `string` | — | `4` | `open` | — | Konteinerio identifikatorius | — |
| `inventorinis_nr` | `string` | — | `4` | `open` | — | Inventoriaus numeris | — |
| `konteinerio_turis` | `number` | — | `4` | `open` | — | Tūris | — |
| `papildomas_turis` | `number` | — | `4` | `open` | — | Papildomas tūris | — |
| `apskaiciuotas_svoris` | `number` | — | `4` | `open` | — | Apskaičiuotos atliekos | — |
| `veiksmo_data` | `datetime` | — | `4` | `open` | — | Veiksmo data | — |
| `veiksmas` | `string` | — | `4` | `open` | — | Veiksmas | — |
| `aptarnavimas` | `string` | — | `4` | `open` | — | Aptarnavimo tipas | — |
| `komentaras` | `string` | — | `4` | `open` | — | Komentaras | — |
| `tvarkytojas` | `string` | — | `4` | `open` | — | Atliekų tvarkytojo pavadinimas | — |
| `geometrija` | `geometry(point, 4326)` | — | `4` | `open` | — | Geometrija | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `veiksmas` | `"Ištuštinti"` | — | — | Ištuštinti | — |
| `veiksmas` | `"Pastatyti"` | — | — | Pastatyti | — |
| `veiksmas` | `"Nuimti"` | — | — | Nuimti | — |
| `veiksmas` | `"Informacinis užsakymas"` | — | — | Informacinis užsakymas | — |
| `veiksmas` | `"Pakeisti"` | — | — | Pakeisti | — |
| `aptarnavimas` | `"Aptarnautas"` | — | — | Aptarnautas | — |
| `aptarnavimas` | `"Neaptarnautas"` | — | — | Neaptarnautas | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L12 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/atlieku_tvarkymas.csv#L12)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/atlieku_tvarkymas (https://data.gov.lt/datasets/3897/)
