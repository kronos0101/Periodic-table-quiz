import os
from win32com.client import Dispatch

# Full list of elements with their families, symbols, names, and electron configurations
elements_with_details = [
    ("Nonmetals", "H", "Hydrogen", 1, "1s1"),
    ("Noble Gases", "He", "Helium", 2, "1s2"),
    ("Alkali Metals", "Li", "Lithium", 3, "1s2 2s1"),
    ("Alkaline Earth Metals", "Be", "Beryllium", 4, "1s2 2s2"),
    ("Boron Group", "B", "Boron", 5, "1s2 2s2 2p1"),
    ("Nonmetals", "C", "Carbon", 6, "1s2 2s2 2p2"),
    ("Nonmetals", "N", "Nitrogen", 7, "1s2 2s2 2p3"),
    ("Nonmetals", "O", "Oxygen", 8, "1s2 2s2 2p4"),
    ("Halogens", "F", "Fluorine", 9, "1s2 2s2 2p5"),
    ("Noble Gases", "Ne", "Neon", 10, "1s2 2s2 2p6"),
    ("Alkali Metals", "Na", "Sodium", 11, "1s2 2s2 2p6 3s1"),
    ("Alkaline Earth Metals", "Mg", "Magnesium", 12, "1s2 2s2 2p6 3s2"),
    ("Boron Group", "Al", "Aluminum", 13, "1s2 2s2 2p6 3s2 3p1"),
    ("Metalloids", "Si", "Silicon", 14, "1s2 2s2 2p6 3s2 3p2"),
    ("Nonmetals", "P", "Phosphorus", 15, "1s2 2s2 2p6 3s2 3p3"),
    ("Nonmetals", "S", "Sulfur", 16, "1s2 2s2 2p6 3s2 3p4"),
    ("Halogens", "Cl", "Chlorine", 17, "1s2 2s2 2p6 3s2 3p5"),
    ("Noble Gases", "Ar", "Argon", 18, "1s2 2s2 2p6 3s2 3p6"),
    ("Alkali Metals", "K", "Potassium", 19, "1s2 2s2 2p6 3s2 3p6 4s1"),
    ("Alkaline Earth Metals", "Ca", "Calcium", 20, "1s2 2s2 2p6 3s2 3p6 4s2"),
    ("Transition Metals", "Sc", "Scandium", 21, "1s2 2s2 2p6 3s2 3p6 4s2 3d1"),
    ("Transition Metals", "Ti", "Titanium", 22, "1s2 2s2 2p6 3s2 3p6 4s2 3d2"),
    ("Transition Metals", "V", "Vanadium", 23, "1s2 2s2 2p6 3s2 3p6 4s2 3d3"),
    ("Transition Metals", "Cr", "Chromium", 24, "1s2 2s2 2p6 3s2 3p6 4s1 3d5"),
    ("Transition Metals", "Mn", "Manganese", 25, "1s2 2s2 2p6 3s2 3p6 4s2 3d5"),
    ("Transition Metals", "Fe", "Iron", 26, "1s2 2s2 2p6 3s2 3p6 4s2 3d6"),
    ("Transition Metals", "Co", "Cobalt", 27, "1s2 2s2 2p6 3s2 3p6 4s2 3d7"),
    ("Transition Metals", "Ni", "Nickel", 28, "1s2 2s2 2p6 3s2 3p6 4s2 3d8"),
    ("Transition Metals", "Cu", "Copper", 29, "1s2 2s2 2p6 3s2 3p6 4s2 3d10"),
    ("Transition Metals", "Zn", "Zinc", 30, "1s2 2s2 2p6 3s2 3p6 4s2 3d10"),
    ("Boron Group", "Ga", "Gallium", 31, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p1"),
    ("Metalloids", "Ge", "Germanium", 32, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p2"),
    ("Metalloids", "As", "Arsenic", 33, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p3"),
    ("Nonmetals", "Se", "Selenium", 34, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p4"),
    ("Halogens", "Br", "Bromine", 35, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p5"),
    ("Noble Gases", "Kr", "Krypton", 36, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6"),
    ("Alkali Metals", "Rb", "Rubidium", 37, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1"),
    ("Alkaline Earth Metals", "Sr", "Strontium", 38, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2"),
    ("Transition Metals", "Y", "Yttrium", 39, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1"),
    ("Transition Metals", "Zr", "Zirconium", 40, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d2"),
    ("Transition Metals", "Nb", "Niobium", 41, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d4"),
    ("Transition Metals", "Mo", "Molybdenum", 42, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d5"),
    ("Transition Metals", "Tc", "Technetium", 43, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d5"),
    ("Transition Metals", "Ru", "Ruthenium", 44, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d7"),
    ("Transition Metals", "Rh", "Rhodium", 45, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d8"),
    ("Transition Metals", "Pd", "Palladium", 46, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s0 4d10"),
    ("Transition Metals", "Ag", "Silver", 47, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d10"),
    ("Transition Metals", "Cd", "Cadmium", 48, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10"),
    ("Transition Metals", "In", "Indium", 49, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p1"),
    ("Transition Metals", "Sn", "Tin", 50, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p2"),
    ("Transition Metals", "Sb", "Antimony", 51, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p3"),
    ("Transition Metals", "Te", "Tellurium", 52, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p4"),
    ("Halogens", "I", "Iodine", 53, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p5"),
    ("Noble Gases", "Xe", "Xenon", 54, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6"),
    ("Alkali Metals", "Cs", "Cesium", 55, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1"),
    ("Alkaline Earth Metals", "Ba", "Barium", 56, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2"),
    ("Lanthanides", "La", "Lanthanum", 57, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2"),
    ("Lanthanides", "Ce", "Cerium", 58, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f1 6s2"),
    ("Lanthanides", "Pr", "Praseodymium", 59, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f3 6s2"),
    ("Lanthanides", "Nd", "Neodymium", 60, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f4 6s2"),
    ("Lanthanides", "Pm", "Promethium", 61, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f5 6s2"),
    ("Lanthanides", "Sm", "Samarium", 62, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f6 6s2"),
    ("Lanthanides", "Eu", "Europium", 63, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f7 6s2"),
    ("Lanthanides", "Gd", "Gadolinium", 64, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f7 5d1 6s2"),
    ("Lanthanides", "Tb", "Terbium", 65, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f9 6s2"),
    ("Lanthanides", "Dy", "Dysprosium", 66, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f10 6s2"),
    ("Lanthanides", "Ho", "Holmium", 67, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f11 6s2"),
    ("Lanthanides", "Er", "Erbium", 68, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f12 6s2"),
    ("Lanthanides", "Tm", "Thulium", 69, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f13 6s2"),
    ("Lanthanides", "Yb", "Ytterbium", 70, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f14 6s2"),
    ("Lanthanides", "Lu", "Lutetium", 71, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f14 5d1 6s2"),
    ("Actinides", "Hf", "Hafnium", 72, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f14 5d2 6s2"),
    ("Transition Metals", "Ta", "Tantalum", 73, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f14 5d3 6s2"),
    ("Transition Metals", "W", "Tungsten", 74, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f14 5d4 6s2"),
    ("Transition Metals", "Re", "Rhenium", 75, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f14 5d5 6s2"),
    ("Transition Metals", "Os", "Osmium", 76, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f14 5d6 6s2"),
    ("Transition Metals", "Ir", "Iridium", 77, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f14 5d7 6s2"),
    ("Transition Metals", "Pt", "Platinum", 78, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f14 5d9 6s1"),
    ("Transition Metals", "Au", "Gold", 79, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f14 5d10 6s1"),
    ("Transition Metals", "Hg", "Mercury", 80, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f14 5d10 6s2"),
    ("Boron Group", "Tl", "Thallium", 81, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f14 5d10 6s2 6p1"),
    ("Carbon Group", "Pb", "Lead", 82, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f14 5d10 6s2 6p2"),
    ("Carbon Group", "Bi", "Bismuth", 83, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f14 5d10 6s2 6p3"),
    ("Halogens", "Po", "Polonium", 84, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f14 5d10 6s2 6p4"),
    ("Noble Gases", "At", "Astatine", 85, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f14 5d10 6s2 6p5"),
    ("Noble Gases", "Rn", "Radon", 86, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f14 5d10 6s2 6p6"),
    ("Alkaline Earth Metals", "Fr", "Francium", 87, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f14 5d10 6s2 6p6 7s1"),
    ("Alkaline Earth Metals", "Ra", "Radium", 88, "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 4f14 5d10 6s2 6p6 7s2"),
    ("Actinides", "Ac", "Actinium", 89, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 6d1 7s2"),
    ("Actinides", "Th", "Thorium", 90, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 6d2 7s2"),
    ("Actinides", "Pa", "Protactinium", 91, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f2 6s2 6p6 6d1 7s2"),
    ("Actinides", "U", "Uranium", 92, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f3 6s2 6p6 6d1 7s2"),
    ("Actinides", "Np", "Neptunium", 93, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f4 6s2 6p6 6d1 7s2"),
    ("Actinides", "Pu", "Plutonium", 94, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f6 6s2 6p6 7s2"),
    ("Actinides", "Am", "Americium", 95, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f7 6s2 6p6 7s2"),
    ("Actinides", "Cm", "Curium", 96, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f7 6s2 6p6 6d1 7s2"),
    ("Actinides", "Bk", "Berkelium", 97, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f9 6s2 6p6 7s2"),
    ("Actinides", "Cf", "Californium", 98, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f10 6s2 6p6 7s2"),
    ("Actinides", "Es", "Einsteinium", 99, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f11 6s2 6p6 7s2"),
    ("Actinides", "Fm", "Fermium", 100, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f12 6s2 6p6 7s2"),
    ("Actinides", "Md", "Mendelevium", 101, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f13 6s2 6p6 7s2"),
    ("Actinides", "No", "Nobelium", 102, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 7s2"),
    ("Actinides", "Lr", "Lawrencium", 103, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d1 7s2"),
    ("Actinides", "Rf", "Rutherfordium", 104, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d2 7s2"),
    ("Actinides", "Db", "Dubnium", 105, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d3 7s2"),
    ("Actinides", "Sg", "Seaborgium", 106, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d4 7s2"),
    ("Actinides", "Bh", "Bohrium", 107, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d5 7s2"),
    ("Actinides", "Hs", "Hassium", 108, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d6 7s2"),
    ("Actinides", "Mt", "Meitnerium", 109, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d7 7s2"),
    ("Actinides", "Ds", "Darmstadtium", 110, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d8 7s2"),
    ("Actinides", "Rg", "Roentgenium", 111, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d9 7s2"),
    ("Actinides", "Cn", "Copernicium", 112, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10"),
    ("Actinides", "Nh", "Nihonium", 113, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10 7s2 7p1"),
    ("Actinides", "Fl", "Flerovium", 114, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10 7s2 7p2"),
    ("Actinides", "Mc", "Moscovium", 115, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10 7s2 7p3"),
    ("Actinides", "Lv", "Livermorium", 116, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10 7s2 7p4"),
    ("Actinides", "Ts", "Tennessine", 117, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10 7s2 7p5"),
    ("Actinides", "Og", "Oganesson", 118, "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10 7s2 7p6"),

]

def create_element_folders(base_path):
    """
    Creates a structured folder hierarchy for the periodic table:
    Periodic-Table\Family\Symbol\Symbol+last 3 characters of the config\Electron-configuration.txt
    
    Args:
    - base_path (str): The root path where the folders will be created.
    """
    try:
        # Ensure the base_path exists
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        
        # Root folder for the periodic table
        periodic_table_folder = os.path.join(base_path, "Periodic-Table")
        if not os.path.exists(periodic_table_folder):
            os.makedirs(periodic_table_folder)
        
        # Process each element
        for i, (family, symbol, name, atomic_number, config) in enumerate(elements_with_details):
            # Create the Family folder
            family_folder_path = os.path.join(periodic_table_folder, family)
            if not os.path.exists(family_folder_path):
                os.makedirs(family_folder_path)
            
            # Create the Symbol folder
            symbol_folder_path = os.path.join(family_folder_path, symbol)
            if not os.path.exists(symbol_folder_path):
                os.makedirs(symbol_folder_path)
            
            # Create the Symbol+Config folder
            short_config = config[-3:]  # Last 3 characters of the electron configuration
            symbol_config_folder_name = f"{symbol}_{short_config}"
            symbol_config_folder_path = os.path.join(symbol_folder_path, symbol_config_folder_name)
            if not os.path.exists(symbol_config_folder_path):
                os.makedirs(symbol_config_folder_path)
            
            # Create the Electron-configuration.txt file
            config_file_path = os.path.join(symbol_config_folder_path, "Electron-configuration.txt")
            with open(config_file_path, "w") as file:
                file.write(f"Element: {name}\n")
                file.write(f"Symbol: {symbol}\n")
                file.write(f"Atomic Number: {atomic_number}\n")
                file.write(f"Family: {family}\n")
                file.write(f"Electron Configuration: {config}\n")
            
            print(f"Created folder and configuration file for: {symbol} - {name}")
            
            # Create a shortcut to the next element's folder, if it exists
            if i + 1 < len(elements_with_details):
                next_family, next_symbol, next_name, next_atomic_number, next_config = elements_with_details[i + 1]
                next_short_config = next_config[-3:]
                next_symbol_config_folder_path = os.path.join(
                    periodic_table_folder, next_family, next_symbol, f"{next_symbol}_{next_short_config}"
                )
                create_shortcut(next_symbol_config_folder_path, symbol_config_folder_path)

    except Exception as e:
        print(f"Error: {e}")


def create_shortcut(target_path, shortcut_path):
    """
    Creates a shortcut to the target folder inside the given shortcut path.
    
    Args:
    - target_path (str): The target folder path for the shortcut.
    - shortcut_path (str): The path where the shortcut will be created.
    """
    try:
        # Convert paths to absolute paths for safety
        target_path = os.path.abspath(target_path)
        shortcut_name = os.path.join(shortcut_path, "Next_Element.lnk")
        
        # Check if the target exists
        if not os.path.exists(target_path):
            print(f"Warning: Target path does not exist: {target_path}")
            return

        # Create a shortcut using the Dispatch library
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortcut(shortcut_name)
        shortcut.TargetPath = target_path
        shortcut.WorkingDirectory = target_path
        shortcut.IconLocation = target_path  # Optional: Set icon to the folder itself
        shortcut.Save()
        
        print(f"Shortcut created: {shortcut_name}")
    
    except Exception as e:
        print(f"Error creating shortcut: {e}")


# Specify the base path where the folders should be created
base_path = r"c:/Users/yourusername/path/Elements"  # Modify this path as necessary
create_element_folders(base_path)


