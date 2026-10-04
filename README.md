# Vstupní úkol DRC: Zpracování a vizualizace senzorických dat v ROS 2

Vítej u vstupního úkolu pro nováčky do DRC! Cílem tohoto úkolu je ověřit (nebo tě naučit) základy práce s Robot Operating System (ROS 2), který je naprostým standardem v moderní robotice. Vyzkoušíš si práci s nahranými daty (rosbag), vytvoření vlastního skriptu (node) a vizualizaci. Celé

---

## 🛠️ Co budeš potřebovat

* **Nainstalovaný ROS 2** (např. Humble, Iron nebo Jazzy) na Linuxu (Ubuntu 22.04 / 24.04).
* **RViz2** – vizualizační nástroj (součást balíčku `ros-<distro>-desktop`).
* Znalost základů Pythonu.
* Základní orientace v Linux terminálu.

---

## ⚠️ Důležité: Načtení prostředí ROS 2 (Sourcing)

Všimni si, že v každém **nově otevřeném terminálu** musíš nejprve načíst prostředí ROS 2. Bez toho ti systém nebude rozumět příkazům jako `ros2` nebo `rviz2` a Python nenajde knihovnu `rclpy`.

Příkaz spustíš podle nainstalované verze (nahraď `<distro>` např. za `humble`):

```bash
source /opt/ros/<distro>/setup.bash
```

*(Tip: Pokud nechceš tento příkaz psát do každého nového okna terminálu, přidej si ho na konec souboru `~/.bashrc`.)*

---

## 💻 Běžíš na Windows? Není problém!

Pokud nemáš na počítači nativní Linux (dual-boot), doporučujeme využít jednu z následujících variant:

1. **WSL 2 (Windows Subsystem for Linux)** – *Doporučeno pro výkon:*
   
   * Vylepšený terminál ve Windows umožňující běžet Ubuntu přímo.
   
   * Ve Windows 11 funguje grafika (GUI) v WSL2 automaticky (WSLg), takže v něm bez problému spustíš i RViz2. Stačí si v příkazové řádce Windows zapnout WSL (`wsl --install -d Ubuntu-22.04`) a do něj nainstalovat ROS 2.
   
   * **📁 Jak přenést soubory (rosbag, skript) do WSL?**  
     V terminálu WSL se přesuň do složky, kam chceš soubory uložit, a zadej příkaz:
     
     ```bash
     explorer.exe .
     ```
     
     *(Tečka na konci je důležitá!)* Příkaz otevře klasické okno Průzkumníka z Windows propojené s Linuxem. Stačí do něj stažený soubor nebo šablonu jednoduše přetáhnout myší.

2. **Virtuální stroj (VirtualBox / VMware)** – *Snadnější na nastavení:*
   
   * Stáhni si [VirtualBox](https://www.virtualbox.org/) a nainstaluj si v něm **Ubuntu Desktop (22.04 LTS)**.
   * Nezapomeň virtuálce přidělit dostatek RAM (ideálně 4–8 GB), alespoň 2–4 jádra CPU a **zapnout 3D akceleraci** v nastavení grafiky, aby běžel RViz2 plynule.

---

## 📝 Zadání úkolu

### 1. Získej dataset (Rosbag)

Stáhni si připravený dataset, který obsahuje reálná data z pohybu robota/dronu (např. GPS data, odometrie, VIO). 

* 🔗 **[ZDE BUDE ODKAZ NA VÁŠ DRB/ROSBAG]** 
* *(Alternativa pro testování: Můžeš si stáhnout ukázkový VIO dataset z [EuRoC MAV Dataset](https://projects.asl.ethz.ch/datasets/doku.php?id=kmavvisualinertialdatasets))*

### 2. Extrakce dat do CSV (Napiš vlastní Node)

Tvým úkolem je doplnit šablonu v Pythonu (`pose_logger_template.py`), která se chová jako ROS 2 node.

#### 📋 Seznam úkolů (TODO) v kódu:

1. **Import zpráv:** Importuj správný typ zprávy podle topicu v datasetu (např. `PoseStamped` nebo `Odometry`).
2. **Hlavička CSV:** Definuj názvy sloupců v CSV souboru (`timestamp`, `x`, `y`, `z`).
3. **Subscriber:** Odkomentuj a nastav `self.create_subscription()` se správným typem zprávy a názvem topicu.
4. **Timer:** Odkomentuj a nastav `self.create_timer()` na periodu `0.1` s (10 Hz).
5. **Callback subscriberu (`pose_callback`):** Ukládej přijatou zprávu do proměnné `self.latest_msg`.
6. **Callback timeru (`timer_callback`):** Extrahuj ze zprávy časové razítko a pozice X, Y, Z.
7. **Zápis do CSV:** Zapiš extrahované hodnoty jako nový řádek do CSV souboru.

#### 🚀 Spuštění skriptu

Až budeš mít kód doplněný, nezapomeň si v terminálu nejprve načíst ROS 2 a skript spusť přímo přes Python:

```bash
source /opt/ros/<distro>/setup.bash
python3 pose_logger_template.py
```

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

Neboj se googlit a používat oficiální ROS 2 dokumentaci nebo fóra! Hodně štěstí a těšíme se na tvoje řešení.

---

## 🐍 Šablona kódového skriptu (`pose_logger_template.py`)

Kód si ulož do souboru `pose_logger_template.py` a doplň místa označená jako `# TODO:`.

```python
#!/usr/bin/env python3

import csv
import rclpy
from rclpy.node import Node

# TODO: Importuj správný typ zprávy podle topicu v datasetu
# Příklady:
# from geometry_msgs.msg import PoseStamped
# from nav_msgs.msg import Odometry


class PoseCsvLogger(Node):
    def __init__(self):
        super().__init__('pose_csv_logger')

        # 1. Příprava CSV souboru
        self.filename = 'robot_trajectory.csv'
        self.csv_file = open(self.filename, mode='w', newline='')
        self.writer = csv.writer(self.csv_file)

        # TODO: Napiš hlavičku CSV podle toho, jaké hodnoty hodláš ukládat
        self.writer.writerow(['timestamp', 'x', 'y', 'z'])

        # Proměnná pro ukládání nejnovější přijaté zprávy
        self.latest_msg = None

        # 2. Vytvoření Subscriberu
        # TODO: Odkomentuj a doplň typ zprávy a správný název topicu z rosbagu
        # self.subscription = self.create_subscription(
        #     TYP_ZPRAVY,
        #     '/NAZEV_TOPICU',
        #     self.pose_callback,
        #     10
        # )

        # 3. Vytvoření Timeru pro uložení dat přesně na 10 Hz (perioda 0.1 s)
        # TODO: Odkomentuj timer a nastav callback
        # timer_period = 0.1  # sekundy
        # self.timer = self.create_timer(timer_period, self.timer_callback)

        self.get_logger().info("Node 'pose_csv_logger' byl spuštěn a čeká na data...")

    def pose_callback(self, msg):
        """ Volá se automaticky při přijetí nové zprávy z topicu """
        # TODO: Ulož si přijatou zprávu do proměnné self.latest_msg
        pass

    def timer_callback(self):
        """ Volá se pravidelně 10x za sekundu (10 Hz) """
        # Čekáme, dokud úspěšně nepřijde první zpráva
        if self.latest_msg is None:
            return

        # TODO: Extrahuj potřebné hodnoty ze self.latest_msg (např. časové razítko a pozice X, Y, Z)
        # timestamp = ...
        # x = ...
        # y = ...
        # z = ...

        # TODO: Zapiš získané údaje do CSV souboru pomocí self.writer.writerow([...])

        # Zajištění okamžitého zápisu na disk
        self.csv_file.flush()

    def destroy_node(self):
        """ Korektní uzavření souboru při ukončení nodu (Ctrl+C) """
        if hasattr(self, 'csv_file') and not self.csv_file.closed:
            self.csv_file.close()
            self.get_logger().info(f"Data byla úspěšně uložena do {self.filename}")
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = PoseCsvLogger()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
```