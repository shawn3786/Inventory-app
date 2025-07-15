import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os
import pickle

# --- File Paths ---
# Use consistent file paths
FINISHED_ITEMS_FILE = os.path.join(os.getcwd(), "Finished Items.txt")
INVENTORY_DICT_FILE = os.path.join(os.getcwd(), "inventory_items_dict.pkl")

# --- Global Initialization (Keep as is based on your request) ---
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# --- User-Provided Initial Data (Keeping as per your request) ---
# This list is used for the 'inventory' page display.
# Note: New items added via "Add Inventory Items" will *not* automatically appear
# in this hardcoded list unless you manually add them here or implement a merge.
# For a fully dynamic inventory, you would typically load this list from a persistent
# storage (like a pickle file) at the start of the app.
inventory_items = [
    {"name": "Wings", "image": "Wings.jpg"},
    {"name": "Filets", "image": "Filets.jpg"},
    {"name": "Fries", "image": "Fries.jpg"},
    {"name": "Burger Buns", "image": "Burger Buns.jpg"},
    {"name": "Potato Pops", "image": "Potato Pops.jpg"},
    {"name": "Onion Rings", "image":"Onion Rings.jpg" },
    {"name": "chicken Nugets Pops", "image":"Chicken Nugets.jpg"},
    {"name": "Chili Cheese Nugets", "image": "Chili Cheese Nugets.jpg"},
    {"name": "Becons", "image": "Becons.jpg"},
    {"name": "Churros", "image": "churros.jpg"},
    {"name": "Brownies", "image": "Brownies.jpg"},
    {"name": "Choclate Fudge Cookies", "image":"Choclate Fudge Cookies.jpg"},
    {"name": "White Macadaima cookies", "image":"White Macadaima cookies.jpg"},
    {"name": "Pink Onion", "image": "Pink Onion.jpg"},
    {"name": "Waffles", "image": "Waffles.jpg" },
    {"name": "Green Onion", "image": "green Onion.jpg"},
    {"name": "Nutella", "image": "Nutella.jpg"},
    {"name": "Oreo Biscuts", "image": "Oreo Biscuts.jpg"},
    {"name": "Gutio", "image": None},
    {"name": "Whipped Cream", "image": None},
    {"name": "Liqude Choclate", "image": None},
    {"name": "Jalapenos can", "image": "Jalapenos can.jpg"},
    {"name": "Coleslaw", "image": "Coleslaw.jpg"},
    {"name": "gurke can", "image": "gurke.jpg"},
    {"name": "Rosmery Katchup bottle", "image": None},
    {"name": "Cheese Sauce Bottle ", "image": None},
    {"name": "Extra Cheese Sauce Bottle ", "image": None},
    {"name": "Jalapeno Sauce Bottle ", "image": None},
    {"name": "Becon Sauce Bottle ", "image": None},
    {"name": "Truffle Sauce Bottle ", "image": None},
    {"name": "Sweet Jalapenu Sauce", "image": "Sweet Jalapenu Sauce.jpg"},
    {"name": "Harisa Mayo", "image": "Harisa Mayo.jpg"},
    {"name": "Garlic Mayo", "image": "Garlic Mayo.jpg"},
    {"name": "Hot Chili Sauce", "image": "Hot Chili Sauce.jpg"},
    {"name": "Rosmary Katchup Sauce", "image": "Rosmery Katchup Sauce.jpg"},
    {"name": "BBQ Sauce", "image": "BBQ Sauce.jpg"},
    {"name": "Truffle Aloi", "image": "Truffle Aloi.jpg"},
    {"name": "white Truffle Flavour", "image": "white Truffle Flavour.jpg"},
    {"name": "Garlic Cheese Flavour", "image": "Garlic Cheese Flavour.jpg"},
    {"name": "American BBQ Flavour ", "image": "American BBQ Flavour.jpg"},
    {"name": "Korean Spice Flavour ", "image": "Korean Spice Flavour.jpg"},
    {"name": "Salse Jalapeno Flavour", "image": "Sweet Jalapenu Sauce.jpg"},
    {"name": "Sweet Chili Flavour", "image": "Sweet Chili Flavour.jpg"},
    {"name": "Blue Hot Habanero Flavour", "image": "Blue Hot Habanero Flavour.jpg"},
    {"name": "Classic Cheese Tortilla", "image": "Classic Cheese Tortilla.jpg"},
    {"name": "Sweet Chili Tortilla", "image": "Sweet Chili Tortilla.jpg"},
    {"name": "Oriental Spices Tortilla", "image": "Oriental Spices Tortilla.jpg"},
    {"name": "American BBQ Tortilla", "image": "American BBQ Tortilla.jpg"},
    {"name": "Salsa Jalapeno Tortilla", "image": "Salsa Jalapeno Tortilla.jpg"},
    {"name": "Blue Hot Habanero Tortilla", "image": "Blue Hot Habanero Tortilla.jpg"},
    {"name": "Milk", "image": "Milk.jpg"},
    {"name": "Salt", "image": "Salt.jpg"},
    {"name": "Coca Cola", "image": "Coca Cola.jpg"},
    {"name": "Coca Cola Zero", "image": "Coca Cola Zero.jpg"},
    {"name": "Sprite", "image": "sprite.jpg"},
    {"name": "Fanta", "image": "Fanta.jpg"},
    {"name": "Mezzo Mix", "image": "Mezzo Mix.jpg"},
    {"name": "Capri Sun Orange", "image": "Capri Sun Orange.jpg"},
    {"name": "Fuze Ice Tea", "image": "Fuze Ice Tea.jpg"},
    {"name": "Fuze Schwarzer Tea", "image": "Fuze Schwarzer Tea.jpg"},
    {"name": "Coca Cola 10l pack", "image": "Coca Cola 10L pack.jpg"},
    {"name": "Coca Cola Zero 10L Pack", "image": "Coca Cola Zero 10L Pack.jpg"},
    {"name": "Fanta 10L Pack", "image": "Fanta 10L Pack.jpg"},
    {"name": "Sprite 10L Pack", "image": "Sprite 10L Pack.jpg"},
    {"name": "Mezzo Mix 10L pack", "image": "Mezzo Mix 10L pack.jpg"},
    {"name": "Red Berries Bottle", "image": None},
    {"name": "Mango Passion Bottle", "image": None},
    {"name": "Popcorn Bottle", "image": None},
    {"name": "Cinnamon Roll Bottle", "image": None},
    {"name": "Pfirsich Bottle", "image": None},
    {"name": "Himbeere Bottle", "image": None},
    {"name": "Toilet Paper", "image": "Toilet Paper.jpg"},
    {"name": "Tissue Paper", "image": "Tissue Paper.jpg"},
    {"name": "Customer Tissue", "image": "Customer Tissue.jpg"},
    {"name": "Blue Tissue Roll for Kitchen", "image": "Blue Tissue Roll for Kitchen.jpg"},
    {"name": "Order Bag", "image": "Order Bag.jpg"},
    {"name": "Wet Wipes", "image": None},
    {"name": "Big Yellow Bucket", "image": "Big Yellow Bucket.jpg"},
    {"name": "Big Bucket Cap", "image": None},
    {"name": "Red Small Bucket", "image": "Red Small Bucket.jpg"},
    {"name": "Small Bucket Cap", "image": None},
    {"name": "Yellow Glass", "image": None},
    {"name": "Yellow Glass cap", "image": None},
    {"name": "Shake Glass", "image": None},
    {"name": "Shake Glass Cap", "image": None},
    {"name": "Straw", "image": "Straw.jpg.png"},
    {"name": "Crispy Frie Box", "image": "Crispy Frie Box.jpg"},
    {"name": "Cheese sauce small packing", "image": None},
    {"name": "Brownie Box", "image": None},
    {"name": "Washing Powder", "image": "Washing Powder.jpg"},
    {"name": "Floor Cleaner Liqued", "image": "Floor Cleaner Liqued.jpg"},
    {"name": "Kitchen Des Special Liqued", "image": None},
    {"name": "Dishwasher Liqued", "image": None},
    {"name": "Spunch", "image": "Spunch.jpg"},
    {"name": "Wipes", "image": "Wipes.jpg"},
    {"name": "Cleaner&Polish", "image": "Cleaner&Polish.jpg"},
    {"name": "EcoLab Cleaner", "image": None},
    {"name": "Handwash Liquid", "image": None},
    {"name": "Iron Sponge", "image": "Iron Sponge.jpg"},
    {"name": "Garbge Bag", "image": "Garbge Bag.jpg"},
    {"name": "Hand Gloves", "image": "Hand Gloves.jpg"},
    {"name": "Sirafan Speed", "image": "Sirafan Speed.jpg"},
    {"name": "Greasecutter Fast Foam", "image": "Greasecutter Fast Foam.jpg"},
    {"name": "Oil Big Can", "image": "Oil Big Can.jpg"},
    {"name": "Packing Sticker", "image": None},
    {"name": "Burger Paper", "image": "Burger Paper.jpg"},
    {"name": "Large Bucket Paper", "image": None},
    {"name": "Tablet Paper", "image": None},
    {"name": "Small Bucket Paper", "image": None},
]

# --- Welcome Page (as per your code) ---
if st.session_state.page == "welcome":
    image_path = "welcome.jpg"
    if os.path.exists(image_path):
        img = Image.open(image_path).convert("RGBA")
        st.image(img, use_column_width=True)
    else:
        st.warning(f"Welcome image not found at {image_path}. Please ensure it's in the correct directory.")
        st.title("Welcome to the Inventory App!") # Fallback title if image is missing

    if st.button("____________👉 Click to Continue____________", key="start"):
        st.session_state.page = "menu"
        st.rerun()

# --- Menu Page (as per your code) ---
elif st.session_state.page == "menu":
    st.title("📋 What would you like to do?")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📦Start Inventory", key="start_invr_button"):
            st.session_state.page = "inventory"
            st.rerun()
        elif st.button("🚫 Add Finished Item", key="add_finish_button"):
            st.session_state.page = "Add Finished Stock"
            st.rerun()
        elif st.button("📈Add new items in inventory list", key="add_item_button"):
            st.session_state.page = "Add Inventory Items"
            st.rerun()
    with col2:
        st.button("🛒 Make New Order", key="new_order_button")
        st.button("⚠️ Check Low Stock", key="low_stock_button")

# --- Inventory Page ---
elif st.session_state.page == "inventory":
    st.title("📦 Current Inventory Check")

    # The inventory_items list is used directly here as per your request
    # If you want new items added via "Add Inventory Items" to show up here,
    # you would need to modify the hardcoded list or load it dynamically.

    if 'index' not in st.session_state:
        st.session_state.index = 0

    if 'quantities' not in st.session_state:
        st.session_state.quantities = {}

    if 'skipped' not in st.session_state:
        st.session_state.skipped = []

    # Ensure we don't go out of bounds if rerun occurs after completion
    if st.session_state.index < len(inventory_items):
        current_item_data = inventory_items[st.session_state.index]

        st.subheader(f"Item: {current_item_data['name']}")

        if current_item_data['image'] and os.path.exists(current_item_data['image']):
            image = Image.open(current_item_data['image'])
            st.image(image, width=400)
        else:
            st.write(f"No image found for '{current_item_data['name']}'.")

        # Initialize the text input with its previously saved value or an empty string
        current_qty_value = st.session_state.quantities.get(current_item_data['name'], "")
        qty = st.text_input("Enter quantity:", value=current_qty_value, key=f"qty_input_{current_item_data['name']}")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            if st.button("Next", key=f"next_btn_{current_item_data['name']}"):
                st.session_state.quantities[current_item_data['name']] = qty.strip()
                st.session_state.index += 1
                st.rerun()
        with col2:
            if st.button("Skip", key=f"skip_btn_{current_item_data['name']}"):
                st.session_state.skipped.append(current_item_data['name'])
                st.session_state.quantities[current_item_data['name']] = "SKIPPED" # Mark as skipped
                st.session_state.index += 1
                st.rerun()
        with col3:
            if st.button("Back", key=f"back_btn_{current_item_data['name']}"):
                if st.session_state.index > 0:
                    st.session_state.quantities[current_item_data['name']] = qty.strip() # Save current value
                    st.session_state.index -= 1
                    st.rerun()
        with col4:
            if st.button("🏡 Main Menu", key=f"main_menu_btn_{current_item_data['name']}"):
                st.session_state.page = "menu"
                st.rerun()

    # --- After Inventory Scan Complete ---
    if st.session_state.index >= len(inventory_items):
        st.success("✅ Inventory complete!")
        st.write("### Collected Quantities:")
        if st.session_state.quantities:
            for item, q in st.session_state.quantities.items():
                if q != "SKIPPED": # Only show non-skipped items
                    st.write(f"- **{item}**: {q}")
            if st.session_state.skipped:
                st.write("### Skipped Items:")
                for item in st.session_state.skipped:
                    st.write(f"- {item}")
        else:
            st.write("No quantities collected yet.")

        if st.button("Back to Menu"):
            st.session_state.page = "menu"
            st.session_state.index = 0 # Reset index for next inventory run
            st.session_state.quantities = {} # Clear quantities
            st.session_state.skipped = [] # Clear skipped
            st.rerun()

# --- Add Finished Stock Page ---
elif st.session_state.page == "Add Finished Stock":
    st.title("🚫 Add Finished Stock")
    st.write("Please write the name of items you anticipate will be finished soon.")

    # Initialize a distinct session state variable for the input's value
    if "finished_item_name_input_value" not in st.session_state:
        st.session_state.finished_item_name_input_value = ""

    finish_item = st.text_input(
        "Write the name of item:",
        value=st.session_state.finished_item_name_input_value, # Controlled by session state
        key="add_finished_item_text_input_widget_key" # Unique key for the widget itself
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("💾 Save & Add Another"):
            if finish_item.strip() != "":
                with open(FINISHED_ITEMS_FILE, "a") as f:
                    f.write(finish_item.strip() + "\n")
                st.success(f"'{finish_item.strip()}' saved successfully!")
                # Clear the input by setting the session state variable
                st.session_state.finished_item_name_input_value = ""
                st.rerun() # Rerun to update the text input visually
            else:
                st.warning("Please write an item name before saving.")

    with col2:
        if st.button("🏡 Main Menu"):
            st.session_state.page = "menu"
            st.rerun()

# --- Add Inventory Items Page ---
elif st.session_state.page == "Add Inventory Items":
    st.title("📈 Add New Inventory Items")
    st.write("Please write the name of items that are new in stock. Please do not try to re-add the name of items already in the Inventory List.")

    # Load or initialize the persistent inventory dictionary
    # This dictionary is separate from the hardcoded `inventory_items` list
    if os.path.exists(INVENTORY_DICT_FILE):
        with open(INVENTORY_DICT_FILE, "rb") as f:
            inventory_dynamic = pickle.load(f)
    else:
        inventory_dynamic = {} # Start with an empty dictionary if file doesn't exist

    # Initialize a distinct session state variable for the input's value
    if "new_inventory_item_input_value" not in st.session_state:
        st.session_state.new_inventory_item_input_value = ""

    new_item_name_input = st.text_input(
        "Enter new item name:",
        value=st.session_state.new_inventory_item_input_value, # Controlled by session state
        key="add_new_inventory_item_text_input_widget_key" # Unique key for the widget
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("💾 Save & Add Another"):
            if new_item_name_input.strip() != "":
                item_clean = new_item_name_input.strip().capitalize()

                if item_clean in inventory_dynamic:
                    st.error(f"'{item_clean}' already exists in the dynamic inventory list.")
                else:
                    # Add new item to the dynamic dictionary with default image "none"
                    inventory_dynamic[item_clean] = {"name": item_clean, "image": None} # Set image to None

                    # Save the updated dictionary back to the pickle file
                    with open(INVENTORY_DICT_FILE, "wb") as f:
                        pickle.dump(inventory_dynamic, f)

                    st.success(f"'{item_clean}' added to dynamic inventory with no image.")
                    # Clear the input by setting the session state variable
                    st.session_state.new_inventory_item_input_value = ""
                    st.rerun() # Rerun to update the text input visually
            else:
                st.warning("Please enter an item name.")

    with col2:
        if st.button("🏡 Main Menu"):
            st.session_state.page = "menu"
            st.rerun()
