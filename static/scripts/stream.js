// utilities for interacting with ollama's API

export const API_ENDPOINT = "http://localhost:11434/api/";

function defaultErrorHandler(err) {
  console.log(err);
}

function defaultChunkHandler(chunk) {
  if (chunk.done) return;
  console.log(chunk.value);
}

/*
Fetch from an API streaming endpoint.

url is appended onto API_ENDPOINT
chunkCallback is called whenever a chunk is recieved from the API.
errorCallback is called if we fail for any reason, so it could recieve a wide variety of inputs.
method is the HTTP method to use.
body is the request body
*/
export function apiFetchStream({
  url,
  chunkCallback = defaultChunkHandler,
  errorCallback = defaultErrorHandler,
  method = "GET",
  body,
}) {
  const options = { method: method };
  if (body) {
    options.body = JSON.stringify(body);
  }
  const decoder = new TextDecoder("utf-8");
  fetch(API_ENDPOINT + url, options)
    .then((res) => {
      if (!res.ok) {
        errorCallback(res);
      }
      const reader = res.body.getReader();
      const chunkRecieved = (data) => {
        chunkCallback({
          done: data.done,
          value: data.done ? null : JSON.parse(decoder.decode(data.value)),
        });
        if (!data.done) reader.read().then(chunkRecieved).catch(errorCallback);
      };
      reader.read().then(chunkRecieved).catch(errorCallback);
    })
    .catch(errorCallback);
}
