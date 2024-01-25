async function main() {
  // Authorization token that must have been created previously. See: https://developer.spotify.com/documentation/web-api/concepts/authorization
  const token = 'BQAfxvfKmsBywwVM3J7dCk3mEnQaLV4rSTlWft61jM22ahRdlstTCfgnNRydyngvKKNJyOn-CbNiGUUjateqcJXtm8lQS-LQ2sBwN035SBplVSfuY6Zxk8RObulECSNz7ysPietR6h_9z4uWe7DM76Iq5FXKZtRBW7YK-hfhvydQ4DrKal_iVN3n5gdzEt5hP1UjL435kmFUpvbyK7mmKh1h9CWPsA9n5pAdieY8cryInsjEhvT8EtrLkXqPVJLRqxP8';
  
  async function fetchWebApi(endpoint, method, body) {
    const res = await fetch(`https://api.spotify.com/${endpoint}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
      method,
      body: JSON.stringify(body),
    });
    return await res.json();
  }
  
  const topTracksIds = [
    '7IoV5eGR85wUOXjninlmNu',
    '5YXJd8EchmByYBuxLNEjZC',
    '5Rdh332wRhjgmrqhwFJXAQ',
    '2IGMVunIBsBLtEQyoI1Mu7',
    '2TVmMYAYOxxu7Ud4kXikGX',
  ];
  
  async function getRecommendations() {
    // Endpoint reference: https://developer.spotify.com/documentation/web-api/reference/get-recommendations
    return (await fetchWebApi(
      `v1/recommendations?limit=5&seed_tracks=${topTracksIds.join(',')}`,
      'GET'
    )).tracks;
  }
  
  const recommendedTracks = await getRecommendations();
  console.log(
    recommendedTracks.map(
      ({ name, artists }) =>
        `${name} by ${artists.map(artist => artist.name).join(', ')}`
    )
  );
}

main(); // Call the async function
