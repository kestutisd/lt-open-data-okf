---
type: Table
title: "KelionesAtvykSuNakv2021 — Atvykusių turistų kelionės su nakvyne 2021 m."
description: "Spinta table datasets/gov/lsd/turizmas/atvyksta/KelionesAtvykSuNakv2021 (55 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/turizmas/atvyksta/KelionesAtvykSuNakv2021"
tags: [gov, lsd, kelionesatvyksunakv2021, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/turizmas/atvyksta.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/lsd/turizmas/atvyksta.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2079/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/turizmas/atvyksta"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# KelionesAtvykSuNakv2021 — Atvykusių turistų kelionės su nakvyne 2021 m.

- **Model:** `datasets/gov/lsd/turizmas/atvyksta/KelionesAtvykSuNakv2021`[^manifest]
- **Dataset:** [Atvykstamojo turizmo statistiniai tyrimai](../atvyksta.md) (`datasets/gov/lsd/turizmas/atvyksta`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/turizmas/atvyksta.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/turizmas/atvyksta.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/turizmas/atvyksta/KelionesAtvykSuNakv2021` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Respondento kodas | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | Respondento lytis |
| `amzius` | `string` | — | `4` | `open` | — | Amžiaus grupė | Respondento amžiaus grupė |
| `gyv_salis` | `string` | — | `3` | `open` | — | Gyvenamoji šalis | Respondento nuolatinė gyvenamoji šalis arba jų grupė |
| `gyv_salies_kodas` | `string` | — | `2` | `open` | — | Gyvenamosios šalies kodas | Respondento nuolatinė gyvenamoji šalis (dviraidis kodas) arba jų grupė (tuščia) |
| `apkl_vieta` | `string` | — | `3` | `open` | — | Apklausos atlikimo vieta | — |
| `ketvirtis` | `string` | — | `3` | `open` | — | Metų ketvirtis | — |
| `tikslas` | `string` | — | `4` | `open` | — | Kelionės tikslas | — |
| `transporto_priemone` | `string` | — | `4` | `open` | — | Transporto priemonė | Pagrindinė transporto priemonė, kuria keliavo |
| `vertinimas` | `integer` | — | `4` | `open` | — | Kaip vertina kelionę | — |
| `pirmakart` | `integer` | `enum: bool` | `4` | `open` | — | Ar pirmąkart lankėsi Lietuvoje | — |
| `info_agentura` | `integer` | `enum: bool` | `4` | `open` | — | Informacijos apie Lietuvą šaltinis - kelionių agentūra | — |
| `info_reklama` | `integer` | `enum: bool` | `4` | `open` | — | Informacijos apie Lietuvą šaltinis - reklama | — |
| `info_draugai` | `integer` | `enum: bool` | `4` | `open` | — | Informacijos apie Lietuvą šaltinis - draugai ir giminės | — |
| `info_verslopartn` | `integer` | `enum: bool` | `4` | `open` | — | Informacijos apie Lietuvą šaltinis - verslo partneriai | — |
| `info_gidas` | `integer` | `enum: bool` | `4` | `open` | — | Informacijos apie Lietuvą šaltinis - kelionės vadovas | — |
| `info_internetas` | `integer` | `enum: bool` | `4` | `open` | — | Informacijos apie Lietuvą šaltinis - internetas | — |
| `info_isanksciau` | `integer` | `enum: bool` | `4` | `open` | — | Informacijos apie Lietuvą šaltinis - ankstesnis vizitas | — |
| `info_kt` | `integer` | `enum: bool` | `4` | `open` | — | Informacijos apie Lietuvą šaltinis - kita | — |
| `lanke_vilnius` | `integer` | `enum: bool` | `4` | `open` | — | Aplankė Vilnių | — |
| `lanke_kaunas` | `integer` | `enum: bool` | `4` | `open` | — | Aplankė Kauną | — |
| `lanke_klaipeda` | `integer` | `enum: bool` | `4` | `open` | — | Aplankė Klaipėdą | — |
| `lanke_palanga` | `integer` | `enum: bool` | `4` | `open` | — | Aplankė Palangą | — |
| `lanke_trakai` | `integer` | `enum: bool` | `4` | `open` | — | Aplankė Trakus | — |
| `lanke_birstonas` | `integer` | `enum: bool` | `4` | `open` | — | Aplankė Birštoną | — |
| `lanke_druskininkai` | `integer` | `enum: bool` | `4` | `open` | — | Aplankė Druskininkus | — |
| `lanke_kursiunerija` | `integer` | `enum: bool` | `4` | `open` | — | Aplankė Kuršių Neriją | — |
| `lanke_alytkaunmarijapskr` | `integer` | `enum: bool` | `4` | `open` | — | Aplankė Alytaus, Kauno arba Marijampolės apskritis | — |
| `lanke_klaiptelsiutauragapskr` | `integer` | `enum: bool` | `4` | `open` | — | Aplankė Klaipėdos, Telšių arba Tauragės apskritis | — |
| `lanke_siauliupanevezapskr` | `integer` | `enum: bool` | `4` | `open` | — | Aplankė Šiaulių arba Panevėžio apskritis | — |
| `lanke_utenosvilniausapskr` | `integer` | `enum: bool` | `4` | `open` | — | Aplankė Utenos arba Vilniaus apskritis | — |
| `islaid_pries` | `integer` | — | `2` | `open` | — | Išlaidos prieš kelionę | Visos išlaidos čia pateiktos vienam asmeniui (respondento nurodytos išlaidos padalintos iš asmenų skaičiaus); apima paslaugų paketą, vizą ir kitas išlaidas prieš kelionę |
| `zmoniu_sk_pries` | `integer` | `U` | `4` | `open` | — | Žmonių skaičius, kuriam nurodytos išlaidos prieš kelionę | — |
| `islaid_paketui` | `integer` | — | `2` | `open` | — | Išlaidos paslaugų paketui | Nurodyta vidutinė kaina vienai šaliai, jei paslaugų paketas apima kelias šalis |
| `islaid_vizai` | `integer` | — | `2` | `open` | — | Išlaidos vizai ir kitiems kelionės dokumentams | — |
| `islaid_ktpries` | `integer` | — | `2` | `open` | — | Kitos išlaidos prieš kelionę | Apima bilietus į renginius ir kt., išskyrus kelionės bilietus |
| `saliu_pakete` | `integer` | `U` | `4` | `open` | — | Kiek šalių apėmė paslaugų paketas | — |
| `islaid_lt` | `integer` | — | `2` | `open` | — | Išlaidos Lietuvoje | Visos išlaidos čia pateiktos vienam asmeniui (respondento nurodytos išlaidos padalintos iš asmenų skaičiaus) |
| `zmoniu_sk` | `integer` | `U` | `4` | `open` | — | Žmonių skaičius, kuriam nurodytos išlaidos Lietuvoje | — |
| `islaid_apgyvend` | `integer` | — | `2` | `open` | — | Išlaidos apgyvendinimui | Konfidencialumo tikslais prie vertės pridėta arba atimta triukšmo, sudarančio ne daugiau kaip 10% vertės |
| `islaid_maistui` | `integer` | — | `2` | `open` | — | Išlaidos maistui | Išlaidos maistui, įskaitant maistą restoranuose ir parduotuvėse |
| `islaid_restoranuose` | `integer` | — | `2` | `open` | — | Išlaidos maistui restoranuose | Įskaitant kavines, barus ir kt. |
| `islaid_parduotuvese` | `integer` | — | `2` | `open` | — | Išlaidos maistui parduotuvėse | — |
| `islaid_transportui` | `integer` | — | `2` | `open` | — | Išlaidos transportui Lietuvoje | Išlaidos apima degalus, transporto nuomą, remontą, viešąjį transportą, bet ne degalus, pirktus parduoti |
| `islaid_degalams` | `integer` | — | `2` | `open` | — | Išlaidos degalams | — |
| `islaid_trnuomai` | `integer` | — | `2` | `open` | — | Išlaidos transporto nuomai | — |
| `islaid_trremontui` | `integer` | — | `2` | `open` | — | Išlaidos transporto remontui | — |
| `islaid_viesajamtr` | `integer` | — | `2` | `open` | — | Išlaidos viešajam transportui ir taksi | — |
| `islaid_laisvalaikiui` | `integer` | — | `2` | `open` | — | Išlaidos laisvalaikiui ir kultūrai | — |
| `islaid_pirkiniams` | `integer` | — | `2` | `open` | — | Išlaidos pirkiniams | — |
| `islaid_pirkmasinai` | `integer` | — | `2` | `open` | — | Išlaidos pirktam automobiliui | Išlaidos neįtraukia automobilių, pirktų perparduoti |
| `islaid_kt` | `integer` | — | `2` | `open` | — | Kitos išlaidos | — |
| `islaid_viso` | `integer` | — | `2` | `open` | — | Viso išlaidų | Visos išlaidos čia pateiktos vienam asmeniui (respondento nurodytos išlaidos padalintos iš asmenų skaičiaus) |
| `naktys` | `integer` | `U` | `4` | `open` | — | Kiek naktų praleido Lietuvoje | — |
| `apgyv_tipas` | `string` | — | `4` | `open` | — | Apgyvendinimo tipas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"1"` | — | — | Vyras | — |
| `lytis` | `"2"` | — | — | Moteris | — |
| `amzius` | `"1"` | — | — | 15-24 | — |
| `amzius` | `"2"` | — | — | 25-34 | — |
| `amzius` | `"3"` | — | — | 35-44 | — |
| `amzius` | `"4"` | — | — | 45-54 | — |
| `amzius` | `"5"` | — | — | 55-64 | — |
| `amzius` | `"6"` | — | — | 65+ | — |
| `tikslas` | `"1"` | — | — | Laisvalaikis | — |
| `tikslas` | `"26"` | — | — | Verslas | — |
| `tikslas` | `"3"` | — | — | Draugų ir giminių lankymas | — |
| `tikslas` | `"4"` | — | — | Sveikatinimo tikslai | — |
| `tikslas` | `"5"` | — | — | Pirkiniai | — |
| `tikslas` | `"7"` | — | — | Kita | — |
| `transporto_priemone` | `"1"` | — | — | Lengvasis automobilis | — |
| `transporto_priemone` | `"2"` | — | — | Maršrutinis autobusas | — |
| `transporto_priemone` | `"3"` | — | — | Nereguliarių reisų autobusas | — |
| `transporto_priemone` | `"4"` | — | — | Traukinys | — |
| `transporto_priemone` | `"5"` | — | — | Lėktuvas | — |
| `transporto_priemone` | `"6"` | — | — | Laivas, keltas | — |
| `transporto_priemone` | `"78"` | — | — | Kita | — |
| `vertinimas` | `1` | — | — | Labai gerai | — |
| `vertinimas` | `2` | — | — | Gerai | — |
| `vertinimas` | `3` | — | — | Patenkinamai | — |
| `vertinimas` | `4` | — | — | Blogai | — |
| `vertinimas` | `5` | — | — | Labai blogai | — |
| `pirmakart` | `1` | — | — | Taip | — |
| `pirmakart` | `0` | — | — | Ne | — |
| `info_agentura` | `1` | — | — | Taip | — |
| `info_agentura` | `0` | — | — | Ne | — |
| `info_reklama` | `1` | — | — | Taip | — |
| `info_reklama` | `0` | — | — | Ne | — |
| `info_draugai` | `1` | — | — | Taip | — |
| `info_draugai` | `0` | — | — | Ne | — |
| `info_verslopartn` | `1` | — | — | Taip | — |
| `info_verslopartn` | `0` | — | — | Ne | — |
| `info_gidas` | `1` | — | — | Taip | — |
| `info_gidas` | `0` | — | — | Ne | — |
| `info_internetas` | `1` | — | — | Taip | — |
| `info_internetas` | `0` | — | — | Ne | — |
| `info_isanksciau` | `1` | — | — | Taip | — |
| `info_isanksciau` | `0` | — | — | Ne | — |
| `info_kt` | `1` | — | — | Taip | — |
| `info_kt` | `0` | — | — | Ne | — |
| `lanke_vilnius` | `1` | — | — | Taip | — |
| `lanke_vilnius` | `0` | — | — | Ne | — |
| `lanke_kaunas` | `1` | — | — | Taip | — |
| `lanke_kaunas` | `0` | — | — | Ne | — |
| `lanke_klaipeda` | `1` | — | — | Taip | — |
| `lanke_klaipeda` | `0` | — | — | Ne | — |
| `lanke_palanga` | `1` | — | — | Taip | — |
| `lanke_palanga` | `0` | — | — | Ne | — |
| `lanke_trakai` | `1` | — | — | Taip | — |
| `lanke_trakai` | `0` | — | — | Ne | — |
| `lanke_birstonas` | `1` | — | — | Taip | — |
| `lanke_birstonas` | `0` | — | — | Ne | — |
| `lanke_druskininkai` | `1` | — | — | Taip | — |
| `lanke_druskininkai` | `0` | — | — | Ne | — |
| `lanke_kursiunerija` | `1` | — | — | Taip | — |
| `lanke_kursiunerija` | `0` | — | — | Ne | — |
| `lanke_alytkaunmarijapskr` | `1` | — | — | Taip | — |
| `lanke_alytkaunmarijapskr` | `0` | — | — | Ne | — |
| `lanke_klaiptelsiutauragapskr` | `1` | — | — | Taip | — |
| `lanke_klaiptelsiutauragapskr` | `0` | — | — | Ne | — |
| `lanke_siauliupanevezapskr` | `1` | — | — | Taip | — |
| `lanke_siauliupanevezapskr` | `0` | — | — | Ne | — |
| `lanke_utenosvilniausapskr` | `1` | — | — | Taip | — |
| `lanke_utenosvilniausapskr` | `0` | — | — | Ne | — |
| `apgyv_tipas` | `"1"` | — | — | Viešbutis ar motelis | — |
| `apgyv_tipas` | `"2"` | — | — | Poilsio namai | — |
| `apgyv_tipas` | `"3"` | — | — | Vasaros poilsio nameliai | — |
| `apgyv_tipas` | `"4"` | — | — | Kempingas | — |
| `apgyv_tipas` | `"5"` | — | — | Turistinė bazė | — |
| `apgyv_tipas` | `"6"` | — | — | Nakvynės namai | — |
| `apgyv_tipas` | `"7"` | — | — | Nuoma privačiame sektoriuje | — |
| `apgyv_tipas` | `"8"` | — | — | Pas gimines ar draugus | — |
| `apgyv_tipas` | `"9"` | — | — | Sanatorija ar kita sveikatinimo įstaiga | — |
| `apgyv_tipas` | `"10"` | — | — | Kita | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `islaid_pries` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_paketui` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_vizai` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_ktpries` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_lt` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_apgyvend` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_maistui` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_restoranuose` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_parduotuvese` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_transportui` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_degalams` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_trnuomai` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_trremontui` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_viesajamtr` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_laisvalaikiui` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_pirkiniams` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_pirkmasinai` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_kt` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `islaid_viso` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/turizmas/atvyksta.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/turizmas/atvyksta.csv#L8)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/turizmas/atvyksta (https://data.gov.lt/datasets/2079/)
