import Component from "component";

export default class Menu extends Component {
  constructor(alignClass = "left") {
    super({ classes: ["menu", alignClass] });
    this.itemsContainer = new Component({
      parent: this,
      classes: ["menu-items-container"],
    });
    this.controlsContainer = new Component({
      parent: this,
      classes: ["menu-controls-container"],
    });
    // TODO: add buttons to menu controls
  }
}
