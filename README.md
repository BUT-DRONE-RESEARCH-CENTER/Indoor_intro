# Vstupní úkol DRC: Zpracování a vizualizace senzorických dat v ROS 2

English version can be seen [HERE](https://github.com/BUT-DRONE-RESEARCH-CENTER/Indoor_intro/blob/main/README_EN.md)
---

Vítej u vstupního úkolu pro nováčky do DRC! Cílem tohoto úkolu je ověřit (nebo tě naučit) základy práce s Robot Operating System (ROS 2), který je naprostým standardem v moderní robotice. Vyzkoušíš si práci s nahranými daty (rosbag), vytvoření vlastního skriptu (node) a vizualizaci. 

**Toto zadání včetně šablony kódu naleznete na** [GitHub - BUT-DRONE-RESEARCH-CENTER/Indoor_intro · GitHub](https://github.com/BUT-DRONE-RESEARCH-CENTER/Indoor_intro)

---

## 💻 Běžíš na Windows? Není problém!

Pokud nemáš na počítači nativní Linux (dual-boot), doporučujeme využít jednu z následujících variant:

1. **WSL 2 (Windows Subsystem for Linux)** – *Doporučeno pro výkon:*

   * Vylepšený terminál ve Windows umožňující běžet Ubuntu přímo.

   * Ve Windows 11 funguje grafika (GUI) v WSL2 automaticky (WSLg), takže v něm bez problému spustíš i RViz2. Stačí si v příkazové řádce Windows zapnout WSL (`wsl --install -d Ubuntu-22.04`) a do něj nainstalovat ROS 2.

   * **📁 Jak přenést soubory jako rosbag (data z dronu) nebo template skriptu do WSL?**  
     V terminálu WSL se přesuň do složky, kam chceš soubory uložit, a zadej příkaz:

     ```bash
     explorer.exe .
     ```

     *(Tečka na konci je důležitá!)* Příkaz otevře klasické okno Průzkumníka z Windows propojené s Linuxem. Stačí do něj stažený soubor nebo šablonu jednoduše přetáhnout myší.

2. **Virtuální stroj (VirtualBox / VMware)** – *Snadnější na nastavení:*

   * Stáhni si [VirtualBox](https://www.virtualbox.org/) a nainstaluj si v něm **Ubuntu Desktop (22.04 LTS)**.
   * Nezapomeň virtuálce přidělit dostatek RAM (ideálně 4–8 GB), alespoň 2–4 jádra CPU a **zapnout 3D akceleraci** v nastavení grafiky, aby běžel RViz2 plynule.

---

## 🛠️ Co budeš potřebovat

* **Nainstalovaný ROS 2** (např. Humble, Iron nebo Jazzy) na Linuxu (Ubuntu 22.04 / 24.04).
* **RViz2** – vizualizační nástroj (součást balíčku `ros-<distro>-desktop`).
* Znalost základů Pythonu.
* Základní orientace v Linux terminálu.

---

## 📝 Zadání úkolu

## 0. Připrav si Python environment a ROS2

Prvně musíš zprovoznit základní Environment pro správně fungování Pythonu na PC. Python může běžet bez environmentu, ale zahltí (udělá tzv. polution) celkový systém a práce se tak stane neorganizovanou.

https://docs.python.org/3/library/venv.html

Dále musíš do tohoto environmentu přidat/nainstalovat balíčky pro ROS2 (v našem případě Humble verzi kompatibilní s Ubuntu 22.04).

https://docs.ros.org/en/humble/Installation.html

### 1. Získej dataset (Rosbag)

Stáhni si připravený dataset, který obsahuje reálná data z pohybu robota/dronu (např. GPS data, odometrie, VIO). 

* **[Vicon ROS2 Bag z DRC uložiště](https://drive.google.com/file/d/1MF6iFzuq9PJtDL8rNpbJOpXDj5JGx6_0/view?usp=sharing)** 
* *(Alternativa pro testování: Můžeš si stáhnout ukázkový VIO dataset z [EuRoC MAV Dataset](https://www.research-collection.ethz.ch/entities/researchdata/bcaf173e-5dac-484b-bc37-faf97a594f1f))

### 2. Extrakce dat do CSV (Napiš vlastní Node)

Tvým úkolem je doplnit šablonu v Pythonu (`node_template.py`), která se chová jako ROS 2 node.

#### 📋 Seznam úkolů (TODO) v kódu:

1. **Hlavička CSV:** Definuj a zapiš názvy sloupců v CSV souboru (`timestamp`, `x`, `y`, `z`).
2. **Subscriber:** Odkomentuj a nastav `self.create_subscription()` se správným typem zprávy a názvem topicu.
3. **Timer:** Vytvoř a nastav timer (`self.create_timer()`) na periodu `0.1` s (10 Hz) a propoj jej s `self.timer_callback`.
4. **Extrakce dat v timeru (`timer_callback`):** Extrahuj ze `self.latest_msg` časové razítko a souřadnice pozice X, Y, Z.
5. **Zápis do CSV:** Zapiš extrahované hodnoty jako nový řádek do CSV souboru pomocí `self.writer.writerow([...])`.

#### 🚀 Spuštění skriptu

Až budeš mít kód doplněný, nezapomeň si v terminálu nejprve načíst ROS 2 a skript spusť přímo přes Python:

```bash
source /opt/ros/<distro>/setup.bash
python3 node_template.py
```

⚠️ **Důležité: Načtení prostředí ROS 2 (Sourcing)**
Všimni si, že v každém **nově otevřeném terminálu** musíš nejprve načíst prostředí ROS 2. Bez toho ti systém nebude rozumět příkazům jako `ros2` nebo `rviz2` a Python nenajde knihovnu `rclpy`.

Příkaz spustíš podle nainstalované verze (nahraď `<distro>` např. za `humble`):

```bash
source /opt/ros/<distro>/setup.bash
```

*(Tip: Pokud nechceš tento příkaz psát do každého nového okna terminálu, přidej si ho na konec souboru `~/.bashrc`.)*

---

### 3. Vizualizace v RViz2

Zatímco tvůj skript poběží na pozadí, chceme trajektorii vidět i vizuálně:

1. V prvním terminálu namiř do složky s datasetem, načti ROS a spusť přehrávání bagu:  
   `source /opt/ros/<distro>/setup.bash`  
   `ros2 bag play <jmeno_slozky_s_bagem>`
2. V druhém terminálu opět načti ROS a zapni vizualizační nástroj RViz2:  
   `source /opt/ros/<distro>/setup.bash`  
   `rviz2`
3. V RVizu si nastav správný **Fixed Frame** (zpravidla `map` nebo `odom`, zjistíš z dat).
4. Přidej si zobrazení trajektorie kliknutím na **Add** (vlevo dole) -> vyber typ zobrazení podle topicu (např. **Odometry** nebo **Path**).
5. Správně nastav název topicu, aby RViz data viděl. Zobrazí se ti křivka nebo šipky ukazující, kudy robot projel.

### 4. Co odevzdat

Až to budeš mít hotové, pošli nám:

1. **Zdrojový kód** tvého skriptu (node), který data ukládal.
2. **Vygenerovaný `.csv` soubor** s nasbíranými daty.
3. **Screenshot nebo krátké video** z RVizu, kde je jasně vidět vykreslená trajektorie robota.
4. **Screenshot informací ohledně datasetu** - jak je velký, jaký publikuje topics.

Neboj se googlit a používat oficiální ROS 2 dokumentaci nebo fóra! Hodně štěstí a těšíme se na tvoje řešení.
