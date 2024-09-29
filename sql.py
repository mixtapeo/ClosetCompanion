import sqlite3
import os

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('image_tags.db')
c = conn.cursor()

def preflight():
    """
    Making sure tables exist.
    """

    # Create Images table
    c.execute('''
    CREATE TABLE IF NOT EXISTS Images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        path TEXT NOT NULL
    )
    ''')

    # Create Tags table
    c.execute('''
    CREATE TABLE IF NOT EXISTS Tags (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tag TEXT UNIQUE NOT NULL
    )
    ''')

    # Create Image_Tag table (to associate images with tags)
    c.execute('''
    CREATE TABLE IF NOT EXISTS Image_Tag (
        image_id INTEGER,
        tag_id INTEGER,
        FOREIGN KEY (image_id) REFERENCES Images(id),
        FOREIGN KEY (tag_id) REFERENCES Tags(id),
        PRIMARY KEY (image_id, tag_id)
    )
    ''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

preflight()

def add_image(name, path):
    conn = sqlite3.connect('image_tags.db')
    c = conn.cursor()
    
    # Insert the image (if it doesn't already exist)
    c.execute('''
        INSERT OR IGNORE INTO Images (name, path) 
        VALUES (?, ?)
    ''', (name, path))
    
    # Get the image ID (since INSERT OR IGNORE won't give it directly)
    c.execute('SELECT id FROM Images WHERE name = ? AND path = ?', (name, path))
    image_id = c.fetchone()[0]
    
    conn.commit()
    conn.close()
    return image_id  # Return the image ID for future linking

def add_tag(tag):
    conn = sqlite3.connect('image_tags.db')
    c = conn.cursor()
    
    # Insert the tag (if it doesn't already exist)
    c.execute('''
        INSERT OR IGNORE INTO Tags (tag)
        VALUES (?)
    ''', (tag,))
    
    # Get the tag ID
    c.execute('SELECT id FROM Tags WHERE tag = ?', (tag,))
    tag_id = c.fetchone()[0]
    
    conn.commit()
    conn.close()
    return tag_id  # Return the tag ID for future linking

def link_image_tag(image_id, tag_id):
    conn = sqlite3.connect('image_tags.db')
    c = conn.cursor()
    
    # Insert the link between image and tag
    c.execute('''
        INSERT OR IGNORE INTO Image_Tag (image_id, tag_id)
        VALUES (?, ?)
    ''', (image_id, tag_id))
    
    conn.commit()
    conn.close()

def add_image(name, path):
    conn = sqlite3.connect('image_tags.db')
    c = conn.cursor()
    
    # Insert the image (if it doesn't already exist)
    c.execute('''
        INSERT OR IGNORE INTO Images (name, path) 
        VALUES (?, ?)
    ''', (name, path))
    
    # Get the image ID (since INSERT OR IGNORE won't give it directly)
    c.execute('SELECT id FROM Images WHERE name = ? AND path = ?', (name, path))
    image_id = c.fetchone()[0]
    
    conn.commit()
    conn.close()
    return image_id  # Return the image ID for future linking

def add_tag(tag):
    conn = sqlite3.connect('image_tags.db')
    c = conn.cursor()
    
    # Insert the tag (if it doesn't already exist)
    c.execute('''
        INSERT OR IGNORE INTO Tags (tag)
        VALUES (?)
    ''', (tag,))
    
    # Get the tag ID
    c.execute('SELECT id FROM Tags WHERE tag = ?', (tag,))
    tag_id = c.fetchone()[0]
    
    conn.commit()
    conn.close()
    return tag_id  # Return the tag ID for future linking

# Get images from a tag
def get_images_for_tag(tag): 
    try:
        with sqlite3.connect('image_tags.db') as conn:
            c = conn.cursor()
            c.execute(''' 
                SELECT i.name, i.path 
                FROM Images i 
                JOIN Image_Tag it ON i.id = it.image_id 
                JOIN Tags t ON it.tag_id = t.id 
                WHERE t.tag = ? 
            ''', (tag,))
            images = c.fetchall()
        return images
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []
    
def add_tags_to_image(image_name, image_path, tags):
    # Step 1: Add the image and get its ID
    image_id = add_image(image_name, image_path)
    
    # Step 2: Add each tag and link it to the image
    for tag in tags:
        tag_id = add_tag(tag)  # Add the tag to the database (if not already present)
        link_image_tag(image_id, tag_id)  # Link the image and the tag


# # Example Usage
# image_name = "a (1).jpg"
# image_path = f"{os.getcwd()}\\{image_name}"
# tags = ["sunset", "beach", "vacation"]

# add_tags_to_image(image_name, image_path, tags)