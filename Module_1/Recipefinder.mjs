// recipeFinder.mjs

// Import the required libraries
import axios from 'axios';

// Set the API endpoint and API key
const API_ENDPOINT = 'https://api.edamam.com/api/recipes/v2';
const APP_ID = '41bdfd5d';
const APP_KEY = '6c754439ddf1d4a5875400eb395d8d92';

// Function to search for recipes
async function searchRecipes(query) {
  try {
    // Set the API request parameters
    const params = {
      q: query,
      app_id: APP_ID,
      app_key: APP_KEY,
      type: 'public' // Search public recipes
    };

    // Make the API request
    const response = await axios.get(API_ENDPOINT, { params });

    // Extract the recipe results
    const recipes = response.data.hits;

    // Return the recipe results
    return recipes;
  } catch (error) {
    console.error(error);
    return [];
  }
}

// Export the searchRecipes function
export default searchRecipes;