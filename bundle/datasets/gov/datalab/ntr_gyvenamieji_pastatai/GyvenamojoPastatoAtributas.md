---
type: Table
title: "GyvenamojoPastatoAtributas — Pastatų atributas"
description: "Spinta table datasets/gov/datalab/ntr_gyvenamieji_pastatai/GyvenamojoPastatoAtributas (41 columns)."
resource: "https://get.data.gov.lt/datasets/gov/datalab/ntr_gyvenamieji_pastatai/GyvenamojoPastatoAtributas"
tags: [gov, datalab, gyvenamojopastatoatributas, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/datalab/ntr_gyvenamieji_pastatai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/datalab/ntr_gyvenamieji_pastatai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3916/"
    title: "data.gov.lt DCAT-AP — datasets/gov/datalab/ntr_gyvenamieji_pastatai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# GyvenamojoPastatoAtributas — Pastatų atributas

- **Model:** `datasets/gov/datalab/ntr_gyvenamieji_pastatai/GyvenamojoPastatoAtributas`[^manifest]
- **Dataset:** [NTR pastatų atributai](../ntr_gyvenamieji_pastatai.md) (`datasets/gov/datalab/ntr_gyvenamieji_pastatai`)[^manifest]
- **Manifest CSV:** [datasets/gov/datalab/ntr_gyvenamieji_pastatai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/datalab/ntr_gyvenamieji_pastatai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/datalab/ntr_gyvenamieji_pastatai/GyvenamojoPastatoAtributas` (`deployed`)[^manifest]
- **Provider:** `datalab` — Valstybės duomenų agentūra (DataLab) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | VDA ID | — |
| `obj_kodas` | `string` | — | `4` | `open` | — | Objekto kodas | — |
| `pastato_panaudojimas` | `string` | — | `4` | `open` | — | Pastato naudojimo paskirtis | — |
| `obje_tipas` | `string` | — | `4` | `open` | — | Objekto tipas | — |
| `obje_pav` | `string` | — | `4` | `open` | — | Objekto pavadinimas | — |
| `sav_kodas` | `string` | — | `4` | `open` | — | Savivaldybės kodas | — |
| `sav_pav` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |
| `sen_kodas` | `string` | — | `4` | `open` | — | Seniūnijos kodas | — |
| `sen_pav` | `string` | — | `4` | `open` | — | Seniūnijos pavadinimas | — |
| `gyv_id_pav` | `string` | — | `4` | `open` | — | Gyvenvietės pavadinimas | — |
| `aob_kodas` | `string` | — | `4` | `open` | — | AOB kodas (adreso objektas) | — |
| `statinio_kategorija` | `string` | — | `4` | `open` | — | Statinio kategorija | — |
| `statybos_pradzios_metai` | `integer` | — | `4` | `open` | — | Statybos pradžia | — |
| `statybos_pabaigos_metai` | `integer` | — | `4` | `open` | — | Statybos pabaiga | — |
| `rekonstravimo_pabaigos_metai` | `integer` | — | `4` | `open` | — | Rekonstrukcijos pabaiga | — |
| `rekonstravimo_pradzios_metai` | `integer` | — | `4` | `open` | — | Rekonstrukcijos pradžia | — |
| `baigtumo_procentas` | `integer` | — | `4` | `open` | — | Baigtumas (%) | — |
| `aukstu_skaicius` | `number` | — | `4` | `open` | — | Aukštų skaičius | — |
| `bendras_plotas` | `number` | — | `4` | `open` | — | Bendras plotas (kv. m) | — |
| `gyvenamasis_plotas` | `number` | — | `4` | `open` | — | Gyvenamasis plotas (kv. m) | — |
| `rusiu_pusrusiu_plotas` | `number` | — | `4` | `open` | — | Rūsių/pusrūsių plotas (kv. m) | — |
| `verslo_plotas` | `number` | — | `4` | `open` | — | Verslo plotas (kv. m) | — |
| `elektra` | `boolean` | — | `4` | `open` | — | Ar yra elektra | — |
| `vandentiekis` | `boolean` | — | `4` | `open` | — | Ar yra vandentiekis | — |
| `karstas_vanduo` | `boolean` | — | `4` | `open` | — | Ar yra karštas vanduo | — |
| `nuoteku_salinimas` | `boolean` | — | `4` | `open` | — | Ar yra nuotekų šalinimas | — |
| `sildymas` | `boolean` | — | `4` | `open` | — | Šildymo tipas arba buvimas | — |
| `dujos` | `boolean` | — | `4` | `open` | — | Ar yra dujos | — |
| `rusys` | `boolean` | — | `4` | `open` | — | Ar yra rūsys | — |
| `vedinimas_ir_kondicionavimas` | `boolean` | — | `4` | `open` | — | Vėdinimas ir kondicionavimas | — |
| `pastato_jo_dalies_energetinio_naudingumo_klase_new` | `string` | — | `4` | `open` | — | Energetinio naudingumo klasė | — |
| `energetinio_naudingumo_grupes` | `string` | — | `4` | `open` | — | Energetinio naudingumo grupė | — |
| `silumines_sanaudos_vienam_kv_m` | `number` | — | `4` | `open` | — | Šilumos sąnaudos 1 kv. m | — |
| `co2` | `number` | — | `4` | `open` | — | CO2 emisijos | — |
| `combined_energetinio_naudingumo_grupes_rf3_naujas` | `string` | — | `4` | `open` | — | Energ. naudingumo grupė | — |
| `combined_silumines_sanaudos_vienam_kv_m_round` | `number` | — | `4` | `open` | — | Šilumos sąnaudos | — |
| `co2_round` | `number` | — | `4` | `open` | — | Apvalintos CO₂ emisijos | — |
| `combined_co2_vienam_kv_m_round` | `number` | — | `4` | `open` | — | Kombinuotos apvalintos CO₂ emisijos | — |
| `atnaujinimo_laikas` | `datetime` | `S` | `4` | `open` | — | Duomenų atnaujinimo data | — |
| `salis` | `string` | — | `4` | `open` | — | Šalis | — |
| `geo_new` | `string` | — | `4` | `open` | — | Geografinė koordinatė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/datalab/ntr_gyvenamieji_pastatai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/datalab/ntr_gyvenamieji_pastatai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/datalab/ntr_gyvenamieji_pastatai (https://data.gov.lt/datasets/3916/)
