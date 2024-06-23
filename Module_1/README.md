**Recipe Finder**
================

A simple web application that allows users to search for recipes using the Edamam API.

Youtube Link https://youtu.be/F-GSv4R14xI

**Getting Started**
---------------

### Prerequisites

* A web browser (e.g. Google Chrome, Mozilla Firefox)
* An Edamam API key and ID (sign up for a free account on the Edamam website)

### Installation

1. Clone or download the repository to your local machine.
2. Open the `index.html` file in a web browser.
3. Replace the `APP_ID` and `APP_KEY` variables in the JavaScript code with your own Edamam API credentials.

**Usage**
-----

1. Enter a search query in the input field (e.g. "chicken recipes", "vegan desserts", etc.).
2. Click the "Search" button to retrieve a list of recipes from the Edamam API.
3. Browse through the search results, which include recipe images, labels, sources, and calorie information.

**Technical Details**
-------------------

### API Integration

The Recipe Finder application uses the Edamam API to retrieve recipe data. The API request is made using the `fetch` API, and the response is parsed as JSON.

**Example Code**
```javascript
const url = `https://api.edamam.com/api/recipes/v2?type=public&q=${encodeURIComponent(query)}&app_id=${41bdfd5d}&app_key=${7f2091ec55463781d65b0ddcd451ecac}`;
const response = await fetch(url);
const recipes = await response.json();