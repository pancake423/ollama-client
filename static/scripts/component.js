/*
dynamically building the DOM with javascript is fun

the "proper" way to do it is server-side with a library like React, but for small
projects this hacky solution is more fun!
*/

export default class Component {
  constructor({
    nodeType: type = "div",
    parent = null,
    classes = [],
    contents = "",
  }) {
    // create element and append to parent
    this.domElement = document.createElement(type);
    for (const c of classes) {
      this.domElement.classList.add(c);
    }
    this.domElement.innerHTML = contents;
    // no parent; don't attach to DOM here
    if (parent === null) {
      return;
    }
    if (parent instanceof Component) {
      // auto detect if parent is a Component instead of a vanilla HMTL element
      parent.domElement.appendChild(this.domElement);
    } else {
      parent.appendChild(this.domElement);
    }
  }

  listen({ event, handler, global = false }) {
    const target = global ? window : this.domElement;
    target.addEventListener(event, handler);
  }

  addChild(component) {
    if (component instanceof Component) {
      this.domElement.appendChild(component.domElement);
    } else {
      this.domElement.appendChild(component);
    }
  }
}
