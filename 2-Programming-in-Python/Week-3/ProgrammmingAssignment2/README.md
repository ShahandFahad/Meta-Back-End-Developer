# Lab Instructions: Abstract Classes and Methods

In this assignment, you will be creating an abstract class for a bank that will be used to create a regular class for a specific bank.  
This class will contain the implementation of the abstract method from the abstract class.  

 <br>

> ### **Tips: Before you Begin**
> #### **To view your code and instructions side-by-side**, select the following in your VSCode toolbar:
> - View -> Editor Layout -> Two Columns
> - To view this file in Preview mode, right click on this README.md file and `Open Preview`
> - Select your code file in the code tree, which will open it up in a new VSCode tab.
> - Drag your assessment code files over to the second column. 
> - Great work! You can now see instructions and code at the same time. 
> - Questions about using VSCode? Please see our support resources [here](https://www.coursera.org/learn/programming-in-python/supplement/2IEyt/visual-studio-code-on-coursera)
> #### **To run your Python code**
> - Select your Python file in the Visual Studio Code file tree 
> - You can right click the file and select "Run Python File in Terminal" 
>   or run the file using the smaller   
    play button in the upper right-hand corner 
>   of VSCode.  
    (Select "Run Python File in Terminal" in the provided button dropdown)
> - Alternatively, you can follow lab instructions which use python3 commands to run your code in terminal.
> 
<br>

## Exercise Instructions

### Instructions

1. Create a class called `Bank` and pass `ABC` to it.  

2. Inside the class you have to define two methods: 
    - 2.1: Define a function called `basicinfo()` and add a print statement inside it saying   
    `"This is a generic bank"` and returning the string `"Generic bank: 0"`. 

    - 2.2: Define a second function called `withdraw` and keep it empty by adding a pass keyword under it.   
    Make this function abstract by adding `'@abstractmethod'` right above it. <br><br>

3. Create another class called `Swiss` and pass the class `Bank` inside it. 
    This means you are inheriting from `class Bank`. 
    -  3.1: Create a constructor for this class that initializes a class variable `bal` to `1000` <br><br>

4. Override both functions from the Bank class: `basicinfo()` and `withdraw()`. 
    - 4.1: Define a function called `basicinfo()` and add a print statement inside it stating `“This is the Swiss Bank”`  
    and returning a string with `"Swiss Bank: "` followed by the current bank balance.   
    For example, if `self.bal = 80`, then it would return `"Swiss Bank: 80"`

    - 4.2 Define a second function,  called `withdraw` and pass one parameter to it (other than `self):` amount.  
     Amount represents the amount that will be withdrawn. 

        - 4.2.1: Update the class variable bal by deducting the value of amount from it. 
        - 4.2.2: Print the value of amount giving output such as: “Withdrawn amount: 30"
        - 4.2.3:  Print the new balance giving an output such as: “New balance: 970”
        - 4.2.4:  Return the new balance
        - Note: Make sure to verify that there is enough money to withdraw!  
        If amount is greater than balance, then do not deduct any money from the 
        class variable `bal`. Instead, print a statement saying `"Insufficient funds"`, and return the original account balance instead.

<br>


## Final Step: Let's submit your code!
Nice work! To complete this assessment:
- Save your file through File -> Save 
- Select "Submit Assignment" in your Lab toolbar. 

Your code will be autograded and return feedback shortly on the "Grades" tab.  
You can also see your score in your Programming Assignment "My Submission" tab.
<br> <br> 