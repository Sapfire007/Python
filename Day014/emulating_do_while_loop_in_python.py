#emulating_do_while_loop_in_python
i = 0
while True:
  print(i)
  i=i+1
  if(i%50==0):
    break

'''
JAVA program for reference as there is no such do while loop in python : 

// Java Program to Illustrate One Time Iteration
// Inside do-while Loop
// When Condition IS Not Satisfied

// Class
class GFG {

    // Main driver method
    public static void main(String[] args)
    {
        // initial counter variable
        int i = 0;

        do {

            // Body of loop that will execute minimum
            // 1 time for sure no matter what
            System.out.println("Print statement");
            i++;
        }

        // Checking condition
        // Note: It is being checked after
        // minimum 1 iteration
        while (i < 0);
    }
}

'''