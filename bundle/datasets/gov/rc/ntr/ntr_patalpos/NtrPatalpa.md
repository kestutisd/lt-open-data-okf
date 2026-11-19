---
type: Table
title: "NtrPatalpa"
description: "Spinta table datasets/gov/rc/ntr/ntr_patalpos/NtrPatalpa (33 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_patalpos/NtrPatalpa"
tags: [gov, rc, ntrpatalpa, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_patalpos.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_patalpos.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1813/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_patalpos"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# NtrPatalpa

- **Model:** `datasets/gov/rc/ntr/ntr_patalpos/NtrPatalpa`[^manifest]
- **Dataset:** [Nekilnojamojo turto registre įregistruotų patalpų duomenys pagal savivaldybes](../ntr_patalpos.md) (`datasets/gov/rc/ntr/ntr_patalpos`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_patalpos.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_patalpos.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_patalpos/NtrPatalpa` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Identifikatorius | Patalpų / buto identifikatorius šiame duomenų rinkinyje |
| `pastato_id` | `integer` | — | `4` | `open` | — | Pastato identifikatorius | Pastato, kuriam priklauso patalpos, identifikatorius šiame duomenų rinkinyje |
| `savivaldybe` | `ref` | [Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybė | Savivaldybės, kurioje yra patalpos / butas, pavadinimas |
| `seniunija` | `ref` | [Seniunija](../../ar/seniunija/Seniunija.md) (`level=4 UUID`: `seniunija._id`) | `4` | `open` | — | Seniūnija | Savivaldybėje esančios seniūnijos, kurioje yra patalpos / butas, pavadinimas |
| `obje_tipas` | `ref` | [NtrObjektoTipas](../ntr_objektai/NtrObjektoTipas.md) (`level=4 UUID`: `obje_tipas._id`) | `4` | `open` | — | Objekto tipas | Objekto (patalpų / buto) tipas |
| `pask_tipas` | `ref` | [NtrPaskirtiesTipas](../ntr_paskirtys/NtrPaskirtiesTipas.md) (`level=4 UUID`: `pask_tipas._id`) | `4` | `open` | — | Paskirties tipas | Objekto (patalpų / buto) paskirtis |
| `stat_pradzios_metai` | `integer` | — | `3` | `open` | — | Statybos pradžios metai | Objekto (patalpų / buto) statybos pradžios metai |
| `stat_pabaigos_metai` | `integer` | — | `3` | `open` | — | Statybos pabaigos metai | Objekto (patalpų / buto) statybos užbaigimo metai |
| `rekonstr_pradzios_metai` | `integer` | — | `3` | `open` | — | Rekonstrukcijos pradžios metai | Objekto (patalpų / buto) rekonstrukcijos pradžios metai |
| `rekonstr_pabaigos_metai` | `integer` | — | `3` | `open` | — | Rekonstrukcijos pabaigos metai | Objekto (patalpų / buto) rekonstrukcijos pabaigos metai |
| `kap_remonto_pradzios_metai` | `integer` | — | `3` | `open` | — | Kapitalinio remonto pradžios metai | Objekto (patalpų / buto) kapitalinio remonto pradžios metai |
| `kap_remonto_pabaigos_metai` | `integer` | — | `3` | `open` | — | Kapitalinio remonto pabaigos metai | Objekto (patalpų / buto) kapitalinio remonto pabaigos metai |
| `sildymas` | `integer` | — | `2` | `open` | — | Šildymas | Objekto (patalpų / buto) šildymo sistema |
| `vandentiekis` | `integer` | — | `2` | `open` | — | Vandentiekis | Objekto (patalpų / buto) vandentiekio sistema |
| `nuoteku_salinimas` | `integer` | — | `2` | `open` | — | Nuotakų šalinimas | Nuotakų šalinimo sistema objekte (patalpose / bute) |
| `dujos` | `integer` | — | `2` | `open` | — | Dujos | Objekto (patalpų / buto) aprūpinimas dujomis |
| `karstas_vanduo` | `integer` | — | `2` | `open` | — | Karštas vanduo | Objekto (patalpų / buto) aprūpinimas karštu vandeniu |
| `virykle` | `integer` | — | `2` | `open` | — | Viryklė | Viryklės objekte (patalpose / bute) buvimo požymis ir tipas |
| `vonios_kambarys` | `integer` | — | `2` | `open` | — | Vonios kambarys | Vonios kambario objekte (patalpose / bute) buvimo požymis |
| `kambariu_sk` | `integer` | `U` | `4` | `open` | — | Kambarių skaičius | Objekto (patalpų / buto) kambarių skaičius |
| `aukstas` | `integer` | — | `4` | `open` | — | Aukštas | Aukštas, kuriame yra objektas (patalpos / butas) |
| `baigtumo_proc` | `integer` | — | `3` | `open` | — | Baigtumo procentas | Objekto (patalpų / buto) statybos baigtumas procentais |
| `bendras_plotas` | `number` | — | `3` | `open` | — | Bendras plotas | Objekto (patalpų / buto) bendrasis plotas |
| `naudingas_plotas` | `number` | — | `3` | `open` | — | Naudingas plotas | Gyvenamosios paskirties patalpų naudingasis plotas - visų kambarių (gyvenamojo ploto), verslo patalpų (verslo ploto) ir apšiltintų pagalbinių patalpų (pagalbinio naudingojo ploto) plotų suma |
| `gyv_plotas` | `number` | — | `3` | `open` | — | Gyvenamasis plotas | Gyvenamosios paskirties patalpų, suformuotų kaip atskiri Kadastro objektai (buto gyvenamuosiuose ir negyvenamuosiuose pastatuose; vieno buto namo; atskiro kambario su bendrojo naudojimo patalpomis), plotas skaičiuojamas kaip gyventi skirtų uždarų ar pusiau uždarų patalpų plotų suma |
| `verslo_plotas` | `number` | — | `3` | `open` | — | Verslo plotas | Verslo plotas - gyvenamojoje patalpoje verslui skirtų patalpų, kuriose užsiimama kuria nors darbine ar kita veikla, aptarnaujami klientai, plotas |
| `pagalb_nenaud_plotas` | `number` | — | `3` | `open` | — | Pagalbinis nenaudingas plotas | Pagalbinis nenaudingas plotas - neapšiltintų pagalbinių patalpų (uždarų lodžijų, įstiklintų balkonų, uždarų verandų, oranžerijų, atriumų, žiemos sodų, priemenių, sandėlių, kitų neapšiltintų patalpų) plotai įskaičiuojami į gyvenamosios patalpos pagalbinį nenaudingąjį plotą |
| `pagalb_naud_plotas` | `number` | — | `3` | `open` | — | Pagalbinis naudingas plotas | Pagalbinis naudingas plotas - pagalbinio ploto dalis, esanti apšiltintomis atitvaromis apribotoje pastato erdvėje, įskaičiuojama į pagalbinį naudingąjį gyvenamosios patalpos plotą |
| `rusiu_plotas` | `number` | — | `3` | `open` | — | Rūsių plotas | Objekto (patalpų / buto) rūsių, pusrūsių ir kitų įgilintų patalpų plotas |
| `garazu_plotas` | `number` | — | `3` | `open` | — | Garažų plotas | Objekto (patalpų / buto) garažų patalpų plotas pastate |
| `pagrindinis_plotas` | `number` | — | `3` | `open` | — | Pagrindinis plotas | Objekto (patalpų / buto) pagrindinis plotas |
| `pagalbinis_plotas` | `number` | — | `3` | `open` | — | Pagalbinis plotas | Objekto (patalpų / buto) pagalbinis plotas |
| `pastato_energ_naud_klase` | `integer` | — | `3` | `open` | — | Pastato energetinio naudingumo klasė | Pagal teisės aktų reikalavimus objektui (patalpoms/butui) nustatyta energetinio naudingumo klasė |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_patalpos.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_patalpos.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_patalpos (https://data.gov.lt/datasets/1813/)
