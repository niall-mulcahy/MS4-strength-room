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


4. Testing


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