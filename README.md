# cookodoo

Cooking module for Odoo 15.0. First version (February 2022)


**Derived ER diagram:**
------

<img src="static/description/Cook_ER_diagram.png" alt="drawing" width="300"/>

<!-- ![A test image](static/description/Cook_ER_diagram.png) -->

### To install this module:

1. Download the project: 
 + Using git:   git clone https://github.com/tonibois/cook.git
 + Download ZIP
2. Unzip in your odoo/addons folder
3. Launch odoo service using developer mode (./odoo-bin --dev=all -d=mydb -c odoo.conf)
4. Entry on your local odoo using web browser (https://localhost:8069)
5. If not set developer mode go to settings and at the bottom of the page activate it
6. Go to Apps and Update packates
7. Update list packages
8. You must see the Cook module
9. Install the cook module

### After installing the module set security settings:

To see the module on the menu, you must first set Access Rights to the models

1. Go to: 
 + Settings --> Technical --> Acces Rights 
2. Set the next permissions 

<img src="static/description/set_AR.png" alt="drawing" width="700"/>

<!-- ![set_permiss](static/description/set_AR.png) -->

### Features:

+ Computation of calories based on protein/fat/carbohydrates and amount of food
+ List of recipes
+ List of ingredients
+ List of instructions
+ Translation languages available: Spanish and Catalan

