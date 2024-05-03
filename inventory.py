import datetime
from enum import Enum


class Part:
    def __init__(self, sku, last_updated,):
        self.sku = sku
        self.last_updated = last_updated

class Resistor(Part):
    def __init__(self, sku, resistance, tolerance, last_updated, quantity):
        super().__init__(sku, last_updated)
        self.resistance = resistance
        self.tolerance = tolerance
        self.quantity = quantity


class Solder(Part):
    def __init__(self, sku, solder_type, length, last_updated, quantity):
        super().__init__(sku, last_updated)
        self.solder_type = solder_type
        self.length = length
        self.quantity = quantity

class Wire(Part):
    def __init__(self, sku, gauge, length, last_updated, quantity):
        super().__init__(sku, last_updated)
        self.gauge = gauge
        self.length = length
        self.quantity = quantity



class DisplayCable(Part):
    def __init__(self, sku, cable_type, length, color, last_updated, quantity):
        super().__init__(sku, last_updated)
        self.cable_type = cable_type
        self.length = length
        self.color = color
        self.quantity = quantity



class EthernetCable(Part):
    def __init__(self, sku, alpha_type, beta_type, speed, length, last_updated, quantity):
        super().__init__(sku, last_updated)
        self.alpha_type = alpha_type
        self.beta_type = beta_type
        self.speed = speed
        self.length = length
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_part(self, part):
        # Checks if a part has the same SKU already
        if part.sku in self.inventory:
            existing_part = self.inventory[part.sku]
            if not isinstance(existing_part, type(part)):
                raise ValueError("A part with SKU {} already exists but of a different type".format(part.sku))

            # Check if SKU is the same but for a different part
            for attr_name, attr_value in part.__dict__.items():
                if attr_name == 'sku' or attr_name == 'quantity':
                    continue
                if getattr(existing_part, attr_name) != attr_value:
                    raise ValueError("A part with SKU {} already exists".format(part.sku))

        # Checks if they don't have all required values
        for attr_name, attr_value in part.__dict__.items():
            if attr_name == 'sku' or attr_name == 'quantity':
                continue
            if attr_value is None:
                raise ValueError("Missing characteristic {} for part with SKU {}".format(attr_name, part.sku))

        # Check if quantity is negative
        if int(part.quantity) < 0:
            raise ValueError("Quantity cannot be negative")

        # Add the part to inventory
        if part.sku in self.inventory:
            current_quantity = int(self.inventory[part.sku].quantity)
            self.inventory[part.sku].quantity = current_quantity + int(part.quantity)
        else:
            self.inventory[part.sku] = part

            

    def add_inventory(self, sku, quantity):
        # Checks if quantity is negative
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        
        # Checks if they are looking for an SKU that doesn't exist
        if sku not in self.inventory:
            raise ValueError("SKU {} does not exist in inventory".format(sku))
        
        # Adds part and updates inventory
        self.inventory[sku].last_updated = datetime.datetime.now()
        self.inventory[sku].quantity = int(self.inventory[sku].quantity) + quantity

    def get_quantity(self, sku):
      if sku in self.inventory:
          return int(self.inventory[sku].quantity)
      else:
          raise ValueError(f"SKU {sku} does not exist in inventory")

    def get_inventory(self):
      inventory_dict = {}
      # Shows everything in the inventory
      for sku, part in self.inventory.items():
          if isinstance(part, Part):
              part_type = type(part).__name__
              part_dict = {key: value for key, value in part.__dict__.items() if key != 'sku'}
              inventory_dict.setdefault(part_type, {})[sku] = part_dict
      return inventory_dict

    def get_part(self, sku):
        if sku not in self.inventory:
            raise ValueError("SKU {} does not exist in inventory".format(sku))
        return self.inventory[sku]

    def search(self, part_class, **kwargs):
        found_parts = []
        for part in self.inventory.values():
            if isinstance(part, part_class):
                matched = True
                for key, value in kwargs.items():
                    if hasattr(part, key):
                        attr_value = getattr(part, key)
                        # Handle enum attributes
                        if isinstance(attr_value, Enum):
                            # Convert search value to enum member
                            try:
                                search_enum_value = getattr(type(attr_value), value.upper())
                            except AttributeError:
                                matched = False  
                                break
                            if attr_value != search_enum_value:
                                matched = False  
                                break
                        else:
                            # For non enum attributes
                            if isinstance(attr_value, (int, float)):
                                # Convert both attribute and search value to float for comparison
                                attr_value = float(attr_value)
                                value = float(value)
                            if attr_value != value:
                                matched = False
                                break
                            # A tolerance to check for small float error
                            elif isinstance(attr_value, float) and isinstance(value, float):
                                tolerance = 0.001  
                                if abs(attr_value - value) > tolerance:
                                    matched = False
                                    break
                    else:
                        matched = False  
                        break
                if matched:
                    found_parts.append(part)
        return found_parts


    def delete_part(self, sku):
        if sku not in self.inventory:
            raise ValueError("SKU {} does not exist in inventory".format(sku))
        del self.inventory[sku]
