# Naam: Stijn Bruggink
# Datum: 15-11-2018
# Versie: 1

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.

# seqs is een lijst met afzonderlijke seqences


def main():
    """Calles to functions.

    Creates variables and gives a value to them trough the lees_inhoud function.
    A user input then accept a user given word to look for all sequences, with the seachword in the header,
    to check if the sequence is DNA and if it is check to see whether enzymes cut in the sequence, both done
    with the functions is_dna and knipt.
    """
    bestand = "alpaca_bestand.fna"
    headers, seqs = lees_inhoud(bestand)
    zoekwoord = input("Geef een zoekwoord op: ")
    for i in range(len(headers)):
        if zoekwoord in headers[i]:
            print("Header:", headers[i])
            check_is_dna = is_dna(seqs[i])
            if check_is_dna:
                print("Sequentie is DNA")
                knipt(seqs[i])
            else:
                print("Sequentie is geen DNA. Er is iets fout gegaan.")


def lees_inhoud(bestands_naam):
    """"Puts file data in lists.

    It opens the file and reads each line seperately to remover commas and enters from said line
    and it will then put the sequence lines in a temporary variable till it hit the next header,
    at that point the temporaty variable is written to the sequence list.
    """
    try:
        bestand = open(bestands_naam)
        headers = []
        seqs = []
        seq = ""
        for line in bestand:
            line = line.strip()
            if ">" in line:
                if seq != "":
                    seqs.append(seq)
                    seq = ""
                    headers.append(line)
            else:
                seq += line.strip()
                seqs.append(seq)

    except FileNotFoundError:
        print('no such file or directory found')
    return headers, seqs

    
def is_dna(seq):
    """"Checks whether the sequence is DNA.

    Creates variable dna at False value and then counts the amount of atcg in the sequence,
    if the sum of all the atcg is equal to the length of the sequence local variable dna will
    adjusted to True, then dna is returned.
    """
    dna = False
    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")
    total = a+t+c+g
    if total == len(seq):
        dna = True
    return dna


def knipt(alpaca_seq):
    """"Looks whether the selected enzymes cut in the sequence.

    It opens the file enzymen.txt and for each line in the file it plits the line in the
    enzym name and enzym effective sequence area and the for the currenly selected enzym
    check whether it cuts in the sequence, and if it does it prints it. If the snipping
    enzym check is done it moves to the next one.
    """
    try:
        bestand = open("enzymen.txt")
        for line in bestand:
            naam, seq = line.split(" ")
            seq = seq.strip().replace("^", "")
            if seq in alpaca_seq:
                print(naam, "knipt in sequentie")
    except FileNotFoundError:
        print('could not open the enzymen.txt file.')


main()
