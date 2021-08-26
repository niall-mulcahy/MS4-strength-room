- - -
# The Strength Room - Milestone Project 4

[View the live project here](https://ms4-strength-room.herokuapp.com/)
## Django Project by Niall Mulcahy

This project was created as part of my Diploma in Software Development with the Code Institute. It is a fitness community site which offers a forum to paying members and various coaching products. I qualified with my degree in Sport and Exercise Science from the University of Limerick in 2020, so I suppose this is my way of combining the two!

![Image of home page of site](/media/home-page.PNG)

### Table of Contents

1. User Experience (UX)
    - Project Goals
    - User Stories
        - First Time User
        - Returning User
        - Frequent User
        - Site Owner
    - Design Choices
        - Colour Scheme
        - Typography
        - Imagery
    - Wireframes



2. Features
    - Existing Features
    - Features Left to Implement


3. Technologies Used
    - Languages
    - Frameworks, Libraries and Programs 


4. Testing
    - Testing User Stories
    - Bugs and Fixes

5. Deployment
    - Running this project locally


6. Credits
    - Media
    - Code
    - Acknowledgements

- - -

# User Experience

- Project Goals
    - The goal of this project was mainly to bring all of the coding knowledge I have accrued so far together in one single app. I wanted to use the feedback I had gotten on previous projects to inform choices that were made here. The goals of the project in no particular order were: 
    
    1. to make the project as nice to look at as possible with a attractive colour scheme and a clear format
    2. Ensure usability on all device sizes, which is something I have struggled with in the past
    3. Provide the user with a very straight-forward experience in which they know what step to take next
    4. Utilise the Django framework for creating the data structure
    5. Accept payments on the site using Stripe
    6. Create a forum on the site which is aesthetically pleasing, has various methods for sorting the posts, and has some form of moderation.
    7. Products and forum portions of the site have CRUD functionality
    8. Create authentication logic which only permits the user to view the forum if they have paid the membership fee

- User Stories
    - First Time Visitor Goals

    1. As a first time visitor of the site I want to be able to know what the purpose of the site is and learn more about what it is they do
    2. I want to be able to navigate around the site with ease
    3. I want to be able to decide if I want to purchase anything from the site quickly, and if so I want the checkout process to be as easy as possible.
    4. I want everything on the site to look well no matter what device I am using

    - Returning Visitor Goals

    1. As a returning visitor of the site I want to be able to register for an account with ease if that is what I choose to do
    2. I want to then be able to log in quickly
    3. If I decide to purchase membership on the site I want to be able to checkout without spending much time and effort on it
    4. I want to be able to browse the forum and search for things that interest me specifically.

    - Frequent User Goals

    1. I want to login to the site with as little friction as possible
    2. The forum must have some way of searching through all the posts so I don't have to scroll down through hundreds of posts to find the posts I'm interested in.
    3. The main all posts page must have some sort of cut off so that I don't have to scroll for ages to see older posts
    4. Posts should be categorised so I can view posts from certain categories.
    5. I should be able to comment under posts and reply to comments so that a proper discourse can be had.
    6. The content should be moderated to a degree because people in the fitness industry can sometimes have very coarse, inflammatory opinions, so if someone is trying to incite hate, or spread false information I would rather not have to engage with this.

    - Site Owners Goals
    1. To create a buzz and hype around the site and the brand, culminating in high traffic on the site's forum
    2. To attract new clients for the coaching products
    3. To be able to add or remove products to the site
    4. To be able to moderate the forum and remove posts if they are deliberately spreading misinformation 

- Design
    - Colour Scheme 
        - This site is built on a dark grey background with white text. There are also blue banners and buttons interspersed around the site to give splashes of colour. The header is white and the footer is black, so there is good contrast around the site too!

    - Typography
        - The Merriweather Sans font was used all over the site with Sans Serif being the backup in case this font couldn't be loaded. I chose this font because it gives a professional, glossy look to the site without appearing too formal.
        - I also used the 'Permanent Marker' font from google fonts for which sans-serif is also the backpup. I used this font as pseudo-branding for the site. Since it looks like graffiti it gives the site the urban feel I was looking for. It is used in the header, the main home page, and the footer.
    - Imagery
        - The main imagery used in the site is on the home page. This is to give the users a break from long passages of text whilst also ensuring that this text is still being presented. 
        - The main home image is the most eye-catching image on the site as it spans the full size of the screen on all viewports. It is overlayed with an almost opaque div so that white text is very easy to view. The colours in the image are already quite dark so the contrast of the text is very high and clear. 
        - The other images on the home page are hidden on smaller view ports so that the text can be read without any difficulty. I considered putting them in vertically but then it felt like the user would have to scroll for too long so just hiding the images on small viewports seemed like the best option.
        - There is also an image on the forum admin page if there are no posts pending approval. It is a large emoji with a thumbs up, congratulating the admin for dealing with all the posts. 

- Wireframes
    - I have attached all the relevant wireframes for this project in the Wireframes directory. The main changes between the final site and the wireframes are in the layout of the forum and the profile pages. The forum section is organised in much better fashion than the wireframes. Also, I placed less emphasis on the user profiles in the finished version of the site, and didn't store data about them such as a bio and a history of their comments. Instead I opted to allow them to view their purhcase history and their billing details. 

# Features 

- Included Features
    - Responsive on all device sizes
    - User authentication and email verification for account creation and password reset
    - User authentication and redirects for unauthorised access to certain portions of the site
    - Paywall preventing users from accessing the forum unless they have paid
    - Forum with pagination, search and filtration via category
    - Users have ability to read others' posts and edit and delete their own
    - Site owner has the ability to create, and remove products
    - Site owner gets to approve posts before they go live for other users to see
- Features Left to Include
    - Instead of a one off payment, a subscription based service to allow more money to be genereated for the site owner in the long run
    - Use carousels on the home page where there are static images currently

# Technologies Used

- Languages Used
    1. [HTML5](https://www.w3schools.com/html/)
    2. [CSS3](https://www.w3schools.com/css/)
    3. [Javascript](https://www.javascript.com/)
    4. [Python](https://www.python.org/)
    
- Frameworks, Libraries and Programs Used
    1. [Bootstrap v5.1.0](https://getbootstrap.com/)
        - Bootstrap was used to assist with the layout and generally sped up the overall design and styling processes.
    2. [Google Fonts](https://fonts.google.com/)
        - Google fonts were used to import the two fonts used in this site which were Merriweather Sans and Permanent Marker. In particalar the Permanent Marker font is a very positive addition to the site
    3. [Font Awesome](https://fontawesome.com/)
        - In my opinion font awesome is one of the most useful tools for web developers out there. The icons can really help with the overall look of a site and can convey a message instantly, much better than text can in many cases
    4. [jQuery](https://jquery.com/)
        - While I didn't use a lot of javascript in this project, jquery did help me write the javascript I did write a little bit faster!
    5. [Django](https://www.djangoproject.com/)
        - I used django as my python framework for this project. It allowed me to have multiple apps, each with their own associated data to all communicate with one another. I utlised the messages, session storage, models and forms features to allow me to maintain consistency within the site while also getting everything up and running relatively quickly.
    6. [AllAuth](https://django-allauth.readthedocs.io/en/latest/installation.html)
        - I used allauth to help with user authentication. It was user-friendly and made setting up good looking pages for multiple different use cases really efficient.
    7. [Heroku](https://www.heroku.com/)
        - I used heroku to deploy my site. I linked it with my GitHub repository so that when I made a push to my GitHub repository, it also pushed to the Heroku master branch, and this would in turn build a start a new build. 
    8. [Git](https://git-scm.com/)
        - Git was used for version control. I used the Git terminal when I wanted to add and commit my changes and ultimately push them to GitHub
    9. [GitHub](https://github.com/)
        -GitHub is where code pushed from the terminal is stored.
    10. [Balsamiq](https://balsamiq.com/wireframes/)
        - I used balsamiq to create all the wireframes which you can find in the wireframes directory
    11. [Stripe](https://stripe.com/en-ie)
        - I used Stripe to help with the payment handling on the site

# Testing 

- Testing User Stories from the User Experience Section
    - First Time Visitor Goals

    1. As a first time visitor of the site I want to be able to know what the purpose of the site is and learn more about what it is they do
        - When a user lands on the site they are met with an attractive hero image. On desktop they see the full nav bar with all the options which are open to them and a short piece of text in the middle of the page which tells them about the community aspect of the site. This is hidden on mobile, however on both viewport sizes the user sees a banner on the bottom of the screen telling them to scroll.
        - Upon scrolling the user can learn more about the various goals of the site including coaching and the membership portion of the site
        - User are prompted to login/ register on the main home page which immediately suggests to them that they can make a profile on the site. 
        - When the user scrolls and looks at the other two sections on the home page they can see large call to action buttons directing them to the products page

    2. I want to be able to navigate around the site with ease
        - To test this I loaded the home page and clicked all the links to ensure they lead to where they were supposed to. While doing this I found several minor bugs. I found that the registration page needed some margin at bottom of the button so that it wasn't pressed up against the footer. I also noticed that there was no home button on this page. Furthermore, I rememebered that the links to social media in my footer section did not actually go anywhere because this is a fictional brand so I just made them open the specified site in a new tab
    3. I want to be able to decide if I want to purchase anything from the site quickly, and if so I want the checkout process to be as easy as possible.
        - If a user wants to purchase a product from the site I decided that they must be logged in. Given the nature of the products, anonymous purchases don't really make sense, because either the user is going to need their profile to access the membership site or else they are going to be signing up for coaching, in which case I will need the same information. However, when a user tries to click on the product they want to purchase they are instructed that they will need to login, which I feel is a bit clunky. To overcome this I added some text to the products page which stated that for the site to provide the best UX that the user must be logged-in to make a purchase. And I also included a toast which says the same thing. While I admit this isn't the perfect solution, it does give the user more of a heads up that they will have to have an account to make purchases without forcing them to make an account immediately when they first land on the site.
    4. I want everything on the site to look well no matter what device I am using
        - To test this I first navigated through all portions of the site on my monitor, which is would be above the extra large breakpoint on Bootstrap. Next, I viewed the site on the large and medium breakpoints. At this breakpoint the home page loses two images and becomes more text focused. I also found that at this size, the register page needed to have margin added so that the content was not directly next to the footer. Finally, on mobile I noticed that on very small viewports such as the IPhone 5, the forum page was very tight with a pixel of the text on the right being hidden by the 'overflow x: hidden' property. To fix this, instead of making the the columns equal sizes, I made the middle column slightly smaller than the other two. 
    
    - Returning Visitor Goals

    1. As a returning visitor of the site I want to be able to register for an account with ease if that is what I choose to do
        - To test this I simply clicked on the register button and attempted to register for an account. I used spaces for the various fields and attempted to leave fields blank in an effort to 'break' the form however the validation all seemed to be working correctly
    2. I want to then be able to log in quickly
        - Upon navigating to the site the login in button is very clear on the home page. It is actually the main call to action upon landing on the site. The login form only contains two fields, the username and the password, making this form also quite quick and painless.
    3. If I decide to purchase membership on the site I want to be able to checkout without spending much time and effort on it
        - When purchasing memebership firstly the user has to logged in, as I've discussed already. Assuming they've made it past the account registration and login procedure, they now navigate to the products page and click on the membership site 'purchase now' button. Following this, they are redirected to the product checkout page in which all they have to do is enter some basic billing information and they are immediately granted access to the forum. An interesting point to mention here, but will be discussed in more detail later is that the membership site product IDs are different in the development and production database, so for testing this made things a little bit awkward. Also there was a bug on this page, where the checkout form was being posted on page load. I discuss solving this bug later in the bugs section.
            - Another interesting bug I found during this portion of testing was that if a user purchased a product after purchasing membership, then their membership was being revoked. The fix for this is discussed later in the bugs section
    4. I want to be able to browse the forum and search for things that interest me specifically.
        - Here I tested the pagination, search, and filtration features of the forum page. By default the user is shown the posts from newest to oldest, with 3 posts being shown per page. This was to prevent long periods of scrolling for the user, and allows them simply to flick through the pages quickly. To test the search feature, I simply typed various keywords into the search bar and ensured that the necessary results were shown. If there was no search criterea entered, an error message was shown to the user, if no searches matched the entered search, then the user was shown an empty page and prompted to make a post about the topic. Finally, to test the categorisation feature, I simply clicked on the various categories and ensured that the correct results were being shown which they were!

    - Frequent User Goals

    1. I want to login to the site with as little friction as possible
        - This goal is accomplished by placing the login button as the main feature of the home page. Browswer cacheing also means that if the user didn't log out last time that they should remain logged in.
    2. The forum must have some way of searching through all the posts so I don't have to scroll down through hundreds of posts to find the posts I'm interested in.
        - Pagination, searching and filtration achieve these goals
    3. The main all posts page must have some sort of cut off so that I don't have to scroll for ages to see older posts
        - Pagination was implemented to achieve this goal
    4. Posts should be categorised so I can view posts from certain categories
        - The filtration feature allows the user to do this
    5. I should be able to comment under posts and reply to comments so that a proper discourse can be had
        - To test the comment feature I added several comments to posts and ensured that they displayed in the correct order and that the correct user information was attached to each comment
    6. The content should be moderated to a degree because people in the fitness industry can sometimes have very coarse, inflammatory opinions, so if someone is trying to incite hate, or spread false information I would rather not have to engage with this
        - To combat this, the site is intended to be moderated and posts don't go live until given approval by the admin.

    - Site Owners Goals
    1. To create a buzz and hype around the site and the brand, culminating in high traffic on the site's forum
        - The most effective thing to create buzz and hype would be advertising, however the initial home page of the site with the hero image is quite attractive, and does leave the user with a good impression
    2. To attract new clients for the coaching products
        - Again, this is mainly down to advertising, however general user friendliness of the site will lead to increased purchases and time spent on the site.
    3. To be able to add or remove products to the site
        - To test this feature I logged into the admin account on my development server. When I navigated to the add product page I found that the form was being posted on page load. I will discuss how I solved this bug in the bugs section later!
    4. To be able to moderate the forum and remove posts if they are deliberately spreading misinformation or hateful 
        - To test this I added 2 new posts as a normal user. One which I would accept as the admin and one which I would reject. I logged in as the admin and went to the Forum Admin page. Here I could see the two posts who were made by the other user. When I accepted the post, the post showed up in the community as expected. However, when rejecting a post there was no way to clear the post from the unaccepted posts page. To fix this, I granted the superuser the ability to delete any posts whilst normal users can only delete their own posts
    
- Bugs
    1. The first bug I awkward bug I encountered was when trying to wire up the posts to show on the main forum page. 
        - E1101: Class 'Post' has no objects 'member'.
        - To fix this bug I headed over to stack overflow to see if anyone had a similar issue. As it happened someone suggested to add the line 'objects = models.Manager()' to the Post model and this fixed the issue.
    2. Placeholder text not displaying in my textarea on the post_display.html page.
        - I remembered that I had a text-white class being applied to most of the elements on the page, so adding a text black class to the placeholder text fixed this issue
    3. Having issues with the comments part of the forum. Had to undo three sets of migrations because the data structure isn't correct. Had the ability to post comments but they weren't being linked to the correct posts
        - The fix for this issue was to use Comments.objects.get_or_create() and inserted the data as a tuple. To associate the comment with the correct post I just used the post object which I got using the post's primary key
    4. Adding toasts to the site. So the issue was when I was trying to add toastss to the site, I wasn't seeing them on the page. However, when I inspected them they were in the dom but their opacity was set to 0. Then I realised I was getting a type error, because the .toast function wasn't being recognised
        - The issue was that I had to add the document.ready() function to make sure the page was fully loaded before attempting to use the .toast function
    5. I also had a bug with closing the toast with the x button
        - I was using the data-dismiss class instead of the data-bs-dismiss class. Changing the class fixed the issue!
    6. I couldn't get conditional formatting of the delete button to work on the forum main page. I was trying to get the delete button to show only if the posts author and the logged in user were the same
        - I realised that the author was coming back as a string and the user was coming back as an object. Therefore, the data types weren't equal. The fix for this actually involved me removing Author from my models altogether and associating posts with the user profiles themselves instead of the author table which I had initially created
    7. Getting an issue with categories after i added pagination. The bug was that it was showing all posts if any were in that category
        - I realised the view was using the page variable because I added pagination. Changing the references from post to page in the view fixed the issue!
    8. Bug - Getting an issue if I show all in categories I lose pagination
        - To fix, instead of redirecting users to a combination of all categories, I simply redirected them to the main forum page
    9. Issue with updating UserProfile is_member field when they purchase membership to the site
        - Testing - To test this issue I firstly added print statements to the checkout success view function.I started by checking that I was printing out the correct value for membership_site.Next I made sure that the conditional statement was checking correctly. Then I added a statement to make sure the profile was being checked correctly. I added a print statement above and below where I changed the memebership status. It turned out that the membership status is being updated but not being saved even though I added a profile.save()
            - To fix this issue I went to the product checkout view, and checked if the user was purchasing membership from the site, if so I updated their membership status there
    10. Related to no. 9, if a user purchased another product after purchasing membership on the site, they lost their membership status / privelleges. 
        - To fix this, I added a conditional statement to check if they were already a member, whilst purchasing another product. If they were, I set the is_member variable to true, if not, I left it as false.
    11. Setting up the approve post form, submitting the form with the approved box unchecked was giving an error. Being passed through as a null value.
        - I ran a check to see if approved is true, if it was true then the post was approved. If it was not true then it had to be false in which case the admin has the choice to delete the post
    12. Another bug relating to post approval, when the approved box was checked I was receiving this error NOT NULL constraint failed: forum_post.user_id. Also this was only an error when the approved box was checked, when the box was unchecked, the form posted correctly.
        - Therefore, when approving a post I had to pass the user from the initial post to the database.
    13. The fix to bug 12 created a new bug in which when a post was given approval by the admin user, a new instance of the post was being created. This isn't an issue, however the issue was that the 'old', unapproved version of the post was also remaining in the database
        - To fix this I had to add the line post.delete(). At this point I debated whether I should delete the post if the admin does not click the approve button, however, I felt that in certain cases the admin may either make a mistake and forget to click it or simply not be sure. Therefore, the unapproved post remains in the database until either the admin approves it, or deletes it through the normal delete post mechanism
    14. I realised that users could 'hack' the system and edit and delete posts that weren't theirs by typing in the URL with the correct post_id followed by edit_post or delete_post
        - To combat this, I went to the edit and delete post views and added a check to see if the logged in user was the user who made the post. I redirected them to the home-page if the condition was not met
    15. This bug was related to my product_checkout view. I left out the parentheses from the is_valid(): method and this part of the code wasn't executing. So the order and checkout forms were being posted correctly, however there was not backend validation. 
        - To fix this, I ended up spending a lot more time than I should have. When trying to use the .save() method I was getting an issue that the product wasn't being passed through. I tried passing the product object through the view to the backend as a hidden field. However, in the end I realised I was still able to use the objects.get_or_create() method *and* check that the form was valid, whereas I was trying to use the .save() method even though there was actually no need to. The form is still being validated and the order is being created correctly now!

# Delpoyment

- Deploying to [Heroku](https://www.heroku.com/)
    - To delpoy the project on Heroku I followed the steps below
        1. I went to [Heroku](https://www.heroku.com/) and created an app. I gave the app a new and chose the eu-west server location
        2. Next, I went to the resources tab and created a new postgres database. I chose the free plan for this database
        3. At this point, I installed dj_database_url and psycopg2-binary. You will find these in the requirements.txt file
        4. I imported dj_database_url into my settings.py file.
        5. I went back to Heroku and went to the config variables, and copied the postgres database url 
        6. In settings.py I commented out the local database and included the new production database
        7. I then ran migrations on the production database by typing 'python3 manage.py migrate'
        8. At this point, I created a new superuser, and manually inputted my categories, and products into the production database
        9. At this point in the deployment I accidentally committed my database url to github for a few hours, so I destroyed that database and repeated steps 2,5,7 and 8 again to connect to the new database and populate it.
        10. I added a statement to check if the app was being run in the development environment, and if so the local db was to be used, if not the production database was used
        11. I then installed gunicorn and froze it into my requirements.txt file
        12. Following this, I created a procfile and added the line
        'web: gunicorn strength_room.wsgi:application' so that heroku would know that it was to create a web dyno. 
        13. At this point, I returned to the heroku dashboard, and set an environment variable 'DISABLE_COLLECTSTATIC'=1
        14. I also added the heroku app name to the allowed hosts in settings.py.
        15. At this stage Heroku was able to build the app and the app was live, however since static files were disabled, there was no styling on the site.
        16. At this point I generated a secret key to add to the heroku config variables
        
- [Amazon Web Services (S3)](https://aws.amazon.com/)
    - I used S3 to host my static and media files. To set everything up I followed the following steps
        1. I set up an account on AWS.
        2. I navigated to s3 and then created a new bucket
        3. I gave the bucket name and selected the region closest to me
        4. I set the bucket privacy to public and created the bucket
        5. I set some generic values for static website hosting
        6. Navigating to the permissions tab I added a CORS configuration which would allow the bucket to communicate with the app, basically granting a few permissions
        7. Then I generated a policy generator to create a bucket policy
        8. I then copied the generated policy into the bucket policy editor, and added a * to the end of the resource to allow access to all resources in the bucket
        9. Finally, I went to the access control list and set the list objects permission to everyone
        10. The next few steps are regarding another AWS service called IAM which stands for Identity and Access Management. Basically, in the next few steps I created a group, an access policy to give this group access to the s3 bucket that I created, and finally I needed to add a user to the group so that they would have access to the s3 bucket.
        11. The first step in this process was navigating to the IAM section of AWS.
        12. I created a new group and then navigated to the policy section
        13. I clicked create policy, navigated to the json tab and then selected 'Import managed policy'.
        14. I imported the S3 full access policy. I then returned to my bucket policy from step 8 and copied the bucket policy ARN and pasted in the resource section of the S3 Full access policy
        15. After clicking next, I was prompted to provide a name and a description for the policy and finally created the policy
        16. Now that the policy was created, the next task was to attach the policy to the group I created in step 12
        17. I did this by navigating to groups, and then clicked on the group created in step 12, clicked on attach policy, selected the policy which I just created and clicked attach policy
        18. The final step was to create a user who would live inside this new group. To do this I clicked on users.
        19. On the next page I clicked add user and then gave the user a username which was relevant to the project and gave them programmatic access
        20. Next, I put the user in the correct group and then clicked create user
        21. Upon completing these steps, I was notified of my success in creating the user and was prompted to download a .csv file containing the relevant information which were going to be sent through to the django app
        22. At this stage I installed boto3 and django-storages
        23. Furthermore I added storages to my installed apps in django and froze the new requirements to my requirements.txt file
        24. At this stage, I started integrating the AWS variables into my settings.py file
        25. I created an if statement to check if 'USE_AWS' was in the environment. I then added this variable to my heroku environment variables after this and set it to true
        26. If 'USE_AWS' was true I wanted to set the rest of my AWS settings so that my app could connect with my bucket
        27. ![Bucket Configuration](/media/bucket-variables.PNG)
        28. The image above shows how I configured the AWS bucket to communicate with the app, and that code only runs if the variable 'USE_AWS' is in the environment
        29. With those settings added, I went to heroku and added the associated variables from the .csv file I downloaded from AWS
        30. I also removed the disable_collectstatic variable to allow django to collect the static files automatically and upload them to S3 
        31. You also may have noticed in the image in step 27, the variable 'AWS_S3_CUSTOM_DOMAIN'. This variable adds the bucket name and adds the amazon url to it so that upload the static files to the correct bucket
        32. At this point I created a file called custom_storages.py which you can find in the project level directory
        33. Here I created custom classes for static files and media files
        34. The final thing I did was to navigate to settings.py and for static and media files, to use the classes I just created.
        35. ![static and media settings](/media/static-and-media.PNG)
        36. The code above is all within the production environment code block.
        37. This code overrides the static and media URLs by setting the custom domain and the new locations for these resources
        38. At this point, I was able to push the code to my heroku master branch. When the app finished building I was able to navigate to my amazon S3 dashboard and see that my static files had been collected
        39. The final steps involved me setting cache control to improve performance for users the site and adding the media files to amazon
        40. To do this, I headed over to my bucket and created a new folder called 'media'. Inside the folder, I uploaded all the images used in my project. I set Manage Public Permissions to 'grant public read access for these objects'. 
        41. When I pushed the code to heroku again my images were all working correctly. 
        42. Finally, I had to set the stripe keys in the heroku environment.
        43. I went to Stripe and in the developers tab I clicked on API keys. I set the publishable key as my 'STRIPE_PUBLIC_KEY' and my secret key as 'STRIPE_SECRET_KEY' in Heroku.
        44. Once I could view the site, I copied the url and returned to stripe. I went to the Developers tab and navigated to the Webhooks section. I clicked on the 'Add Endpoint' button and pasted the URL into the endpoint url input box followed by '/products/wh/'.
        45. I selected the receive all events button and clicked 'Add Endpoint'.
        46. Stripe generated a 'Signing Secret' which I then added to my Heroku config vars.


- Running this Project Locally
    - To run this project locally you will need to follow the steps as laid out.
    - General Steps for Cloning the Project
        1. Download the Google Chrome Browser
        2. Type in GitPod in the extensions section of settings
        3. Install the GitPod Chrome browser extension
        4. Log into GitHub
        5. Navigate to my [GitHub repository](https://github.com/niall-mulcahy/MS4-strength-room)
        6. Click the clone or download button which you can find under the repository name
        7. If you wish to clone with HTTPS copy the link which will being with https://github.com/---
        8. At this stage you should open Git Bash and change the to directory in which you want the cloned project to be made.
        9. Next, you will need to type git clone followed by the link you copied in step 7 into your terminal. 
        10. Press enter to create your local clone of this project
    
    - Specific Steps for MS4-strength-room
        1. Run the command 'pip3 install -r requirements.txt' to install the associated dependencies
        2. At this stage you will have set a few environment variables for the project to work correctly
        ![Development Variables](/media/development-variables.PNG)
        3. In reference to the image above, you will need to create a variable called 'DEVELOPMENT', and set the value to True. This is to direct the setting.py file to use the local database
        4. The 'SECRET_KEY' variable is in reference to the Django Secret Key, [here](https://miniwebtool.com/django-secret-key-generator/) is where I generated my django secret key. 
        5. To setup your stripe environment variables you will need to navigate to [Stripe](https://stripe.com/en-ie) and create an account
        6. Click on the developers tab and click on API keys. The publishable key is your 'STRIPE_PUBLIC_KEY' and your secret key is 'STRIPE_SECRET_KEY'. 
        7. At this stage we will need to get the local database all setup. To do this type 'python3 manage.py makemigrations' followed by 'python3 manage.py migrate'. This will get the database setup with the correct models and data-structure.
        8. Now would be a good time to create a superuser. To do this type 'python3 manage.py createsuperuser'. You will be prompted in the terminal to input username, email and passwords.
        9. To run this project type 'python3 manage.py runserver' into the console.
        10. Once you can view the site, copy the url and return to stripe. Go to the Developers tab and navigate to the Webhooks section. Click on the 'Add Endpoint' button and paste the URL into the endpoint url input box followed by '/products/wh/'.
        11. Select the receive all events button and click 'Add Endpoint'.
        12. Stripe will generate a 'Signing Secret' which you should keep secret and out of version control at all costs!
        13. Return to your environment variables and set the 'STRIPE_WH_SECRET' to your signing secret. This will now allow the product_checkout page on the site to work correctly.

# Credits 

- Media 

    - Hero Image 
        - This image was taken from Pexels, shot by [Victor Freitas](https://www.pexels.com/@victorfreitas)
    - Treadmill Image 
        - This image was taken from Pexels, shot by [William Choquette](https://www.pexels.com/@willpicturethis)
    - Deadlift Image
        - This image was taken from Pixaby by [Revolution Printers](https://pixabay.com/users/revolutionprinters-13267890/)
    - Thumbs Up Emoji 
        - This image was also taken from Pixaby and was by user [Dark Athena](https://pixabay.com/users/darkathena-5167878/)

- Code
    - Forum 
        - I took some inspiration for the forum data structure from a youtube series in which [Selmi Tech](https://www.youtube.com/channel/UCmrvAIpkl1L8WlalusTRlnw) creates a forum app using django. I watched the video series more to get a conceptual understanding of how one would set up their data structure so that users would be associated with the correct posts and that the comments would be associated with the correct user. In terms of actual code, I did not use any of his. 
    - Products
        - I leaned quite heavily on the Boutique Ado lessons throughout the product checkout portion of the site, especially for the stripe checkout portion. The webhooks.py and the webhook_handler.py files have been taken almost exactly from the Boutiqe Ado project. 
    - Setting up AWS
        - When deploying to Heroku and setting up AWS, I followed the method as laid out in the Boutique Ado project quite closely. 
    - Stripe_elements.js
        - I followed the stripe documentation/ boutique ado code for this section of the project.
    - Ensuring the footer remained at the bottom of the page
        - I took code from a [stack overflow](https://stackoverflow.com/questions/4575826/how-to-push-a-footer-to-the-bottom-of-page-when-content-is-short-or-missing) to help me write css to ensure that the footer always remained at the bottom of the screen
    - Creating an overlay for the hero image
        - To make the hero image darker and to make text more visible I added an overlay to sit on top of it. I took the code from a [W3 Schools](https://www.w3schools.com/howto/howto_css_overlay.asp) answer. I removed the display: none property.
    - The User Profile Model
        - I took at lot of the same fields and logic for the user profile model from the boutique ado project. 
    - Updating the delivery information on the profile page
        - I took the idea of being able to update delivery information on the users profile page from boutique ado as well