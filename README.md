# How I Built a Mortgage Calculator 
I will be showing my thought process and how I came to my solution. This project was part of a personal project assignment in my Intro to Computer Architecture class

# 1. Initial Code Logic
So before I started making any code I tried to list out all the information beforehand on what information I needed from the user to get to my conclusion. This way I could build in sections and the assignment would have more structure.
- What States or user defined amount ? I decided to both
- Loan Term
- Interest Rate
- Mortgage Formula to calculate information

# 2. Setting State Parameters/Dictionary and Finding Median Home Prices in AR, TX, and OK
- First, I needed to know whether the user wanted to use the median home price for a specific state (Arkansas, Texas, or Oklahoma) or if they preferred to enter a custom loan amount.
- If they chose a state, the program would automatically use the median home price for that state. Otherwise, they would enter their own loan amount.

# 3. Loan Term
- I needed to ask the user for the loan term (the number of years they plan to repay the loan). This is important because it determines how many payments the user will make and affects the calculation of the monthly payment.

# 4. Interest Rate
- The user also had to provide the interest rate for the mortgage. This is a critical factor in the calculation, as the rate determines how much interest will be added to the loan over time.

# 5. Mortgage Formula
- With the loan amount, interest rate, and loan term, I could then calculate the monthly payment using the standard mortgage formula.
