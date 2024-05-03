from flask import Flask, render_template, request, jsonify
import datetime

from inventory import Inventory, Resistor, Solder, Wire, DisplayCable, EthernetCable
from inventory import Part

import json 

app = Flask(__name__)

inventory_system = Inventory()

@app.route("/")
def index():
    return render_template("index.html")

# Adding parts individually to interact with html easily
@app.route("/add_resistor", methods=["POST"])
def add_resistor():
    # Getting characteristics 
    resistance = request.form["resistance"]
    tolerance = request.form["tolerance"]
    sku = request.form["SKU"]
    quantity = request.form["quantity"]  
    resistor = Resistor(sku, resistance, tolerance, datetime.datetime.now(), quantity)
    inventory_system.add_part(resistor)
    return "Resistor added successfully"

@app.route("/add_solder", methods=["POST"])
def add_solder():
    solder_type = request.form["type"]
    length = request.form["length"]
    sku = request.form["SKU"]
    quantity = request.form["quantity"]  
    solder = Solder(sku, solder_type, float(length), datetime.datetime.now(), quantity)
    inventory_system.add_part(solder)
    return "Solder added successfully"

@app.route("/add_wire", methods=["POST"])
def add_wire():
    gauge = request.form["gauge"]
    length = request.form["length"]
    sku = request.form["SKU"]
    quantity = request.form["quantity"]  
    wire = Wire(sku, gauge, float(length), datetime.datetime.now(), quantity)
    inventory_system.add_part(wire)
    return "Wire added successfully"

@app.route("/add_displaycable", methods=["POST"])
def add_displaycable():
    cable_type = request.form["type"]
    length = request.form["length"]
    color = request.form["color"]
    sku = request.form["SKU"]
    quantity = request.form["quantity"]  
    display_cable = DisplayCable(sku, cable_type, float(length), color, datetime.datetime.now(), quantity)
    inventory_system.add_part(display_cable)
    return "Display Cable added successfully"

@app.route("/add_ethernetcable", methods=["POST"])
def add_ethernetcable():
    alpha_type = request.form["alpha"]
    beta_type = request.form["beta"]
    speed = request.form["speed"]
    length = request.form["length"]
    sku = request.form["SKU"]
    quantity = request.form["quantity"]  
    ethernet_cable = EthernetCable(sku, alpha_type, beta_type, speed, float(length), datetime.datetime.now(), quantity)
    inventory_system.add_part(ethernet_cable)
    return "Ethernet Cable added successfully"


# Add inventory route
@app.route("/add_inventory", methods=["POST"])
def add_inventory():
    sku = request.form["SKU"]
    quantity = int(request.form["quantity"])
    try:
        inventory_system.add_inventory(sku, quantity)
        return "Inventory added successfully"
    except ValueError as e:
        return str(e), 400  


# Get quantity route  
@app.route("/get_quantity", methods=["GET"])
def get_quantity():
    sku = request.args.get("SKU")
    try:
        quantity = inventory_system.get_quantity(sku)
        if isinstance(quantity, (int, float, str, bool)):
            return jsonify({"quantity": quantity})
        else:
            return jsonify({"quantity": str(quantity)})
    except ValueError as e:
        return str(e), 400  


# Get inventory route
@app.route("/get_inventory", methods=["GET"])
def get_inventory():
    inventory = inventory_system.get_inventory()
    inventory_json = {}
    for sku, part in inventory.items():
        if isinstance(part, Part):
            part_dict = {key: value for key, value in part.__dict__.items() if key != 'sku'}
            part_type = part.__class__.__name__ 
            inventory_json[sku] = {part_type: part_dict}
        else:
            inventory_json[sku] = part  

    return jsonify(inventory_json)



# Get part route
@app.route("/get_part", methods=["GET"])
def get_part():
    sku = request.args.get("SKU")
    part = inventory_system.get_part(sku)
    part_dict = {key: value for key, value in part.__dict__.items()}
    return jsonify(part_dict)



# Search part route
@app.route("/search", methods=["GET"])
def search():
    # Checking name of part class
    part_class_name = request.args.get("part_class")
    characteristics = request.args.get("characteristics") 
    # Gets object from global namespace
    part_class = globals().get(part_class_name)
    # Error for not finding a part class
    if part_class is None:
        return jsonify({"error": f"Part '{part_class_name}' not found"}), 400
    
    search_params = {}
    if characteristics:
        try:
            # Parsing through the characteristics 
            characteristics_list = characteristics.split(",")
            
            for char in characteristics_list:
                key, value = char.strip().split("=")
                
                # Checks if attribute is enum
                if hasattr(part_class, key):
                    attr_type = getattr(part_class, key)
                    if isinstance(attr_type, Enum):
                        # Converts value to enum member and get rid of hyphens or 
                        value = attr_type[value.strip().replace("-", "_").upper()]
                
                search_params[key.strip()] = value.strip()
        except Exception as e:
            return jsonify({"error": f"Parsing failed: {e}"}), 400
    # Searches for parts based on the parameters
    found_parts = inventory_system.search(part_class, **search_params)
    found_parts_dict = [part.__dict__ for part in found_parts]
    
    return jsonify({"result": found_parts_dict})


# Delete Part route
@app.route("/delete_part", methods=["GET"])
def delete_part():
    sku = request.args.get("SKU")
    inventory_system.delete_part(sku)
    return "Part deleted successfully"

if __name__ == "__main__":
    app.run(debug=True)