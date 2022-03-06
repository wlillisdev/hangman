# HANGMAN

- You play game here [here](https://hangman-wl.herokuapp.com/)..

![Hangman](images_readme/multi_screen_home.png)


# Aim of Game

The goal of this Game is to create an interactive word game that is both fun a challenging for the user. It has will be programmed entirely in Python and run on Code Institute Huroko app. I picked hangman as it a popular word game that i enjoyed playing as a child with just pen and paper. If you are not familiar with the game check it out here [find out more](https://en.wikipedia.org/wiki/Hangman_(game)) I have put a modern twist on an old game by using python code. Word games are loved all over the world by both kids and adults and have and have shown to have a number of great benefits for the user [find out more](https://www.wordunscramble.io/articles/benefits-of-playing-word-games) It is also a cool way for a developer or even a full stack student to relax and enjoy a few word games in-between dealing with coding challenges.


# How to Play
  - The aim of the game is to guess the hidden word that is generated at random by the game
  - The word will be shown the the user  with _ _ _ _ _ to show user how many letters are in the word
  - The user will have 7 tries or lives to guess the hidden word.
  - After each guess the user will get feed back weather they have guessed correctly or incorrectly. If they have guessed correctly the the letter will be revaled in the hidden word A P _ _ E
  - If user guesses incorrectly they will be notified of incorrect guess and they will lose a life. They will also get a visual representaiton of a hangman image been built for every life lost
  - Game is over when either all the users lives have gone or if the user correctly guesses the word

 ![Game displaying,SecrteLives,Guesses,Words Guessed,Hangman Visual](images_readme/how_to_play.png) 


# User Stories
  The target audience for this game is both adults and kids as both demopgrhics enjoy word games, I tried to strike a balance between fun and engaging and also challenging to the user.
  - As a  user, I want to quickly and easily navigate the game.
  - As a user, I want to know the rules of the game.
  - As a user, i want the game to be fun and easy to play.
  - As a user, i want the game to be challenging.


# Features 

 __Start Screen__
 - The user is initially greeted by an bold hangman graphic in yellow.This Asci Art banner was created at [Asci banner](https://manytools.org/hacker-tools/ascii-banner/) A typewrite effect was added to keep user engaged, it gives a brief message there can only be one winner, and asks the user for their name. 
  
    ![Strat Screen Hangman](images_readme/start_screen.png)

  - The user enters name and is greeted with some more text also in type writer effect, this was added to create engagement with the user and makes them feel part of the game it’s also a bit of fun.

    ![Text After Input](images_readme/text_after_name-input.png)
  
  - The user must enter a valid name, error handling is put in place to ensure they do, they will be notified if not valid input.

    ![Error Not Valid Input](images_readme/error_input_name.png)


__Game Menu__
 
  - After the start up screen The terminal is cleared and the player is brought to the main menu of the game. The palyer has 3 options to chose from.1.Hangman Rules 2.Start Game 3.Exit Game

      ![Main Menu](images_readme/menu_hangman.png)

  - The Hangman Rules section outlines the rules of the game, this text is delivered in a type writer effect to amke it more engaging to the user.

     ![Hangman Rules](images_readme/hangman_rules.png)

  - The Exit Game option will allow the user to completely terminate the game

      ![Exit Game](images_readme/exit_game.png)

  - Error handling menu,The user will be notified of an invalid selection on the menu screen

      ![Error Handling Menu](images_readme/errors_handling_menu.png)

  - Error handling hangman rules.The user will be notified of an invalid selection on the hangman rules section

      ![Error Handling Menu](images_readme/error_handling_instructions.png)


__Main Game__

  - At game start screen, the user is greeted with a bright game interface. It displays the current users lives, What letters he has guessed, (current nothing displayed as game has yet to start) What the Hidden word is _ _ _ _  that is randomly selected form a directory of over 400 words.
  The screen also asks the user to guess a letter. I also included asci art in to the lives dictionary to display at the opening screen of the game saying Good Luck.

    ![Main Game Interface](images_readme/start_game.png)

  - Each user guess is recorded in you have used these letters. Every time they guess wrong thy lose a life and the hangman visual builds. The user also gets a message in red telling them that letter is not in the word.

    ![Display Lives & Visual hangman](images_readme/how_to_play.png)

  - When the user guesses a correct letter in the hidden word. the letter is revealed in current word, And get notfied of correct guess in terminal also in green text.

    ![Show Letter in current word when correct](images_readme/correct_guess.png)

  - Clear terminal in between each move was also integrated to improve user experience

  - If the user gets all the letters correct in the current word they win, And message you win will appear.

    ![User Win](images_readme/you_win.png)

  - If the user loses all their lives & the hangman visual will be completed the hangman wins, and the game over message is displayed. The hidden word will also be revealed.

    ![Hangman Wins](images_readme/game_over.png)

  - At the end of each game the user will be given an option to play again or not play again. If the user plays again the terminal is cleared for a new game and a new random word is picked. If the user decides not to play again, they will be brought back to the main menu.
    ![Play Again menu](images_readme/play_again.png)

  
__Error Handling Main Game__

  - If the user enters a guess that is not in the alphabet, an error warning will be returned to the user, invalid character

    ![invalid character](images_readme/invalid_input_main.png)

  - if the user guesses the same character of a previous guess, they will be given a warning, and prompted for another guess. 

    ![same guess](images_readme/invalid_input_main.png)

- When the game is over the user must select either Y or N, if they don’t select this an error message will be displayed. 

      ![restart check](images_readme/error_handling_restart.png)




 

__Fact Generator__

  - This is a fun app that will create a new random interesting  fact every time the user clicks on the button.
  - This is aimed at grabbing a new users attention and helping to encourage  a user to click on a quiz after playing.
  - The button has a hover effect and will change color once clicked.

 ![Fact Generator](assets/readme/new-fact-generator.png)


__Footer__

  - The footer is simple and clean design it is the same on all pages of the website.
  - It contains 3 social media platforms as requested by Quizz Master they will also open in a new window to allow easy navigation for the user.
  - The main aim of the footer is to increase engagement with visitors.With the goal of getting the user to subscribe to the channel in order to get updates on new quizzes. 

 ![Footer Bar](assets/readme/footer.png)

- __Hoover__

  - Each clickable element on the website changes color when hovered over with a mouse. This is to encourage users to click on buttons and links and increase engagement and user experience.
  

__Quizzes Page__

  -  This page clearly lays out the main quiz topics. The user can easily navigate to the diffrent quizzes.
  - Each specific quiz category has an eye catching image in relation to the different topics. Each topic has a button type icon in the centre of it that also has a hover effect to improve the users experience.
  - At the bottom of the page there is an interactive google map. The map has various markers at locations all around the world.
  - When the user clicks on the marker a info window appears and the users can view an interesting fact from this location.
  - This is aimed at improving  the users engagement  on the site. As all quiz lovers enjoys interesting  facts and information this map will cater for this need and provide some fun for the user as they take a break between quizzes.
  
  - Quizzes Page
 ![Quizz Featuer](assets/readme/quizzes-featuers.png)

 - Quizzes Page Google Map Feature
 ![Map Quizzes Featuer](assets/readme/map-quizzes.png)

  [View Quizzes Page Featuers](https://wlillisdev.github.io/quiz-master/quizzes.html)


__Quiz Page__

  -  The quiz page is the same format on all quizzes, 5 questions with a multiple choice of 3 answers per question.The user answer is easily and quickly recorder in a radio input.

  - Quiz Page
 ![Quizz Featuer](assets/readme/quizz-page.png)

  - The user has to answer all questions for the quiz to be successful. If they don't they will be given an alert saying you have missed a question.

  - Alert warning
 ![Quizz Featuer](assets/readme/alert-quizz.png)

  - At the end of the quiz the user presses get results  button, And a message tells them how many questions they have got correct.
  - The results is also accompanied with a GIF image, there a 3 different  images that relate to different  score ranges.
  - GIF for All Correct
  ![Quiz Results](assets/readme/quizz-full-marks.png)
  - The answers to the questions are also revealed  once the user has submitted at the end of the quiz.  
  
  [View Quiz Page Featuers](https://wlillisdev.github.io/quiz-master/quizz-triva.html)



__Contact Us Page__

 [View Contact Us Featuers](https://wlillisdev.github.io/quiz-master/contact-us.html)

  - It has a simple but elegant contact us form layout. That captures enough information so Quiz Master can follow up on the lead. And allows a user’s to quickly fill out the form with minimal information.
  - It also has a video background of question marks. It continues the animation theme and quesion mark logo from the home page it is fun and interesting.
 
 ![Contact Us Form](assets/readme/contact-us.png)

__Thank You Page__
  - When the user successfully submits the contact us form, they will be brought to a thank you page. Which will also encourage the user to check out our social channels.
  ![Thank You Page](assets/readme/thank-you.png)

# Design
 - Theme
   - The Theme of the website was to build a bright and engaging Quiz website with a blend of both quizzes and fun. 
   - Fonts were imported from google fonts, Boogaloo was used for the logo and nav menu, Libre Franklin for hompage hero text, Montserrat for headings, and Roboto for body text.These were picked as they were crisp and complimented each other and the theme of the site.

 - Color Palette
   - The color palette is made up of four main colors which creates a good contrast and helps support the overall theme.

 ![Color Palette](assets/readme/color-pallet.png)

- Imagery
   - The images that were selected for the website were bold and bright images related to the Quiz Genre.

- Wireframes
   - To create the initial layout and wireframe I used Balsamiq. This helped fine tune the design and layout. It also helped in calculating the amount of content and images required.

  - ![Homepage Wireframe Concept](assets/readme/home-wireframe.png)
  - [Quizzes Page Wireframe Concept](assets/readme/quizzes-wireframe-new.png)
  - [Quizz Page Wireframe Concept](assets/readme/quizz-wireframe.png)
   

# Future Development

- Difficulty Levels
  - There will be 3 difficulty levels, Easy, Medium & Hard, Hard will have 4 lives, Medium 7 lives and easy 10 lives. This will make the game more challenging

- Leader Board
  - The game will have a points system the user will earn point for correct guesses at the end of the game the users score will be uploaded in to a high scores screen.        

- Word Themes 
  - Currently all the words are just random words, it would be interesting if the user could select a theme and the words were directly related to that, for example movies


# Testing

### Validator Testing 

 - HTML Validator
   - [W3C](https://validator.w3.org/) site was used to validate the **HTML** code.
   - A number of small errors were initially flagged up. Some duplicate tags were removed and I also had to rename a number of images. I also misplaced a link tag in the homepage, as I copied this page structure for the rest of the site i had to fix it on all of these pages also
     - [Erros From Validator Hompage](assets/readme/html-home-error.png)
     - [Erros From Validator Quizzes](assets/readme/error-validator-quizzes.png)
     - [Erros From Validator Triva Quiz](assets/readme/validaor-error-triva-quiz.png)

   

 ### All Pages are now error free see links below:

 ![Home Page](assets/readme/homepage-pass-validator.png)
   - [Homepage](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwlillisdev.github.io%2Fquiz-master%2Findex.html)
   - [Quizzes Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwlillisdev.github.io%2Fquiz-master%2Fquizzes.html)
   - [Triva Quizz](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwlillisdev.github.io%2Fquiz-master%2Fquizz-triva.html) Error because image is hidden until event happens
   - [Sport Quizz](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwlillisdev.github.io%2Fquiz-master%2Fsport-quizz.html) Error because image is hidden until event happens
   - [Film Quizz](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwlillisdev.github.io%2Fquiz-master%2Ffilm-quizz.html) Error because image is hidden until event happens
   - [Film Quizz](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwlillisdev.github.io%2Fquiz-master%2Fmusic-quizz.html) Error because image is hidden until event happens
   - [Contact Us Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwlillisdev.github.io%2Fquiz-master%2Fcontact-us.html)
   - [Thank You Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwlillisdev.github.io%2Fquiz-master%2Fthank-you.html)

## CSS Validator
  - The [W3C](https://validator.w3.org/) was used to validate the **CSS** code
  - The website passed with no errors

  ![CSS Pass](assets/readme/css-pass-validator.png)

  ### See links below for Results:

   - [CSS Test Results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fwlillisdev.github.io%2Fquiz-master%2Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

 
## Lighthouse
 - Lighthouse testing was carried out in Developer Tools in Chrome. Initially it gave a number of improvements and flagged up a number of images that needed to be reduced in size. Which was done.

 - The results were also skewed as the chrome extensions on my testing device was affecting the lighthouse results. The tests of all pages were redone in a incognito window and performance score increased.

 ![Hompage](assets/readme/lighthouse-homepage-crop.png)
 - [Quizzes Page lighthouse results](assets/readme/quizzes-pages-lighthouse.png) results are slightly down mainly due to the integration  of google maps api.
 - [Contact Us lighthoust results](assets/readme/contact-lighthouse-crop.png)

 ## JavaScript
 - The [JShint](https://jshint.com/) was used to validate the **JavaScrip** code
 - The results initally highlighted a few warnings.
     - [Erros From JShint](assets/readme/jshint-error.png)
     
 - Each item was addressed, The validation loop for the quizz was edited to remove eval as Jshint highlighted it could be harmful for security issues. And stack overflow suggested adding / /*jshint esversion: 6 */ to the notes this prevented this error.

 ![JShint Scan Pass](assets/readme/jshint-scan-pass.png)
 
## Manual Testing
  - All the site links were manually tested to see if they all worked ok and linked to the correct locations.
  - The form was checked that name and email were required, that the radio buttons functioned and that the submit button worked.
  - The site was further tested using feedback from mentor,family and friends who checked it on different  devices they had.
  - All of the page's features were tested on Google Chrome, Microsoft Edge, Mozilla Firefox, Safari, and Opera .
  - Google Chrome's Developer Tool was used to inspect page elements during the build and helped identify  and debug issues within the HTML and CSS.
  - The README.md was checked before final submission and links verified.



# Bugs

  - After running the site through HTML checker, a number of small bugs were identified. Each error was identified and an appropriate solution applied, i went through all pages and fixed any errors. It was good lesson and practice in finding problems with code and fixing them.
  - After Running all the pages through lighthouse, it identified issues with a number of images due to size. Lighthouse suggested to change some larger images which was done.
  - Initially  i had a mouse over event listener  on google maps markers but this was no use for mobile which i realised  when testing, so i changed it to onclick event.
  - I had eval in my validate quiz function, jshint gave this as a warning and a potential security risk so i removed it.
  

  # Unfixed Bugs
  - I am aware there is a console.log Error with Permissions-Policy header: Unrecognized feature: 'interest-cohort'.From what i have researched this is a issue between Github and Google and has no effect on the sites performance.
  - I am aware the website has a lot of large rich images and although images were cropped and compressed it could lead to reduced speed until cached. I have experimented with next gen image formats but currently  they lack browser compatibility  so i just went with png compressed and cropped format for this site.


# Deployment

The site was created using Visual Studio Code and GitHub, and deployed to GitHub pages for testing using the below process:


 - Clicked on my respository for [wlillisdev/quizz-master](https://github.com/wlillisdev/quiz-master).
 - Clicked settings tab and navigated down to "pages"
 - Selected "Main" in branch drop down box.
 - Clicked "save" which produced the live link which can be viewed [here](https://wlillisdev.github.io/quiz-master/).. 

 ## Version Control
  - Git was used as the version control software. Commands such as git add ., git status, git commit and git push were used to add, save, stage and push the code to the GitHub repository.

## Cloning

1. On [GitHub](www.github.com), navigate to the main page of the repository.  [Click Here for Reposititory Link](https://github.com/wlillisdev/quiz-master)

2. Above the list of files, click Code.

3. click Use GitHub CLI, then click the copy icon.

4. Open Git Bash and change the current working directory to the location where you want the cloned directory.

5. Type git clone, and then paste the URL that was copied previously  in step 3.

6. Press Enter to create the local clone.

[git cloning steps with pictuers](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop)


# Credits

- ## Languages

  - [HTML5](https://en.wikipedia.org/wiki/HTML5)
  - [CSS](https://en.wikipedia.org/wiki/CSS)
  - [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

- ## Content
   - The code for the contact us form was taken from the love running tutorial from [Code Institute](https://codeinstitute.net/ie/) and modified.
   - The icons used throughout the site were from [Font Awesome](https://fontawesome.com/)
   - Variour Youtube tutorial were used to help understand flexbox.
   - [Flexbox](https://www.youtube.com/watch?v=fYq5PXgSsbE)
   - Animated Text on home page from [bulldogpatch](https://codepen.io/bulldogpatch-the-sasster/pen/JjoyeGg)
   - Tutorials for Randon Fact generator from freecode camp ,learn web-dev & dev.to were used to inspire the generator.
   - YouTube videos from Eduonix Learning Solutions,Kevin Briggs & Web Dev Simplified were used as a base for the quizz.
   - Youtube videos about google maps api with javascript were followed from Traversy Media & Sam Codes.


    

-  ## Images
   - All images were taken from [Pexels](https://www.pexels.com/)

  
 -  ## Resources
    - [Stack Overflow](https://stackoverflow.com/)
    - [W3Schools](https://www.w3schools.com/)
    - [w3docs](https://www.w3docs.com/)
    - Notes & Videos from course work from [Code Institute](https://codeinstitute.net/ie/)

-  ## Tools
   - [Balsamiq](https://balsamiq.com/) - Used to create wireframes
   - [Google Fonts](https://fonts.google.com/) - Used to import fonts
   - [TinyPNG](https://tinypng.com/) - Used to compress images

-  ## Acknowledgements
 - Special thanks to my mentor Miguel Martinez
 for his help and guidance in the development of my project. Special thanks to my tutor Kasia and our regular class meeting’s and members of the awesome slack community


   # Conclusion
    - I would like to experiment more with javaScript but as i am only getting to grips with the language i kept the concept simple.
    - If I was to build this site again, I would spend more time on the wireframes and know exactly how to structure each section and element before i start.
    - If i had time i would like to add a timer function to the quizz.    
    - I would also learn to make more commits during the project built.

