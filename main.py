import numpy as np
def main():
    print("Hallo World")
    
    with open("sumfile.txt", "w") as f:
        f.write("Das ist ein Test")
    print(np.abs(-3.5))

if __name__ == "__main__":
    main()