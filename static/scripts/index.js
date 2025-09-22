import Page from "page";
import { apiFetchStream } from "stream";

window.apiFetchStream = apiFetchStream;

window.onload = () => {
  new Page();
};
