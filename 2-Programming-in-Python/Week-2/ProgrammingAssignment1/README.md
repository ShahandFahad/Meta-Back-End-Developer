# Lab Instructions: Functions, loops and data structures

In this lab you will be presented with a menu ordering system which will allow users to   
input three choices for a select menu. You are tasked with completing the menu system so   
that it returns and calculates the final bill for the user.
 <br><br>

> ### **Tips: Before you Begin**
> #### **To view your code and instructions side-by-side**, select the following in your VSCode toolbar:
> - View -> Editor Layout -> Two Columns
> - To view this file in Preview mode, right click on this README.md file and `Open Preview`
> - Select your code file in the code tree, which will open it up in a new VSCode tab.
> - Drag your assessment code files over to the second column. 
> - Great work! You can now see instructions and code at the same time. 
> - Questions about using VSCode? Please see our support resources [here](https://www.coursera.org/learn/programming-in-python/supplement/2IEyt/visual-studio-code-on-coursera).
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

## There are three main objectives of this activity:
1. Create new functions to solve specific problems.
2. Gain experience of using for loops to iterate over different data collections.
3. Create and use data structures to store, retrieve and loop over data.

<br>

## Exercise Instructions

1. Open the script ordering_system.py present inside the project folder.

2. Run the script and, when requested, enter in the three products of your choice based on the menu - 1 = espresso, 2 = coffee etc.

3. To run the script, open terminal and execute the following command. 

    ```
    python3 ordering_system.py
    ```

4. Extend the script to have a new function called `calculate_subtotal`.  
 It should accept one argument which is the order list and return the sum   
 of the prices of the items in the order list.

5. Implement `calculate_tax()` which calculates the tax of the subtotal.   
The tax percentage is 15% of overall bill.

6. Implement `summarize_order()` which returns a list of the names of the items   
that the customer ordered and the total amount (including tax) that they have to pay.  
 The orders should show the name and price.

<br>

## Final Step: Let's submit your code!
Nice work! To complete this assessment:
- Save your file through File -> Save 
- Select "Submit Assignment" in your Lab toolbar. 

Your code will be autograded and return feedback shortly on the "Grades" tab.  
You can also see your score in your Programming Assignment "My Submission" tab.