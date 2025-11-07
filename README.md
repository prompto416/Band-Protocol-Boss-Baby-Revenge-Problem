# Band-Protocol-Boss-Baby-Revenge-Problem

Hi, this is your candidate Phobphoomin Siriboon. 
You can find the solution in the file in this directory with explanation as comments in the code
Additionally, I'll write a solution here 

## There are only two cases to set your eyes on with the 2nd case being a bit tricky but overall it's a very easy one pointer problem

1.The Boss Baby shot first. We can immediately return a Bad Boy by checking the 0th index to see if it's an R string

2.The Boss Baby did not return fire. We can check by counting up R and subtracting it for each R we finds afterward. 

2.1 If there are remaining S we returns Bad boy 

2.2 If S = 0 but we find an R we ignore it because the boss baby can shoot back as much as he wants "as long as he doesn't shoot first".

