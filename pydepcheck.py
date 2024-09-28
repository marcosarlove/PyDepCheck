#! /usr/bin/python3

import argparse
import subprocess
import sys
import ast
import json
from os.path import exists

MATCH_FILE = "matches.json"

def listAllDepends(file):
    with open(file, "r") as f:
        tree = ast.parse(f.read(), filename=file)

    depends = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                depends.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            depends.add(node.module)

    return clearDepends(depends)


def clearDepends(depends):

    parsed = set()

    for dep in depends:
        index = dep.find(".")
        if index == -1: parsed.add(dep)
        else: parsed.add(dep[:dep.find(".")])

    return list(parsed)


def replaceDepends(depends):

    global MATCH_FILE
    try:
        with open(MATCH_FILE) as fp:
            text = json.loads(fp.read())
    except FileNotFoundError: return depends
    else:
        matches = []
        for i in depends: matches.append(text.get(i, i))
        return matches

def checkDepends(depends):

    notInstalled = []
    for dep in depends:
        try: __import__(dep)
        except ImportError: notInstalled.append(dep)
    return notInstalled



def installDepends(depends, autoInstall = False):

    depends = replaceDepends(depends)
    for dep in depends:
        if not autoInstall:
            answer = input(f"Do you want to install \033[32m{dep}\033[0m package? (y/n): ")
            if answer.lower() == 'y': installDepend(dep)
        else: installDepend(dep)

def installDepend(depend):
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", depend])

    except subprocess.CalledProcessError:
        print(f"Failed to install {depend} dependency")

def commandLineArguments():

    parser = argparse.ArgumentParser(description='PyDepCheck - Analyzes and installs Python script dependencies.')
    parser.add_argument('script', help='Path of the Python script to be parsed.')
    parser.add_argument('-i', '--install', action='store_true', help='Automatically installs any uninstalled dependencies.')

    return parser.parse_args()



def main(args):


    if not exists(MATCH_FILE):
        print(f"\033[31mCorrespondence file {MATCH_FILE} not found. The program will not work correctly.\033[0m")
    depends = listAllDepends(args.script)
    print("Dependencies Found: \033[32m", ", ".join(depends), "\033[0m")
    notInstalled = checkDepends(depends)
    print("Dependencies not installed: \033[32m", ", ".join(notInstalled), "\033[0m")

    if notInstalled:
        print("The following dependencies must be installed: \033[33m", ", ".join(replaceDepends(notInstalled)), "\033[0m")
        autoInstall = True if args.install else False
        installDepends(notInstalled, autoInstall)
    else:
        print("\033[32mAll dependencies are already installed.\033[0m")


if __name__ == "__main__":
    args = commandLineArguments()
    main(args)
