import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF
import os
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

elif  st.session_state.page == "inventory":
    store_inventory_items = [{"name": name, "image": img} for name, img in all_inventory_dict.items()]
    kitchen_item_names = ["Tomatoes", "Onions", "Garlic"]
    kitchen_inventory_items = [item for item in store_inventory_items if item["name"] in kitchen_item_names]

# --- Initialize session state ---
    if "phase" not in st.session_state:
        st.session_state.phase = "kitchen"
        st.session_state.kitchen_data = {}  # to store kitchen quantities
        st.session_state.store_data = {}    # to store final store quantities
        st.session_state.index = 0

    st.title("📋 Inventory App")

 # --- Kitchen Phase ---
    if st.session_state.phase == "kitchen":
        st.header("🍳 Step 1: Enter Kitchen Inventory")
        if st.session_state.index < len(kitchen_inventory_items):
            item = kitchen_inventory_items[st.session_state.index]
            st.subheader(f"Item: {item['name']}")

            if item['image'] and os.path.exists(item['image']):
                st.image(Image.open(item['image']), width=250)

            qty = st.text_input("Enter kitchen quantity:", key="kitchen_" + item['name'])

            col1, col2 = st.columns(2)
            with col1:
                if st.button("Next", key=f"kitchen_next_{item['name']}"):
                    st.session_state.kitchen_data[item['name']] = qty
                    st.session_state.index += 1
                    st.rerun()
            with col2:
                if st.button("Back", key=f"kitchen_back_{item['name']}") and st.session_state.index > 0:
                    st.session_state.index -= 1
                    st.rerun()
        else:
            st.success("✅ Kitchen inventory complete. Now continue with store inventory...")
            st.session_state.phase = "store"
            st.session_state.index = 0
            st.rerun()

# --- Store Phase ---
    elif st.session_state.phase == "store":
        st.header("🏬 Step 2: Complete Store Inventory")
        if st.session_state.index < len(store_inventory_items):
            item = store_inventory_items[st.session_state.index]
            name = item['name']
            st.subheader(f"Item: {name}")

            if item['image'] and os.path.exists(item['image']):
                 st.image(Image.open(item['image']), width=250)

            prev_kitchen = st.session_state.kitchen_data.get(name, None)
            if prev_kitchen:
                 st.info(f"Kitchen quantity previously entered: {prev_kitchen}")

            qty = st.text_input("Enter final store quantity:", key="store_" + name)

            col1, col2 = st.columns(2)
            with col1:
                if st.button("Next", key=f"store_next_{name}"):
                    st.session_state.store_data[name] = qty
                    st.session_state.index += 1
                    st.rerun()
            with col2:
                if st.button("Back", key=f"store_back_{name}") and st.session_state.index > 0:
                    st.session_state.index -= 1
                    st.rerun()
        else:
            st.success("🎉 All inventory completed. Showing final result...")
            st.session_state.phase = "done"
            st.rerun()

# --- Final Result Phase ---
    elif st.session_state.phase == "done":
        st.header("📦 Final Store Inventory")

        final_result = st.session_state.store_data
        for name, value in final_result.items():
            st.write(f"**{name}**: {value}")

    # Generate downloadable PDF
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

    # Session state setup
    if 'index' not in st.session_state:
        st.session_state.index = 0
    if 'quantities' not in st.session_state:
        st.session_state.quantities = {}
    if 'skipped' not in st.session_state:
        st.session_state.skipped = []
    
    # Ensure we don't go out of bounds
    if st.session_state.index < len(inventory_items):
        current_item_data = inventory_items[st.session_state.index]
        st.subheader(f"Item: {current_item_data['name']}")
    
        if current_item_data['image'] and os.path.exists(current_item_data['image']):
            image = Image.open(current_item_data['image'])
            st.image(image, width=300)
        else:
            st.write("No image found for this item.")
    
        qty = st.text_input("Enter quantity:", key=current_item_data['name'])
    
        col1, col2, col3, col4 = st.columns(4)
    
        with col1:
            if st.button("Next"):
                st.session_state.quantities[current_item_data['name']] = qty
                st.session_state.index += 1
                st.rerun()
        with col2:
            if st.button("Skip"):
                st.session_state.skipped.append(current_item_data['name'])
                st.session_state.index += 1
                st.rerun()
        with col3:
            if st.button("Back"):
                if st.session_state.index > 0:
                    st.session_state.quantities[current_item_data['name']] = qty
                    st.session_state.index -= 1
                    st.rerun()
        with col4:
            if st.button("🏡 Main Menu"):
                st.session_state.page = "menu"
                st.rerun()
    
    # When all items are done
    if st.session_state.index >= len(inventory_items):
        st.success("📦🛒🛍️ List is ready for order New Items. Best Luck!")
    
        if st.button("Back to Menu"):
            st.session_state.page = "menu"
            st.session_state.index = 0
            st.session_state.quantities = {}
            st.session_state.skipped = []
            st.rerun()
    
        # Show collected quantities
        st.write("### Collected Quantities:")
        if st.session_state.quantities:
            for item, q in st.session_state.quantities.items():
                st.write(f"- {item}: {q}")
        else:
            st.write("No quantities collected yet.")
    
        # ✅ Generate PDF from collected data
        def generate_inventory_pdf(data_dict):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Inventory Quantities", ln=True, align='C')
            pdf.ln(10)
            for item, qty in data_dict.items():
                pdf.cell(200, 10, txt=f"{item}: {qty}", ln=True)
            return pdf.output(dest="S").encode("latin-1")
    
        if st.session_state.quantities:
            pdf_data = generate_inventory_pdf(st.session_state.quantities)
            st.download_button(
                label="📄 Download Inventory Summary as PDF",
                data=pdf_data,
                file_name="Inventory_Summary.pdf",
                mime="application/pdf"
            )
