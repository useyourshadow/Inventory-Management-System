To run, make sure all files are in same directory and in the terminal type: python3 app.py   or   python app.py
Also make sure flask is installed
Click on the link and it will direct you to a website where you can use all the functions
All functions are useable by just typing the value wanted into the text box
I chose this interface because I believe this would be the most easily understood by users. The website is very user-friendly and allows for less user error.

When adding parts, if it was done successfuly it would state, "{part} added successfully" 


When doing get quantity it will display the quantity for the given SKU (for example)
{
  "quantity": 3
}



GetInventory will show all items, under the name of the part it will show the SKU number (for example)
{
  "EthernetCable": {
    "545": {
      "alpha_type": "male",
      "beta_type": "male",
      "last_updated": "Thu, 02 May 2024 23:11:01 GMT",
      "length": 7.0,
      "quantity": "9",
      "speed": "10mbps"
    }
  },
  "Resistor": {
    "4": {
      "last_updated": "Thu, 02 May 2024 23:10:55 GMT",
      "quantity": "3",
      "resistance": "1",
      "tolerance": "2"
    }
  },
  "Solder": {
    "7": {
      "last_updated": "Thu, 02 May 2024 23:10:54 GMT",
      "length": 3.0,
      "quantity": "5",
      "solder_type": "lead"
    }
  }
}




GetPart will simply show the characterisitcs of the part with that SKU
{
  "last_updated": "Thu, 02 May 2024 23:10:55 GMT",
  "quantity": "3",
  "resistance": "1",
  "sku": "4",
  "tolerance": "2"
}


Add Inventory will add a certain amount of quantity to the part with the given SKU, and will display
Inventory added successfully


Delete part will delete the part with the given SKU and wil display
Part deleted successfully


NOTE: for Search, in Part Class, it has to be capitalized and characteristics are done with "=". 
Search allows for multiple characterisitcs to be put it in as long as they are seperated with a comma.
So an example is (in part class) Resistor  (and in characteristics) resistance = 1

Other examples
Resistor        resistance = 1, tolerance = 2
Solder          solder_type = lead
DisplayCable    cable_type = hdmi
EthernetCable   alpha_type = male
EthernetCable   beta_type = male
EthernetCable   speed = 10mbps