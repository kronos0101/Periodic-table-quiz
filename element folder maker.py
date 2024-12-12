import os

# List of elements with their families, symbols, names, and electron configurations in order of atomic number from 1 to 118
elements_with_details = [
    ("Alkali Metals", "H", "Hydrogen", "1s1"), ("Noble Gases", "He", "Helium", "1s2"),
    ("Alkali Metals", "Li", "Lithium", "1s2 2s1"), ("Alkaline Earth Metals", "Be", "Beryllium", "1s2 2s2"),
    ("Metalloids", "B", "Boron", "1s2 2s2 2p1"), ("Nonmetals", "C", "Carbon", "1s2 2s2 2p2"),
    ("Nonmetals", "N", "Nitrogen", "1s2 2s2 2p3"), ("Nonmetals", "O", "Oxygen", "1s2 2s2 2p4"),
    ("Halogens", "F", "Fluorine", "1s2 2s2 2p5"), ("Noble Gases", "Ne", "Neon", "1s2 2s2 2p6"),
    ("Alkali Metals", "Na", "Sodium", "1s2 2s2 2p6 3s1"), ("Alkaline Earth Metals", "Mg", "Magnesium", "1s2 2s2 2p6 3s2"),
    ("Metalloids", "Al", "Aluminum", "1s2 2s2 2p6 3s2 3p1"), ("Metalloids", "Si", "Silicon", "1s2 2s2 2p6 3s2 3p2"),
    ("Nonmetals", "P", "Phosphorus", "1s2 2s2 2p6 3s2 3p3"), ("Nonmetals", "S", "Sulfur", "1s2 2s2 2p6 3s2 3p4"),
    ("Halogens", "Cl", "Chlorine", "1s2 2s2 2p6 3s2 3p5"), ("Noble Gases", "Ar", "Argon", "1s2 2s2 2p6 3s2 3p6"),
    ("Alkali Metals", "K", "Potassium", "1s2 2s2 2p6 3s2 3p6 4s1"), ("Alkaline Earth Metals", "Ca", "Calcium", "1s2 2s2 2p6 3s2 3p6 4s2"),
    ("Transition Metals", "Sc", "Scandium", "1s2 2s2 2p6 3s2 3p6 3d1 4s2"),
    ("Transition Metals", "Ti", "Titanium", "1s2 2s2 2p6 3s2 3p6 3d2 4s2"),
    ("Transition Metals", "V", "Vanadium", "1s2 2s2 2p6 3s2 3p6 3d3 4s2"),
    ("Transition Metals", "Cr", "Chromium", "1s2 2s2 2p6 3s2 3p6 3d5 4s1"),
    ("Transition Metals", "Mn", "Manganese", "1s2 2s2 2p6 3s2 3p6 3d5 4s2"),
    ("Transition Metals", "Fe", "Iron", "1s2 2s2 2p6 3s2 3p6 3d6 4s2"),
    ("Transition Metals", "Co", "Cobalt", "1s2 2s2 2p6 3s2 3p6 3d7 4s2"),
    ("Transition Metals", "Ni", "Nickel", "1s2 2s2 2p6 3s2 3p6 3d8 4s2"),
    ("Transition Metals", "Cu", "Copper", "1s2 2s2 2p6 3s2 3p6 3d10 4s1"),
    ("Transition Metals", "Zn", "Zinc", "1s2 2s2 2p6 3s2 3p6 3d10 4s2"),
    ("Post-transition Metals", "Ga", "Gallium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p1"),
    ("Metalloids", "Ge", "Germanium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p2"),
    ("Metalloids", "As", "Arsenic", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p3"),
    ("Nonmetals", "Se", "Selenium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p4"),
    ("Halogens", "Br", "Bromine", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p5"),
    ("Noble Gases", "Kr", "Krypton", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6"),
    ("Alkali Metals", "Rb", "Rubidium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1"),
    ("Alkaline Earth Metals", "Sr", "Strontium", "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2"),
    # Add more elements as needed ...
]

def create_element_folders(base_path):
    """
    Creates folders for each element in the periodic table with the format:
    'Family Folder > Symbol - Element Name Folder > Electron Configuration Folder',
    and places the electron configuration inside the electron configuration folder.
    
    Args:
    - base_path (str): The path where the folders will be created.
    """
    try:
        # Ensure base_path exists, if not, create it
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        
        # Loop through the elements and create folders
        for family, symbol, name, config in elements_with_details:
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
            else:
                print(f"Folder already exists: {config_folder_path}")
    
    except Exception as e:
        print(f"Error: {e}")

# Specify the base path where the folders should be created
base_path = r"C:\Users\Yourusername\Desktop\PeriodicTable"  # Modify this path as necessary
create_element_folders(base_path)
