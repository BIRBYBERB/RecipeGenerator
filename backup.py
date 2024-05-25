#importing stufffz
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox, ttk
from tkinter import ttk
from tkinter import *
import random

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title_font = tkfont.Font(family='Arial', size=15, weight="bold", slant="italic")
        self.geometry("750x500")
        self.title("Recipe Generator")
        self.saved_recipes = []  # Initialize the saved recipes list
        

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainMenu, RecipePage, CreditPage, MeatPage, VegetablePage, SavedRecipesPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == "SavedRecipesPage":
            frame.update_recipes() 

    def on_closing(self):
        if messagebox.askyesno(title='Quit?', message='Are you sure you want to quit?'):
            self.destroy()

    def update_saved_recipes_page(self):
        self.frames["SavedRecipesPage"].update_recipes()

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text='This is the Main Menu')
        label.place(relx=0.5, rely=0.1, anchor='n')

        button1 = tk.Button(self, text='Recipes', command=lambda: controller.show_frame('RecipePage'))
        button2 = tk.Button(self, text='Credits', command=lambda: controller.show_frame('CreditPage'))
        button3 = tk.Button(self, text='Saved Recipes', command=lambda: controller.show_frame('SavedRecipesPage'))

        label.pack()
        button1.pack()
        button2.pack()
        button3.pack()

        button1.place(relx=0.5, rely=0.3, anchor='n')
        button2.place(relx=0.5, rely=0.4, anchor='n')
        button3.place(relx=0.5, rely=0.5, anchor='n')

#Preperations
boil = [
    "Boil on Water",
    "Boil on Milk"
]
utilities = [
    "Pan",
    "Pot"
]
teaspoon = [
    "Put two teaspoons of",
    "Put a quarter of teaspoons of"
]
seasoning = [
    "Parsley",
    "Garlic"
]
meat_ingredients = [
    "Sirloin Cut",
    "Chicken Breast",
    "Mushroom"
]
vegetable_ingredients = [
    "Cabbage",
    "Salad"
]
toppings = [
    "Tomato",
    "Cilantro",
    "Sliced Broccoli",
    "Red Bell Peppers"
]
addons = [
    "Onions",
    "Butter",
    "Oil"
]
unnamed = [
    "Soy Sauce",
    "White Pepper"
]
unnamedno2 = [
    "Beef Stock",
    "Shaoxing Wine"
]

temperature = random.randint(32, 50)
rest = random.randint(5, 10)

class RecipePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the Recipe Page", font=controller.title_font)
        label.pack(side='top', fill='x', pady=10)
        frame = tk.Frame(self)

        user_recipes = tk.LabelFrame(frame, text='Pick Your Recipes!')
        user_recipes.pack(padx=20, pady=10)

        label1 = tk.Label(user_recipes, text='Main Ingredient')
        self.combobox1 = ttk.Combobox(user_recipes, values=["", "Meat", "Vegetables"])

        label2 = tk.Label(user_recipes, text='Sub Ingredient')
        self.combobox2 = ttk.Combobox(user_recipes, values=["", "Meat", "Vegetables"])

        buttonMenu = tk.Button(self, text='Back to Main Menu',
                               command=lambda: controller.show_frame('MainMenu'))

        buttonGenerate = tk.Button(self, text='Generate Recipe', command=self.random_recipe)
        self.text = tk.Text(self, height=10, width=60)

        buttonFind = tk.Button(self, text='Find Recipe', command=self.find_recipe)

        self.text.pack()
        frame.pack()

        label1.pack()
        self.combobox1.pack()
        label2.pack()
        self.combobox2.pack()

        buttonGenerate.pack(pady=5)
        buttonFind.pack(pady=5)
        buttonMenu.pack(pady=5)

    def find_recipe(self):
        value1 = self.combobox1.get()
        value2 = self.combobox2.get()

        if value1 == "Meat" and value2 == "":
            self.controller.show_frame('MeatPage')
        elif value1 == "Vegetables" and value2 == "":
            self.controller.show_frame('VegetablePage')
        else:
            messagebox.showwarning("Selection Error", "Please select a main ingredient and optionally a sub ingredient.")

    def random_recipe(self):
        value1 = self.combobox1.get()
        value2 = self.combobox2.get()
        
        if value1 == "Meat" and value2 == "":
            self.random_meat_recipe()
        elif value1 == "Vegetables" and value2 == "":
            self.random_vegetable_recipe()
        elif value1 == "Meat" and value2 == "Vegetables" or value1 == "Vegetables" and value2 == "Meat":
            self.random_meatveggie_recipe()
        else:
            messagebox.showwarning("Selection Error", "Please select a main ingredient and optionally a sub ingredient.")

    def random_meat_recipe(self):
        recipe = (
            f"On a {random.choice(utilities)}, sizzling already with {random.choice(addons)}, cook {random.choice(meat_ingredients)} at {temperature} Celsius\n"
            f"Add {random.choice(teaspoon)} of {random.choice(seasoning)}\n"
            f"Then let the {random.choice(meat_ingredients)} rest for about {rest} minutes before serving!"
        )
        self.display_recipe(recipe)

    def random_vegetable_recipe(self):
        recipe = (
            f"Wash the {random.choice(vegetable_ingredients)} in a {random.choice(utilities)} for {rest} minutes\n"
            f"Top it off with some {random.choice(toppings)} and serve!"
        )
        self.display_recipe(recipe)
    
    def random_meatveggie_recipe(self):
        recipe = (
            f"Mix {random.choice(unnamed)} and {random.choice(unnamedno2)} in a {random.choice(utilities)} together, let it boil at {temperature} Celsius for about {rest} minutes.\n"
            f"Once it's all mixed properly, put {random.choice(meat_ingredients)} before {random.choice(vegetable_ingredients)} so the soup can absorb the meat's juices and make the vegetables more tasty.\n"
            f"Keep stirring for {rest} minutes before serving! Vóila!"
        )
        self.display_recipe(recipe)

    def display_recipe(self, recipe):
        self.text.config(state=tk.NORMAL)
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, recipe)
        self.text.config(state=tk.DISABLED)

import tkinter as tk
from tkinter import font as tkfont, messagebox

class MeatPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Meat Recipes! Get'cho Meat Recipes!", font=controller.title_font)
        label.pack(side='top', fill='x', pady=10)

        canvas = tk.Canvas(self)
        self.scrollable_frame = tk.Frame(canvas)

        scrollbar = tk.Scrollbar(self, orient='vertical', command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side='right', fill='y')
        canvas.pack(side='left', fill='both', expand=True)
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor='n')

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        self.create_meat_recipes()

        buttonMenu = tk.Button(self, text='Back to Main Menu',
                               command=lambda: controller.show_frame('MainMenu'))
        buttonMenu.pack(pady=10)

        # Bind mouse wheel to scroll
        canvas.bind_all("<MouseWheel>", lambda event: self._on_mousewheel(event, canvas))

    def _on_mousewheel(self, event, canvas):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def create_meat_recipes(self):
        self.CheckButton1_var = tk.IntVar()
        self.CheckButton2_var = tk.IntVar()
        self.CheckButton3_var = tk.IntVar()
        self.Filipino_Beef_Steak()
        self.Sweet_Potato_Skin_Tacos()
        self.Beef_Sliders()

    def Filipino_Beef_Steak(self):
        filipinoscorch = tk.LabelFrame(self.scrollable_frame, text='Filipino Beef Steak')
        filipinoscorch.pack(padx=20, pady=10)  # Center the label frame with fill

        buttonInfo = tk.Button(filipinoscorch, text='Show Ingredients', command=self.info1)
        CheckButton = tk.Checkbutton(filipinoscorch, variable=self.CheckButton1_var,
                                     command=lambda: self.save_recipe(self.CheckButton1_var, 'Filipino Beef Steak', self.Filipino_Beef_Steak_Recipe()))

        label = tk.Label(filipinoscorch, text=self.Filipino_Beef_Steak_Recipe())

        label.grid(row=0, column=0, columnspan=2, sticky='w')
        buttonInfo.grid(row=1, column=0, sticky='w')
        CheckButton.grid(row=1, column=1, sticky='e')

    def Sweet_Potato_Skin_Tacos(self):
        sweetpotatoskin = tk.LabelFrame(self.scrollable_frame, text="Stuffed Sweet Potato Skin Tacos")
        sweetpotatoskin.pack(padx=20, pady=10)  # Center the label frame with fill

        button2Info = tk.Button(sweetpotatoskin, text='Show Ingredients', command=self.info2)
        CheckButton2 = tk.Checkbutton(sweetpotatoskin, variable=self.CheckButton2_var,
                                      command=lambda: self.save_recipe(self.CheckButton2_var, 'Stuffed Sweet Potato Skin Tacos', self.Sweet_Potato_Skin_Recipe()))
        label2 = tk.Label(sweetpotatoskin, text=self.Sweet_Potato_Skin_Recipe())

        label2.grid(row=0, column=0, columnspan=2, sticky='w')
        button2Info.grid(row=1, column=0, sticky='w')
        CheckButton2.grid(row=1, column=1, sticky='e')

    def Beef_Sliders(self):
        beefsliders = tk.LabelFrame(self.scrollable_frame, text="Beef Sliders")
        beefsliders.pack(padx=20, pady=10)  # Center the label frame with fill

        button3Info = tk.Button(beefsliders, text='Show Ingredients', command=self.info3)
        CheckButton3 = tk.Checkbutton(beefsliders, variable=self.CheckButton3_var,
                                      command=lambda: self.save_recipe(self.CheckButton3_var, 'Beef Sliders', self.Beef_Sliders_Recipe()))
        label3 = tk.Label(beefsliders, text=self.Beef_Sliders_Recipe())

        label3.grid(row=0, column=0, columnspan=2, sticky='w')
        button3Info.grid(row=1, column=0, sticky='w')
        CheckButton3.grid(row=1, column=1, sticky='e')

    def Filipino_Beef_Steak_Recipe(self):
        return (
            'Step 1\n'
            'Place sliced beef in a large bowl. Whisk together lemon juice, soy sauce, sugar, salt, and pepper in a small bowl; pour over beef and toss to coat. Stir in cornstarch. Cover and refrigerate for 1 hour to overnight.\n'
            '\nStep 2\n'
            'Heat vegetable oil in a large skillet over medium heat.\n'
            '\nStep 3\n'
            'Remove beef slices from marinade, shaking to remove any excess liquid. Discard marinade.\n'
            '\nStep 4\n'
            'Working in batches, fry beef slices in hot oil until they start to firm and are reddish-pink and juicy in the center, 2 to 4 minutes per side. Transfer beef slices to a serving platter.\n'
            '\nStep 5\n'
            'Heat olive oil in a small skillet over medium heat. Cook and stir onion and garlic in hot oil until onion is golden brown, 5 to 7 minutes; spoon over beef slices.'
        )

    def Sweet_Potato_Skin_Recipe(self):
        return (
            'Step 1\n'
            'Preheat the oven to 400 degrees F (200 degrees C) and line a sheet pan with foil.\n'
            '\nStep 2\n'
            'Slice each sweet potato in half lengthwise, and rub cut surfaces and skins with olive oil. Evenly sprinkle about 1 tablespoon taco seasoning all over sweet potatoes and place on the prepared pan, cut side down.\n'
            '\nStep 3\n'
            'Roast in the preheated oven for 15 minutes, then turn and continue roasting until potatoes are fork-tender, about 15 minutes more.\n'
            '\nStep 4\n'
            'Meanwhile, heat a large skillet over medium heat. Cook and stir ground beef in the hot skillet until browned and crumbly, breaking up clumps with a spatula, 5 to 8 minutes; drain excess fat.\n'
            '\nStep 5\n'
            'Sprinkle meat with remaining 2 tablespoons taco seasoning mix and stir in water. Simmer until liquid is evaporated, about 5 minutes.\n'
            '\nStep 6\n'
            'Place roasted sweet potatoes on a cutting board and scoop out most of the sweet potato flesh, leaving about 1/4-inch flesh inside the skins. Cut the sweet potato flesh into bite-sized pieces and stir into the ground beef mixture.\n'
            '\nStep 7\n'
            'Fill each sweet potato shell with beef and sweet potato mixture, gently pressing to fill. Place filled sweet potato skins on a serving plate and top with taco toppings.'
        )
    
    def Beef_Sliders_Recipe(self):
        return (
            'Step 1\n'
            'Preheat the oven to 350 degrees F (175 degrees C). Brush the bottom and sides of a 9x13-inch baking dish with melted butter until lightly coated.\n'
            '\nStep 2\n'
            'Place bottom half of rolls in baking dish and top evenly with roast beef slices. Drizzle BBQ sauce evenly over roast beef and dollop cheese sauce evenly over the top. Place top roll halves on top.\n'
            '\nStep 3\n'
            'Stir together remaining butter, garlic powder, and onion powder and brush evenly over bun tops.  Sprinkle with bagel seasoning.\n'
            '\nStep 4\n'
            'Bake in the preheated oven until the center is warm and melted, and bread is toasted and golden brown, 12 to 14 minutes.'
        )

    def info1(self):
        messagebox.showinfo("Ingredients for Filipino Beef Steak", 
                            "Ingredients:\n- Beef\n- Lemon juice\n- Soy sauce\n- Sugar\n- Salt\n- Pepper\n- Cornstarch\n- Vegetable oil\n- Onion\n- Garlic\n- Olive oil")

    def info2(self):
        messagebox.showinfo("Ingredients for Stuffed Sweet Potato Skin Tacos", 
                            "Ingredients:\n- Sweet potatoes\n- Olive oil\n- Taco seasoning\n- Ground beef\n- Water\n- Taco toppings")

    def info3(self):
        messagebox.showinfo("Ingredients for Roasted Beef Sliders:",
                            "\n- 4 tablespoons butter, melted, divided\n- 1 (12 roll) package Hawaiian rolls, split in half horizontally\n- 12 ounces deli roast beef\n- 1/2 cup  thin tangy BBQ sauce, such as Arby's® Original Sauce\n- 1 cup Cheddar cheese sauce\n- 1/4 teaspoon garlic powder\n- 1/4 teaspoon onion powder\n- 2 teaspoons everything bagel seasoning")

    def save_recipe(self, var, title, recipe):
        if var.get() == 1:
            if (title, recipe) not in self.controller.saved_recipes:
                self.controller.saved_recipes.append((title, recipe))
        else:
            if (title, recipe) in self.controller.saved_recipes:
                self.controller.saved_recipes.remove((title, recipe))
        self.controller.update_saved_recipes_page()
    
    def uncheck_all(self):
        self.CheckButton1_var.set(0)
        self.CheckButton2_var.set(0)
        self.CheckButton3_var.set(0)


class VegetablePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Vegetable Recipes! Cling Clang, Cling! Healthy for your body!", font=controller.title_font)
        label.pack(side='top', fill='x', pady=10)
        frame = tk.Frame(self)

        buttonMenu = tk.Button(self, text='Back to Main Menu',
                               command=lambda: controller.show_frame('MainMenu'))
        
        frame.pack()
        buttonMenu.pack()

        canvas = tk.Canvas(self)
        self.scrollable_frame = tk.Frame(canvas)

        scrollbar = tk.Scrollbar(self, orient='vertical', command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side='right', fill='y')
        canvas.pack(side='left', fill='both', expand=True)
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor='n')

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        self.create_veggie_recipes()
        # Bind mouse wheel to scroll
        canvas.bind_all("<MouseWheel>", lambda event: self._on_mousewheel(event, canvas))

    def _on_mousewheel(self, event, canvas):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def create_veggie_recipes(self):
        self.CheckButton1_var = tk.IntVar()
        self.CheckButton2_var = tk.IntVar()
        self.Vegan_French_Toast()
        self.Sweet_Potato_And_Peanut_Curry()
        self.Beef_Sliders()

    def Vegan_French_Toast(self):
        VFT = tk.LabelFrame(self.scrollable_frame, text='Vegan French Toast')
        VFT.pack(padx=20, pady=10, anchor='center')  # Center the label frame with fill

        buttonInfo = tk.Button(VFT, text='Show Ingredients', command=self.info1)
        CheckButton = tk.Checkbutton(VFT, variable=self.CheckButton1_var,
                                     command=lambda: self.save_recipe(self.CheckButton1_var, 'Vegan French Toast', self.VFT_Recipe()))

        label = tk.Label(VFT, text=self.VFT_Recipe())

        label.grid(row=0, column=0, columnspan=2, sticky='w')
        buttonInfo.grid(row=1, column=0, sticky='w')
        CheckButton.grid(row=1, column=1, sticky='e')

    def Sweet_Potato_And_Peanut_Curry(self):
        SP2C = tk.LabelFrame(self.scrollable_frame, text="Sweet Potato and Peanut Curry")
        SP2C.pack(padx=20, pady=10, anchor='center')  # Center the label frame with fill

        button2Info = tk.Button(SP2C, text='Show Ingredients', command=self.info2)
        CheckButton2 = tk.Checkbutton(SP2C, variable=self.CheckButton2_var,
                                      command=lambda: self.save_recipe(self.CheckButton2_var, 'Sweet Potato and Peanut Curry', self.SPAPC_Recipe()))
        label2 = tk.Label(SP2C, text=self.SPAPC_Recipe())

        label2.grid(row=0, column=0, columnspan=2, sticky='w')
        button2Info.grid(row=1, column=0, sticky='w')
        CheckButton2.grid(row=1, column=1, sticky='e')

    def Beef_Sliders(self):
        beefsliders = tk.LabelFrame(self.scrollable_frame, text="Stuffed Sweet Potato Skin Tacos")
        beefsliders.pack(padx=20, pady=10, anchor='center')  # Center the label frame with fill

        button2Info = tk.Button(beefsliders, text='Show Ingredients', command=self.info2)
        CheckButton2 = tk.Checkbutton(beefsliders, variable=self.CheckButton2_var,
                                      command=lambda: self.save_recipe(self.CheckButton2_var, 'Beef Sliders', self.Beef_Sliders()))
        label2 = tk.Label(beefsliders, text=self.Beef_Sliders())

        label2.grid(row=0, column=0, columnspan=2, sticky='w')
        button2Info.grid(row=1, column=0, sticky='w')
        CheckButton2.grid(row=1, column=1, sticky='e')

    def VFT_Recipe(self):
        return (
            'Step 1\n'
            'In a blender combine milk, cashews, and dates and blend until smooth.\n'
            '\nStep 2\n'
            'While still blending add the rest of ingredients.\n'
            '\nStep 3\n'
            'Pour the batter into a pie or cake dish, dip both sides of each slice of bread in the batter, or use a spatula to evenly spread a layer of batter on the slice of bread.\n'
            '\nStep 4\n'
            'Then brown in a lightly oiled skillet.\n'
            '\nStep 5\n'
            'Top with pure maple syrup or your favorite fruit topping.'
        )

    def SPAPC_Recipe(self):
        return (
            'Step 1\n'
            'Melt 1 tbsp coconut oil in a saucepan over a medium heat and soften 1 chopped onion for 5 mins. Add 2 grated garlic cloves and a grated thumb-sized piece of ginger, and cook for 1 min until fragrant.\n'
            '\nStep 2\n'
            'Stir in 3 tbsp Thai red curry paste, 1 tbsp smooth peanut butter and 500g sweet potato, peeled and cut into chunks, then add 400ml coconut milk and 200ml water.\n'
            '\nStep 3\n'
            'Bring to the boil, turn down the heat and simmer, uncovered, for 25-30 mins or until the sweet potato is soft.\n'
            '\nStep 4\n'
            'Stir through 200g spinach and the juice of 1 lime, and season well. Serve with cooked rice, and if you want some crunch, sprinkle over a few dry roasted peanuts.'
        )
    
    def Beef_Sliders(self):
        return (
            'Step 1\n'
            'Preheat the oven to 350 degrees F (175 degrees C). Brush the bottom and sides of a 9x13-inch baking dish with melted butter until lightly coated.\n'
            '\nStep 2\n'
            'Place bottom half of rolls in baking dish and top evenly with roast beef slices. Drizzle BBQ sauce evenly over roast beef and dollop cheese sauce evenly over the top. Place top roll halves on top.\n'
            '\nStep 3\n'
            'Stir together remaining butter, garlic powder, and onion powder and brush evenly over bun tops.  Sprinkle with bagel seasoning.\n'
            '\nStep 4\n'
            'Bake in the preheated oven until the center is warm and melted, and bread is toasted and golden brown, 12 to 14 minutes.'
        )

    def info1(self):
        messagebox.showinfo("Ingredients for Roasted Beef Sliders:",
                            "\n- 1 Cup organic soy or rice milk\n- 1 Cup cashews unsalted\n- 3/4 Cup Dates Pitted\n- 2 tbsp egg replacer\n- 1/2 tsp sea salt\n- 1 tbsp vanilla\n- 8-10 slices of your favorite bread")

    def info2(self):
        messagebox.showinfo("Ingredients for Roasted Sweet Potato and Peanut Curry:",
                            "\n- 1 tbsp coconut oil\n- 1 onion, chopped\n- 2 garlic cloves, grated\n- thumb-sized piece ginger, grated\n- 3 tbsp Thai red curry paste (check the label to make sure its vegetarian/ vegan)\n- 1 tbsp smooth peanut butter\n- 500g sweet potato, peeled and cut into chunks\n- 400ml can coconut milk\n- 200g bag spinach\n- 1 lime, juiced\n- cooked rice, to serve (optional)\n- dry roasted peanuts, to serve (optional)")

    def info3(self):
        messagebox.showinfo("Ingredients for Roasted Beef Sliders:",
                            "\n- 4 tablespoons butter, melted, divided\n- 1 (12 roll) package Hawaiian rolls, split in half horizontally\n- 12 ounces deli roast beef\n- 1/2 cup  thin tangy BBQ sauce, such as Arby's® Original Sauce\n- 1 cup Cheddar cheese sauce\n- 1/4 teaspoon garlic powder\n- 1/4 teaspoon onion powder\n- 2 teaspoons everything bagel seasoning")

    def save_recipe(self, var, title, recipe):
        if var.get() == 1:
            if (title, recipe) not in self.controller.saved_recipes:
                self.controller.saved_recipes.append((title, recipe))
        else:
            if (title, recipe) in self.controller.saved_recipes:
                self.controller.saved_recipes.remove((title, recipe))
        self.controller.update_saved_recipes_page()
    
    def uncheck_all(self):
        self.CheckButton1_var.set(0)
        self.CheckButton2_var.set(0)

import tkinter as tk
from tkinter import messagebox

class SavedRecipesPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.buttonMenu = tk.Button(self, text="Return to Main Menu", 
                               command=lambda: controller.show_frame('MainMenu'))
        self.buttonMenu.pack(padx=5, pady=5)

        canvas = tk.Canvas(self)
        self.scrollable_frame = tk.Frame(canvas)

        scrollbar = tk.Scrollbar(self, orient='vertical', command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side='right', fill='y')
        canvas.pack(side='left', fill='both', expand=True)
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor='n')

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.bind_all("<MouseWheel>", lambda event: self._on_mousewheel(event, canvas))

    def _on_mousewheel(self, event, canvas):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def update_recipes(self):
        # Clear the scrollable frame content
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        if not self.controller.saved_recipes:
            label = tk.Label(self.scrollable_frame, text="No saved recipes.", font=self.controller.title_font)
            label.pack(side='top', fill='x', pady=10)
        else:
            for title, recipe in self.controller.saved_recipes:
                frame = tk.LabelFrame(self.scrollable_frame, text=title)
                frame.pack(padx=20, pady=10, fill='x', expand=True)  # Ensure it expands
                label = tk.Label(frame, text=recipe)
                label.pack()

        clearButton = tk.Button(self.scrollable_frame, text='Clear All', command=self.AYS)
        clearButton.pack(pady=10)

    def AYS(self):
        if self.controller.saved_recipes and messagebox.askyesno(title="Clear All", message="Are you sure you would like to clear your saved recipes?"):
            self.clear_recipes()
        else:
            messagebox.showinfo("", "There is nothing.")

    def clear_recipes(self):
        self.controller.saved_recipes.clear()
        self.controller.frames['MeatPage'].uncheck_all()  # Uncheck all checkboxes in MeatPage
        self.controller.frames['VegetablePage'].uncheck_all()
        self.update_recipes()

class CreditPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Muhammad Faiz Adri Ar Rasyid \n(21120123140183)", font=controller.title_font)
        label.pack(side='top', fill='x', pady=10)
        button = tk.Button(self, text='Back to Main Menu',
                           command=lambda: controller.show_frame('MainMenu'))

        button.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()