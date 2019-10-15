# nama file: import.py

# mengimpor Hukum Newton 3
import HukumNewton3
def main():

    #gayagesek
    U = 10 # gesekan
    N = 8  # gaya normal

    gayagesek = HukumNewton3.gayagesek(U, N)

    print("HUKUM NEWTON 3")
    print("gesekan\t\t: ", U)
    print("gaya normal\t: ", N)
    print("hasil\t\t: ", gayagesek)

    #gayaberat
    M = 8 # massa benda
    G = 4  # gravitasi bumi

    gayaberat = HukumNewton3.gayaberat(M, G)

    print("HUKUM NEWTON 3")
    print("massa benda\t: ", M)
    print("gravitasi bumi\t: ", G)
    print("hasil\t\t: ", gayaberat)

    #beratsejenis
    W = 12 # berat benda
    V = 4 # volume benda

    beratsejenis = HukumNewton3.beratsejenis(W, V)

    print("HUKUM NEWTON 3")
    print("berat benda\t: ", W)
    print("volume benda\t: ", V)
    print("hasil\t\t: ", beratsejenis)

if __name__ == "__main__":
    main()
