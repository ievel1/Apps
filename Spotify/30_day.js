// Authorization token that must have been created previously. See : https://developer.spotify.com/documentation/web-api/concepts/authorization
const token = 'BQDHL-uMk8CdgNB2ocG4NvNz6_-HM4YyPUXoYlWluYL_p0T2VzPmvFeqFJUtU8RfyAymm0wj3QSrhsOQV8L5mLNunxgfBnBnoe1lWwsZnSLC8iTAsjboHTJfLWP7yB2jMbWcecSUIxCCodyHWPns8MMTTyhqmGXxqCY4JSWLQtHo1nCbvQPwsGA2D0LsmgoiN-DH3p38xnOmDNRBzoQIhie5N8V4AQbjlSU14D8iHFblM9MtUj4grFuKg4b9XRtnOrTh';

async function fetchWebApi(endpoint, method, body) {
  const res = await fetch(`https://api.spotify.com/${endpoint}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    method,
    body: JSON.stringify(body)
  });
  return await res.json();
}

async function getTopTracks() {
  // Endpoint reference : https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks
  return (await fetchWebApi(
    'v1/me/top/tracks?time_range=short_term&limit=10', 'GET'
  )).items;
}

async function main() {
  const topTracks = await getTopTracks();
  console.log(
    topTracks?.map(
      ({ name, artists }) =>
        `${name} by ${artists.map(artist => artist.name).join(', ')}`
    )
  );
}

main(); // Call the async function
