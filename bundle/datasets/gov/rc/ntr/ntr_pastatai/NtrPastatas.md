---
type: Table
title: "NtrPastatas"
description: "Spinta table datasets/gov/rc/ntr/ntr_pastatai/NtrPastatas (43 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_pastatai/NtrPastatas"
tags: [gov, rc, ntrpastatas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_pastatai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_pastatai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1812/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_pastatai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# NtrPastatas

- **Model:** `datasets/gov/rc/ntr/ntr_pastatai/NtrPastatas`[^manifest]
- **Dataset:** [Nekilnojamojo turto registre įregistruotų pastatų duomenys pagal savivaldybes](../ntr_pastatai.md) (`datasets/gov/rc/ntr/ntr_pastatai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_pastatai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_pastatai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_pastatai/NtrPastatas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Objekto identifikatorius | Dirbtinis nekinojamojo turto objekto identifikatorius |
| `savivaldybe` | `ref` | [Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybė | Savivaldybės pavadinimas |
| `seniunija` | `ref` | [Seniunija](../../ar/seniunija/Seniunija.md) (`level=4 UUID`: `seniunija._id`) | `4` | `open` | — | Seniūnija | Savivaldybėje esančios seniūnijos pavadinimas |
| `statinio_kategorija` | `string` | — | `3` | `open` | — | Statinio kategorija | Statinio rūšis pagal LR statybos įstatymą. Nuo statinio kategorijos priklauso koks projektas turi būti parengtas, kokie reikalavimai keliami projekto vadovui ir kitiems statybos techninės veiklos pagrindinių sričių (STVPS) vadovams ir statybą leidžiančio dokumento (SLD) privalomumas. |
| `obje_tipas` | `ref` | [NtrObjektoTipas](../ntr_objektai/NtrObjektoTipas.md) (`level=4 UUID`: `obje_tipas._id`) | `4` | `open` | — | Objekto tipas | Pastato tipas |
| `pask_tipas` | `ref` | [NtrPaskirtiesTipas](../ntr_paskirtys/NtrPaskirtiesTipas.md) (`level=4 UUID`: `pask_tipas._id`) | `4` | `open` | — | Paskirties tipas | Pastato paskirtis |
| `atr_uzstatytas_plotas` | `number` | — | `3` | `open` | — | Atributas užstatytas plotas | Pastatu užstatytas žemės plotas |
| `bendras_plotas` | `number` | — | `3` | `open` | — | Bendras plotas | Pastato bendrasis plotas |
| `naudingas_plotas` | `number` | — | `3` | `open` | — | Naudingas plotas | Gyvenamosios paskirties patalpų naudingasis plotas - visų kambarių (gyvenamojo ploto), verslo patalpų (verslo ploto) ir apšiltintų pagalbinių patalpų (pagalbinio naudingojo ploto) plotų suma |
| `gyv_plotas` | `number` | — | `3` | `open` | — | Gyvenamasis plotas | Gyvenamosios paskirties patalpų, suformuotų kaip atskiri Kadastro objektai (buto gyvenamuosiuose ir negyvenamuosiuose pastatuose; vieno buto namo; atskiro kambario su bendrojo naudojimo patalpomis), plotas skaičiuojamas kaip gyventi skirtų uždarų ar pusiau uždarų patalpų plotų suma |
| `verslo_plotas` | `number` | — | `3` | `open` | — | Verslo plotas | Verslo plotas - gyvenamojoje patalpoje verslui skirtų patalpų, kuriose užsiimama kuria nors darbine ar kita veikla, aptarnaujami klientai, plotas |
| `pagalb_nenaud_plotas` | `number` | — | `3` | `open` | — | Pagalbinis nenaudingas plotas | Pagalbinis nenaudingas plotas - neapšiltintų pagalbinių patalpų (uždarų lodžijų, įstiklintų balkonų, uždarų verandų, oranžerėjų, atriumų, žiemos sodų, priemenių, sandėlių, kitų neapšiltintų patalpų) plotai įskaičiuojami į gyvenamosios patalpos pagalbinį nenaudingąjį plotą |
| `pagalb_naud_plotas` | `number` | — | `3` | `open` | — | Pagalbinis naudingas plotas | Pagalbinis naudingas plotas - pagalbinio ploto dalis, esanti apšiltintomis atitvaromis apribotoje pastato erdvėje, įskaičiuojama į pagalbinį naudingąjį gyvenamosios patalpos plotą |
| `rusiu_plotas` | `number` | — | `3` | `open` | — | Rūsių plotas | Pastato rūsių, pusrūsių ir kitų įgilintų patalpų plotas |
| `garazu_plotas` | `number` | — | `3` | `open` | — | Garažų plotas | Garažų patalpų plotas pastate |
| `patalpu_kaip_atsir_nt_skaicius` | `integer` | `U` | `4` | `open` | — | Patalpų, kaip atskiro nekilnojamojo turto skaičius | Patalpų, suformuotų kaip atskiri nekilnojamojo turto objektai, skaičius |
| `gyv_pask_patalpu_sk` | `integer` | `U` | `4` | `open` | — | Gyvenamosios paskirties patalpų skaičius | Gyvenamosios paskirties patalpų pastate skaičius |
| `pastato_energ_naud_klase` | `integer` | — | `2` | `open` | — | Pastato energetinio naudingumo klasė | Pagal teisės aktų reikalavimus pastatui nustatyta Pastato energetinio naudingumo klasė |
| `aukstu_skaicius` | `integer` | `U` | `4` | `open` | — | Aukštų skaičius | Pastato aukštų skaičius - pagal antžeminių aukštų kiekį, neskaitant požeminių aukštų, pastogės patalpų, antstatų. Jeigu prie esamo pastato pristatytame priestate yra didesnis antžeminių aukštų skaičius (neskaitant rūsių, pusrūsių (cokolinių aukštų), pastogės patalpų ir antstatų) negu pagrindiniame pastate, viso pastato aukštų skaičius nustatomas pagal priestato aukštų skaičių |
| `stat_pradzios_metai` | `integer` | — | `3` | `open` | — | Statybos pradžios metai | Pastato statybos užbaigimo metai |
| `stat_pabaigos_metai` | `integer` | — | `3` | `open` | — | Statybos pabaigos metai | Pastato statybos užbaigimo metai |
| `modern_pradzios_metai` | `integer` | — | `3` | `open` | — | Modernizavimo pradžios metai | Pastato renovacijos pradžios metai |
| `modern_pabaigos_metai` | `integer` | — | `3` | `open` | — | Modernizavimo pabaigos metai | Pastato renovacijos pabaigos metai |
| `sildymas` | `integer` | — | `2` | `open` | — | Šildymas | Pastato šildymo sistema |
| `vandentiekis` | `integer` | — | `2` | `open` | — | Vandentiekis | Pastato vandentiekio sistema |
| `nuoteku_salinimas` | `integer` | — | `2` | `open` | — | Nuotakų šalinimas | Nuotakų šalinimo sistema pastate |
| `dujos` | `integer` | — | `2` | `open` | — | Dujos | Pastato aprūpinimas dujomis |
| `karstas_vanduo` | `integer` | — | `2` | `open` | — | Karštas vanduo | Pastato aprūpinimas karštu vandeniu |
| `elektra` | `integer` | — | `2` | `open` | — | Elektra | Elektros instaliacija pastate |
| `virykle` | `integer` | — | `2` | `open` | — | Viryklė | Viryklių skaičius pastate |
| `vonios_kambarys` | `integer` | — | `2` | `open` | — | Vonios kambarys | Vonios kambarių skaičius pastate |
| `vedin_kondicionav` | `integer` | — | `2` | `open` | — | Vėdinimas-kondicionavimas | Pastato vėdinimo kondicionavimo sistema |
| `pamatai` | `integer` | — | `2` | `open` | — | Pamatai | Pamatų rūšis ir medžiaga |
| `sienos` | `integer` | — | `2` | `open` | — | Sienos | Sienų medžiaga |
| `stogo_konstrukcija` | `integer` | — | `2` | `open` | — | Stogo konstrukcija | Stogo konstrukcija |
| `stogo_danga` | `integer` | — | `2` | `open` | — | Stogo danga | Stogo dangos medžiaga |
| `perdanga` | `integer` | — | `2` | `open` | — | Perdanga | Perdangos medžiaga |
| `isores_apdaila` | `integer` | — | `2` | `open` | — | Išorės apdaila | Išorės apdailos medžiaga |
| `vidaus_apdaila` | `integer` | — | `2` | `open` | — | Vidaus apdaila | Vidaus apdailos medžiaga |
| `pertvaros` | `integer` | — | `2` | `open` | — | Pertvaros | Pertvarų medžiaga |
| `grindys` | `integer` | — | `2` | `open` | — | Grindys | Grindų medžiaga |
| `langai` | `integer` | — | `2` | `open` | — | Langai | Langų medžiaga |
| `durys` | `integer` | — | `2` | `open` | — | Durys | Durų medžiaga |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_pastatai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_pastatai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_pastatai (https://data.gov.lt/datasets/1812/)
