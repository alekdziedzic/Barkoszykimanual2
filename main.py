import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(page_title="Bar Koszyki - Manual", page_icon=Image.open("logo.png"))


def main():
    st.title("Bar koszyki - manual")
    st.caption("Wersja 1.1")
    menu = st.selectbox("Menu", ["Manual Koktajli", "Manual Alkoholi", "Piwo", "Wino"], key="menu")
    if menu == "Manual Koktajli":
        st.header("Manual Koktajli")
        df = pd.read_csv("ExternalFIles/koktajle.csv", sep=";", encoding="Windows-1250")

        szukaj = st.text_input("Znajdź koktajl", max_chars=25, key="szukaj",
        placeholder="np. Łiski Szałer", value="")

        for index, row in df.iterrows():
            name = f"**{row['nazwa']}** _({row['tagi']})_"
            if szukaj.lower() in name.lower():
                expand = st.expander(name)
                if row["historia"] != "0":
                    expand.caption(row["historia"])
                expand.write((row["receptura"]).replace(",", "<br>"), unsafe_allow_html=True)
                expand.image("CocktailImages/" + row["zdjecie"])
                expand.write(f"Metoda: {row['Metoda']}")
                if row['Lód'] != "0":
                    expand.write(f":blue[Lód]: {row['Lód']}")
                expand.write(f":green[Szkło]: {row['Szkło']}")
                if row['Garnish'] != "0":
                    expand.write(f":violet[Garnish]: {row['Garnish']}")

        st.caption(":grey[Materiały: Adrian Kot, Edycja: Aleksander Dziedzic]")
    elif menu == "Manual Alkoholi":
        st.header("Manual Alkoholi")
        rodzinki = pd.read_csv("ExternalFIles/Rodzina_alkohole.csv", sep=";", encoding="Windows-1250")
        alkohole = pd.read_csv("ExternalFIles/alkohole.csv", sep=";", encoding="Windows-1250")

        szukaj = st.text_input("Znajdź alkohol", max_chars=25, key="szukaj",
                               placeholder="np. Małpa 47", value="")

        for i, r in rodzinki.iterrows():
            name = f"**{r['Marka']}** _({r['Tagi']})_"
            expand = st.expander(name)
            if szukaj.lower() in name.lower():
                if r["Historia marki"] != "0":
                    expand.caption(r["Historia marki"])
                for index, row in alkohole.iterrows():
                    if r["Marka"] == row["rodzina"]:
                        expand.subheader(row["alkohol"])
                        if row["historia"] != "0":
                            expand.caption(row["historia"])
                        expand.markdown(row["opis"])
                        expand.image("AlcoholImages/" + row["zdjecie"])
                        if row["aromat"] != "0":
                            expand.markdown(f":blue[Aromat]: {row['aromat'].capitalize()}")
                        if row["smak"] != "0":
                            expand.markdown(f":green[Smak]: {row['smak'].capitalize()}")
                        if row["finisz"] != "0":
                            expand.markdown(f":violet[Finisz]: {row['finisz'].capitalize()}")

    elif menu == "Piwo":
        st.header("Opis piw")
        st.subheader("Bierhalle Pills (lager)")
        st.write('''Pils to najbardziej rozpowszechniony gatunek piwa na świecie 
                  (mocno powiązany z pilsnerem). Piwo jasne, dolnej fermentacji (przypis poniżej), 
                  istensywna chmielowa goryczka połączona ze smakiem słodu jęczmiennego. <br> <br>
                  Alkohol: 5.0%''', unsafe_allow_html=True)

        st.subheader("Bierhalle Weizen (pszeniczne)")
        st.write('''Weizen jest piwem górnej fermentacji (przypis poniżej) 
                  o wyczuwalnym zapachu: bananowo-goździkowym, cynamonu oraz aromatycznego chmielu. 
                  Goryczka przeplata się ze smakiem pszenicznego słodu. Większa ilość "bąbelków"  
                  sprawia, że piwo pszeniczne nabiera lekko kwaskowatego smaku i doskonale gasi 
                  pragnienie. Słód pszeniczny stanowi ponad 50% całkowitego zasypu. <br> <br>
                  Alkohol: 5.2%''', unsafe_allow_html=True)
        st.subheader("Bierhalle Marcowe (podwójnie słodowany lager)")
        st.write('''Piwo marcowe, zwane również Oktoberfestbier, dawniej warzone było 
                  tylko sezonowo. Dzisiaj, dzięki nowoczesnym systemom chłodzenia można produkować 
                  je okrągły rok. Piwo jest pełne smaków pochodzących z mieszaniny słodów 
                  jęczmiennych i aromatycznego chmielu. <br> <br>
                  Alkohol: 5.2%''', unsafe_allow_html=True)
        st.subheader("Pilsner Urquell")
        st.write('''Prekursor piw typu lager. Tworzony metodą równoległego warzenia. 
                  Swoją wyjątkowość zawdzięcza wielu innowacjom w produkcji piwa, niezmiennym 
                  od ponad 175 lat sposobem produkcji, oraz stosowaniu rzadko już spotykanej 
                  techniki potrójnej dekokcji (przypis poniżej). 
                  Od pierwszego łyku atakuje wyraźna ziołowa goryczka — krótka i przyjemna. 
                  Dobrze równoważy smak jasnego słodu, maślany finisz. Smak jest kwintesencją 
                  zwrotu czysty profilowo pils. Nic tutaj się nie kłóci, każdy akcent jest wyważony 
                  i ma dla siebie odpowiednio dużo miejsca, aby wybrzmieć. Pilsner pachnie mieszanką 
                  ziół, kojarzącą się z miksem tymianku i trawy cytrynowej. 
                  (Czysto, rześko, przyjemnie.)<br> <br>
                  Alkohol: 4.4%
                  ''', unsafe_allow_html=True)

        slide1 = st.expander("Ciężkie słowa (pojęcia dla nerdów)")

        slide1.header("Drożdże dolnej fermentacji")
        slide1.write('''Podczas fermentacji, drożdże dolnej fermentacji zbierają się 
                  na dnie (stąd nazwa). Optymalna temperatura fermentacji dla drożdży dolnej 
                  fermentacji wynosi w przybliżeniu 10°C. Wykorzystywane przy produkcji lagerów.''')

        slide1.header("Drożdże górnej fermentacji")
        slide1.write('''
                  Podczas fermentacji, drożdże górnej fermentacji "wspinają" się na powierzchnię 
                  młodego piwa i tworzą tam warstwę piany (stąd nazwa). Optymalna temperatura 
                  fermentacji dla drożdży górnej fermentacji wynosi w przybliżeniu 20°C.
                  Główną cechą odróżniającą piwa górnej fermentacji jest ich
                  kwiatowy zapach i owocowy smak.''')

        slide1.header("Dekokcja (zacieranie dekokcyjne)")
        slide1.write('''
                  Typ zacierania w którym różne temperatury zacierania są osiągnięte przez 
                  odebranie części zacieru, zagotowanie go w osobnym zbiorniku, następnie użycie 
                  go jako woda infuzyjna aby ogrzać pozostały zacier. Jest to tradycyjna metoda 
                  używana w wielu kontynentalnych europejskich stylach piw, 
                  a w szczególności w niemieckich i czeskich.<br>

                  W metodzie dekokcyjnej wyróżnia się system jednowarowy, dwuwarowy oraz 
                  trójwarowy. Oznacza to, że dekokcja została przeprowadzona jednokrotnie, 
                  dwukrotnie lub trzykrotnie. Ze względów ekonomicznych metoda dekokcyjna 
                  zacierania słodu stosowana jest obecnie rzadko. Najczęściej stosuje się ją 
                  przy warzeniu koźlaków, piw pszenicznych lub pilznerów.''', unsafe_allow_html=True)

        slide1.header("Metoda równoległego warzenia (Pilsner)")
        slide1.write('''
                  [...]kiedy browar został zmodernizowany w 1992 roku i wprowadziliśmy nową 
                  technologię, zaczęliśmy fermentować i leżakować większość naszego piwa w 
                  zbiornikach ze stali nierdzewnej znajdujących się nad ziemią. Oznaczało to,  
                  że mogliśmy dokładniej kontrolować proces warzenia, na przykład temperaturę
                  i ilość dodawanych drożdży.<br> <br>

                  Oczywiście obawialiśmy się, czy ta zmiana nie wpłynie na smak naszego piwa - 
                  zawsze się o to martwimy! Tak więc zespół pod kierownictwem Václava Berki, 
                  naszego Mistrza Warzelnictwa, zdecydował, że powinniśmy nadal warzyć 
                  niewielką porcję naszego piwa w piwnicach - w ten sposób można je porównać 
                  z piwem produkowanym w nowych zbiornikach. Nazwaliśmy to równoległym warzeniem. <br> <br>

                  Proces ten polega na warzeniu piwa w taki sam sposób, jak robiliśmy to od 
                  zawsze, a następnie przeprowadzeniu porównawczych testów smakowych w 
                  laboratorium przez zespół obecnych i emerytowanych Mistrzów Warzelnictwa, 
                  a także przez panel degustatorów browaru. Chodzi nam o to, aby zespół 
                  ekspertów nie znalazł między nimi żadnych różnic - w ten sposób możemy 
                  być pewni, że zachowaliśmy spójność jakości naszego piwa. [...]
                  ''', unsafe_allow_html=True)
        slide1.caption(":grey[źródło: **pilsnerurquell.com**]")

        st.header("Proces produkcji piwa")
        st.subheader("Do produkcji piwa wykorzystywane są cztery różne składniki")

        slod = st.expander("Słód")
        slod.write('''
                  Słód jest produkowany z ziarna, głównie jęczmiennego. Pierwszą czynnością 
                  jest dokładne oczyszczenie ziarna. Oczyszczone ziarno jest moczone w 
                  wodzie aż do uzyskania wymaganej wilgotności wynoszącej 44 %. Następnie 
                  ziarno kiełkuje w warunkach, gdzie kontrolowane są: temperatura i 
                  wilgotność. Podczas tego procesu zawarte enzymy zostają pobudzone do 
                  działania, a skrobia i białko zawarte w ziarnie jęczmienia zostaje 
                  częściowo rozłożone. Słód z kiełkami trafia do suszarni gdzie jest suszony. 
                  Im temperatura suszenia jest wyższa, tym więcej cukrów ulega karmelizacji. 
                  Im więcej powstanie karmelu tym ciemniejsze piwo zostanie wyprodukowane z 
                  takiego słodu. Zawartość alkoholu w piwie zależy od ilości słodu, jaką 
                  używa się do jego wyprodukowania, a nie od koloru: jasnego czy 
                  ciemnego piwa.''')

        woda = st.expander("Woda")
        woda.write('''
                  Dla produkcji piwa duże znaczenie ma to, czy woda używana do produkcji 
                  jest czysta i wolna od zanieczyszczeń. W przeciwieństwie do przeszłości, 
                  zawartość minerałów w wodzie (twardość wody) nie ma decydującego znaczenia 
                  od czasu, kiedy możliwe jest zrównoważenie składu chemicznego wody przez 
                  sposób słodowania (wytwarzania słodu) i operacje technologiczne 
                  podczas produkcji piwa.''')

        chmiel = st.expander("Chmiel")
        chmiel.write('''
                  Prócz dostarczenia odpowiedniego zapachu i goryczki, chmiel wykonuje 
                  podczas procesu produkcji piwa ważne zadanie: jest antyseptykiem. 
                  Ze względu na zawartość naturalnych olejków (podobne jak rumianek i eukaliptus)  
                  zabezpiecza piwo przed jego nieoczekiwanym zepsuciem. 
                  (W "Bierhalle" używane są chmiele goryczkowe i aromatyczne).''')

        drozdze = st.expander("Drożdże")
        drozdze.write('''
                  Podczas procesu fermentacji, zadaniem drożdży jest zamiana cukrów 
                  rozpuszczonych w wodzie, a pochodzących ze słodu w alkohol i CO2. 
                  Są dwa ważne typy drożdży: drożdże górnej fermentacji i drożdże dolnej
                  fermentacji. Podczas fermentacji, drożdże górnej fermentacji "wspinają" 
                  się na powierzchnię młodego piwa i tworzą tam warstwę piany (stąd nazwa). 
                  Optymalna temperatura fermentacji dla drożdży górnej fermentacji wynosi 
                  w przybliżeniu 20°C. Podczas fermentacji, drożdże dolnej fermentacji 
                  zbierają się na dnie (stąd nazwa). Optymalna temperatura fermentacji 
                  dla drożdży dolnej fermentacji wynosi w przybliżeniu 10°C. Główną cechą 
                  odróżniającą piwa górnej fermentacji jest ich kwiatowy zapach i owocowy smak.''')

        st.header("Prawo czystości piw Bierhalle")
        st.write('''
                  Piwo w Bierhalle produkowane jest zgodnie z edyktem Reinheitsgebot (Prawo Czystości) 
                  z 1516r., według którego do produkcji piwa używamy wyłącznie czterech surowców: 
                  wody, słodu, chmielu i drożdży. Piwa nie zawierają żadnych stabilizatorów ani konserwantów, 
                  są niepasteryzowane i niefiltrowane, wysycone naturalnym dwutlenkiem węgla, 
                  pochodzącym z długotrwałego procesu fermentacji i leżakowania.''')
    elif menu == "Wino":
        st.header(":red[Czerwone wina]")
        df1 = pd.read_csv("ExternalFIles/czerwone_wina.csv")
        st.table(df1)

        carmenere = st.expander("Aresti Carmenere Reserva")
        carmenere.write('''
        Carmenere z serii "CABINA 56" upamiętnia pierwszego pick-upa 
        należącego do Vicente Aresti - założyciela winnicy. Używał go 
        przez wiele lat podczas każdego zbioru. Ten model miał wielką
        charakterystyczną kabinę, dlatego od początku był nazywany "kabiną". 
        Od ponad 60 lat ten klasyczny już pojazd należy do rodziny. 
        Wino leżakowało w dębowych beczkach ok. 12 miesięcy.
        <br> <br>
        Nos to czerwone owoce, także jeżyny, akcenty czekolady i wanilii.<br> <br>
        :blue[Sugestie kulinarne]: łagodne sosy, pieczenie, kaczki, dania z grilla.''', unsafe_allow_html=True)
        carmenere.image("Wineimages/czerwone/carmenere.jpg")

        monte = st.expander("Gran Sasso Montepulciano D’Abruzzo")
        monte.write('''
        Winnice zlokalizowane w Crecchio, San Salvo oraz Pollutri. 
        Odszypułkowanie i delikatne prasowanie gron. Maceracja przez 15 dni w 
        kadziach ze stalli nierdzewnej. Fermentacja i dojrzewanie w 
        beczkach z francuskiego dębu przez dwa do trzech miesięcy.
        <br> <br>
        Dobrze zbudowane wino o mocnych aromatach owocowych 
        ( jeżyny, śliwki, porzeczki i wiśnie), z lekkim akcentem ziołowym. 
        W ustach soczyste, zmysłowe, o miękkich garbnikach i stonowanej kwasowości.<br> <br>
        :blue[Sugestie kulinarne]: wędliny, mięsa z grilla, dojrzewające sery. 
        ''', unsafe_allow_html=True)
        monte.image("Wineimages/czerwone/monte.jpg")

        malbec = st.expander("Elsa Bianchi Malbec San Rafael Mendoza")
        malbec.write('''
        Klasyczny Malbec z aromatami dojrzałych śliwek i fiołków z aluwialnych gleb 
        w winnicach Finca Doña Elsa i Finca Asti (750 m n.p.m.), które 
        przekazują winu swoje mineralne nuty. Ręczny zbiór, fermentacja w kadziach
        ze stali nierdzewnej, dojrzewanie w dębinie.
        <br> <br>
        Aromaty dojrzałych śliwek i fiołków, podkreślonych delikatną nutą dębu. 
        W ustach zmysłowe, pełne owocu z dobrze ułożonymi taninami, jedwabistą fakturą
        i intensywnym owocowym posmakiem. Wszystkie te cechy dają w efekcie eleganckie,
        dobrze zbalansowane wino, które może być idealnym partnerem przy stole.<br> <br>
        :blue[Sugestie kulinarne]: Grillowane mięso
        ''', unsafe_allow_html=True)
        malbec.image("Wineimages/czerwone/malbec.jpg")

        primitivo = st.expander("Primitivo Botoromagno")
        primitivo.write('''
        Murgijskie Primitivo, jeden z najstarszych i najszlachetniejszych szczepów Apulii. 
        Sprowadzony na początku XIX wieku przez mnichów benedyktynów, prawdopodobnie z 
        Chorwacji. Winorośl prowadzona jest wyłącznie "na głowę" (goblet), o naturalnie 
        niskiej wydajności z hektara. 500 m n.p.m., niezwykła osobowość i głębia. Stare 
        winnice są zlokalizowane w Murgii. Ręczny zbiór. Dziesięciodniowa fermentacja na 
        skórkach w 26°-28°C. Fermentacja malolaktyczna, dojrzewanie w kadziach ze stali 
        nierdzewnej o kontrolowanej temperaturze przez 10 miesięcy, potem przez 
        6 miesięcy w butelce.
        <br> <br>
        Nos niezwykle owocowy z przewagą wiśni, czereśni i morwy czerwonej. 
        Nuty wanilii, cynamonu, szałwii, mięty i tytoniu dopełniają aromatycznej całości.
        Krągłe, otulające bardzo lekkimi taninami, eleganckie i pachnące wino, z nutami 
        porzeczek, śliwek, czarnego pieprzu i czekolady. <br> <br>
        :blue[Sugestie kulinarne]: wędliny, sery, jagnięcina z grilla i dziczyzna.
        ''', unsafe_allow_html=True)
        primitivo.image("Wineimages/czerwone/primitivo.png")

        st.header("Białe wina")
        df2 = pd.read_csv("ExternalFIles/biale_wina.csv")
        st.table(df2)

        chardonnay = st.expander('Aresti Chardonnay')
        chardonnay.write('''Wytrawne wino o żółtawej barwie z zielonymi refleksami. W nosie ekspresyjny
         aromat dojrzałych owoców ananasa, gruszek, cytrusów i bananów. W ustach wino bogate, cieliste, 
         miękkie i aksamitne z posmakiem wanilii i nutą kawy. 90 punktów w Wine Advocate Roberta Parkera. <br> <br>
        :blue[Sugestie kulinarne]: Drób, zwłaszcza kurczak i indyk''', unsafe_allow_html=True)
        chardonnay.image("Wineimages/białe/chardonnay.jpg")

        sauvignon = st.expander('Moulin de Gassac Sauvignon')
        sauvignon.write('''Wino białe, bardzo owocowe i rześkie z czystym aromatem agrestu i towarzyszącą mu nutą 
        cytrusów i brzoskwiń. W ustach świeże, owocowe, eleganckie.<br> <br>
        :blue[Sugestie kulinarne]: Sałatki, ryby i desery
        ''', unsafe_allow_html=True)
        sauvignon.image("Wineimages/białe/sauvignon.jpg")

        trebbiano = st.expander("Gran Sasso Trebbiano d'Abruzzo")
        trebbiano.write('''Lekkie, orzeźwiające wino o aromatach żółtych owoców (brzoskwinia i nieszpułka, głóg), z 
        nutami kwiatu pomarańczy. Delikatnie wytrawne, o średnim ekstrakcie. W ustach rześkie, owocowe, świeże, z 
        mocnym smakiem cytrusów i jabłek. Łagodne, dobrze zrównoważone. Szczególnie dobrze komponuje się z 
        lekkimi potrawami.<br> <br>
        :blue[Sugestie kulinarne]: Aperitif, lekkie dania z ryb, sałatki, owoce morza.
        ''', unsafe_allow_html=True)
        trebbiano.image("Wineimages/białe/trebbiano.jpg")

        riesling = st.expander('Klaus Meyer Riesling')
        riesling.write('''Żywy, wytrawny Riesling. Cytrusy, ananas i jabłka, podkreślone delikatną nutą siana i akcentem
         krzemienia. W ustach napięte, delikatnie słonawe z wyrazista owocowością i orzeźwiając kwasowością.<br> <br>
         :blue[Sugestie kulinarne]: Idealne wino do pełnych, obfitych dań.
         ''', unsafe_allow_html=True)
        riesling.image("Wineimages/białe/riesling.jpg")

        st.header("Wina musujące")
        st.subheader("Prosecco")
        st.caption("Z definicji białe wino musujące produkowane w północno-wschodnich Włoszech.")
        mpro = st.expander("Martini Prosecco")
        mpro.write('''Wino o delikatnym jasno słomkowym kolorze. Delikatny aromat ujawnia nuty kwitnącego sadu oraz 
        subtelne niuanse zielonych jabłek i gruszek. Orzeźwiający smak podkreśla cytrusowe i kwiatowe nuty z 
        eleganckimi ziołowymi niuansami. Posmak jest żywy i lekki.Polecany jako aperitif, do lekkich dań z ryb i 
        owoców morza, sałatek warzywnych oraz odtłuszczonych miękkich i twardych serów. Aby w pełni cieszyć się 
        wyjątkowym świeżym i lekkim smakiem tego wspaniałego wina, zalecasię schłodzenie do 6-8 °''')
        mpro.image("Wineimages/prosecco/martiniprosecco.jpg")
        mpro.caption("Źródło: alkoholeswiata24.pl")

        belstar = st.expander("Belstar")
        belstar.write('''Prosecco Belstar Brut należy do wielce zasłużonej dla regionu rodziny Bisol z Valdobbiadene. 
        Pierwsza udokumentowana wzmianka o działalności winiarskiej rodziny pochodzi z 1542 roku. Obecnie 
        posiadłościami o łącznej powierzchni upraw 177 h zarządza przedstawiciel 21 pokolenia Desiderio Bisol. W smaku 
        subtelne kwiatowo-owocowe aromaty. Wino produkowane jest metodą Charmata''')
        belstar.image('Wineimages/prosecco/belstar.jpg')
        belstar.caption("Źródło: wina.pl")

        st.subheader("Szampan")
        st.caption('''Szampan swoją nazwę zawdzięcza Szampanii - regionowi w północno-wschodniej Francji w którym jest
                   tworzony. "Bąbelki" nie są efektem nasycania napoju dwutlenkiem węgla, a jego wytworzeniem 
                   przy pomocy naturalnego procesu dojrzewania w butelce (metoda szampańska). Spośród innych win wyróżnia
                   się wieloma oryginalnymi cechami: <br> <br>
                   	:white_medium_square: Zbiór winogron jest ręczny (winogrona muszą być w idealnym stanie) <br> <br>
                   	:white_medium_square: To wino musujące utrzymywane pod ciśnieniem w butelce, zamkniętej 
                   	korkiem w kształcie grzyba (w przeciwieństwie do korków cylindrycznych), przytrzymywanym kapslem 
                   	i kagańcem z drutu. <br> <br>
                   	:white_medium_square: Marka (nieobowiązkowa) jest podstawowym elementem identyfikacji szampanów 
                   	(najbardziej poszukiwane są wina markowe)<br> <br>
                   	:white_medium_square: Jest to jedyne francuskie wino różowe, które może być wytwarzane przez 
                   	łączenie wina czerwonego (z Szampanii) z winem białym; różowy szampan uzyskuje się również 
                   	pozwalając skórce czarnych winogron zabarwić sok po wyciśnięciu.<br> <br>
                   	Do produkcji dopuszczane jest wiele odmian winorości z rodziny _pinot_. 3 najczęściej 
                   	wykorzystywane to: <br> <br>
                   	:white_medium_square: Chardonnay<br> 
                   	:white_medium_square: Pinot noir<br> 
                   	:white_medium_square: Pinot meunier''', unsafe_allow_html=True)
        mummcr = st.expander("Mumm cordon rouge brut")
        mummcr.caption('''Styl Domu Mumm charakteryzują subtelnie wyważone wina o świeżym i intensywnym smaku. Owoce 
        używane do produkcji szampana G.H.Mumm to najwyższej klasy winogrona szczepów białych Chardonnay oraz 
        czerwonych: Pinot Noir i Pinot Meunier, zbierane podczas wrześniowych corocznych żniw – co ważne – bez użycia 
        maszyn – tylko tradycyjnie ręcznie przez blisko tysiąc specjalnie do tego celu zatrudnionych osób.''')
        mummcr.write('''Kompozycja win z 77 winnic regionu Szampanii, z wykorzystaniem dużej proporcji win klasy 
        reserve i aż do 5 różnych roczników tworzących doskonałej jakości świeży, bogaty i kompleksowy szampan. 
        Świetnie komponuje się z daniami z owoców morza, grillowaną rybą i pieczonym mięsem. ''')
        mummcr.image("Wineimages/szampan/mummcr.jpg")
        mummcr.caption("Źródło: propaganda24h.pl")

        mummice = st.expander("Mumm ice extra")
        mummice.write('''Ten szampan ma przygotowaną formułę  gotową do zrównoważenia wszystkich kontrastów szampana w 
        kontakcie z lodem. Jego optymalna temperatura dla przyjemności wynosi około 6ºC. Nie tylko jest najlepszym 
        sprzymierzeńcem do serwowania z lodem, ale również doskonale komponuje się ze świeżymi składnikami, takimi jak 
        bazylia czy grejpfrut. Mumm Ice Xtra jest pełen kontrastów i egzotycznych aromatów, ponieważ wina rezerwowe, 
        które go tworzą, dojrzewają w beczkach z amerykańskiego dębu, które nadają mu waniliowego charakteru oraz 
        lekkich i subtelnych nut drzewnych. Ponadto charakter winogron Pinot Noir pozostaje w jego absolutnej 
        jędrności. Szampan jest pozyskiwany innowacyjną metodą leżakowania w beczkach po rumie.''')
        mummice.image("Wineimages/szampan/mummice.jpg")
        mummice.caption("Źródło: alkoholeswiata24.pl")

        cuvee = st.expander("Cuvee R. Lalou")
        cuvee.write('''Cuvee R. Lalou to wyjątkowy, rocznikowy szampan, będący wyrazem uznania dla wielkiego 
        wizjonera, Rene Lalou, który stał na czele Domu Szampańskiego G.H. Mumm od lat 30. XX wieku.<br> <br>
         Jego filozofia produkcji szampana opierała się na terroir, czyli miejscu pochodzenia winogron. Owoce używane 
         do produkcji Cuvee R. Lalou pochodzą tylko z najlepszych części winnic G.H. Mumm. Szampan Cuvee R. Lalou był 
         produkowany do 1985, jednak w 2007 roku Mistrz Piwnicy Didier Mariotti postanowił wskrzesić wielką legendę, 
         komponując wyjątkowe cuvee z roczników 1999 i 2002.''', unsafe_allow_html=True)
        cuvee.image("Wineimages/szampan/cuvee.jpg")
        cuvee.caption("Źródło: smaczajama.pl")

        perrier = st.expander("Perrier-Jouët")
        perrier.caption("Perrier-Jouët to obok Dom Pérignon najsłynniejszy szampan. Firmę założył w 1811 roku Pierre "
                        "Nicolas Marie Perrier. Nazwa szampana pochodzi od nazwiska panieńskiego żony Pierre’a. Od 1811 "
                        "roku szampan Perrier-Jouët stał się ulubionym trunkiem arystokracji i szlachty na całym "
                        "świecie. W 1902 roku mistrz form szklanych i czołowa postać stylu Art Nouveau - Émile Gallé "
                        "- stworzył niezwykły projekt butelki szampana Perrier-Jouët Belle Epoque. Florystyczny wzór "
                        "anemonów jest rozpoznawalny na całym świecie. O jakości szampanów Perrier-Jouët świadczy też "
                        "fakt, że te legendarne trunki do dzisiaj dostarczane są na dwory królewskie - między "
                        "innymi na dwór Monako.")
        perrier.write('''Stylowy, rocznikowy i wytrawny szampan o aromacie białych kwiatów i wyczuwalnej subtelnej 
        owocowo-imbirowej nucie. Komponuje się z owocami morza, doskonale uzupełniając lekko słony smak langusty, 
        pasuje do wykwintnych białych wędlin.
        Podawać w temperaturze 10-12 °C.<br>
        Szczepy: 50% chardonnay, 45% pinot noir, 5% pinot meunier''', unsafe_allow_html=True)
        perrier.image("Wineimages/szampan/perrier.jpg")
        perrier.caption("Źródło: smaczajama.pl, hurtowniaalkoholi.pl")


if __name__ == '__main__':
    main()
