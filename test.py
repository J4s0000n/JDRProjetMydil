import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3


# Connexion à la base de données SQLite
conn = sqlite3.connect('jdr_campaign.db')
c = conn.cursor()

# Création de la table des personnages
c.execute('''CREATE TABLE IF NOT EXISTS characters
             (id INTEGER PRIMARY KEY, name TEXT, firstname TEXT, stats TEXT)''')

# Création de la table des scénarios
c.execute('''CREATE TABLE IF NOT EXISTS scenarios
             (id INTEGER PRIMARY KEY, name TEXT)''')

# Création de la table des objets
c.execute('''CREATE TABLE IF NOT EXISTS items
             (id INTEGER PRIMARY KEY, name TEXT)''')

conn.commit()

class JdRCampaignManager:
    def __init__(self, master):
        self.master = master
        master.title("Gestionnaire de Campagne de JdR")

        self.label = tk.Label(master, text="Bienvenue dans le Gestionnaire de Campagne de JdR !")
        self.label.pack()

        self.load_campaign_button = tk.Button(master, text="Charger Campagne", command=self.load_campaign)
        self.load_campaign_button.pack()

        self.create_campaign_button = tk.Button(master, text="Créer Campagne", command=self.create_campaign)
        self.create_campaign_button.pack()

    def load_campaign(self):
        # Mettez ici le code pour charger une campagne existante
        messagebox.showinfo("Charger Campagne", "Fonctionnalité à implémenter")

    def create_campaign(self):
        # Mettez ici le code pour créer une nouvelle campagne
        messagebox.showinfo("Créer Campagne", "Fonctionnalité à implémenter")


class CharactersPage:
    def __init__(self, master):
        self.master = master
        master.title("Gérer les Personnages")

        self.tabControl = ttk.Notebook(master)
        self.tabControl.pack(expand=1, fill="both")

        # Onglet "Ajouter Personnage"
        self.add_character_tab = tk.Frame(self.tabControl)
        self.tabControl.add(self.add_character_tab, text="Ajouter Personnage")
        self.add_character_frame = tk.Frame(self.add_character_tab)
        self.add_character_frame.pack(padx=10, pady=10)

        # Ajout des champs pour ajouter un personnage
        self.add_name_label = tk.Label(self.add_character_frame, text="Nom:")
        self.add_name_label.grid(row=0, column=0, sticky="e")
        self.add_name_entry = tk.Entry(self.add_character_frame)
        self.add_name_entry.grid(row=0, column=1)

        self.add_firstname_label = tk.Label(self.add_character_frame, text="Prénom:")
        self.add_firstname_label.grid(row=1, column=0, sticky="e")
        self.add_firstname_entry = tk.Entry(self.add_character_frame)
        self.add_firstname_entry.grid(row=1, column=1)

        self.add_stats_label = tk.Label(self.add_character_frame, text="Stats:")
        self.add_stats_label.grid(row=2, column=0, sticky="e")
        self.add_stats_entry = tk.Entry(self.add_character_frame)
        self.add_stats_entry.grid(row=2, column=1)

        self.add_character_button = tk.Button(self.add_character_frame, text="Ajouter", command=self.add_character)
        self.add_character_button.grid(row=3, columnspan=2)

        # Onglet "Modifier Personnage"
        self.modify_character_tab = tk.Frame(self.tabControl)
        self.tabControl.add(self.modify_character_tab, text="Modifier Personnage")
        self.modify_character_frame = tk.Frame(self.modify_character_tab)
        self.modify_character_frame.pack(padx=10, pady=10)

        # Ajout des champs pour modifier les statistiques d'un personnage
        self.modify_listbox_label = tk.Label(self.modify_character_frame, text="Liste des Personnages:")
        self.modify_listbox_label.grid(row=0, column=0, sticky="e")
        self.modify_characters_listbox = tk.Listbox(self.modify_character_frame)
        self.modify_characters_listbox.grid(row=0, column=1, padx=5, pady=5)

        self.modify_stats_label = tk.Label(self.modify_character_frame, text="Nouvelles Stats:")
        self.modify_stats_label.grid(row=1, column=0, sticky="e")
        self.modify_stats_entry = tk.Entry(self.modify_character_frame)
        self.modify_stats_entry.grid(row=1, column=1)

        self.modify_listbox_label = tk.Label(self.modify_character_frame, text="Liste des Personnages:")
        self.modify_listbox_label.grid(row=0, column=0, sticky="e")
        self.modify_characters_listbox = tk.Listbox(self.modify_character_frame)
        self.modify_characters_listbox.grid(row=0, column=1, padx=5, pady=5)

        self.modify_button = tk.Button(self.modify_character_frame, text="Modifier", command=self.modify_character)
        self.modify_button.grid(row=2, columnspan=2)

        # Onglet "Liste des Personnages"
        self.list_characters_tab = tk.Frame(self.tabControl)
        self.tabControl.add(self.list_characters_tab, text="Liste des Personnages")
        self.list_characters_frame = tk.Frame(self.list_characters_tab)
        self.list_characters_frame.pack(padx=10, pady=10)

        # Liste des personnages
        self.list_characters_label = tk.Label(self.list_characters_frame, text="Liste des Personnages:")
        self.list_characters_label.pack()
        self.list_characters_listbox = tk.Listbox(self.list_characters_frame)
        self.list_characters_listbox.pack()

        # Charger les personnages
        self.load_characters()



        # Création de la combobox pour sélectionner la statistique à modifier
        self.stats_label = tk.Label(self.modify_character_frame, text="Statistique à modifier:")
        self.stats_label.grid(row=1, column=0, sticky="e")
        self.stats_options = ["Force", "Agilité", "Intelligence"]  # Options de la combobox
        self.stats_combobox = ttk.Combobox(self.modify_character_frame, values=self.stats_options)
        self.stats_combobox.grid(row=1, column=1)

        # Bouton pour modifier le personnage
        self.modify_button = tk.Button(self.modify_character_frame, text="Modifier", command=self.modify_character)
        self.modify_button.grid(row=2, columnspan=2)

        # Charger les personnages pour la modification
        self.load_characters_for_modification()

    def add_character(self):
        name = self.add_name_entry.get()
        firstname = self.add_firstname_entry.get()
        stats = self.add_stats_entry.get()

        # Vérifier si tous les champs sont remplis
        if name and firstname and stats:
            c.execute("INSERT INTO characters (name, firstname, stats) VALUES (?, ?, ?)", (name, firstname, stats))
            conn.commit()
            messagebox.showinfo("Ajouter Personnage", "Personnage ajouté avec succès.")
            self.load_characters()  # Recharger la liste des personnages après l'ajout
        else:
            messagebox.showwarning("Ajouter Personnage", "Veuillez remplir tous les champs.")

    def load_characters(self):
        self.list_characters_listbox.delete(0, tk.END)
        c.execute("SELECT name, firstname FROM characters")
        characters = c.fetchall()
        for character in characters:
            self.list_characters_listbox.insert(tk.END, f"{character[0]} {character[1]}")

    def modify_character(self):
        selected_character = self.modify_characters_listbox.get(tk.ACTIVE)
        new_stat_value = self.modify_stats_entry.get()
        selected_stat = self.modify_stats_combobox.get()

        if selected_character and new_stat_value and selected_stat:
            character_name, character_firstname = selected_character.split()
            # Modifier la statistique sélectionnée pour le personnage sélectionné
            c.execute("UPDATE characters SET ?=? WHERE name=? AND firstname=?", (selected_stat.lower(), new_stat_value, character_name, character_firstname))
            conn.commit()
            messagebox.showinfo("Modifier Personnage", f"{selected_stat} du personnage modifiée avec succès.")
        else:
            messagebox.showwarning("Modifier Personnage", "Veuillez sélectionner un personnage, une statistique et entrer une nouvelle valeur de statistique.")

    def load_characters_for_modification(self):
        self.modify_characters_listbox.delete(0, tk.END)
        c.execute("SELECT name, firstname FROM characters")
        characters = c.fetchall()
        for character in characters:
            self.modify_characters_listbox.insert(tk.END, f"{character[0]} {character[1]}")
...

# Dans la fonction switch_to_characters_page, utilisez CharactersPage au lieu de CharactersPageFrame

def switch_to_characters_page():
    characters_window = tk.Toplevel(root)
    characters_page = CharactersPage(characters_window)



class ScenariosPage:
    def __init__(self, master):
        self.master = master
        master.title("Gérer les Scénarios")

        self.label = tk.Label(master, text="Page de Gestion des Scénarios")
        self.label.pack()

        self.add_scenario_button = tk.Button(master, text="Ajouter Scénario", command=self.add_scenario)
        self.add_scenario_button.pack()

    def add_scenario(self):
        messagebox.showinfo("Ajouter Scénario", "Fonctionnalité à implémenter")

class ItemsPage:
    def __init__(self, master):
        self.master = master
        master.title("Gérer les Objets")

        self.label = tk.Label(master, text="Page de Gestion des Objets")
        self.label.pack()

        self.add_item_button = tk.Button(master, text="Ajouter Objet", command=self.add_item)
        self.add_item_button.pack()

    def add_item(self):
        messagebox.showinfo("Ajouter Objet", "Fonctionnalité à implémenter")

def switch_to_characters_page():
    characters_window = tk.Toplevel(root)
    characters_page = CharactersPage(characters_window)

def switch_to_scenarios_page():
    scenarios_window = tk.Toplevel(root)
    scenarios_page = ScenariosPage(scenarios_window)

def switch_to_items_page():
    items_window = tk.Toplevel(root)
    items_page = ItemsPage(items_window)

root = tk.Tk()
campaign_manager = JdRCampaignManager(root)

characters_button = tk.Button(root, text="Personnages", command=switch_to_characters_page)
characters_button.pack()

scenarios_button = tk.Button(root, text="Scénarios", command=switch_to_scenarios_page)
scenarios_button.pack()

items_button = tk.Button(root, text="Objets", command=switch_to_items_page)
items_button.pack()

root.mainloop()
