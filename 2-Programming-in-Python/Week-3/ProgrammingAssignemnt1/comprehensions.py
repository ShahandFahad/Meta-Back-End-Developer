# Input data: List of dictionaries
employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]

# Function to be passed to the map() function. Do not change this.
def mod(employee_list):
   temp = employee_list['name'] + "_" + employee_list["department"]
   return temp

def to_mod_list(employee_list):
   """ Modifies the employee list of dictionaries into list of employee-department strings

   [IMPLEMENT ME] 
      1. Use the map() method to apply mod() to all elements in employee_list

   Args:
      employee_list: list of employee objects

   Returns:
      list - A list of strings consisting of name + department.
   """
   ### WRITE SOLUTION CODE HERE
   return list(map(mod, employee_list))
#    raise NotImplementedError()

def generate_usernames(mod_list):
   """ Generates a list of usernames 

   [IMPLEMENT ME] 
      1. Use list comprehension and the replace() function to replace space
         characters with underscores

      List comprehension looks like:
      list = [ function() for <item> in <list> ]

      The format for the replace() function is:

      test_str.replace(“a”, “z”) # replaces every “a” in test_str with “z”

   Args:
      mod_list: list of employee-department strings

   Returns:
      list - A list of usernames consisting of name + department delimited by underscores.
   """
   ### WRITE SOLUTION CODE HERE
   def replcae_with_underscore(str):
       return str.replace(' ', '_')
   
   return [replcae_with_underscore(user_name) for user_name in mod_list]
#    raise NotImplementedError()

def map_id_to_initial(employee_list):
   """ Maps employee id to first initial

   [IMPLEMENT ME] 
      1. Use dictionary comprehension to map each employee's id (value) to the first letter in their name (key)

      Dictionary comprehension looks like:
      dict = { key : value for <item> in <list> }

   Args:
      employee_list: list of employee objects

   Returns:
      dict - A dictionary mapping an employee's id (value) to their first initial (key).
   """
   ### WRITE SOLUTION CODE HERE
   def emp_id_initial(employee_list):
       return employee_list["name"][0]
   def emp_id(employee_list):
        return employee_list['id']
   
   employee_id_initial_list = [emp_id_initial(employee) for employee in employee_list]
   employee_id_list = [emp_id(employee) for employee in employee_list]
   
   return {key:value for (key, value) in zip(employee_id_initial_list, employee_id_list) }

def main():
   mod_emp_list = to_mod_list(employee_list)
   print("Modified employee list: " + str(mod_emp_list) + "\n")

   print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

   print(f"Initials and ids: {map_id_to_initial(employee_list)}")

if __name__ == "__main__":
   main()