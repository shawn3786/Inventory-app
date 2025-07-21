import streamlit as st
from PIL import Image
from fpdf import FPDF
import os
import json

INVENTORY_SAVE_FILE = "inventory_progress.json"
ORDER_SAVE_FILE = "order_progress.json"

# ✅ Load saved inventory progress safely
def load_inventory_progress():
    if os.path.exists(INVENTORY_SAVE_FILE):
        try:
            with open(INVENTORY_SAVE_FILE, "r") as f:
                saved_data = json.load(f)
                # Only load inventory-related data
                inventory_keys = ["phase", "index", "kitchen_data", "store_data"]
                for key, value in saved_data.items():
                    if key in inventory_keys:
                        st.session_state[key] = value
        except (json.JSONDecodeError, ValueError):
            os.remove(INVENTORY_SAVE_FILE)
            st.warning("⚠️ Corrupted inventory file removed.")

# ✅ Save inventory progress
def save_inventory_progress():
    with open(INVENTORY_SAVE_FILE, "w") as f:
        json.dump({
            "phase": st.session_state.phase,
            "index": st.session_state.index,
            "kitchen_data": st.session_state.kitchen_data,
            "store_data": st.session_state.store_data,
        }, f)

# ✅ Load saved order progress safely
def load_order_progress():
    if os.path.exists(ORDER_SAVE_FILE):
        try:
            with open(ORDER_SAVE_FILE, "r") as f:
                saved_data = json.load(f)
                st.session_state.order_data = saved_data.get("order_data", {})
                st.session_state.order_index = saved_data.get("order_index", 0)
        except (json.JSONDecodeError, ValueError):
            os.remove(ORDER_SAVE_FILE)
            st.warning("⚠️ Corrupted order file removed.")

# ✅ Save order progress
def save_order_progress():
    with open(ORDER_SAVE_FILE, "w") as f:
        json.dump({
            "order_data": st.session_state.order_data,
            "order_index": st.session_state.order_index,
        }, f)

# ✅ Clear order progress
def clear_order_progress():
    if os.path.exists(ORDER_SAVE_FILE):
        os.remove(ORDER_SAVE_FILE)
    st.session_state.order_data = {}
    st.session_state.order_index = 0

# ✅ Initialize session_state first, then load progress
if "page" not in st.session_state:
    st.session_state.page = "welcome"
if "phase" not in st.session_state:
    st.session_state.phase = "kitchen"
if "index" not in st.session_state:
    st.session_state.index = 0
if "kitchen_data" not in st.session_state:
    st.session_state.kitchen_data = {}
if "store_data" not in st.session_state:
    st.session_state.store_data = {}
if "quantities" not in st.session_state:
    st.session_state.quantities = {}
if "skipped" not in st.session_state:
    st.session_state.skipped = []
if "order_data" not in st.session_state:
    st.session_state.order_data = {}
if "order_index" not in st.session_state:
    st.session_state.order_index = 0

# ✅ Only load order progress automatically (inventory will load on demand)
load_order_progress()
inventory_items = [
    {"name": "Wings", "image": "Wings.jpg"},
    {"name": "Filets", "image": "Filets.jpg"},
    {"name": "Fries", "image": "Fries.jpg"},
    {"name": "Burger Buns", "image": "Burger Buns.jpg"},
    {"name": "Potato Pops", "image": "Potato Pops.jpg"},
    {"name": "Onion Rings", "image": "Onion Rings.jpg"},
    {"name": "chicken Nugets Pops", "image": "Chicken Nugets.jpg"},
    {"name": "Chili Cheese Nugets", "image": "Chili Cheese Nugets.jpg"},
    {"name": "Becons", "image": "Becons.jpg"},
    {"name": "Churros", "image": "churros.jpg"},
    {"name": "Brownies", "image": "Brownies.jpg"},
    {"name": "Choclate Fudge Cookies", "image": "Choclate Fudge Cookies.jpg"},
    {"name": "White Macadaima cookies", "image": "White Macadaima cookies.jpg"},
    {"name": "Pink Onion", "image": "Pink Onion.jpg"},
    {"name": "Waffles", "image": "Waffles.jpg"},
    {"name": "Green Onion", "image": "green Onion.jpg"},
    {"name": "Nutella", "image": "Nutella.jpg"},
    {"name": "Oreo Biscuts", "image": "Oreo Biscuts.jpg"},
    {"name": "Guttio", "image": "Giotto.jpg"},
    {"name": "Dairy Cream", "image": "Dairy Cream.jpg"},
    {"name": "Dark Chocolate Sauce", "image": "Dark Chocolate Sauce.jpg"},
    {"name": "Jalapenos can", "image": "Jalapenos can.jpg"},
    {"name": "Coleslaw", "image": "Coleslaw.jpg"},
    {"name": "gurke can", "image": "gurke.jpg"},
    {"name": "Rosmery Katchup bottle", "image": "Rosmary Ketchup.jpg"},
    {"name": "Cheese Sauce Bottle", "image": "Cheese Sauce.jpg"},
    {"name": "Extra Cheese Sauce Bottle", "image": "Extra Cheese Sauce Bottle.jpg"},
    {"name": "Harisa Sauce Bottle", "image": "Harisa Sauce Bottle.jpg"},
    {"name": "BBQ Becon Sauce Bottle", "image": "BBQ Becon Sauce Bottle.jpg"},
    {"name": "Truffle Sauce Bottle", "image": "Truffle Sauce Bottle.jpg"},
    {"name": "Sweet Jalapenu Sauce", "image": "Sweet Jalapenu Sauce.jpg"},
    {"name": "Harisa Mayo", "image": "Harisa Mayo.jpg"},
    {"name": "Garlic Mayo", "image": "Garlic Mayo.jpg"},
    {"name": "Hot Chili Sauce", "image": "Hot Chili Sauce.jpg"},
    {"name": "Rosmary Katchup Sauce", "image": "Rosmary Katchup Sauce.jpg"},
    {"name": "BBQ Sauce", "image": "BBQ Sauce.jpg"},
    {"name": "Truffle Aloi", "image": "Truffle Aloi.jpg"},
    {"name": "white Truffle Flavour", "image": "white Truffle Flavour.jpg"},
    {"name": "Garlic Cheese Flavour", "image": "Garlic Cheese Flavour.jpg"},
    {"name": "American BBQ Flavour", "image": "American BBQ Flavour.jpg"},
    {"name": "Korean Spice Flavour", "image": "Korean Spice Flavour.jpg"},
    {"name": "Salse Jalapeno Flavour", "image": "Salse Jalapeno Flavour.jpg"},
    {"name": "Sweet Chili Flavour", "image": "Sweet Chili Flavour.jpg"},
    {"name": "Blue Hot Habanero Flavour", "image": "Blue Hot Habanero Flavour.jpg"},
    {"name": "Classic Cheese Tortilla", "image": "Classic Cheese Tortilla.jpg"},
    {"name": "Sweet Chili Tortilla", "image": "Sweet Chili Tortilla.jpg"},
    {"name": "Oriental Spices Tortilla", "image": "Oriental Spices Tortilla.jpg"},
    {"name": "American BBQ Tortilla", "image": "American BBQ Tortilla.jpg"},
    {"name": "Salsa Jalapeno Tortilla", "image": "Salsa Jalapeno Tortilla.jpg"},
    {"name": "Blue Hot Habanero Tortilla", "image": "Blue Hot Habanero Tortilla.jpg"},
    {"name": "Milk", "image": "Milk.jpg"},
    {"name": "Coca Cola", "image": "Coca Cola.jpg"},
    {"name": "Coca Cola Zero", "image": "Coca Cola Zero.jpg"},
    {"name": "Sprite", "image": "Sprite.jpg"},
    {"name": "Fanta", "image": "Fanta.jpg"},
    {"name": "Mezzo Mix", "image": "Mezzo Mix.jpg"},
    {"name": "Capri Sun Orange", "image": "Capri Sun Orange.jpg"},
    {"name": "Fuze Ice Tea", "image": "Fuze Ice Tea.jpg"},
    {"name": "Fuze Schwarzer Tea", "image": "Fuze Schwarzer Tea.jpg"},
    {"name": "Red Fruits Tea Bottle", "image": "Red Fruits Tea Bottle.jpg"},
    {"name": "Mango Passion Tea Bottle", "image": "Mango Passion Tea Bottle.jpg"},
    {"name": "Popcorn Tea Bottle", "image": "Popcorn Tea Bottle.jpg"},
    {"name": "Cinnamon Roll Tea Bottle", "image": "Cinnamon Roll Tea Bottle.jpg"},
    {"name": "Pfirsich Tea Bottle", "image": "Pfirsich Tea Bottle.jpg"},
    {"name": "Himbeere Tea Bottle", "image": "Himbeere Tea Bottle.jpg"},
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
    {"name": "Handwash Liquid", "image": "Hand Wash.jpg"},
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
    {"name": "Chocolate Frappe Base", "image": "Chocolate Frappe Base.jpg"},
    {"name": "Vanila Frappe Base", "image": "Vanila Frappe Base.jpg"},
    {"name": "Disposable fork", "image": "disposable fork.jpg"},
    {"name": "Brownie Box paper", "image": "Small Bucket Paper.jpg"},
    {"name": "Glass Cleaner", "image": "Glass Cleaner.jpg"}
]

store_inventory_items = inventory_items.copy()
kitchen_item_names = ["Wings", "Filets", "Fries", "Burger Buns", "Potato Pops", "Onion Rings", "chicken Nugets Pops", "Chili Cheese Nugets", "Becons", "Churros", "Brownies", "Choclate Fudge Cookies", "White Macadaima cookies", "Nutella", "Oreo Biscuts", "Guttio", "Dairy Cream", "Dark Chocolate Sauce", "Jalapenos can", "Coleslaw", "gurke can", "Rosmery Katchup bottle", "Cheese Sauce Bottle", "Extra Cheese Sauce Bottle", "Harisa Sauce Bottle", "BBQ Becon Sauce Bottle", "Truffle Sauce Bottle", "Sweet Jalapenu Sauce", "Harisa Mayo", "Garlic Mayo", "Hot Chili Sauce", "Rosmary Katchup Sauce", "BBQ Sauce", "Truffle Aloi", "white Truffle Flavour", "Garlic Cheese Flavour", "American BBQ Flavour", "Korean Spice Flavour", "Salse Jalapeno Flavour", "Sweet Chili Flavour", "Blue Hot Habanero Flavour", "Classic Cheese Tortilla", "Sweet Chili Tortilla", "Oriental Spices Tortilla", "American BBQ Tortilla", "Salsa Jalapeno Tortilla", "Blue Hot Habanero Tortilla", "Milk", "Coca Cola", "Coca Cola Zero", "Sprite", "Fanta", "Mezzo Mix", "Capri Sun Orange", "Fuze Ice Tea", "Fuze Schwarzer Tea", "Red Fruits Tea Bottle", "Mango Passion Tea Bottle", "Popcorn Tea Bottle", "Cinnamon Roll Tea Bottle", "Pfirsich Tea Bottle", "Himbeere Tea Bottle", "Customer Tissue", "Blue Tissue Roll for Kitchen", "Order Bag", "Wet Wipes", "Yellow Large Bucket", "Yellow Large Bucket Cap", "Red Small Bucket", "Red Small Bucket Cap", "Yellow Glass", "Yellow Glass cap", "Shake Glass", "Shake Glass Cap", "Straw", "Crispy Frie Box", "Extra Cheese sauce small packing", "Brownie Box", "Cleaner&Polish", "Garbge Bag", "Hand Gloves", "Sirafan Speed", "Greasecutter Fast Foam", "Loco Sticker", "Large Bucket Paper", "Tablet Paper", "Small Bucket Paper", "Chocolate Frappe Base", "Vanila Frappe Base", "Disposable fork", "Brownie Box paper"]

kitchen_inventory_items = [item for item in store_inventory_items if item["name"] in kitchen_item_names]

# ---------------------- Welcome Page ----------------------
if st.session_state.page == "welcome":
    if os.path.exists("welcome.jpg"):
        st.image("welcome.jpg", use_column_width=True)
    if st.button("____________👉 Click to Continue____________", key="start"):
        st.session_state.page = "menu"
        st.rerun()

# ---------------------- Menu Page ----------------------
elif st.session_state.page == "menu":
    st.title("📋 What would you like to do?")
    # Check if there's existing inventory progress
    has_inventory_progress = os.path.exists(INVENTORY_SAVE_FILE)
    
    if has_inventory_progress:
        st.info("📋 Previous inventory progress found!")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📦 Start Fresh Inventory", key="start_fresh_invr_button"):
                # Clear the inventory progress file completely when starting fresh
                if os.path.exists(INVENTORY_SAVE_FILE):
                    os.remove(INVENTORY_SAVE_FILE)
                st.session_state.page = "inventory"
                st.session_state.phase = "kitchen"
                st.session_state.index = 0
                # Clear any existing progress
                st.session_state.kitchen_data = {}
                st.session_state.store_data = {}
                save_inventory_progress()
                st.rerun()
        with col2:
            if st.button("🔄 Continue Previous Inventory", key="continue_invr_button"):
                # Load previous progress and continue
                load_inventory_progress()
                st.session_state.page = "inventory"
                st.rerun()
        with col3:
            if st.button("🛒 Make New Order", key="new_order_button"):
                st.session_state.page = "New Stock"
                st.session_state.order_index = 0
                st.rerun()
    else:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📦 Start Inventory", key="start_invr_button"):
                st.session_state.page = "inventory"
                st.session_state.phase = "kitchen"
                st.session_state.index = 0
                # Clear any existing progress
                st.session_state.kitchen_data = {}
                st.session_state.store_data = {}
                save_inventory_progress()
                st.rerun()
        with col2:
            if st.button("🛒 Make New Order", key="new_order_button"):
                st.session_state.page = "New Stock"
                st.session_state.order_index = 0
                st.rerun()

# ---------------------- New Order Page ----------------------
elif st.session_state.page == "New Stock":
    st.header("🛒 New Order - Add Items to Order List")

    # Initialize order data if not exists
    if "order_data" not in st.session_state:
        st.session_state.order_data = {}
    if "order_index" not in st.session_state:
        st.session_state.order_index = 0

    if st.session_state.order_index < len(inventory_items):
        item = inventory_items[st.session_state.order_index]
        st.subheader(f"Item {st.session_state.order_index + 1} of {len(inventory_items)}: {item['name']}")

        image_path = f"resized_for_streamlit/{item['image']}"
        if item['image'] and os.path.exists(image_path):
            st.image(image_path, width=250)
        else:
            st.warning("📷 Image not found.")

        # Show current order quantity if exists
        current_qty = st.session_state.order_data.get(item['name'], "")

        qty = st.text_input(
            "Enter quantity to order (leave empty to skip):", 
            value=current_qty,
            key=f"order_qty_{st.session_state.order_index}"
        )

        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            if st.button("Next", key=f"order_next_{st.session_state.order_index}"):
                if qty.strip():  # Only add to order if quantity is provided
                    st.session_state.order_data[item['name']] = qty
                st.session_state.order_index += 1
                save_order_progress()
                st.rerun()

        with col2:
            if st.button("Back", key=f"order_back_{st.session_state.order_index}"):
                if st.session_state.order_index > 0:
                    st.session_state.order_index -= 1
                    save_order_progress()
                    st.rerun()

        with col3:
            if st.button("Skip Item", key=f"order_skip_{st.session_state.order_index}"):
                st.session_state.order_index += 1
                save_order_progress()
                st.rerun()

        with col4:
            if st.button("🗑️ Clear Order", key=f"order_clear_{st.session_state.order_index}"):
                clear_order_progress()
                st.success("✅ Order data cleared!")
                st.rerun()

        with col5:
            if st.button("🏡 Main Menu", key=f"order_menu_{st.session_state.order_index}"):
                st.session_state.page = "menu"
                st.rerun()

        # Show progress
        progress = (st.session_state.order_index / len(inventory_items)) * 100
        st.progress(progress / 100)
        st.write(f"Progress: {st.session_state.order_index}/{len(inventory_items)} items ({progress:.1f}%)")

    else:
        # Show final order summary
        st.success("🎉 Order list complete!")
        st.header("📋 Your Order Summary")

        if st.session_state.order_data:
            total_items = 0
            for item_name, quantity in st.session_state.order_data.items():
                st.write(f"**{item_name}**: {quantity}")
                try:
                    total_items += int(quantity) if quantity.isdigit() else 0
                except:
                    pass

            st.info(f"**Total items to order: {total_items}**")

            # Generate PDF for order
            def generate_order_pdf(order_dict):
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.cell(200, 10, txt="New Stock Order List", ln=True, align='C')
                pdf.ln(10)

                total = 0
                for item, qty in order_dict.items():
                    pdf.cell(200, 10, txt=f"{item}: {qty}", ln=True)
                    try:
                        total += int(qty) if qty.isdigit() else 0
                    except:
                        pass

                pdf.ln(10)
                pdf.cell(200, 10, txt=f"Total Items: {total}", ln=True)
                return pdf.output(dest="S").encode("latin-1")

            pdf_bytes = generate_order_pdf(st.session_state.order_data)

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.download_button(
                    label="📄 Download Order List as PDF",
                    data=pdf_bytes,
                    file_name="New_Stock_Order.pdf",
                    mime="application/pdf"
                )

            with col2:
                if st.button("🔁 Create New Order"):
                    clear_order_progress()
                    st.rerun()

            with col3:
                if st.button("🗑️ Reset Order Data"):
                    clear_order_progress()
                    st.success("✅ Order data cleared!")
                    st.rerun()

            with col4:
                if st.button("🏡 Back to Menu"):
                    st.session_state.page = "menu"
                    st.rerun()

        else:
            st.warning("No items were added to the order.")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🏡 Back to Menu"):
                    st.session_state.page = "menu"
                    st.rerun()
            with col2:
                if st.button("🗑️ Reset Order Data"):
                    clear_order_progress()
                    st.success("✅ Order data cleared!")
                    st.rerun()

# ---------------------- Inventory Flow ----------------------
elif st.session_state.page == "inventory":

    # Phase 1: Kitchen Inventory
    if st.session_state.phase == "kitchen":
        st.header("🍳 Step 1: Enter Kitchen Inventory")
        kitchen_items = kitchen_inventory_items

        # Debug info to see what's happening
        st.write(f"Debug: Current index: {st.session_state.index}, Total kitchen items: {len(kitchen_items)}")

        if st.session_state.index < len(kitchen_items):
            item = kitchen_items[st.session_state.index]
            st.subheader(f"Item {st.session_state.index + 1} of {len(kitchen_items)}: {item['name']}")

            image_path = f"resized_for_streamlit/{item['image']}"
            if item['image'] and os.path.exists(image_path):
                st.image(image_path, width=250)
            else:
                st.warning("📷 Image not found.")

            qty = st.text_input(
                "Enter quantity:", 
                value=st.session_state.kitchen_data.get(item['name'], ""), 
                key=f"kitchen_qty_{st.session_state.index}"
            )

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                if st.button("Save & Next", key=f"kitchen_next_{st.session_state.index}"):
                    st.session_state.kitchen_data[item['name']] = qty
                    st.session_state.index += 1
                    save_inventory_progress()
                    st.rerun()
            with col2:
                if st.button("Back", key=f"kitchen_back_{st.session_state.index}"):
                    if st.session_state.index > 0:
                        st.session_state.index -= 1
                        save_inventory_progress()
                        st.rerun()
            with col3:
                if st.button("🗑️ Reset All", key=f"kitchen_reset_{st.session_state.index}"):
                    if os.path.exists(INVENTORY_SAVE_FILE):
                        os.remove(INVENTORY_SAVE_FILE)
                    # Reset all session state properly
                    st.session_state.page = "menu"
                    st.session_state.phase = "kitchen"
                    st.session_state.index = 0
                    st.session_state.kitchen_data = {}
                    st.session_state.store_data = {}
                    st.success("✅ All inventory data cleared!")
                    st.rerun()
            with col4:
                if st.button("🏡 Main Menu", key=f"kitchen_menu_{st.session_state.index}"):
                    st.session_state.page = "menu"
                    save_inventory_progress()
                    st.rerun()
        else:
            st.success("✅ Kitchen inventory complete.")
            if st.button("👉 Continue to Store Inventory", key="continue_to_store"):
                st.session_state.phase = "store"
                st.session_state.index = 0
                save_inventory_progress()
                st.rerun()

    # Phase 2: Store Inventory
    elif st.session_state.phase == "store":
        st.header("🏬 Step 2: Complete Store Inventory")
        if st.session_state.index < len(inventory_items):
            item = inventory_items[st.session_state.index]
            name = item['name']
            st.subheader(f"Item {st.session_state.index + 1} of {len(inventory_items)}: {name}")

            image_path = f"resized_for_streamlit/{item['image']}"
            if item['image'] and os.path.exists(image_path):
                st.image(image_path, width=250)
            else:
                st.warning("📷 Image not found.")

            prev_kitchen = st.session_state.kitchen_data.get(name)
            if prev_kitchen:
                st.info(f"Kitchen quantity previously entered: {prev_kitchen}")

            qty = st.text_input(
                "Enter final store quantity:", 
                value=st.session_state.store_data.get(name, ""), 
                key=f"store_qty_{st.session_state.index}"
            )

            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                if st.button("Next", key=f"store_next_{st.session_state.index}"):
                    st.session_state.store_data[name] = qty
                    st.session_state.index += 1
                    save_inventory_progress()
                    st.rerun()
            with col2:
                if st.button("Back", key=f"store_back_{st.session_state.index}"):
                    if st.session_state.index > 0:
                        st.session_state.index -= 1
                        save_inventory_progress()
                        st.rerun()
            with col3:
                if st.button("🗑️ Reset All", key=f"store_reset_{st.session_state.index}"):
                    if os.path.exists(INVENTORY_SAVE_FILE):
                        os.remove(INVENTORY_SAVE_FILE)
                    # Reset all session state properly
                    st.session_state.page = "menu"
                    st.session_state.phase = "kitchen"
                    st.session_state.index = 0
                    st.session_state.kitchen_data = {}
                    st.session_state.store_data = {}
                    st.success("✅ All inventory data cleared!")
                    st.rerun()
            with col4:
                if st.button("Reset Progress", key=f"store_reset_progress_{st.session_state.index}"):
                    if os.path.exists(INVENTORY_SAVE_FILE):
                        os.remove(INVENTORY_SAVE_FILE)
                    # Reset all session state properly
                    st.session_state.page = "menu"
                    st.session_state.phase = "kitchen"
                    st.session_state.index = 0
                    st.session_state.kitchen_data = {}
                    st.session_state.store_data = {}
                    st.rerun()
            with col5:
                if st.button("🏡 Main Menu", key=f"store_menu_{st.session_state.index}"):
                    st.session_state.page = "menu"
                    save_inventory_progress()
                    st.rerun()
        else:
            st.success("🎉 All inventory completed. Showing final result...")
            st.session_state.phase = "done"
            save_inventory_progress()
            st.rerun()

    # Phase 3: Done
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
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.download_button(
                label="📄 Download Inventory as PDF",
                data=pdf_bytes,
                file_name="Store_Inventory.pdf",
                mime="application/pdf"
            ):
                if os.path.exists(INVENTORY_SAVE_FILE):
                    os.remove(INVENTORY_SAVE_FILE)

        with col2:
            if st.button("🔁 Restart Inventory"):
                if os.path.exists(INVENTORY_SAVE_FILE):
                    os.remove(INVENTORY_SAVE_FILE)
                for key in ["phase", "kitchen_data", "store_data", "index"]:
                    if key in st.session_state:
                        del st.session_state[key]
                st.rerun()

        with col3:
            if st.button("🗑️ Reset All Data"):
                if os.path.exists(INVENTORY_SAVE_FILE):
                    os.remove(INVENTORY_SAVE_FILE)
                # Reset all session state properly
                st.session_state.page = "menu"
                st.session_state.phase = "kitchen"
                st.session_state.index = 0
                st.session_state.kitchen_data = {}
                st.session_state.store_data = {}
                st.success("✅ All inventory data cleared!")
                st.rerun()
