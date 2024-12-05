import os
import winshell
from win32com.client import Dispatch

# Full list of elements with their families, symbols, names, electron configurations
elements_with_details = [
    ("Nonmetals", "H", "Hydrogen", "1s1"),
    ("Noble Gases", "He", "Helium", "1s2"),
    ("Alkali Metals", "Li", "Lithium", "1s2 2s1"),
    ("Alkaline Earth Metals", "Be", "Beryllium", "1s2 2s2"),
    ("Metalloids", "B", "Boron", "1s2 2s2 2p1"),
    ("Nonmetals", "C", "Carbon", "1s2 2s2 2p2"),
    ("Nonmetals", "N", "Nitrogen", "1s2 2s2 2p3"),
    ("Nonmetals", "O", "Oxygen", "1s2 2s2 2p4"),
    ("Halogens", "F", "Fluorine", "1s2 2s2 2p5"),
    ("Noble Gases", "Ne", "Neon", "1s2 2s2 2p6"),
    ("Alkali Metals", "Na", "Sodium", "1s2 2s2 2p6 3s1"),
    ("Alkaline Earth Metals", "Mg", "Magnesium", "1s2 2s2 2p6 3s2"),
    ("Transition Metals", "Al", "Aluminum", "1s2 2s2 2p6 3s2 3p1"),
    ("Metalloids", "Si", "Silicon", "1s2 2s2 2p6 3s2 3p2"),
    ("Nonmetals", "P", "Phosphorus", "1s2 2s2 2p6 3s2 3p3"),
    ("Nonmetals", "S", "Sulfur", "1s2 2s2 2p6 3s2 3p4"),
    ("Halogens", "Cl", "Chlorine", "1s2 2s2 2p6 3s2 3p5"),
    ("Noble Gases", "Ar", "Argon", "1s2 2s2 2p6 3s2 3p6"),
    ("Alkali Metals", "K", "Potassium", "1s2 2s2 2p6 3s2 3p6 4s1"),
    ("Alkaline Earth Metals", "Ca", "Calcium", "1s2 2s2 2p6 3s2 3p6 4s2"),
    ("Transition Metals", "Sc", "Scandium", "1s2 2s2 2p6 3s2 3p6 4s2 3d1"),
    ("Transition Metals", "Ti", "Titanium", "1s2 2s2 2p6 3s2 3p6 4s2 3d2"),
    ("Transition Metals", "V", "Vanadium", "1s2 2s2 2p6 3s2 3p6 4s2 3d3"),
    ("Transition Metals", "Cr", "Chromium", "1s2 2s2 2p6 3s2 3p6 4s2 3d5"),
    ("Transition Metals", "Mn", "Manganese", "1s2 2s2 2p6 3s2 3p6 4s2 3d5"),
    ("Transition Metals", "Fe", "Iron", "1s2 2s2 2p6 3s2 3p6 4s2 3d6"),
    ("Transition Metals", "Co", "Cobalt", "1s2 2s2 2p6 3s2 3p6 4s2 3d7"),
    ("Transition Metals", "Ni", "Nickel", "1s2 2s2 2p6 3s2 3p6 4s2 3d8"),
    ("Transition Metals", "Cu", "Copper", "1s2 2s2 2p6 3s2 3p6 4s2 3d10"),
    ("Transition Metals", "Zn", "Zinc", "1s2 2s2 2p6 3s2 3p6 4s2 3d10"),
    ("Lanthanides", "La", "Lanthanum", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2"),
    ("Lanthanides", "Ce", "Cerium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1"),
    ("Lanthanides", "Pr", "Praseodymium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1"),
    ("Lanthanides", "Nd", "Neodymium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1"),
    ("Lanthanides", "Pm", "Promethium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1"),
    ("Lanthanides", "Sm", "Samarium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1"),
    ("Lanthanides", "Eu", "Europium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1"),
    ("Lanthanides", "Gd", "Gadolinium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1"),
    ("Lanthanides", "Tb", "Terbium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1"),
    ("Lanthanides", "Dy", "Dysprosium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1"),
    ("Lanthanides", "Ho", "Holmium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1"),
    ("Lanthanides", "Er", "Erbium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1"),
    ("Lanthanides", "Tm", "Thulium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1"),
    ("Lanthanides", "Yb", "Ytterbium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1"),
    ("Lanthanides", "Lu", "Lutetium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1"),
    ("Actinides", "Ac", "Actinium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1"),
    ("Actinides", "Th", "Thorium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d2"),
    ("Actinides", "Pa", "Protactinium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d3"),
    ("Actinides", "U", "Uranium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d4"),
    ("Actinides", "Np", "Neptunium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d5"),
    ("Actinides", "Pu", "Plutonium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d6"),
    ("Actinides", "Am", "Americium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d7"),
    ("Actinides", "Cm", "Curium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d8"),
    ("Actinides", "Bk", "Berkelium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d9"),
    ("Actinides", "Cf", "Californium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10"),
    ("Actinides", "Es", "Einsteinium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d11"),
    ("Actinides", "Fm", "Fermium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d12"),
    ("Actinides", "Md", "Mendelevium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d13"),
    ("Actinides", "No", "Nobelium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d14"),
    ("Actinides", "Lr", "Lawrencium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d15"),
    ("Actinides", "Rf", "Rutherfordium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d16"),
    ("Actinides", "Db", "Dubnium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d17"),
    ("Actinides", "Sg", "Seaborgium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d18"),
    ("Actinides", "Bh", "Bohrium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d19"),
    ("Actinides", "Hs", "Hassium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d20"),
    ("Actinides", "Mt", "Meitnerium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d21"),
    ("Actinides", "Ds", "Darmstadtium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d22"),
    ("Actinides", "Rg", "Roentgenium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d23"),
    ("Actinides", "Cn", "Copernicium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d24"),
    ("Actinides", "Nh", "Nihonium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d25"),
    ("Actinides", "Fl", "Flerovium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d26"),
    ("Actinides", "Mc", "Moscovium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d27"),
    ("Actinides", "Lv", "Livermorium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d28"),
    ("Actinides", "Ts", "Tennessine", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d29"),
    ("Actinides", "Og", "Oganesson", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d30 5p6")

]

def create_element_folders(base_path):
    """
    Creates folders for each element in the periodic table with the format:
    'Family Folder > Symbol - Element Name Folder > Electron Configuration Folder',
    and places the electron configuration inside the electron configuration folder. It also creates a shortcut to the next element.
    
    Args:
    - base_path (str): The path where the folders will be created.
    """
    try:
        # Ensure base_path exists, if not, create it
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        
        # Loop through the elements and create folders
        for i, (family, symbol, name, config) in enumerate(elements_with_details):
            # Family Folder
            family_folder_path = os.path.join(base_path, family)
            if not os.path.exists(family_folder_path):
                os.makedirs(family_folder_path)

            # Symbol - Element Name Folder
            element_folder_name = f"{symbol} - {name}"
            element_folder_path = os.path.join(family_folder_path, element_folder_name)
            
            if not os.path.exists(element_folder_path):
                os.makedirs(element_folder_path)

            # Electron Configuration Folder
            config_folder_name = f"Config - {config}"
            config_folder_path = os.path.join(element_folder_path, config_folder_name)

            if not os.path.exists(config_folder_path):
                os.makedirs(config_folder_path)

                # Create a file with the electron configuration inside the electron config folder
                with open(os.path.join(config_folder_path, "electron_configuration.txt"), "w") as file:
                    file.write(config)
                
                print(f"Folder created: {config_folder_path}")
            
            # Create a shortcut to the next element's configuration folder, if it exists
            if i + 1 < len(elements_with_details):
                next_family, next_symbol, next_name, next_config = elements_with_details[i + 1]
                next_element_folder_name = f"{next_symbol} - {next_name}"
                next_config_folder_name = f"Config - {next_config}"
                
                # Path to next configuration folder
                next_config_folder_path = os.path.join(base_path, next_family, next_element_folder_name, next_config_folder_name)
                
                # Create shortcut to next element's configuration folder
                create_shortcut(config_folder_path, next_config_folder_path)

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
        # Create the shortcut name
        shortcut_name = os.path.join(shortcut_path, "Next_Element_Shortcut.lnk")
        
        # Create a shortcut using the winshell and Dispatch libraries
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortcut(shortcut_name)
        shortcut.TargetPath = target_path  # The path to the next element's electron config folder
        shortcut.WorkingDirectory = target_path
        shortcut.Save()
        
        print(f"Shortcut created: {shortcut_name}")
    
    except Exception as e:
        print(f"Error creating shortcut: {e}")

# Specify the base path where the folders should be created
base_path = r"C:\Users\yourusername\Desktop\PeriodicTable"  # Modify this path as necessary
create_element_folders(base_path)
