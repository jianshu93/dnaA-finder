from oriFinder import findOri

def main():
    with open("Project-1/salmonella.txt", "r") as fin:
        #read the genome
        genome = fin.read().strip()
        #get origin of replication
        oriPos = findOri(genome)
        print(oriPos)
        #find frequent approx 9mers with upto 2 mismatches
        #window 1 -> 500 bp ending at oriPos
        for p in oriPos:
            ori = genome[p-499:p+1]
        #window 2 -> 500 bp starting at oriPos
        #window 3 -> 500 bp centered at oriPos

if __name__ == "__main__":
    main()
