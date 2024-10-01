// Async function to fetch and process user data
async function processUserData(userId) {
  try {
    const response = await fetch(`https://api.example.com/users/${userId}`);
    const userData = await response.json();

    if (!userData) {
      throw new Error('User not found');
    }

    const { name, email, preferences } = userData;
    
    // Process user preferences
    const settings = preferences.reduce((acc, pref) => {
      acc[pref.key] = pref.value;
      return acc;
    }, {});

    console.log(`Processing data for ${name} (${email})`);

    return {
      id: userId,
      name,
      email,
      settings,
      lastUpdated: new Date().toISOString()
    };
  } catch (error) {
    console.error(`Error processing user ${userId}:`, error.message);
    return null;
  }
}

// Example usage
const userId = 12345;
processUserData(userId).then(result => {
  if (result) {
    console.log('Processed user data:', result);
  } else {
    console.log('Failed to process user data');
  }
});