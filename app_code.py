import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF
import os
import json
# --- Initialize session state early to avoid attribute errors ---


SAVE_FILE = "inventory_progress.json"

def save_progress():
    with open(SAVE_FILE, "w") as f:
        json.dump(dict(st.session_state), f)

def load_progress():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            saved_data = json.load(f)
            for key, value in saved_data.items():
                st.session_state[key] = value
# --- Initialize session state early to avoid attribute errors ---
if "page" not in st.session_state:
    st.session_state.page = "welcome"
if "index" not in st.session_state:
    st.session_state.index = 0
if "phase" not in st.session_state:
    st.session_state.phase = "kitchen"
if "kitchen_data" not in st.session_state:
    st.session_state.kitchen_data = {}
if "store_data" not in st.session_state:
    st.session_state.store_data = {}
if "quantities" not in st.session_state:
    st.session_state.quantities = {}
if "skipped" not in st.session_state:
    st.session_state.skipped = []

# ✅ Load saved progress if available
load_progress()

inventory_items = [
{"name": "Wings", "image": "Wings.jpg"}, # Example path
{"name": "Filets", "image": "Filets.jpg"}, # Example path
{"name": "Fries", "image": "Fries.jpg"},
{"name": "Burger Buns", "image": "Burger Buns.jpg"}, # No image available
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
{"name": "Guttio", "image": "Giotto.jpg"},
{"name": "Dairy Cream", "image":"Dairy Cream.jpg" },
{"name": "Dark Chocolate Sauce", "image": "Dark Chocolate Sauce.jpg"},
{"name": "Jalapenos can", "image": "Jalapenos can.jpg"},
{"name": "Coleslaw", "image": "Coleslaw.jpg"},
{"name": "gurke can", "image": "gurke.jpg"},
{"name": "Rosmery Katchup bottle", "image": "Rosmary Ketchup.jpg"},
{"name": "Cheese Sauce Bottle ", "image": "Cheese Sauce.jpg"},
{"name": "Extra Cheese Sauce Bottle ", "image": "Extra Cheese Sauce .jpg"},
{"name": "Harissa Sauce Bottle ", "image": "Harisa Sauce.jpg"},
{"name": " BBQ Becon Sauce Bottle ", "image": "BBQ Becon Sauce.jpg"},
{"name": "Truffle Sauce Bottle ", "image": "Truffle Sacue.jpg"},
{"name": "Sweet Jalapenu Sauce", "image": "Sweet Jalapenu Sauce.jpg"},
{"name": "Harissa Mayo", "image": "Harisa Mayo.jpg"},
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
{"name": "Red Fruits Tea Bottle", "image": "Red Fruits.jpg"},
{"name": "Mango Passion Tea Bottle", "image": "Mango Passion.jpg"},
{"name": "Popcorn Tea Bottle", "image": "Popcorn Tea.jpg"},
{"name": "Cinnamon Roll  Tea Bottle", "image": "Cinnamon Roll Tea.jpg"},
{"name": "Pfirsich Tea Bottle", "image": "Pfirsich Tea.jpg"},
{"name": "Himbeere Tea Bottle", "image": "Himbeer Tea.jpg"},
{"name": "Toilet Paper", "image": "Toilet Paper.jpg"},
{"name": "Tissue Paper", "image": "Tissue Paper.jpg"},
{"name": "Customer Tissue", "image": "Customer Tissue.jpg"},
{"name": "Blue Tissue Roll for Kitchen", "image": "Blue Tissue Roll for Kitchen.jpg"},
{"name": "Order Bag", "image": "Order Bag.jpg"},
{"name": "Wet Wipes", "image": "Wet Wipe.jpg"},
{"name": "Yellow Large Bucket", "image": "Big Yellow Bucket.jpg"},
{"name": "Yellow Large Bucket Cap", "image": "Large Bucket Cap.jpg"},
{"name": "Red Small Bucket", "image": "Red Small Bucket.jpg"},
{"name": "Red Small Bucket Cap", "image": "Small Bucket Cap.jpg"},
{"name": "Yellow Glass", "image": "Yellow Glass.jpg"},
{"name": "Yellow Glass cap", "image": "Yellow Glass Cap.jpg"},
{"name": "Shake Glass", "image": "Shake Glass.jpg"},
{"name": "Shake Glass Cap", "image": "Shake Glass Cap.jpg"},
{"name": "Straw", "image": "Straws.jpg"},
{"name": "Crispy Frie Box", "image": "Crispy Frie Box.jpg"},
{"name": "Extra Cheese sauce small packing", "image": "Extra Cheese Sauce Packing .jpg"},
{"name": "Brownie Box", "image": "Brownie Box.jpg"},
{"name": "Washing Powder", "image": "Washing Powder.jpg"},
{"name": "Floor Cleaner Liqued", "image": "Floor Cleaner Liqued.jpg"},
{"name": "Kitchen Dishwashing Liquid", "image": "Kitchen Dishwashing Liquid.jpg"},
{"name": "Dishwasher Liqued", "image": "Dishwasher Liquid.jpg"},
{"name": "Spunch", "image": "Spunch.jpg"},
{"name": "Wipes", "image": "Wipes.jpg"},
{"name": "Cleaner&Polish", "image": "Cleaner&Polish.jpg"},
{"name": "EcoLab Toilet Cleaner", "image": "EcoLab Toilot Cleaner.jpg"},
{"name": "Handwash Liquid", "image":"Hand Wash.jpg"},
{"name": "Iron Sponge", "image": "Iron Sponge.jpg"},
{"name": "Garbge Bag", "image": "Garbge Bag.jpg"},
{"name": "Hand Gloves", "image": "Hand Gloves.jpg"},
{"name": "Sirafan Speed", "image": "Sirafan Speed.jpg"},
{"name": "Greasecutter Fast Foam", "image": "Greasecutter Fast Foam.jpg"},
{"name": "Oil Big Can", "image": "Oil Big Can.jpg"},
{"name": "Loco Sticker", "image": "Loco Sticker.jpg"},
{"name": "Burger Paper", "image": "Burger Paper.jpg"},
{"name": "Large Bucket Paper", "image": "Large Bucket Paper .jpg"},
{"name": "Tablet Paper", "image": "Tablet Paper.jpg"},
{"name": "Small Bucket Paper", "image": "Small Bucket Paper.jpg"},
{"name": "Chocolate Frappe Base", "image":"Chocolate Frappe Base.jpg"},
{"name": "Vanila Frappe Base", "image":"Vanila Frappe Base.jpg"},
{"name": "Disposable fork", "image":"disposable fork.jpg"},
{"name": "Brownie Box paper", "image":"Small Bucket Paper.jpg"},
{"name": "Glass Cleaner", "image":"Glass Cleaner.jpg"}
    ]
store_inventory_items = inventory_items.copy()
kitchen_item_names = item_names = ["Wings", "Filets", "Fries", "Burger Buns", "Potato Pops", "Onion Rings", "chicken Nugets Pops", "Chili Cheese Nugets", "Becons", "Churros", "Brownies", "Choclate Fudge Cookies", "White Macadaima cookies", "Nutella", "Oreo Biscuts", "Guttio", "Dairy Cream", "Dark Chocolate Sauce", "Jalapenos can", "Coleslaw","gurke can",
"Rosmery Katchup bottle", "Cheese Sauce Bottle ", "Extra Cheese Sauce Bottle ", "Harisa Sauce Bottle ", " BBQ Becon Sauce Bottle ", "Truffle Sauce Bottle ", "Sweet Jalapenu Sauce", "Harisa Mayo", "Garlic Mayo", "Hot Chili Sauce", "Rosmary Katchup Sauce", "BBQ Sauce", "Truffle Aloi", "white Truffle Flavour", "Garlic Cheese Flavour", "American BBQ Flavour ", "Korean Spice Flavour ", "Salse Jalapeno Flavour", "Sweet Chili Flavour", "Blue Hot Habanero Flavour", "Classic Cheese Tortilla", "Sweet Chili Tortilla", "Oriental Spices Tortilla", "American BBQ Tortilla", "Salsa Jalapeno Tortilla", "Blue Hot Habanero Tortilla", "Milk", "Coca Cola", "Coca Cola Zero", "Sprite", "Fanta", "Mezzo Mix", "Capri Sun Orange", "Fuze Ice Tea", "Fuze Schwarzer Tea", "Red Fruits Tea Bottle", "Mango Passion Tea Bottle", "Popcorn Tea Bottle", "Cinnamon Roll  Tea Bottle", "Pfirsich Tea Bottle", "Himbeere Tea Bottle", "Customer Tissue", "Blue Tissue Roll for Kitchen", "Order Bag", "Wet Wipes", "Yellow Large Bucket", "Yellow Large Bucket Cap", "Red Small Bucket", "Red Small Bucket Cap", "Yellow Glass", "Yellow Glass cap", "Shake Glass", "Shake Glass Cap", "Straw", "Crispy Frie Box", "Extra Cheese sauce small packing", "Brownie Box", "Cleaner&Polish", "Garbge Bag", "Hand Gloves", "Sirafan Speed", "Greasecutter Fast Foam", "Loco Sticker", "Large Bucket Paper", "Tablet Paper", "Small Bucket Paper", "Chocolate Frappe Base", "Vanila Frappe Base", "Disposable fork", "Brownie Box paper"
]

kitchen_inventory_items = [item for item in store_inventory_items if item["name"] in kitchen_item_names]

if "page" not in st.session_state:
    st.session_state.page = "welcome"

if st.session_state.page == "welcome":
    image_path = "welcome.jpg"
    img = Image.open(image_path).convert("RGBA")
    st.image(img, use_column_width=True)

    if st.button("____________👉 Click to Continue____________", key="start"):
        st.session_state.page = "menu"
        st.rerun()

elif st.session_state.page == "menu":
    st.title("📋 What would you like to do?")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📦Start Inventory", key="start_invr_button"):
            st.session_state.page = "inventory" # Corrected assignment
            st.rerun()
    with col2:
        if st.button("🛒 Make New Order", key="new_order_button"):
            st.session_state.page = "New Stock"
            st.rerun()

elif st.session_state.page == "inventory":
    st.title("📋 Inventory App")

    # --- Transition if kitchen is done ---
    if st.session_state.index >= len(kitchen_inventory_items):
        st.success("✅ Kitchen inventory complete.")
        if st.button("👉 Continue to Store Inventory"):
            st.session_state.phase = "store"
            st.session_state.index = 0
            st.rerun()
    else:
       # Normal kitchen item input flow here
    if st.session_state.phase == "kitchen":
        st.header("🍳 Step 1: Enter Kitchen Inventory")
        if st.session_state.index < len(inventory_items):
            item = inventory_items[st.session_state.index]
            st.subheader(f"Item: {item['name']}")
            if item['image'] and os.path.exists(item['image']):
                st.image(item['image'], width=250)
            qty = st.text_input("Enter quantity:", value=st.session_state.get(item['name'], ""), key=item['name'])

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                if st.button("Save & Next"):
                    st.session_state.kitchen_data[item['name']] = qty
                    st.session_state.index += 1
                    save_progress()
                    st.rerun()
            with col2:
                if st.button("Back") and st.session_state.index > 0:
                    st.session_state.index -= 1
                    st.rerun()
            with col3:
                if st.button("Reset Progress"):
                    if os.path.exists(SAVE_FILE):
                        os.remove(SAVE_FILE)
                    st.session_state.clear()
                    st.rerun()
            with col4:
                if st.button("🏡 Main Menu"):
                    st.session_state.page = "menu"
                    st.rerun()

    elif st.session_state.phase == "store":
        st.header("🏬 Step 2: Complete Store Inventory")
        if st.session_state.index < len(inventory_items):
            item = inventory_items[st.session_state.index]
            name = item['name']
            st.subheader(f"Item: {name}")
            if item['image'] and os.path.exists(item['image']):
                st.image(item['image'], width=250)
            prev_kitchen = st.session_state.kitchen_data.get(name)
            if prev_kitchen:
                st.info(f"Kitchen quantity previously entered: {prev_kitchen}")
            qty = st.text_input("Enter final store quantity:", value=st.session_state.get("store_" + name, ""), key="store_" + name)

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                if st.button("Next"):
                    st.session_state.store_data[name] = qty
                    st.session_state.index += 1
                    st.rerun()
            with col2:
                if st.button("Back") and st.session_state.index > 0:
                    st.session_state.index -= 1
                    st.rerun()
            with col3:
                if st.button("Reset Progress"):
                    if os.path.exists(SAVE_FILE):
                        os.remove(SAVE_FILE)
                    st.session_state.clear()
                    st.rerun()
            with col4:
                if st.button("🏡 Main Menu"):
                    st.session_state.page = "menu"
                    st.rerun()
        else:
            st.success("🎉 All inventory completed. Showing final result...")
            st.session_state.phase = "done"
            st.rerun()

    elif st.session_state.phase == "done":
        st.header("📦 Final Store Inventory")
        final_result = st.session_state.store_data
        for name, value in final_result.items():
            st.write(f"**{name}**: {value}")

        def generate_pdf(data_dict):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Final Store Inventory", ln=True, align='C')
            pdf.ln(10)
            for item, val in data_dict.items():
                pdf.cell(200, 10, txt=f"{item}: {val}", ln=True)
            return pdf.output(dest="S").encode("latin-1")

        pdf_bytes = generate_pdf(final_result)
        st.download_button(
            label="📄 Download Inventory as PDF",
            data=pdf_bytes,
            file_name="Store_Inventory.pdf",
            mime="application/pdf"
        )

        if st.button("🔁 Restart Inventory"):
            for key in ["phase", "kitchen_data", "store_data", "index"]:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

elif st.session_state.page == "New Stock":
    if st.session_state.index >= len(inventory_items):
        st.success("📦🛒🛍️ List is ready for order New Items. Best Luck!")
        if st.button("Back to Menu"):
            st.session_state.page = "menu"
            st.session_state.index = 0
            st.session_state.quantities = {}
            st.session_state.skipped = []
            st.rerun()

        st.write("### Collected Quantities:")
        for item, q in st.session_state.quantities.items():
            st.write(f"- {item}: {q}")

        def generate_inventory_pdf(data_dict):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Inventory Quantities", ln=True, align='C')
            pdf.ln(10)
            for item, qty in data_dict.items():
                pdf.cell(200, 10, txt=f"{item}: {qty}", ln=True)
            return pdf.output(dest="S").encode("latin-1")

        pdf_data = generate_inventory_pdf(st.session_state.quantities)
        st.download_button(
            label="📄 Download Inventory Summary as PDF",
            data=pdf_data,
            file_name="Inventory_Summary.pdf",
            mime="application/pdf"
        )
    else:
        current_item = inventory_items[st.session_state.index]
        st.subheader(f"Item: {current_item['name']}")
        if current_item['image'] and os.path.exists(current_item['image']):
            st.image(current_item['image'], width=250)
        qty = st.text_input("Enter quantity:", value=st.session_state.get(current_item['name'], ""), key=current_item['name'])

        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            if st.button("Save & Next"):
                st.session_state.quantities[current_item['name']] = qty
                st.session_state.index += 1
                save_progress()
                st.rerun()
        with col2:
            if st.button("Skip"):
                st.session_state.skipped.append(current_item['name'])
                st.session_state.index += 1
                st.rerun()
        with col3:
            if st.button("Back"):
                if st.session_state.index > 0:
                    st.session_state.index -= 1
                    st.rerun()
        with col4:
            if st.button("Reset Progress"):
                if os.path.exists(SAVE_FILE):
                    os.remove(SAVE_FILE)
                st.session_state.clear()
                st.rerun()
        with col5:
            if st.button("🏡 Main Menu"):
                st.session_state.page = "menu"
                st.rerun()
