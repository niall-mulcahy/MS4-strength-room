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
    - Content
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
        - Again, this is mainly down to advertising, however general user friendliness of the site will lead to increased purchases.
    3. To be able to add or remove products to the site
        - To test this feature I logged into the admin account on my development server. When I navigated to the add product page I found that the form was being posted on page load. I will discuss how I solved this bug in the bugs section later!
    4. To be able to moderate the forum and remove posts if they are deliberately spreading misinformation 
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
    15. 