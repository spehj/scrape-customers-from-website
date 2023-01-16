# Python Developer PredictLeads naloge

Najprej naloži vse potrebne knjižnice iz requirements.txt datoteke.

```bash
pip install -r requirements.txt
```

## Naloga 1

Za preizkus naloge 1 poženi skripto **get_customers.py** z argumentom, ki naj vsebuje ime končne JSON datoteke. Ta vsebuje ime stranke in povezavo do logotipa stranke.

Primer:

```bash
python get_customers.py customers.json
```

Datoteka **scraper.py** vsebuje objekt in metoda za scrapanje strani https://scale.com/.

Rezultat naloge se nahaja v datoteki **customers.json**.

## Naloga 2

Ideje:

Prva možnost je poiskati testamonials sekcijo na domači strani in iz nje dobiti img element, ki vsebuje vir slike. Npr. poiščemo elemente, ki imajo v imenu classa "logo". Nato poiščemo child element tipa img, ki ima začetek src v obliki "https://...". Kateremu podjetju pripada ta logo se lahko ugotovi preko kakšnega servica, ki to počne (npr. google search ali podobno).

Vsaka stran vsebuje svojo podstran /customers (ali podobno poddomeno, razvidna je iz menija domače strani ali pa iz footerja). Tu bi iskal ključne besede kot so Customers, Case studies, Customer Stories, Success Stories itd. Te strani se razlikujejo, zato bi uporabil naslednji pristop.

Najprej ugotovimo, za katero od teh ključnih besed obstajajo a linki. Izberemo ta link in pridemo recimo na podstran /customers.

Na /customers podstrani bi poiskal vse a elemente, ki imajo href, ki je sestavljen iz /customers/neko-podjetje. Neko-podjetje se nanaša na potencialen case study nekega podjetja. Scraper lahko klikne na to povezavo in s pomočjo NLP algoritma razbere kdo je stranka (preizkusil sem en random primer iz Gusto case studya s pomočjo chatGPT in je delovalo dobro - pravilno je razpoznalo ponudnika storitve in stranko). Na tej podstrani /customers/neko-podjetje, se lahko poišče img elemente, in se nato po hierarhiji navzgor gleda ali parent element vsebuje besedo "logo". Če jo vsebuje, lahko ta img element interpretiramo kot logo. Kateremu podjetju pripada ta logo se lahko ugotovi preko kakšnega servica, ki je temu namenjen. Tu je potrebno biti pazljiv in preveriti, ali se ime podjetja sklada s tistim, ki je razpoznano z NLP v besedilu na podstrani s case studyem (primer napačnega logota so logoti integracij pri case studijih pagerduty).

Druga možnost je, da se na strani /customers ponovno išče a linke s href, ki vsebujejo ključne besede: Stories, Studies, All, More. Scraper lahko pošlje requeste na te linke in pregleda naslednjo stran na prej opisan način.
