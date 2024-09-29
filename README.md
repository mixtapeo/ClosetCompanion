## Instructions
ImageClassification.py: takes in jpeg in a pre-specified folder (./images), runs a ??? model to return tags
app.py: flask webserver running react app
sql.py: has sql POST functions for tag and image

1. install chrome extension (dev mode, load unpacked, and open the extension folder)
2. make a virtual env (<=python 3.10), pip install -r requirements
3. open the root folder in vscode, run app.py
4. run: 
    npm install 
    npm run
5. add images of your wardrobe items to ./images
6. go to uniqlo


## Inspiration
Overspending, and impulse buying clothes and accessories, when much can be done with what you already have.

### Initial Concept Roadmap
![OutfitMaker drawio](https://github.com/user-attachments/assets/61181ed3-1faf-4815-997b-514b4ddf361f)


## What it does
When on a website such as Uniqlo (currently the only supported one), matches one's wardrobe under ./images, and compares it to the current image of a product on screen. If the item on the website is similar enough (determined by a machine learning model), an alert will show up informing you of such. Other features might make it if we have time! such as AI suggested outfits, and tagging showing up on react page.
## How we built it
Using react and tailwind css for the front end, python flask for the backend and 2 machine learning models -> one for tagging, the other for determining similarity of two images. An SQL database of tags and images is also created to link tags to images.

## Challenges we ran into
1. Tailwind css has a learning curve!
2. The first python ML similarity model using euclidian distancing, image flattening and resizing to achieve a similarity ranking. Though, this would function differently in varying situations, being generally unreliable, requiring a new model that used ORB (Oriented FAST and Rotated BRIEF) for feature detection and Brute Force Matcher to compare the descriptors of keypoints in both images to find the best matches.
3. The browser extension was very new to everyone involved, and required a team effort to pull off. We faced problems related to javascripting functions and responses; DOMContent listener would never actually respond in time, or finish, thus decided to implement a 3.2 second timer to call the functions needed for scraping needed data. Finding the data itself was a tough challenge, finding images on a dynamic website like Uniqlo to save, and run comparisons on.
4. As we were all inexperienced in many of the facets of making, coordinating a project, in addition to not knowing much of the technologies such as react developement, ML model training, flask backend, and the extension.

## Accomplishments that we're proud of
Everything; the GUI looking nice, with dynamic tiles updating on the react home page if one drags in an image into ./images. The backend flask server interfacing with the browser extension and responding to calls, running functions and replying to REST requests.

## What we learned
React, tailwind css, teamwork, teambuilding, coordination, ideation, opencv, image matching, working separately on parts of a project to bring it all together.

## What's next for Closet Companion
Add more websites than Uniqlo, use openai API chat embeddings to send images, and recieve combinations of auto-suggested outfits. Currently the react page's "add" section doesn't save the image in to the local folder, which needs to be worked on. In addition, the tags that are created by sql.py can be displayed under the images on the home page, and a search function should help users search large wardrobes for certain pieces.

## Final GUI / UX after 1 day hacking!
![Screenshot 2024-09-29 100147](https://github.com/user-attachments/assets/c56567bf-e7d9-4b79-9612-bace0b25aa4c)

