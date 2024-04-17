import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class JdRCampaignManager:
    def __init__(self, master):
        self.master = master
        master.title("Gestionnaire de Campagne de JdR")

        self.label = tk.Label(master, text="Bienvenue dans le Gestionnaire de Campagne de JdR !")
        self.label.pack()

        # Menu
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)

        # Menu Fichier
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Fichier", menu=self.file_menu)
        self.file_menu.add_command(label="Charger Campagne", command=self.load_campaign)
        self.file_menu.add_command(label="Enregistrer Campagne", command=self.save_campaign)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quitter", command=master.quit)

        # Menu Gérer
        self.manage_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Gérer", menu=self.manage_menu)
        self.manage_menu.add_command(label="Personnages", command=self.switch_to_characters_page)
        self.manage_menu.add_command(label="Scénarios", command=self.switch_to_scenarios_page)
        self.manage_menu.add_command(label="Objets", command=self.switch_to_items_page)

    def load_campaign(self):
        file_path = filedialog.askopenfilename(title="Charger Campagne", filetypes=[("Fichiers de Campagne", "*.json")])
        if file_path:
            messagebox.showinfo("Charger Campagne", f"Chargement depuis {file_path}")

    def save_campaign(self):
        file_path = filedialog.asksaveasfilename(title="Enregistrer Campagne", filetypes=[("Fichiers de Campagne", "*.json")])
        if file_path:
            messagebox.showinfo("Enregistrer Campagne", f"Enregistrement vers {file_path}")

    def switch_to_characters_page(self):
        characters_window = tk.Toplevel(self.master)
        characters_page = CharactersPage(characters_window)

    def switch_to_scenarios_page(self):
        scenarios_window = tk.Toplevel(self.master)
        scenarios_page = ScenariosPage(scenarios_window)

    def switch_to_items_page(self):
        items_window = tk.Toplevel(self.master)
        items_page = ItemsPage(items_window)

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

root = tk.Tk()
campaign_manager = JdRCampaignManager(root)
root.mainloop()
