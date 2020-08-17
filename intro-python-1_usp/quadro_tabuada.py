if __name__ == "__main__":
    pass

linha = 1
coluna = 1

print("-X-\t[1]\t[2]\t[3]\t[4]\t[5]\t[6]\t[7]\t[8]\t[9]\t[10]")
print()
while linha <= 10:
    print(f"[{linha}]", end="\t")
    while coluna <= 10:
        print(linha * coluna, end="\t")
        coluna += 1
    print("\n")
    linha += 1
    coluna = 1
