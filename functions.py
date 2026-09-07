import sys

ERRORS = ["error", "couldn't", "cannot", "no such file", "failed", "fail", "fatal"]
WARNING = ["warning", "warn", "[!]"]

## Line count
def lineCount(FILE):
    with open(FILE, "r") as file:
        for indice, name in enumerate(file):
            total = indice + 1

        return total

## Error count
def errorCount(FILE):
    with open(FILE, "r") as file:
        count = 0
        for i in file:
            if any(error in i.lower() for error in ERRORS):
                count += 1

        return count

## Warning count
def warnCount(FILE):
    with open(FILE, "r") as file:
        count = 0
        for i in file:
            if any(warn in i.lower() for warn in WARNING):
                count += 1

        return count

## IP count
def ipCount(FILE):
    with open(FILE, "r") as file:
        count = 0
        for i in file:
            if "." in i:
                count += 1
        if count == 3:
            return count 
