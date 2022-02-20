const mongoose = require("mongoose");

console.log("Starting");

main().catch((err) => console.log(err));

async function main() {
  await mongoose.connect("mongodb://127.0.0.1:27017/test");

  const kittySchema = new mongoose.Schema({ name: String });
  kittySchema.methods.speak = function () {
    return this.name ? "Meow name is " + this.name : "I don't have a name";
  };

  const Kitten = mongoose.model("Kitten", kittySchema);

  const silence = new Kitten({ name: "Silence" });
  silence.save();
  console.log(silence.speak());
}
