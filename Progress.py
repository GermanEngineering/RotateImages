import math

def PrintProgress(numberOfProcessedFiles):
    if numberOfProcessedFiles == 1:
        print("""
       OO          OO
      OOOO        OOOO
      OOO         OOO
     O              OO
    O                 O
   O    OO       OO    O
  O    OOO      OOO    OO OO
  OO    O        O     OOO  O
 OOOO                 OOOOO   O
OOOOOO      O      OOOOOOOO    O
 OOOOOOOOO       OOOOOOOOOO     O
   OOOOOOOOO   OOOOOOOOOOOO      O
      OOOOOOOOOOOOOOOOOOOOO       O
               OOOOOOOOO           O
             OOOOOOOOOO      OOO    O
           OOOOOOOOOO      OOOOOOO   O
          OOOOOOO         OOOOOOOOO OO
                          OOOOOOOOO O
                    OOOOOOOOOOOOOOO
                     OOOOOOOOOOOOO""")

    progress = numberOfProcessedFiles - (math.floor(numberOfProcessedFiles/13) * 13)
    print("{0}{1} Processed Files: {2}".format(progress * "\|/", (39 - 3 * progress) * " ", numberOfProcessedFiles), end="\r")
