import argparse,re,os

from colorama import Fore
from sub import subnet,interface


class Main:
    def __init__(self) -> None:
        parser = argparse.ArgumentParser(description="")
        parser.add_argument('choice',choices=["subnet","interface"])
        parser.add_argument('-i','--interface',help="for interface scan")
        parser.add_argument('-r','--range',help="for range scan")
        self.args = parser.parse_args()
        self.red = Fore.RED
        self.reset = Fore.RESET

    def scan(self):
        print(f"""{self.red}
        ╔═╗┬┌┬┐┌─┐┬  ┌─┐  ╔═╗┌─┐┌─┐┌┐┌┌┐┌┌─┐┬─┐
        ╚═╗││││├─┘│  ├┤   ╚═╗│  ├─┤││││││├┤ ├┬┘
        ╚═╝┴┴ ┴┴  ┴─┘└─┘  ╚═╝└─┘┴ ┴┘└┘┘└┘└─┘┴└─{self.reset}
                                --Angel-Caido--
        """)
        choice = self.args.choice
        ipRange = self.args.range
        interfaceName = self.args.interface

        if(choice == "interface" and (interface!=None or interface!="")):
            interface.InterfaceScanner(interfaceName).scan()
        elif(choice=="subnet" and (ipRange!=None or ipRange!="")):
            subnet.Scanner(ipRange).scan()
        else:
            print("ip range or interface required")

        



runner = Main()
try:
    runner.scan()
except PermissionError:
    print(f"{Fore.RED}[X] Root permission Required !!{Fore.RESET}")
