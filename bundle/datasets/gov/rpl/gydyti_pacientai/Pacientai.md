---
type: Table
title: "Pacientai — VšĮ Rokiškio psichiatrijos ligoninėje gydytų pacientų duomenys"
description: "Paciento gyvenamosios vietos regionas (miesto ar rajono pavadinimas), atsiuntusi įstaiga, diagnozė, amžius, lytis, gydymosi laikotarpis, gydymo rezultatas"
resource: "https://get.data.gov.lt/datasets/gov/rpl/gydyti_pacientai/Pacientai"
tags: [gov, rpl, pacientai, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rpl/gydyti_pacientai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rpl/gydyti_pacientai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2029/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rpl/gydyti_pacientai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pacientai — VšĮ Rokiškio psichiatrijos ligoninėje gydytų pacientų duomenys

Paciento gyvenamosios vietos regionas (miesto ar rajono pavadinimas), atsiuntusi įstaiga, diagnozė, amžius, lytis, gydymosi laikotarpis, gydymo rezultatas[^manifest]

- **Model:** `datasets/gov/rpl/gydyti_pacientai/Pacientai`[^manifest]
- **Dataset:** [VšĮ Rokiškio psichiatrijos ligoninėje gydytų pacientų duomenys](../gydyti_pacientai.md) (`datasets/gov/rpl/gydyti_pacientai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rpl/gydyti_pacientai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rpl/gydyti_pacientai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rpl/gydyti_pacientai/Pacientai` (`deployed`)[^manifest]
- **Provider:** `rpl` — Rokiškio psichiatrijos ligoninė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `pavarde_vardas` | `string` | — | `4` | `open` | — | Paciento pavardė, vardas | Šifruotas identifikatorius |
| `ak` | `string` | — | `4` | `open` | — | Asmens kodas | Šifruotas identifikatorius |
| `ak_check` | `string` | — | `4` | `open` | — | Asmens kodo automatinis patikrinimas | — |
| `paguldyta` | `date` | `M` | `4` | `open` | — | Paciento guldymo data mėnesio tikslumu | — |
| `israsyta` | `date` | `M` | `4` | `open` | — | Paciento išrašymo data mėnesio tikslumu | — |
| `lovadieniai` | `integer` | `d` | `4` | `open` | — | Lovadienių skaičius | — |
| `tlk10` | `string` | — | `4` | `open` | — | Diagnozė | — |
| `lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `gim_m_gr` | `string` | — | `4` | `open` | — | Paciento gimimo metų grupė, kas 5 m. | — |
| `gim_m` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai (pagal gimimo metų grupę, priskirti pirmi grupėje nurodyti metai, kas 5 m.) | — |
| `miestas` | `string` | — | `2` | `open` | — | Paciento adresas: miestas | — |
| `gyd_istaiga` | `string` | — | `2` | `open` | — | Gydymo įstaigos pavadinimas, kuri išdavė pacientui siuntimą | — |
| `pirmas_kartas` | `boolean` | — | `4` | `open` | — | Pacientas atvyko pirmą kartą | — |
| `ligos_eiga` | `string` | — | `4` | `open` | — | Paciento ligos eiga | — |
| `ligos_baigtis` | `string` | — | `4` | `open` | — | Paciento ligos baigtis | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ak_check` | `"Tinkamas"` | — | — | Tinkamas | — |
| `ak_check` | `"Netinkamas kontrolinis skaitmuo"` | — | — | Netinkamas kontrolinis skaitmuo | — |
| `ak_check` | `"Netinkamas ilgis"` | — | — | Netinkamas ilgis | — |
| `ak_check` | `"Netinkama gimimo data"` | — | — | Netinkama gimimo data | — |
| `ak_check` | `"Netinkamas pirmas skaitmuo"` | — | — | Netinkamas pirmas skaitmuo | — |
| `ligos_eiga` | `"pagerėjo"` | — | — | Pagerėjo | — |
| `ligos_eiga` | `"pablogėjo"` | — | — | Pablogėjo | — |
| `ligos_eiga` | `"nepakito"` | — | — | Nepakito | — |
| `ligos_baigtis` | `"išrašytas"` | — | — | Išrašytas | — |
| `ligos_baigtis` | `"į kitą stac."` | — | — | Perkeltas kitą stacionarą | — |
| `ligos_baigtis` | `"mirė"` | — | — | Mirė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rpl/gydyti_pacientai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rpl/gydyti_pacientai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rpl/gydyti_pacientai (https://data.gov.lt/datasets/2029/)
