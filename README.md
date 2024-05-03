# Requirements #
- Created by Oliver Jen
- Discord: olvier

# Requirements #
- python 3.12.3

### modules ###
- flask

### optional ###
- git https://git-scm.com/downloads
- vscode https://code.visualstudio.com/
 - python extension by microsoft


# Why I chose this implementation #
- Using an html website for a display allowed for a more straightfoward and user friendly experience and lessened possible user error
  

# Instruction #
*These instructions are intended to be done on a windows machine*
1. Install python 3.12.3 https://www.python.org/downloads/
2. Get project files
 - git clone https://github.com/useyourshadow/Inventory-Management-System.git (recommended)
 - Download and unzip project from github
3. Open powershell, integrated terminal, or command prompt
4. pip install -U Flask
5. py app.py or python3 app.py
6. The command prompt shows an website that's hosting the test application.
 - ex. htpp://127.0.0.1:5000
7. Open up a browser and enter the ip in your url
8. To test functionality of APIs enter in desired values
9. Hit back button to test another API

## Helpful Information ##
- When adding a part, it will give a "{part} added succesfully confirmation" to the user.
- When doing get quantity it will display the quantity for the given SKU (for example)
 {
   "quantity": 3
 }

### GetInventory Example ###
>{
>  "EthernetCable": {
>    "545": {
>      "alpha_type": "male",
>      "beta_type": "male",
>      "last_updated": "Thu, 02 May 2024 23:11:01 GMT",
>      "length": 7.0,
>      "quantity": "9",
>      "speed": "10mbps"
>    }
>  },
>  "Resistor": {
>    "4": {
>      "last_updated": "Thu, 02 May 2024 23:10:55 GMT",
>      "quantity": "3",
>      "resistance": "1",
>      "tolerance": "2"
>    }
>  },
>  "Solder": {
>    "7": {
>      "last_updated": "Thu, 02 May 2024 23:10:54 GMT",
>      "length": 3.0,
>      "quantity": "5",
>      "solder_type": "lead"
>    }
>  }
>}

### GetPart Example ###
>{
>  "last_updated": "Thu, 02 May 2024 23:10:55 GMT",
>  "quantity": "3",
>  "resistance": "1",
>  "sku": "4",
>  "tolerance": "2"
>}

#### Add Inventory ####
- Add Inventory will add a certain amount of quantity to the part with the given SKU, and will display
Inventory added successfully

#### Delete Part ####
- Delete part will delete the part with the given SKU and wil display
Part deleted successfully

#### NOTE ####
 - For Search, in Part Class, it has to be capitalized and characteristics are done with "=". 
 - Search allows for multiple characterisitcs to be put it in as long as they are seperated with a comma.
 - So an example is (in part class) Resistor  (and in characteristics) resistance = 1
 - It has been implemented so there will be only be one SKU per any item, so entering the same SKU will result in an error

#### Other Examples ####
- Resistor        resistance = 1, tolerance = 2
- Solder          solder_type = lead
- DisplayCable    cable_type = hdmi
- EthernetCable   alpha_type = male
- EthernetCable   beta_type = male
- EthernetCable   speed = 10mbps
