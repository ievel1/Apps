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

const tracksUri = [
  'spotify:track:7IoV5eGR85wUOXjninlmNu',
  'spotify:track:7d9212orrSfVHQaSdesffl',
  'spotify:track:5YXJd8EchmByYBuxLNEjZC',
  'spotify:track:1DylljLs4Ofw3l5QuhxoJG',
  'spotify:track:5Rdh332wRhjgmrqhwFJXAQ',
  'spotify:track:2eLDUK7EkpENZkDL9O5yhz',
  'spotify:track:2IGMVunIBsBLtEQyoI1Mu7',
  'spotify:track:3C9ABxT2MTpkMXgU11BuRZ',
  'spotify:track:2TVmMYAYOxxu7Ud4kXikGX',
  'spotify:track:7avreNC8Af4ifQDk8CGJOz',
];

async function createPlaylist(tracksUri) {
  const { id: user_id } = await fetchWebApi('v1/me', 'GET');

  const playlist = await fetchWebApi('v1/users/${user_id}/playlists', 'POST', {
    name: 'My recommendation playlist',
    description: 'Playlist created by the tutorial on developer.spotify.com',
    public: false,
  });

  await fetchWebApi('v1/playlists/${playlist.id}/tracks?uris=${tracksUri.join(",")}', 'POST');

  return playlist;
}

async function main() {
  const createdPlaylist = await createPlaylist(tracksUri);
  console.log(createdPlaylist.name, createdPlaylist.id);
}

main(); // Call the async function
