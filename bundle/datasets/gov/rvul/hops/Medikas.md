---
type: Table
title: "Medikas — Medikai"
description: "Lentelė „Medikai“. Lentelę sudaro: mediko identifikatorius, asmens kodas, jo validacijos stulpelis, gimimo metai iš tinkamo asmens kodo bei VASPVT Sveikatos priežiūros ir farmacijos specialistų praktikos licencijų registro (LICREG), lytis iš HOPS, tinkamo asmens kodo ir..."
resource: "https://get.data.gov.lt/datasets/gov/rvul/hops/Medikas"
tags: [gov, rvul, medikas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L24"
    title: "atviriduomenys/manifest — datasets/gov/rvul/hops.csv#L24"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3865/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rvul/hops"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Medikas — Medikai

Lentelė „Medikai“. Lentelę sudaro: mediko identifikatorius, asmens kodas, jo validacijos stulpelis, gimimo metai iš tinkamo asmens kodo bei VASPVT Sveikatos priežiūros ir farmacijos specialistų praktikos licencijų registro (LICREG), lytis iš HOPS, tinkamo asmens kodo ir LICREG, kvalifikacija, šifruotas licencijos numeris, licenciją išdavusi įstaiga, išdavimo data, licencijos būsena, būsenos data ir licencijos panaikinimo data. Vienas lentelės įrašas atitinka vieną mediko, licencijos ir jos būsenos kombinaciją. Lentelėje įtraukti visi Respublikinėje Vilniaus universitetinėje ligoninėje dirbę medikai. Dalies medikų licencijų duomenys nėra rodomi, kadangi jų asmens kodų nėra LICREG duomenų bazėje, kas yra įprasta slaugytojams. Nors medikų lytys iš HOPS yra saugomos trimis skirtingais skaitiniais kodais, vienas kodas gali atitikti ne vieną lytį. Licencijos panaikinimo datos stulpelis buvo įtrauktas todėl, kad pavieniais atvejais jis gali nesutapti su būsenos, kai ši yra panaikinta, datos stulpeliu.[^manifest]

- **Model:** `datasets/gov/rvul/hops/Medikas`[^manifest]
- **Dataset:** [Pacientams atliktų operacijų duomenys](../hops.md) (`datasets/gov/rvul/hops`)[^manifest]
- **Manifest CSV:** [datasets/gov/rvul/hops.csv#L24](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L24)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rvul/hops/Medikas` (`deployed`)[^manifest]
- **Provider:** `rvul` — VšĮ Respublikinė Vilniaus universitetinė ligoninė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `id` | `string` | — | `4` | `open` | — | Mediko identifikatorius | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Mediko asmens kodas | — |
| `asmens_kodo_validacija` | `string` | — | `4` | `open` | — | Asmens kodo validacija | — |
| `gimimo_metai_licreg` | `date` | `Y` | `4` | `open` | — | Gimimo metai iš LICREG | — |
| `vda_gimimo_metai_ak` | `date` | `Y` | `4` | `open` | — | Gimimo metai iš asmens kodo | — |
| `lytis_hops` | `string` | — | `4` | `open` | — | Lytis iš HOPS | — |
| `lytis_licreg` | `string` | — | `4` | `open` | — | Lytis iš LICREG | — |
| `vda_lytis_ak` | `string` | — | `4` | `open` | — | Lytis iš asmens kodo | — |
| `kvalifikacijos_pavadinimas` | `string` | — | `4` | `open` | — | Mediko kvalifikacija pagal licenciją | — |
| `licencijos_nr` | `string` | — | `4` | `open` | — | Licencijos šifruotas numeris | — |
| `licencija_isdavusi_institucija` | `string` | — | `4` | `open` | — | Licenciją išdavusi institucija | — |
| `licencijos_isdavimo_data` | `date` | `D` | `4` | `open` | — | Licencijos išdavimo data | — |
| `licencijos_busena` | `string` | — | `4` | `open` | — | Licencijos būsena | — |
| `licencijos_busenos_data` | `date` | `D` | `4` | `open` | — | Licencijos būsenos data | — |
| `licencijos_panaikinimo_data` | `date` | `D` | `4` | `open` | — | Licencijos panaikinimo data | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `asmens_kodo_validacija` | `"Tinkamas"` | — | — | Tinkamas | — |
| `asmens_kodo_validacija` | `"Netinkamas ilgis"` | — | — | Netinkamas ilgis | — |
| `asmens_kodo_validacija` | `"Netinkamas kontrolinis skaitmuo"` | — | — | Netinkamas kontrolinis skaitmuo | — |
| `lytis_hops` | `"M"` | — | — | Moteris | — |
| `lytis_hops` | `"N"` | — | — | Nežinoma | — |
| `lytis_hops` | `"V"` | — | — | Vyras | — |
| `lytis_licreg` | `"M"` | — | — | Moteris | — |
| `lytis_licreg` | `"V"` | — | — | Vyras | — |
| `vda_lytis_ak` | `"M"` | — | — | Moteris | — |
| `vda_lytis_ak` | `"N"` | — | — | Nežinoma | — |
| `licencija_isdavusi_institucija` | `"Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba prie Sveikatos apsaugos ministerijos"` | — | — | Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba prie Sveikatos apsaugos ministerijos | — |
| `licencija_isdavusi_institucija` | `"Odontologų rūmai"` | — | — | Odontologų rūmai | — |
| `licencijos_busena` | `"išduota"` | — | — | Išduota | — |
| `licencijos_busena` | `"panaikinta"` | — | — | Panaikinta | — |
| `licencijos_busena` | `"sustabdyta"` | — | — | Sustabdyta | — |
| `licencijos_busena` | `"patikslinta"` | — | — | Patikslinta | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rvul/hops.csv#L24 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L24)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rvul/hops (https://data.gov.lt/datasets/3865/)
