import random
def periodic_table_quiz():
    # Dictionary of elements with their symbols as keys and names as values
    

    elements = {
    "H": "Hydrogen (1) \n~~~~ Family: Nonmetal \n~~~~ Electron Configuration: 1s1",
    "He": "Helium (2) \n~~~~ Family: Noble Gas \n~~~~ Electron Configuration: 1s2",
    "Li": "Lithium (3) \n~~~~ Family: Alkali Metal \n~~~~ Electron Configuration: He 2s1",
    "Be": "Beryllium (4) \n~~~~ Family: Alkaline Earth Metal \n~~~~ Electron Configuration: 2s2",
    "B": "Boron (5) \n~~~~ Family: Metalloid \n~~~~ Electron Configuration: He 2s2 2p1",
    "C": "Carbon (6) \n~~~~ Family: Nonmetal \n~~~~ Electron Configuration: He 2s2 2p2",
    "N": "Nitrogen (7) \n~~~~ Family: Nonmetal \n~~~~ Electron Configuration: He 2s2 2p3",
    "O": "Oxygen (8) \n~~~~ Family: Nonmetal \n~~~~ Electron Configuration: He 2s2 2p4",
    "F": "Fluorine (9) \n~~~~ Family: Halogen \n~~~~ Electron Configuration: He 2s2 2p5",
    "Ne": "Neon (10) \n~~~~ Family: Noble Gas \n~~~~ Electron Configuration: He 2s2 2p6",
    "Na": "Sodium (11) \n~~~~ Family: Alkali Metal \n~~~~ Electron Configuration: Ne 3s1",
    "Mg": "Magnesium (12) \n~~~~ Family: Alkaline Earth Metal \n~~~~ Electron Configuration: Ne 3s2",
    "Al": "Aluminum (13) \n~~~~ Family: Post\n~~~~Transition Metal \n~~~~ Electron Configuration: Ne 3s2 3p1",
    "Si": "Silicon (14) \n~~~~ Family: Metalloid \n~~~~ Electron Configuration: Ne 3s2 3p2",
    "P": "Phosphorus (15) \n~~~~ Family: Nonmetal \n~~~~ Electron Configuration: Ne 3s2 3p3",
    "S": "Sulfur (16) \n~~~~ Family: Nonmetal \n~~~~ Electron Configuration: Ne 3s2 3p4",
    "Cl": "Chlorine (17) \n~~~~ Family: Halogen \n~~~~ Electron Configuration: Ne 3s2 3p5",
    "Ar": "Argon (18) \n~~~~ Family: Noble Gas \n~~~~ Electron Configuration: Ne 3s2 3p6",
    "K": "Potassium (19) \n~~~~ Family: Alkali Metal \n~~~~ Electron Configuration: Ar 4s1",
    "Ca": "Calcium (20) \n~~~~ Family: Alkaline Earth Metal \n~~~~ Electron Configuration: Ar 4s2",
    "Sc": "Scandium (21) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Ar 3d1 4s2",
    "Ti": "Titanium (22) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Ar 3d2 4s2",
    "V": "Vanadium (23) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Ar 3d3 4s2",
    "Cr": "Chromium (24) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Ar 3d5 4s1",
    "Mn": "Manganese (25) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Ar 3d5 4s2",
    "Fe": "Iron (26) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Ar 3d6 4s2",
    "Co": "Cobalt (27) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Ar 3d7 4s2",
    "Ni": "Nickel (28) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Ar 3d8 4s2",
    "Cu": "Copper (29) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Ar 3d10 4s1",
    "Zn": "Zinc (30) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Ar 3d10 4s2",
    "Ga": "Gallium (31) \n~~~~ Family: Post\n~~~~Transition Metal \n~~~~ Electron Configuration: Ar 3d10 4s2 4p1",
    "Ge": "Germanium (32) \n~~~~ Family: Metalloid \n~~~~ Electron Configuration: Ar 3d10 4s2 4p2",
    "As": "Arsenic (33) \n~~~~ Family: Metalloid \n~~~~ Electron Configuration: Ar 3d10 4s2 4p3",
    "Se": "Selenium (34) \n~~~~ Family: Nonmetal \n~~~~ Electron Configuration: Ar 3d10 4s2 4p4",
    "Br": "Bromine (35) \n~~~~ Family: Halogen \n~~~~ Electron Configuration: Ar 3d10 4s2 4p5",
    "Kr": "Krypton (36) \n~~~~ Family: Noble Gas \n~~~~ Electron Configuration: Ar 3d10 4s2 4p6",
    "Rb": "Rubidium (37) \n~~~~ Family: Alkali Metal \n~~~~ Electron Configuration: Kr 5s1",
    "Sr": "Strontium (38) \n~~~~ Family: Alkaline Earth Metal \n~~~~ Electron Configuration: Kr 5s2",
    "Y": "Yttrium (39) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Kr 4d1 5s2",
    "Zr": "Zirconium (40) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Kr 4d2 5s2",
    "Nb": "Niobium (41) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Kr 4d4 5s1",
    "Mo": "Molybdenum (42) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Kr 4d5 5s1",
    "Tc": "Technetium (43) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Kr 4d5 5s2",
    "Ru": "Ruthenium (44) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Kr 4d7 5s1",
    "Rh": "Rhodium (45) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Kr 4d8 5s1",
    "Pd": "Palladium (46) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Kr 4d10",
    "Ag": "Silver (47) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Kr 4d10 5s1",
    "Cd": "Cadmium (48) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Kr 4d10 5s2", 
    "In": "Indium (49) \n~~~~ Family: Post-Transition Metal \n~~~~ Electron Configuration: Kr 4d10 5s2 5p1",
    "Sn": "Tin (50) \n~~~~ Family: Post\n~~~~Transition Metal \n~~~~ Electron Configuration: Kr 4d10 5s2 5p2",
    "Sb": "Antimony (51) \n~~~~ Family: Metalloid \n~~~~ Electron Configuration: Kr 4d10 5s2 5p3",
    "Te": "Tellurium (52) \n~~~~ Family: Metalloid \n~~~~ Electron Configuration: Kr 4d10 5s2 5p4",
    "I": "Iodine (53) \n~~~~ Family: Halogen \n~~~~ Electron Configuration: Kr 4d10 5s2 5p5",
    "Xe": "Xenon (54) \n~~~~ Family: Noble Gas \n~~~~ Electron Configuration: Kr 4d10 5s2 5p6",
    "Cs": "Cesium (55) \n~~~~ Family: Alkali Metal \n~~~~ Electron Configuration: Xe 6s1",
    "Ba": "Barium (56) \n~~~~ Family: Alkaline Earth Metal \n~~~~ Electron Configuration: Xe 6s2",
    "La": "Lanthanum (57) \n~~~~ Family: Lanthanide \n~~~~ Electron Configuration: Xe 5d1 6s2",
    "Ce": "Cerium (58) \n~~~~ Family: Lanthanide \n~~~~ Electron Configuration: Xe 4f1 5d1 6s2",
    "Pr": "Praseodymium (59) \n~~~~ Family: Lanthanide \n~~~~ Electron Configuration: Xe 4f3 6s2",
    "Nd": "Neodymium (60) \n~~~~ Family: Lanthanide \n~~~~ Electron Configuration: Xe 4f4 6s2",
    "Pm": "Promethium (61) \n~~~~ Family: Lanthanide \n~~~~ Electron Configuration: Xe 4f5 6s2",
    "Sm": "Samarium (62) \n~~~~ Family: Lanthanide \n~~~~ Electron Configuration: Xe 4f6 6s2",
    "Eu": "Europium (63) \n~~~~ Family: Lanthanide \n~~~~ Electron Configuration: Xe 4f7 6s2",
    "Gd": "Gadolinium (64) \n~~~~ Family: Lanthanide \n~~~~ Electron Configuration: Xe 4f7 5d1 6s2",
    "Tb": "Terbium (65) \n~~~~ Family: Lanthanide \n~~~~ Electron Configuration: Xe 4f9 6s2",
    "Dy": "Dysprosium (66) \n~~~~ Family: Lanthanide \n~~~~ Electron Configuration: Xe 4f10 6s2",
    "Ho": "Holmium (67) \n~~~~ Family: Lanthanide \n~~~~ Electron Configuration: Xe 4f11 6s2",
    "Er": "Erbium (68) \n~~~~ Family: Lanthanide \n~~~~ Electron Configuration: Xe 4f12 6s2",
    "Tm": "Thulium (69) \n~~~~ Family: Lanthanide \n~~~~ Electron Configuration: Xe 4f13 6s2",
    "Yb": "Ytterbium (70) \n~~~~ Family: Lanthanide \n~~~~ Electron Configuration: Xe 4f14 6s2",
    "Lu": "Lutetium (71) \n~~~~ Family: Lanthanide \n~~~~ Electron Configuration: Xe 4f14 5d1 6s2",
    "Hf": "Hafnium (72) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Xe 4f14 5d2 6s2",
    "Ta": "Tantalum (73) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Xe 4f14 5d3 6s2",
    "W": "Tungsten (74) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Xe 4f14 5d4 6s2",
    "Re": "Rhenium (75) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Xe 4f14 5d5 6s2",
    "Os": "Osmium (76) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Xe 4f14 5d6 6s2",
    "Ir": "Iridium (77) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Xe 4f14 5d7 6s2",
    "Pt": "Platinum (78) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Xe 4f14 5d9 6s1",
    "Au": "Gold (79) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Xe 4f14 5d10 6s1",
    "Hg": "Mercury (80) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Xe 4f14 5d10 6s2",
    "Tl": "Thallium (81) \n~~~~ Family: Post\n~~~~Transition Metal \n~~~~ Electron Configuration: Xe 4f14 5d10 6s2 6p1",
    "Pb": "Lead (82) \n~~~~ Family: Post\n~~~~Transition Metal \n~~~~ Electron Configuration: Xe 4f14 5d10 6s2 6p2",
    "Bi": "Bismuth (83) \n~~~~ Family: Post\n~~~~Transition Metal \n~~~~ Electron Configuration: Xe 4f14 5d10 6s2 6p3",
    "Po": "Polonium (84) \n~~~~ Family: Metalloid \n~~~~ Electron Configuration: Xe 4f14 5d10 6s2 6p4",
    "At": "Astatine (85) \n~~~~ Family: Metalloid \n~~~~ Electron Configuration: Xe 4f14 5d10 6s2 6p5",
    "Rn": "Radon (86) \n~~~~ Family: Noble Gas \n~~~~ Electron Configuration: Xe 4f14 5d10 6s2 6p6",
    "Fr": "Francium (87) \n~~~~ Family: Alkali Metal \n~~~~ Electron Configuration: Rn 7s1",
    "Ra": "Radium (88) \n~~~~ Family: Alkaline Earth Metal \n~~~~ Electron Configuration: Rn 7s2",
    "Ac": "Actinium (89) \n~~~~ Family: Actinide \n~~~~ Electron Configuration: Rn 6d1 7s2",
    "Th": "Thorium (90) \n~~~~ Family: Actinide \n~~~~ Electron Configuration: Rn 6d2 7s2",
    "Pa": "Protactinium (91) \n~~~~ Family: Actinide \n~~~~ Electron Configuration: Rn 5f2 6d1 7s2",
    "U": "Uranium (92) \n~~~~ Family: Actinide \n~~~~ Electron Configuration: Rn 5f3 6d1 7s2",
    "Np": "Neptunium (93) \n~~~~ Family: Actinide \n~~~~ Electron Configuration: Rn 5f4 6d1 7s2",
    "Pu": "Plutonium (94) \n~~~~ Family: Actinide \n~~~~ Electron Configuration: Rn 5f6 7s2",
    "Am": "Americium (95) \n~~~~ Family: Actinide \n~~~~ Electron Configuration: Rn 5f7 7s2",
    "Cm": "Curium (96) \n~~~~ Family: Actinide \n~~~~ Electron Configuration: Rn 5f7 6d1 7s2",
    "Bk": "Berkelium (97) \n~~~~ Family: Actinide \n~~~~ Electron Configuration: Rn 5f9 7s2",
    "Cf": "Californium (98) \n~~~~ Family: Actinide \n~~~~ Electron Configuration: Rn 5f10 7s2",
    "Es": "Einsteinium (99) \n~~~~ Family: Actinide \n~~~~ Electron Configuration: Rn 5f11 7s2",
    "Fm": "Fermium (100) \n~~~~ Family: Actinide \n~~~~ Electron Configuration: Rn 5f12 7s2",
    "Md": "Mendelevium (101) \n~~~~ Family: Actinide \n~~~~ Electron Configuration: Rn 5f13 7s2",
    "No": "Nobelium (102) \n~~~~ Family: Actinide \n~~~~ Electron Configuration: Rn 5f14 7s2",
    "Lr": "Lawrencium (103) \n~~~~ Family: Actinide \n~~~~ Electron Configuration: Rn 5f14 7s2 7p1",
    "Rf": "Rutherfordium (104) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Rn 5f14 6d2 7s2",
    "Db": "Dubnium (105) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Rn 5f14 6d3 7s2",
    "Sg": "Seaborgium (106) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Rn 5f14 6", 
    "Bh": "Bohrium (107) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Rn 5f14 6d5 7s2", "Hs": "Hassium (108) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Rn 5f14 6d6 7s2", "Mt": "Meitnerium (109) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Rn 5f14 6d7 7s2", "Ds": "Darmstadtium (110) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Rn 5f14 6d9 7s1", "Rg": "Roentgenium (111) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Rn 5f14 6d10 7s1", "Cn": "Copernicium (112) \n~~~~ Family: Transition Metal \n~~~~ Electron Configuration: Rn 5f14 6d10 7s2", "Nh": "Nihonium (113) \n~~~~ Family: Post\n~~~~Transition Metal \n~~~~ Electron Configuration: Rn 5f14 6d10 7s2 7p1", "Fl": "Flerovium (114) \n~~~~ Family: Post\n~~~~Transition Metal \n~~~~ Electron Configuration: Rn 5f14 6d10 7s2 7p2", "Mc": "Moscovium (115) \n~~~~ Family: Post\n~~~~Transition Metal \n~~~~ Electron Configuration: Rn 5f14 6d10 7s2 7p3", "Lv": "Livermorium (116) \n~~~~ Family: Post\n~~~~Transition Metal \n~~~~ Electron Configuration: Rn 5f14 6d10 7s2 7p4", "Ts": "Tennessine (117) \n~~~~ Family: Halogen \n~~~~ Electron Configuration: Rn 5f14 6d10 7s2 7p5", "Og": "Oganesson (118) \n~~~~ Family: Noble Gas \n~~~~ Electron Configuration: Rn 5f14 6d10 7s2 7p6"
	
}



   

   
    name = input("Enter your name: ").strip()
    correct = 0
    wrong = 0
    asked = set()
    all_questions = list(elements.items())

    print("\nWelcome to the Periodic Table Quiz!")
    print("You will answer questions until you get 10 wrong answers.")
    print("\n")

    while wrong < 10:
        if len(asked) == len(all_questions):  # Reset if all questions have been asked
            print("\nYou've gone through all the elements. Repeating questions now.")
            asked.clear()

        while True:
            symbol, element_name = random.choice(all_questions)
            if symbol not in asked:
                asked.add(symbol)
                break

        answer = input(f" What is the symbol for this element '{element_name}'? ").strip().title()
        if answer == symbol:
            print("Correct!")
            correct += 1
        else:
            print(f"Wrong! The correct answer is {symbol}.")
            wrong += 1

        print(f"Correct: {correct}, Wrong: {wrong}/10")

    print(f"\nGame over! You answered {correct} questions correctly before getting 10 wrong.")


periodic_table_quiz()
