from generator import generate

try:
    count = int(input("ENTER NUMBER OF GENERATIONS\n"))
    chain = str(input("ENTER SOL, EVM, APTOS or BTC depending on which wallets you need\n")).upper()
    if chain == "BTC":
        bip = str(input("ENTER BIP44 or BIP49 or BIP84 GENERATION STANDARD\n")).upper()
        generate(count=count, chain = chain, bip = bip)
    else:
        generate(count=count, chain = chain)
except:
    generate()
