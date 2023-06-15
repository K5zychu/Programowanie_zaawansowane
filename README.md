 <h1><center>Dokumentacja aplikacji "Ekspres do kawy" wraz z testami jednostkowymi</center></h1>

  <h2>a. Struktura aplikacji</h2>
  <p>
    Plik <code>main.py</code> zawiera główną logikę aplikacji, w której wykorzystywany jest wzorzec projektowy Abstract Factory.
    Istnieją abstrakcyjne klasy produktów (<code>Coffee</code> i <code>CoffeeBeans</code>), które są implementowane przez konkretne klasy (<code>Espresso</code>, <code>Latte</code>, itd.) oraz abstrakcyjną fabrykę (<code>CoffeeMachineFactory</code>), która jest implementowana przez konkretne fabryki (<code>EspressoMachineFactory</code>, <code>LatteMachineFactory</code>, itd.).
    Klasa <code>CoffeeMachine</code> reprezentuje sam ekspres do kawy, umożliwiając wybór rodzaju kawy i wykonanie operacji parzenia.
    Testy jednostkowe są zaimplementowane w pliku <code>test_main.py</code> i sprawdzają różne aspekty działania aplikacji.
  </p>

  <h2>b. Scenariusze testów</h2>
  <ul>
    <li>Testy jednostkowe dla klas abstrakcyjnych produktów (<code>Coffee</code>, <code>CoffeeBeans</code>):</li>
    <ul>
      <li>Sprawdzenie, czy metody abstrakcyjne <code>brew()</code> i <code>grind()</code> są poprawnie zadeklarowane.</li>
      <li>Sprawdzenie, czy metoda <code>brew()</code> podnosi wyjątek <code>NotImplementedError</code> przy bezpośrednim wywołaniu na obiekcie klasy abstrakcyjnej.</li>
    </ul>
    <li>Testy jednostkowe dla konkretnych produktów (<code>Espresso</code>, <code>Latte</code>, <code>Cappuccino</code>, <code>Mocha</code>, <code>ArabicaBeans</code>, <code>RobustaBeans</code>, <code>ColombianBeans</code>):</li>
    <ul>
      <li>Sprawdzenie, czy metody <code>brew()</code> (dla kawy) i <code>grind()</code> (dla ziaren) działają poprawnie.</li>
      <li>Porównanie wyników parzenia różnych rodzajów kawy z oczekiwanymi wynikami.</li>
    </ul>
    <li>Testy jednostkowe dla konkretnej fabryki (<code>EspressoMachineFactory</code>, <code>LatteMachineFactory</code>, itd.):</li>
    <ul>
      <li>Sprawdzenie, czy metoda <code>create_coffee()</code> zwraca odpowiedni obiekt klasy kawy.</li>
      <li>Sprawdzenie, czy metoda <code>create_coffee_beans()</code> zwraca odpowiedni obiekt klasy ziaren.</li>
    </ul>
    <li>Testy jednostkowe dla klasy <code>CoffeeMachine</code>:</li>
    <ul>
      <li>Sprawdzenie, czy metoda <code>choose_factory()</code> poprawnie ustawia fabrykę na podstawie wyboru użytkownika.</li>
      <li>Sprawdzenie, czy metoda <code>make_coffee()</code> wykonuje operacje parzenia kawy przy poprawnie wybranej fabryce.</li>
      <li>Sprawdzenie, czy metoda <code>make_coffee()</code> wyświetla odpowiednie komunikaty w przypadku nieprawidłowego wyboru fabryki lub braku wyboru fabryki.</li>
    </ul>
  </ul>

<h2>c. Wykorzystane narzędzia i/lub biblioteki</h2>
<p>
  Podczas implementacji aplikacji "Ekspres do kawy" oraz pisania testów jednostkowych wykorzystano kilka narzędzi i bibliotek, które umożliwiły efektywne tworzenie i testowanie kodu. Oto niektóre z wykorzystanych narzędzi i bibliotek:
</p>
<ul>
  <li>Python: Język programowania użyty do napisania aplikacji i testów jednostkowych. Python jest popularnym językiem ze względu na jego czytelność, elastyczność i obszerną społeczność, co ułatwia rozwój oprogramowania.</li>
  <li>unittest: Biblioteka standardowa Pythona do implementacji testów jednostkowych. unittest zapewnia zestaw narzędzi i metod umożliwiających pisanie i wykonywanie testów jednostkowych. Jest to wszechstronna biblioteka, która umożliwia grupowanie testów, zarządzanie danymi testowymi oraz tworzenie asercji i sprawdzanie oczekiwanych rezultatów.</li>
</ul>
<p>
  Oprócz narzędzi i bibliotek wymienionych powyżej, aplikacja "Ekspres do kawy" została zaimplementowana w czystym Pythonie, korzystając z klas, dziedziczenia, metod abstrakcyjnych i innych konstrukcji języka, które umożliwiły zastosowanie wzorca projektowego Abstract Factory.
</p>
  <h2>d. Ewentualne problemy i ich rozwiązanie</h2>
  <p>
    - Problem: Nieprawidłowy wybór kawy przez użytkownika.
    Rozwiązanie: W metodzie <code>choose_factory()</code> klasy <code>CoffeeMachine</code> sprawdzane jest, czy wybór użytkownika odpowiada poprawnym opcjom. W przeciwnym przypadku, wyświetlany jest odpowiedni komunikat o nieprawidłowym wyborze.
  </p>
  <p>
    - Problem: Brak wyboru fabryki przed wykonaniem operacji parzenia.
    Rozwiązanie: W metodzie <code>make_coffee()</code> klasy <code>CoffeeMachine</code> sprawdzane jest, czy fabryka została wybrana. Jeśli nie, wyświetlany jest odpowiedni komunikat o konieczności wyboru fabryki przed parzeniem kawy.
  </p>
  <p>
    - Problem: Wywołanie metody abstrakcyjnej na obiekcie klasy abstrakcyjnej.
    Rozwiązanie: Metoda <code>brew()</code> w klasie abstrakcyjnej <code>Coffee</code> podnosi wyjątek <code>NotImplementedError</code> w celu zabezpieczenia przed bezpośrednim wywołaniem na obiekcie klasy abstrakcyjnej. Implementacje konkretnych rodzajów kawy muszą dostarczyć własne implementacje tej metody.
  </p>
