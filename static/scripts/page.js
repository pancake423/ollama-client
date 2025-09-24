import Component from "component";
import Menu from "menu";

export default class Page extends Component {
  constructor() {
    super({
      type: "div",
      parent: document.body,
      classes: ["page"],
    });

    this.addChild(new Menu("left"));
    this.addChild(new Menu("right"));
  }
}
