import tkinter as tk
from tkinter import messagebox

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

        self.label = tk.Label(master, text="Page de Gestion des Personnages")
        self.label.pack()

        self.add_character_button = tk.Button(master, text="Ajouter Personnage", command=self.add_character)
        self.add_character_button.pack()

    def add_character(self):
        messagebox.showinfo("Ajouter Personnage", "Fonctionnalité à implémenter")

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

