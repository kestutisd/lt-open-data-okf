---
type: Table
title: "NtrPatalpa"
description: "Spinta table datasets/gov/rc/ntr/ntr_patalpos/NtrPatalpa (33 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_patalpos/NtrPatalpa"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_patalpos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_patalpos.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# NtrPatalpa

- **Model:** `datasets/gov/rc/ntr/ntr_patalpos/NtrPatalpa`[^manifest]
- **Dataset:** [Nekilnojamojo turto registre įregistruotų patalpų duomenys pagal savivaldybes](../ntr_patalpos.md) (`datasets/gov/rc/ntr/ntr_patalpos`)
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_patalpos.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_patalpos.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_patalpos/NtrPatalpa`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Identifikatorius | Patalpų / buto identifikatorius šiame duomenų rinkinyje |
| `pastato_id` | `integer` | — | `4` | `open` | — | Pastato identifikatorius | Pastato, kuriam priklauso patalpos, identifikatorius šiame duomenų rinkinyje |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybė | Savivaldybės, kurioje yra patalpos / butas, pavadinimas |
| `seniunija` | `ref` | [/datasets/gov/rc/ar/seniunija/Seniunija](../../ar/seniunija/Seniunija.md) | `4` | `open` | — | Seniūnija | Savivaldybėje esančios seniūnijos, kurioje yra patalpos / butas, pavadinimas |
| `obje_tipas` | `ref` | [/datasets/gov/rc/ntr/ntr_objektai/NtrObjektoTipas](../ntr_objektai/NtrObjektoTipas.md) | `4` | `open` | — | Objekto tipas | Objekto (patalpų / buto) tipas |
| `pask_tipas` | `ref` | [/datasets/gov/rc/ntr/ntr_paskirtys/NtrPaskirtiesTipas](../ntr_paskirtys/NtrPaskirtiesTipas.md) | `4` | `open` | — | Paskirties tipas | Objekto (patalpų / buto) paskirtis |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_patalpos.csv
