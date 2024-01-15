import colorama as color
##R = E/I (ohmios = voltios divididos por amperios)

print(r"    // | |                                                          /__  ___/                           ")
print(r"   //__| |     __      ___   /          ( )   __      ___             / /   ___      ___     //  ___    ")
print(r"  / ___  |   //  ) ) //   ) / //   / / / / //   ) ) //   ) )         / /  //   ) ) //   ) ) // ((   ) ) ")
print(r" //    | |  //      //   / / //   / / / / //   / / //   / /         / /  //   / / //   / / //   \ \     ")
print(r"//     | | //      ((___/ / ((___( ( / / //   / / ((___/ /   _____ / /  ((___/ / ((___/ / // //   ) )")

print("")
print("")

print("[1] calculadora de resistencia (Ω)")

x = input(">")
if x=="1":
	V=input("Voltaje: ")
	A=input("Amperios: ")

	O=float(V)/float(A)

	print(f"{O}Ω")
