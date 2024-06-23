import axios from 'axios';

const API_ENDPOINT = 'https://api.edamam.com/api/recipes/v2';
const APP_ID = '41bdfd5d';
const APP_KEY = '6c754439ddf1d4a5875400eb395d8d92';

async function searchRecipes(query) {
  try {
    const params = new URLSearchParams();
    params.append('q', query);
    params.append('app_id', APP_ID);
    params.append('app_key', APP_KEY);
    params.append('type', 'public');

    const response = await axios.get(API_ENDPOINT, { params: params });
    const recipes = response.data.hits;

    console.log('Recipes:', recipes);
    return recipes;
  } catch (error) {
    console.error('Error:', error);
    return [];
  }
}

export default searchRecipes;