async function main() {
  // Authorization token that must have been created previously. See: https://developer.spotify.com/documentation/web-api/concepts/authorization
  const token = 'BQDHL-uMk8CdgNB2ocG4NvNz6_-HM4YyPUXoYlWluYL_p0T2VzPmvFeqFJUtU8RfyAymm0wj3QSrhsOQV8L5mLNunxgfBnBnoe1lWwsZnSLC8iTAsjboHTJfLWP7yB2jMbWcecSUIxCCodyHWPns8MMTTyhqmGXxqCY4JSWLQtHo1nCbvQPwsGA2D0LsmgoiN-DH3p38xnOmDNRBzoQIhie5N8V4AQbjlSU14D8iHFblM9MtUj4grFuKg4b9XRtnOrTh';
  
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
