# Manual Testing
### Test descriptions
- A. Header and Footer
  1. Checking all navigation buttons redirect to the appropriate pages.
  2. Non signed in users navbar displays 'register' and 'login' buttons.
  3. Signed in users navbar displays 'cart', 'profile' and 'log out' buttons.
  3. Signed in admins navbar displays the additional 'admin' button.
  4. The logout button, successfully logs out the user from their account.
  6. The logo redirects to the index page.
  7. The GitHub icon opens a new page to my GitHub repository and social media icons open their homepages.

- B. Registration
  1. The registration form records all user data. 
  2. A successful registration redirects to the profile page.
  3. On submission of an invalid form, the user is warned of the error and stays on the same page.

- C. Sign In Form
  1. A successful registration redirects to the home page.
  2. On submission of an invalid form, the user is warned of the error and stays on the same page.
 
- D. Home page
  1. Signed in users have 'bugs' and 'features' displayed under the tagline.
  2. Non signed in users have 'register' under the tagline.
  3. The graphs show the correct information.
  4. The 'See Bugs' and 'See Features' button under the description redirects to the appropriate pages.

- E. Bugs/ Features
  1. The 'Add' button redirects to the add ticket page.
  2. The 'View Ticket' button redirects to the appropriate bug/feature detail page.

- F. Bugs detail
  1. If the user is the ticket creator or admin, the 'edit' button appears.
  2. The 'upvote' button upvotes the ticket by one point and is then disabled for that user.
  3. A comment posted is displayed on the same page.
  4. The 'Edit' button redirects to the edit page.

- G. Feature detail
  1. If the user is the ticket creator or admin, the 'edit' button appears.
  2. A user is made aware that they are upvoting the same feature after the first upvote.
  3. A upvoted feature is sent to the cart.
  4. A comment posted is displayed on the same page.
  5. The 'Edit' button redirects to the edit page.
 
- H. Add/ Edit page
  1. All the correct information is recorded and displayed on the correct pages.
  2. If the user is admin, there is the option to change the status.
  3. Edit values are preloaded into the form fields.

- I. Cart
  1. The user is able to remove tickets from the cart
  2. The 'checkout' button redirects to the checkout page.

- J. Checkout
  1. A succesful payment redirects the user to the homepage, and displays a message of success.
  2. On submission of an invalid form, the user is warned of the error and stays on the same page.
  3. Payment is received on Stripe.
  4. The correct feature receives one upvote point.

### Manual Test checklist

|Pass|Fail|
|:--:|:--:|
|P|F|

|     |Chrome|FireFox|Edge|Opera|Safari|Mobile|
|:---|:----:|:-----:|:--:|:---:|:----:|:----:|
|**A. i**|      P|P|P|P|P|P|
|**A. ii**|     P|P|P|P|P|P|
|**A. iii**|    P|P|P|P|P|P|
|**A. iv**|     P|P|P|P|P|P|
|**A. v**|      P|P|P|P|P|P|
|**A. vi**|     P|P|P|P|P|P|       
|**A. vii**|    P|P|P|P|F|P|
|**B. i**|      P|P|P|P|P|P|
|**B. ii**|     P|P|P|P|P|P|
|**B. iii**|    P|P|P|P|P|P|
|**C. i**|      P|P|P|P|P|P|
|**C. ii**|     P|P|P|P|P|P|
|**D. i**|      P|P|P|P|P|P|
|**D. ii**|     P|P|P|P|P|P|
|**D. iii**|    P|P|P|P|**F**|P|
|**D. iv**|     P|P|P|P|P|P|
|**E. i**|      P|P|P|P|P|P|
|**E. ii**|     P|P|P|P|P|P|
|**F. i**|      P|P|P|P|P|P|
|**F. ii**|     P|P|P|P|P|P|
|**F. iii**|    P|P|P|P|P|P|
|**F. iV**|     P|P|P|P|P|P|
|**G. i**|      P|P|P|P|P|P|
|**G. ii**|     P|P|P|P|P|P|
|**G. iii**|    P|P|P|P|P|P|
|**G. iv**|     P|P|P|P|P|P|
|**G. v**|      P|P|P|P|P|P|
|**H. i**|      P|P|P|P|P|P|
|**H. ii**|     P|P|P|P|P|P|
|**H. iii**|    P|P|P|P|P|P|
|**I. i**|      P|P|P|P|P|P|
|**I. ii**|     P|P|P|P|P|P|
|**J. i**|      P|P|P|P|**F**|P|
|**J. ii**|     P|P|P|P|P|P|
|**J. iii**|    P|P|P|P|**F**|P|
|**J. iv**|     P|P|P|P|**F**|P|

#### Notes:
- Safari:
  - I'm running safari on windows. **The last version update was back in 2012.** This would suggest that this version of browser doesn't support some css or jquery attributes the same as other browsers do.
  - Redirection to my GitHub account doesn't work.
  - The second part of the homepage can't be seen, most likely due to the jquery 'show fade', I have on the elements.
  - If I tried to make payment I would get 'We were unable to take a payment with that card!' error. That would be an issue with Stripe. Since payment cannot be made, I could not upvote the feature.
  - A lot of css wasn't compatible. Forms were stretched out or squashed. The bugs and feature tickets took up the whole row instead of lining up next to each other.
