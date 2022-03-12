const mongoose = require("mongoose");

console.log("starting...");

// schema/method
const userSchema = new mongoose.Schema({
  name: String,
  password: String,
  id: String,
});
userSchema.methods.getId = function () {
  return this.id;
};

const User = mongoose.model("User", userSchema);

// run function
writeUser().catch((err) => console.log(err));

// functions

async function getUser() {
  await mongoose.connect("mongodb://127.0.0.1:27017/test?authSource=admin", {
    user: "elia",
    pass: "password",
  });

  User.find({ id: "123" }).exec((err, users) => {
    if (err) throw err;
    console.log(users);
  });
}

async function writeUser() {
  await mongoose.connect("mongodb://127.0.0.1:27017/test?authSource=admin", {
    user: "elia",
    pass: "password",
  });

  const elia = new User({ name: "Elia", password: "password", id: "12223" });

  console.log(elia.getId());

  elia.save();
}
