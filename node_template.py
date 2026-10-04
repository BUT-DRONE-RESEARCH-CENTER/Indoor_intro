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
        # Čekáme, dokud neúspěšně nepřejde první zpráva
        if self.latest_msg is None:
            return

        # TODO: Extrahuj potřebné hodnoty ze self.latest_msg (např. časové razítko a pozice X, Y, Z)
        # timestamp = ...
        # x = ...
        # y = ...
        # z = ...

        # TODO: Zapiš získáne údaje do CSV souboru pomocí self.writer.writerow([...])
        
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