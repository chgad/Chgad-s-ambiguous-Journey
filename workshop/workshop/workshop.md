class: center, middle

# Coding Style, Dokumentation & Github

---

# Was machen wir heute

* Allgemeiner Coding Style
* Wie dokumentieren wir unsere Projekte
* Wie nutzen wir Github

---

# Coding Style - Warum?

Einheitlicher Code ist...
* besser lesbar
* einfacher wartbar
* weniger fehleranfällig

Genaue Ausführung eigentlich irrelevant, wichtig ist sich auf eine Art und Weise zu einigen

---

# Wo ist der Fehler?

```c++
if ( check_position( pos ) )
{ for ( auto p : p1_stones ) {
if ( ( pos.first+1==p.first && pos.second==p.second ) ||
 ( pos.first == p.first && pos.second-1 == p.second )
 || ( pos.first - 1 == p.first && pos.second == p.second )
 || ( pos.first == p.first && pos.second - 1 == p.second )){
stonePlaced = true;
}}
```
.small[Hint: es sind zwei Fehler im Code]

---

# Wo ist der Fehler?

```c++
if ( check_position( pos ) )
{
    for ( auto p : p1_stones )
    {
        if ( ( pos.first + 1 == p.first && pos.second     == p.second )
          || ( pos.first     == p.first && pos.second - 1 == p.second )
          || ( pos.first - 1 == p.first && pos.second     == p.second )
          || ( pos.first     == p.first && pos.second - 1 == p.second ) )
        {
            stonePlaced = true;
        }
    }
```

---

# Wo ist der Fehler?

```C
if ( check_position( pos ) )
{
    for ( auto p : p1_stones )
    {
        if ( ( pos.first + 1 == p.first && pos.second     == p.second )
          || ( pos.first     == p.first && pos.second - 1 == p.second )
          || ( pos.first - 1 == p.first && pos.second     == p.second )
    --->  || ( pos.first     == p.first && pos.second - 1 == p.second ) )
        {
            stonePlaced = true;
        }
    }
    <---
```

---


# Coding Style - Allgemeine Regeln I

* Lieber mehr Code schreiben, der besser lesbar und erweiterbar ist, als kurzen Code, "weil's geht".

```c++
return (id == 0) ? "FAIL" : (! ships[id - 1]->is_dead())
? "You hit a ship!" : "You sunk a ship!";
```

---

# Coding Style - Allgemeine Regeln I

```c++
switch ( id )
{
    case 0:
        return "FAIL";
    default:
        if ( ships[id - 1]->is_dead() )
        {
            return "You sunk a ship!";
        }
        else
        {
            return "You hit a ship!";
        }
}
```

---

# Coding Style - Lists

Alle Kommars richtig gesetzt?
```c++
Board::Board ( unsigned int x, unsigned int y, WINDOW* win )
    : dim ( x, y ), window ( win ), board ( dim.second ), vSpace ( 1 ),
posCursorStart ( 1, 1 ), posCursor ( posCursorStart )
{
}
```

---

# Coding Style - Lists

Ja, alles korrekt!
```c++
Board::Board ( unsigned int x, unsigned int y, WINDOW* win )
    : dim ( x, y )
    , window ( win )
    , board ( dim.second )
    , vSpace ( 1 )
    , posCursorStart ( 1, 1 )
    , posCursor ( posCursorStart )
{
}
```

---

# Coding Style - Kommentare

```
// Für einzeilige Kommentare,
// kann auch erweitert werden.

/* Für längere Kommentare innerhalb
einer Klasse/Funktion. */

/**
 * Zur Dokumentation einer Funktion/Klasse.
 */
```

---

# Coding Style - Allgemeine Regeln II

* Geringe Nutzung von `?:`
* `{}` auf neuer Zeile
* ... und bei **allen** if/else/for/while vorhanden
* Keine Tabs, sondern **4** Leerzeichen
* max **120** Zeichen auf einer Zeile, optimal **80**
* nur eine Variabel pro Deklaration ~~`int a,b;`~~
* `default` bei `switch` statement erforderlich

---

# Coding Style - Benennung


* Variabeln, Funktionen: `camelCase`
* Klassen: `UpperCamelCase`
* Dateien: **keine** Leerzeichen! `use_underscores.php`
* **english** please

---

# Coding Style - Allgemeine Regeln III

* Funktionen sollten nur eine Funktion implementieren
* ...und nicht länger als ~25 Zeilen sein.
* Jede Datei sollte eine Aufgabe haben (z.B. Implementation einer Klasse)
* Leerzeichen in Klammern erleichtern das Lesen

---

# Coding Style - Beispiel

```c++
// in file class_board.cpp
class Board
{
    bool move_local ( pair<int, int> pos ) const
    {
        if ( pos.first  < 1 || pos.first  > dim.first
          || pos.second < 1 || pos.second > dim.second )
        {
            return false;
        }
        else
        {
            int sepLength = (int)fieldSeparate.length();
            move( pos.second + bStartGlobal.second
                , bStartGlobal.first + pos.first * ( sepLength + 1 ) );
            return true;
        }
    }
};
```

---

# Coding Style - Misc

* Unix line ending & `/` slash in Dateipfaden
* Wenn Code umgeschrieben wird, kommentiere den alten nur aus
* Code sollte immer in einem guten Zustand verlassen werden -> keinen fehlerhaften Code zurücklassen, wenn Zeit knapp wird

---
class: middle, center

# Coding Style - Weitere Ideen

---

# Dokumentation

* Ebenfalls einheitlich innerhalb eines Projektes
* Kann Lesen des Codes nicht ersetzen, aber eleichtern
* Sollte auch für Außenstehende verständlich sein - OpenSource Gedanke

---

# Dokumentation - Beispiel I

```php
/**
 * @brief check if a postion is valid for a new ship.
 * That means: a) the pos is on the board
 *             b) the pos is free (there is no ship there)
 *             c) there is no ship within one tile
 * @param  pos  the pos to be checkesd (local coords)
 * @return bool if pos is valid
 */
bool check_position ( std::pair<int, int> pos ) const;
```

---

# Dokumentation - Allgemeines Format

```php
/**
 * @brief Kurze Beschreibung
 * Längere Beschreibung danach
 * @author
 * @date Letzte Änderung
 * (@licence)
 * @todo
 * @bug
 * Bei Funktionen:
 * @param Für jeden Paramter kurze Beschriebung
 * @return Beschreibung was die Funktion zurückgibt
 */
```
---

# Dokumentation - Allgemeine Regeln

* Dokumentation einer Datei:
    * Name der Datei
    * Funktion/Aufgabe
    * Projekt
    * Autoren
    * Datum
    * (Lizenz)

---

```c++
/**
 * This function always returns true
 */
bool has_user_won ()
{
    return false;
}
```

---

# Never trust comments!

```c++
/**
 * This function always returns true
 */
bool has_user_won ()
{
    return false;
}
```


---
# Dokumentation - Allgemeine Regeln II

* Jede Funktion/Methode/Klasse sollte dokumentiert werden
* nutze Kürzel z.B. `LG, BK` für Änderungen
* Kommentare im Code sollten kurz und nützlich sein, keine trivialen Dinge kommentieren
```php
    ...
    return 0; // returns 0
```

---
class: center, middle

# Dokumentation - weitere Ideen

---
class: middle, center

# Github

---

# Github - Ein Repository erstellen

```
$ git init              # erstelle ein lokales Repo in aktuellem Ordner
$ git clone <server>    # "checkout", klone ein Repo
$ ls -a
... .git ...
```

---

# Github - Workflow

.image_max_width[![Workflow](https://rogerdudler.github.io/git-guide/img/trees.png)]
```
$ git add FILES            # Füge Änderungen der "staging area" hinzu
$ git rm FILES             # Löscht die Dateien aus dem Repository
$ git commit -m "message"  # Änderungen sind nun im HEAD
$ git push                 # Erst jetzt werden Änderungen hochgeladen
```

---

# Github - Allgemeines

```
$ git status                     # Zeigt Dateien in der staging Area und
                                 # solche, die noch nicht ge*add*ed wurden
$ git config                     # Stelle Accountname und E-Mail ein
$ git remote add origin <server> # Ändere Ziel des push-Befehls zu <server>
```

---

# Github - Branches

.image_max_width[![Branches](https://rogerdudler.github.io/git-guide/img/branches.png)]

```
$ git checkout <branch>     # Wechsele zu branch <branch>
$ git checkout master       # Wechsele zurück zum master branch
$ git push origin <branch>  # Push zu Branch <branch>
$ git branch -d <branch>    # Lösche <branch> (auch über Website)
```

---

# Github - Update & Merge

```
$ git pull                          # Update lokales Repo
$ git merge <branch>                # Füge <branch> zu master hinzu
$ git diff <source_branch> <target> # Zeige Unterschiede an
$ git blame                         # Zeige an, wer was wann geändert hat
```

---

# Github - Allgemeine Regeln

* Initialien in commit messages
* Jedes Projekt sollte auf Github sein
* Änderung commiten und pushen

(Cheat sheet: https://rogerdudler.github.io/git-guide/)
---

# Linux on one slide

```
$ ls                    # -a alle Dateien, -l mehr Informationen
$ cd
$ nano  FILE
$ mkdir DIRECTORY
$ mv    SOURCE DEST
$ cp    SOURCE DEST     # -R kopiere Ordner
$ rm    FILE            # -r lösche Ordner
$ ssh   BENUTZER@HOST
  ~/                    # Homeordner
  .FILE                 # Versteckte Datei
  <TAB>                 # Autovervollständigung von Dateinamen und Commands
```

