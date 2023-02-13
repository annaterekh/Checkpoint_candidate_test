# Checkpoint_candidate_test
Checkpoint Candidate Test

Question 1
  Please see the Q1.docx
Question 2
  1. Explicit wait - waiting for a specific condition like an element is available.
     Implicit wait - waiting for a specified time without any condition.
     
     Explicit wait should be used when there is an element that it takes more time to load it, implicit wait is used when it takes time for all elements on page to load
  2. The code is implemented in class GreenKartShopper.py. The function is getting a dictionary with required items and their amount. It is finding the items, 
     adding them to cart and apply the discount. There is no output or prints.
     Assumption: input to the function is correct, the requested items can be found in GreenKart
     
Question 3 
  1. Tests:
        1. Test response - send request to https://ipinfo.io and get html status code 200 - success
        2. Test positive know IP - send the request with the IP from example https://ipinfo.io/161.185.160.93/geo and verify correctness of the response
        3. Negative test while IP is invalid and one or more of its elements is larger than 255:
           3.1. Only one number is greater than 255. Check for the first, second, third and fourth numbers
           3.2. Two numbers are greater than 255. Check for all possible permutations (first + second, first + third etc.)
           3.3 Three numbers are greater than 255. Check for all possible permutations (first + second + third etc.)
           3.4 All four numbers are invalid
           
 Question 4
  The code is implemented in file Question4.py. It keeps the variable for the max integer. Then the function is going through the list, and check whether 
  the current item is one digit number and whether it's bigger than the saved max integer. If yes, it replaces the saved max integer with the founded value.
  If there is no one digit integer, the function will return None.
  Complexity - O(n)
