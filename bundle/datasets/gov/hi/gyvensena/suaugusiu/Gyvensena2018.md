---
type: Table
title: "Gyvensena2018 — Suaugusiųjų gyvensenos tyrimo 2018 metų duomenys"
description: "Klausimynas skelbiamas internete: https://www.hi.lt/uploads/Visuomenes_sveikatos_technologiju_centras/Suaugusiu_gyvensenos_klausimynas_20180313_1.pdf"
resource: "https://get.data.gov.lt/datasets/gov/hi/gyvensena/suaugusiu/Gyvensena2018"
tags: [gov, hi, gyvensena2018, deployed, cadence-quadrennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/gyvensena/suaugusiu.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/hi/gyvensena/suaugusiu.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1226/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/gyvensena/suaugusiu"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Gyvensena2018 — Suaugusiųjų gyvensenos tyrimo 2018 metų duomenys

Klausimynas skelbiamas internete: https://www.hi.lt/uploads/Visuomenes_sveikatos_technologiju_centras/Suaugusiu_gyvensenos_klausimynas_20180313_1.pdf[^manifest]

- **Model:** `datasets/gov/hi/gyvensena/suaugusiu/Gyvensena2018`[^manifest]
- **Dataset:** [Suaugusiųjų gyvensenos duomenys](../suaugusiu.md) (`datasets/gov/hi/gyvensena/suaugusiu`)[^manifest]
- **Manifest CSV:** [datasets/gov/hi/gyvensena/suaugusiu.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/gyvensena/suaugusiu.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/gyvensena/suaugusiu/Gyvensena2018` (`deployed`)[^manifest]
- **Provider:** `hi` — Suaugusiųjų ir vaikų gyvensenos duomenys *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUADRENNIAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `resp_kodas` | `string` | — | `4` | `open` | — | Respondento kodas | — |
| `darzoves` | `string` | — | `4` | `open` | — | Kaip dažnai valgote daržovių? | — |
| `vaisiai` | `string` | — | `4` | `open` | — | Kaip dažnai valgote vaisių? | — |
| `druska` | `string` | — | `4` | `open` | — | Ar Jūs dedate druskos į paruoštą maistą? | — |
| `men_tabakas` | `string` | — | `4` | `open` | — | Ar vartojote tabako gaminius per paskutines 30 dienų? | — |
| `metai_tabakas` | `string` | — | `4` | `open` | — | Ar vartojote tabako gaminius per paskutinius 12 mėnesių? | — |
| `men_elektronines_cigaretes` | `string` | — | `4` | `open` | — | Ar rūkėte elektronines cigaretes per paskutines 30 dienų? | — |
| `metai_elektronines_cigaretes` | `string` | — | `4` | `open` | — | Ar rūkėte elektronines cigaretes per paskutinius 12 mėnesių? | — |
| `men_alkoholis` | `string` | — | `4` | `open` | — | Ar vartojote alkoholinių gėrimų per paskutines 30 dienų? | — |
| `metai_alkoholis` | `string` | — | `4` | `open` | — | Ar vartojote alkoholinių gėrimų per paskutinius 12 mėnesių? | — |
| `men_apsvaigimas` | `string` | — | `4` | `open` | — | Ar buvo atvejų, kai buvote stipriai apsvaigęs nuo alkoholinio gėrimo per paskutines 30 dienų? | — |
| `metai_apsvaigimas` | `string` | — | `4` | `open` | — | Ar buvo atvejų, kai buvote stipriai apsvaigęs nuo alkoholinio gėrimo per paskutinius 12 mėnesių? | — |
| `gyvenimas_apsvaigimas` | `string` | — | `4` | `open` | — | Ar buvo atvejų, kai buvote stipriai apsvaigęs nuo alkoholinio gėrimo per savo gyvenimą? | — |
| `men_narkotikai` | `string` | — | `4` | `open` | — | Ar bent kartą vartojote narkotinių ar psichtropinių medžiagų (narkotikų) be gydytojo paskyrimo per paskutines 30 dienų? | — |
| `metai_narkotikai` | `string` | — | `4` | `open` | — | Ar bent kartą vartojote narkotinių ar psichtropinių medžiagų (narkotikų) be gydytojo paskyrimo per paskutinius 12 mėnesių? | — |
| `gyvenimas_narkotikai` | `string` | — | `4` | `open` | — | Ar bent kartą vartojote narkotinių ar psichtropinių medžiagų (narkotikų) be gydytojo paskyrimo per savo gyvenimą? | — |
| `loterijos` | `string` | — | `4` | `open` | — | Ar per pastaruosius 2 metus esate lošęs (-usi) azartinius lošimus / dalyvavęs (-usi) loterijose? Loterijose | — |
| `kazino` | `string` | — | `4` | `open` | — | Ar per pastaruosius 2 metus esate lošęs (-usi) azartinius lošimus / dalyvavęs (-usi) loterijose? Lošimo namuose (kazino) | — |
| `lazybu_punktas` | `string` | — | `4` | `open` | — | Ar per pastaruosius 2 metus esate lošęs (-usi) azartinius lošimus / dalyvavęs (-usi) loterijose? Lošimo automatų salone | — |
| `losimo_automatai` | `string` | — | `4` | `open` | — | Ar per pastaruosius 2 metus esate lošęs (-usi) azartinius lošimus / dalyvavęs (-usi) loterijose? Lošimo automatų salone | — |
| `losimai_internetu` | `string` | — | `4` | `open` | — | Ar per pastaruosius 2 metus esate lošęs (-usi) azartinius lošimus / dalyvavęs (-usi) loterijose? Internetu | — |
| `losimai_kitur` | `string` | — | `4` | `open` | — | Ar per pastaruosius 2 metus esate lošęs (-usi) azartinius lošimus / dalyvavęs (-usi) loterijose? Kitur | — |
| `daznumas_azartiniai_losimai` | `string` | — | `4` | `open` | — | Kaip dažnai Jūs lošiate azartinius lošimus? | — |
| `daznumas_loterijos` | `string` | — | `4` | `open` | — | Kaip dažnai Jūs dalyvaujate loterijose? | — |
| `fizine_veikla` | `string` | — | `4` | `open` | — | Kiek kartų per savaitę užsiimate mažiausiai 30 min. užsiimate energinga fizine veikla taip, kad pagreitėtų kvėpavimas ir pulsas? | — |
| `bendravimas_seimos_nariai` | `string` | — | `4` | `open` | — | Kaip dažnai Jūs per paskutinius 12 mėn bendravote su šeimos nariais? | — |
| `bendravimas_giminaiciai` | `string` | — | `4` | `open` | — | Kaip dažnai Jūs per paskutinius 12 mėn bendravote su giminaičiais (ne šeimos nariais)? | — |
| `bendravimas_draugai` | `string` | — | `4` | `open` | — | Kaip dažnai Jūs per paskutinius 12 mėn bendravote su draugais? | — |
| `nerimas` | `string` | — | `4` | `open` | — | Ar per praėjusį mėnesį Jus buvo apėmusi prislėgta nuotaika, nerimas? | — |
| `gyvenimo_kokybe` | `string` | — | `4` | `open` | — | Kaip vertinate savo gyvenimo kokybę? | — |
| `sveikata` | `string` | — | `4` | `open` | — | Kaip vertinate dabartinę savo sveikatos būklę? | — |
| `laimingumas` | `string` | — | `4` | `open` | — | Ar jaučiatės laimingas? | — |
| `gyvensenos_pakeitimas` | `string` | — | `4` | `open` | — | Ar per paskutinius 12 mėnesių esate pakeitęs savo gyvenseną dėl sveikatos? | — |
| `sveikiau_maintintis` | `string` | — | `4` | `open` | — | Jei į 16 klausimą atsakėte taip, ar Jūs pradėjote sveikiau gyventi? Pradėjau sveikiau maitintis | — |
| `tapti_fiziskai_aktyvesniu` | `string` | — | `4` | `open` | — | Jei į 16 klausimą atsakėte taip, ar Jūs pradėjote sveikiau gyventi? Tapau fiziškai aktyvesnis | — |
| `maziau_rukyti` | `string` | — | `4` | `open` | — | Jei į 16 klausimą atsakėte taip, ar Jūs pradėjote sveikiau gyventi? Mažiau rūkau arba mečiau rukyti | — |
| `maziau_vartoti_alkoholiu` | `string` | — | `4` | `open` | — | Jei į 16 klausimą atsakėte taip, ar Jūs pradėjote sveikiau gyventi? Mažiau vartoju alkoholio arba mečiau gerti | — |
| `zino_profilaktines_programas` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Informacijos gyventojams teikimas (straipsniai, lankstinukai ir pan.) apie profilaktines programas (pvz., širdies ir kraujagyslių ligų, gimdos kaklelio, krūties, prostatos ir storosios žarnos vėžio prevencijos). Žinau | — |
| `zino_sveikatos_stiprinimas` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Informacijos gyventojams teikimas (straipsniai, lankstinukai ir pan.) apie sveikatą ir jos stiprinimą. Žinau | — |
| `zino_zalingi_aplinkos_veiksniai` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Informacijos gyventojams teikimas (straipsniai, lankstinukai ir pan.) apie sveikatai žalingus aplinkos veiksnius. Žinau | — |
| `zino_uzkreciamosios_ligos` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Informacijos gyventojams teikimas (straipsniai, lankstinukai ir pan.) apie užkrečiamas ligas ir jų profilaktiką. Žinau | — |
| `zino_individualios_konsultacijos` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Individualios konsultacijos sveikatos stiprinimo ir išsaugojimo klausimais. Žinau | — |
| `zino_mokymai` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Mokymai, paskaitos sveikatos stiprinimo ir išsaugojimo klausimais. Žinau | — |
| `zino_sveikatos_skatinimas` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Sveiką gyvenseną skatinantys renginiai (pvz., sporto renginiai, viktorinos, konkursai ir pan.). Žinau | — |
| `zino_kita` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Kita. Žinau | — |
| `dalyvauja_profilaktines_programas` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Informacijos gyventojams teikimas (straipsniai, lankstinukai ir pan.) apie profilaktines programas (pvz., širdies ir kraujagyslių ligų, gimdos kaklelio, krūties, prostatos ir storosios žarnos vėžio prevencijos). Naudojausi / dalyvavau | — |
| `dalyvauja_sveikatos_stiprinimas` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Informacijos gyventojams teikimas (straipsniai, lankstinukai ir pan.) apie sveikatą ir jos stiprinimą. Naudojausi / dalyvavau | — |
| `naudoja_info_zalingi_aplinkos_veiksniai` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Informacijos gyventojams teikimas (straipsniai, lankstinukai ir pan.) apie sveikatai žalingus aplinkos veiksnius. Naudojausi / dalyvavau | — |
| `naudoja_info_uzkreciamosios_ligos` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Informacijos gyventojams teikimas (straipsniai, lankstinukai ir pan.) apie užkrečiamas ligas ir jų profilaktiką. Naudojausi / dalyvavau | — |
| `dalyvauja_individualios_konsultacijos` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Individualios konsultacijos sveikatos stiprinimo ir išsaugojimo klausimais. Naudojausi / dalyvavau | — |
| `dalyvauja_mokymai` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Mokymai, paskaitos sveikatos stiprinimo ir išsaugojimo klausimais. Naudojausi / dalyvavau | — |
| `dalyvauja_sveikatos_skatinimas` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Sveiką gyvenseną skatinantys renginiai (pvz., sporto renginiai, viktorinos, konkursai ir pan.). Naudojausi / dalyvavau | — |
| `naudoja_kita` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Kita. Naudojausi / dalyvavau | — |
| `patenkinti_profilaktines_programas` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Informacijos gyventojams teikimas (straipsniai, lankstinukai ir pan.) apie profilaktines programas (pvz., širdies ir kraujagyslių ligų, gimdos kaklelio, krūties, prostatos ir storosios žarnos vėžio prevencijos). Esu patenkintas (pildoma, jei paslauga naudojotės) | — |
| `patenkinti_sveikatos_stiprinimas` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Informacijos gyventojams teikimas (straipsniai, lankstinukai ir pan.) apie sveikatą ir jos stiprinimą. Esu patenkintas (pildoma, jei paslauga naudojotės) | — |
| `patenkinti_info_zalingi_aplinkos_veiksniai` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Informacijos gyventojams teikimas (straipsniai, lankstinukai ir pan.) apie sveikatai žalingus aplinkos veiksnius. Esu patenkintas (pildoma, jei paslauga naudojotės) | — |
| `patenkinti_info_uzkreciamosios_ligos` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Informacijos gyventojams teikimas (straipsniai, lankstinukai ir pan.) apie užkrečiamas ligas ir jų profilaktiką. Esu patenkintas (pildoma, jei paslauga naudojotės) | — |
| `patenkinti_individualios_konsultacijos` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Individualios konsultacijos sveikatos stiprinimo ir išsaugojimo klausimais. Esu patenkintas (pildoma, jei paslauga naudojotės) | — |
| `patenkinti_mokymai` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Mokymai, paskaitos sveikatos stiprinimo ir išsaugojimo klausimais. Esu patenkintas (pildoma, jei paslauga naudojotės) | — |
| `patenkinti_sveikatos_skatinimas` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Sveiką gyvenseną skatinantys renginiai (pvz., sporto renginiai, viktorinos, konkursai ir pan.). Esu patenkintas (pildoma, jei paslauga naudojotės) | — |
| `patenkinti_kita` | `string` | — | `4` | `open` | — | Kokias žinote savivaldybės teritorijoje teikiamas visuomenės sveikatos priežiūros paslaugas (veiklas), kokiomis pasinaudojote per paskutinius 12 mėn ir kaip jas vertinate? Kita. Esu patenkintas (pildoma, jei paslauga naudojotės) | — |
| `info_vs_prieziuros_paslaugos` | `string` | — | `4` | `open` | — | Iš kur Jūs dažniausiai sužinote apie Jūsų savivaldybėje visuomenės sveikatos priežiūros įstaigų teikiamas visuomenės sveikatos priežiūros paslaugas? Galimi keli atsakymo variantai | — |
| `patirtis` | `string` | — | `4` | `open` | — | Apibendrindami savo naudojimo visuomenės sveikatos priežiūros paslaugomis patirtį, įvertinkite visuomenės sveikatos priežiūros įstaigų Jums suteiktas paslaugas | — |
| `triuksmas` | `string` | — | `4` | `open` | — | Ar esate informuotas (-a) apie šiuos aplinkos rizikos veiksnius ir jų galimą neigiamą poveikį sveikatai? Triukšmą | — |
| `aplinkos_uzterstumas` | `string` | — | `4` | `open` | — | Ar esate informuotas (-a) apie šiuos aplinkos rizikos veiksnius ir jų galimą neigiamą poveikį sveikatai? Aplinkos užterštumą (pvz., oro, vandens) | — |
| `ultravioletine_spinduliuote` | `string` | — | `4` | `open` | — | Ar esate informuotas (-a) apie šiuos aplinkos rizikos veiksnius ir jų galimą neigiamą poveikį sveikatai? Ultravioletinę spinduliuotę (pvz. saulės, soliarumų) | — |
| `chemine_medziaga` | `string` | — | `4` | `open` | — | Ar esate informuotas (-a) apie šiuos aplinkos rizikos veiksnius ir jų galimą neigiamą poveikį sveikatai? Chemines medžiagas (pvz., buityje, darbe) | — |
| `info_aplinkos_rizikos_veiksniai` | `string` | — | `4` | `open` | — | Iš kur gaunate informacijos apie aplinkos rizikos veiksnius? Galimi keli atsakymo variantai. | — |
| `info_ligos_gydymas` | `string` | — | `4` | `open` | — | Ar Jums lengva rasti informacijos apie Jus dominančios ligos gydymą? | — |
| `info_profesionali_pagalba` | `string` | — | `4` | `open` | — | Ar Jums lengva rasti informacijos, kur gauti profesionalią pagalbą susirgus? | — |
| `suprasti_gydytojas` | `string` | — | `4` | `open` | — | Ar Jums lengva suprasti, ką sako Jūsų gydytojas? | — |
| `suprasti_vartoti_vaistus` | `string` | — | `4` | `open` | — | Ar Jums lengva suprasti gydytojo ar vaistininko nurodymus, kaip vartoti paskirtus vaistus? | — |
| `ivertinti_kitas_gydytojas` | `string` | — | `4` | `open` | — | Ar Jums lengva įvertinti, kada Jums reikalinga kito gydytojo muomonė? | — |
| `pasinaudoti_gydytojo_info` | `string` | — | `4` | `open` | — | Ar Jums lengva pasinaudoti gydytojo suteikta informacija priimant sprendimus, susijusius su Jūsų liga? | — |
| `laikytis_nurodymu` | `string` | — | `4` | `open` | — | Ar Jums lengva laikytis Jūsų gydytojo ar vaistininko nurodymų? | — |
| `rasti_info_psichikos_sveikata` | `string` | — | `4` | `open` | — | Ar Jums lengva rasti informacijos kaip valdyti psichikos sveikatos problemas, tokias kaip stresas ar depresija? | — |
| `suprasti_ispejimus_zalinga_sveikatai` | `string` | — | `4` | `open` | — | Ar Jums lengvasuprasti įspėjimus apie rūkymo, mažo fizinio aktyvumo, alkoholio vartojimo žalą sveikatai? | — |
| `suprasti_profilaktyniai_tyrimai` | `string` | — | `4` | `open` | — | Ar Jums lengva suprasti, kodėl reikia atlikti profilaktinius sveikatos tyrimus? | — |
| `ivertinti_info_patikimumas` | `string` | — | `4` | `open` | — | Ar Jums lengva įvertinti ar žiniasklaidoje pateikiama informacija apie pavojų sveikatai yra patikima? | — |
| `nuspresti_apsauga` | `string` | — | `4` | `open` | — | Ar Jums lengva nuspręsti, kaip apsisaugoti nuo ligų, reminatis žiniasklaidoje pateikiama informacija? | — |
| `rasti_veiksniai_psichikos_sveikata` | `string` | — | `4` | `open` | — | Ar Jums lengva rasti informacijos apie veiksmus, kurie sustiprintų psichikos sveikatą? | — |
| `suprasti_seimos_patarimus` | `string` | — | `4` | `open` | — | Ar Jums lengva rasti informacijos apie veiksmus, kurie sustiprintų psichikos sveikatą? | — |
| `suprasti_ziniasklaidos_info` | `string` | — | `4` | `open` | — | Ar Jums lengva suprasti žiniasklaidoje pateikiamą informaciją apie tai, kaip tapti sveikesniu? | — |
| `ivertinti_iprociu_itaka` | `string` | — | `4` | `open` | — | Ar Jums lengva suprasti žiniasklaidoje pateikiamą informaciją apie tai, kaip tapti sveikesniu? | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `darzoves` | `'1'` | — | — | vieną ar daugiau kartų per dieną | — |
| `darzoves` | `'2'` | — | — | 4–6 kartus per savaitę | — |
| `darzoves` | `'3'` | — | — | 1–3 kartus per savaitę | — |
| `darzoves` | `'4'` | — | — | mažiau nei kartą per savaitę | — |
| `darzoves` | `'5'` | — | — | niekada | — |
| `darzoves` | `'9'` | — | — | neatsakyta į klausimą | — |
| `vaisiai` | `'1'` | — | — | vieną ar daugiau kartų per dieną | — |
| `vaisiai` | `'2'` | — | — | 4–6 kartus per savaitę | — |
| `vaisiai` | `'3'` | — | — | 1–3 kartus per savaitę | — |
| `vaisiai` | `'4'` | — | — | mažiau nei kartą per savaitę | — |
| `vaisiai` | `'5'` | — | — | niekada | — |
| `vaisiai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `druska` | `'1'` | — | — | nededu | — |
| `druska` | `'2'` | — | — | taip, kai mano nuomone trūksta druskos | — |
| `druska` | `'3'` | — | — | taip, beveik visada net neragavęs/-usi | — |
| `druska` | `'9'` | — | — | neatsakyta į klausimą | — |
| `men_tabakas` | `'1'` | — | — | ne | — |
| `men_tabakas` | `'2'` | — | — | taip, kasdien | — |
| `men_tabakas` | `'3'` | — | — | taip, retkarciais | — |
| `men_tabakas` | `'4'` | — | — | taip, bent karta | — |
| `men_tabakas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `metai_tabakas` | `'1'` | — | — | ne | — |
| `metai_tabakas` | `'2'` | — | — | taip, kasdien | — |
| `metai_tabakas` | `'3'` | — | — | taip, retkarciais | — |
| `metai_tabakas` | `'4'` | — | — | taip, bent karta | — |
| `metai_tabakas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `men_elektronines_cigaretes` | `'1'` | — | — | ne | — |
| `men_elektronines_cigaretes` | `'2'` | — | — | taip, kasdien | — |
| `men_elektronines_cigaretes` | `'3'` | — | — | taip, retkarciais | — |
| `men_elektronines_cigaretes` | `'4'` | — | — | taip, bent karta | — |
| `men_elektronines_cigaretes` | `'9'` | — | — | neatsakyta į klausimą | — |
| `metai_elektronines_cigaretes` | `'1'` | — | — | ne | — |
| `metai_elektronines_cigaretes` | `'2'` | — | — | taip, kasdien | — |
| `metai_elektronines_cigaretes` | `'3'` | — | — | taip, retkarciais | — |
| `metai_elektronines_cigaretes` | `'4'` | — | — | taip, bent karta | — |
| `metai_elektronines_cigaretes` | `'9'` | — | — | neatsakyta į klausimą | — |
| `men_alkoholis` | `'1'` | — | — | ne | — |
| `men_alkoholis` | `'2'` | — | — | taip, kasdien | — |
| `men_alkoholis` | `'3'` | — | — | taip, 2–3 kartus per savaitę | — |
| `men_alkoholis` | `'4'` | — | — | taip, kartą per savaitę | — |
| `men_alkoholis` | `'5'` | — | — | taip, 2–3 kartus per mėnesį | — |
| `men_alkoholis` | `'6'` | — | — | taip, kelis kartus per metus | — |
| `men_alkoholis` | `'9'` | — | — | neatsakyta į klausimą | — |
| `metai_alkoholis` | `'1'` | — | — | ne | — |
| `metai_alkoholis` | `'2'` | — | — | taip, kasdien | — |
| `metai_alkoholis` | `'3'` | — | — | taip, 2–3 kartus per savaitę | — |
| `metai_alkoholis` | `'4'` | — | — | taip, kartą per savaitę | — |
| `metai_alkoholis` | `'5'` | — | — | taip, 2–3 kartus per mėnesį | — |
| `metai_alkoholis` | `'6'` | — | — | taip, kelis kartus per metus | — |
| `metai_alkoholis` | `'9'` | — | — | neatsakyta į klausimą | — |
| `men_apsvaigimas` | `'1'` | — | — | taip | — |
| `men_apsvaigimas` | `'2'` | — | — | ne | — |
| `men_apsvaigimas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `metai_apsvaigimas` | `'1'` | — | — | taip | — |
| `metai_apsvaigimas` | `'2'` | — | — | ne | — |
| `metai_apsvaigimas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `gyvenimas_apsvaigimas` | `'1'` | — | — | taip | — |
| `gyvenimas_apsvaigimas` | `'2'` | — | — | ne | — |
| `gyvenimas_apsvaigimas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `men_narkotikai` | `'1'` | — | — | taip | — |
| `men_narkotikai` | `'2'` | — | — | ne | — |
| `men_narkotikai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `metai_narkotikai` | `'1'` | — | — | taip | — |
| `metai_narkotikai` | `'2'` | — | — | ne | — |
| `metai_narkotikai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `gyvenimas_narkotikai` | `'1'` | — | — | taip | — |
| `gyvenimas_narkotikai` | `'2'` | — | — | ne | — |
| `gyvenimas_narkotikai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `loterijos` | `'1'` | — | — | taip | — |
| `loterijos` | `'2'` | — | — | ne | — |
| `loterijos` | `'9'` | — | — | neatsakyta į klausimą | — |
| `kazino` | `'1'` | — | — | taip | — |
| `kazino` | `'2'` | — | — | ne | — |
| `kazino` | `'9'` | — | — | neatsakyta į klausimą | — |
| `lazybu_punktas` | `'1'` | — | — | taip | — |
| `lazybu_punktas` | `'2'` | — | — | ne | — |
| `lazybu_punktas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `losimo_automatai` | `'1'` | — | — | taip | — |
| `losimo_automatai` | `'2'` | — | — | ne | — |
| `losimo_automatai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `losimai_internetu` | `'1'` | — | — | taip | — |
| `losimai_internetu` | `'2'` | — | — | ne | — |
| `losimai_internetu` | `'9'` | — | — | neatsakyta į klausimą | — |
| `losimai_kitur` | `'1'` | — | — | taip | — |
| `losimai_kitur` | `'2'` | — | — | ne | — |
| `losimai_kitur` | `'9'` | — | — | neatsakyta į klausimą | — |
| `daznumas_azartiniai_losimai` | `'1'` | — | — | kasdien arba beveik kasdien | — |
| `daznumas_azartiniai_losimai` | `'2'` | — | — | kelis kartus per savaitę | — |
| `daznumas_azartiniai_losimai` | `'3'` | — | — | kartą per savaitą | — |
| `daznumas_azartiniai_losimai` | `'4'` | — | — | kartą per mėnesį | — |
| `daznumas_azartiniai_losimai` | `'5'` | — | — | kartą per 6 mėnesius | — |
| `daznumas_azartiniai_losimai` | `'6'` | — | — | kartą per metus | — |
| `daznumas_azartiniai_losimai` | `'7'` | — | — | rečiau nei kartą per metus | — |
| `daznumas_azartiniai_losimai` | `'8'` | — | — | niekada | — |
| `daznumas_azartiniai_losimai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `daznumas_loterijos` | `'1'` | — | — | kasdien arba beveik kasdien | — |
| `daznumas_loterijos` | `'2'` | — | — | kelis kartus per savaitę | — |
| `daznumas_loterijos` | `'3'` | — | — | kartą per savaitą | — |
| `daznumas_loterijos` | `'4'` | — | — | kartą per mėnesį | — |
| `daznumas_loterijos` | `'5'` | — | — | kartą per 6 mėnesius | — |
| `daznumas_loterijos` | `'6'` | — | — | kartą per metus | — |
| `daznumas_loterijos` | `'7'` | — | — | rečiau nei kartą per metus | — |
| `daznumas_loterijos` | `'8'` | — | — | niekada | — |
| `daznumas_loterijos` | `'9'` | — | — | neatsakyta į klausimą | — |
| `fizine_veikla` | `'1'` | — | — | neužsiimu tokia fizine veikla | — |
| `fizine_veikla` | `'2'` | — | — | 1 diena | — |
| `fizine_veikla` | `'3'` | — | — | 2 dienas | — |
| `fizine_veikla` | `'4'` | — | — | 3 dienas | — |
| `fizine_veikla` | `'5'` | — | — | 4 dienas | — |
| `fizine_veikla` | `'6'` | — | — | 5 dienas | — |
| `fizine_veikla` | `'7'` | — | — | 6 dienas | — |
| `fizine_veikla` | `'8'` | — | — | 7 dienas | — |
| `fizine_veikla` | `'9'` | — | — | neatsakyta į klausimą | — |
| `bendravimas_seimos_nariai` | `'1'` | — | — | kasdien | — |
| `bendravimas_seimos_nariai` | `'2'` | — | — | kiekvieną savaitę (ne kasdien) | — |
| `bendravimas_seimos_nariai` | `'3'` | — | — | kelis kartus per mėnesį | — |
| `bendravimas_seimos_nariai` | `'4'` | — | — | kartą per mėnesį | — |
| `bendravimas_seimos_nariai` | `'5'` | — | — | bent kartą per 12 mėnesių | — |
| `bendravimas_seimos_nariai` | `'6'` | — | — | niekada | — |
| `bendravimas_seimos_nariai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `bendravimas_giminaiciai` | `'1'` | — | — | kasdien | — |
| `bendravimas_giminaiciai` | `'2'` | — | — | kiekvieną savaitę (ne kasdien) | — |
| `bendravimas_giminaiciai` | `'3'` | — | — | kelis kartus per mėnesį | — |
| `bendravimas_giminaiciai` | `'4'` | — | — | kartą per mėnesį | — |
| `bendravimas_giminaiciai` | `'5'` | — | — | bent kartą per 12 mėnesių | — |
| `bendravimas_giminaiciai` | `'6'` | — | — | niekada | — |
| `bendravimas_giminaiciai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `bendravimas_draugai` | `'1'` | — | — | kasdien | — |
| `bendravimas_draugai` | `'2'` | — | — | kiekvieną savaitę (ne kasdien) | — |
| `bendravimas_draugai` | `'3'` | — | — | kelis kartus per mėnesį | — |
| `bendravimas_draugai` | `'4'` | — | — | kartą per mėnesį | — |
| `bendravimas_draugai` | `'5'` | — | — | bent kartą per 12 mėnesių | — |
| `bendravimas_draugai` | `'6'` | — | — | niekada | — |
| `bendravimas_draugai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `nerimas` | `'1'` | — | — | ne, nebuvo | — |
| `nerimas` | `'2'` | — | — | taip, bet ne labiau nei anksčiau | — |
| `nerimas` | `'3'` | — | — | taip, ir šiek tiek labiau nei anksčiau | — |
| `nerimas` | `'4'` | — | — | taip, ir daug labiau nei anksčiau | — |
| `nerimas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `gyvenimo_kokybe` | `'1'` | — | — | labai gera | — |
| `gyvenimo_kokybe` | `'2'` | — | — | gera | — |
| `gyvenimo_kokybe` | `'3'` | — | — | patenkinama | — |
| `gyvenimo_kokybe` | `'4'` | — | — | bloga | — |
| `gyvenimo_kokybe` | `'5'` | — | — | labai bloga | — |
| `gyvenimo_kokybe` | `'9'` | — | — | neatsakyta į klausimą | — |
| `sveikata` | `'1'` | — | — | labai gera | — |
| `sveikata` | `'2'` | — | — | gera | — |
| `sveikata` | `'3'` | — | — | patenkinama | — |
| `sveikata` | `'4'` | — | — | bloga | — |
| `sveikata` | `'5'` | — | — | labai bloga | — |
| `sveikata` | `'9'` | — | — | neatsakyta į klausimą | — |
| `laimingumas` | `'1'` | — | — | labai laimingas (-a) | — |
| `laimingumas` | `'2'` | — | — | laimingas (-a) | — |
| `laimingumas` | `'3'` | — | — | nei laimingas (-a) nei nelaimingas (-a) | — |
| `laimingumas` | `'4'` | — | — | nelaimingas (-a) | — |
| `laimingumas` | `'5'` | — | — | labai nelaimingas (-a) | — |
| `laimingumas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `gyvensenos_pakeitimas` | `'1'` | — | — | taip | — |
| `gyvensenos_pakeitimas` | `'2'` | — | — | ne | — |
| `gyvensenos_pakeitimas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `sveikiau_maintintis` | `'1'` | — | — | taip | — |
| `sveikiau_maintintis` | `'2'` | — | — | taip, bandžiau, bet nesėkmingai | — |
| `sveikiau_maintintis` | `'3'` | — | — | ne | — |
| `sveikiau_maintintis` | `'9'` | — | — | neatsakyta į klausimą | — |
| `tapti_fiziskai_aktyvesniu` | `'1'` | — | — | taip | — |
| `tapti_fiziskai_aktyvesniu` | `'2'` | — | — | taip, bandžiau, bet nesėkmingai | — |
| `tapti_fiziskai_aktyvesniu` | `'3'` | — | — | ne | — |
| `tapti_fiziskai_aktyvesniu` | `'9'` | — | — | neatsakyta į klausimą | — |
| `maziau_rukyti` | `'1'` | — | — | taip | — |
| `maziau_rukyti` | `'2'` | — | — | taip, bandžiau, bet nesėkmingai | — |
| `maziau_rukyti` | `'3'` | — | — | ne | — |
| `maziau_rukyti` | `'9'` | — | — | neatsakyta į klausimą | — |
| `maziau_vartoti_alkoholiu` | `'1'` | — | — | taip | — |
| `maziau_vartoti_alkoholiu` | `'2'` | — | — | taip, bandžiau, bet nesėkmingai | — |
| `maziau_vartoti_alkoholiu` | `'3'` | — | — | ne | — |
| `maziau_vartoti_alkoholiu` | `'9'` | — | — | neatsakyta į klausimą | — |
| `zino_profilaktines_programas` | `'1'` | — | — | taip | — |
| `zino_profilaktines_programas` | `'2'` | — | — | ne | — |
| `zino_profilaktines_programas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `zino_sveikatos_stiprinimas` | `'1'` | — | — | taip | — |
| `zino_sveikatos_stiprinimas` | `'2'` | — | — | ne | — |
| `zino_sveikatos_stiprinimas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `zino_zalingi_aplinkos_veiksniai` | `'1'` | — | — | taip | — |
| `zino_zalingi_aplinkos_veiksniai` | `'2'` | — | — | ne | — |
| `zino_zalingi_aplinkos_veiksniai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `zino_uzkreciamosios_ligos` | `'1'` | — | — | taip | — |
| `zino_uzkreciamosios_ligos` | `'2'` | — | — | ne | — |
| `zino_uzkreciamosios_ligos` | `'9'` | — | — | neatsakyta į klausimą | — |
| `zino_individualios_konsultacijos` | `'1'` | — | — | taip | — |
| `zino_individualios_konsultacijos` | `'2'` | — | — | ne | — |
| `zino_individualios_konsultacijos` | `'9'` | — | — | neatsakyta į klausimą | — |
| `zino_mokymai` | `'1'` | — | — | taip | — |
| `zino_mokymai` | `'2'` | — | — | ne | — |
| `zino_mokymai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `zino_sveikatos_skatinimas` | `'1'` | — | — | taip | — |
| `zino_sveikatos_skatinimas` | `'2'` | — | — | ne | — |
| `zino_sveikatos_skatinimas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `zino_kita` | `'1'` | — | — | taip | — |
| `zino_kita` | `'2'` | — | — | ne | — |
| `zino_kita` | `'9'` | — | — | neatsakyta į klausimą | — |
| `dalyvauja_profilaktines_programas` | `'1'` | — | — | taip | — |
| `dalyvauja_profilaktines_programas` | `'2'` | — | — | ne | — |
| `dalyvauja_profilaktines_programas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `dalyvauja_sveikatos_stiprinimas` | `'1'` | — | — | taip | — |
| `dalyvauja_sveikatos_stiprinimas` | `'2'` | — | — | ne | — |
| `dalyvauja_sveikatos_stiprinimas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `naudoja_info_zalingi_aplinkos_veiksniai` | `'1'` | — | — | taip | — |
| `naudoja_info_zalingi_aplinkos_veiksniai` | `'2'` | — | — | ne | — |
| `naudoja_info_zalingi_aplinkos_veiksniai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `naudoja_info_uzkreciamosios_ligos` | `'1'` | — | — | taip | — |
| `naudoja_info_uzkreciamosios_ligos` | `'2'` | — | — | ne | — |
| `naudoja_info_uzkreciamosios_ligos` | `'9'` | — | — | neatsakyta į klausimą | — |
| `dalyvauja_individualios_konsultacijos` | `'1'` | — | — | taip | — |
| `dalyvauja_individualios_konsultacijos` | `'2'` | — | — | ne | — |
| `dalyvauja_individualios_konsultacijos` | `'9'` | — | — | neatsakyta į klausimą | — |
| `dalyvauja_mokymai` | `'1'` | — | — | taip | — |
| `dalyvauja_mokymai` | `'2'` | — | — | ne | — |
| `dalyvauja_mokymai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `dalyvauja_sveikatos_skatinimas` | `'1'` | — | — | taip | — |
| `dalyvauja_sveikatos_skatinimas` | `'2'` | — | — | ne | — |
| `dalyvauja_sveikatos_skatinimas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `naudoja_kita` | `'1'` | — | — | taip | — |
| `naudoja_kita` | `'2'` | — | — | ne | — |
| `naudoja_kita` | `'9'` | — | — | neatsakyta į klausimą | — |
| `patenkinti_profilaktines_programas` | `'1'` | — | — | taip | — |
| `patenkinti_profilaktines_programas` | `'2'` | — | — | ne | — |
| `patenkinti_profilaktines_programas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `patenkinti_sveikatos_stiprinimas` | `'1'` | — | — | taip | — |
| `patenkinti_sveikatos_stiprinimas` | `'2'` | — | — | ne | — |
| `patenkinti_sveikatos_stiprinimas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `patenkinti_info_zalingi_aplinkos_veiksniai` | `'1'` | — | — | taip | — |
| `patenkinti_info_zalingi_aplinkos_veiksniai` | `'2'` | — | — | ne | — |
| `patenkinti_info_zalingi_aplinkos_veiksniai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `patenkinti_info_uzkreciamosios_ligos` | `'1'` | — | — | taip | — |
| `patenkinti_info_uzkreciamosios_ligos` | `'2'` | — | — | ne | — |
| `patenkinti_info_uzkreciamosios_ligos` | `'9'` | — | — | neatsakyta į klausimą | — |
| `patenkinti_individualios_konsultacijos` | `'1'` | — | — | taip | — |
| `patenkinti_individualios_konsultacijos` | `'2'` | — | — | ne | — |
| `patenkinti_individualios_konsultacijos` | `'9'` | — | — | neatsakyta į klausimą | — |
| `patenkinti_mokymai` | `'1'` | — | — | taip | — |
| `patenkinti_mokymai` | `'2'` | — | — | ne | — |
| `patenkinti_mokymai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `patenkinti_sveikatos_skatinimas` | `'1'` | — | — | taip | — |
| `patenkinti_sveikatos_skatinimas` | `'2'` | — | — | ne | — |
| `patenkinti_sveikatos_skatinimas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `patenkinti_kita` | `'1'` | — | — | taip | — |
| `patenkinti_kita` | `'2'` | — | — | ne | — |
| `patenkinti_kita` | `'9'` | — | — | neatsakyta į klausimą | — |
| `info_vs_prieziuros_paslaugos` | `'1'` | — | — | iš televizijos, radijo, skaičiau spaudoje, internete | — |
| `info_vs_prieziuros_paslaugos` | `'2'` | — | — | iš draugų, artimųjų | — |
| `info_vs_prieziuros_paslaugos` | `'3'` | — | — | iš šeimos gydytojo | — |
| `info_vs_prieziuros_paslaugos` | `'4'` | — | — | iš kito sveikatos priežiūros specialisto | — |
| `info_vs_prieziuros_paslaugos` | `'5'` | — | — | iš savivaldybės visuomenės sveikatos biuro | — |
| `info_vs_prieziuros_paslaugos` | `'6'` | — | — | iš nacionalinių visuomenės sveikatos priežiūros įstaigų | — |
| `info_vs_prieziuros_paslaugos` | `'7'` | — | — | iš nevyriausybinių organizacijų | — |
| `info_vs_prieziuros_paslaugos` | `'8'` | — | — | kita | — |
| `info_vs_prieziuros_paslaugos` | `'9'` | — | — | neatsakyta į klausimą | — |
| `patirtis` | `'1'` | — | — | labai patenkintas (-a) | — |
| `patirtis` | `'2'` | — | — | patenkintas (-a) | — |
| `patirtis` | `'3'` | — | — | nei patenkintas (-a) nei nepatenkintas (-a) | — |
| `patirtis` | `'4'` | — | — | nepatenkintas (-a) | — |
| `patirtis` | `'5'` | — | — | labai nepatenkintas (-a) | — |
| `patirtis` | `'6'` | — | — | nesinaudojau | — |
| `patirtis` | `'9'` | — | — | neatsakyta į klausimą | — |
| `triuksmas` | `'1'` | — | — | taip, pakankamai | — |
| `triuksmas` | `'2'` | — | — | taip, bet nepakankamai | — |
| `triuksmas` | `'3'` | — | — | ne | — |
| `triuksmas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `aplinkos_uzterstumas` | `'1'` | — | — | taip, pakankamai | — |
| `aplinkos_uzterstumas` | `'2'` | — | — | taip, bet nepakankamai | — |
| `aplinkos_uzterstumas` | `'3'` | — | — | ne | — |
| `aplinkos_uzterstumas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `ultravioletine_spinduliuote` | `'1'` | — | — | taip, pakankamai | — |
| `ultravioletine_spinduliuote` | `'2'` | — | — | taip, bet nepakankamai | — |
| `ultravioletine_spinduliuote` | `'3'` | — | — | ne | — |
| `ultravioletine_spinduliuote` | `'9'` | — | — | neatsakyta į klausimą | — |
| `chemine_medziaga` | `'1'` | — | — | taip, pakankamai | — |
| `chemine_medziaga` | `'2'` | — | — | taip, bet nepakankamai | — |
| `chemine_medziaga` | `'3'` | — | — | ne | — |
| `chemine_medziaga` | `'9'` | — | — | neatsakyta į klausimą | — |
| `info_aplinkos_rizikos_veiksniai` | `'1'` | — | — | iš televizijos, radijo, skaičiau spaudoje, internete | — |
| `info_aplinkos_rizikos_veiksniai` | `'2'` | — | — | iš draugų, artimųjų | — |
| `info_aplinkos_rizikos_veiksniai` | `'3'` | — | — | iš šeimos gydytojo | — |
| `info_aplinkos_rizikos_veiksniai` | `'4'` | — | — | iš kito sveikatos priežiūros specialisto | — |
| `info_aplinkos_rizikos_veiksniai` | `'5'` | — | — | iš savivaldybės visuomenės sveikatos biuro | — |
| `info_aplinkos_rizikos_veiksniai` | `'6'` | — | — | iš nacionalinių visuomenės sveikatos priežiūros įstaigų | — |
| `info_aplinkos_rizikos_veiksniai` | `'7'` | — | — | iš nevyriausybinių organizacijų | — |
| `info_aplinkos_rizikos_veiksniai` | `'8'` | — | — | kita | — |
| `info_aplinkos_rizikos_veiksniai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `info_ligos_gydymas` | `'1'` | — | — | labai sunku | — |
| `info_ligos_gydymas` | `'2'` | — | — | sunku | — |
| `info_ligos_gydymas` | `'3'` | — | — | lengva | — |
| `info_ligos_gydymas` | `'4'` | — | — | labai lengva | — |
| `info_ligos_gydymas` | `'5'` | — | — | nežinau | — |
| `info_ligos_gydymas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `info_profesionali_pagalba` | `'1'` | — | — | labai sunku | — |
| `info_profesionali_pagalba` | `'2'` | — | — | sunku | — |
| `info_profesionali_pagalba` | `'3'` | — | — | lengva | — |
| `info_profesionali_pagalba` | `'4'` | — | — | labai lengva | — |
| `info_profesionali_pagalba` | `'5'` | — | — | nežinau | — |
| `info_profesionali_pagalba` | `'9'` | — | — | neatsakyta į klausimą | — |
| `suprasti_gydytojas` | `'1'` | — | — | labai sunku | — |
| `suprasti_gydytojas` | `'2'` | — | — | sunku | — |
| `suprasti_gydytojas` | `'3'` | — | — | lengva | — |
| `suprasti_gydytojas` | `'4'` | — | — | labai lengva | — |
| `suprasti_gydytojas` | `'5'` | — | — | nežinau | — |
| `suprasti_gydytojas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `suprasti_vartoti_vaistus` | `'1'` | — | — | labai sunku | — |
| `suprasti_vartoti_vaistus` | `'2'` | — | — | sunku | — |
| `suprasti_vartoti_vaistus` | `'3'` | — | — | lengva | — |
| `suprasti_vartoti_vaistus` | `'4'` | — | — | labai lengva | — |
| `suprasti_vartoti_vaistus` | `'5'` | — | — | nežinau | — |
| `suprasti_vartoti_vaistus` | `'9'` | — | — | neatsakyta į klausimą | — |
| `ivertinti_kitas_gydytojas` | `'1'` | — | — | labai sunku | — |
| `ivertinti_kitas_gydytojas` | `'2'` | — | — | sunku | — |
| `ivertinti_kitas_gydytojas` | `'3'` | — | — | lengva | — |
| `ivertinti_kitas_gydytojas` | `'4'` | — | — | labai lengva | — |
| `ivertinti_kitas_gydytojas` | `'5'` | — | — | nežinau | — |
| `ivertinti_kitas_gydytojas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `pasinaudoti_gydytojo_info` | `'1'` | — | — | labai sunku | — |
| `pasinaudoti_gydytojo_info` | `'2'` | — | — | sunku | — |
| `pasinaudoti_gydytojo_info` | `'3'` | — | — | lengva | — |
| `pasinaudoti_gydytojo_info` | `'4'` | — | — | labai lengva | — |
| `pasinaudoti_gydytojo_info` | `'5'` | — | — | nežinau | — |
| `pasinaudoti_gydytojo_info` | `'9'` | — | — | neatsakyta į klausimą | — |
| `laikytis_nurodymu` | `'1'` | — | — | labai sunku | — |
| `laikytis_nurodymu` | `'2'` | — | — | sunku | — |
| `laikytis_nurodymu` | `'3'` | — | — | lengva | — |
| `laikytis_nurodymu` | `'4'` | — | — | labai lengva | — |
| `laikytis_nurodymu` | `'5'` | — | — | nežinau | — |
| `laikytis_nurodymu` | `'9'` | — | — | neatsakyta į klausimą | — |
| `rasti_info_psichikos_sveikata` | `'1'` | — | — | labai sunku | — |
| `rasti_info_psichikos_sveikata` | `'2'` | — | — | sunku | — |
| `rasti_info_psichikos_sveikata` | `'3'` | — | — | lengva | — |
| `rasti_info_psichikos_sveikata` | `'4'` | — | — | labai lengva | — |
| `rasti_info_psichikos_sveikata` | `'5'` | — | — | nežinau | — |
| `rasti_info_psichikos_sveikata` | `'9'` | — | — | neatsakyta į klausimą | — |
| `suprasti_ispejimus_zalinga_sveikatai` | `'1'` | — | — | labai sunku | — |
| `suprasti_ispejimus_zalinga_sveikatai` | `'2'` | — | — | sunku | — |
| `suprasti_ispejimus_zalinga_sveikatai` | `'3'` | — | — | lengva | — |
| `suprasti_ispejimus_zalinga_sveikatai` | `'4'` | — | — | labai lengva | — |
| `suprasti_ispejimus_zalinga_sveikatai` | `'5'` | — | — | nežinau | — |
| `suprasti_ispejimus_zalinga_sveikatai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `suprasti_profilaktyniai_tyrimai` | `'1'` | — | — | labai sunku | — |
| `suprasti_profilaktyniai_tyrimai` | `'2'` | — | — | sunku | — |
| `suprasti_profilaktyniai_tyrimai` | `'3'` | — | — | lengva | — |
| `suprasti_profilaktyniai_tyrimai` | `'4'` | — | — | labai lengva | — |
| `suprasti_profilaktyniai_tyrimai` | `'5'` | — | — | nežinau | — |
| `suprasti_profilaktyniai_tyrimai` | `'9'` | — | — | neatsakyta į klausimą | — |
| `ivertinti_info_patikimumas` | `'1'` | — | — | labai sunku | — |
| `ivertinti_info_patikimumas` | `'2'` | — | — | sunku | — |
| `ivertinti_info_patikimumas` | `'3'` | — | — | lengva | — |
| `ivertinti_info_patikimumas` | `'4'` | — | — | labai lengva | — |
| `ivertinti_info_patikimumas` | `'5'` | — | — | nežinau | — |
| `ivertinti_info_patikimumas` | `'9'` | — | — | neatsakyta į klausimą | — |
| `nuspresti_apsauga` | `'1'` | — | — | labai sunku | — |
| `nuspresti_apsauga` | `'2'` | — | — | sunku | — |
| `nuspresti_apsauga` | `'3'` | — | — | lengva | — |
| `nuspresti_apsauga` | `'4'` | — | — | labai lengva | — |
| `nuspresti_apsauga` | `'5'` | — | — | nežinau | — |
| `nuspresti_apsauga` | `'9'` | — | — | neatsakyta į klausimą | — |
| `rasti_veiksniai_psichikos_sveikata` | `'1'` | — | — | labai sunku | — |
| `rasti_veiksniai_psichikos_sveikata` | `'2'` | — | — | sunku | — |
| `rasti_veiksniai_psichikos_sveikata` | `'3'` | — | — | lengva | — |
| `rasti_veiksniai_psichikos_sveikata` | `'4'` | — | — | labai lengva | — |
| `rasti_veiksniai_psichikos_sveikata` | `'5'` | — | — | nežinau | — |
| `rasti_veiksniai_psichikos_sveikata` | `'9'` | — | — | neatsakyta į klausimą | — |
| `suprasti_seimos_patarimus` | `'1'` | — | — | labai sunku | — |
| `suprasti_seimos_patarimus` | `'2'` | — | — | sunku | — |
| `suprasti_seimos_patarimus` | `'3'` | — | — | lengva | — |
| `suprasti_seimos_patarimus` | `'4'` | — | — | labai lengva | — |
| `suprasti_seimos_patarimus` | `'5'` | — | — | nežinau | — |
| `suprasti_seimos_patarimus` | `'9'` | — | — | neatsakyta į klausimą | — |
| `suprasti_ziniasklaidos_info` | `'1'` | — | — | labai sunku | — |
| `suprasti_ziniasklaidos_info` | `'2'` | — | — | sunku | — |
| `suprasti_ziniasklaidos_info` | `'3'` | — | — | lengva | — |
| `suprasti_ziniasklaidos_info` | `'4'` | — | — | labai lengva | — |
| `suprasti_ziniasklaidos_info` | `'5'` | — | — | nežinau | — |
| `suprasti_ziniasklaidos_info` | `'9'` | — | — | neatsakyta į klausimą | — |
| `ivertinti_iprociu_itaka` | `'1'` | — | — | labai sunku | — |
| `ivertinti_iprociu_itaka` | `'2'` | — | — | sunku | — |
| `ivertinti_iprociu_itaka` | `'3'` | — | — | lengva | — |
| `ivertinti_iprociu_itaka` | `'4'` | — | — | labai lengva | — |
| `ivertinti_iprociu_itaka` | `'5'` | — | — | nežinau | — |
| `ivertinti_iprociu_itaka` | `'9'` | — | — | neatsakyta į klausimą | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/gyvensena/suaugusiu.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/gyvensena/suaugusiu.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/gyvensena/suaugusiu (https://data.gov.lt/datasets/1226/)
