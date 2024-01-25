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
