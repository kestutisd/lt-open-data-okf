---
type: Table
title: "Pazymejimas — Išduotų galiojančių vairuotojų pažymėjimų duomenys"
description: "AB \"Regitra\" išduotų ir galiojančių vairuotojų pažymėjimų duomenys"
resource: "https://get.data.gov.lt/datasets/gov/regitra/ktpvr/Pazymejimas"
tags: [gov, regitra, pazymejimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/ktpvr.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/regitra/ktpvr.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2934/"
    title: "data.gov.lt DCAT-AP — datasets/gov/regitra/ktpvr"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pazymejimas — Išduotų galiojančių vairuotojų pažymėjimų duomenys

AB "Regitra" išduotų ir galiojančių vairuotojų pažymėjimų duomenys[^manifest]

- **Model:** `datasets/gov/regitra/ktpvr/Pazymejimas`[^manifest]
- **Dataset:** [Išduotų galiojančių vairuotojų pažymėjimų duomenys](../ktpvr.md) (`datasets/gov/regitra/ktpvr`)[^manifest]
- **Manifest CSV:** [datasets/gov/regitra/ktpvr.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/ktpvr.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/regitra/ktpvr/Pazymejimas` (`deployed`)[^manifest]
- **Provider:** `regitra` — AB „Regitra“ *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vairuotojo_pazymejimo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vairuotojo_pazymejimo_id` | `string` | — | `4` | `open` | — | Šifruotas vairuotojo pažymėjimo identifikatorius | — |
| `asmens_id` | `string` | — | `4` | `open` | — | Šifruotas asmens identifikatorius | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Šifruotas asmens kodas | — |
| `vda_asmens_kodo_validacija` | `string` | — | `4` | `open` | — | VDA atliktas asmens kodo tikrinimas | — |
| `pazymejimas_galioja_nuo` | `date` | `D` | `4` | `open` | — | Išduotas vairuotojo pažymėjimas galioja nuo | — |
| `galiojimo_busena` | `string` | — | `4` | `open` | — | Vairuotojo pažymėjimo galiojimo busena | — |
| `kraujo_grupe_abo` | `string` | — | `4` | `open` | — | Asmens kraujo grupė | — |
| `kraujo_grupes_rezus` | `string` | — | `4` | `open` | — | Asmens kraujo grupės rezus faktorius | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Asmens gimimo metai | — |
| `vda_gimimo_metai_ask` | `date` | `Y` | `4` | `open` | — | VDA iš asmens kodo nustatyti asmens gimimo metai | — |
| `lytis` | `string` | — | `4` | `open` | — | Asmens lytis | — |
| `vda_lytis_is_ak` | `string` | — | `4` | `open` | — | VDA iš asmens kodo nustatyta lytis | — |
| `asmens_gimimo_salis` | `string` | — | `4` | `open` | — | Asmens gimimo šalis | — |
| `vairuotojo_kategorijos` | `string` | — | `4` | `open` | — | Vairuotojo pažymėjime nurodytos vairuotojo kategorijos | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vda_asmens_kodo_validacija` | `"Tinkamas"` | — | — | Tinkamas asmens kodas | — |
| `vda_asmens_kodo_validacija` | `"Netinkamas ilgis"` | — | — | Netinkamas asmens kodo ilgis | — |
| `vda_asmens_kodo_validacija` | `"Netinkamas kontrolinis skaitmuo"` | — | — | Netinkamas kontrolinis skaitmuo | — |
| `vda_asmens_kodo_validacija` | `"Netinkamas pirmas skaitmuo"` | — | — | Netinkamas pirmas skaitmuo | — |
| `vda_asmens_kodo_validacija` | `"Netinkama gimimo data"` | — | — | Netinkama gimimo data | — |
| `galiojimo_busena` | `"Galioja"` | — | — | Vairuotojo pažymėjimas galioja | — |
| `kraujo_grupe_abo` | `"I( O )"` | — | — | Pirma grupė | — |
| `kraujo_grupe_abo` | `"II( A )"` | — | — | Antra grupė | — |
| `kraujo_grupe_abo` | `"III( B )"` | — | — | Trečia grupė | — |
| `kraujo_grupe_abo` | `"IV( AB )"` | — | — | Ketvirta grupė | — |
| `kraujo_grupe_abo` | `"Cenzūruota"` | — | — | Cenzūruota | — |
| `kraujo_grupes_rezus` | `"+"` | — | — | Teigimas | — |
| `kraujo_grupes_rezus` | `"-"` | — | — | Neigiamas | — |
| `kraujo_grupes_rezus` | `"Cenzūruota"` | — | — | Cenzūruta | — |
| `lytis` | `"Vyras"` | — | — | Vyras | — |
| `lytis` | `"Moteris"` | — | — | Moteris | — |
| `vda_lytis_is_ak` | `"Vyras"` | — | — | Vyras | — |
| `vda_lytis_is_ak` | `"Moteris"` | — | — | Moteris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/regitra/ktpvr.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/ktpvr.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/regitra/ktpvr (https://data.gov.lt/datasets/2934/)
