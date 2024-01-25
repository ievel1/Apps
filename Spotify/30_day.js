// Authorization token that must have been created previously. See : https://developer.spotify.com/documentation/web-api/concepts/authorization
const token = 'BQB0eXzch_7LzTBByksA9QJLL1FgIWMd0BbvJ0d7nMQ3O2NrptqyJzyCv0RT-1xl1GXpagCy-28B0fIWaG1KFOJYuYqFXbugr6ujpmusORtnpCtSv2InDW4LQW4sxUlkrpdNbLHViWD-KBhcjF8wxO91bWgLPMhCBp0nWrAjB_BK0hThArpi5Q0ITIM8GfOuypvo1i9vC6qb1Jep1bHYCtnVoSLkdruBWZuRKVQorVRAlUd1pFmdhNPKOLZuxibAumr_';

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
