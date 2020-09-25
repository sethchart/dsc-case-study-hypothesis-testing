# Case Study - Hypothesis Testing

## Question 1: Is there a difference in quantity of products sold by discount rate?

View notebook [Here](notebooks/Question1.ipynb)

* Investigate Data
    * Obtain Necessary Data
    
* ANOVA Test
    * Defining H0, HA and alpha
    * ANOVA Assumptions
    * Perform statistical tests
* Conclusion

## Question 2: Not Addressed

## Question 3: Is there a difference in mean sales between Sales Managers and Sales Representatives?

View notebook [Here](notebooks/Question2.ipynb)

To answer this question, we collected all products purchased from the `OrderDetail` table with their `UnitPrice`, `Quantity`, and `Discount`. For each row, we also joined on `OrderId` to obtain information about the sales employee associated with the order. Specifically, we collected `Employee Id` and `Title` from the `Employee` table.

Next, we computed the total cost of items represented in each row by discounting the unit price by the discount percentage and multiplying by the quantity. We then grouped on `OrderID` and summed over all products contained in the order to obtain an order total for each order in the data set. 

With the data adequately processed, we split the order totals into two samples based on the title of the responsible sales employee. With these samples in hand, we plan to use a Welch's t-test to check for a difference in means. We inspected the distributions of the price per sale and noted substantial right skew in the distributions, however both samples were large enough that the Central Limit Theorem insures sufficient normality in the sampling distributions of the sample means. 

<img src='images/sales.png' width='500'/>

### Conclusion
Based on the outcome of our t-test (p = 0.99), we fail to reject the null hypothesis that there is no difference in the mean sales for representatives and managers.

<img src='images/meme.jpeg' width='500'/>

## Points of Interest

 * Our team collaborated using a single github repo where re were able to push all of our work.
 * The `NorthWindConnector` module provides the DbConnector class which in turn provides a clean interface for interacting with the database. 
