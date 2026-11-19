---
type: Table
title: "ZemesDarbas — Šiaulių miesto savivaldybės išduoti leidimai žemės darbams"
description: "Informacija apie Šiaulių miesto savivaldybės išduotus leidimus žemės darbams"
resource: "https://get.data.gov.lt/datasets/gov/siauliu_m_sav/leidimu_administravimas/ZemesDarbas"
tags: [gov, siauliu_m_sav, zemesdarbas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/leidimu_administravimas.csv#L34"
    title: "atviriduomenys/manifest — datasets/gov/siauliu_m_sav/leidimu_administravimas.csv#L34"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2912/"
    title: "data.gov.lt DCAT-AP — datasets/gov/siauliu_m_sav/leidimu_administravimas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# ZemesDarbas — Šiaulių miesto savivaldybės išduoti leidimai žemės darbams

Informacija apie Šiaulių miesto savivaldybės išduotus leidimus žemės darbams[^manifest]

- **Model:** `datasets/gov/siauliu_m_sav/leidimu_administravimas/ZemesDarbas`[^manifest]
- **Dataset:** [Šiaulių miesto savivaldybės išduoti leidimai ir jų apmokėjimai](../leidimu_administravimas.md) (`datasets/gov/siauliu_m_sav/leidimu_administravimas`)[^manifest]
- **Manifest CSV:** [datasets/gov/siauliu_m_sav/leidimu_administravimas.csv#L34](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/leidimu_administravimas.csv#L34)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/siauliu_m_sav/leidimu_administravimas/ZemesDarbas` (`deployed`)[^manifest]
- **Provider:** `siauliu_m_sav` — Šiaulių miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `leidimo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `leidimo_id` | `string` | — | `4` | `open` | — | Leidimo identifikatorius | — |
| `adresas` | `string` | — | `4` | `open` | — | Adresas | — |
| `priezastis_zemes_darbams_lt` | `string` | — | `4` | `open` | — | Priežastis, kodėl buvo pradėti žemės darbai | — |
| `ilguma` | `number` | — | `4` | `open` | — | Ilguma | — |
| `platuma` | `number` | — | `4` | `open` | — | Platuma | — |
| `iskastos_zemes_kiekis` | `number` | — | `4` | `open` | — | Iškastos žemės kiekis | — |
| `pasalintos_zemes_kiekis_lt` | `string` | — | `4` | `open` | — | Pašalintos žemės kiekis | — |
| `leidimas_galioja_nuo` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo pradžia | — |
| `planuojamas_leidimo_galiojimas_iki` | `date` | `D` | `4` | `open` | — | Leidimo planuojama galiojimo pabaiga | — |
| `darbai_baigti` | `boolean` | — | `4` | `open` | — | Identifikatorius ar darbai pagal leidimą baigti | — |
| `leidimo_tipas` | `string` | — | `4` | `open` | — | Leidimo tipas | — |
| `leidimo_numeris` | `string` | — | `4` | `open` | — | Leidimo numeris | — |
| `juridinio_asmens_kodas` | `string` | — | `4` | `open` | — | Juridinio asmens, kuriam išduota leidimas, kodas | — |
| `juridinio_asmens_pavadinimas` | `string` | — | `4` | `open` | — | Juridinio asmens, kuriam išduota leidimas, pavadinimas | — |
| `fizinio_asmens_kodas` | `string` | — | `4` | `open` | — | Fizinio asmens, kuriam išduotas leidimas, kodas | — |
| `fizinio_asmens_vardas_pavarde` | `string` | — | `4` | `open` | — | Fizinio asmens, kuriam išduota leidimas, vardas ir pavardė | — |
| `asmens_tipas` | `string` | — | `4` | `open` | — | Asmens tipas | — |
| `vda_asmens_tipas` | `string` | — | `4` | `open` | — | VDA nustatytas asmens tipas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `leidimo_tipas` | `"KasinejimoDarbai.VykdytiZemesDarbus"` | — | — | Licencija išduota vykdyti žemės darbams | — |
| `leidimo_tipas` | `"KasinejimoDarbai.AtitvertiDaliViesojoNaudojimoTeritorijos"` | — | — | Licencija išduota atitverti dalį viešojo naudojimo teritorijos | — |
| `asmens_tipas` | `"LietuvosJuridinis"` | — | — | Juridinis asmuo įsisteigęs Lietuvoje | — |
| `asmens_tipas` | `"LietuvosFizinis"` | — | — | Fizinis asmuo įsisteigęs Lietuvoje | — |
| `asmens_tipas` | `"UzsienioJuridinis"` | — | — | Juridinis asmuo įsisteigęs užsienyje | — |
| `vda_asmens_tipas` | `"Juridinis asmuo"` | — | — | Juridinis asmuo įsisteigęs Lietuvoje | — |
| `vda_asmens_tipas` | `"Fizinis asmuo"` | — | — | Fizinis asmuo Lietuvos pilietis | — |
| `vda_asmens_tipas` | `"Kita"` | — | — | Nenustatytas asmuo | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `priezastis_zemes_darbams_lt` | `update(property: "priezastis_zemes_darbams_lt@lt", type: "text")` | `type` | — | — | — | — | — |
| `pasalintos_zemes_kiekis_lt` | `update(property: "pasalintos_zemes_kiekis_lt@lt", type: "text")` | `type` | — | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/siauliu_m_sav/leidimu_administravimas.csv#L34 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/leidimu_administravimas.csv#L34)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/siauliu_m_sav/leidimu_administravimas (https://data.gov.lt/datasets/2912/)
