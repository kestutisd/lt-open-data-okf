---
type: Dataset
title: "Socialinio būsto duomenys"
description: "Rinkinyje pateikiami socialinio būsto Lietuvoje duomenys nuo 1990 metų."
resource: "https://get.data.gov.lt/datasets/gov/sadm/socialinis_bustas"
tags: [gov, sadm, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/soc_bustas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/sadm/soc_bustas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Socialinio būsto duomenys

Rinkinyje pateikiami socialinio būsto Lietuvoje duomenys nuo 1990 metų. Rinkinys susideda iš 5 lentelių: 1. Socialinio būsto fondas Lentelėje pateikiama informacija apie būstus Lietuvoje, kurie tam tikru laikotarpiu praeityje atliko ar iki šiol atlieka socialinio būsto funkciją. Lentelės objektas – vienas būstas. Nurodomos būsto charakteristikos (plotas, kambarių skaičius, būsena duomenų atnaujinimo metu, pirmo ir paskutinio apgyvendinimo datos) bei vietovės duomenys (gyvenvietė, savivaldybė, koordinatės pagal LKS ir WGS koordinačių sistemas). Duomenys jungiami su lentele „Socialinio ir savivaldybės būsto nuomos duomenys“ pagal lauką „busto_id“. 2. Socialinio ir savivaldybės būsto nuomos duomenys Lentelėje pateikiami socialinio ir savivaldybės būsto nuomos Lietuvos savivaldybėse istorijos duomenys nuo 20 a. pabaigos. Lentelės objektas – vieno socialinio arba savivaldybės būsto statusas (nuomojamas, laisvas, rezervuotas, parduotas ir kt.) tam tikru laikotarpiu. Lentelėje pateikiami būsto statuso duomenys (būsena, būsenos pradžia ir pabaiga, būsto charakteristikos, vietovė) ir nuomos informacija (sutarties dėl nuomos pasirašymo metai, būsto nuomos kainos savivaldybėje ataskaitiniais metais, 25 %, 50 % ir 75 % kvantiliai bei požymis, nurodantis, ar būste gyvena asmuo iš socialinio būsto eilės sąrašo; duomenų naudotojams primename, jog kvantilis nurodo reikšmę, už kurią x dalis duomenų yra mažesni arba lygūs). Duomenys jungiami su lentele „Socialinio būsto fondas“ pagal lauką „busto_id“. 3. Socialinio būsto gavėjų charakteristikos Lentelėje pateikiamos socialinį būstą gaunančių asmenų ar šeimų bendrosios charakteristikos nuo 2000 metų. Įrašas lentelėje nurodo vieną asmenį ar šeimą, tais metais pasirašiusius socialinio būsto nuomos sutartį. Nurodomos būsto gavėjo charakteristikos (požymiai, ar yra bedarbių, ar asmuo patenka į socialinės rizikos įskaitą, įtraukimo į įskaitą priežastis, namų ūkį sudarančių asmenų skaičius ir šeimos tipas) ir gyvenamosios vietos duomenys savivaldybės arba apskrities lygmeniu. 4. Socialinio būsto prašymų duomenys Lentelėje pateikiami prašymų gauti socialinį būstą arba būsto nuomos mokesčio dalies kompensaciją nuo 20 a. pabaigos duomenys: - prašymo dėl paramos būstui išsinuomoti BP-3 forma (dėl įrašymo į asmenų ir šeimų, turinčių teisę į socialinio būsto nuomą, sąrašą), - prašymo dėl paramos būstui išsinuomoti BP-5 forma (neįrašytiems į turinčių teisę sąrašus), - prašymo dėl paramos būstui išsinuomoti BP-4 forma (būsto nuomos mokesčio dalies kompensacijai gauti). Lentelės objektas – vienas prašymas. Pateikiami duomenys apie prašymą (pateikimo laikas, kaip nurodyta socialinio būsto įstatyme, prašymo būsena duomenų atnaujinimo metu, pagal įstatymą apibrėžta būsto grupė, į kurią pretenduoja prašymą pateikęs asmuo, bei prašymo pagerinti būstą priežastis) ir jį teikusį asmenį (gyvenamoji savivaldybė ir duomenys apie turimą būstą). Lentelė jungiasi su kita rinkinio lentele „Sprendimai suteikti socialinį būstą“ pagal lauką „prasymo_id“. 5. Sprendimai suteikti socialinį būstą Lentelėje nurodomi sprendimai skirti socialinį būstą asmenims, pateikusiems prašymą, ir duomenys apie sprendimą – data ir sprendimą priėmusi savivaldybė. Jeigu asmuo arba šeima, kaip numatyta socialinio būsto įstatyme, netenka teisės į socialinį būstą, tuomet nurodoma sprendimo priėmimo išbraukti asmenį iš sąrašo data, priežastis ir išbraukimo data. Taip pat pateikiamas asmens, įrašyto į būsto laukiančiųjų sąrašą, eilės numeris duomenų atnaujinimo metu, nurodomas jo eilės numeris tuo metu, kai jam buvo paskirtas socialinis būstas, ir fiksuojama įsikraustymo į pirmąjį socialinį būstą data. Lentelės naudotojai, sujungę duomenis su prašymų lentele pagal lauką „prasymo_id“, gali apskaičiuoti skirtumą tarp prašymo teikimo, sprendimo priėmimo ir pirmo įsikraustymo į suteiktą socialinį būstą datų. Nuoroda į socialinio būsto įstatymą: https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/620cd9e0584311e49df480952cc07606/asr. Duomenų teikėjas – Socialinės apsaugos ir darbo ministerija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^manifest]

- **Namespace:** `datasets/gov/sadm/socialinis_bustas`[^manifest]
- **Manifest CSV:** [datasets/gov/sadm/soc_bustas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/soc_bustas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sadm/socialinis_bustas` (`deployed`)[^manifest]
- **Provider:** `sadm` — Lietuvos Respublikos socialinės apsaugos ir darbo ministerija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `5` (5 lentelės)[^manifest]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Bustas](socialinis_bustas/Bustas.md) | Socialinio būsto fondas | `4` | `busto_id` | — | `14` | Lentelėje pateikiama informacija apie būstus Lietuvoje, kurie tam tikru laikotarpiu praeityje atliko ar iki šiol atlieka socialinio būsto funkciją. |
| [Gavejas](socialinis_bustas/Gavejas.md) | Socialinio būsto gavėjų charakteristikos | `4` | `statuso_id` | — | `10` | Lentelėje pateikiamos socialinį būstą gaunančių asmenų ar šeimų bendrosios charakteristikos nuo 2000 metų. |
| [Statusas](socialinis_bustas/Statusas.md) | Socialinio ir savivaldybės būsto nuomos duomenys | `4` | `ivykio_id` | — | `16` | Lentelėje pateikiami socialinio ir savivaldybės būsto nuomos Lietuvos savivaldybėse istorijos duomenys nuo 20 a. |
| [Prasymas](socialinis_bustas/Prasymas.md) | Socialinio būsto prašymų duomenys | `4` | `prasymo_id` | — | `10` | Lentelėje pateikiami prašymų gauti socialinį būstą arba būsto nuomos mokesčio dalies kompensaciją nuo 20 a. |
| [Sprendimas](socialinis_bustas/Sprendimas.md) | Sprendimai suteikti socialinį būstą | `4` | `sprendimo_id` | — | `11` | Lentelėje nurodomi sprendimai skirti socialinį būstą asmenims, pateikusiems prašymą, ir duomenys apie sprendimą – data ir sprendimą priėmusi savivaldybė. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/sadm/soc_bustas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/soc_bustas.csv#L2)
